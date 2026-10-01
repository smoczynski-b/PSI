#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

from compile_task_contract import (
    INTENT_POLICIES,
    ascii_fold,
    detect_intents,
    known_node_ids,
    unsupported_exclusion,
)
from memory_retrieval import load_attested_edges, local_pool, certified_triples

ROOT = Path(__file__).resolve().parents[1]

ANALOGY_RULES = [
    {"relation": "ANALOGY_TO", "role": "ANALOGY", "priority": 60, "expand_target": False},
]
ANALOGY_MARKERS = (
    "analogie",
    "analogia",
    "analogiczne",
    "podobienstwa strukturalne",
)
STRICT_CERT_MARKERS = (
    "tylko pelne certyfikaty",
    "wylacznie pelne certyfikaty",
    "tylko certyfikowane fragmenty",
    "wylacznie certyfikowane fragmenty",
)

INTENT_RULES = dict(INTENT_POLICIES)
INTENT_RULES["ANALOGY"] = ANALOGY_RULES


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def detect_anchors(task: str) -> list[str]:
    folded = ascii_fold(task)
    hits = []
    for node_id in known_node_ids():
        nid = ascii_fold(node_id)
        pattern = rf"(?<![A-Za-z0-9_.-]){re.escape(nid)}(?![A-Za-z0-9_.-])"
        m = re.search(pattern, folded)
        if m:
            hits.append((m.start(), -len(nid), node_id))
    hits.sort()
    return [node_id for _, _, node_id in hits]


def detect_composed_intents(task: str) -> list[str]:
    intents = detect_intents(task)
    folded = ascii_fold(task)
    if any(marker in folded for marker in ANALOGY_MARKERS):
        intents.append("ANALOGY")
    return intents


def strict_cert_mode(task: str) -> bool:
    folded = ascii_fold(task)
    return any(marker in folded for marker in STRICT_CERT_MARKERS)


def build_policy(intents: list[str]) -> list[dict]:
    policy = []
    seen = set()
    for intent in intents:
        for rule in INTENT_RULES[intent]:
            if rule["relation"] not in seen:
                policy.append(dict(rule))
                seen.add(rule["relation"])
    return policy


def intent_budget(intents: list[str]) -> int:
    budget = 0
    if "PROOF_PREREQUISITE" in intents:
        budget += 8
    if "BOUNDARY" in intents:
        budget += 4
    if "ANALOGY" in intents:
        budget += 2
    return budget


def strict_coverage(anchor: str, intents: list[str], radius: int = 2) -> dict:
    edges = load_attested_edges()
    _, pool, _ = local_pool(edges, anchor=anchor, radius=radius)
    cert = certified_triples()
    coverage = {}
    for intent in intents:
        rels = {r["relation"] for r in INTENT_RULES[intent]}
        candidates = [e for e in pool if e["relation"] in rels]
        certified = [e for e in candidates if (e["from"], e["relation"], e["to"]) in cert]
        coverage[intent] = {
            "candidate_edges": len(candidates),
            "certified_edges": len(certified),
            "status": "COVERED" if certified else "UNCOVERED",
        }
    return coverage


def compile_composed_task(task: str) -> dict:
    anchors = detect_anchors(task)
    intents = detect_composed_intents(task)
    strict = strict_cert_mode(task)

    base = {
        "task": task,
        "anchors": anchors,
        "intents": intents,
        "relation_policy": [],
        "local_radius": None,
        "edge_budget": None,
        "stop_condition": "NO_RETRIEVAL",
        "attestation_mode": "VALID_FRAGMENT_CERT_ONLY" if strict else "VALID_FRAGMENT_CERT_OR_ROUTING_ATTESTED",
        "compiler": "M14-COMPOSE-01",
    }

    if not anchors:
        return {**base, "status": "NEEDS_ANCHOR", "anchor": None, "conflicts": ["MISSING_ANCHOR"]}
    if len(anchors) > 1:
        return {**base, "status": "NEEDS_ANCHOR_POLICY", "anchor": None, "conflicts": ["MULTIPLE_ANCHORS_WITHOUT_POLICY"]}
    anchor = anchors[0]
    if unsupported_exclusion(task):
        return {**base, 'status': 'NEEDS_CONTRACT', 'anchor': anchor, 'conflicts': ['UNSUPPORTED_EXCLUSION']}
    if not intents:
        return {**base, "status": "NEEDS_CONTRACT", "anchor": anchor, "conflicts": ["MISSING_TASK_INTENT"]}

    policy = build_policy(intents)
    budget = intent_budget(intents)
    coverage = strict_coverage(anchor, intents) if strict else {}
    uncovered = [intent for intent, info in coverage.items() if info["status"] == "UNCOVERED"]

    if strict and uncovered:
        return {
            **base,
            "status": "CONTRACT_CONFLICT",
            "anchor": anchor,
            "relation_policy": policy,
            "local_radius": 2,
            "edge_budget": budget,
            "coverage": coverage,
            "conflicts": [f"STRICT_CERT_NO_COVERAGE:{intent}" for intent in uncovered],
        }

    return {
        **base,
        "status": "COMPILED",
        "anchor": anchor,
        "relation_policy": policy,
        "local_radius": 2,
        "edge_budget": budget,
        "stop_condition": "EDGE_BUDGET_OR_FRONTIER_EXHAUSTED",
        "coverage": coverage,
        "conflicts": [],
    }


def main(argv: list[str]) -> int:
    task = " ".join(argv[1:]).strip()
    if not task:
        print("usage: compose_task_contract.py <natural-language task>", file=sys.stderr)
        return 2
    print(json.dumps(compile_composed_task(task), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
