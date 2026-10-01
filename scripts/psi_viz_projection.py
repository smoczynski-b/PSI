#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping
import hashlib
import json
import math

from active_memory import Workspace


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


VISUAL_CHANNELS = {"color", "symbol", "position", "motion", "line_style", "opacity"}
MOTION_KINDS = {"REPOSITION", "EDGE_ADD", "EDGE_REMOVE", "STATUS_CHANGE", "COLLAPSE"}
RELATION_SEMANTICS = {"DIRECTED", "SYMMETRIC"}


@dataclass(frozen=True)
class VisualContract:
    visual_contract_id: str
    source_contract_id: str
    source_contract_digest: str
    source_revision: int
    source_state_digest: str
    task_id: str
    visible_metadata: tuple[str, ...]
    channel_meanings: tuple[tuple[str, str], ...]
    relation_semantics: tuple[tuple[str, str], ...] = ()

    def __post_init__(self):
        for field in (
            "visual_contract_id",
            "source_contract_id",
            "source_contract_digest",
            "source_state_digest",
            "task_id",
        ):
            value = str(getattr(self, field)).strip()
            if not value:
                raise ValueError(f"{field} is required")
            object.__setattr__(self, field, value)
        if isinstance(self.source_revision, bool) or int(self.source_revision) < 0:
            raise ValueError("source_revision must be a non-negative integer")
        object.__setattr__(self, "source_revision", int(self.source_revision))
        visible = tuple(sorted({str(x).strip() for x in self.visible_metadata if str(x).strip()}))
        illegal = set(visible) - {"provenance", "status"}
        if illegal:
            raise ValueError(f"unsupported visible metadata: {sorted(illegal)}")
        object.__setattr__(self, "visible_metadata", visible)
        meanings = tuple((str(k).strip(), str(v).strip()) for k, v in self.channel_meanings)
        if not meanings or any(not k or not v for k, v in meanings):
            raise ValueError("channel_meanings must be non-empty")
        keys = [k for k, _ in meanings]
        if len(set(keys)) != len(keys):
            raise ValueError("duplicate visual channel")
        illegal_channels = set(keys) - VISUAL_CHANNELS
        if illegal_channels:
            raise ValueError(f"unsupported visual channels: {sorted(illegal_channels)}")
        object.__setattr__(self, "channel_meanings", tuple(sorted(meanings)))

        typed = tuple((str(name).strip(), str(kind).strip().upper()) for name, kind in self.relation_semantics)
        if any(not name or kind not in RELATION_SEMANTICS for name, kind in typed):
            raise ValueError("relation_semantics entries require relation -> DIRECTED|SYMMETRIC")
        names = [name for name, _ in typed]
        if len(set(names)) != len(names):
            raise ValueError("duplicate relation_semantics declaration")
        object.__setattr__(self, "relation_semantics", tuple(sorted(typed)))

    def relation_kind(self, relation: str) -> str:
        mapping = dict(self.relation_semantics)
        if not mapping:
            # Backward-compatible legacy mode. It carries no direction claim.
            return "UNSPECIFIED"
        key = str(relation)
        if key not in mapping:
            raise ValueError(f"relation semantics missing for visible relation: {key}")
        return mapping[key]

    def verify_source(self, workspace: Workspace) -> None:
        if workspace.contract_id != self.source_contract_id:
            raise ValueError("visual contract/source contract_id mismatch")
        if workspace.contract_digest != self.source_contract_digest:
            raise ValueError("visual contract/source contract_digest mismatch")
        if workspace.revision != self.source_revision:
            raise ValueError("visual contract/source revision mismatch")
        if workspace.state_digest != self.source_state_digest:
            raise ValueError("visual contract/source state_digest mismatch")


@dataclass(frozen=True)
class LayoutSpec:
    layout_id: str
    positions: Mapping[str, tuple[float, float]]

    def __post_init__(self):
        lid = str(self.layout_id).strip()
        if not lid:
            raise ValueError("layout_id is required")
        object.__setattr__(self, "layout_id", lid)
        clean: dict[str, tuple[float, float]] = {}
        for node, pair in self.positions.items():
            nid = str(node).strip()
            if not nid or not isinstance(pair, (tuple, list)) or len(pair) != 2:
                raise ValueError("each layout position requires node -> (x,y)")
            x, y = pair
            if isinstance(x, bool) or isinstance(y, bool):
                raise ValueError("layout coordinates must be finite numbers")
            xf, yf = float(x), float(y)
            if not math.isfinite(xf) or not math.isfinite(yf):
                raise ValueError("layout coordinates must be finite numbers")
            clean[nid] = (xf, yf)
        object.__setattr__(self, "positions", clean)


@dataclass(frozen=True)
class VisualFrame:
    visual_contract_id: str
    task_id: str
    source_state_digest: str
    source_revision: int
    semantic_payload: dict
    semantic_digest: str
    layout_payload: dict
    layout_digest: str

    def as_dict(self) -> dict:
        return {
            "visual_contract_id": self.visual_contract_id,
            "task_id": self.task_id,
            "source_state_digest": self.source_state_digest,
            "source_revision": self.source_revision,
            "semantic_payload": self.semantic_payload,
            "semantic_digest": self.semantic_digest,
            "layout_payload": self.layout_payload,
            "layout_digest": self.layout_digest,
        }


