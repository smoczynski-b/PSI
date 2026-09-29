#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import subprocess
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANCHOR = "II.9"
RADIUS = 2
EDGE_BUDGET = 12
CONTRACT = ROOT / "experiments/m12-task-contract.tsv"
TABLES = [
    ROOT / "docs/memory/psi-memory-edges-history-01.tsv",
    ROOT / "docs/memory/psi-memory-edges-relational-01.tsv",
    ROOT / "docs/memory/psi-memory-edges-bridges-01.tsv",
]
M9 = ROOT / "docs/memory/psi-memory-m9-verified-delta-01.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def git_blob(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return subprocess.check_output(["git", "hash-object", str(rel)], cwd=ROOT, text=True).strip()


def load_attested_edges():
    by_triple = {}
    for table in TABLES:
        for row in read_tsv(table):
            source = row["source"]
            source_path = ROOT / source
            if not source.startswith("docs/") or not source_path.exists():
                continue
            triple = (row["from"], row["relation"], row["to"])
            payload = "\t".join([*triple, source, row.get("note", "")]).encode("utf-8")
            by_triple[triple] = {
                "from": row["from"],
                "relation": row["relation"],
                "to": row["to"],
                "source": source,
                "source_blob_sha": git_blob(source_path),
                "routing_attestation_sha256": hashlib.sha256(payload).hexdigest(),
                "attestation": "ROUTING_ATTESTED",
            }

    # M9 is already source-fragment verified; include only its verified EDGE rows.
    for row in read_tsv(M9):
        if row["object_kind"] != "EDGE" or row["status"] != "VERIFIED":
            continue
        source = row["path"]
        source_path = ROOT / source
        assert source_path.exists()
        triple = (row["id_or_from"], row["relation_or_kind"], row["to_or_label"])
        by_triple[triple] = {
            "from": triple[0],
            "relation": triple[1],
            "to": triple[2],
            "source": source,
            "source_blob_sha": row["verified_git_blob_sha"],
            "routing_attestation_sha256": row["fragment_sha256"],
            "attestation": "VALID_FRAGMENT_CERT",
        }
    return list(by_triple.values())


def local_pool(edges, anchor=ANCHOR, radius=RADIUS):
    undirected = defaultdict(set)
    for e in edges:
        undirected[e["from"]].add(e["to"])
        undirected[e["to"]].add(e["from"])
    dist = {anchor: 0}
    q = deque([anchor])
    while q:
        node = q.popleft()
        if dist[node] >= radius:
            continue
        for nxt in sorted(undirected[node]):
            if nxt not in dist:
                dist[nxt] = dist[node] + 1
                q.append(nxt)
    nodes = set(dist)
    pool = [e for e in edges if e["from"] in nodes and e["to"] in nodes]
    return nodes, pool, dist


def load_policy():
    rows = read_tsv(CONTRACT)
    return {
        r["relation"]: {
            "role": r["role"],
            "priority": int(r["priority"]),
            "expand": r["expand_target"] == "YES",
        }
        for r in rows
    }


def select(pool, policy, budget=EDGE_BUDGET):
    outgoing = defaultdict(list)
    for e in pool:
        if e["relation"] in policy:
            outgoing[e["from"]].append(e)

    selected = []
    selected_triples = set()
    expanded = set()
    queued = {ANCHOR}
    q = deque([ANCHOR])

    while q and len(selected) < budget:
        node = q.popleft()
        queued.discard(node)
        if node in expanded:
            continue
        expanded.add(node)
        options = sorted(
            outgoing[node],
            key=lambda e: (-policy[e["relation"]]["priority"], e["relation"], e["to"], e["source"]),
        )
        for e in options:
            triple = (e["from"], e["relation"], e["to"])
            if triple in selected_triples:
                continue
            if len(selected) >= budget:
                break
            selected.append(e)
            selected_triples.add(triple)
            if policy[e["relation"]]["expand"] and e["to"] not in expanded and e["to"] not in queued:
                q.append(e["to"])
                queued.add(e["to"])
    return selected


def triples(edges):
    return {(e["from"], e["relation"], e["to"]) for e in edges}


