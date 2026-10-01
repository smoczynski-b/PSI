#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

from compile_task_contract import ascii_fold, unsupported_exclusion
from compose_task_contract import (
    build_policy,
    detect_anchors,
    intent_budget,
    strict_coverage,
)

LANG = {
    "PL": {
        "PROOF_PREREQUISITE": ("przeslanki dowodu", "przeslanki dowodowe", "zaleznosci dowodowe"),
        "BOUNDARY": ("granice", "czego nie implikuje", "nie implikuje"),
        "ANALOGY": ("analogie", "analogia", "podobienstwa strukturalne"),
        "STRICT": ("tylko pelne certyfikaty", "wylacznie pelne certyfikaty", "tylko certyfikowane fragmenty"),
    },
    "EN": {
        "PROOF_PREREQUISITE": ("proof prerequisites", "proof dependencies", "proof premises"),
        "BOUNDARY": ("boundaries", "limits", "does not imply", "doesn't imply"),
        "ANALOGY": ("analogies", "analogy", "structural similarities"),
        "STRICT": ("only full certificates", "full certificates only", "only fragment certificates"),
    },
    "DE": {
        "PROOF_PREREQUISITE": ("beweisvoraussetzungen", "beweisabhangigkeiten", "beweispraemissen"),
        "BOUNDARY": ("grenzen", "beschrankungen", "impliziert nicht"),
        "ANALOGY": ("analogien", "analogie", "strukturelle ahnlichkeiten"),
        "STRICT": ("nur vollstandige zertifikate", "ausschliesslich vollstandige zertifikate", "nur fragmentzertifikate"),
    },
}


def markers_present(task: str, language: str, family: str) -> bool:
    folded = ascii_fold(task)
    return any(marker in folded for marker in LANG[language][family])


def compile_multilingual_task(task: str, language: str) -> dict:
    language = language.upper()
    base = {
        "task": task,
        "language": language,
        "compiler": "M15-LANG-01",
        "relation_policy": [],
        "local_radius": None,
        "edge_budget": None,
        "stop_condition": "NO_RETRIEVAL",
        "conflicts": [],
    }
    if language not in LANG:
        return {**base, "status": "NEEDS_LANGUAGE_ADAPTER", "anchor": None, "anchors": [], "intents": [], "attestation_mode": None}

    anchors = detect_anchors(task)
    intents = []
    for family in ("PROOF_PREREQUISITE", "BOUNDARY", "ANALOGY"):
        if markers_present(task, language, family):
            intents.append(family)
    strict = markers_present(task, language, "STRICT")
    attestation = "VALID_FRAGMENT_CERT_ONLY" if strict else "VALID_FRAGMENT_CERT_OR_ROUTING_ATTESTED"
    base.update({"anchors": anchors, "intents": intents, "attestation_mode": attestation})

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
    }


def executable_signature(contract: dict) -> dict:
    """Language-independent part of a compiled retrieval contract."""
    keys = ("status", "anchor", "intents", "relation_policy", "local_radius", "edge_budget", "stop_condition", "attestation_mode", "conflicts")
    return {k: contract.get(k) for k in keys}


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("usage: compile_multilingual_contract.py <PL|EN|DE> <task>", file=sys.stderr)
        return 2
    language = argv[1]
    task = " ".join(argv[2:]).strip()
    print(json.dumps(compile_multilingual_task(task, language), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
