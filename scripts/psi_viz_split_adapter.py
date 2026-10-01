#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
import re

from psi_viz_projection import VisualFrame, verify_visual_frame


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _digest_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _token(value: str, field: str) -> str:
    out = str(value).strip()
    if not out:
        raise ValueError(f"{field} is required")
    return out


@dataclass(frozen=True)
class SplitEventSpec:
    source_object_id: str
    new_object_id: str
    separating_relation: str

    def __post_init__(self):
        source = _token(self.source_object_id, "source_object_id")
        new = _token(self.new_object_id, "new_object_id")
        relation = _token(self.separating_relation, "separating_relation")
        if source == new:
            raise ValueError("SPLIT source and new object must differ")
        object.__setattr__(self, "source_object_id", source)
        object.__setattr__(self, "new_object_id", new)
        object.__setattr__(self, "separating_relation", relation)


@dataclass(frozen=True)
class SplitTimeline:
    source_semantic_digest: str
    target_semantic_digest: str
    source_state_digest: str
    target_state_digest: str
    source_revision: int
    target_revision: int
    from_layout_digest: str
    to_layout_digest: str
    duration_seconds: float
    payload: dict
    payload_digest: str

    def as_dict(self) -> dict:
        return {
            "source_semantic_digest": self.source_semantic_digest,
            "target_semantic_digest": self.target_semantic_digest,
            "source_state_digest": self.source_state_digest,
            "target_state_digest": self.target_state_digest,
            "source_revision": self.source_revision,
            "target_revision": self.target_revision,
            "from_layout_digest": self.from_layout_digest,
            "to_layout_digest": self.to_layout_digest,
            "duration_seconds": self.duration_seconds,
            "payload": self.payload,
            "payload_digest": self.payload_digest,
        }


@dataclass(frozen=True)
class ExecutableSplitScene:
    source_split_digest: str
    class_name: str
    source: str
    source_digest: str


def _edge_key(row: dict) -> str:
    return _canon(row)


def _contract_fields(frame: VisualFrame) -> tuple:
    p = frame.semantic_payload
    return (
        frame.visual_contract_id,
        frame.task_id,
        p.get("source_contract_id"),
        p.get("source_contract_digest"),
        _canon(p.get("visible_metadata", [])),
        _canon(p.get("channel_meanings", [])),
        _canon(p.get("relation_semantics", [])),
    )


def _validate_split(before: VisualFrame, after: VisualFrame, spec: SplitEventSpec) -> dict:
    verify_visual_frame(before)
    verify_visual_frame(after)
    if not isinstance(spec, SplitEventSpec):
        raise TypeError("typed SPLIT requires SplitEventSpec")
    if _contract_fields(before) != _contract_fields(after):
        raise ValueError("SPLIT cannot change visual/task/source contract fields")
    if after.source_revision != before.source_revision + 1:
        raise ValueError("SPLIT requires one exact source revision advance")
    if after.source_state_digest == before.source_state_digest:
        raise ValueError("SPLIT requires a real source state change")
    if after.semantic_digest == before.semantic_digest:
        raise ValueError("SPLIT requires a semantic digest change")

    bnodes = {str(x) for x in before.semantic_payload["nodes"]}
    anodes = {str(x) for x in after.semantic_payload["nodes"]}
    if spec.source_object_id not in bnodes or spec.source_object_id not in anodes:
        raise ValueError("SPLIT source object must survive the transition")
    if spec.new_object_id in bnodes:
        raise ValueError("SPLIT new object already existed before transition")
    if anodes - bnodes != {spec.new_object_id} or bnodes - anodes:
        raise ValueError("SPLIT must add exactly one object and remove none")

    bstatus = before.semantic_payload.get("node_status", {})
    astatus = after.semantic_payload.get("node_status", {})
    for node in bnodes:
        if bstatus.get(node, "") != astatus.get(node, ""):
            raise ValueError("SPLIT cannot change status of pre-existing objects")

    bedges = list(before.semantic_payload["edges"])
    aedges = list(after.semantic_payload["edges"])
    bkeys = {_edge_key(row) for row in bedges}
    akeys = {_edge_key(row) for row in aedges}
    if not bkeys.issubset(akeys):
        raise ValueError("SPLIT cannot remove or rewrite pre-existing relations")
    added = [row for row in aedges if _edge_key(row) not in bkeys]
    if len(added) != 1:
        raise ValueError("SPLIT must add exactly one separating relation")
    edge = added[0]
    expected = {
        "from": spec.source_object_id,
        "relation": spec.separating_relation,
        "to": spec.new_object_id,
        "relation_semantics": "DIRECTED",
    }
    if edge != expected:
        raise ValueError("SPLIT separating relation does not match typed specification")

    relation_map = dict(after.semantic_payload.get("relation_semantics", []))
    if relation_map.get(spec.separating_relation) != "DIRECTED":
        raise ValueError("SPLIT separating relation must be explicitly DIRECTED")

    bpos = before.layout_payload["positions"]
    apos = after.layout_payload["positions"]
    for node in bnodes:
        if list(bpos[node]) != list(apos[node]):
            raise ValueError("SPLIT cannot smuggle REPOSITION of existing objects")
    source_pos = [float(v) for v in bpos[spec.source_object_id]]
    target_pos = [float(v) for v in apos[spec.new_object_id]]
    if source_pos == target_pos:
        raise ValueError("SPLIT target must be visibly separated from source")

    return {
        "before_nodes": sorted(bnodes),
        "after_nodes": sorted(anodes),
        "added_edge": edge,
        "source_position": source_pos,
        "target_position": target_pos,
    }


