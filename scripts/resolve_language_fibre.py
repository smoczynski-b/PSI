#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEXICON = ROOT / "experiments/m15-denotation-lexicon.tsv"
WORLD = ROOT / "experiments/m15-world-relations.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def lexical_fibre(language: str, token: str) -> set[str] | None:
    for row in read_tsv(LEXICON):
        if row["language"] == language and row["token"] == token:
            return {x for x in row["candidate_world_ids"].split(",") if x}
    return None


def support(relation: str, obj: str, rows=None) -> set[str]:
    return {
        row["subject"]
        for row in (read_tsv(WORLD) if rows is None else rows)
        if row["relation"] == relation and row["object"] == obj
    }


def fibre_status(fibre: set[str]) -> str:
    if not fibre:
        return "INCONSISTENT"
    if len(fibre) == 1:
        return "IDENTIFIED"
    return "UNRESOLVED"


def resolve(language: str, token: str, constraints: list[tuple[str, str]]) -> dict:
    initial = lexical_fibre(language, token)
    if initial is None:
        return {
            "status": "NO_LEXICAL_FIBRE",
            "language": language,
            "token": token,
            "initial_fibre": None,
            "final_fibre": None,
            "trace": [],
        }

    fibre = set(initial)
    world = read_tsv(WORLD)
    known_relations = {row['relation'] for row in world}
    unknown = sorted({relation for relation, _ in constraints} - known_relations)
    if unknown:
        return {'status': 'NO_RELATION_CONTRACT', 'language': language, 'token': token,
                'initial_fibre': sorted(initial), 'final_fibre': None, 'trace': [],
                'unknown_relations': unknown}
    trace = [{
        "step": 0,
        "relation": None,
        "object": None,
        "fibre": sorted(fibre),
        "size": len(fibre),
        "status": fibre_status(fibre),
    }]

    for i, (relation, obj) in enumerate(constraints, start=1):
        before = set(fibre)
        fibre &= support(relation, obj, world)
        assert fibre <= before, "relational refinement must never enlarge the fibre"
        trace.append({
            "step": i,
            "relation": relation,
            "object": obj,
            "fibre": sorted(fibre),
            "size": len(fibre),
            "status": fibre_status(fibre),
        })

    return {
        "status": fibre_status(fibre),
        "language": language,
        "token": token,
        "initial_fibre": sorted(initial),
        "final_fibre": sorted(fibre),
        "trace": trace,
    }


def parse_constraint(raw: str) -> tuple[str, str]:
    if "=" not in raw:
        raise ValueError(f"constraint must be RELATION=OBJECT, got: {raw}")
    relation, obj = raw.split("=", 1)
    relation, obj = relation.strip(), obj.strip()
    if not relation or not obj:
        raise ValueError(f"constraint must be RELATION=OBJECT, got: {raw}")
    return relation, obj


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("usage: resolve_language_fibre.py <LANG> <TOKEN> [RELATION=OBJECT ...]", file=sys.stderr)
        return 2
    language, token = argv[1], argv[2]
    try:
        constraints = [parse_constraint(x) for x in argv[3:]]
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(resolve(language, token, constraints), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
