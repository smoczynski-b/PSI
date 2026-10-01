#!/usr/bin/env python3
from __future__ import annotations

from active_memory import MemoryEvent, apply_delta, compile_workspace
from psi_viz_projection import LayoutSpec, VisualContract, compile_visual_frame
from psi_viz_outputs import OutputProfile, compile_animation_timeline, compile_print_keyframe


CONTRACT = {
    "status": "COMPILED",
    "contract_id": "PSI-VIZ-F4.1-SOURCE-01",
    "anchor": "Y",
    "task": "render one checked PSI-VIZ scene to print and animation outputs",
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

CHANNELS = (
    ("color", "stable object identity"),
    ("symbol", "typed mathematical role"),
    ("position", "layout only; no metric semantics"),
    ("motion", "declared transition kind"),
    ("line_style", "typed relation class"),
)


def vc(ws, *, visible=("provenance", "status"), task="EXACT-TASK-DECIDABILITY-DEMO", suffix="r0"):
    return VisualContract(
        visual_contract_id=f"PSI-VIZ-F4.1-01:{suffix}",
        source_contract_id=ws.contract_id,
        source_contract_digest=ws.contract_digest,
        source_revision=ws.revision,
        source_state_digest=ws.state_digest,
        task_id=task,
        visible_metadata=tuple(visible),
        channel_meanings=CHANNELS,
    )


def fibre_layout():
    return LayoutSpec(
        "FIBRE_LAYOUT",
        {
            "Y": (0.0, 2.5),
            "x1": (-1.2, 1.0),
            "x2": (1.2, 1.0),
            "m": (0.0, -0.8),
        },
    )


def quotient_layout():
    return LayoutSpec(
        "QUOTIENT_LAYOUT",
        {
            "Y": (-2.2, 0.0),
            "x1": (-0.6, 1.2),
            "x2": (-0.6, -1.2),
            "m": (1.7, 0.0),
        },
    )


def main() -> None:
    ws = compile_workspace(CONTRACT, RETRIEVAL)
    frame_a = compile_visual_frame(ws, vc(ws), fibre_layout())
    frame_b = compile_visual_frame(ws, vc(ws), quotient_layout())

    profile = OutputProfile(
        profile_id="BYRNE-PRINT-01",
        paper_width=1600,
        paper_height=1000,
        margin=100,
        node_radius=22,
        font_family="serif",
        background="ivory",
        foreground="black",
        identity_palette=("red", "blue", "gold", "black"),
    )

    # The print packet is derived only from the already checked VisualFrame.
    print_a = compile_print_keyframe(frame_a, profile)
    print_b = compile_print_keyframe(frame_b, profile)
    assert print_a.source_semantic_digest == frame_a.semantic_digest
    assert print_a.source_layout_digest == frame_a.layout_digest
    assert print_a.payload["vector_safe"] is True
    assert print_a.payload["gradients"] is False
    assert print_a.payload["source"]["source_state_digest"] == ws.state_digest
    assert len(print_a.payload["nodes"]) == len(ws.nodes)
    assert len(print_a.payload["edges"]) == len(ws.edges)

    # Stable graphic identity survives layout change; coordinates may change.
    ids_a = {row["object_id"]: row["asset_id"] for row in print_a.payload["nodes"]}
    ids_b = {row["object_id"]: row["asset_id"] for row in print_b.payload["nodes"]}
    assert ids_a == ids_b
    assert print_a.payload_digest != print_b.payload_digest

    # The same two checked frames produce a renderer-neutral Manim timeline.
    timeline = compile_animation_timeline(frame_a, frame_b, "REPOSITION", duration_seconds=1.5)
    assert timeline.source_semantic_digest == timeline.target_semantic_digest == frame_a.semantic_digest
    assert timeline.from_layout_digest != timeline.to_layout_digest
    assert timeline.payload["renderer_target"] == "MANIM_ADAPTER"
    assert timeline.payload["transition"]["reason"] == "LAYOUT_ONLY"
    assert timeline.payload["commands"]
    assert all(row["kind"] == "MOVE_NODE" for row in timeline.payload["commands"])
    assert all(row["asset_id"] == ids_a[row["object_id"]] for row in timeline.payload["commands"])

    # A real source-state change can be represented only after a new checked frame exists.
    event = MemoryEvent(
        event_id="viz:f4.1:separate:x2",
        kind="EDGE_UPSERT",
        event_time="2026-09-30T18:30:00Z",
        ingest_time="2026-09-30T18:30:00.001000Z",
        payload={
            "from": "x2",
            "relation": "SEPARATED_BY_OBSERVATION",
            "to": "x2'",
            "source": "source:separating-observation",
            "status": "ADMITTED",
        },
    )
    ws2 = apply_delta(ws, (event,)).workspace
    frame_c = compile_visual_frame(
        ws2,
        vc(ws2, suffix="r1"),
        LayoutSpec(
            "POST_OBSERVATION",
            {"Y": (0, 2.5), "x1": (-1.2, 1), "x2": (0.8, 1), "m": (0, -0.8), "x2'": (2, 0)},
        ),
    )
    semantic_timeline = compile_animation_timeline(frame_a, frame_c, "EDGE_ADD", duration_seconds=2.0)
    assert semantic_timeline.source_semantic_digest != semantic_timeline.target_semantic_digest
    assert semantic_timeline.payload["commands"] == [{
        "kind": "SEMANTIC_EVENT",
        "declared_motion": "EDGE_ADD",
        "from_semantic_digest": frame_a.semantic_digest,
        "to_semantic_digest": frame_c.semantic_digest,
        "t0": 0.0,
        "t1": 2.0,
    }]

    # A renderer may not turn a change of task or visibility contract into a fake semantic event.
    changed_task = compile_visual_frame(
        ws2,
        vc(ws2, task="OTHER-TASK", suffix="other-task"),
        frame_c_layout := LayoutSpec(
            "POST_OBSERVATION_2",
            {"Y": (0, 2.5), "x1": (-1.2, 1), "x2": (0.8, 1), "m": (0, -0.8), "x2'": (2, 0)},
        ),
    )
    try:
        compile_animation_timeline(frame_a, changed_task, "EDGE_ADD")
        raise AssertionError("task change masqueraded as semantic animation")
    except ValueError as exc:
        assert "task_id" in str(exc)

    changed_visibility = compile_visual_frame(
        ws2,
        vc(ws2, visible=("status",), suffix="restricted"),
        frame_c_layout,
    )
    try:
        compile_animation_timeline(frame_a, changed_visibility, "EDGE_ADD")
        raise AssertionError("visibility-contract change masqueraded as semantic animation")
    except ValueError as exc:
        assert "visible_metadata" in str(exc)

    # Redaction already performed in F4.0 survives print compilation. No renderer-side leak.
    restricted_base = compile_visual_frame(ws, vc(ws, visible=("status",), suffix="restricted-base"), fibre_layout())
    restricted_print = compile_print_keyframe(restricted_base, profile)
    assert all("provenance" not in row for row in restricted_print.payload["edges"])
    assert all("status" in row for row in restricted_print.payload["edges"])

    print("PSI-VIZ-F4.1-01 PASS_WITH_BOUNDARY")
    print("one_visual_frame_to_print_packet=PASS")
    print("same_scene_to_animation_timeline=PASS")
    print("stable_asset_identity_across_layouts=PASS")
    print("semantic_event_requires_checked_target_frame=PASS")
    print("renderer_cannot_change_task_or_visibility_contract=PASS")
    print("redaction_survives_output_compilation=PASS")
    print("actual_svg_pdf_manim_rendering=NOT_IMPLEMENTED")
    print(f"semantic_digest={frame_a.semantic_digest}")
    print(f"print_digest={print_a.payload_digest}")
    print(f"timeline_digest={timeline.payload_digest}")


if __name__ == "__main__":
    main()
