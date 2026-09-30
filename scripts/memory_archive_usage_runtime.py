#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import json

from active_memory import Workspace
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


EVIDENCE_MAP_ASSOCIATION = "MAP_ASSOCIATION"
EVIDENCE_VERIFIED_CONSUMPTION = "VERIFIED_CONSUMPTION"
EVIDENCE_KINDS = {EVIDENCE_MAP_ASSOCIATION, EVIDENCE_VERIFIED_CONSUMPTION}


class UsageArchiveError(ArchiveError):
    pass


@dataclass(frozen=True)
class ArchiveConsumptionReceipt:
    """Durable receipt emitted by the exact archive read path.

    The receipt establishes which version/revision/content digest was returned by
    ``consume_version`` for one committed movement. It does not prove that a
    model semantically understood the returned workspace.
    """

    receipt_id: str
    version_id: str
    movement_request_id: str
    session_id: str
    object_id: str
    movement_digest: str
    content_digest: str
    source_revision: int
    created_at: str

    def __post_init__(self):
        for field in (
            "receipt_id",
            "version_id",
            "movement_request_id",
            "session_id",
            "object_id",
            "movement_digest",
            "content_digest",
            "created_at",
        ):
            value = str(getattr(self, field)).strip()
            if not value:
                raise ValueError(f"{field} is required")
            object.__setattr__(self, field, value)
        if isinstance(self.source_revision, bool) or int(self.source_revision) < 0:
            raise ValueError("source_revision must be a non-negative integer")
        object.__setattr__(self, "source_revision", int(self.source_revision))

    def as_dict(self) -> dict:
        return {
            "receipt_id": self.receipt_id,
            "version_id": self.version_id,
            "movement_request_id": self.movement_request_id,
            "session_id": self.session_id,
            "object_id": self.object_id,
            "movement_digest": self.movement_digest,
            "content_digest": self.content_digest,
            "source_revision": self.source_revision,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, row: dict) -> "ArchiveConsumptionReceipt":
        return cls(
            receipt_id=row["receipt_id"],
            version_id=row["version_id"],
            movement_request_id=row["movement_request_id"],
            session_id=row["session_id"],
            object_id=row["object_id"],
            movement_digest=row["movement_digest"],
            content_digest=row["content_digest"],
            source_revision=row["source_revision"],
            created_at=row["created_at"],
        )


@dataclass(frozen=True)
class ConsumedArchiveView:
    receipt: ArchiveConsumptionReceipt
    workspace: Workspace


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
    evidence_kind: str = EVIDENCE_MAP_ASSOCIATION
    consumption_receipt_id: str = ""
    content_digest: str = ""
    source_revision: int | None = None

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
        evidence = str(self.evidence_kind).strip().upper()
        if evidence not in EVIDENCE_KINDS:
            raise ValueError("unsupported archive usage evidence_kind")
        object.__setattr__(self, "evidence_kind", evidence)
        receipt_id = str(self.consumption_receipt_id).strip()
        content_digest = str(self.content_digest).strip()
        object.__setattr__(self, "consumption_receipt_id", receipt_id)
        object.__setattr__(self, "content_digest", content_digest)
        if evidence == EVIDENCE_VERIFIED_CONSUMPTION:
            if not receipt_id or not content_digest or self.source_revision is None:
                raise ValueError("verified consumption requires receipt, content digest and source revision")
            if isinstance(self.source_revision, bool) or int(self.source_revision) < 0:
                raise ValueError("source_revision must be a non-negative integer")
            object.__setattr__(self, "source_revision", int(self.source_revision))
        else:
            if receipt_id or content_digest or self.source_revision is not None:
                raise ValueError("map association must not carry verified-consumption fields")

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
            "evidence_kind": self.evidence_kind,
            "consumption_receipt_id": self.consumption_receipt_id,
            "content_digest": self.content_digest,
            "source_revision": self.source_revision,
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
            evidence_kind=row.get("evidence_kind", EVIDENCE_MAP_ASSOCIATION),
            consumption_receipt_id=row.get("consumption_receipt_id", ""),
            content_digest=row.get("content_digest", ""),
            source_revision=row.get("source_revision"),
        )


class UsageChronicle:
    """Restricted L2 journal. It stores typed references, not copied movement records."""

    def __init__(self, path: str | Path):
        self.wal = JSONLWAL(path)

    def append_usage(self, usage: ArchiveUsageRef) -> None:
        payload = {"usage": usage.as_dict(), "usage_digest": _digest(usage.as_dict())}
        self.wal.append("ARCHIVE_USAGE", usage.usage_id, payload)

    def append_consumption(self, receipt: ArchiveConsumptionReceipt) -> None:
        payload = {
            "receipt": receipt.as_dict(),
            "receipt_digest": _digest(receipt.as_dict()),
        }
        self.wal.append("ARCHIVE_CONSUMPTION", receipt.receipt_id, payload)

    def append(self, usage: ArchiveUsageRef) -> None:
        self.append_usage(usage)

    def records(self):
        return self.wal.read_valid_prefix().records


