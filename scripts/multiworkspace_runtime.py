#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Iterable

from active_memory import Edge, MemoryEvent, Workspace
from active_memory_runtime import ActiveRuntime, SparsePatch


@dataclass(frozen=True)
class RoutedPatch:
    workspace_id: str
    patch: SparsePatch


@dataclass(frozen=True)
class IndexRefreshCost:
    edge_visits: int
    node_membership_updates: int
    dependency_membership_updates: int

    @property
    def membership_updates(self) -> int:
        return self.node_membership_updates + self.dependency_membership_updates


@dataclass(frozen=True)
class DispatchResult:
    event_id: str
    candidate_workspaces: tuple[str, ...]
    delivered_workspaces: tuple[str, ...]
    ignored_workspaces: tuple[str, ...]
    routed_patches: tuple[RoutedPatch, ...]
    examined_workspaces: int
    mutations: int
    examined_events: int
    history_items_copied: int
    history_items_appended: int
    index_refresh_edge_visits: int
    index_node_membership_updates: int
    index_dependency_membership_updates: int

    @property
    def index_membership_updates(self) -> int:
        return self.index_node_membership_updates + self.index_dependency_membership_updates


@dataclass(frozen=True)
class WorkspaceInvalidationResult:
    changed_dependencies: tuple[str, ...]
    stale_workspaces: tuple[str, ...]
    visited_tokens: tuple[str, ...]
    examined_dependency_links: int


