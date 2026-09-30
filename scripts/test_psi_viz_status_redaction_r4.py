#!/usr/bin/env python3
from __future__ import annotations

from active_memory import MemoryEvent, apply_delta, compile_workspace
from psi_viz_projection import LayoutSpec, VisualContract, compile_visual_frame
from psi_viz_outputs import OutputProfile, compile_animation_timeline, compile_print_keyframe
from psi_viz_renderer import compile_manim_plan, render_svg
from psi_viz_manim_exec import compile_executable_manim_scene


CONTRACT = {
    "status": "COMPILED",
    "contract_id": "PSI-VIZ-R4-SOURCE-01",
    "anchor": "Y",
    "task": "verify complete status redaction across the PSI-VIZ projection chain",
}

RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "Y",
    "edges": [
        {
            "from": "Y",
            "relation": "COMPATIBLE_WITH",
            "to": "X",
            "source": "source:r4-witness",
            "status": "ADMITTED",
        }
    ],
}


def visual_contract(ws, *, visible, visual_id):
    return VisualContract(
        visual_contract_id=visual_id,
        source_contract_id=ws.contract_id,
        source_contract_digest=ws.contract_digest,
        source_revision=ws.revision,
        source_state_digest=ws.state_digest,
        task_id="R4-STATUS-REDACTION",
        visible_metadata=tuple(visible),
        channel_meanings=(
            ("color", "stable object identity"),
            ("position", "layout only"),
            ("motion", "declared transition kind"),
            ("line_style", "typed relation class"),
        ),
    )


def assert_token_absent(token: str, value, label: str) -> None:
    if token in str(value):
        raise AssertionError(f"hidden status leaked into {label}: {token}")


def main() -> None:
    ws0 = compile_workspace(CONTRACT, RETRIEVAL)
    ws = apply_delta(
        ws0,
        (
            MemoryEvent(
                event_id="r4:set-x-needs-recheck",
                kind="NODE_STATUS_SET",
                event_time="2026-09-30T20:40:00Z",
                ingest_time="2026-09-30T20:40:00.001000Z",
                payload={"node": "X", "status": "NEEDS_RECHECK"},
            ),
        ),
    ).workspace
    assert ws.node_status["X"] == "NEEDS_RECHECK"

    layout_a = LayoutSpec("R4-A", {"Y": (0.0, 1.0), "X": (0.0, -1.0)})
    layout_b = LayoutSpec("R4-B", {"Y": (-1.0, 0.0), "X": (1.0, 0.0)})
    profile = OutputProfile("R4-PRINT")

    hidden_contract = visual_contract(ws, visible=(), visual_id="PSI-VIZ-R4-HIDDEN")
    hidden_a = compile_visual_frame(ws, hidden_contract, layout_a)
    hidden_b = compile_visual_frame(ws, hidden_contract, layout_b)

    # R4.1: hidden status must be absent at the projection boundary for both nodes and edges.
    assert hidden_a.semantic_payload.get("node_status", {}) == {}
    assert all("status" not in row for row in hidden_a.semantic_payload["edges"])
    assert_token_absent("NEEDS_RECHECK", hidden_a.as_dict(), "VisualFrame")
    assert_token_absent("ADMITTED", hidden_a.as_dict(), "VisualFrame edge status")

    # R4.2: downstream print packet must not reconstruct hidden status.
    hidden_keyframe = compile_print_keyframe(hidden_a, profile)
    assert all(not row.get("status") for row in hidden_keyframe.payload["nodes"])
    assert all("status" not in row for row in hidden_keyframe.payload["edges"])
    assert_token_absent("NEEDS_RECHECK", hidden_keyframe.as_dict(), "PrintKeyframe")
    assert_token_absent("ADMITTED", hidden_keyframe.as_dict(), "PrintKeyframe edge status")

    # R4.3: SVG text/metadata is downstream evidence, not producer-only evidence.
    hidden_svg = render_svg(hidden_keyframe)
    assert_token_absent("NEEDS_RECHECK", hidden_svg.svg, "SVG")
    assert_token_absent("ADMITTED", hidden_svg.svg, "SVG edge status")
    assert "psi-visible-status" not in hidden_svg.svg

    # R4.4: hidden status must not reappear in animation plan or executable source.
    hidden_timeline = compile_animation_timeline(hidden_a, hidden_b, "REPOSITION")
    hidden_plan = compile_manim_plan(hidden_keyframe, hidden_timeline)
    hidden_scene = compile_executable_manim_scene(hidden_plan, class_name="PSIVizR4Hidden")
    assert_token_absent("NEEDS_RECHECK", hidden_plan.payload, "ManimPlan")
    assert_token_absent("ADMITTED", hidden_plan.payload, "ManimPlan edge status")
    assert_token_absent("NEEDS_RECHECK", hidden_scene.source, "executable Manim source")
    assert_token_absent("ADMITTED", hidden_scene.source, "executable Manim edge status")

    # R4.5: the same source state explicitly permits status when the contract says so.
    visible_contract = visual_contract(ws, visible=("status",), visual_id="PSI-VIZ-R4-VISIBLE")
    visible = compile_visual_frame(ws, visible_contract, layout_a)
    assert visible.semantic_payload["node_status"] == {"X": "NEEDS_RECHECK"}
    assert visible.semantic_payload["edges"][0]["status"] == "ADMITTED"

    visible_keyframe = compile_print_keyframe(visible, profile)
    x_rows = [row for row in visible_keyframe.payload["nodes"] if row["object_id"] == "X"]
    assert len(x_rows) == 1 and x_rows[0]["status"] == "NEEDS_RECHECK"
    assert visible_keyframe.payload["edges"][0]["status"] == "ADMITTED"

    visible_svg = render_svg(visible_keyframe)
    assert "NEEDS_RECHECK" in visible_svg.svg
    assert "ADMITTED" in visible_svg.svg
    assert "psi-visible-status" in visible_svg.svg

    # R3 remains operative: all downstream objects above were produced and verified
    # through the existing digest/binding checks after redaction.
    assert hidden_a.semantic_digest != visible.semantic_digest

    print("PSI-VIZ-R4 STATUS_REDACTION_PASS")
    print("hidden_node_status_projection=PASS")
    print("hidden_edge_status_projection=PASS")
    print("hidden_print_packet=PASS")
    print("hidden_svg=PASS")
    print("hidden_manim_plan_and_source=PASS")
    print("explicit_visible_status=PASS")
    print("r3_integrity_after_redaction=PASS")


if __name__ == "__main__":
    main()