class MemoryArchiveUsageRuntime:
    """F3.2 L2 bridge between archive versions and ACCESS_STEWARD movement telemetry.

    ``link_movement`` without a consumption receipt records only MAP_ASSOCIATION.
    VERIFIED_CONSUMPTION requires a receipt emitted by ``consume_version``, which
    reconstructs and returns the exact archive version while durably binding its
    version id, source revision and content digest. Restricted telemetry remains
    in ACCESS_STEWARD; detailed archive reads re-run VIEW_TELEMETRY authorization.
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
        self._receipts: dict[str, ArchiveConsumptionReceipt] = {}
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

    def _validate_receipt(self, receipt: ArchiveConsumptionReceipt) -> None:
        manifest = self.archive.manifest(receipt.version_id)
        movement = self._movement_payload(receipt.movement_request_id)
        if str(movement.get("result", "")) != "MOVED":
            raise UsageArchiveError("consumption receipt requires committed movement")
        if manifest.object_id != receipt.object_id or manifest.object_id != str(movement.get("map_to", "")):
            raise UsageArchiveError("consumption receipt version/map mismatch")
        if str(movement.get("session_id", "")) != receipt.session_id:
            raise ArchiveCorruption("consumption receipt session does not match movement")
        if _digest(movement) != receipt.movement_digest:
            raise ArchiveCorruption("consumption receipt movement digest mismatch")
        restored = self.archive.reconstruct(receipt.version_id)
        if restored.workspace.state_digest != receipt.content_digest:
            raise ArchiveCorruption("consumption receipt content digest mismatch")
        if restored.workspace.revision != receipt.source_revision:
            raise ArchiveCorruption("consumption receipt source revision mismatch")
        if manifest.content_digest != receipt.content_digest:
            raise ArchiveCorruption("consumption receipt does not match manifest content digest")

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

        if usage.evidence_kind == EVIDENCE_VERIFIED_CONSUMPTION:
            receipt = self._receipts.get(usage.consumption_receipt_id)
            if receipt is None:
                raise UsageArchiveError("verified usage lacks consumption receipt")
            if receipt.version_id != usage.version_id:
                raise UsageArchiveError("consumption receipt/version mismatch")
            if receipt.movement_request_id != usage.movement_request_id:
                raise UsageArchiveError("consumption receipt/movement mismatch")
            if receipt.session_id != usage.session_id or receipt.object_id != usage.map_to:
                raise UsageArchiveError("consumption receipt usage binding mismatch")
            if receipt.content_digest != usage.content_digest:
                raise UsageArchiveError("consumption receipt/content digest mismatch")
            if receipt.source_revision != usage.source_revision:
                raise UsageArchiveError("consumption receipt/source revision mismatch")
            self._validate_receipt(receipt)

    def _load(self) -> None:
        for record in self.chronicle.records():
            kind = record.get("kind")
            payload = dict(record.get("payload", {}))
            if kind == "ARCHIVE_CONSUMPTION":
                receipt = ArchiveConsumptionReceipt.from_dict(payload.get("receipt", {}))
                expected = str(payload.get("receipt_digest", ""))
                if not expected or expected != _digest(receipt.as_dict()):
                    raise ArchiveCorruption(f"consumption receipt digest mismatch: {receipt.receipt_id}")
                prior = self._receipts.get(receipt.receipt_id)
                if prior is not None and _canon(prior.as_dict()) != _canon(receipt.as_dict()):
                    raise ArchiveCorruption(f"consumption receipt id collision: {receipt.receipt_id}")
                self._validate_receipt(receipt)
                self._receipts.setdefault(receipt.receipt_id, receipt)
                continue
            if kind == "ARCHIVE_USAGE":
                usage = ArchiveUsageRef.from_dict(payload.get("usage", {}))
                expected = str(payload.get("usage_digest", ""))
                if not expected or expected != _digest(usage.as_dict()):
                    raise ArchiveCorruption(f"usage digest mismatch: {usage.usage_id}")
                prior = self._usage.get(usage.usage_id)
                if prior is not None and _canon(prior.as_dict()) != _canon(usage.as_dict()):
                    raise ArchiveCorruption(f"usage id collision: {usage.usage_id}")
                self._validate_usage(usage)
                self._usage.setdefault(usage.usage_id, usage)
                continue
            raise ArchiveCorruption(f"unknown L2 usage record kind: {kind}")

    def _gate(self, kind: str, key: str, payload: dict) -> None:
        digest = _digest(payload)
        command = ServantCommand(
            command_id=f"ARCHIVE-L2-GATE:{kind}:{key}:{digest[:20]}",
            kind="INSTITUTION_ACTION",
            runbook_id=self.runbook_id,
            institution_action="NOTICE",
            subject_id=f"CURATOR_ARCHIVE:{kind}:{key}:{digest}",
        )
        decision = self.archive.servant.handle(command)
        if decision.disposition != "ACK_TRANSITION":
            raise UsageArchiveError(f"SERVANT gate rejected {kind.lower()}:{key}: {decision.reason_code}")

    def consume_version(
        self,
        receipt_id: str,
        version_id: str,
        movement_request_id: str,
        *,
        created_at: str,
    ) -> ConsumedArchiveView:
        rid = str(receipt_id).strip()
        vid = str(version_id).strip()
        mid = str(movement_request_id).strip()
        timestamp = str(created_at).strip()
        if not rid or not vid or not mid or not timestamp:
            raise ValueError("receipt_id, version_id, movement_request_id and created_at are required")

        movement = self._movement_payload(mid)
        if str(movement.get("result", "")) != "MOVED":
            raise UsageArchiveError("only committed movement can consume an archive version")
        restored = self.archive.reconstruct(vid)
        if restored.manifest.object_id != str(movement.get("map_to", "")):
            raise UsageArchiveError("consumed archive version does not name movement destination map")

        receipt = ArchiveConsumptionReceipt(
            receipt_id=rid,
            version_id=vid,
            movement_request_id=mid,
            session_id=str(movement["session_id"]),
            object_id=restored.manifest.object_id,
            movement_digest=_digest(movement),
            content_digest=restored.workspace.state_digest,
            source_revision=restored.workspace.revision,
            created_at=timestamp,
        )
        prior = self._receipts.get(rid)
        if prior is not None:
            if _canon(prior.as_dict()) != _canon(receipt.as_dict()):
                raise UsageArchiveError(f"consumption receipt id collision: {rid}")
            replay = self.archive.reconstruct(prior.version_id)
            return ConsumedArchiveView(prior, replay.workspace)

        self._validate_receipt(receipt)
        self._gate("CONSUMPTION", rid, receipt.as_dict())
        self.chronicle.append_consumption(receipt)
        self._receipts[rid] = receipt
        return ConsumedArchiveView(receipt, restored.workspace)

    def link_movement(
        self,
        usage_id: str,
        version_id: str,
        movement_request_id: str,
        *,
        created_at: str,
        consumption_receipt_id: str | None = None,
    ) -> ArchiveUsageRef:
        uid = str(usage_id).strip()
        vid = str(version_id).strip()
        rid = str(movement_request_id).strip()
        timestamp = str(created_at).strip()
        receipt_id = str(consumption_receipt_id or "").strip()
        if not uid or not vid or not rid or not timestamp:
            raise ValueError("usage_id, version_id, movement_request_id and created_at are required")
        movement = self._movement_payload(rid)
        if str(movement.get("result", "")) != "MOVED":
            raise UsageArchiveError("only committed movement can be linked to archive usage")

        evidence_kind = EVIDENCE_MAP_ASSOCIATION
        content_digest = ""
        source_revision = None
        if receipt_id:
            receipt = self._receipts.get(receipt_id)
            if receipt is None:
                raise UsageArchiveError(f"unknown consumption receipt: {receipt_id}")
            if receipt.version_id != vid:
                raise UsageArchiveError("consumption receipt/version mismatch")
            if receipt.movement_request_id != rid:
                raise UsageArchiveError("consumption receipt/movement mismatch")
            evidence_kind = EVIDENCE_VERIFIED_CONSUMPTION
            content_digest = receipt.content_digest
            source_revision = receipt.source_revision

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
            created_at=timestamp,
            evidence_kind=evidence_kind,
            consumption_receipt_id=receipt_id,
            content_digest=content_digest,
            source_revision=source_revision,
        )
        prior = self._usage.get(uid)
        if prior is not None:
            if _canon(prior.as_dict()) != _canon(usage.as_dict()):
                raise UsageArchiveError(f"usage id collision: {uid}")
            return prior
        self._validate_usage(usage)
        self._gate("USAGE", uid, usage.as_dict())
        self.chronicle.append_usage(usage)
        self._usage[uid] = usage
        return usage

    def consumption_receipt(self, receipt_id: str) -> ArchiveConsumptionReceipt:
        rid = str(receipt_id).strip()
        if rid not in self._receipts:
            raise UsageArchiveError(f"unknown consumption receipt: {rid}")
        return self._receipts[rid]

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
                "verified_consumption_count": sum(
                    row.evidence_kind == EVIDENCE_VERIFIED_CONSUMPTION for row in rows
                ),
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

        body = {
            "usage_id": usage.usage_id,
            "version_id": usage.version_id,
            "movement_request_id": usage.movement_request_id,
            "session_id": usage.session_id,
            "map_from": usage.map_from,
            "map_to": usage.map_to,
            "actual_cost": usage.actual_cost.as_dict(),
            "policy_version": usage.policy_version,
            "created_at": usage.created_at,
            "evidence_kind": usage.evidence_kind,
        }
        if usage.evidence_kind == EVIDENCE_VERIFIED_CONSUMPTION:
            body.update({
                "consumption_receipt_id": usage.consumption_receipt_id,
                "content_digest": usage.content_digest,
                "source_revision": usage.source_revision,
            })
        return {
            "status": "ALLOWED",
            "class": usage.telemetry_class,
            "usage": body,
        }

    def counts(self) -> dict[str, int]:
        return {
            "consumption_receipts": len(self._receipts),
            "usage_refs": len(self._usage),
            "records": len(self.chronicle.records()),
        }
