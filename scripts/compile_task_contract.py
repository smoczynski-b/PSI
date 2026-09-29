#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INTENT_POLICIES = {
    "PROOF_PREREQUISITE": [
        {"relation": "HARD_DEPENDS_ON", "role": "PROOF_PREREQUISITE", "priority": 100, "expand_target": True},
        {"relation": "USES_DEFINITION", "role": "PROOF_PREREQUISITE", "priority": 95, "expand_target": True},
        {"relation": "USES_LEMMA", "role": "PROOF_PREREQUISITE", "priority": 95, "expand_target": True},
    ],
    "BOUNDARY": [
        {"relation": "NOT_DEPENDS_ON", "role": "BOUNDARY", "priority": 90, "expand_target": False},
        {"relation": "DOES_NOT_IMPLY", "role": "BOUNDARY", "priority": 90, "expand_target": False},
    ],
}

PROOF_MARKERS = (
    "przeslanki dowodu",
    "zaleznosci dowodowe",
    "zaleznosci dowodu",
    "przeslanki dowodowe",
)
BOUNDARY_MARKERS = (
    "granice",
    "czego twierdzenie nie implikuje",
    "czego nie implikuje",
    "nie implikuje",
    "ograniczenia twierdzenia",
)

POLISH_ASCII = str.maketrans({
    "ł": "l",
    "Ł": "L",
})


def ascii_fold(text: str) -> str:
    # NFKD removes combining accents but Polish l-stroke is not decomposed,
    # so normalize that character explicitly before stripping marks.
    text = text.translate(POLISH_ASCII)
    text = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in text if not unicodedata.combining(ch)).lower()


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def known_node_ids() -> list[str]:
    ids = set()
    for path in sorted((ROOT / "docs/memory").glob("psi-memory-nodes*.tsv")):
        for row in read_tsv(path):
            if row.get("id"):
                ids.add(row["id"])
    m9 = ROOT / "docs/memory/psi-memory-m9-verified-delta-01.tsv"
    if m9.exists():
        for row in read_tsv(m9):
            if row.get("object_kind") == "NODE" and row.get("status") == "VERIFIED":
                ids.add(row["id_or_from"])
    return sorted(ids, key=lambda x: (-len(x), x))


def detect_anchor(task: str) -> str | None:
    folded = ascii_fold(task)
    for node_id in known_node_ids():
        nid = ascii_fold(node_id)
        pattern = rf"(?<![A-Za-z0-9_.-]){re.escape(nid)}(?![A-Za-z0-9_.-])"
        if re.search(pattern, folded):
            return node_id
    return None


def detect_intents(task: str) -> list[str]:
    folded = ascii_fold(task)
    intents = []
    if any(marker in folded for marker in PROOF_MARKERS):
        intents.append("PROOF_PREREQUISITE")
    if any(marker in folded for marker in BOUNDARY_MARKERS):
        intents.append("BOUNDARY")
    return intents


def compile_task(task: str) -> dict:
    anchor = detect_anchor(task)
    intents = detect_intents(task)

    if not anchor:
        return {
            "status": "NEEDS_ANCHOR",
            "task": task,
            "anchor": None,
            "intents": intents,
            "relation_policy": [],
            "local_radius": None,
            "edge_budget": None,
            "stop_condition": "NO_RETRIEVAL",
        }
    if not intents:
        return {
            "status": "NEEDS_CONTRACT",
            "task": task,
            "anchor": anchor,
            "intents": [],
            "relation_policy": [],
            "local_radius": None,
            "edge_budget": None,
            "stop_condition": "NO_RETRIEVAL",
        }

    policy = []
    seen = set()
    for intent in intents:
        for rule in INTENT_POLICIES[intent]:
            if rule["relation"] not in seen:
                policy.append(dict(rule))
                seen.add(rule["relation"])

    # Frozen M13 budget rule. It is deliberately simple and explicit.
    budget = 0
    if "PROOF_PREREQUISITE" in intents:
        budget += 8
    if "BOUNDARY" in intents:
        budget += 4

    return {
        "status": "COMPILED",
        "task": task,
        "anchor": anchor,
        "intents": intents,
        "relation_policy": policy,
        "local_radius": 2,
        "edge_budget": budget,
        "stop_condition": "EDGE_BUDGET_OR_FRONTIER_EXHAUSTED",
        "attestation_mode": "VALID_FRAGMENT_CERT_OR_ROUTING_ATTESTED",
        "compiler": "M13-LEXICAL-01",
    }


def main(argv: list[str]) -> int:
    task = " ".join(argv[1:]).strip()
    if not task:
        print("usage: compile_task_contract.py <natural-language task>", file=sys.stderr)
        return 2
    print(json.dumps(compile_task(task), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
