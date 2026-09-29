#!/usr/bin/env python3
from __future__ import annotations

import csv
from itertools import combinations, permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORLD = ROOT / "experiments/m17-world-objects.tsv"
LEXICON = ROOT / "experiments/m17-lexical-partitions.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def world_rows():
    return read_tsv(WORLD)


def world_ids():
    return {row["object_id"] for row in world_rows()}


def lexical_fibre(language: str, token: str) -> set[str] | None:
    for row in read_tsv(LEXICON):
        if row["language"] == language and row["token"] == token:
            return {x for x in row["candidate_world_ids"].split(",") if x}
    return None


def support(relation: str, value: str) -> set[str]:
    rows = world_rows()
    if not rows or relation not in rows[0] or relation == "object_id":
        return set()
    return {row["object_id"] for row in rows if row[relation] == value}


def status(fibre: set[str]) -> str:
    if not fibre:
        return "INCONSISTENT"
    if len(fibre) == 1:
        return "IDENTIFIED"
    return "UNRESOLVED"


def resolve(language: str, token: str, constraints: list[tuple[str, str]]):
    initial = lexical_fibre(language, token)
    if initial is None:
        return {
            "status": "NO_LEXICAL_FIBRE",
            "initial": None,
            "final": None,
            "sizes": [],
            "trace": [],
        }
    fibre = set(initial)
    trace = [set(fibre)]
    for relation, value in constraints:
        before = set(fibre)
        fibre &= support(relation, value)
        assert fibre <= before
        trace.append(set(fibre))
    return {
        "status": status(fibre),
        "initial": set(initial),
        "final": set(fibre),
        "sizes": [len(x) for x in trace],
        "trace": trace,
    }


def crossing_pairs():
    entries = []
    for row in read_tsv(LEXICON):
        entries.append((row["language"], row["token"], {x for x in row["candidate_world_ids"].split(",") if x}))
    out = []
    for a, b in combinations(entries, 2):
        A, B = a[2], b[2]
        if A & B and not A <= B and not B <= A:
            out.append((a, b, A & B))
    return out


