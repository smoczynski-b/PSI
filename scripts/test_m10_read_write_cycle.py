#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import subprocess
from collections import defaultdict, deque
from pathlib import Path

from build_edge_provenance import extract_fragment
from build_m8_context import ROOT, build_context, validated_evidence

DELTA = ROOT / "docs/memory/psi-memory-m9-verified-delta-01.tsv"
AUDIT = ROOT / "docs/memory/psi-memory-m9-admission-ledger-01.tsv"
BASE_PROV = ROOT / "docs/memory/psi-memory-edge-provenance-spec-01.tsv"
BRIDGE_PROV = ROOT / "docs/memory/psi-memory-edge-provenance-m8-bridge-spec-01.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def blob_sha(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return subprocess.check_output(["git", "hash-object", str(rel)], cwd=ROOT, text=True).strip()


def admitted_delta():
    rows = read_tsv(DELTA)
    node_rows = [r for r in rows if r["object_kind"] == "NODE" and r["status"] == "VERIFIED"]
    edge_rows = [r for r in rows if r["object_kind"] == "EDGE" and r["status"] == "VERIFIED"]
    evidence = {}
    edges = []
    nodes = {}
    for r in node_rows + edge_rows:
        fragment = extract_fragment(ROOT / r["path"], r["selector_type"], r["selector"])
        current_fragment_sha = hashlib.sha256(fragment).hexdigest()
        current_blob = blob_sha(ROOT / r["path"])
        if current_fragment_sha != r["fragment_sha256"]:
            status = "STALE"
        elif current_blob != r["verified_git_blob_sha"]:
            status = "SOURCE_DRIFT"
        else:
            status = "VALID"
        eid = "EV-M9-" + r["fragment_sha256"][:12]
        evidence[eid] = {
            "evidence_id": eid,
            "path": r["path"],
            "fragment_sha256": current_fragment_sha,
            "fragment_bytes": len(fragment),
            "fragment": fragment.decode("utf-8"),
            "status": status,
        }
        if r["object_kind"] == "NODE":
            nodes[r["id_or_from"]] = r
        else:
            edges.append({
                "edge_id": "E-M9-" + r["id_or_from"] + "-" + r["to_or_label"],
                "from": r["id_or_from"],
                "relation": r["relation_or_kind"],
                "to": r["to_or_label"],
                "evidence_id": eid,
            })
    return nodes, edges, evidence


def build_post_context(start: str, radius: int, force_m9_status: str | None = None):
    base_evidence = validated_evidence()
    nodes_delta, edges_delta, m9_evidence = admitted_delta()
    if force_m9_status is not None:
        m9_evidence = {k: dict(v, status=force_m9_status) for k, v in m9_evidence.items()}
    evidence = dict(base_evidence)
    evidence.update(m9_evidence)
    prov = read_tsv(BASE_PROV) + read_tsv(BRIDGE_PROV) + edges_delta

    adjacency = defaultdict(list)
    for edge in prov:
        ev = evidence.get(edge["evidence_id"])
        if ev and ev["status"] == "VALID":
            adjacency[edge["from"]].append(edge)

    dist = {start: 0}
    q = deque([start])
    selected = []
    seen = set()
    while q:
        node = q.popleft()
        if dist[node] >= radius:
            continue
        for edge in sorted(adjacency[node], key=lambda x: x["edge_id"]):
            if edge["edge_id"] not in seen:
                selected.append(edge)
                seen.add(edge["edge_id"])
            target = edge["to"]
            if target not in dist:
                dist[target] = dist[node] + 1
                q.append(target)

    ev_ids = sorted({e["evidence_id"] for e in selected})
    return {
        "nodes": sorted(dist),
        "edges": selected,
        "evidence": [evidence[eid] for eid in ev_ids],
        "delta_nodes": nodes_delta,
    }


def edge_triples(ctx):
    return {(e["from"], e["relation"], e["to"]) for e in ctx["edges"]}


def main():
    pre2 = build_context("GO-G4", 2)
    post2 = build_post_context("GO-G4", 2)
    assert set(n["id"] for n in pre2["nodes"]) == set(post2["nodes"]), "radius-2 view must not change"
    assert edge_triples(pre2) == edge_triples(post2), "radius-2 edges must not change"

    pre3 = build_context("GO-G4", 3)
    post3 = build_post_context("GO-G4", 3)
    pre_nodes = {n["id"] for n in pre3["nodes"]}
    post_nodes = set(post3["nodes"])
    assert post_nodes - pre_nodes == {"BIT-MINIMALITY"}, (pre_nodes, post_nodes)

    pre_edges = edge_triples(pre3)
    post_edges = edge_triples(post3)
    expected_new = {("II.9", "DOES_NOT_IMPLY", "BIT-MINIMALITY")}
    assert post_edges - pre_edges == expected_new, post_edges - pre_edges

    audit = read_tsv(AUDIT)
    assert any(r["submission_id"] == "B-E1" and r["outcome"] == "CONFLICT_UNVERIFIED" for r in audit)
    assert ("II.9", "IMPLIES", "BIT-MINIMALITY") not in post_edges, "audit conflict leaked into usable context"

    # If the newly admitted evidence ceases to be strictly VALID, retrieval returns to pre-M9 state.
    for status in ("STALE", "SOURCE_DRIFT"):
        degraded = build_post_context("GO-G4", 3, force_m9_status=status)
        assert set(degraded["nodes"]) == pre_nodes
        assert edge_triples(degraded) == pre_edges

    m9_evidence_ids = {e["evidence_id"] for e in post3["evidence"] if e["evidence_id"].startswith("EV-M9-")}
    assert len(m9_evidence_ids) == 1, m9_evidence_ids

    print("PSI-MEMORY M10 PASS")
    print("cycle: READ -> candidate work -> ADMIT -> READ' closes")
    print("radius2 delta: nodes=0 edges=0")
    print("radius3 delta: nodes=1 edges=1")
    print("added node=BIT-MINIMALITY")
    print("added edge=II.9 DOES_NOT_IMPLY BIT-MINIMALITY")
    print("CONFLICT_UNVERIFIED leakage=0")
    print("STALE/SOURCE_DRIFT fallback to pre-M9 view=PASS")


if __name__ == "__main__":
    main()
