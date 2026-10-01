#!/usr/bin/env python3
from __future__ import annotations

from relation_crossview import graph_crossview, world_crossview


def bucket(view: dict, relation: str, key: str, value: str) -> dict:
    for row in view["distribution"][relation]:
        if row[key] == value:
            return row
    raise AssertionError((relation, key, value, view))


def main():
    # World view: the same relation family distributed over many objects.
    world = world_crossview({"POSITION", "MECHANISM", "FUNCTION", "MEASURES"})
    assert world["object_count"] == 24

    for pos in ("WRIST", "POCKET", "WALL", "TABLE"):
        b = bucket(world, "POSITION", "value", pos)
        assert b["count"] == 6
        assert abs(b["share"] - 0.25) < 1e-12

    for mech in ("MECHANICAL", "QUARTZ"):
        b = bucket(world, "MECHANISM", "value", mech)
        assert b["count"] == 12
        assert abs(b["share"] - 0.5) < 1e-12

    for fn in ("SIMPLE", "ALARM", "CHRONO"):
        b = bucket(world, "FUNCTION", "value", fn)
        assert b["count"] == 8

    measures = bucket(world, "MEASURES", "value", "TIME")
    assert measures["count"] == 24 and measures["share"] == 1.0

    # Cross-object matrix: same relation dimensions for selected concrete objects.
    subset = world_crossview(
        {"POSITION", "MECHANISM", "FUNCTION"},
        {"T-WR-QU-AL", "T-TA-QU-AL", "T-WR-ME-AL"},
    )
    assert subset["matrix"]["T-WR-QU-AL"] == {
        "FUNCTION": "ALARM", "MECHANISM": "QUARTZ", "POSITION": "WRIST"
    }
    assert subset["matrix"]["T-TA-QU-AL"] == {
        "FUNCTION": "ALARM", "MECHANISM": "QUARTZ", "POSITION": "TABLE"
    }
    assert subset["matrix"]["T-WR-ME-AL"] == {
        "FUNCTION": "ALARM", "MECHANISM": "MECHANICAL", "POSITION": "WRIST"
    }

    # Native PSI memory graph view: compare the same dependency relation across theorem objects.
    graph = graph_crossview({"HARD_DEPENDS_ON"})
    m = graph["matrix"]
    assert "II.9" in m and "II.7" in m and "C58" in m
    assert "II.7" in m["II.9"]["HARD_DEPENDS_ON"]
    assert "II.4" in m["II.7"]["HARD_DEPENDS_ON"]
    assert "C57" in m["C58"]["HARD_DEPENDS_ON"]

    # Inverted distribution exposes shared dependency targets instead of hiding them in per-node views.
    hard = graph["distribution"]["HARD_DEPENDS_ON"]
    assert any(row["target"] == "C57" and "C58" in row["subjects"] for row in hard)

    # Adding more requested relation families changes only the projection, not the source graph.
    graph2 = graph_crossview({"HARD_DEPENDS_ON", "USES_DEFINITION", "USES_LEMMA"}, {"II.7", "II.9"})
    assert set(graph2["matrix"]) == {"II.7", "II.9"}
    assert set(graph2["matrix"]["II.9"]) >= {"HARD_DEPENDS_ON", "USES_DEFINITION", "USES_LEMMA"}
    assert set(graph2["matrix"]["II.7"]) >= {"HARD_DEPENDS_ON", "USES_DEFINITION", "USES_LEMMA"}

    print("PSI-MEMORY M19-CROSSVIEW PASS_WITH_BOUNDARY")
    print("world distribution: POSITION=4x6, MECHANISM=2x12, FUNCTION=3x8, MEASURES TIME=24/24")
    print("cross-object relation matrix=PASS")
    print("native graph HARD_DEPENDS_ON cross-object view=PASS")
    print("inverted relation->target->subjects distribution=PASS")
    print("BOUNDARY: crossview is a read-only projection; frequencies describe the selected domain, not causal/statistical laws")


if __name__ == "__main__":
    main()
