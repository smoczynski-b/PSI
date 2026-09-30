#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import json

from active_memory import compile_workspace
from psi_viz_outputs import OutputProfile, compile_animation_timeline, compile_print_keyframe
from psi_viz_projection import LayoutSpec, VisualContract, compile_visual_frame
from psi_viz_renderer import compile_manim_plan, render_svg
from psi_viz_manim_exec import UnsupportedTimelineSchedule, compile_executable_manim_scene


CONTRACT = {
    "status": "COMPILED",
    "contract_id": "PSI-VIZ-F4.3-SOURCE-01",
    "anchor": "Y",
    "task": "execute a checked layout-only transition without semantic change",
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


def visual_contract(ws):
    return VisualContract(
        visual_contract_id="PSI-VIZ-F4.3-01",
        source_contract_id=ws.contract_id,
        source_contract_digest=ws.contract_digest,
        source_revision=ws.revision,
        source_state_digest=ws.state_digest,
        task_id="EXACT-TASK-DECIDABILITY-DEMO",
        visible_metadata=("status",),
        channel_meanings=(
            ("color", "stable object/type identity"),
            ("symbol", "typed mathematical role"),
            ("position", "layout only; no metric semantics"),
            ("motion", "declared transition kind"),
            ("line_style", "typed relation class"),
        ),
    )


def payload_digest(payload: dict) -> str:
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


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
    vc = visual_contract(ws)
    frame_a = compile_visual_frame(ws, vc, layout_a)
    frame_b = compile_visual_frame(ws, vc, layout_b)

    assert frame_a.semantic_digest == frame_b.semantic_digest
    assert frame_a.layout_digest != frame_b.layout_digest

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
    key_a = compile_print_keyframe(frame_a, profile)
    key_b = compile_print_keyframe(frame_b, profile)
    svg_a = render_svg(key_a)
    svg_b = render_svg(key_b)

    timeline = compile_animation_timeline(frame_a, frame_b, "REPOSITION", duration_seconds=1.25)
    plan = compile_manim_plan(key_a, timeline)
    scene = compile_executable_manim_scene(plan, class_name="PSIVizReposition")
    scene_again = compile_executable_manim_scene(plan, class_name="PSIVizReposition")

    assert scene.source == scene_again.source
    assert scene.source_digest == scene_again.source_digest
    assert scene.source_plan_digest == plan.payload_digest
    assert "Workspace" not in scene.source
    assert "source:fibre" not in scene.source
    assert "source:quotient" not in scene.source
    assert scene.source.count("always_redraw") == 8
    assert scene.source.count("self.play(") == 1
    assert scene.source.count(".animate.move_to(") == 4
    assert "COMPATIBLE_WITH" in scene.source
    assert "TASK_EQUIV" in scene.source
    assert "run_time=1.25" in scene.source
    assert "def _relation_label" in scene.source
    assert "BackgroundRectangle" in scene.source
    assert "font_size=12" in scene.source
    assert "#FFFFFF" in scene.source

    # Scheduler test is independent of R3 integrity. Recompute the digest after
    # intentionally constructing a hash-consistent but unsupported schedule.
    bad_payload = json.loads(json.dumps(plan.payload))
    bad_payload["actions"][0]["t0"] = 0.1
    from psi_viz_renderer import ManimPlan
    bad_plan = ManimPlan(
        plan.source_keyframe_digest,
        plan.source_timeline_digest,
        bad_payload,
        payload_digest(bad_payload),
    )
    try:
        compile_executable_manim_scene(bad_plan)
        raise AssertionError("non-shared schedule was guessed instead of rejected")
    except UnsupportedTimelineSchedule:
        pass

    out = Path("build/psi-viz-f4.3")
    out.mkdir(parents=True, exist_ok=True)
    (out / "fibre-keyframe.svg").write_text(svg_a.svg, encoding="utf-8")
    (out / "quotient-keyframe.svg").write_text(svg_b.svg, encoding="utf-8")
    (out / "reposition-scene.py").write_text(scene.source, encoding="utf-8")
    (out / "reposition-plan.json").write_text(
        json.dumps(plan.payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out / "manifest.json").write_text(
        json.dumps(
            {
                "class_name": scene.class_name,
                "source_state_digest": ws.state_digest,
                "semantic_digest": frame_a.semantic_digest,
                "from_layout_digest": frame_a.layout_digest,
                "to_layout_digest": frame_b.layout_digest,
                "timeline_payload_digest": timeline.payload_digest,
                "manim_plan_digest": plan.payload_digest,
                "scene_source_digest": scene.source_digest,
                "duration_seconds": 1.25,
                "semantic_change": False,
                "motion": "REPOSITION",
                "visible_edges": 4,
                "visible_nodes": 4,
                "legibility_guard": "contrast+edge-label-background+perpendicular-offset",
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        ) + "\n",
        encoding="utf-8",
    )

    print("PSI-VIZ-F4.3-01 SOURCE_PASS")
    print("semantic_digest_invariant=PASS")
    print("parallel_timeline_execution=PASS")
    print("typed_edges_follow_nodes=PASS")
    print("renderer_has_no_workspace_access=PASS")
    print("projection_redaction_survives_scene_source=PASS")
    print("unsupported_schedule_fail_closed=PASS")
    print("legibility_guards=PASS")
    print(f"scene_source_digest={scene.source_digest}")
    print(f"semantic_digest={frame_a.semantic_digest}")


if __name__ == "__main__":
    main()
