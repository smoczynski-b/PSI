#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

from compile_task_contract import compile_task
from memory_retrieval import retrieve
from test_m12_local_competition import load_attested_edges, local_pool, select, triples

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "experiments/m13-natural-tasks.tsv"
MANUAL = ROOT / "experiments/m12-task-contract.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def policy_for_selector(contract: dict):
    return {
        row["relation"]: {
            "role": row["role"],
            "priority": int(row["priority"]),
            "expand": bool(row["expand_target"]),
        }
        for row in contract["relation_policy"]
    }


def manual_policy():
    return {
        row["relation"]: {
            "role": row["role"],
            "priority": int(row["priority"]),
            "expand": row["expand_target"] == "YES",
        }
        for row in read_tsv(MANUAL)
    }


def main():
    fixtures = {row["case_id"]: row for row in read_tsv(FIXTURES)}
    compiled = {cid: compile_task(row["task"]) for cid, row in fixtures.items()}

    for cid, row in fixtures.items():
        got = compiled[cid]
        assert got["status"] == row["expected_status"], (cid, got)
        assert (got["anchor"] or "") == row["expected_anchor"], (cid, got)
        expected_intents = [x for x in row["expected_intents"].split(",") if x]
        assert got["intents"] == expected_intents, (cid, got["intents"], expected_intents)

    # Paraphrase invariance: two natural formulations compile to the same executable contract.
    c1, c2 = compiled["T1"], compiled["T2"]
    for key in ["anchor", "intents", "relation_policy", "local_radius", "edge_budget", "stop_condition", "attestation_mode"]:
        assert c1[key] == c2[key], key

    # The natural task recreates the manually frozen M12 relation policy.
    assert policy_for_selector(c1) == manual_policy()
    assert c1["edge_budget"] == 12
    assert c1["local_radius"] == 2

    edges = load_attested_edges()
    _, pool, _ = local_pool(edges, anchor=c1["anchor"], radius=c1["local_radius"])
    selected_manual = select(pool, manual_policy(), budget=12)
    selected_compiled = retrieve(c1)['edges']
    assert triples(selected_manual) == triples(selected_compiled)
    assert len(selected_compiled) == 12

    # Narrower task -> narrower executable projection, without boundary relations.
    c3 = compiled["T3"]
    p3 = policy_for_selector(c3)
    selected_proof = retrieve(c3)['edges']
    selected_proof_t = triples(selected_proof)
    assert set(p3) == {"HARD_DEPENDS_ON", "USES_DEFINITION", "USES_LEMMA"}
    assert len(selected_proof) == 7
    assert not any(rel in {"NOT_DEPENDS_ON", "DOES_NOT_IMPLY"} for _, rel, _ in selected_proof_t)
    assert triples(selected_proof).issubset(triples(selected_compiled))

    # Negative controls: ambiguity or missing anchor must not silently broaden retrieval.
    for cid in ["T4", "T5"]:
        c = compiled[cid]
        assert c["relation_policy"] == []
        assert c["stop_condition"] == "NO_RETRIEVAL"
        assert c["edge_budget"] is None

    print("PSI-MEMORY M13 PASS_WITH_BOUNDARY")
    print("T1/T2 paraphrase contract invariance=PASS")
    print("natural task reproduces manual M12 policy=PASS")
    print("compiled M12-equivalent selected_edges=12")
    print("proof-only task selected_edges=7 boundary_edges=0")
    print("ambiguous task -> NEEDS_CONTRACT / NO_RETRIEVAL")
    print("missing anchor -> NEEDS_ANCHOR / NO_RETRIEVAL")
    print("BOUNDARY: M13-LEXICAL-01 is a narrow deterministic compiler, not general language understanding")


if __name__ == "__main__":
    main()