def main():
    rows = world_rows()
    ids = world_ids()
    relation_families = [x for x in rows[0] if x != "object_id"]

    assert len(rows) == 24
    assert len(ids) == 24
    assert relation_families == ["POSITION", "MECHANISM", "FUNCTION", "ENERGY", "DISPLAY", "MEASURES"]

    # Every lexical candidate must denote an object in the same frozen world domain.
    for row in read_tsv(LEXICON):
        fibre = {x for x in row["candidate_world_ids"].split(",") if x}
        assert fibre
        assert fibre <= ids

    # The lexical system is genuinely non-hierarchical: many fibres overlap without inclusion.
    crossings = crossing_pairs()
    assert len(crossings) >= 20
    pl_watch = lexical_fibre("PL", "zegarek")
    de_chrono = lexical_fibre("DE", "Chronograph")
    assert pl_watch is not None and de_chrono is not None
    assert pl_watch & de_chrono
    assert not pl_watch <= de_chrono and not de_chrono <= pl_watch

    # Same world object can be reached from different initial lexical fibre widths.
    constraints = [("POSITION", "WRIST"), ("MECHANISM", "QUARTZ"), ("FUNCTION", "ALARM")]
    pl = resolve("PL", "zegarek", constraints)
    en = resolve("EN", "watch", constraints)
    de = resolve("DE", "Uhr", constraints)
    target = {"T-WR-QU-AL"}
    assert pl["final"] == en["final"] == de["final"] == target
    assert len(pl["initial"]) == 12
    assert len(en["initial"]) == 6
    assert len(de["initial"]) == 24

    # A broad German fibre narrows in stages under independent relation families.
    staged = resolve("DE", "Uhr", [("MECHANISM", "QUARTZ"), ("FUNCTION", "ALARM"), ("POSITION", "TABLE")])
    assert staged["sizes"] == [24, 12, 4, 1]
    assert staged["final"] == {"T-TA-QU-AL"}

    # A relation shared by every object is correctly non-discriminating.
    nondisc = resolve("DE", "Uhr", [("MEASURES", "TIME")])
    assert nondisc["sizes"] == [24, 24]
    assert nondisc["status"] == "UNRESOLVED"

    # Redundant physical relations may preserve fibre width rather than falsely add evidence.
    redundant = resolve("DE", "Uhr", [("MECHANISM", "QUARTZ"), ("ENERGY", "BATTERY")])
    redundant_rev = resolve("DE", "Uhr", [("ENERGY", "BATTERY"), ("MECHANISM", "QUARTZ")])
    assert redundant["sizes"] == [24, 12, 12]
    assert redundant_rev["sizes"] == [24, 12, 12]
    assert redundant["final"] == redundant_rev["final"]

    # Conjunctive order changes the trace but not the final fibre.
    base_constraints = [("MECHANISM", "QUARTZ"), ("FUNCTION", "ALARM"), ("POSITION", "TABLE")]
    finals = {tuple(sorted(resolve("DE", "Uhr", list(p))["final"])) for p in permutations(base_constraints)}
    assert finals == {("T-TA-QU-AL",)}

    # Function-based and form-based language partitions cross rather than define one canonical taxonomy.
    pl_chrono = lexical_fibre("PL", "chronograf")
    en_clock = lexical_fibre("EN", "clock")
    assert pl_chrono is not None and en_clock is not None
    assert len(pl_chrono & en_clock) == 4
    assert not pl_chrono <= en_clock and not en_clock <= pl_chrono

    # Equivalent function words can also converge across languages after relational refinement.
    chrono_constraints = [("POSITION", "POCKET"), ("MECHANISM", "MECHANICAL")]
    chrono_pl = resolve("PL", "chronograf", chrono_constraints)
    chrono_en = resolve("EN", "chronograph", chrono_constraints)
    chrono_de = resolve("DE", "Chronograph", chrono_constraints)
    assert chrono_pl["final"] == chrono_en["final"] == chrono_de["final"] == {"T-PO-ME-CH"}

    # Contradiction empties the fibre and later conjuncts cannot resurrect candidates.
    bad = resolve("DE", "Uhr", [("MECHANISM", "MECHANICAL"), ("ENERGY", "BATTERY")])
    assert bad["sizes"] == [24, 12, 0]
    assert bad["status"] == "INCONSISTENT"
    no_resurrection = resolve("DE", "Uhr", [("MECHANISM", "MECHANICAL"), ("ENERGY", "BATTERY"), ("POSITION", "WRIST")])
    assert no_resurrection["sizes"] == [24, 12, 0, 0]

    # Unknown lexical surface remains distinct from contradiction in a known fibre.
    unknown = resolve("PL", "nie-ma-takiego-slowa", [("POSITION", "WRIST")])
    assert unknown["status"] == "NO_LEXICAL_FIBRE"
    assert unknown["initial"] is None and unknown["final"] is None

    print("PSI-MEMORY M17 PASS_WITH_BOUNDARY")
    print("world_objects=24 relation_families=6 lexical_entries=%d" % len(read_tsv(LEXICON)))
    print("crossing lexical fibre pairs=%d" % len(crossings))
    print("different initial widths PL/EN/DE=12/6/24 -> same object T-WR-QU-AL")
    print("partial evidence DE Uhr sizes 24->12->4->1=PASS")
    print("non-discriminating MEASURES TIME sizes 24->24=PASS")
    print("redundant relation family sizes 24->12->12=PASS")
    print("all 6 permutations of three conjuncts -> same singleton=PASS")
    print("cross-partition non-nesting=PASS")
    print("contradiction 24->12->0 and no resurrection=PASS")
    print("unknown lexical surface != inconsistent fibre=PASS")
    print("BOUNDARY: lexical partitions and world attributes are frozen combinatorial fixtures, not empirical lexicography or a natural ontology")


if __name__ == "__main__":
    main()
