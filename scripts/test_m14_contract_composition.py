#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

from compose_task_contract import compile_composed_task, certified_triples
from test_m12_local_competition import load_attested_edges, local_pool, select, triples

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "experiments/m14-composition-tasks.tsv"


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


def selected_for(contract: dict, strict=False):
    edges = load_attested_edges()
    _, pool, _ = local_pool(edges, anchor=contract["anchor"], radius=contract["local_radius"])
    if strict:
        cert = certified_triples()
        pool = [e for e in pool if (e["from"], e["relation"], e["to"]) in cert]
    return select(pool, policy_for_selector(contract), budget=contract["edge_budget"])


def main():
    fixtures = {row["case_id"]: row for row in read_tsv(FIXTURES)}
    compiled = {cid: compile_composed_task(row["task"]) for cid, row in fixtures.items()}

    for cid, row in fixtures.items():
        got = compiled[cid]
        assert got["status"] == row["expected_status"], (cid, got)
        assert (got.get("anchor") or "") == row["expected_anchor"], (cid, got)
        expected_intents = [x for x in row["expected_intents"].split(",") if x]
        assert got["intents"] == expected_intents, (cid, got["intents"], expected_intents)
        if row["expected_attestation"]:
            assert got["attestation_mode"] == row["expected_attestation"]

    # C1: compatible composition genuinely adds analogy to the prior proof+boundary view.
    c1 = compiled["C1"]
    s1 = selected_for(c1)
    t1 = triples(s1)
    assert len(s1) == 13, len(s1)
    assert ("II.9", "ANALOGY_TO", "II.6") in t1
    assert ("II.9", "HARD_DEPENDS_ON", "II.7") in t1
    assert ("II.9", "DOES_NOT_IMPLY", "FINITE-MEMORY") in t1
    assert c1["edge_budget"] == 14

    # C2: strict certificates + requested analogy is fail-closed because the local
    # analogy family has no fragment-certified edge.
    c2 = compiled["C2"]
    assert c2["stop_condition"] == "NO_RETRIEVAL"
    assert "STRICT_CERT_NO_COVERAGE:ANALOGY" in c2["conflicts"]
    assert c2["coverage"]["ANALOGY"]["candidate_edges"] >= 1
    assert c2["coverage"]["ANALOGY"]["certified_edges"] == 0
    assert c2["coverage"]["PROOF_PREREQUISITE"]["certified_edges"] >= 1

    # C3: two explicit anchors without a composition policy do not silently pick one.
    c3 = compiled["C3"]
    assert set(c3["anchors"]) == {"II.9", "II.11.PSI-BRIDGE"}
    assert c3["anchor"] is None
    assert c3["stop_condition"] == "NO_RETRIEVAL"
    assert c3["conflicts"] == ["MULTIPLE_ANCHORS_WITHOUT_POLICY"]

    # C4: strict mode itself is legal when the requested relation family has
    # fragment-certified support. Ordinary routing attestations must not leak.
    c4 = compiled["C4"]
    s4 = selected_for(c4, strict=True)
    cert = certified_triples()
    assert len(s4) == 4
    assert all((e["from"], e["relation"], e["to"]) in cert for e in s4)
    assert all(e["relation"] in {"NOT_DEPENDS_ON", "DOES_NOT_IMPLY"} for e in s4)

    print("PSI-MEMORY M14 PASS_WITH_BOUNDARY")
    print("compatible composition: proof + boundary + analogy -> selected_edges=13")
    print("strict-cert analogy conflict -> CONTRACT_CONFLICT / NO_RETRIEVAL")
    print("multiple anchors without policy -> NEEDS_ANCHOR_POLICY / NO_RETRIEVAL")
    print("strict-cert boundary-only contract -> selected_edges=4, routing leakage=0")
    print("composition is typed and fail-closed=PASS")
    print("BOUNDARY: intent detection remains narrow lexical compilation; multi-anchor execution policy is not yet implemented")


if __name__ == "__main__":
    main()
