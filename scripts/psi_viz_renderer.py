#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from html import escape
import hashlib
import json
import math
import re
from typing import Mapping

from psi_viz_outputs import (
    AnimationTimeline,
    PrintKeyframe,
    verify_animation_timeline,
    verify_print_keyframe,
)


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest_payload(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _digest_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _num(value) -> str:
    if isinstance(value, bool):
        raise ValueError("SVG coordinate cannot be boolean")
    out = float(value)
    if not math.isfinite(out):
        raise ValueError("SVG coordinate must be finite")
    text = f"{out:.6f}".rstrip("0").rstrip(".")
    return text or "0"


def _attr(value) -> str:
    return escape(str(value), quote=True)


def _xml_id(asset_id: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9_.-]+", "-", str(asset_id)).strip("-")
    return f"psi-{clean or 'asset'}"


@dataclass(frozen=True)
class SVGRender:
    source_payload_digest: str
    svg: str
    svg_digest: str


@dataclass(frozen=True)
class ManimPlan:
    source_keyframe_digest: str
    source_timeline_digest: str
    payload: dict
    payload_digest: str


class UnsupportedSemanticEvent(RuntimeError):
    pass


def verify_manim_plan(plan: ManimPlan) -> None:
    """Recompute plan payload and verify duplicated source bindings."""
    if not isinstance(plan, ManimPlan):
        raise TypeError("verify_manim_plan requires ManimPlan")
    if _digest_payload(plan.payload) != plan.payload_digest:
        raise ValueError("ManimPlan payload/digest mismatch")
    try:
        if plan.payload["format"] != "PSI-VIZ-MANIM-PLAN-1":
            raise ValueError("unsupported Manim plan format")
        source = plan.payload["source"]
        if str(source["print_payload_digest"]) != plan.source_keyframe_digest:
            raise ValueError("ManimPlan duplicated keyframe digest mismatch")
        if str(source["timeline_payload_digest"]) != plan.source_timeline_digest:
            raise ValueError("ManimPlan duplicated timeline digest mismatch")
        for row in plan.payload["assets"].values():
            if row.get("kind") != "EDGE":
                continue
            semantics = str(row.get("relation_semantics", "UNSPECIFIED"))
            primitive = str(row.get("primitive", "line+text"))
            if semantics == "DIRECTED" and primitive != "arrow+text":
                raise ValueError("ManimPlan directed edge primitive mismatch")
            if semantics in {"SYMMETRIC", "UNSPECIFIED"} and primitive != "line+text":
                raise ValueError("ManimPlan non-directed edge primitive mismatch")
            if semantics not in {"DIRECTED", "SYMMETRIC", "UNSPECIFIED"}:
                raise ValueError("ManimPlan invalid relation semantics")
    except KeyError as exc:
        raise ValueError("ManimPlan missing source binding") from exc


def render_svg(keyframe: PrintKeyframe) -> SVGRender:
    """Render the checked F4.1 print scene to deterministic, vector-only SVG.

    The renderer consumes PrintKeyframe only. It does not know how to fetch a
    Workspace and it never reconstructs metadata absent from the keyframe.
    """
    if not isinstance(keyframe, PrintKeyframe):
        raise TypeError("render_svg requires PrintKeyframe")
    verify_print_keyframe(keyframe)
    payload = keyframe.payload
    if payload.get("format") != "PSI-VIZ-PRINT-SCENE-1":
        raise ValueError("unsupported print scene format")
    if payload.get("vector_safe") is not True or payload.get("gradients") is not False:
        raise ValueError("print scene is not declared vector-safe")

    canvas = payload["canvas"]
    width = _num(canvas["width"])
    height = _num(canvas["height"])
    background = _attr(canvas["background"])
    source = payload["source"]

    metadata = {
        "format": "PSI-VIZ-SVG-1",
        "semantic_digest": keyframe.source_semantic_digest,
        "layout_digest": keyframe.source_layout_digest,
        "profile_id": keyframe.profile_id,
        "print_payload_digest": keyframe.payload_digest,
        "visual_contract_id": source["visual_contract_id"],
        "task_id": source["task_id"],
        "source_revision": source["source_revision"],
        "source_state_digest": source["source_state_digest"],
    }
    meta_text = escape(_canon(metadata))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'  <metadata id="psi-viz-binding">{meta_text}</metadata>',
    ]
    if any(str(row.get("relation_semantics", "UNSPECIFIED")) == "DIRECTED" for row in payload["edges"]):
        lines.extend([
            '  <defs>',
            '    <marker id="psi-arrowhead" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="strokeWidth">',
            '      <path d="M0,0 L8,4 L0,8 Z" fill="context-stroke"/>',
            '    </marker>',
            '  </defs>',
        ])
    lines.extend([
        f'  <rect id="psi-background" x="0" y="0" width="{width}" height="{height}" fill="{background}"/>',
        '  <g id="psi-edges">',
    ])

    for row in sorted(payload["edges"], key=lambda r: str(r["asset_id"])):
        asset = str(row["asset_id"])
        stroke = _attr(row["stroke"])
        relation = _attr(row["relation"])
        semantics = str(row.get("relation_semantics", "UNSPECIFIED"))
        if semantics not in {"DIRECTED", "SYMMETRIC", "UNSPECIFIED"}:
            raise ValueError("unsupported SVG relation semantics")
        label = escape(str(row["label"]))
        x1, y1, x2, y2 = (_num(row[k]) for k in ("x1", "y1", "x2", "y2"))
        mx = _num((float(row["x1"]) + float(row["x2"])) / 2.0)
        my = _num((float(row["y1"]) + float(row["y2"])) / 2.0)
        lines.append(
            f'    <g id="{_xml_id(asset)}" data-asset-id="{_attr(asset)}" data-relation="{relation}" data-relation-semantics="{_attr(semantics)}">'
        )
        marker = ' marker-end="url(#psi-arrowhead)"' if semantics == "DIRECTED" else ""
        lines.append(f'      <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}"{marker}/>')
        lines.append(f'      <text x="{mx}" y="{my}" text-anchor="middle">{label}</text>')
        if "status" in row and str(row["status"]):
            lines.append(f'      <text class="psi-visible-status" x="{mx}" y="{_num(float(my) + 16)}" text-anchor="middle">{escape(str(row["status"]))}</text>')
        if "provenance" in row and str(row["provenance"]):
            lines.append(f'      <text class="psi-visible-provenance" x="{mx}" y="{_num(float(my) + 32)}" text-anchor="middle">{escape(str(row["provenance"]))}</text>')
        lines.append('    </g>')
    lines.append('  </g>')
    lines.append('  <g id="psi-nodes">')

    for row in sorted(payload["nodes"], key=lambda r: str(r["asset_id"])):
        asset = str(row["asset_id"])
        cx, cy, radius = (_num(row[k]) for k in ("cx", "cy", "radius"))
        fill = _attr(row["fill"])
        stroke = _attr(row["stroke"])
        label = escape(str(row["label"]))
        font = _attr(row["font_family"])
        lines.append(f'    <g id="{_xml_id(asset)}" data-asset-id="{_attr(asset)}">')
        lines.append(f'      <circle cx="{cx}" cy="{cy}" r="{radius}" fill="{fill}" stroke="{stroke}"/>')
        lines.append(f'      <text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="middle" font-family="{font}">{label}</text>')
        if str(row.get("status", "")):
            lines.append(f'      <text class="psi-visible-status" x="{cx}" y="{_num(float(cy) + float(radius) + 16)}" text-anchor="middle">{escape(str(row["status"]))}</text>')
        lines.append('    </g>')
    lines.extend(['  </g>', '</svg>', ''])

    svg = "\n".join(lines)
    banned = ("<image", "<filter", "<linearGradient", "<radialGradient", "data:image/")
    if any(token in svg for token in banned):
        raise AssertionError("renderer emitted forbidden raster/filter/gradient content")
    return SVGRender(keyframe.payload_digest, svg, _digest_text(svg))


