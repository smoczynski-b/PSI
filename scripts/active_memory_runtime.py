#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable
import hashlib
import json

from active_memory import Edge, MemoryEvent, Workspace


def _canon(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def semantic_digest(workspace: Workspace) -> str:
    """Digest task-relevant state, excluding operational revision/event history."""
    payload = {
        "contract_id": workspace.contract_id,
        "contract_digest": workspace.contract_digest,
        "anchor": workspace.anchor,
        "node_status": dict(sorted(workspace.node_status.items())),
        "edges": [workspace.edges[k].as_dict() for k in sorted(workspace.edges)],
    }
    return hashlib.sha256(_canon(payload).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class SparsePatch:
    event_id: str
    op: str
    relation: str
    source_index: int
    target_index: int
    source: str
    target: str


@dataclass(frozen=True)
class RuntimeDelta:
    workspace: Workspace
    affected_nodes: tuple[str, ...]
    affected_edges: tuple[tuple[str, str, str], ...]
    ignored_events: tuple[str, ...]
    sparse_patches: tuple[SparsePatch, ...]
    examined_events: int
    mutations: int
    history_items_copied: int
    history_items_appended: int


class ActiveRuntime:
    """Single-writer indexed execution layer for one already compiled Workspace.

    The authoritative semantic object remains Workspace. This sidecar keeps O(1)
    membership and stable append-only node indices so one delta does not require
    scanning/copying the whole memory view. Concurrency/rollback are deliberately
    outside this reference implementation.

    Cost accounting is explicit. `history_items_copied` reports the number of
    already-recorded event identifiers recopied by the current tuple-backed
    `processed_events` implementation. It is intentionally observational: this
    class does not hide or optimize that cost in F0.4.
    """

    def __init__(self, workspace: Workspace):
        self.workspace = workspace
        self._processed_ids = set(workspace.processed_events)
        self._refcount: dict[str, int] = {}
        for edge in workspace.edges.values():
            self._refcount[edge.source] = self._refcount.get(edge.source, 0) + 1
            self._refcount[edge.target] = self._refcount.get(edge.target, 0) + 1

        initial_nodes = sorted(workspace.nodes)
        self.node_to_index = {node: i for i, node in enumerate(initial_nodes)}
        self.index_to_node = list(initial_nodes)

    def _is_active_node(self, node: str) -> bool:
        return (
            node == self.workspace.anchor
            or node in self.workspace.node_status
            or self._refcount.get(node, 0) > 0
        )

    def _ensure_index(self, node: str) -> int:
        idx = self.node_to_index.get(node)
        if idx is not None:
            return idx
        idx = len(self.index_to_node)
        self.node_to_index[node] = idx
        self.index_to_node.append(node)
        return idx

    def _inc_edge(self, edge: Edge) -> None:
        self._refcount[edge.source] = self._refcount.get(edge.source, 0) + 1
        self._refcount[edge.target] = self._refcount.get(edge.target, 0) + 1
        self._ensure_index(edge.source)
        self._ensure_index(edge.target)

    def _dec_node(self, node: str) -> None:
        count = self._refcount.get(node, 0)
        if count <= 1:
            self._refcount.pop(node, None)
        else:
            self._refcount[node] = count - 1

    def _dec_edge(self, edge: Edge) -> None:
        self._dec_node(edge.source)
        self._dec_node(edge.target)

    @property
    def index_capacity(self) -> int:
        return len(self.index_to_node)

    def apply(self, events: Iterable[MemoryEvent]) -> RuntimeDelta:
        ws = self.workspace
        affected_nodes: set[str] = set()
        affected_edges: set[tuple[str, str, str]] = set()
        ignored: list[str] = []
        accepted: list[str] = []
        patches: list[SparsePatch] = []
        examined = 0
        history_items_copied = 0

        for event in events:
            examined += 1
            if event.event_id in self._processed_ids:
                ignored.append(event.event_id)
                continue
            if event.kind == "FORUM_OBJECT_SEEN":
                ignored.append(event.event_id)
                continue

            if event.kind in {"EDGE_UPSERT", "EDGE_REMOVE"}:
                edge = Edge.from_mapping(event.payload)
                if event.kind == "EDGE_UPSERT":
                    if not (self._is_active_node(edge.source) or self._is_active_node(edge.target)):
                        ignored.append(event.event_id)
                        continue
                    old = ws.edges.get(edge.triple)
                    if old == edge:
                        ignored.append(event.event_id)
                        continue
                    if old is None:
                        self._inc_edge(edge)
                    else:
                        self._ensure_index(edge.source)
                        self._ensure_index(edge.target)
                    ws.edges[edge.triple] = edge
                    op = "SET"
                else:
                    old = ws.edges.get(edge.triple)
                    if old is None:
                        ignored.append(event.event_id)
                        continue
                    self._ensure_index(old.source)
                    self._ensure_index(old.target)
                    del ws.edges[edge.triple]
                    self._dec_edge(old)
                    edge = old
                    op = "REMOVE"

                affected_edges.add(edge.triple)
                affected_nodes.update((edge.source, edge.target))
                accepted.append(event.event_id)
                patches.append(SparsePatch(
                    event_id=event.event_id,
                    op=op,
                    relation=edge.relation,
                    source_index=self.node_to_index[edge.source],
                    target_index=self.node_to_index[edge.target],
                    source=edge.source,
                    target=edge.target,
                ))
                continue

            if event.kind == "NODE_STATUS_SET":
                node = str(event.payload.get("node", "")).strip()
                status = str(event.payload.get("status", "")).strip()
                if not node or not status:
                    raise ValueError("NODE_STATUS_SET requires node and status")
                if not self._is_active_node(node):
                    ignored.append(event.event_id)
                    continue
                if ws.node_status.get(node) == status:
                    ignored.append(event.event_id)
                    continue
                ws.node_status[node] = status
                self._ensure_index(node)
                affected_nodes.add(node)
                accepted.append(event.event_id)

        if accepted:
            ws.revision += 1
            history_items_copied = len(ws.processed_events)
            ws.processed_events = tuple((*ws.processed_events, *accepted))
            self._processed_ids.update(accepted)

        return RuntimeDelta(
            workspace=ws,
            affected_nodes=tuple(sorted(affected_nodes)),
            affected_edges=tuple(sorted(affected_edges)),
            ignored_events=tuple(ignored),
            sparse_patches=tuple(patches),
            examined_events=examined,
            mutations=len(accepted),
            history_items_copied=history_items_copied,
            history_items_appended=len(accepted),
        )

    def sparse_planes(self) -> dict[str, Any]:
        """Full materialization on demand, using stable runtime indices."""
        relations: dict[str, list[list[float | int]]] = {}
        for key in sorted(self.workspace.edges):
            edge = self.workspace.edges[key]
            relations.setdefault(edge.relation, []).append([
                self.node_to_index[edge.source],
                self.node_to_index[edge.target],
                1.0,
            ])
        return {
            "nodes": list(self.index_to_node),
            "shape": [self.index_capacity, self.index_capacity],
            "relations": {k: relations[k] for k in sorted(relations)},
        }
