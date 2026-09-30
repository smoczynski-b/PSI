#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable
import copy
import hashlib
import json
import os

from active_memory import MemoryEvent, Workspace
from mvcc_workspace import MVCCCommitResult, MVCCProposal
from shared_memory_runtime import SharedCommitResult, SharedMemoryRuntime


def _canon(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _hash(value: Any) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


class WALCorruption(RuntimeError):
    pass


class SimulatedCrash(RuntimeError):
    pass


@dataclass(frozen=True)
class WALReadResult:
    records: tuple[dict[str, Any], ...]
    tail_truncated: bool


class JSONLWAL:
    """Append-only fsync-backed JSONL WAL with a per-record hash chain."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch(exist_ok=True)
        read = self.read_valid_prefix()
        self._seq = len(read.records)
        self._last_hash = read.records[-1]["record_hash"] if read.records else "GENESIS"

    @staticmethod
    def _verify_record(record: dict[str, Any], expected_seq: int, expected_prev: str) -> str:
        if record.get("seq") != expected_seq:
            raise WALCorruption(f"WAL sequence mismatch at {expected_seq}")
        if record.get("prev_hash") != expected_prev:
            raise WALCorruption(f"WAL hash-chain predecessor mismatch at {expected_seq}")
        recorded = str(record.get("record_hash", ""))
        payload = dict(record)
        payload.pop("record_hash", None)
        actual = _hash(payload)
        if recorded != actual:
            raise WALCorruption(f"WAL record hash mismatch at {expected_seq}")
        return recorded

    def append(self, kind: str, txid: str, payload: dict[str, Any]) -> dict[str, Any]:
        record = {
            "seq": self._seq,
            "prev_hash": self._last_hash,
            "kind": str(kind),
            "txid": str(txid),
            "payload": payload,
        }
        record["record_hash"] = _hash(record)
        line = (_canon(record) + "\n").encode("utf-8")
        with self.path.open("ab", buffering=0) as fh:
            fh.write(line)
            fh.flush()
            os.fsync(fh.fileno())
        self._seq += 1
        self._last_hash = record["record_hash"]
        return record

    def read_valid_prefix(self) -> WALReadResult:
        raw = self.path.read_bytes()
        if not raw:
            return WALReadResult((), False)
        lines = raw.splitlines(keepends=True)
        records: list[dict[str, Any]] = []
        expected_prev = "GENESIS"
        tail_truncated = False
        for i, raw_line in enumerate(lines):
            complete = raw_line.endswith(b"\n")
            if not complete:
                if i != len(lines) - 1:
                    raise WALCorruption("incomplete WAL record before tail")
                tail_truncated = True
                break
            try:
                record = json.loads(raw_line.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                if i == len(lines) - 1:
                    tail_truncated = True
                    break
                raise WALCorruption(f"invalid WAL JSON at record {i}") from exc
            expected_prev = self._verify_record(record, i, expected_prev)
            records.append(record)
        return WALReadResult(tuple(records), tail_truncated)

    def repair_truncated_tail(self) -> bool:
        read = self.read_valid_prefix()
        if not read.tail_truncated:
            return False
        data = b"".join((_canon(record) + "\n").encode("utf-8") for record in read.records)
        with self.path.open("wb", buffering=0) as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        self._seq = len(read.records)
        self._last_hash = read.records[-1]["record_hash"] if read.records else "GENESIS"
        return True


def _event_to_dict(event: MemoryEvent) -> dict[str, Any]:
    return {
        "event_id": event.event_id,
        "kind": event.kind,
        "event_time": event.event_time,
        "ingest_time": event.ingest_time,
        "payload": dict(event.payload),
    }


def _event_from_dict(row: dict[str, Any]) -> MemoryEvent:
    return MemoryEvent(**row)


def _proposal_to_dict(proposal: MVCCProposal) -> dict[str, Any]:
    return {
        "proposal_id": proposal.proposal_id,
        "actor_id": proposal.actor_id,
        "base_revision": proposal.base_revision,
        "read_set": list(proposal.read_set),
        "event": _event_to_dict(proposal.event),
    }


def _proposal_from_dict(row: dict[str, Any]) -> MVCCProposal:
    return MVCCProposal(
        proposal_id=row["proposal_id"],
        actor_id=row["actor_id"],
        base_revision=int(row["base_revision"]),
        read_set=tuple(row.get("read_set", ())),
        event=_event_from_dict(row["event"]),
    )


@dataclass(frozen=True)
class DurableCommitResult:
    txid: str
    result: SharedCommitResult
    wal_state: str


class DurableSharedMemoryRuntime:
    """Shared-memory runtime protected by an append-only WAL.

    The caller supplies deterministic baseline constructors. Recovery rebuilds
    authoritative memory and local views by replaying only transactions with a
    durable COMMIT record. PREPARE-only transactions are ignored. ACK records
    certify completed propagation, but replay does not depend on them.
    """

    def __init__(
        self,
        authoritative_seed: Workspace,
        wal_path: str | Path,
        register_views: Callable[[SharedMemoryRuntime], None],
        *,
        recover: bool = True,
    ):
        self._authoritative_seed = copy.deepcopy(authoritative_seed)
        self._register_views = register_views
        self.wal = JSONLWAL(wal_path)
        if self.wal.read_valid_prefix().tail_truncated:
            self.wal.repair_truncated_tail()
        initial_records = self.wal.read_valid_prefix().records
        self._known_txids = {record["txid"] for record in initial_records}
        self.shared = self._fresh_shared()
        if recover:
            self.recover()

    def _fresh_shared(self) -> SharedMemoryRuntime:
        fresh = SharedMemoryRuntime(copy.deepcopy(self._authoritative_seed))
        self._register_views(fresh)
        if hasattr(self, "shared"):
            self.shared.reset_from(fresh)
            return self.shared
        return fresh

    @property
    def revision(self) -> int:
        return self.shared.revision

    def workspace(self, workspace_id: str) -> Workspace:
        return self.shared.workspace(workspace_id)

    def status(self, workspace_id: str) -> str:
        return self.shared.status(workspace_id)

    def _records_by_tx(self) -> tuple[list[str], dict[str, list[dict[str, Any]]]]:
        read = self.wal.read_valid_prefix()
        order: list[str] = []
        by_tx: dict[str, list[dict[str, Any]]] = {}
        for record in read.records:
            txid = record["txid"]
            if txid not in by_tx:
                by_tx[txid] = []
                order.append(txid)
            by_tx[txid].append(record)
        return order, by_tx

    def _propagate_committed(
        self,
        proposals: tuple[MVCCProposal, ...],
        mvcc: MVCCCommitResult,
    ) -> SharedCommitResult:
        by_id = {p.proposal_id: p for p in proposals}
        delivered: set[str] = set()
        routed_patches = []
        examined_workspaces = 0
        examined_events = 0
        history_items_copied = 0
        history_items_appended = 0
        index_refresh_edge_visits = 0
        index_node_membership_updates = 0
        index_dependency_membership_updates = 0

        for pid in mvcc.applied_proposals:
            routed = self.shared.views.dispatch(by_id[pid].event)
            examined_workspaces += routed.examined_workspaces
            examined_events += routed.examined_events
            history_items_copied += routed.history_items_copied
            history_items_appended += routed.history_items_appended
            index_refresh_edge_visits += routed.index_refresh_edge_visits
            index_node_membership_updates += routed.index_node_membership_updates
            index_dependency_membership_updates += routed.index_dependency_membership_updates
            delivered.update(routed.delivered_workspaces)
            routed_patches.extend(routed.routed_patches)

        invalidation = self.shared.views.invalidate(
            f"workspace:{wid}" for wid in sorted(delivered)
        ) if delivered else None
        return SharedCommitResult(
            status=mvcc.status,
            base_revision=mvcc.snapshot_revision,
            new_revision=mvcc.new_revision,
            applied_proposals=mvcc.applied_proposals,
            duplicate_proposals=mvcc.duplicate_proposals,
            conflict_tokens=mvcc.conflict_tokens,
            stale_tokens=mvcc.stale_tokens,
            delivered_workspaces=tuple(sorted(delivered)),
            invalidated_workspaces=(invalidation.stale_workspaces if invalidation else ()),
            routed_patches=tuple(routed_patches),
            examined_versions=mvcc.examined_versions,
            examined_workspaces=examined_workspaces,
            examined_dependency_links=(invalidation.examined_dependency_links if invalidation else 0),
            examined_events=examined_events,
            history_items_copied=history_items_copied,
            history_items_appended=history_items_appended,
            index_refresh_edge_visits=index_refresh_edge_visits,
            index_node_membership_updates=index_node_membership_updates,
            index_dependency_membership_updates=index_dependency_membership_updates,
            commit_chain_before=mvcc.commit_chain_before,
            commit_chain_after=mvcc.commit_chain_after,
            reason=mvcc.reason,
        )

    def _inject_partial_propagation(
        self,
        proposals: tuple[MVCCProposal, ...],
        applied: tuple[str, ...],
    ) -> None:
        by_id = {p.proposal_id: p for p in proposals}
        if applied:
            self.shared.views.dispatch(by_id[applied[0]].event)
        raise SimulatedCrash("MID_PROPAGATE")

    def commit(
        self,
        txid: str,
        proposals: Iterable[MVCCProposal],
        *,
        crash_at: str | None = None,
    ) -> DurableCommitResult:
        txid = str(txid).strip()
        if not txid:
            raise ValueError("txid is required")
        if txid in self._known_txids:
            raise ValueError(f"txid already exists in WAL: {txid}")
        batch = tuple(proposals)
        self.wal.append("PREPARE", txid, {"proposals": [_proposal_to_dict(p) for p in batch]})
        self._known_txids.add(txid)
        if crash_at == "AFTER_PREPARE":
            raise SimulatedCrash("AFTER_PREPARE")

        mvcc = self.shared.memory.commit(batch)
        if mvcc.status != "COMMITTED":
            self.wal.append("REJECT", txid, {
                "status": mvcc.status,
                "reason": mvcc.reason,
                "new_revision": mvcc.new_revision,
            })
            return DurableCommitResult(txid, SharedMemoryRuntime._empty_from_mvcc(mvcc), "REJECT")

        self.wal.append("COMMIT", txid, {
            "new_revision": mvcc.new_revision,
            "applied_proposals": list(mvcc.applied_proposals),
            "commit_chain_after": mvcc.commit_chain_after,
        })
        if crash_at == "AFTER_COMMIT":
            raise SimulatedCrash("AFTER_COMMIT")
        if crash_at == "MID_PROPAGATE":
            self._inject_partial_propagation(batch, mvcc.applied_proposals)

        result = self._propagate_committed(batch, mvcc)
        self.wal.append("ACK", txid, {
            "delivered_workspaces": list(result.delivered_workspaces),
            "invalidated_workspaces": list(result.invalidated_workspaces),
        })
        return DurableCommitResult(txid, result, "ACK")

    def recover(self) -> None:
        self.shared = self._fresh_shared()
        order, by_tx = self._records_by_tx()
        self._known_txids = set(by_tx)
        for txid in order:
            records = by_tx[txid]
            prepare = next((r for r in records if r["kind"] == "PREPARE"), None)
            commit = next((r for r in records if r["kind"] == "COMMIT"), None)
            if prepare is None or commit is None:
                continue
            proposals = tuple(_proposal_from_dict(p) for p in prepare["payload"]["proposals"])
            result = self.shared.commit(proposals)
            if result.status != "COMMITTED":
                raise WALCorruption(f"committed WAL transaction cannot replay: {txid}: {result.status}")
            expected = tuple(commit["payload"]["applied_proposals"])
            if result.applied_proposals != expected:
                raise WALCorruption(f"WAL applied proposal mismatch during replay: {txid}")
            if result.commit_chain_after != commit["payload"]["commit_chain_after"]:
                raise WALCorruption(f"WAL commit-chain mismatch during replay: {txid}")
            if not any(r["kind"] == "ACK" for r in records):
                self.wal.append("ACK", txid, {
                    "recovered": True,
                    "delivered_workspaces": list(result.delivered_workspaces),
                    "invalidated_workspaces": list(result.invalidated_workspaces),
                })
