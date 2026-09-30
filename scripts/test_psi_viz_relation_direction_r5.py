#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from active_memory import compile_workspace
from psi_viz_outputs import OutputProfile, compile_animation_timeline, compile_print_keyframe
from psi_viz_projection import LayoutSpec, VisualContract, compile_visual_frame
from psi_viz_renderer import compile_manim_plan, render_svg
from psi_viz_manim_exec import compile_executable_manim_scene


CONTRACT = {
    "status": "COMPILED",
    "contract_id": "PSI-VIZ-R5-SOURCE-01",
    "anchor": "A",
    "task": "R5 typed relation direction witness",
}

PROFILE = OutputProfile(
    "PSI-R5-PRINT-01",
    paper_width=1000,
    paper_height=600,
    margin=90,
    node_radius=24,
    font_family="serif",
    background="ivory",
    foreground="black",
    identity_palette=("red", "blue", "gold", "black"),
)

LAYOUT_A = LayoutSpec("R5-L0", {"A": (-1.0, 0.0), "B": (1.0, 0.0)})
LAYOUT_B = LayoutSpec("R5-L1", {"A": (-1.2, 0.25), "B": (1.2, -0.25)})


def make_workspace(relation: str, source: str, target: str):
    retrieval = {
        "status": "RETRIEVED",
        "anchor": "A",
        "edges": [
            {
                "from": source,
                "relation": relation,
                "to": target,
                "source": "source:r5",
                "status": "ADMITTED",
            }
        ],
    }
    return compile_workspace(CONTRACT, retrieval)


def visual_contract(ws):
    return VisualContract(
        visual_contract_id="PSI-VIZ-R5-01",
        source_contract_id=ws.contract_id,
        source_contract_digest=ws.contract_digest,
        source_revision=ws.revision,
        source_state_digest=ws.state_digest,
        task_id="RELATION-DIRECTION-R5",
        visible_metadata=(),
        channel_meanings=(
            ("color", "stable object identity"),
            ("position", "layout only"),
            ("motion", "declared transition kind"),
            ("line_style", "typed relation semantics"),
        ),
        relation_semantics=(
            ("DEPENDS_ON", "DIRECTED"),
            ("PEER_WITH", "SYMMETRIC"),
        ),
    )


def products(relation: str, source: str, target: str, tag: str):
    ws = make_workspace(relation, source, target)
    vc = visual_contract(ws)
    f0 = compile_visual_frame(ws, vc, LAYOUT_A)
    f1 = compile_visual_frame(ws, vc, LAYOUT_B)
    kf = compile_print_keyframe(f0, PROFILE)
    svg = render_svg(kf)
    tl = compile_animation_timeline(f0, f1, "REPOSITION", duration_seconds=0.4)
    plan = compile_manim_plan(kf, tl)
    scene = compile_executable_manim_scene(plan, class_name=f"R5{tag}")
    return kf, svg, plan, scene


def edge_visual(row: dict) -> tuple:
    return (
        row["asset_id"],
        row["from_object_id"],
        row["to_object_id"],
        row["x1"], row["y1"], row["x2"], row["y2"],
        row["relation"],
        row["relation_semantics"],
        row["primitive"],
    )


def main() -> None:
    dab, svg_dab, plan_dab, scene_dab = products("DEPENDS_ON", "A", "B", "DirectedAB")
    dba, svg_dba, plan_dba, scene_dba = products("DEPENDS_ON", "B", "A", "DirectedBA")
    sab, svg_sab, plan_sab, scene_sab = products("PEER_WITH", "A", "B", "SymmetricAB")
    sba, svg_sba, plan_sba, scene_sba = products("PEER_WITH", "B", "A", "SymmetricBA")

    de_ab = dab.payload["edges"][0]
    de_ba = dba.payload["edges"][0]
    se_ab = sab.payload["edges"][0]
    se_ba = sba.payload["edges"][0]

    # Direction is explicit contract data, not inferred from relation name/geometry.
    assert de_ab["relation_semantics"] == "DIRECTED"
    assert de_ba["relation_semantics"] == "DIRECTED"
    assert se_ab["relation_semantics"] == "SYMMETRIC"
    assert se_ba["relation_semantics"] == "SYMMETRIC"

    # Directed reversal must remain visibly different in both output backends.
    assert 'data-relation-semantics="DIRECTED"' in svg_dab.svg
    assert 'marker-end="url(#psi-arrowhead)"' in svg_dab.svg
    assert 'marker-end="url(#psi-arrowhead)"' in svg_dba.svg
    assert edge_visual(de_ab) != edge_visual(de_ba)
    assert "Arrow(" in scene_dab.source
    assert "Arrow(" in scene_dba.source

    # Symmetric reversal canonicalizes the visible edge: no arrow and same visual row.
    assert edge_visual(se_ab) == edge_visual(se_ba)
    assert 'data-relation-semantics="SYMMETRIC"' in svg_sab.svg
    assert 'marker-end="url(#psi-arrowhead)"' not in svg_sab.svg
    assert 'marker-end="url(#psi-arrowhead)"' not in svg_sba.svg
    assert "Line(" in scene_sab.source and "Arrow(" not in scene_sab.source
    assert "Line(" in scene_sba.source and "Arrow(" not in scene_sba.source

    # The checked Manim plan itself carries typed relation semantics.
    edge_asset_d = next(row for row in plan_dab.payload["assets"].values() if row["kind"] == "EDGE")
    edge_asset_s = next(row for row in plan_sab.payload["assets"].values() if row["kind"] == "EDGE")
    assert edge_asset_d["relation_semantics"] == "DIRECTED"
    assert edge_asset_s["relation_semantics"] == "SYMMETRIC"

    out = Path("build/psi-viz-r5")
    out.mkdir(parents=True, exist_ok=True)
    (out / "directed-ab.svg").write_text(svg_dab.svg, encoding="utf-8")
    (out / "directed-ba.svg").write_text(svg_dba.svg, encoding="utf-8")
    (out / "symmetric-ab.svg").write_text(svg_sab.svg, encoding="utf-8")
    (out / "symmetric-ba.svg").write_text(svg_sba.svg, encoding="utf-8")
    (out / "directed-ab.py").write_text(scene_dab.source, encoding="utf-8")
    (out / "directed-ba.py").write_text(scene_dba.source, encoding="utf-8")
    (out / "symmetric-ab.py").write_text(scene_sab.source, encoding="utf-8")
    (out / "symmetric-ba.py").write_text(scene_sba.source, encoding="utf-8")

    print("PSI-VIZ-R5-RELATION-DIRECTION PASS_WITH_BOUNDARY")
    print("directed_reversal_visible=PASS")
    print("symmetric_reversal_visual_canonicalization=PASS")
    print("relation_semantics_explicit_not_heuristic=PASS")


if __name__ == "__main__":
    main()
