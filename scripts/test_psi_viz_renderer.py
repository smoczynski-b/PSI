#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import xml.etree.ElementTree as ET

from active_memory import MemoryEvent, apply_delta, compile_workspace
from psi_viz_outputs import OutputProfile, compile_animation_timeline, compile_print_keyframe
from psi_viz_projection import LayoutSpec, VisualContract, compile_visual_frame
from psi_viz_renderer import (
    UnsupportedSemanticEvent,
    compile_manim_plan,
    render_manim_python,
    render_svg,
)


CONTRACT = {
    "status": "COMPILED",
    "contract_id": "PSI-VIZ-F4.2-SOURCE-01",
    "anchor": "Y",
    "task": "render a checked fibre/quotient scene without renderer access to Workspace",
}

RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "Y",
    "edges": [
        {"from": "Y", "relation": "COMPATIBLE_WITH", "to": "x1", "source": "source:fibre", "status": "ADMITTED"},
        {"from": "Y", "relation": "COMPATIBLE_WITH", "to": "x2", "source": "source:fibre", "status": "ADMITTED"},
        {"from": "x1", "relation": "TASK_EQUIV", "to": "m", "source": "source:quotient", "status": "ADMITTED"},
        {"from": "x2", "relation": "TASK_EQUIV", "to": "m", "source": "source:quotient", "status": "ADMITTED"},
    ],
}


def vcontract(ws, visual_id: str):
    return VisualContract(
        visual_contract_id=visual_id,
        source_contract_id=ws.contract_id,
        source_contract_digest=ws.contract_digest,
        source_revision=ws.revision,
        source_state_digest=ws.state_digest,
        task_id="EXACT-TASK-DECIDABILITY-DEMO",
        # Deliberately restricted: provenance must not reappear downstream.
        visible_metadata=("status",),
        channel_meanings=(
            ("color", "stable object/type identity"),
            ("symbol", "typed mathematical role"),
            ("position", "layout only; no metric semantics"),
            ("motion", "declared transition kind"),
            ("line_style", "typed relation class"),
        ),
    )


