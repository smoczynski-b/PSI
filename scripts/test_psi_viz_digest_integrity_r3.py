#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json

from active_memory import compile_workspace
from psi_viz_projection import classify_transition, compile_visual_frame
from psi_viz_outputs import (
    AnimationTimeline,
    OutputProfile,
    PrintKeyframe,
    compile_animation_timeline,
    compile_print_keyframe,
)
from psi_viz_renderer import (
    ManimPlan,
    compile_manim_plan,
    render_manim_python,
    render_svg,
)
from psi_viz_manim_exec import compile_executable_manim_scene
from test_psi_viz_outputs import CONTRACT, RETRIEVAL, fibre_layout, quotient_layout, vc


def canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value) -> str:
    return hashlib.sha256(canon(value).encode("utf-8")).hexdigest()


def profile() -> OutputProfile:
    return OutputProfile(
        profile_id="BYRNE-R3",
        paper_width=1600,
        paper_height=1000,
        margin=100,
        node_radius=22,
        font_family="serif",
        background="ivory",
        foreground="black",
        identity_palette=("red", "blue", "gold", "black"),
    )


def must_reject(name: str, fn, accepted: list[str]) -> None:
    try:
        fn()
    except (ValueError, RuntimeError):
        return
    accepted.append(name)


def main() -> None:
    ws = compile_workspace(CONTRACT, RETRIEVAL)
    frame_a = compile_visual_frame(ws, vc(ws), fibre_layout())
    frame_b = compile_visual_frame(ws, vc(ws), quotient_layout())
    out_profile = profile()
    keyframe = compile_print_keyframe(frame_a, out_profile)
    timeline = compile_animation_timeline(frame_a, frame_b, "REPOSITION", duration_seconds=1.25)
    plan = compile_manim_plan(keyframe, timeline)

    # Control: the unchanged legitimate chain must remain executable.
    assert classify_transition(frame_a, frame_b, "REPOSITION")["legal"] is True
    assert render_svg(keyframe).source_payload_digest == keyframe.payload_digest
    assert render_manim_python(plan)
    assert compile_executable_manim_scene(plan).source_plan_digest == plan.payload_digest

    accepted: list[str] = []

    # A frozen dataclass is not a frozen nested payload. Keep the old digest and
    # mutate data actually consumed downstream.
    stale_semantic = copy.deepcopy(frame_a)
    stale_semantic.semantic_payload["node_status"]["Y"] = "R3-TAMPER"
    must_reject(
        "VisualFrame.semantic_payload -> classify_transition",
        lambda: classify_transition(stale_semantic, frame_b, "REPOSITION"),
        accepted,
    )
    must_reject(
        "VisualFrame.semantic_payload -> compile_print_keyframe",
        lambda: compile_print_keyframe(stale_semantic, out_profile),
        accepted,
    )

    stale_layout = copy.deepcopy(frame_a)
    stale_layout.layout_payload["positions"]["Y"][0] += 0.375
    must_reject(
        "VisualFrame.layout_payload -> compile_animation_timeline",
        lambda: compile_animation_timeline(stale_layout, frame_b, "REPOSITION", duration_seconds=1.25),
        accepted,
    )

    stale_keyframe = copy.deepcopy(keyframe)
    stale_keyframe.payload["nodes"][0]["label"] = "R3-STALE-LABEL"
    must_reject(
        "PrintKeyframe.payload -> render_svg",
        lambda: render_svg(stale_keyframe),
        accepted,
    )
    must_reject(
        "PrintKeyframe.payload -> compile_manim_plan",
        lambda: compile_manim_plan(stale_keyframe, timeline),
        accepted,
    )

    # Hash-correct packet with a contradictory duplicated binding must also fail.
    bad_k_payload = copy.deepcopy(keyframe.payload)
    bad_k_payload["source"]["semantic_digest"] = "R3-OTHER-SEMANTIC"
    bad_keyframe = PrintKeyframe(
        source_semantic_digest=keyframe.source_semantic_digest,
        source_layout_digest=keyframe.source_layout_digest,
        profile_id=keyframe.profile_id,
        payload=bad_k_payload,
        payload_digest=digest(bad_k_payload),
    )
    must_reject(
        "PrintKeyframe duplicated semantic binding",
        lambda: render_svg(bad_keyframe),
        accepted,
    )

    stale_timeline = copy.deepcopy(timeline)
    stale_timeline.payload["commands"][0]["to"][0] += 0.25
    must_reject(
        "AnimationTimeline.payload -> compile_manim_plan",
        lambda: compile_manim_plan(keyframe, stale_timeline),
        accepted,
    )

    bad_t_payload = copy.deepcopy(timeline.payload)
    bad_t_payload["transition"]["declared_motion"] = "EDGE_ADD"
    bad_timeline = AnimationTimeline(
        source_semantic_digest=timeline.source_semantic_digest,
        target_semantic_digest=timeline.target_semantic_digest,
        from_layout_digest=timeline.from_layout_digest,
        to_layout_digest=timeline.to_layout_digest,
        declared_motion=timeline.declared_motion,
        duration_seconds=timeline.duration_seconds,
        payload=bad_t_payload,
        payload_digest=digest(bad_t_payload),
    )
    must_reject(
        "AnimationTimeline duplicated declared_motion binding",
        lambda: compile_manim_plan(keyframe, bad_timeline),
        accepted,
    )

    stale_plan = copy.deepcopy(plan)
    first_asset = sorted(stale_plan.payload["assets"])[0]
    stale_plan.payload["assets"][first_asset]["stroke"] = "magenta"
    must_reject(
        "ManimPlan.payload -> render_manim_python",
        lambda: render_manim_python(stale_plan),
        accepted,
    )
    must_reject(
        "ManimPlan.payload -> compile_executable_manim_scene",
        lambda: compile_executable_manim_scene(stale_plan),
        accepted,
    )

    bad_p_payload = copy.deepcopy(plan.payload)
    bad_p_payload["source"]["print_payload_digest"] = "R3-OTHER-PRINT"
    bad_plan = ManimPlan(
        source_keyframe_digest=plan.source_keyframe_digest,
        source_timeline_digest=plan.source_timeline_digest,
        payload=bad_p_payload,
        payload_digest=digest(bad_p_payload),
    )
    must_reject(
        "ManimPlan duplicated keyframe binding",
        lambda: render_manim_python(bad_plan),
        accepted,
    )

    if accepted:
        raise AssertionError("stale or contradictory visual packets were consumed: " + "; ".join(accepted))

    print("PSI-VIZ-R3-DIGEST-INTEGRITY-01 PASS")
    print("visual_frame_semantic_recompute=PASS")
    print("visual_frame_layout_recompute=PASS")
    print("print_keyframe_payload_recompute=PASS")
    print("timeline_payload_recompute=PASS")
    print("manim_plan_payload_recompute=PASS")
    print("duplicated_binding_consistency=PASS")
    print("valid_f4_chain_preserved=PASS")


if __name__ == "__main__":
    main()
