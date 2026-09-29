#!/usr/bin/env python3
from __future__ import annotations

import csv
import itertools
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "experiments/chem-vision-worlds-01.tsv"


def read_rows():
    with DATA.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def parse_side(text: str) -> Counter:
    text = text.strip()
    if not text:
        return Counter()
    out = Counter()
    for token in text.split("+"):
        token = token.strip()
        if not token:
            raise ValueError("empty species token")
        out[token] += 1
    return out


def parse_network(text: str):
    reactions = []
    for raw in text.split(";"):
        left, right = raw.split("->")
        reactions.append((parse_side(left), parse_side(right)))
    return reactions


def species(network):
    return sorted({s for left, right in network for s in set(left) | set(right)})


def remap_counter(counter: Counter, mapping: dict[str, str]) -> Counter:
    return Counter({mapping[k]: v for k, v in counter.items()})


def isomorphic_reaction_languages(a_text: str, b_text: str) -> bool:
    a = parse_network(a_text)
    b = parse_network(b_text)
    sa, sb = species(a), species(b)
    if len(sa) != len(sb) or len(a) != len(b):
        return False
    target = sorted((tuple(sorted(l.items())), tuple(sorted(r.items()))) for l, r in b)
    for perm in itertools.permutations(sb):
        mapping = dict(zip(sa, perm))
        mapped = sorted(
            (tuple(sorted(remap_counter(l, mapping).items())), tuple(sorted(remap_counter(r, mapping).items())))
            for l, r in a
        )
        if mapped == target:
            return True
    return False


def visual_fibre(rows, trace: str):
    return [r for r in rows if r["visual_trace"] == trace]


def reaction_count_fibre(rows, count: int):
    return [r for r in rows if len(parse_network(r["reaction_language"])) == count]


def main():
    rows = read_rows()
    by_id = {r["world_id"]: r for r in rows}
    assert set(by_id) == {"SEQ_A", "SEQ_X", "COUPLED"}

    # 1. The eye receives exactly the same coarse image geometry for three
    # distinct reaction mechanisms.
    trace = rows[0]["visual_trace"]
    vf = visual_fibre(rows, trace)
    assert len(vf) == 3
    assert len({r["reaction_language"] for r in vf}) == 3

    # 2. Reaction notation is treated as a typed hypergraph language, not as
    # a bag of species names. Relabelling species preserves the sequential motif.
    assert isomorphic_reaction_languages(by_id["SEQ_A"]["reaction_language"], by_id["SEQ_X"]["reaction_language"])
    assert not isomorphic_reaction_languages(by_id["SEQ_A"]["reaction_language"], by_id["COUPLED"]["reaction_language"])

    # 3. A coarse language observation ('there are two elementary steps')
    # narrows the object fibre but does not identify the concrete world.
    lf = reaction_count_fibre(vf, 2)
    assert {r["world_id"] for r in lf} == {"SEQ_A", "SEQ_X"}
    assert len(lf) == 2

    # 4. Yet the task quotient 'reaction motif' is already a singleton.
    motifs = {r["motif"] for r in lf}
    assert motifs == {"SEQUENTIAL_2STEP"}

    # 5. Provenance/history can identify the concrete realization later.
    identified = [r for r in lf if r["sample_tag"] == "SAMPLE-ALPHA"]
    assert [r["world_id"] for r in identified] == ["SEQ_A"]

    # 6. The coupled branch contains one true 2-reactant hyperedge; ordinary
    # binary-edge intuition would lose this structural distinction.
    coupled = parse_network(by_id["COUPLED"]["reaction_language"])
    assert any(sum(left.values()) == 2 for left, _ in coupled)
    seq = parse_network(by_id["SEQ_A"]["reaction_language"])
    assert all(sum(left.values()) == 1 for left, _ in seq)

    print("PSI-CHEM-VISION-LAB-01 PASS_WITH_BOUNDARY")
    print("visual-only fibre=3 distinct mechanisms")
    print("reaction-count constraint fibre=2")
    print("object identification=NO; task motif quotient=SEQUENTIAL_2STEP singleton")
    print("species relabelling structural isomorphism=PASS")
    print("hyperedge arity distinguishes coupled branch=PASS")
    print("provenance/sample tag resolves concrete realization=PASS")
    print("BOUNDARY: visual_trace is a synthetic image-feature surrogate; no pixel-level vision claim is made")


if __name__ == "__main__":
    main()
