#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable, Mapping
from collections import defaultdict
import copy
import hashlib
import json


def _canon(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest(value: Any) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _parse_time(value: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise ValueError("time must be a non-empty ISO-8601 string")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


@dataclass(frozen=True, order=True)
class Edge:
    source: str
    relation: str
    target: str
    provenance: str = ""
    status: str = "ADMITTED"

    @property
    def triple(self) -> tuple[str, str, str]:
        return (self.source, self.relation, self.target)

    @classmethod
    def from_mapping(cls, row: Mapping[str, Any]) -> "Edge":
        source = str(row.get("from", row.get("source_node", ""))).strip()
        relation = str(row.get("relation", "")).strip()
        target = str(row.get("to", row.get("target", ""))).strip()
        if not source or not relation or not target:
            raise ValueError("edge requires source/relation/target")
        provenance = str(row.get("source", row.get("provenance", ""))).strip()
        status = str(row.get("status", row.get("attestation", "ADMITTED"))).strip() or "ADMITTED"
        return cls(source, relation, target, provenance, status)

    def as_dict(self) -> dict[str, str]:
        return {
            "from": self.source,
            "relation": self.relation,
            "to": self.target,
            "provenance": self.provenance,
            "status": self.status,
        }


@dataclass(frozen=True)
class MemoryEvent:
    event_id: str
    kind: str
    event_time: str
    ingest_time: str
    payload: Mapping[str, Any]

    def __post_init__(self):
        if not self.event_id:
            raise ValueError("event_id is required")
        _parse_time(self.event_time)
        _parse_time(self.ingest_time)
        if self.kind not in {
            "EDGE_UPSERT",
            "EDGE_REMOVE",
            "NODE_STATUS_SET",
            "FORUM_OBJECT_SEEN",
        }:
            raise ValueError(f"unsupported event kind: {self.kind}")


@dataclass
class Workspace:
    contract_id: str
    contract_digest: str
    anchor: str
    edges: dict[tuple[str, str, str], Edge] = field(default_factory=dict)
    node_status: dict[str, str] = field(default_factory=dict)
    revision: int = 0
    processed_events: tuple[str, ...] = ()

    @property
    def nodes(self) -> set[str]:
        out = {self.anchor}
        out.update(self.node_status)
        for edge in self.edges.values():
            out.add(edge.source)
            out.add(edge.target)
        return out

    @property
    def dependencies(self) -> set[str]:
        deps = {f"contract:{self.contract_digest}"}
        for edge in self.edges.values():
            deps.add(f"edge:{edge.source}|{edge.relation}|{edge.target}")
            if edge.provenance:
                deps.add(f"source:{edge.provenance}")
        return deps

    def canonical_state(self) -> dict[str, Any]:
        return {
            "contract_id": self.contract_id,
            "contract_digest": self.contract_digest,
            "anchor": self.anchor,
            "revision": self.revision,
            "node_status": dict(sorted(self.node_status.items())),
            "edges": [self.edges[k].as_dict() for k in sorted(self.edges)],
            "processed_events": list(self.processed_events),
        }

    @property
    def state_digest(self) -> str:
        return _digest(self.canonical_state())


@dataclass(frozen=True)
class DeltaResult:
    workspace: Workspace
    affected_nodes: tuple[str, ...]
    affected_edges: tuple[tuple[str, str, str], ...]
    ignored_events: tuple[str, ...]


def compile_workspace(contract: Mapping[str, Any], retrieval: Mapping[str, Any]) -> Workspace:
    if contract.get("status") != "COMPILED":
        raise ValueError("workspace requires a COMPILED contract")
    if retrieval.get("status") != "RETRIEVED":
        raise ValueError("workspace requires a RETRIEVED memory view")
    anchor = str(retrieval.get("anchor") or contract.get("anchor") or "").strip()
    if not anchor:
        raise ValueError("workspace requires an anchor")
    contract_id = str(contract.get("contract_id") or contract.get("task_id") or _digest(contract)[:16])
    ws = Workspace(contract_id=contract_id, contract_digest=_digest(contract), anchor=anchor)
    for row in retrieval.get("edges", []):
        edge = Edge.from_mapping(row)
        ws.edges[edge.triple] = edge
    return ws


def _touches_workspace(ws: Workspace, edge: Edge) -> bool:
    nodes = ws.nodes
    return edge.source in nodes or edge.target in nodes


def apply_delta(workspace: Workspace, events: Iterable[MemoryEvent]) -> DeltaResult:
    ws = copy.deepcopy(workspace)
    affected_nodes: set[str] = set()
    affected_edges: set[tuple[str, str, str]] = set()
    ignored: list[str] = []
    accepted_event_ids: list[str] = []

    for event in events:
        if event.event_id in ws.processed_events:
            ignored.append(event.event_id)
            continue

        if event.kind == "FORUM_OBJECT_SEEN":
            # Observation of a FORUM object is not itself a semantic admission.
            ignored.append(event.event_id)
            continue

        if event.kind in {"EDGE_UPSERT", "EDGE_REMOVE"}:
            edge = Edge.from_mapping(event.payload)
            if event.kind == "EDGE_UPSERT":
                if not _touches_workspace(ws, edge):
                    ignored.append(event.event_id)
                    continue
                old = ws.edges.get(edge.triple)
                if old == edge:
                    ignored.append(event.event_id)
                    continue
                ws.edges[edge.triple] = edge
                affected_edges.add(edge.triple)
                affected_nodes.update((edge.source, edge.target))
                accepted_event_ids.append(event.event_id)
            else:
                if edge.triple not in ws.edges:
                    ignored.append(event.event_id)
                    continue
                del ws.edges[edge.triple]
                affected_edges.add(edge.triple)
                affected_nodes.update((edge.source, edge.target))
                accepted_event_ids.append(event.event_id)

        elif event.kind == "NODE_STATUS_SET":
            node = str(event.payload.get("node", "")).strip()
            status = str(event.payload.get("status", "")).strip()
            if not node or not status:
                raise ValueError("NODE_STATUS_SET requires node and status")
            if node not in ws.nodes:
                ignored.append(event.event_id)
                continue
            if ws.node_status.get(node) == status:
                ignored.append(event.event_id)
                continue
            ws.node_status[node] = status
            affected_nodes.add(node)
            accepted_event_ids.append(event.event_id)

    if accepted_event_ids:
        ws.revision += 1
        ws.processed_events = tuple((*ws.processed_events, *accepted_event_ids))

    return DeltaResult(
        workspace=ws,
        affected_nodes=tuple(sorted(affected_nodes)),
        affected_edges=tuple(sorted(affected_edges)),
        ignored_events=tuple(ignored),
    )


def compile_sparse_planes(workspace: Workspace) -> dict[str, Any]:
    """Backend-neutral COO-like relation planes, ready for tensor/GPU adapters."""
    nodes = sorted(workspace.nodes)
    index = {node: i for i, node in enumerate(nodes)}
    planes: dict[str, list[list[float | int]]] = defaultdict(list)
    for key in sorted(workspace.edges):
        edge = workspace.edges[key]
        planes[edge.relation].append([index[edge.source], index[edge.target], 1.0])
    return {
        "nodes": nodes,
        "shape": [len(nodes), len(nodes)],
        "relations": {relation: planes[relation] for relation in sorted(planes)},
    }


def consolidate_workspace(workspace: Workspace, status: str = "CANDIDATE") -> dict[str, Any]:
    payload = workspace.canonical_state()
    state_digest = workspace.state_digest
    return {
        "id": f"workspace:{state_digest[:20]}",
        "kind": "WORKSPACE_SNAPSHOT",
        "contract_id": workspace.contract_id,
        "contract_digest": workspace.contract_digest,
        "state_digest": state_digest,
        "dependencies": sorted(workspace.dependencies),
        "status": status,
        "created_at": _iso_now(),
        "payload": payload,
    }


def restore_workspace(record: Mapping[str, Any]) -> Workspace:
    if record.get("kind") != "WORKSPACE_SNAPSHOT":
        raise ValueError("not a workspace snapshot")
    payload = copy.deepcopy(record.get("payload"))
    if not isinstance(payload, dict):
        raise ValueError("snapshot payload missing")
    edges: dict[tuple[str, str, str], Edge] = {}
    for row in payload.get("edges", []):
        edge = Edge.from_mapping(row)
        edges[edge.triple] = edge
    ws = Workspace(
        contract_id=str(payload["contract_id"]),
        contract_digest=str(payload["contract_digest"]),
        anchor=str(payload["anchor"]),
        edges=edges,
        node_status=dict(payload.get("node_status", {})),
        revision=int(payload.get("revision", 0)),
        processed_events=tuple(payload.get("processed_events", [])),
    )
    if ws.state_digest != record.get("state_digest"):
        raise ValueError("snapshot digest mismatch")
    return ws


def snapshot_stale(record: Mapping[str, Any], changed_dependencies: Iterable[str]) -> bool:
    return bool(set(record.get("dependencies", ())) & set(changed_dependencies))


def forum_object_to_event(
    oid: str,
    obj: Mapping[str, Any],
    *,
    event_time: str,
    ingest_time: str | None = None,
) -> MemoryEvent:
    """Translate a FORUM object conservatively.

    Only an explicit RELATION with typed from/relation/to payload becomes an edge
    proposal. Other objects are observations and do not mutate semantic state.
    """
    ingest = ingest_time or event_time
    kind = str(obj.get("kind", "")).strip()
    payload = obj.get("payload", {})
    if kind == "RELATION" and isinstance(payload, Mapping):
        if all(str(payload.get(k, "")).strip() for k in ("from", "relation", "to")):
            return MemoryEvent(
                event_id=f"forum:{oid}",
                kind="EDGE_UPSERT",
                event_time=event_time,
                ingest_time=ingest,
                payload={
                    "from": payload["from"],
                    "relation": payload["relation"],
                    "to": payload["to"],
                    "source": f"forum:{oid}",
                    "status": "FORUM_RELATION",
                },
            )
    return MemoryEvent(
        event_id=f"forum:{oid}",
        kind="FORUM_OBJECT_SEEN",
        event_time=event_time,
        ingest_time=ingest,
        payload={"oid": oid, "kind": kind},
    )
