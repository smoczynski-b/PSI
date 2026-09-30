#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import json

from access_steward_runtime import (
    AccessStewardRuntime,
    CostVector,
    TelemetryQuery,
)
from durable_shared_memory import JSONLWAL
from memory_archive_runtime import ArchiveCorruption, ArchiveError, MemoryArchiveRuntime
from servant_runtime import ServantCommand


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


class UsageArchiveError(ArchiveError):
    pass


@dataclass(frozen=True)
class ArchiveUsageRef:
    usage_id: str
    version_id: str
    movement_request_id: str
    session_id: str
    map_from: str
    map_to: str
    telemetry_class: str
    movement_digest: str
    actual_cost: CostVector
    policy_version: str
    created_at: str

    def __post_init__(self):
        for field in (
            "usage_id",
            "version_id",
            "movement_request_id",
            "session_id",
            "map_from",
            "map_to",
            "telemetry_class",
            "movement_digest",
            "policy_version",
            "created_at",
        ):
            value = str(getattr(self, field)).strip()
            if not value:
                raise ValueError(f"{field} is required")
            object.__setattr__(self, field, value)
        if self.telemetry_class not in {"T0_SESSION_LOCAL", "T1_SECURITY_RESTRICTED", "T2_AUDIT_DURABLE"}:
            raise ValueError("usage detail must reference a non-aggregated telemetry class")
        if not isinstance(self.actual_cost, CostVector):
            raise TypeError("actual_cost must be CostVector")

    def as_dict(self) -> dict:
        return {
            "usage_id": self.usage_id,
            "version_id": self.version_id,
            "movement_request_id": self.movement_request_id,
            "session_id": self.session_id,
            "map_from": self.map_from,
            "map_to": self.map_to,
            "telemetry_class": self.telemetry_class,
            "movement_digest": self.movement_digest,
            "actual_cost": self.actual_cost.as_dict(),
            "policy_version": self.policy_version,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, row: dict) -> "ArchiveUsageRef":
        return cls(
            usage_id=row["usage_id"],
            version_id=row["version_id"],
            movement_request_id=row["movement_request_id"],
            session_id=row["session_id"],
            map_from=row["map_from"],
            map_to=row["map_to"],
            telemetry_class=row["telemetry_class"],
            movement_digest=row["movement_digest"],
            actual_cost=CostVector(**row["actual_cost"]),
            policy_version=row["policy_version"],
            created_at=row["created_at"],
        )


class UsageChronicle:
    """Restricted L2 journal. It stores typed references, not copied movement records."""

    def __init__(self, path: str | Path):
        self.wal = JSONLWAL(path)

    def append(self, usage: ArchiveUsageRef) -> None:
        payload = {"usage": usage.as_dict(), "usage_digest": _digest(usage.as_dict())}
        self.wal.append("ARCHIVE_USAGE", usage.usage_id, payload)

    def records(self):
        return self.wal.read_valid_prefix().records