def compile_split_timeline(
    before: VisualFrame,
    after: VisualFrame,
    spec: SplitEventSpec,
    *,
    duration_seconds: float = 0.9,
) -> SplitTimeline:
    if isinstance(duration_seconds, bool):
        raise ValueError("duration_seconds must be a finite positive number")
    duration = float(duration_seconds)
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("duration_seconds must be a finite positive number")
    witness = _validate_split(before, after, spec)
    payload = {
        "format": "PSI-VIZ-SPLIT-TIMELINE-1",
        "declared_motion": "SPLIT",
        "reason": "TYPED_SPLIT_VISIBLE",
        "source": {
            "from_revision": before.source_revision,
            "to_revision": after.source_revision,
            "from_state_digest": before.source_state_digest,
            "to_state_digest": after.source_state_digest,
            "from_semantic_digest": before.semantic_digest,
            "to_semantic_digest": after.semantic_digest,
            "from_layout_digest": before.layout_digest,
            "to_layout_digest": after.layout_digest,
        },
        "split": {
            "source_object_id": spec.source_object_id,
            "new_object_id": spec.new_object_id,
            "separating_relation": spec.separating_relation,
            "relation_semantics": "DIRECTED",
            "source_position": witness["source_position"],
            "target_position": witness["target_position"],
        },
        "duration_seconds": duration,
    }
    timeline = SplitTimeline(
        source_semantic_digest=before.semantic_digest,
        target_semantic_digest=after.semantic_digest,
        source_state_digest=before.source_state_digest,
        target_state_digest=after.source_state_digest,
        source_revision=before.source_revision,
        target_revision=after.source_revision,
        from_layout_digest=before.layout_digest,
        to_layout_digest=after.layout_digest,
        duration_seconds=duration,
        payload=payload,
        payload_digest=_digest(payload),
    )
    verify_split_timeline(timeline)
    return timeline


def verify_split_timeline(timeline: SplitTimeline) -> None:
    if not isinstance(timeline, SplitTimeline):
        raise TypeError("verify_split_timeline requires SplitTimeline")
    if _digest(timeline.payload) != timeline.payload_digest:
        raise ValueError("SplitTimeline payload/digest mismatch")
    p = timeline.payload
    if p.get("format") != "PSI-VIZ-SPLIT-TIMELINE-1":
        raise ValueError("unsupported SplitTimeline format")
    if p.get("declared_motion") != "SPLIT" or p.get("reason") != "TYPED_SPLIT_VISIBLE":
        raise ValueError("SplitTimeline typed motion binding mismatch")
    source = p.get("source", {})
    expected = (
        int(source.get("from_revision", -1)),
        int(source.get("to_revision", -1)),
        str(source.get("from_state_digest", "")),
        str(source.get("to_state_digest", "")),
        str(source.get("from_semantic_digest", "")),
        str(source.get("to_semantic_digest", "")),
        str(source.get("from_layout_digest", "")),
        str(source.get("to_layout_digest", "")),
        float(p.get("duration_seconds", -1)),
    )
    actual = (
        timeline.source_revision,
        timeline.target_revision,
        timeline.source_state_digest,
        timeline.target_state_digest,
        timeline.source_semantic_digest,
        timeline.target_semantic_digest,
        timeline.from_layout_digest,
        timeline.to_layout_digest,
        timeline.duration_seconds,
    )
    if expected != actual:
        raise ValueError("SplitTimeline duplicated source binding mismatch")
    split = p.get("split", {})
    if split.get("relation_semantics") != "DIRECTED":
        raise ValueError("SplitTimeline must carry DIRECTED separating relation")
    if split.get("source_object_id") == split.get("new_object_id"):
        raise ValueError("SplitTimeline source/new identity collision")


COLORS = ("#C92A2A", "#2457C5", "#D9A520", "#111111")


def _node_color(node: str) -> str:
    idx = int(hashlib.sha256(node.encode("utf-8")).hexdigest()[:8], 16) % len(COLORS)
    return COLORS[idx]


def _label_color(fill: str) -> str:
    r = int(fill[1:3], 16) / 255.0
    g = int(fill[3:5], 16) / 255.0
    b = int(fill[5:7], 16) / 255.0
    return "#FFFFFF" if 0.2126 * r + 0.7152 * g + 0.0722 * b < 0.48 else "#111111"


def _class_name(value: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9_]", "", str(value))
    if not clean or clean[0].isdigit():
        raise ValueError("invalid Manim class name")
    return clean


