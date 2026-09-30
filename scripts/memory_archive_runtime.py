#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import hashlib
import json

from active_memory import Edge, MemoryEvent, Workspace, apply_delta, restore_workspace
from durable_shared_memory import JSONLWAL
from servant_runtime import ServantCommand, ServantRuntime


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _event_to_dict(event: MemoryEvent) -> dict:
    return {
        "event_id": event.event_id,
        "kind": event.kind,
        "event_time": event.event_time,
        "ingest_time": event.ingest_time,
        "payload": dict(event.payload),
    }


def _event_from_dict(row: dict) -> MemoryEvent:
    return MemoryEvent(
        event_id=str(row["event_id"]),
        kind=str(row["kind"]),
        event_time=str(row["event_time"]),
        ingest_time=str(row["ingest_time"]),
        payload=dict(row["payload"]),
    )


def _snapshot_record(workspace: Workspace) -> dict:
    return {
        "kind": "WORKSPACE_SNAPSHOT",
        "contract_id": workspace.contract_id,
        "contract_digest": workspace.contract_digest,
        "state_digest": workspace.state_digest,
        "payload": workspace.canonical_state(),
    }


class ArchiveError(RuntimeError):
    pass


class ArchiveCorruption(ArchiveError):
    pass


@dataclass(frozen=True)
class ArchiveManifest:
    version_id: str
    object_id: str
    parent_version_ids: tuple[str, ...]
    base_snapshot_id: str
    delta_ids: tuple[str, ...]
    content_digest: str
    contract_id: str
    contract_digest: str
    provenance_refs: tuple[str, ...]
    epistemic_status_ref: str
    access_policy_ref: str
    lifecycle_state: str
    created_at: str

    def __post_init__(self):
        for field in (
            "version_id",
            "object_id",
            "base_snapshot_id",
            "content_digest",
            "contract_id",
            "contract_digest",
            "epistemic_status_ref",
            "access_policy_ref",
            "lifecycle_state",
            "created_at",
        ):
            value = str(getattr(self, field)).strip()
            if not value:
                raise ValueError(f"{field} is required")
            object.__setattr__(self, field, value)
        parents = tuple(str(x).strip() for x in self.parent_version_ids if str(x).strip())
        deltas = tuple(str(x).strip() for x in self.delta_ids if str(x).strip())
        provenance = tuple(sorted({str(x).strip() for x in self.provenance_refs if str(x).strip()}))
        if len(set(parents)) != len(parents):
            raise ValueError("duplicate parent_version_id")
        if len(set(deltas)) != len(deltas):
            raise ValueError("duplicate delta_id")
        if not provenance:
            raise ValueError("at least one provenance_ref is required")
        object.__setattr__(self, "parent_version_ids", parents)
        object.__setattr__(self, "delta_ids", deltas)
        object.__setattr__(self, "provenance_refs", provenance)

    def as_dict(self) -> dict:
        return {
            "version_id": self.version_id,
            "object_id": self.object_id,
            "parent_version_ids": list(self.parent_version_ids),
            "base_snapshot_id": self.base_snapshot_id,
            "delta_ids": list(self.delta_ids),
            "content_digest": self.content_digest,
            "contract_id": self.contract_id,
            "contract_digest": self.contract_digest,
            "provenance_refs": list(self.provenance_refs),
            "epistemic_status_ref": self.epistemic_status_ref,
            "access_policy_ref": self.access_policy_ref,
            "lifecycle_state": self.lifecycle_state,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, row: dict) -> "ArchiveManifest":
        return cls(
            version_id=row["version_id"],
            object_id=row["object_id"],
            parent_version_ids=tuple(row.get("parent_version_ids", ())),
            base_snapshot_id=row["base_snapshot_id"],
            delta_ids=tuple(row.get("delta_ids", ())),
            content_digest=row["content_digest"],
            contract_id=row["contract_id"],
            contract_digest=row["contract_digest"],
            provenance_refs=tuple(row.get("provenance_refs", ())),
            epistemic_status_ref=row["epistemic_status_ref"],
            access_policy_ref=row["access_policy_ref"],
            lifecycle_state=row["lifecycle_state"],
            created_at=row["created_at"],
        )


@dataclass(frozen=True)
class ArchiveRestore:
    manifest: ArchiveManifest
    workspace: Workspace
    reconstruction_steps: int


class ArchiveChronicle:
    """Hash-chained append-only archive journal."""

    def __init__(self, path: str | Path):
        self.wal = JSONLWAL(path)

    def append(self, kind: str, key: str, payload: dict) -> None:
        self.wal.append(f"ARCHIVE_{kind}", key, payload)

    def records(self):
        return self.wal.read_valid_prefix().records


