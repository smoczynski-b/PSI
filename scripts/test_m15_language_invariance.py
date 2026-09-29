#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

from compile_multilingual_contract import compile_multilingual_task, executable_signature
from compose_task_contract import certified_triples
from test_m12_local_competition import load_attested_edges, local_pool, select, triples

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "experiments/m15-language-tasks.tsv"
LEXICON = ROOT / "experiments/m15-denotation-lexicon.tsv"
WORLD = ROOT / "experiments/m15-world-relations.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def selector_policy(contract: dict):
    return {
        row["relation"]: {
            "role": row["role"],
            "priority": int(row["priority"]),
            "expand": bool(row["expand_target"]),
        }
        for row in contract["relation_policy"]
    }


def selected_for(contract: dict):
    edges = load_attested_edges()
    _, pool, _ = local_pool(edges, anchor=contract["anchor"], radius=contract["local_radius"])
    if contract["attestation_mode"] == "VALID_FRAGMENT_CERT_ONLY":
        cert = certified_triples()
        pool = [e for e in pool if (e["from"], e["relation"], e["to"]) in cert]
    return select(pool, selector_policy(contract), budget=contract["edge_budget"])


def lexical_candidates(language: str, token: str) -> set[str]:
    for row in read_tsv(LEXICON):
        if row["language"] == language and row["token"] == token:
            return {x for x in row["candidate_world_ids"].split(",") if x}
    return set()


def relational_filter(candidates: set[str], relation: str, obj: str) -> set[str]:
    allowed = {
        row["subject"]
        for row in read_tsv(WORLD)
        if row["relation"] == relation and row["object"] == obj
    }
    return candidates & allowed


def main():
    rows = read_tsv(TASKS)
    compiled = {}
    for row in rows:
        c = compile_multilingual_task(row["task"], row["language"])
        compiled[row["case_id"]] = c
        assert c["status"] == row["expected_status"], (row["case_id"], c)

    # Language invariance is checked on executable contracts, not on strings.
    broad = [compiled[x] for x in ("L1", "L2", "L3")]
    sigs = [executable_signature(c) for c in broad]
    assert sigs[0] == sigs[1] == sigs[2]
    selected = [triples(selected_for(c)) for c in broad]
    assert selected[0] == selected[1] == selected[2]
    assert len(selected[0]) == 12

    # Same check in strict evidence mode.
    strict = [compiled[x] for x in ("L4", "L5", "L6")]
    strict_sigs = [executable_signature(c) for c in strict]
    assert strict_sigs[0] == strict_sigs[1] == strict_sigs[2]
    strict_selected = [triples(selected_for(c)) for c in strict]
    assert strict_selected[0] == strict_selected[1] == strict_selected[2]
    assert len(strict_selected[0]) == 4
    cert = certified_triples()
    assert strict_selected[0].issubset(cert)

    # Unknown language adapter fails closed.
    assert compiled["L7"]["stop_condition"] == "NO_RETRIEVAL"
    assert compiled["L7"]["relation_policy"] == []

    # Denotation witness: lexical scopes need not be equal across languages.
    pl = lexical_candidates("PL", "zegarek")
    en = lexical_candidates("EN", "watch")
    de = lexical_candidates("DE", "Uhr")
    assert pl == {"OBJ-WRIST"}
    assert en == {"OBJ-WRIST"}
    assert de == {"OBJ-WRIST", "OBJ-WALL"}
    assert de != pl, "M15 must not force lexical scope equality"

    # A shared but non-discriminating world relation does not erase ambiguity.
    assert relational_filter(de, "MEASURES", "TIME") == de

    # A discriminating relation of the world resolves the wider lexical fibre.
    de_wrist = relational_filter(de, "ATTACHED_TO", "WRIST")
    de_wall = relational_filter(de, "ATTACHED_TO", "WALL")
    assert de_wrist == {"OBJ-WRIST"}
    assert de_wall == {"OBJ-WALL"}

    # Once grounded relationally, PL/EN/DE identify the same world object.
    assert pl == en == de_wrist

    print("PSI-MEMORY M15-LANG PASS_WITH_BOUNDARY")
    print("PL/EN/DE broad task -> executable contract invariant=PASS")
    print("PL/EN/DE broad task -> selected 12-edge graph invariant=PASS")
    print("PL/EN/DE strict boundary -> selected 4 certified-edge graph invariant=PASS")
    print("unknown language adapter -> NO_RETRIEVAL")
    print("lexical scope equality is NOT required: DE Uhr has 2 candidates; PL zegarek/EN watch have 1")
    print("shared relation MEASURES TIME does not falsely disambiguate=PASS")
    print("world relation ATTACHED_TO WRIST resolves DE Uhr -> OBJ-WRIST=PASS")
    print("BOUNDARY: fixtures test language adapters and relational grounding, not general multilingual understanding or ontology-independent perception")


if __name__ == "__main__":
    main()