def compile_manim_plan(
    keyframe: PrintKeyframe,
    timeline: AnimationTimeline,
    *,
    semantic_event_adapters: Mapping[str, str] | None = None,
) -> ManimPlan:
    """Compile F4.1 outputs into a deterministic executable scene plan."""
    if not isinstance(keyframe, PrintKeyframe) or not isinstance(timeline, AnimationTimeline):
        raise TypeError("compile_manim_plan requires PrintKeyframe and AnimationTimeline")
    verify_print_keyframe(keyframe)
    verify_animation_timeline(timeline)
    if keyframe.source_semantic_digest != timeline.source_semantic_digest:
        raise ValueError("keyframe/timeline semantic source mismatch")
    if keyframe.source_layout_digest != timeline.from_layout_digest:
        raise ValueError("keyframe/timeline layout source mismatch")

    explicit = dict(semantic_event_adapters or {})
    assets = {}
    for row in keyframe.payload["nodes"]:
        assets[str(row["asset_id"])] = {
            "kind": "NODE",
            "object_id": row["object_id"],
            "label": row["label"],
            "fill": row["fill"],
            "stroke": row["stroke"],
            "radius": row["radius"],
        }
    for row in keyframe.payload["edges"]:
        assets[str(row["asset_id"])] = {
            "kind": "EDGE",
            "from_object_id": row["from_object_id"],
            "to_object_id": row["to_object_id"],
            "relation": row["relation"],
            "relation_semantics": row.get("relation_semantics", "UNSPECIFIED"),
            "primitive": row.get("primitive", "line+text"),
            "stroke": row["stroke"],
        }

    actions = []
    for command in timeline.payload["commands"]:
        kind = str(command.get("kind", ""))
        if kind == "MOVE_NODE":
            asset_id = str(command["asset_id"])
            if asset_id not in assets or assets[asset_id]["kind"] != "NODE":
                raise ValueError("MOVE_NODE references unknown/non-node asset")
            actions.append({
                "op": "ANIMATE_MOVE_TO",
                "asset_id": asset_id,
                "object_id": command["object_id"],
                "from": list(command["from"]),
                "to": list(command["to"]),
                "t0": float(command["t0"]),
                "t1": float(command["t1"]),
            })
        elif kind == "SEMANTIC_EVENT":
            event = str(command.get("declared_motion", "")).upper()
            adapter = explicit.get(event)
            if not adapter:
                raise UnsupportedSemanticEvent(
                    f"no explicit Manim adapter for semantic event: {event or '<missing>'}"
                )
            actions.append({
                "op": "CALL_SEMANTIC_ADAPTER",
                "adapter": str(adapter),
                "declared_motion": event,
                "from_semantic_digest": command["from_semantic_digest"],
                "to_semantic_digest": command["to_semantic_digest"],
                "t0": float(command["t0"]),
                "t1": float(command["t1"]),
            })
        else:
            raise ValueError(f"unknown timeline command kind: {kind}")

    payload = {
        "format": "PSI-VIZ-MANIM-PLAN-1",
        "renderer": "MANIM",
        "source": {
            "print_payload_digest": keyframe.payload_digest,
            "timeline_payload_digest": timeline.payload_digest,
            "semantic_digest": keyframe.source_semantic_digest,
            "from_layout_digest": keyframe.source_layout_digest,
            "to_layout_digest": timeline.to_layout_digest,
        },
        "assets": {k: assets[k] for k in sorted(assets)},
        "actions": actions,
    }
    plan = ManimPlan(
        keyframe.payload_digest,
        timeline.payload_digest,
        payload,
        _digest_payload(payload),
    )
    verify_manim_plan(plan)
    return plan


