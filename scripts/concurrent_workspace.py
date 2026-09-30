#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Any
import copy
import hashlib
import json

from active_memory import Edge, MemoryEvent, Workspace
from active_memory_runtime import ActiveRuntime, SparsePatch, semantic_digest


def _canon(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _fingerprint(value: Any) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Proposal:
    proposal_id: str
    actor_id: str
    base_revision: int
    event: MemoryEvent

    def __post_init__(self):
        if not self.proposal_id:
            raise ValueError("proposal_id is required")
        if not self.actor_id:
            raise ValueError("actor_id is required")
        if self.base_revision < 0:
            raise ValueError("base_revision must be non-negative")


@dataclass(frozen=True)
class CommitResult:
    status: str
    base_revision: int
    new_revision: int
    applied_proposals: tuple[str, ...]
    duplicate_proposals: tuple[str, ...]
    conflict_targets: tuple[str, ...]
    ignored_event_ids: tuple[str, ...]
    sparse_patches: tuple[SparsePatch, ...]
    state_digest_before: str
    state_digest_after: str
    reason: str = ""


class ConcurrentWorkspace:
    """Reference optimistic transaction layer over one active Workspace.

    Proposals are authored independently against an explicit base revision.
    A batch commits only when every proposal targets the current revision and
    no target has contradictory intents. Identical intents coalesce. Actor
    identity has no priority semantics.

    Atomicity is implemented conservatively by applying the batch to a deep
    copied trial runtime and publishing it only after the whole batch succeeds.
    This is a correctness reference, not the final scalable implementation.
    """

    def __init__(self, workspace: Workspace):
        self._runtime = ActiveRuntime(copy.deepcopy(workspace))

    @property
    def workspace(self) -> Workspace:
        return self._runtime.workspace

    @property
    def revision(self) -> int:
        return self.workspace.revision

    @property
    def state_digest(self) -> str:
        return semantic_digest(self.workspace)

    @staticmethod
    def _intent(event: MemoryEvent) -> tuple[str, str]:
        if event.kind == "EDGE_UPSERT":
            edge = Edge.from_mapping(event.payload)
            target = f"EDGE|{edge.source}|{edge.relation}|{edge.target}"
            fp = _fingerprint({"kind": event.kind, "edge": edge.as_dict()})
            return target, fp

        if event.kind == "EDGE_REMOVE":
            edge = Edge.from_mapping(event.payload)
            target = f"EDGE|{edge.source}|{edge.relation}|{edge.target}"
            fp = _fingerprint({"kind": event.kind, "triple": edge.triple})
            return target, fp

        if event.kind == "NODE_STATUS_SET":
            node = str(event.payload.get("node", "")).strip()
            status = str(event.payload.get("status", "")).strip()
            if not node or not status:
                raise ValueError("NODE_STATUS_SET requires node and status")
            target = f"NODE_STATUS|{node}"
            fp = _fingerprint({"kind": event.kind, "node": node, "status": status})
            return target, fp

        raise ValueError(f"event kind is not transaction-admissible: {event.kind}")

    def commit(self, proposals: Iterable[Proposal]) -> CommitResult:
        batch = tuple(proposals)
        before = self.state_digest
        current_revision = self.revision

        if not batch:
            return CommitResult(
                status="NO_OP",
                base_revision=current_revision,
                new_revision=current_revision,
                applied_proposals=(),
                duplicate_proposals=(),
                conflict_targets=(),
                ignored_event_ids=(),
                sparse_patches=(),
                state_digest_before=before,
                state_digest_after=before,
                reason="empty batch",
            )

        proposal_ids = [p.proposal_id for p in batch]
        if len(set(proposal_ids)) != len(proposal_ids):
            return CommitResult(
                status="INVALID_BATCH",
                base_revision=current_revision,
                new_revision=current_revision,
                applied_proposals=(),
                duplicate_proposals=(),
                conflict_targets=(),
                ignored_event_ids=(),
                sparse_patches=(),
                state_digest_before=before,
                state_digest_after=before,
                reason="duplicate proposal_id",
            )

        if any(p.base_revision != current_revision for p in batch):
            return CommitResult(
                status="REBASE_REQUIRED",
                base_revision=current_revision,
                new_revision=current_revision,
                applied_proposals=(),
                duplicate_proposals=(),
                conflict_targets=(),
                ignored_event_ids=(),
                sparse_patches=(),
                state_digest_before=before,
                state_digest_after=before,
                reason="at least one proposal was authored against a stale or future revision",
            )

        by_target: dict[str, list[tuple[Proposal, str]]] = {}
        try:
            for proposal in batch:
                target, intent_fp = self._intent(proposal.event)
                by_target.setdefault(target, []).append((proposal, intent_fp))
        except (TypeError, ValueError) as exc:
            return CommitResult(
                status="INVALID_BATCH",
                base_revision=current_revision,
                new_revision=current_revision,
                applied_proposals=(),
                duplicate_proposals=(),
                conflict_targets=(),
                ignored_event_ids=(),
                sparse_patches=(),
                state_digest_before=before,
                state_digest_after=before,
                reason=str(exc),
            )

        conflicts = tuple(sorted(
            target for target, rows in by_target.items()
            if len({fp for _, fp in rows}) > 1
        ))
        if conflicts:
            return CommitResult(
                status="CONFLICT",
                base_revision=current_revision,
                new_revision=current_revision,
                applied_proposals=(),
                duplicate_proposals=(),
                conflict_targets=conflicts,
                ignored_event_ids=(),
                sparse_patches=(),
                state_digest_before=before,
                state_digest_after=before,
                reason="contradictory intents target the same semantic slot",
            )

        selected: list[Proposal] = []
        duplicates: list[str] = []
        for target in sorted(by_target):
            rows = sorted(by_target[target], key=lambda row: row[0].proposal_id)
            selected.append(rows[0][0])
            duplicates.extend(row[0].proposal_id for row in rows[1:])

        # Reference atomicity: mutate only an isolated trial copy. The live
        # runtime is replaced iff the complete application succeeds.
        trial_runtime = ActiveRuntime(copy.deepcopy(self.workspace))
        ordered_selected = sorted(selected, key=lambda p: self._intent(p.event)[0])
        result = trial_runtime.apply(tuple(p.event for p in ordered_selected))

        ignored_set = set(result.ignored_events)
        applied = tuple(
            p.proposal_id for p in ordered_selected
            if p.event.event_id not in ignored_set
        )
        after = semantic_digest(trial_runtime.workspace)

        if result.mutations:
            self._runtime = trial_runtime
            status = "COMMITTED"
        else:
            status = "NO_OP"
            after = before

        return CommitResult(
            status=status,
            base_revision=current_revision,
            new_revision=self.revision,
            applied_proposals=applied,
            duplicate_proposals=tuple(sorted(duplicates)),
            conflict_targets=(),
            ignored_event_ids=tuple(sorted(result.ignored_events)),
            sparse_patches=tuple(result.sparse_patches) if status == "COMMITTED" else (),
            state_digest_before=before,
            state_digest_after=after,
            reason="",
        )