def main() -> None:
    ws = compile_workspace(CONTRACT, RETRIEVAL)
    layout_a = LayoutSpec(
        "FIBRE_LAYOUT",
        {"Y": (0.0, 2.5), "x1": (-1.2, 1.0), "x2": (1.2, 1.0), "m": (0.0, -0.8)},
    )
    layout_b = LayoutSpec(
        "QUOTIENT_LAYOUT",
        {"Y": (-2.2, 0.0), "x1": (-0.6, 1.2), "x2": (-0.6, -1.2), "m": (1.7, 0.0)},
    )
    vc = vcontract(ws, "PSI-VIZ-F4.2-01")
    frame_a = compile_visual_frame(ws, vc, layout_a)
    frame_b = compile_visual_frame(ws, vc, layout_b)

    profile = OutputProfile(
        "PSI-BYRNE-PRINT-01",
        paper_width=1600,
        paper_height=1000,
        margin=96,
        node_radius=26,
        font_family="serif",
        background="ivory",
        foreground="black",
        identity_palette=("red", "blue", "gold", "black"),
    )
    keyframe = compile_print_keyframe(frame_a, profile)
    svg1 = render_svg(keyframe)
    svg2 = render_svg(keyframe)

    # Real, deterministic SVG.
    assert svg1.svg == svg2.svg
    assert svg1.svg_digest == svg2.svg_digest
    root = ET.fromstring(svg1.svg)
    assert root.tag.endswith("svg")
    metadata = next(child for child in root if child.tag.endswith("metadata"))
    binding = json.loads(metadata.text or "{}")
    assert binding["semantic_digest"] == frame_a.semantic_digest
    assert binding["layout_digest"] == frame_a.layout_digest
    assert binding["profile_id"] == profile.profile_id
    assert binding["print_payload_digest"] == keyframe.payload_digest

    asset_ids = [row["asset_id"] for row in keyframe.payload["nodes"] + keyframe.payload["edges"]]
    for asset_id in asset_ids:
        assert f'data-asset-id="{asset_id}"' in svg1.svg
    for forbidden in ("<image", "<filter", "<linearGradient", "<radialGradient", "data:image/"):
        assert forbidden not in svg1.svg
    assert "source:fibre" not in svg1.svg
    assert "source:quotient" not in svg1.svg
    assert "ADMITTED" in svg1.svg  # status was explicitly visible.

    # Timeline -> deterministic Manim plan -> syntactically executable Python.
    timeline = compile_animation_timeline(frame_a, frame_b, "REPOSITION", duration_seconds=1.25)
    plan = compile_manim_plan(keyframe, timeline)
    source1 = render_manim_python(plan)
    source2 = render_manim_python(plan)
    assert source1 == source2
    assert "from manim import *" in source1
    assert "Workspace" not in source1
    assert "source:fibre" not in source1
    assert all(action["op"] == "ANIMATE_MOVE_TO" for action in plan.payload["actions"])
    assert len(plan.payload["actions"]) == 4

    # A semantic change cannot be guessed by the generic adapter.
    event = MemoryEvent(
        event_id="viz:f4.2:separate:x2",
        kind="EDGE_UPSERT",
        event_time="2026-09-30T18:35:00Z",
        ingest_time="2026-09-30T18:35:00.001000Z",
        payload={
            "from": "x2",
            "relation": "SEPARATED_BY_OBSERVATION",
            "to": "x2'",
            "source": "source:separating-observation",
            "status": "ADMITTED",
        },
    )
    ws2 = apply_delta(ws, (event,)).workspace
    layout_c = LayoutSpec(
        "POST_OBSERVATION",
        {"Y": (0, 2.5), "x1": (-1.2, 1.0), "x2": (0.8, 1.0), "m": (0, -0.8), "x2'": (2.0, 0.0)},
    )
    frame_c = compile_visual_frame(ws2, vcontract(ws2, "PSI-VIZ-F4.2-01:r1"), layout_c)
    semantic_timeline = compile_animation_timeline(frame_a, frame_c, "EDGE_ADD", duration_seconds=0.8)
    try:
        compile_manim_plan(keyframe, semantic_timeline)
        raise AssertionError("semantic event was guessed without explicit adapter")
    except UnsupportedSemanticEvent as exc:
        assert "EDGE_ADD" in str(exc)

    explicit_plan = compile_manim_plan(
        keyframe,
        semantic_timeline,
        semantic_event_adapters={"EDGE_ADD": "psi_edge_add_v1"},
    )
    assert explicit_plan.payload["actions"][0]["op"] == "CALL_SEMANTIC_ADAPTER"
    try:
        render_manim_python(explicit_plan)
        raise AssertionError("generic renderer executed semantic adapter implicitly")
    except UnsupportedSemanticEvent:
        pass

    # Persist real renderer products for CI artifact inspection.
    out = Path("build/psi-viz-f4.2")
    out.mkdir(parents=True, exist_ok=True)
    (out / "fibre-keyframe.svg").write_text(svg1.svg, encoding="utf-8")
    (out / "reposition-scene.py").write_text(source1, encoding="utf-8")
    (out / "reposition-plan.json").write_text(
        json.dumps(plan.payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out / "manifest.json").write_text(
        json.dumps(
            {
                "semantic_digest": frame_a.semantic_digest,
                "layout_digest": frame_a.layout_digest,
                "print_payload_digest": keyframe.payload_digest,
                "svg_digest": svg1.svg_digest,
                "timeline_payload_digest": timeline.payload_digest,
                "manim_plan_digest": plan.payload_digest,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        ) + "\n",
        encoding="utf-8",
    )

    print("PSI-VIZ-F4.2-01 PASS_WITH_BOUNDARY")
    print("real_svg=PASS")
    print("deterministic_svg=PASS")
    print("asset_identity_preserved=PASS")
    print("projection_redaction_survives_svg=PASS")
    print("move_node_manim_adapter=PASS")
    print("unknown_semantic_event_fail_closed=PASS")
    print(f"svg_digest={svg1.svg_digest}")
    print(f"manim_plan_digest={plan.payload_digest}")


if __name__ == "__main__":
    main()