def render_manim_python(plan: ManimPlan, class_name: str = "PSIVizScene") -> str:
    """Emit a deterministic Manim Python scene from a checked ManimPlan."""
    if not isinstance(plan, ManimPlan):
        raise TypeError("render_manim_python requires ManimPlan")
    verify_manim_plan(plan)
    if any(action["op"] != "ANIMATE_MOVE_TO" for action in plan.payload["actions"]):
        raise UnsupportedSemanticEvent("generic F4.2 Manim renderer supports MOVE_NODE only")
    cname = re.sub(r"[^A-Za-z0-9_]", "", str(class_name))
    if not cname or cname[0].isdigit():
        raise ValueError("invalid Manim class name")

    moved = {a["asset_id"]: a for a in plan.payload["actions"]}
    nodes = [(aid, row) for aid, row in plan.payload["assets"].items() if row["kind"] == "NODE"]
    missing = sorted(aid for aid, _ in nodes if aid not in moved)
    if missing:
        raise ValueError(f"Manim witness lacks explicit start position for assets: {missing}")

    lines = [
        "from manim import *",
        "",
        f"# PSI-VIZ-MANIM-PLAN digest: {plan.payload_digest}",
        f"class {cname}(Scene):",
        "    def construct(self):",
        "        assets = {}",
        "        scale = 1.0",
    ]
    for aid, row in sorted(nodes):
        action = moved[aid]
        x, y = action["from"]
        label = repr(str(row["label"]))
        fill = repr(str(row["fill"]))
        stroke = repr(str(row["stroke"]))
        var = "a_" + hashlib.sha256(aid.encode("utf-8")).hexdigest()[:12]
        lines.append(f"        {var} = VGroup(Circle(radius=0.28, color={stroke}, fill_color={fill}, fill_opacity=1), Text({label}, font_size=22))")
        lines.append(f"        {var}.move_to([{float(x)!r}*scale, {float(y)!r}*scale, 0])")
        lines.append(f"        assets[{aid!r}] = {var}")
    lines.append("        self.add(*assets.values())")
    for action in plan.payload["actions"]:
        aid = action["asset_id"]
        x, y = action["to"]
        duration = float(action["t1"]) - float(action["t0"])
        lines.append(f"        self.play(assets[{aid!r}].animate.move_to([{float(x)!r}*scale, {float(y)!r}*scale, 0]), run_time={duration!r})")
    lines.append("")
    source = "\n".join(lines)
    compile(source, "<psi-viz-manim>", "exec")
    return source