def main():
    edges = load_attested_edges()
    nodes, pool, dist = local_pool(edges)
    policy = load_policy()
    selected = select(pool, policy)
    selected_reverse_input = select(list(reversed(pool)), policy)

    pool_t = triples(pool)
    selected_t = triples(selected)
    selected_reverse_t = triples(selected_reverse_input)

    # M12 stress condition: meaningful local competition, not a tiny star.
    assert len(pool) >= 25, f"local pool too small for competition test: {len(pool)}"
    assert len(nodes) >= 15, f"local node pool too small: {len(nodes)}"
    assert len(selected) <= EDGE_BUDGET
    assert selected_t == selected_reverse_t, "selection depends on input ordering"

    # Alternate routes already present in the real mapped history sector.
    assert ("II.9", "USES_DEFINITION", "C57") in pool_t
    assert ("II.9", "HARD_DEPENDS_ON", "II.7") in pool_t
    assert ("II.7", "USES_DEFINITION", "C57") in pool_t
    assert ("II.9", "USES_LEMMA", "C58") in pool_t
    assert ("II.7", "USES_LEMMA", "C58") in pool_t

    # Frozen task coverage: proof prerequisites plus explicit theorem boundaries.
    required = {
        ("II.9", "HARD_DEPENDS_ON", "II.7"),
        ("II.9", "USES_DEFINITION", "C57"),
        ("II.9", "USES_LEMMA", "C58"),
        ("II.9", "NOT_DEPENDS_ON", "II.8"),
        ("II.9", "DOES_NOT_IMPLY", "FINITE-MEMORY"),
        ("II.9", "DOES_NOT_IMPLY", "COMPUTABILITY"),
        ("II.9", "DOES_NOT_IMPLY", "EFFICIENCY"),
        ("II.9", "DOES_NOT_IMPLY", "BIT-MINIMALITY"),
        ("II.7", "HARD_DEPENDS_ON", "II.4"),
        ("II.7", "USES_DEFINITION", "C57"),
        ("II.7", "USES_LEMMA", "C58"),
        ("C58", "HARD_DEPENDS_ON", "C57"),
    }
    assert selected_t == required, (selected_t, required)

    # Terminal relation semantics prevent irrelevant expansion through II.8/properties.
    assert not any(e["from"] == "II.8" for e in selected)
    assert not any(e["relation"] in {"ANALOGY_TO", "EVIDENCE_FOR", "EXEMPLIFIES", "CONTAINS", "CONTRASTS_WITH", "REGRESSION_FOR"} for e in selected)

    selected_nodes = {ANCHOR}
    for e in selected:
        selected_nodes.add(e["from"])
        selected_nodes.add(e["to"])

    # Budget is genuinely selective relative to nearby, source-attested structure.
    assert len(selected) < len(pool) * 0.60, (len(selected), len(pool))
    assert len(selected_nodes) < len(nodes)

    valid_fragment = sum(1 for e in selected if e["attestation"] == "VALID_FRAGMENT_CERT")
    routing_attested = len(selected) - valid_fragment
    print("PSI-MEMORY M12 PASS_WITH_BOUNDARY")
    print(f"anchor={ANCHOR} local_radius={RADIUS} edge_budget={EDGE_BUDGET}")
    print(f"local_pool_nodes={len(nodes)} local_pool_edges={len(pool)}")
    print(f"selected_nodes={len(selected_nodes)} selected_edges={len(selected)}")
    print(f"edge_selection_ratio={len(selected)/len(pool):.4f}")
    print(f"selected VALID_FRAGMENT_CERT={valid_fragment} ROUTING_ATTESTED={routing_attested}")
    print("input-order invariance=PASS")
    print("alternate routes to C57/C58 present=PASS")
    print("terminal boundary non-expansion=PASS")
    print("BOUNDARY: ROUTING_ATTESTED checks current mapped/source provenance, not theorem-level re-proof")
    for e in selected:
        print("SELECTED\t" + "\t".join([e["from"], e["relation"], e["to"], e["attestation"]]))


if __name__ == "__main__":
    main()
