#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable
import hashlib
import json

from active_memory import Edge, MemoryEvent, Workspace
from active_memory_runtime import ActiveRuntime, SparsePatch, semantic_digest


def _canon(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _fingerprint(value: Any) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _edge_token(source: str, relation: str, target: str) -> str:
    return f"EDGE|{source}|{relation}|{target}"


def _node_status_token(node: str) -> str:
    return f"NODE_STATUS|{node}"


@dataclass(frozen=True)
class MVCCProposal:
    proposal_id: str
    actor_id: str
    base_revision: int
    event: MemoryEvent
    read_set: tuple[str, ...] = ()

    def __post_init__(self):
        if not self.proposal_id:
            raise ValueError("proposal_id is required")
        if not self.actor_id:
            raise ValueError("actor_id is required")
        if self.base_revision < 0:
            raise ValueError("base_revision must be non-negative")
        normalized = tuple(sorted({str(token).strip() for token in self.read_set if str(token).strip()}))
        object.__setattr__(self, "read_set", normalized)


@dataclass(frozen=True)
class MVCCCommitResult:
    status: str
    snapshot_revision: int
    new_revision: int
    applied_proposals: tuple[str, ...]
    duplicate_proposals: tuple[str, ...]
    conflict_tokens: tuple[str, ...]
    stale_tokens: tuple[str, ...]
    ignored_event_ids: tuple[str, ...]
    sparse_patches: tuple[SparsePatch, ...]
    examined_versions: int
    commit_chain_before: str
    commit_chain_after: str
    reason: str = ""


class MVCCWorkspace:
    """Optimistic MVCC layer over one ActiveRuntime without global state copy.

    Each semantic write slot carries the revision of its last committed change.
    A proposal may commit from an older snapshot iff none of its declared reads
    nor its write target changed after that snapshot. Batches fail closed on
    write/write or declared read/write hazards.

    Full semantic digests are intentionally on-demand only; commit uses an
    incremental hash chain so the hot path does not scan the whole workspace.
    """

    def __init__(self, workspace: Workspace):
        self._runtime = ActiveRuntime(workspace)
        self._epoch_revision = workspace.revision
        self._slot_versions: dict[str, int] = {}
        for edge in workspace.edges.values():
            self._slot_versions[_edge_token(*edge.triple)] = self._epoch_revision
        for node in workspace.node_status:
            self._slot_versions[_node_status_token(node)] = self._epoch_revision
        self._commit_chain = _fingerprint({
            "kind": "MVCC_INIT",
            "revision": workspace.revision,
            "semantic_digest": semantic_digest(workspace),
        })

    @property
    def workspace(self) -> Workspace:
        return self._runtime.workspace

    @property
    def revision(self) -> int:
        return self.workspace.revision

    @property
    def semantic_digest(self) -> str:
        return semantic_digest(self.workspace)

    @property
    def commit_chain_digest(self) -> str:
        return self._commit_chain

    @staticmethod
    def edge_token(source: str, relation: str, target: str) -> str:
        return _edge_token(source, relation, target)

    @staticmethod
    def node_status_token(node: str) -> str:
        return _node_status_token(node)

    @staticmethod
    def _intent(event: MemoryEvent) -> tuple[str, str]:
        if event.kind == "EDGE_UPSERT":
            edge = Edge.from_mapping(event.payload)
            target = _edge_token(*edge.triple)
            fp = _fingerprint({"kind": event.kind, "edge": edge.as_dict()})
            return target, fp

        if event.kind == "EDGE_REMOVE":
            edge = Edge.from_mapping(event.payload)
            target = _edge_token(*edge.triple)
            fp = _fingerprint({"kind": event.kind, "triple": edge.triple})
            return target, fp

        if event.kind == "NODE_STATUS_SET":
            node = str(event.payload.get("node", "")).strip()
            status = str(event.payload.get("status", "")).strip()
            if not node or not status:
                raise ValueError("NODE_STATUS_SET requires node and status")
            target = _node_status_token(node)
            fp = _fingerprint({"kind": event.kind, "node": node, "status": status})
            return target, fp

        raise ValueError(f"event kind is not MVCC-admissible: {event.kind}")

    def _version(self, token: str) -> int:
        return self._slot_versions.get(token, self._epoch_revision)

    def _preflight(self, event: MemoryEvent) -> str:
        if event.event_id in self._runtime._processed_ids:
            return "NO_OP"

        if event.kind == "EDGE_UPSERT":
            edge = Edge.from_mapping(event.payload)
            if not (self._runtime._is_active_node(edge.source) or self._runtime._is_active_node(edge.target)):
                return "NO_OP"
            if self.workspace.edges.get(edge.triple) == edge:
                return "NO_OP"
            return "MUTATE"

        if event.kind == "EDGE_REMOVE":
            edge = Edge.from_mapping(event.payload)
            return "MUTATE" if edge.triple in self.workspace.edges else "NO_OP"

        if event.kind == "NODE_STATUS_SET":
            node = str(event.payload.get("node", "")).strip()
            status = str(event.payload.get("status", "")).strip()
            if not node or not status:
                raise ValueError("NODE_STATUS_SET requires node and status")
            if not self._runtime._is_active_node(node):
                return "NO_OP"
            if self.workspace.node_status.get(node) == status:
                return "NO_OP"
            return "MUTATE"

        raise ValueError(f"event kind is not MVCC-admissible: {event.kind}")

    @staticmethod
    def _apply_order(proposal: MVCCProposal, target: str) -> tuple[int, str, str]:
        rank = {"EDGE_UPSERT": 0, "NODE_STATUS_SET": 1, "EDGE_REMOVE": 2}
        return (rank[proposal.event.kind], target, proposal.proposal_id)

    def _result(
        self,
        *,
        status: str,
        snapshot_revision: int,
        chain_before: str,
        applied: Iterable[str] = (),
        duplicates: Iterable[str] = (),
        conflicts: Iterable[str] = (),
        stale: Iterable[str] = (),
        ignored: Iterable[str] = (),
        patches: Iterable[SparsePatch] = (),
        examined_versions: int = 0,
        reason: str = "",
    ) -> MVCCCommitResult:
        return MVCCCommitResult(
            status=status,
            snapshot_revision=snapshot_revision,
            new_revision=self.revision,
            applied_proposals=tuple(applied),
            duplicate_proposals=tuple(sorted(duplicates)),
            conflict_tokens=tuple(sorted(set(conflicts))),
            stale_tokens=tuple(sorted(set(stale))),
            ignored_event_ids=tuple(sorted(ignored)),
            sparse_patches=tuple(patches),
            examined_versions=examined_versions,
            commit_chain_before=chain_before,
            commit_chain_after=self._commit_chain,
            reason=reason,
        )

    def commit(self, proposals: Iterable[MVCCProposal]) -> MVCCCommitResult:
        batch = tuple(proposals)
        snapshot_revision = self.revision
        chain_before = self._commit_chain

        if not batch:
            return self._result(
                status="NO_OP",
                snapshot_revision=snapshot_revision,
                chain_before=chain_before,
                reason="empty batch",
            )

        proposal_ids = [p.proposal_id for p in batch]
        if len(set(proposal_ids)) != len(proposal_ids):
            return self._result(
                status="INVALID_BATCH",
                snapshot_revision=snapshot_revision,
                chain_before=chain_before,
                reason="duplicate proposal_id",
            )

        if any(p.base_revision < self._epoch_revision or p.base_revision > snapshot_revision for p in batch):
            return self._result(
                status="REBASE_REQUIRED",
                snapshot_revision=snapshot_revision,
                chain_before=chain_before,
                reason="proposal snapshot is older than MVCC epoch or newer than current revision",
            )

        by_target: dict[str, list[tuple[MVCCProposal, str]]] = {}
        proposal_target: dict[str, str] = {}
        try:
            for proposal in batch:
                target, intent_fp = self._intent(proposal.event)
                proposal_target[proposal.proposal_id] = target
                by_target.setdefault(target, []).append((proposal, intent_fp))
        except (TypeError, ValueError) as exc:
            return self._result(
                status="INVALID_BATCH",
                snapshot_revision=snapshot_revision,
                chain_before=chain_before,
                reason=str(exc),
            )

        conflicts = {
            target
            for target, rows in by_target.items()
            if len({fp for _, fp in rows}) > 1
        }
        if conflicts:
            return self._result(
                status="CONFLICT",
                snapshot_revision=snapshot_revision,
                chain_before=chain_before,
                conflicts=conflicts,
                reason="contradictory writes target the same semantic slot",
            )

        writer_targets = set(by_target)
        rw_conflicts: set[str] = set()
        for proposal in batch:
            own = proposal_target[proposal.proposal_id]
            for token in proposal.read_set:
                if token in writer_targets and token != own:
                    rw_conflicts.add(token)
        if rw_conflicts:
            return self._result(
                status="CONFLICT",
                snapshot_revision=snapshot_revision,
                chain_before=chain_before,
                conflicts=rw_conflicts,
                reason="declared read/write hazard inside one batch",
            )

        stale_tokens: set[str] = set()
        examined_versions = 0
        for proposal in batch:
            tokens = set(proposal.read_set)
            tokens.add(proposal_target[proposal.proposal_id])
            for token in sorted(tokens):
                examined_versions += 1
                if self._version(token) > proposal.base_revision:
                    stale_tokens.add(token)
        if stale_tokens:
            return self._result(
                status="REBASE_REQUIRED",
                snapshot_revision=snapshot_revision,
                chain_before=chain_before,
                stale=stale_tokens,
                examined_versions=examined_versions,
                reason="declared read/write slot changed after proposal snapshot",
            )

        selected: list[MVCCProposal] = []
        duplicates: list[str] = []
        for target in sorted(by_target):
            rows = sorted(by_target[target], key=lambda row: row[0].proposal_id)
            selected.append(rows[0][0])
            duplicates.extend(row[0].proposal_id for row in rows[1:])

        mutate: list[tuple[MVCCProposal, str, str]] = []
        ignored: list[str] = []
        try:
            for proposal in selected:
                target = proposal_target[proposal.proposal_id]
                state = self._preflight(proposal.event)
                if state == "MUTATE":
                    _, fp = self._intent(proposal.event)
                    mutate.append((proposal, target, fp))
                else:
                    ignored.append(proposal.event.event_id)
        except (TypeError, ValueError) as exc:
            return self._result(
                status="INVALID_BATCH",
                snapshot_revision=snapshot_revision,
                chain_before=chain_before,
                examined_versions=examined_versions,
                reason=str(exc),
            )

        if not mutate:
            return self._result(
                status="NO_OP",
                snapshot_revision=snapshot_revision,
                chain_before=chain_before,
                duplicates=duplicates,
                ignored=ignored,
                examined_versions=examined_versions,
            )

        ordered = sorted(mutate, key=lambda row: self._apply_order(row[0], row[1]))
        runtime_result = self._runtime.apply(tuple(row[0].event for row in ordered))

        if runtime_result.mutations != len(ordered):
            raise RuntimeError("MVCC preflight/apply divergence")

        new_revision = self.revision
        for _, target, _ in ordered:
            self._slot_versions[target] = new_revision

        chain_payload = {
            "previous": chain_before,
            "revision": new_revision,
            "writes": [(target, fp) for _, target, fp in ordered],
        }
        self._commit_chain = _fingerprint(chain_payload)

        return self._result(
            status="COMMITTED",
            snapshot_revision=snapshot_revision,
            chain_before=chain_before,
            applied=(row[0].proposal_id for row in ordered),
            duplicates=duplicates,
            ignored=ignored,
            patches=runtime_result.sparse_patches,
            examined_versions=examined_versions,
        )
