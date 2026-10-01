#!/usr/bin/env python3
from __future__ import annotations

from active_memory import MemoryEvent, apply_delta, compile_workspace
from psi_viz_projection import LayoutSpec, VisualContract, classify_transition, compile_visual_frame


CONTRACT = {
    "status": "COMPILED",
    "contract_id": "PSI-VIZ-F4.0-SOURCE-01",
    "anchor": "Y",
    "task": "preserve typed fibre/quotient relations across visual layouts",
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


def visual_contract(ws, *, visible=("provenance", "status"), visual_id="PSI-VIZ-F4.0-01"):
    return VisualContract(
        visual_contract_id=visual_id,
        source_contract_id=ws.contract_id,
        source_contract_digest=ws.contract_digest,
        source_revision=ws.revision,
        source_state_digest=ws.state_digest,
        task_id="EXACT-TASK-DECIDABILITY-DEMO",
        visible_metadata=tuple(visible),
        channel_meanings=(
            ("color", "stable object/type identity; never inferred from screen position"),
            ("symbol", "typed mathematical role"),
            ("position", "layout only in F4.0; no metric semantics"),
            ("motion", "declared transition kind; REPOSITION is layout-only"),
            ("line_style", "typed relation class"),
        ),
    )


def main() -> None:
    ws = compile_workspace(CONTRACT, RETRIEVAL)
    assert ws.revision == 0

    by_fibre = LayoutSpec(
        "FIBRE_LAYOUT",
        {
            "Y": (0.0, 2.5),
            "x1": (-1.2, 1.0),
            "x2": (1.2, 1.0),
            "m": (0.0, -0.8),
        },
    )
    by_quotient = LayoutSpec(
        "QUOTIENT_LAYOUT",
        {
            "Y": (-2.2, 0.0),
            "x1": (-0.6, 1.2),
            "x2": (-0.6, -1.2),
            "m": (1.7, 0.0),
        },
    )

    vc = visual_contract(ws)
    frame_a = compile_visual_frame(ws, vc, by_fibre)
    frame_b = compile_visual_frame(ws, vc, by_quotient)

    # Same authoritative revision + same visual semantics, different geometry.
    assert frame_a.source_state_digest == ws.state_digest
    assert frame_b.source_state_digest == ws.state_digest
    assert frame_a.semantic_digest == frame_b.semantic_digest
    assert frame_a.layout_digest != frame_b.layout_digest
    assert frame_a.semantic_payload["edges"] == frame_b.semantic_payload["edges"]
    assert frame_a.semantic_payload["node_status"] == frame_b.semantic_payload["node_status"]

    reposition = classify_transition(frame_a, frame_b, "REPOSITION")
    assert reposition == {
        "declared_motion": "REPOSITION",
        "semantic_changed": False,
        "layout_changed": True,
        "legal": True,
        "reason": "LAYOUT_ONLY",
    }

    # Repositioning cannot masquerade as a semantic event.
    false_edge_add = classify_transition(frame_a, frame_b, "EDGE_ADD")
    assert not false_edge_add["legal"]
    assert false_edge_add["reason"] == "SEMANTIC_MOTION_WITHOUT_SEMANTIC_CHANGE"

    # Source binding is exact: an old visual contract cannot silently render a
    # new memory revision.
    event = MemoryEvent(
        event_id="viz:f4:separate:x2",
        kind="EDGE_UPSERT",
        event_time="2026-09-30T18:15:00Z",
        ingest_time="2026-09-30T18:15:00.001000Z",
        payload={
            "from": "x2",
            "relation": "SEPARATED_BY_OBSERVATION",
            "to": "x2'",
            "source": "source:separating-observation",
            "status": "ADMITTED",
        },
    )
    ws2 = apply_delta(ws, (event,)).workspace
    assert ws2.revision == 1
    try:
        compile_visual_frame(
            ws2,
            vc,
            LayoutSpec(
                "ILLEGAL_STALE_BINDING",
                {"Y": (0, 2), "x1": (-1, 1), "x2": (1, 1), "m": (0, 0), "x2'": (2, 0)},
            ),
        )
        raise AssertionError("stale visual contract rendered a new memory revision")
    except ValueError as exc:
        assert "revision mismatch" in str(exc) or "state_digest mismatch" in str(exc)

    layout2 = LayoutSpec(
        "POST_OBSERVATION",
        {"Y": (0, 2.5), "x1": (-1.2, 1.0), "x2": (0.8, 1.0), "m": (0, -0.8), "x2'": (2.0, 0.0)},
    )
    frame_c = compile_visual_frame(ws2, visual_contract(ws2, visual_id="PSI-VIZ-F4.0-01:r1"), layout2)
    assert frame_c.semantic_digest != frame_a.semantic_digest
    edge_add = classify_transition(frame_a, frame_c, "EDGE_ADD")
    assert edge_add["legal"]
    assert edge_add["semantic_changed"]

    # A restricted visual contract redacts provenance instead of leaking it.
    restricted = compile_visual_frame(
        ws,
        visual_contract(ws, visible=("status",), visual_id="PSI-VIZ-F4.0-RESTRICTED"),
        by_fibre,
    )
    assert all("provenance" not in row for row in restricted.semantic_payload["edges"])
    assert all("status" in row for row in restricted.semantic_payload["edges"])
    assert restricted.semantic_digest != frame_a.semantic_digest

    # Layout must name exactly the visible node set; silent node disappearance is illegal.
    try:
        compile_visual_frame(
            ws,
            vc,
            LayoutSpec("MISSING_NODE", {"Y": (0, 0), "x1": (1, 0), "m": (0, 1)}),
        )
        raise AssertionError("layout silently dropped a node")
    except ValueError as exc:
        assert "layout node mismatch" in str(exc)

    print("PSI-VIZ-F4.0-01 CONTRACT_PASS")
    print("same_revision_multiple_layouts=PASS")
    print("semantic_digest_layout_invariant=PASS")
    print("reposition_is_layout_only=PASS")
    print("semantic_event_requires_semantic_change=PASS")
    print("exact_source_revision_binding=PASS")
    print("metadata_redaction=PASS")
    print("no_silent_node_drop=PASS")
    print(f"source_state_digest={ws.state_digest}")
    print(f"semantic_digest={frame_a.semantic_digest}")
    print(f"layout_a_digest={frame_a.layout_digest}")
    print(f"layout_b_digest={frame_b.layout_digest}")


if __name__ == "__main__":
    main()