class MemoryArchiveUsageRuntime:
    """F3.2 L2 bridge between archive versions and ACCESS_STEWARD movement telemetry.

    The runtime stores only a minimal typed usage binding plus a digest of the
    original movement record. Restricted telemetry remains in ACCESS_STEWARD;
    detailed archive reads re-run VIEW_TELEMETRY authorization. T3 reads expose
    only aggregate usage counts/cost and never session identifiers.
    """

    def __init__(
        self,
        archive: MemoryArchiveRuntime,
        steward: AccessStewardRuntime,
        chronicle_path: str | Path,
        *,
        runbook_id: str = "CURATOR-ARCHIVE-01",
    ):
        if archive.servant.durable is not steward.servant.durable:
            raise ValueError("archive and ACCESS_STEWARD must share authoritative durable memory")
        self.archive = archive
        self.steward = steward
        self.chronicle = UsageChronicle(chronicle_path)
        self.runbook_id = str(runbook_id).strip()
        if not self.runbook_id:
            raise ValueError("runbook_id is required")
        self._usage: dict[str, ArchiveUsageRef] = {}
        self._load()

    def _movement_payload(self, request_id: str) -> dict:
        rid = str(request_id).strip()
        rows = [
            dict(record.get("payload", {}))
            for record in self.steward.chronicle.records()
            if record.get("kind") == "ACCESS_MOVEMENT"
            and str(record.get("payload", {}).get("request_id", "")) == rid
        ]
        if len(rows) != 1:
            raise UsageArchiveError(f"movement reference must resolve exactly once: {rid}")
        return rows[0]

    def _validate_usage(self, usage: ArchiveUsageRef) -> None:
        manifest = self.archive.manifest(usage.version_id)
        if manifest.object_id != usage.map_to:
            raise UsageArchiveError(
                f"archive version/map mismatch: {usage.version_id} names {manifest.object_id}, movement enters {usage.map_to}"
            )
        movement = self._movement_payload(usage.movement_request_id)
        if _digest(movement) != usage.movement_digest:
            raise ArchiveCorruption(f"movement digest mismatch: {usage.movement_request_id}")
        if str(movement.get("session_id", "")) != usage.session_id:
            raise ArchiveCorruption("usage session does not match movement telemetry")
        if str(movement.get("map_from", "")) != usage.map_from or str(movement.get("map_to", "")) != usage.map_to:
            raise ArchiveCorruption("usage route does not match movement telemetry")
        if str(movement.get("telemetry_class", "")) != usage.telemetry_class:
            raise ArchiveCorruption("usage telemetry class does not match movement telemetry")
        if str(movement.get("policy_version", "")) != usage.policy_version:
            raise ArchiveCorruption("usage policy version does not match movement telemetry")
        cost = CostVector(**dict(movement.get("actual_cost", {})))
        if _canon(cost.as_dict()) != _canon(usage.actual_cost.as_dict()):
            raise ArchiveCorruption("usage cost does not match movement telemetry")

    def _load(self) -> None:
        for record in self.chronicle.records():
            if record.get("kind") != "ARCHIVE_USAGE":
                raise ArchiveCorruption(f"unknown L2 usage record kind: {record.get('kind')}")
            payload = dict(record.get("payload", {}))
            usage = ArchiveUsageRef.from_dict(payload.get("usage", {}))
            expected = str(payload.get("usage_digest", ""))
            if not expected or expected != _digest(usage.as_dict()):
                raise ArchiveCorruption(f"usage digest mismatch: {usage.usage_id}")
            prior = self._usage.get(usage.usage_id)
            if prior is not None and _canon(prior.as_dict()) != _canon(usage.as_dict()):
                raise ArchiveCorruption(f"usage id collision: {usage.usage_id}")
            self._validate_usage(usage)
            self._usage.setdefault(usage.usage_id, usage)

    def _gate(self, usage: ArchiveUsageRef) -> None:
        digest = _digest(usage.as_dict())
        command = ServantCommand(
            command_id=f"ARCHIVE-L2-GATE:{usage.usage_id}:{digest[:20]}",
            kind="INSTITUTION_ACTION",
            runbook_id=self.runbook_id,
            institution_action="NOTICE",
            subject_id=f"CURATOR_ARCHIVE:USAGE:{usage.usage_id}:{digest}",
        )
        decision = self.archive.servant.handle(command)
        if decision.disposition != "ACK_TRANSITION":
            raise UsageArchiveError(f"SERVANT gate rejected usage:{usage.usage_id}: {decision.reason_code}")

    def link_movement(
        self,
        usage_id: str,
        version_id: str,
        movement_request_id: str,
        *,
        created_at: str,
    ) -> ArchiveUsageRef:
        uid = str(usage_id).strip()
        vid = str(version_id).strip()
        rid = str(movement_request_id).strip()
        if not uid or not vid or not rid or not str(created_at).strip():
            raise ValueError("usage_id, version_id, movement_request_id and created_at are required")
        movement = self._movement_payload(rid)
        if str(movement.get("result", "")) != "MOVED":
            raise UsageArchiveError("only committed movement can be linked to archive usage")
        usage = ArchiveUsageRef(
            usage_id=uid,
            version_id=vid,
            movement_request_id=rid,
            session_id=str(movement["session_id"]),
            map_from=str(movement["map_from"]),
            map_to=str(movement["map_to"]),
            telemetry_class=str(movement["telemetry_class"]),
            movement_digest=_digest(movement),
            actual_cost=CostVector(**dict(movement["actual_cost"])),
            policy_version=str(movement["policy_version"]),
            created_at=str(created_at).strip(),
        )
        prior = self._usage.get(uid)
        if prior is not None:
            if _canon(prior.as_dict()) != _canon(usage.as_dict()):
                raise UsageArchiveError(f"usage id collision: {uid}")
            return prior
        self._validate_usage(usage)
        self._gate(usage)
        self.chronicle.append(usage)
        self._usage[uid] = usage
        return usage

    def usage(self, usage_id: str) -> ArchiveUsageRef:
        uid = str(usage_id).strip()
        if uid not in self._usage:
            raise UsageArchiveError(f"unknown usage: {uid}")
        return self._usage[uid]

    def view_usage(self, usage_id: str, query: TelemetryQuery) -> dict:
        usage = self.usage(usage_id)
        authorized = self.steward.view_telemetry(query)
        if authorized.get("status") != "ALLOWED":
            return {"status": "DENIED", "reason": authorized.get("reason", "TELEMETRY_DENIED")}

        if query.telemetry_class == "T3_AGGREGATED":
            rows = [row for row in self._usage.values() if row.version_id == usage.version_id]
            return {
                "status": "ALLOWED",
                "class": "T3_AGGREGATED",
                "version_id": usage.version_id,
                "usage_count": len(rows),
                "total_cost_l1": sum(row.actual_cost.l1 for row in rows),
            }

        if query.telemetry_class != usage.telemetry_class:
            return {"status": "DENIED", "reason": "ARCHIVE_USAGE_CLASS_MISMATCH"}
        if query.telemetry_class == "T0_SESSION_LOCAL" and query.session_id != usage.session_id:
            return {"status": "DENIED", "reason": "SESSION_LOCAL_USAGE_MISMATCH"}

        movement_rows = authorized.get("records", [])
        movement = next(
            (dict(row) for row in movement_rows if str(row.get("request_id", "")) == usage.movement_request_id),
            None,
        )
        if movement is None:
            raise ArchiveCorruption("authorized telemetry no longer contains referenced movement")
        if _digest(movement) != usage.movement_digest:
            raise ArchiveCorruption("referenced movement changed after archive linkage")

        return {
            "status": "ALLOWED",
            "class": usage.telemetry_class,
            "usage": {
                "usage_id": usage.usage_id,
                "version_id": usage.version_id,
                "movement_request_id": usage.movement_request_id,
                "session_id": usage.session_id,
                "map_from": usage.map_from,
                "map_to": usage.map_to,
                "actual_cost": usage.actual_cost.as_dict(),
                "policy_version": usage.policy_version,
                "created_at": usage.created_at,
            },
        }

    def counts(self) -> dict[str, int]:
        return {
            "usage_refs": len(self._usage),
            "records": len(self.chronicle.records()),
        }
