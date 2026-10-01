#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEMORY_DIR = ROOT / "docs/memory"
WORLD = ROOT / "experiments/m17-world-objects.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_memory_edges() -> list[dict]:
    triples = {}
    for path in sorted(MEMORY_DIR.glob("psi-memory-edges*.tsv")):
        for row in read_tsv(path):
            if not {"from", "relation", "to"}.issubset(row):
                continue
            triple = (row["from"], row["relation"], row["to"])
            triples.setdefault(triple, {
                "from": row["from"],
                "relation": row["relation"],
                "to": row["to"],
                "sources": [],
            })["sources"].append(path.name)
    return list(triples.values())


def graph_crossview(relations: set[str], subjects: set[str] | None = None) -> dict:
    all_edges = load_memory_edges()
    unknown = relations - {e['relation'] for e in all_edges}
    if unknown:
        raise ValueError('unknown graph relation(s): ' + ','.join(sorted(unknown)))
    edges = [e for e in all_edges if e["relation"] in relations]
    if subjects is not None:
        edges = [e for e in edges if e["from"] in subjects]

    matrix = defaultdict(lambda: defaultdict(set))
    inverted = defaultdict(lambda: defaultdict(set))
    for e in edges:
        matrix[e["from"]][e["relation"]].add(e["to"])
        inverted[e["relation"]][e["to"]].add(e["from"])

    matrix_out = {
        subject: {rel: sorted(targets) for rel, targets in sorted(by_rel.items())}
        for subject, by_rel in sorted(matrix.items())
    }
    distribution = {
        rel: [
            {
                "target": target,
                "subjects": sorted(xs),
                "count": len(xs),
            }
            for target, xs in sorted(by_target.items())
        ]
        for rel, by_target in sorted(inverted.items())
    }
    return {
        "mode": "graph",
        "evidence_mode": "DECLARED_RELATIONS_NOT_REVALIDATED",
        "relations": sorted(relations),
        "subjects": sorted(matrix_out),
        "edge_count": len(edges),
        "matrix": matrix_out,
        "distribution": distribution,
    }


def world_crossview(relations: set[str], object_ids: set[str] | None = None) -> dict:
    rows = read_tsv(WORLD)
    if rows:
        unknown = relations - (set(rows[0]) - {"object_id"})
        if unknown:
            raise ValueError("unknown world relation(s): " + ",".join(sorted(unknown)))
    if object_ids is not None:
        unknown_ids = object_ids - {row['object_id'] for row in rows}
        if unknown_ids:
            raise ValueError('unknown world object(s): ' + ','.join(sorted(unknown_ids)))
        rows = [row for row in rows if row["object_id"] in object_ids]

    matrix = {}
    inverted = defaultdict(lambda: defaultdict(list))
    for row in rows:
        matrix[row["object_id"]] = {rel: row[rel] for rel in sorted(relations)}
        for rel in relations:
            inverted[rel][row[rel]].append(row["object_id"])

    n = len(rows)
    distribution = {
        rel: [
            {
                "value": value,
                "objects": sorted(ids),
                "count": len(ids),
                "share": (len(ids) / n if n else 0.0),
            }
            for value, ids in sorted(by_value.items())
        ]
        for rel, by_value in sorted(inverted.items())
    }
    return {
        "mode": "world",
        "relations": sorted(relations),
        "objects": sorted(matrix),
        "object_count": n,
        "matrix": {k: matrix[k] for k in sorted(matrix)},
        "distribution": distribution,
    }


def parse_set(raw: str | None) -> set[str] | None:
    if raw is None:
        return None
    return {x.strip() for x in raw.split(",") if x.strip()}


def main() -> int:
    p = argparse.ArgumentParser(description="Cross-object view of the same relation families.")
    p.add_argument("mode", choices=["graph", "world"])
    p.add_argument("relations", help="comma-separated relation names")
    p.add_argument("--objects", help="comma-separated subject/object ids")
    args = p.parse_args()

    relations = parse_set(args.relations) or set()
    objects = parse_set(args.objects)
    if not relations:
        p.error("at least one relation is required")

    if args.mode == "graph":
        result = graph_crossview(relations, objects)
    else:
        result = world_crossview(relations, objects)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
