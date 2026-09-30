#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from active_memory import Workspace
from mvcc_workspace import MVCCCommitResult, MVCCProposal, MVCCWorkspace
from multiworkspace_runtime import MultiWorkspaceRuntime, RoutedPatch


@dataclass(frozen=True)
class SharedCommitResult:
    status: str
    base_revision: int
    new_revision: int
    applied_proposals: tuple[str, ...]
    duplicate_proposals: tuple[str, ...]
    conflict_tokens: tuple[str, ...]
    stale_tokens: tuple[str, ...]
    delivered_workspaces: tuple[str, ...]
    invalidated_workspaces: tuple[str, ...]
    routed_patches: tuple[RoutedPatch, ...]
    examined_versions: int
    examined_workspaces: int
    examined_dependency_links: int
    examined_events: int
    history_items_copied: int
    history_items_appended: int
    index_refresh_edge_visits: int
    index_node_membership_updates: int
    index_dependency_membership_updates: int
    commit_chain_before: str
    commit_chain_after: str
    reason: str = ""

    @property
    def index_membership_updates(self) -> int:
        return self.index_node_membership_updates + self.index_dependency_membership_updates


class SharedMemoryRuntime:
    """One authoritative MVCC memory plus indexed task-local workspaces.

    The authoritative workspace accepts transactions. Only events that actually
    commit are routed into local active workspaces. A local workspace that
    changes emits workspace:<id> as an invalidation token for downstream views.

    Work accounting distinguishes MVCC version checks, selected workspaces,
    event processing, local index refresh scans, dependency invalidation and
    processed-event history copying. `examined_workspaces` therefore must not be
    read as the total cost of a commit.

    This layer deliberately does not make FORUM observations authoritative and
    does not scan all workspaces after a commit. It is a deterministic,
    crash-free, single-process integration reference; durable recovery and
    distributed execution are outside this implementation.
    """

    def __init__(self, authoritative_workspace: Workspace):
        self.memory = MVCCWorkspace(authoritative_workspace)
        self.views = MultiWorkspaceRuntime()

    def reset_from(self, other: "SharedMemoryRuntime") -> None:
        """Install recovered state without invalidating long-lived handles.

        `self` and `self.views` keep object identity; their contents are replaced
        by the freshly replayed runtime. This is the recovery boundary used by
        institutional components that retain the shared/view handles.
        """
        if not isinstance(other, SharedMemoryRuntime):
            raise TypeError("reset_from requires SharedMemoryRuntime")
        if other is self:
            return
        self.memory = other.memory
        self.views.reset_from(other.views)

    @property
    def revision(self) -> int:
        return self.memory.revision

    def register(
        self,
        workspace_id: str,
        workspace: Workspace,
        *,
        extra_dependencies: Iterable[str] = (),
    ) -> None:
        self.views.register(
            workspace_id,
            workspace,
            extra_dependencies=extra_dependencies,
        )

    def workspace(self, workspace_id: str) -> Workspace:
        return self.views.workspace(workspace_id)

    def status(self, workspace_id: str) -> str:
        return self.views.status(workspace_id)

    @staticmethod
    def _empty_from_mvcc(result: MVCCCommitResult) -> SharedCommitResult:
        return SharedCommitResult(
            status=result.status,
            base_revision=result.snapshot_revision,
            new_revision=result.new_revision,
            applied_proposals=result.applied_proposals,
            duplicate_proposals=result.duplicate_proposals,
            conflict_tokens=result.conflict_tokens,
            stale_tokens=result.stale_tokens,
            delivered_workspaces=(),
            invalidated_workspaces=(),
            routed_patches=(),
            examined_versions=result.examined_versions,
            examined_workspaces=0,
            examined_dependency_links=0,
            examined_events=0,
            history_items_copied=0,
            history_items_appended=0,
            index_refresh_edge_visits=0,
            index_node_membership_updates=0,
            index_dependency_membership_updates=0,
            commit_chain_before=result.commit_chain_before,
            commit_chain_after=result.commit_chain_after,
            reason=result.reason,
        )

    def commit(self, proposals: Iterable[MVCCProposal]) -> SharedCommitResult:
        batch = tuple(proposals)
        by_id = {proposal.proposal_id: proposal for proposal in batch}

        mvcc = self.memory.commit(batch)
        if mvcc.status != "COMMITTED":
            return self._empty_from_mvcc(mvcc)

        delivered: set[str] = set()
        routed_patches: list[RoutedPatch] = []
        examined_workspaces = 0
        examined_events = 0
        history_items_copied = 0
        history_items_appended = 0
        index_refresh_edge_visits = 0
        index_node_membership_updates = 0
        index_dependency_membership_updates = 0

        # The MVCC result is the admission boundary. No rejected/no-op proposal
        # is allowed to reach a local workspace.
        for proposal_id in mvcc.applied_proposals:
            proposal = by_id[proposal_id]
            routed = self.views.dispatch(proposal.event)
            examined_workspaces += routed.examined_workspaces
            examined_events += routed.examined_events
            history_items_copied += routed.history_items_copied
            history_items_appended += routed.history_items_appended
            index_refresh_edge_visits += routed.index_refresh_edge_visits
            index_node_membership_updates += routed.index_node_membership_updates
            index_dependency_membership_updates += routed.index_dependency_membership_updates
            delivered.update(routed.delivered_workspaces)
            routed_patches.extend(routed.routed_patches)

        # Directly updated workspaces are current with respect to the committed
        # delta. Their *dependants* must re-check derived state. The workspace
        # token therefore forms the bridge between routing and invalidation.
        invalidation = self.views.invalidate(
            f"workspace:{workspace_id}" for workspace_id in sorted(delivered)
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
            invalidated_workspaces=(
                invalidation.stale_workspaces if invalidation is not None else ()
            ),
            routed_patches=tuple(routed_patches),
            examined_versions=mvcc.examined_versions,
            examined_workspaces=examined_workspaces,
            examined_dependency_links=(
                invalidation.examined_dependency_links if invalidation is not None else 0
            ),
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
