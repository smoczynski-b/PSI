#!/usr/bin/env python3
from __future__ import annotations

from active_memory import MemoryEvent, apply_delta, compile_workspace
from psi_viz_outputs import compile_animation_timeline
from psi_viz_projection import LayoutSpec, VisualContract, compile_visual_frame


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


def main() -> None:
    ws0 = compile_workspace(CONTRACT, RETRIEVAL)
    f0 = compile_visual_frame(
        ws0,
        vcontract(ws0),
        LayoutSpec("BEFORE", {"Y": (0, 2.5), "x1": (-1.2, 1), "x2": (1.2, 1), "m": (0, -0.8)}),
    )

    # Counterexample: a generic semantic change is NOT a SPLIT.
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
    f_bad = compile_visual_frame(
        ws_bad,
        vcontract(ws_bad),
        LayoutSpec(
            "UNRELATED_CHANGE",
            {"Y": (0, 2.5), "x1": (-1.2, 1), "x2": (1.2, 1), "m": (0, -0.8), "z": (-2.2, -0.1)},
        ),
    )

    try:
        compile_animation_timeline(f0, f_bad, "SPLIT", duration_seconds=0.8)
        raise AssertionError("generic semantic change was incorrectly accepted as SPLIT")
    except ValueError:
        pass

    print("F4.4 false-SPLIT witness PASS")


if __name__ == "__main__":
    main()