class MultiWorkspaceRuntime:
    """Indexed single-writer coordinator for multiple active workspaces.

    Event routing and epistemic invalidation are deliberately separate:
    - events are routed by active node membership and are then interpreted by
      each workspace's ActiveRuntime;
    - invalidation is routed only through declared dependency tokens.

    Cost counters deliberately expose hidden local work. In the current
    reference implementation `_refresh_indices` materializes both
    `workspace.nodes` and `workspace.dependencies`; each property scans all
    workspace edges. Therefore one refresh reports two edge visits per current
    edge. F0.4 measures this behaviour; it does not optimize it away.

    This reference layer does not implement concurrent writers or transactions.
    """

    def __init__(self):
        self._runtimes: dict[str, ActiveRuntime] = {}
        self._extra_dependencies: dict[str, frozenset[str]] = {}
        self._workspace_nodes: dict[str, frozenset[str]] = {}
        self._workspace_dependencies: dict[str, frozenset[str]] = {}
        self._node_to_workspaces: dict[str, set[str]] = defaultdict(set)
        self._dependency_to_workspaces: dict[str, set[str]] = defaultdict(set)
        self._status: dict[str, str] = {}

    def reset_from(self, other: "MultiWorkspaceRuntime") -> None:
        """Replace recovered contents while preserving this public handle.

        Long-lived institutional components may keep a reference to the view
        coordinator. Recovery must therefore replace the coordinator's state,
        not the coordinator object itself. Runtime/workspace identities inside
        the coordinator are not promised to survive recovery.
        """
        if not isinstance(other, MultiWorkspaceRuntime):
            raise TypeError("reset_from requires MultiWorkspaceRuntime")
        if other is self:
            return
        self._runtimes = other._runtimes
        self._extra_dependencies = other._extra_dependencies
        self._workspace_nodes = other._workspace_nodes
        self._workspace_dependencies = other._workspace_dependencies
        self._node_to_workspaces = other._node_to_workspaces
        self._dependency_to_workspaces = other._dependency_to_workspaces
        self._status = other._status

    @property
    def workspace_count(self) -> int:
        return len(self._runtimes)

    def has_workspace(self, workspace_id: str) -> bool:
        return str(workspace_id).strip() in self._runtimes

    def workspace(self, workspace_id: str) -> Workspace:
        return self._runtimes[workspace_id].workspace

    def status(self, workspace_id: str) -> str:
        return self._status[workspace_id]

    def dependency_tokens(self, workspace_id: str) -> frozenset[str]:
        return self._workspace_dependencies[workspace_id]

    def direct_dependents(self, dependency_token: str) -> tuple[str, ...]:
        """Return indexed direct dependents without mutating epistemic status."""
        token = str(dependency_token).strip()
        if not token:
            raise ValueError("dependency_token is required")
        return tuple(sorted(self._dependency_to_workspaces.get(token, ())))

    def register(
        self,
        workspace_id: str,
        workspace: Workspace,
        *,
        extra_dependencies: Iterable[str] = (),
    ) -> None:
        wid = str(workspace_id).strip()
        if not wid:
            raise ValueError("workspace_id is required")
        if wid in self._runtimes:
            raise ValueError(f"workspace already registered: {wid}")
        extras = frozenset(str(dep).strip() for dep in extra_dependencies if str(dep).strip())
        if f"workspace:{wid}" in extras:
            raise ValueError("workspace cannot depend directly on itself")
        self._runtimes[wid] = ActiveRuntime(workspace)
        self._extra_dependencies[wid] = extras
        self._status[wid] = "VALID"
        self._refresh_indices(wid)

    def mark_valid(self, workspace_id: str) -> None:
        if workspace_id not in self._runtimes:
            raise KeyError(workspace_id)
        self._status[workspace_id] = "VALID"

    def _refresh_indices(self, workspace_id: str) -> IndexRefreshCost:
        runtime = self._runtimes[workspace_id]
        edge_count = len(runtime.workspace.edges)

        # Current implementation scans every edge once for nodes and once for
        # dependencies. Count those visits explicitly rather than treating this
        # refresh as free work behind a one-workspace routing result.
        new_nodes = frozenset(runtime.workspace.nodes)
        new_dependencies = frozenset(
            set(runtime.workspace.dependencies) | set(self._extra_dependencies[workspace_id])
        )
        edge_visits = 2 * edge_count

        old_nodes = self._workspace_nodes.get(workspace_id, frozenset())
        removed_nodes = old_nodes - new_nodes
        added_nodes = new_nodes - old_nodes
        for node in removed_nodes:
            bucket = self._node_to_workspaces.get(node)
            if bucket is not None:
                bucket.discard(workspace_id)
                if not bucket:
                    self._node_to_workspaces.pop(node, None)
        for node in added_nodes:
            self._node_to_workspaces[node].add(workspace_id)
        self._workspace_nodes[workspace_id] = new_nodes

        old_dependencies = self._workspace_dependencies.get(workspace_id, frozenset())
        removed_dependencies = old_dependencies - new_dependencies
        added_dependencies = new_dependencies - old_dependencies
        for dep in removed_dependencies:
            bucket = self._dependency_to_workspaces.get(dep)
            if bucket is not None:
                bucket.discard(workspace_id)
                if not bucket:
                    self._dependency_to_workspaces.pop(dep, None)
        for dep in added_dependencies:
            self._dependency_to_workspaces[dep].add(workspace_id)
        self._workspace_dependencies[workspace_id] = new_dependencies

        return IndexRefreshCost(
            edge_visits=edge_visits,
            node_membership_updates=len(removed_nodes) + len(added_nodes),
            dependency_membership_updates=len(removed_dependencies) + len(added_dependencies),
        )

    def _event_candidates(self, event: MemoryEvent) -> set[str]:
        if event.kind == "FORUM_OBJECT_SEEN":
            return set()
        if event.kind in {"EDGE_UPSERT", "EDGE_REMOVE"}:
            edge = Edge.from_mapping(event.payload)
            return set(self._node_to_workspaces.get(edge.source, ())) | set(
                self._node_to_workspaces.get(edge.target, ())
            )
        if event.kind == "NODE_STATUS_SET":
            node = str(event.payload.get("node", "")).strip()
            if not node:
                raise ValueError("NODE_STATUS_SET requires node")
            return set(self._node_to_workspaces.get(node, ()))
        return set()

    def dispatch(self, event: MemoryEvent) -> DispatchResult:
        candidates = tuple(sorted(self._event_candidates(event)))
        delivered: list[str] = []
        ignored: list[str] = []
        patches: list[RoutedPatch] = []
        mutations = 0
        examined_events = 0
        history_items_copied = 0
        history_items_appended = 0
        index_refresh_edge_visits = 0
        index_node_membership_updates = 0
        index_dependency_membership_updates = 0

        for wid in candidates:
            result = self._runtimes[wid].apply((event,))
            examined_events += result.examined_events
            history_items_copied += result.history_items_copied
            history_items_appended += result.history_items_appended
            if result.mutations:
                delivered.append(wid)
                mutations += result.mutations
                patches.extend(RoutedPatch(wid, patch) for patch in result.sparse_patches)
                refresh = self._refresh_indices(wid)
                index_refresh_edge_visits += refresh.edge_visits
                index_node_membership_updates += refresh.node_membership_updates
                index_dependency_membership_updates += refresh.dependency_membership_updates
            else:
                ignored.append(wid)

        return DispatchResult(
            event_id=event.event_id,
            candidate_workspaces=candidates,
            delivered_workspaces=tuple(delivered),
            ignored_workspaces=tuple(ignored),
            routed_patches=tuple(patches),
            examined_workspaces=len(candidates),
            mutations=mutations,
            examined_events=examined_events,
            history_items_copied=history_items_copied,
            history_items_appended=history_items_appended,
            index_refresh_edge_visits=index_refresh_edge_visits,
            index_node_membership_updates=index_node_membership_updates,
            index_dependency_membership_updates=index_dependency_membership_updates,
        )

    def invalidate(self, changed_dependencies: Iterable[str]) -> WorkspaceInvalidationResult:
        initial = tuple(sorted({str(dep).strip() for dep in changed_dependencies if str(dep).strip()}))
        queue = deque(initial)
        visited_tokens: set[str] = set()
        stale: set[str] = set()
        examined_links = 0

        while queue:
            token = queue.popleft()
            if token in visited_tokens:
                continue
            visited_tokens.add(token)
            dependents = self._dependency_to_workspaces.get(token, ())
            examined_links += len(dependents)
            for wid in sorted(dependents):
                if wid in stale:
                    continue
                stale.add(wid)
                self._status[wid] = "NEEDS_RECHECK"
                queue.append(f"workspace:{wid}")

        return WorkspaceInvalidationResult(
            changed_dependencies=initial,
            stale_workspaces=tuple(sorted(stale)),
            visited_tokens=tuple(sorted(visited_tokens)),
            examined_dependency_links=examined_links,
        )
