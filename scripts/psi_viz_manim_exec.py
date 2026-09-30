#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
import re

from psi_viz_renderer import ManimPlan


COLOR_MAP = {
    "red": "#C92A2A",
    "blue": "#2457C5",
    "gold": "#D9A520",
    "black": "#111111",
    "ivory": "#F6F0DD",
    "white": "#FFFFFF",
}


class UnsupportedTimelineSchedule(RuntimeError):
    pass


@dataclass(frozen=True)
class ExecutableManimScene:
    source_plan_digest: str
    class_name: str
    source: str
    source_digest: str


def _digest_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _class_name(value: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9_]", "", str(value))
    if not clean or clean[0].isdigit():
        raise ValueError("invalid Manim class name")
    return clean


def _var(prefix: str, token: str) -> str:
    return f"{prefix}_{hashlib.sha256(token.encode('utf-8')).hexdigest()[:12]}"


def _color(token: str) -> str:
    raw = str(token).strip()
    if raw.startswith("#") and len(raw) in {4, 7, 9}:
        return raw
    return COLOR_MAP.get(raw.lower(), "#111111")


def _shared_interval(actions: list[dict]) -> tuple[float, float]:
    if not actions:
        raise UnsupportedTimelineSchedule("F4.3 requires at least one MOVE_NODE action")
    intervals = {(float(a["t0"]), float(a["t1"])) for a in actions}
    if len(intervals) != 1:
        raise UnsupportedTimelineSchedule(
            "F4.3 supports one shared MOVE_NODE interval only; overlapping/sequential schedules require a later typed scheduler"
        )
    t0, t1 = next(iter(intervals))
    if not math.isfinite(t0) or not math.isfinite(t1) or t0 < 0 or t1 <= t0:
        raise UnsupportedTimelineSchedule("invalid MOVE_NODE interval")
    return t0, t1


def compile_executable_manim_scene(
    plan: ManimPlan,
    *,
    class_name: str = "PSIVizReposition",
    background: str = "ivory",
) -> ExecutableManimScene:
    """Compile an F4.2 MOVE_NODE plan into an actually renderable Manim scene.

    F4.3 preserves the checked plan. It renders nodes plus typed relation edges,
    makes edges follow moving nodes, and respects the shared timeline interval by
    executing all MOVE_NODE animations in one parallel ``self.play`` call.
    No semantic event adapter is accepted here.
    """
    if not isinstance(plan, ManimPlan):
        raise TypeError("compile_executable_manim_scene requires ManimPlan")
    cname = _class_name(class_name)
    payload = plan.payload
    if payload.get("format") != "PSI-VIZ-MANIM-PLAN-1":
        raise ValueError("unsupported Manim plan format")

    actions = list(payload.get("actions", []))
    if any(str(a.get("op", "")) != "ANIMATE_MOVE_TO" for a in actions):
        raise UnsupportedTimelineSchedule("F4.3 executable renderer accepts MOVE_NODE plans only")
    t0, t1 = _shared_interval(actions)
    duration = t1 - t0

    assets = payload.get("assets", {})
    nodes = {aid: row for aid, row in assets.items() if row.get("kind") == "NODE"}
    edges = {aid: row for aid, row in assets.items() if row.get("kind") == "EDGE"}
    moved = {str(a["asset_id"]): a for a in actions}
    if set(nodes) != set(moved):
        missing = sorted(set(nodes) - set(moved))
        extra = sorted(set(moved) - set(nodes))
        raise UnsupportedTimelineSchedule(f"explicit node movement mismatch: missing={missing}, extra={extra}")

    object_to_asset: dict[str, str] = {}
    for aid, row in nodes.items():
        oid = str(row["object_id"])
        if oid in object_to_asset:
            raise ValueError(f"duplicate visible object_id: {oid}")
        object_to_asset[oid] = aid

    for aid, row in edges.items():
        src = str(row["from_object_id"])
        dst = str(row["to_object_id"])
        if src not in object_to_asset or dst not in object_to_asset:
            raise ValueError(f"edge {aid} references a node absent from the checked plan")

    lines = [
        "from manim import *",
        "",
        f"# PSI-VIZ-F4.3 source plan digest: {plan.payload_digest}",
        f"class {cname}(Scene):",
        "    def construct(self):",
        f"        self.camera.background_color = {repr(_color(background))}",
        "        nodes = {}",
        "        edges = {}",
    ]

    # Nodes: stable visual identity, explicit initial positions from the checked timeline.
    node_vars: dict[str, str] = {}
    for aid, row in sorted(nodes.items()):
        action = moved[aid]
        x, y = (float(v) for v in action["from"])
        var = _var("node", aid)
        node_vars[aid] = var
        label = repr(str(row["label"]))
        fill = repr(_color(str(row["fill"])))
        stroke = repr(_color(str(row["stroke"])))
        lines.append(
            f"        {var} = VGroup(Circle(radius=0.30, color={stroke}, fill_color={fill}, fill_opacity=1.0), Text({label}, font_size=24, color={stroke}))"
        )
        lines.append(f"        {var}.move_to([{x!r}, {y!r}, 0])")
        lines.append(f"        nodes[{aid!r}] = {var}")

    # Typed relation edges are display objects only. They follow node positions;
    # they do not create or modify any relation in memory.
    edge_vars: dict[str, str] = {}
    for aid, row in sorted(edges.items()):
        src_aid = object_to_asset[str(row["from_object_id"])]
        dst_aid = object_to_asset[str(row["to_object_id"])]
        src_var = node_vars[src_aid]
        dst_var = node_vars[dst_aid]
        group_var = _var("edge", aid)
        edge_vars[aid] = group_var
        relation = repr(str(row["relation"]))
        stroke = repr(_color(str(row["stroke"])))
        line_var = _var("line", aid)
        label_var = _var("label", aid)
        lines.append(
            f"        {line_var} = always_redraw(lambda: Line({src_var}.get_center(), {dst_var}.get_center(), color={stroke}, stroke_width=2.0).set_z_index(-2))"
        )
        lines.append(
            f"        {label_var} = always_redraw(lambda: Text({relation}, font_size=14, color={stroke}).move_to(({src_var}.get_center()+{dst_var}.get_center())/2 + UP*0.16).set_z_index(-1))"
        )
        lines.append(f"        {group_var} = VGroup({line_var}, {label_var})")
        lines.append(f"        edges[{aid!r}] = {group_var}")

    lines.append("        self.add(*edges.values())")
    lines.append("        self.add(*nodes.values())")
    lines.append("        self.wait(0.20)")

    animations = []
    for aid, action in sorted(moved.items()):
        x, y = (float(v) for v in action["to"])
        animations.append(f"nodes[{aid!r}].animate.move_to([{x!r}, {y!r}, 0])")
    lines.append(f"        self.play({', '.join(animations)}, run_time={duration!r})")
    lines.append("        self.wait(0.20)")
    lines.append("")

    source = "\n".join(lines)
    compile(source, "<psi-viz-f4.3-manim>", "exec")
    return ExecutableManimScene(
        source_plan_digest=plan.payload_digest,
        class_name=cname,
        source=source,
        source_digest=_digest_text(source),
    )