def compile_executable_split_scene(
    before: VisualFrame,
    after: VisualFrame,
    spec: SplitEventSpec,
    timeline: SplitTimeline,
    *,
    class_name: str = "PSIVizSplit",
) -> ExecutableSplitScene:
    witness = _validate_split(before, after, spec)
    verify_split_timeline(timeline)
    if (
        timeline.source_semantic_digest != before.semantic_digest
        or timeline.target_semantic_digest != after.semantic_digest
        or timeline.source_state_digest != before.source_state_digest
        or timeline.target_state_digest != after.source_state_digest
        or timeline.from_layout_digest != before.layout_digest
        or timeline.to_layout_digest != after.layout_digest
    ):
        raise ValueError("SplitTimeline does not bind the supplied visual frames")
    split_payload = timeline.payload["split"]
    if (
        split_payload["source_object_id"] != spec.source_object_id
        or split_payload["new_object_id"] != spec.new_object_id
        or split_payload["separating_relation"] != spec.separating_relation
    ):
        raise ValueError("SplitTimeline/spec mismatch")

    cname = _class_name(class_name)
    bpos = before.layout_payload["positions"]
    old_edges = list(before.semantic_payload["edges"])
    nodes = sorted(before.semantic_payload["nodes"])
    new_node = spec.new_object_id
    target = witness["target_position"]
    source = spec.source_object_id
    duration = timeline.duration_seconds

    lines = [
        "from manim import *",
        "import numpy as np",
        "",
        "def _relation_label(text, a, b, fg, bg):",
        "    delta = b.get_center() - a.get_center()",
        "    normal = np.array([-delta[1], delta[0], 0.0])",
        "    norm = np.linalg.norm(normal)",
        "    normal = UP if norm < 1e-9 else normal / norm",
        "    label = Text(text, font_size=12, color=fg)",
        "    box = BackgroundRectangle(label, color=bg, fill_opacity=0.92, buff=0.035, stroke_width=0)",
        "    return VGroup(box, label).move_to((a.get_center()+b.get_center())/2 + 0.28*normal)",
        "",
        f"# PSI-VIZ-F4.4 typed SPLIT digest: {timeline.payload_digest}",
        f"class {cname}(Scene):",
        "    def construct(self):",
        "        self.camera.background_color = '#F6F0DD'",
        "        nodes = {}",
    ]

    for node in nodes:
        x, y = (float(v) for v in bpos[node])
        fill = _node_color(node)
        ink = _label_color(fill)
        lines.append(
            f"        nodes[{node!r}] = VGroup(Circle(radius=0.30, color='#111111', fill_color={fill!r}, fill_opacity=1.0), Text({node!r}, font_size=24, color={ink!r})).move_to([{x!r}, {y!r}, 0])"
        )

    lines.append("        old_edges = VGroup()")
    for i, edge in enumerate(old_edges):
        src = str(edge["from"])
        dst = str(edge["to"])
        rel = str(edge["relation"])
        semantics = str(edge.get("relation_semantics", "UNSPECIFIED"))
        connector = "Arrow" if semantics == "DIRECTED" else "Line"
        if connector == "Arrow":
            expr = f"Arrow(nodes[{src!r}].get_center(), nodes[{dst!r}].get_center(), buff=0.30, color='#111111', stroke_width=2.0, max_tip_length_to_length_ratio=0.14)"
        else:
            expr = f"Line(nodes[{src!r}].get_center(), nodes[{dst!r}].get_center(), color='#111111', stroke_width=2.0)"
        lines.append(f"        old_line_{i} = {expr}")
        lines.append(f"        old_label_{i} = _relation_label({rel!r}, nodes[{src!r}], nodes[{dst!r}], '#111111', '#F6F0DD')")
        lines.append(f"        old_edges.add(old_line_{i}, old_label_{i})")

    fill = _node_color(new_node)
    ink = _label_color(fill)
    sx, sy = witness["source_position"]
    tx, ty = target
    lines.extend([
        "        self.add(old_edges, *nodes.values())",
        "        self.wait(0.20)",
        f"        split_new = VGroup(Circle(radius=0.30, color='#111111', fill_color={fill!r}, fill_opacity=1.0), Text({new_node!r}, font_size=24, color={ink!r})).move_to([{sx!r}, {sy!r}, 0]).set_opacity(0.0)",
        "        self.add(split_new)",
        f"        self.play(split_new.animate.move_to([{tx!r}, {ty!r}, 0]).set_opacity(1.0), run_time={duration!r})",
        f"        split_edge = Arrow(nodes[{source!r}].get_center(), split_new.get_center(), buff=0.30, color='#111111', stroke_width=2.4, max_tip_length_to_length_ratio=0.14)",
        f"        split_label = _relation_label({spec.separating_relation!r}, nodes[{source!r}], split_new, '#111111', '#F6F0DD')",
        "        self.play(Create(split_edge), FadeIn(split_label), run_time=0.35)",
        "        self.wait(0.20)",
        "",
    ])
    source_text = "\n".join(lines)
    compile(source_text, "<psi-viz-f4.4-split>", "exec")
    return ExecutableSplitScene(
        source_split_digest=timeline.payload_digest,
        class_name=cname,
        source=source_text,
        source_digest=_digest_text(source_text),
    )