def verify_visual_frame(frame: VisualFrame) -> None:
    """Verify hashes and duplicated source bindings immediately before use.

    This is an integrity/binding check only. A matching digest does not establish
    truth, admission, authorization or provenance authority.
    """
    if not isinstance(frame, VisualFrame):
        raise TypeError("verify_visual_frame requires VisualFrame")
    if _digest(frame.semantic_payload) != frame.semantic_digest:
        raise ValueError("VisualFrame semantic payload/digest mismatch")
    if _digest(frame.layout_payload) != frame.layout_digest:
        raise ValueError("VisualFrame layout payload/digest mismatch")

    semantic = frame.semantic_payload
    try:
        if str(semantic["task_id"]) != frame.task_id:
            raise ValueError("VisualFrame duplicated task_id mismatch")
        if int(semantic["source_revision"]) != frame.source_revision:
            raise ValueError("VisualFrame duplicated source_revision mismatch")
        if str(semantic["source_state_digest"]) != frame.source_state_digest:
            raise ValueError("VisualFrame duplicated source_state_digest mismatch")
        nodes = {str(x) for x in semantic["nodes"]}
        positions = {str(x) for x in frame.layout_payload["positions"]}
        declarations = [(str(k), str(v).upper()) for k, v in semantic.get("relation_semantics", [])]
        if any(v not in RELATION_SEMANTICS for _, v in declarations):
            raise ValueError("VisualFrame invalid relation semantics declaration")
        if len({k for k, _ in declarations}) != len(declarations):
            raise ValueError("VisualFrame duplicate relation semantics declaration")
        relation_map = dict(declarations)
        for row in semantic["edges"]:
            relation = str(row["relation"])
            carried = str(row.get("relation_semantics", ""))
            expected = relation_map.get(relation) if relation_map else "UNSPECIFIED"
            if expected is None:
                raise ValueError("VisualFrame visible relation lacks typed semantics")
            if carried != expected:
                raise ValueError("VisualFrame edge relation semantics mismatch")
    except (KeyError, TypeError, ValueError) as exc:
        if isinstance(exc, ValueError) and (
            str(exc).startswith("VisualFrame duplicated")
            or str(exc).startswith("VisualFrame invalid")
            or str(exc).startswith("VisualFrame duplicate")
            or str(exc).startswith("VisualFrame visible")
            or str(exc).startswith("VisualFrame edge")
        ):
            raise
        raise ValueError("VisualFrame malformed binding payload") from exc
    if nodes != positions:
        raise ValueError("VisualFrame semantic/layout node binding mismatch")


def compile_visual_frame(workspace: Workspace, contract: VisualContract, layout: LayoutSpec) -> VisualFrame:
    if not isinstance(workspace, Workspace):
        raise TypeError("compile_visual_frame requires Workspace")
    contract.verify_source(workspace)
    nodes = sorted(workspace.nodes)
    missing = sorted(set(nodes) - set(layout.positions))
    extra = sorted(set(layout.positions) - set(nodes))
    if missing or extra:
        raise ValueError(f"layout node mismatch: missing={missing}, extra={extra}")

    edges = []
    for key in sorted(workspace.edges):
        edge = workspace.edges[key]
        row = {
            "from": edge.source,
            "relation": edge.relation,
            "to": edge.target,
            "relation_semantics": contract.relation_kind(edge.relation),
        }
        if "provenance" in contract.visible_metadata:
            row["provenance"] = edge.provenance
        if "status" in contract.visible_metadata:
            row["status"] = edge.status
        edges.append(row)

    semantic_payload = {
        "source_contract_id": workspace.contract_id,
        "source_contract_digest": workspace.contract_digest,
        "source_revision": workspace.revision,
        "source_state_digest": workspace.state_digest,
        "task_id": contract.task_id,
        "nodes": nodes,
        "node_status": dict(sorted(workspace.node_status.items())) if "status" in contract.visible_metadata else {},
        "edges": edges,
        "visible_metadata": list(contract.visible_metadata),
        "channel_meanings": [list(x) for x in contract.channel_meanings],
        "relation_semantics": [list(x) for x in contract.relation_semantics],
    }
    layout_payload = {
        "layout_id": layout.layout_id,
        "positions": {node: list(layout.positions[node]) for node in nodes},
    }
    frame = VisualFrame(
        visual_contract_id=contract.visual_contract_id,
        task_id=contract.task_id,
        source_state_digest=workspace.state_digest,
        source_revision=workspace.revision,
        semantic_payload=semantic_payload,
        semantic_digest=_digest(semantic_payload),
        layout_payload=layout_payload,
        layout_digest=_digest(layout_payload),
    )
    verify_visual_frame(frame)
    return frame


def classify_transition(before: VisualFrame, after: VisualFrame, declared_motion: str) -> dict:
    verify_visual_frame(before)
    verify_visual_frame(after)
    motion = str(declared_motion).strip().upper()
    if motion not in MOTION_KINDS:
        raise ValueError("unknown declared_motion")
    semantic_changed = before.semantic_digest != after.semantic_digest
    layout_changed = before.layout_digest != after.layout_digest

    if motion == "REPOSITION":
        legal = (not semantic_changed) and layout_changed
        reason = "LAYOUT_ONLY" if legal else "REPOSITION_MUST_NOT_CHANGE_SEMANTICS"
    else:
        legal = semantic_changed
        reason = "SEMANTIC_EVENT_VISIBLE" if legal else "SEMANTIC_MOTION_WITHOUT_SEMANTIC_CHANGE"
    return {
        "declared_motion": motion,
        "semantic_changed": semantic_changed,
        "layout_changed": layout_changed,
        "legal": legal,
        "reason": reason,
    }
