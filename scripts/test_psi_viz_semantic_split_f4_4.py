#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from active_memory import MemoryEvent, apply_delta, compile_workspace
from psi_viz_outputs import OutputProfile, compile_animation_timeline, compile_print_keyframe
from psi_viz_projection import LayoutSpec, VisualContract, compile_visual_frame
from psi_viz_renderer import render_svg
from psi_viz_split_adapter import (
    SplitEventSpec,
    compile_executable_split_scene,
    compile_split_timeline,
    verify_split_timeline,
)


CONTRACT = {
    "status": "COMPILED",
    "contract_id": "PSI-VIZ-F4.4-SOURCE-01",
    "anchor": "Y",
    "task": "typed semantic SPLIT witness",
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

RELATION_TYPES = (
    ("COMPATIBLE_WITH", "DIRECTED"),
    ("TASK_EQUIV", "DIRECTED"),
    ("SEPARATED_BY_OBSERVATION", "DIRECTED"),
    ("UNRELATED", "DIRECTED"),
)

PROFILE = OutputProfile(
    "PSI-BYRNE-F4.4-01",
    paper_width=1200,
    paper_height=760,
    margin=88,
    node_radius=26,
    font_family="serif",
    background="ivory",
    foreground="black",
    identity_palette=("red", "blue", "gold", "black"),
)


def vcontract(ws):
    return VisualContract(
        visual_contract_id="PSI-VIZ-F4.4-01",
        source_contract_id=ws.contract_id,
        source_contract_digest=ws.contract_digest,
        source_revision=ws.revision,
        source_state_digest=ws.state_digest,
        task_id="SEMANTIC-SPLIT-F4.4",
        visible_metadata=(),
        channel_meanings=(
            ("color", "stable object identity"),
            ("position", "layout only except explicit semantic adapter target"),
            ("motion", "declared typed semantic transition"),
            ("line_style", "typed relation semantics"),
        ),
        relation_semantics=RELATION_TYPES,
    )


def expect_reject(fn, marker: str) -> None:
    try:
        fn()
        raise AssertionError(marker)
    except ValueError:
        pass


def main() -> None:
    ws0 = compile_workspace(CONTRACT, RETRIEVAL)
    base_positions = {"Y": (0, 2.5), "x1": (-1.2, 1), "x2": (1.2, 1), "m": (0, -0.8)}
    f0 = compile_visual_frame(ws0, vcontract(ws0), LayoutSpec("BEFORE", base_positions))

    # Separating witness from the PSI-VIZ lineage: x2 survives, while one new
    # distinguishable object x2' and one directed separating relation appear.
    separating = MemoryEvent(
        event_id="viz:f4.4:separate:x2",
        kind="EDGE_UPSERT",
        event_time="2026-10-01T00:11:00Z",
        ingest_time="2026-10-01T00:11:00.001000Z",
        payload={
            "from": "x2",
            "relation": "SEPARATED_BY_OBSERVATION",
            "to": "x2'",
            "source": "source:separating-observation",
            "status": "ADMITTED",
        },
    )
    ws1 = apply_delta(ws0, (separating,)).workspace
    after_positions = dict(base_positions)
    after_positions["x2'"] = (2.5, 0.0)
    f1 = compile_visual_frame(ws1, vcontract(ws1), LayoutSpec("AFTER_SPLIT", after_positions))

    assert ws1.revision == ws0.revision + 1
    assert f0.source_state_digest != f1.source_state_digest
    assert f0.semantic_digest != f1.semantic_digest

    # Generic semantic-transition machinery has no right to call an arbitrary
    # digest change SPLIT. SPLIT is owned by the typed adapter below.
    expect_reject(
        lambda: compile_animation_timeline(f0, f1, "SPLIT", duration_seconds=0.8),
        "generic semantic change was incorrectly accepted as SPLIT",
    )

    # Counterexample: a different semantic delta is also not silently upgraded
    # to SPLIT by the generic API.
    unrelated = MemoryEvent(
        event_id="viz:f4.4:unrelated",
        kind="EDGE_UPSERT",
        event_time="2026-10-01T00:10:00Z",
        ingest_time="2026-10-01T00:10:00.001000Z",
        payload={
            "from": "x1",
            "relation": "UNRELATED",
            "to": "z",
            "source": "source:unrelated",
            "status": "ADMITTED",
        },
    )
    ws_bad = apply_delta(ws0, (unrelated,)).workspace
    bad_positions = dict(base_positions)
    bad_positions["z"] = (-2.2, -0.1)
    f_bad = compile_visual_frame(ws_bad, vcontract(ws_bad), LayoutSpec("UNRELATED_CHANGE", bad_positions))
    expect_reject(
        lambda: compile_animation_timeline(f0, f_bad, "SPLIT", duration_seconds=0.8),
        "unrelated semantic change was incorrectly accepted as SPLIT",
    )

    spec = SplitEventSpec("x2", "x2'", "SEPARATED_BY_OBSERVATION")
    split = compile_split_timeline(f0, f1, spec, duration_seconds=0.9)
    verify_split_timeline(split)
    assert split.payload["declared_motion"] == "SPLIT"
    assert split.payload["reason"] == "TYPED_SPLIT_VISIBLE"
    assert split.payload["split"]["relation_semantics"] == "DIRECTED"
    assert split.source_semantic_digest == f0.semantic_digest
    assert split.target_semantic_digest == f1.semantic_digest

    # Exact typed binding: wrong source/new/relation cannot be substituted.
    expect_reject(
        lambda: compile_split_timeline(f0, f1, SplitEventSpec("x1", "x2'", "SEPARATED_BY_OBSERVATION")),
        "wrong split source accepted",
    )
    expect_reject(
        lambda: compile_split_timeline(f0, f1, SplitEventSpec("x2", "x2'", "UNRELATED")),
        "wrong separating relation accepted",
    )
    expect_reject(
        lambda: compile_split_timeline(f0, f1, SplitEventSpec("x2", "ghost", "SEPARATED_BY_OBSERVATION")),
        "wrong new object accepted",
    )

    # SPLIT may add its new target position, but cannot move an old object too.
    mixed_positions = dict(after_positions)
    mixed_positions["x1"] = (-2.0, 1.0)
    f_mixed = compile_visual_frame(ws1, vcontract(ws1), LayoutSpec("SPLIT_PLUS_REPOSITION", mixed_positions))
    expect_reject(
        lambda: compile_split_timeline(f0, f_mixed, spec),
        "SPLIT smuggled REPOSITION of an existing object",
    )

    scene = compile_executable_split_scene(f0, f1, spec, split, class_name="PSIVizSplit")
    assert "class PSIVizSplit(Scene):" in scene.source
    assert "Workspace" not in scene.source
    assert "SEPARATED_BY_OBSERVATION" in scene.source
    assert "split_new.animate.move_to" in scene.source
    assert "Arrow(" in scene.source

    before_keyframe = compile_print_keyframe(f0, PROFILE)
    after_keyframe = compile_print_keyframe(f1, PROFILE)
    before_svg = render_svg(before_keyframe)
    after_svg = render_svg(after_keyframe)
    assert before_svg.svg_digest != after_svg.svg_digest
    assert "x2&#x27;" not in before_svg.svg
    assert "x2&#x27;" in after_svg.svg
    assert 'data-relation="SEPARATED_BY_OBSERVATION"' in after_svg.svg
    assert 'data-relation-semantics="DIRECTED"' in after_svg.svg

    out = Path("build/psi-viz-f4.4")
    out.mkdir(parents=True, exist_ok=True)
    (out / "before.svg").write_text(before_svg.svg, encoding="utf-8")
    (out / "after.svg").write_text(after_svg.svg, encoding="utf-8")
    (out / "split-scene.py").write_text(scene.source, encoding="utf-8")
    (out / "split-timeline.json").write_text(
        json.dumps(split.as_dict(), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out / "manifest.json").write_text(
        json.dumps(
            {
                "from_revision": f0.source_revision,
                "to_revision": f1.source_revision,
                "from_state_digest": f0.source_state_digest,
                "to_state_digest": f1.source_state_digest,
                "from_semantic_digest": f0.semantic_digest,
                "to_semantic_digest": f1.semantic_digest,
                "split_timeline_digest": split.payload_digest,
                "scene_source_digest": scene.source_digest,
                "before_svg_digest": before_svg.svg_digest,
                "after_svg_digest": after_svg.svg_digest,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        ) + "\n",
        encoding="utf-8",
    )

    print("PSI-VIZ-F4.4-01 PASS_WITH_BOUNDARY")
    print("generic_false_split_fail_closed=PASS")
    print("typed_split_exact_delta=PASS")
    print("split_source_survives=PASS")
    print("split_adds_exactly_one_object_and_relation=PASS")
    print("split_cannot_smuggle_reposition=PASS")
    print("executable_split_scene=PASS")
    print(f"split_timeline_digest={split.payload_digest}")
    print(f"scene_source_digest={scene.source_digest}")


if __name__ == "__main__":
    main()
