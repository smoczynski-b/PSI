#!/usr/bin/env python3
from __future__ import annotations

from resolve_language_fibre import resolve


def sizes(result: dict) -> list[int]:
    return [step["size"] for step in result["trace"]]


def assert_monotone(result: dict):
    s = sizes(result)
    assert all(b <= a for a, b in zip(s, s[1:])), s


def main():
    # 1. Wider German lexical fibre stays unresolved under a non-discriminating relation.
    de_measure = resolve("DE", "Uhr", [("MEASURES", "TIME")])
    assert de_measure["status"] == "UNRESOLVED"
    assert de_measure["initial_fibre"] == ["OBJ-WALL", "OBJ-WRIST"]
    assert de_measure["final_fibre"] == ["OBJ-WALL", "OBJ-WRIST"]
    assert sizes(de_measure) == [2, 2]
    assert_monotone(de_measure)

    # 2. Adding a discriminating world relation collapses the fibre legally.
    de_wrist = resolve("DE", "Uhr", [("MEASURES", "TIME"), ("ATTACHED_TO", "WRIST")])
    assert de_wrist["status"] == "IDENTIFIED"
    assert de_wrist["final_fibre"] == ["OBJ-WRIST"]
    assert sizes(de_wrist) == [2, 2, 1]
    assert_monotone(de_wrist)

    # 3. Constraint order does not change the final relational fibre.
    de_wrist_rev = resolve("DE", "Uhr", [("ATTACHED_TO", "WRIST"), ("MEASURES", "TIME")])
    assert de_wrist_rev["final_fibre"] == de_wrist["final_fibre"]
    assert de_wrist_rev["status"] == de_wrist["status"]
    assert_monotone(de_wrist_rev)

    # 4. Different language fibres can converge to the same world object.
    pl_wrist = resolve("PL", "zegarek", [("MEASURES", "TIME"), ("ATTACHED_TO", "WRIST")])
    en_wrist = resolve("EN", "watch", [("MEASURES", "TIME"), ("ATTACHED_TO", "WRIST")])
    assert pl_wrist["status"] == en_wrist["status"] == de_wrist["status"] == "IDENTIFIED"
    assert pl_wrist["final_fibre"] == en_wrist["final_fibre"] == de_wrist["final_fibre"] == ["OBJ-WRIST"]

    # 5. Contradictory language/world evidence gives the empty fibre; no nearest-match fallback.
    pl_conflict = resolve("PL", "zegarek", [("ATTACHED_TO", "WALL")])
    assert pl_conflict["status"] == "INCONSISTENT"
    assert pl_conflict["final_fibre"] == []
    assert sizes(pl_conflict) == [1, 0]
    assert_monotone(pl_conflict)

    # Once empty, later relations cannot resurrect a candidate.
    pl_no_resurrection = resolve("PL", "zegarek", [("ATTACHED_TO", "WALL"), ("MEASURES", "TIME")])
    assert pl_no_resurrection["status"] == "INCONSISTENT"
    assert pl_no_resurrection["final_fibre"] == []
    assert sizes(pl_no_resurrection) == [1, 0, 0]

    # 6. Unknown lexical surface is different from an inconsistent known fibre.
    unknown = resolve("DE", "Zeitding", [("MEASURES", "TIME")])
    assert unknown["status"] == "NO_LEXICAL_FIBRE"
    assert unknown["initial_fibre"] is None
    assert unknown["final_fibre"] is None
    assert unknown["trace"] == []

    print("PSI-MEMORY M16 PASS_WITH_BOUNDARY")
    print("fibre update law: F_{k+1}=F_k intersection support(r_k,o_k)=PASS")
    print("monotone narrowing=PASS")
    print("non-discriminating relation preserves ambiguity: DE Uhr sizes 2->2=PASS")
    print("discriminating relation identifies: DE Uhr sizes 2->2->1=PASS")
    print("constraint-order final-fibre invariance=PASS")
    print("PL/EN/DE relational convergence -> OBJ-WRIST=PASS")
    print("contradiction -> empty fibre / no nearest-match fallback=PASS")
    print("empty-fibre resurrection blocked=PASS")
    print("unknown lexical surface != inconsistent known fibre=PASS")
    print("BOUNDARY: M16 uses frozen lexical/world fixtures; it does not infer relations from raw perception or free natural language")


if __name__ == "__main__":
    main()