class MemoryArchiveRuntime:
    """F3.1 reference archive: snapshot + ordered deltas + manifest + pointer.

    The archive does not decide truth, admission or reusability. Persistent
    archive writes are first passed through a pre-authorized SERVANT institution
    gate, then appended to this hash-chained journal. Reconstruction is purely
    deterministic and verifies the manifest content digest.
    """

    def __init__(
        self,
        servant: ServantRuntime,
        chronicle_path: str | Path,
        *,
        runbook_id: str = "CURATOR-ARCHIVE-01",
    ):
        self.servant = servant
        self.chronicle = ArchiveChronicle(chronicle_path)
        self.runbook_id = str(runbook_id).strip()
        if not self.runbook_id:
            raise ValueError("runbook_id is required")
        self._snapshots: dict[str, dict] = {}
        self._deltas: dict[str, dict] = {}
        self._versions: dict[str, ArchiveManifest] = {}
        self._current: dict[str, str] = {}
        self._load()

    def _load(self) -> None:
        for record in self.chronicle.records():
            kind = str(record.get("kind", ""))
            payload = dict(record.get("payload", {}))
            if kind == "ARCHIVE_SNAPSHOT":
                sid = str(payload.get("snapshot_id", ""))
                snap = payload.get("snapshot")
                if not sid or not isinstance(snap, dict):
                    raise ArchiveCorruption("invalid snapshot record")
                prior = self._snapshots.get(sid)
                if prior is not None and _canon(prior) != _canon(snap):
                    raise ArchiveCorruption(f"snapshot id collision: {sid}")
                self._snapshots.setdefault(sid, snap)
            elif kind == "ARCHIVE_DELTA":
                did = str(payload.get("delta_id", ""))
                event = payload.get("event")
                if not did or not isinstance(event, dict):
                    raise ArchiveCorruption("invalid delta record")
                prior = self._deltas.get(did)
                if prior is not None and _canon(prior) != _canon(event):
                    raise ArchiveCorruption(f"delta id collision: {did}")
                self._deltas.setdefault(did, event)
            elif kind == "ARCHIVE_VERSION":
                manifest = ArchiveManifest.from_dict(payload.get("manifest", {}))
                prior = self._versions.get(manifest.version_id)
                if prior is not None and _canon(prior.as_dict()) != _canon(manifest.as_dict()):
                    raise ArchiveCorruption(f"version id collision: {manifest.version_id}")
                self._versions.setdefault(manifest.version_id, manifest)
            elif kind == "ARCHIVE_POINTER":
                object_id = str(payload.get("object_id", ""))
                version_id = str(payload.get("version_id", ""))
                if not object_id or not version_id:
                    raise ArchiveCorruption("invalid current pointer record")
                self._current[object_id] = version_id
            else:
                raise ArchiveCorruption(f"unknown archive record kind: {kind}")
        self._validate_loaded_references()

    def _validate_loaded_references(self) -> None:
        for version_id, manifest in self._versions.items():
            if manifest.base_snapshot_id not in self._snapshots:
                raise ArchiveCorruption(f"missing base snapshot for {version_id}")
            missing = [did for did in manifest.delta_ids if did not in self._deltas]
            if missing:
                raise ArchiveCorruption(f"missing delta for {version_id}: {missing}")
            for parent in manifest.parent_version_ids:
                if parent not in self._versions:
                    raise ArchiveCorruption(f"missing parent version for {version_id}: {parent}")
        for object_id, version_id in self._current.items():
            manifest = self._versions.get(version_id)
            if manifest is None or manifest.object_id != object_id:
                raise ArchiveCorruption(f"invalid CURRENT pointer: {object_id}->{version_id}")

    def _gate(self, action: str, key: str, payload_digest: str) -> None:
        # F3.1 uses the existing typed institution gate. The archive-specific
        # semantic action is preserved in subject_id and in the archive journal;
        # SERVANT remains procedural and does not interpret archive content.
        command = ServantCommand(
            command_id=f"ARCHIVE-GATE:{action}:{key}:{payload_digest[:20]}",
            kind="INSTITUTION_ACTION",
            runbook_id=self.runbook_id,
            institution_action="NOTICE",
            subject_id=f"CURATOR_ARCHIVE:{action}:{key}:{payload_digest}",
        )
        decision = self.servant.handle(command)
        if decision.disposition != "ACK_TRANSITION":
            raise ArchiveError(f"SERVANT gate rejected {action}:{key}: {decision.reason_code}")

    @staticmethod
    def _collision(existing: dict | None, incoming: dict, kind: str, key: str) -> bool:
        if existing is None:
            return False
        if _canon(existing) != _canon(incoming):
            raise ArchiveError(f"{kind} id collision: {key}")
        return True

    def store_snapshot(self, snapshot_id: str, workspace: Workspace) -> str:
        sid = str(snapshot_id).strip()
        if not sid:
            raise ValueError("snapshot_id is required")
        snap = _snapshot_record(workspace)
        if self._collision(self._snapshots.get(sid), snap, "snapshot", sid):
            return sid
        digest = _digest(snap)
        self._gate("SNAPSHOT", sid, digest)
        self.chronicle.append("SNAPSHOT", sid, {"snapshot_id": sid, "snapshot": snap, "record_digest": digest})
        self._snapshots[sid] = snap
        return sid

    def store_delta(self, delta_id: str, event: MemoryEvent) -> str:
        did = str(delta_id).strip()
        if not did:
            raise ValueError("delta_id is required")
        row = _event_to_dict(event)
        if self._collision(self._deltas.get(did), row, "delta", did):
            return did
        digest = _digest(row)
        self._gate("DELTA", did, digest)
        self.chronicle.append("DELTA", did, {"delta_id": did, "event": row, "record_digest": digest})
        self._deltas[did] = row
        return did

    def _reconstruct_unchecked(self, manifest: ArchiveManifest) -> ArchiveRestore:
        snap = self._snapshots.get(manifest.base_snapshot_id)
        if snap is None:
            raise ArchiveError(f"missing base snapshot: {manifest.base_snapshot_id}")
        try:
            workspace = restore_workspace(snap)
        except (KeyError, TypeError, ValueError) as exc:
            raise ArchiveCorruption(f"invalid base snapshot: {manifest.base_snapshot_id}") from exc
        if workspace.contract_id != manifest.contract_id or workspace.contract_digest != manifest.contract_digest:
            raise ArchiveError("manifest contract does not match base snapshot contract")
        steps = 0
        for delta_id in manifest.delta_ids:
            row = self._deltas.get(delta_id)
            if row is None:
                raise ArchiveError(f"missing delta: {delta_id}")
            try:
                event = _event_from_dict(row)
                applied = apply_delta(workspace, (event,))
            except (KeyError, TypeError, ValueError) as exc:
                raise ArchiveCorruption(f"invalid delta: {delta_id}") from exc
            if applied.ignored_events:
                raise ArchiveError(f"delta did not mutate reconstructed state: {delta_id}")
            workspace = applied.workspace
            steps += 1
        if workspace.state_digest != manifest.content_digest:
            raise ArchiveError(
                f"content digest mismatch for {manifest.version_id}: "
                f"expected {manifest.content_digest}, got {workspace.state_digest}"
            )
        return ArchiveRestore(manifest, workspace, steps)

    def publish_version(self, manifest: ArchiveManifest) -> ArchiveManifest:
        existing = self._versions.get(manifest.version_id)
        if existing is not None:
            if _canon(existing.as_dict()) != _canon(manifest.as_dict()):
                raise ArchiveError(f"version id collision: {manifest.version_id}")
            return existing
        for parent in manifest.parent_version_ids:
            if parent not in self._versions:
                raise ArchiveError(f"missing parent version: {parent}")
        restored = self._reconstruct_unchecked(manifest)
        digest = _digest(manifest.as_dict())
        self._gate("VERSION", manifest.version_id, digest)
        self.chronicle.append(
            "VERSION",
            manifest.version_id,
            {
                "manifest": manifest.as_dict(),
                "manifest_digest": digest,
                "verified_state_digest": restored.workspace.state_digest,
            },
        )
        self._versions[manifest.version_id] = manifest
        return manifest

    def publish_current(self, object_id: str, version_id: str) -> str:
        oid = str(object_id).strip()
        vid = str(version_id).strip()
        if not oid or not vid:
            raise ValueError("object_id and version_id are required")
        manifest = self._versions.get(vid)
        if manifest is None:
            raise ArchiveError(f"unknown version: {vid}")
        if manifest.object_id != oid:
            raise ArchiveError("CURRENT pointer object/version mismatch")
        if self._current.get(oid) == vid:
            return vid
        payload = {"object_id": oid, "version_id": vid}
        digest = _digest(payload)
        self._gate("CURRENT_POINTER", oid, digest)
        self.chronicle.append("POINTER", oid, payload)
        self._current[oid] = vid
        return vid

    def current(self, object_id: str) -> str | None:
        return self._current.get(str(object_id).strip())

    def manifest(self, version_id: str) -> ArchiveManifest:
        vid = str(version_id).strip()
        if vid not in self._versions:
            raise ArchiveError(f"unknown version: {vid}")
        return self._versions[vid]

    def reconstruct(self, version_id: str) -> ArchiveRestore:
        return self._reconstruct_unchecked(self.manifest(version_id))

    def restore_candidate(self, version_id: str) -> ArchiveRestore:
        # Candidate materialization is read-only. It does not ADMIT, release,
        # clear quarantine, alter CURRENT, or change epistemic_status_ref.
        return self.reconstruct(version_id)

    def counts(self) -> dict[str, int]:
        return {
            "snapshots": len(self._snapshots),
            "deltas": len(self._deltas),
            "versions": len(self._versions),
            "current_pointers": len(self._current),
            "records": len(self.chronicle.records()),
        }
