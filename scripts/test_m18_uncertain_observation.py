#!/usr/bin/env python3
from __future__ import annotations

import csv
from itertools import permutations
from pathlib import Path

from resolve_uncertain_fibre import resolve_uncertain

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "experiments/m18-observation-contracts.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def cases():
    grouped = {}
    for row in read_tsv(CONTRACTS):
        case = grouped.setdefault(row["case_id"], {
            "language": row["language"],
            "token": row["token"],
            "max_conflicts": int(row["max_conflicts"]),
            "observations": [],
        })
        assert case["language"] == row["language"]
        assert case["token"] == row["token"]
        assert case["max_conflicts"] == int(row["max_conflicts"])
        case["observations"].append({
            "observation_id": row["observation_id"],
            "relation": row["relation"],
            "allowed_values": [x for x in row["allowed_values"].split(",") if x],
        })
    return grouped


def run(case):
    return resolve_uncertain(
        case["language"],
        case["token"],
        case["observations"],
        case["max_conflicts"],
    )


def sizes(result):
    return [step["size"] for step in result["trace"]]


def main():
    C = cases()
    R = {name: run(case) for name, case in C.items()}
    target = "T-WR-QU-AL"

    # b=0 and singleton-valued observations recover the exact M16/M17 law.
    assert R["E0"]["status"] == "IDENTIFIED_EXACT"
    assert R["E0"]["final_fibre"] == [target]
    assert sizes(R["E0"]) == [24, 6, 3, 1]

    # Set-valued observation means disjunction within one observation, not a guess.
    assert R["U0"]["status"] == "UNRESOLVED"
    assert set(R["U0"]["final_fibre"]) == {"T-WR-QU-AL", "T-TA-QU-AL"}
    assert sizes(R["U0"]) == [24, 12, 6, 2]

    # One tolerated conflict with four observations leaves two candidates: no ranking.
    assert R["A0"]["status"] == "UNRESOLVED"
    assert set(R["A0"]["final_fibre"]) == {"T-WR-QU-AL", "T-WR-ME-AL"}
    assert len(R["A0"]["final_fibre"]) == 2

    # The same noisy evidence is inconsistent exactly, but legal under explicit tolerance.
    assert R["N0"]["status"] == "INCONSISTENT"
    assert R["N0"]["final_fibre"] == []
    assert R["N1"]["status"] == "IDENTIFIED_WITH_TOLERANCE"
    assert R["N1"]["final_fibre"] == [target]
    assert R["N1"]["violations"][target] == ["N-DISP"]

    # One additional independent observation separates the two b=1 candidates from A0.
    assert set(R["N1"]["final_fibre"]) < set(R["A0"]["final_fibre"])

    # Increasing the tolerance budget widens admissibility; it is not additional evidence.
    assert set(R["N0"]["final_fibre"]) <= set(R["N1"]["final_fibre"])
    assert set(R["N1"]["final_fibre"]) < set(R["N2"]["final_fibre"])
    assert len(R["N2"]["final_fibre"]) > 1
    assert R["N2"]["status"] == "UNRESOLVED"

    # Fixed tolerance plus more observations is monotone: every trace is non-increasing.
    for result in R.values():
        seq = sizes(result)
        assert all(b <= a for a, b in zip(seq, seq[1:])), (result, seq)

    # Final robust fibre is order-invariant for the same observation multiset.
    n1 = C["N1"]
    finals = set()
    for p in permutations(n1["observations"]):
        result = resolve_uncertain(n1["language"], n1["token"], list(p), n1["max_conflicts"])
        finals.add(tuple(result["final_fibre"]))
    assert finals == {(target,)}

    # Unknown lexical surface remains different from contradiction in a known fibre.
    unknown = resolve_uncertain("DE", "nicht-im-lexikon", C["N1"]["observations"], 1)
    assert unknown["status"] == "NO_LEXICAL_FIBRE"
    assert unknown["final_fibre"] is None

    # The resolver exposes admissible sets and violations, not scores or a nearest winner.
    forbidden_keys = {"score", "scores", "probability", "probabilities", "best_candidate", "ranking"}
    for result in list(R.values()) + [unknown]:
        assert forbidden_keys.isdisjoint(result.keys())

    print("PSI-MEMORY M18 PASS_WITH_BOUNDARY")
    print("exact recovery b=0 sizes 24->6->3->1=PASS")
    print("set-valued uncertainty sizes 24->12->6->2; remains UNRESOLVED=PASS")
    print("tolerated ambiguity b=1 returns 2 candidates; no ranking=PASS")
    print("same noisy observations: b=0 empty, b=1 singleton-with-tolerance, b=2 wider=PASS")
    print("fixed-tolerance refinement monotone=PASS")
    print("all 120 permutations of five noisy observations -> same final b=1 singleton=PASS")
    print("unknown lexical fibre != inconsistent known fibre=PASS")
    print("BOUNDARY: uncertainty is finite set-valued observation plus integer conflict budget; no probabilities, weights, learned likelihoods, or raw-sensor inference")


if __name__ == "__main__":
    main()
