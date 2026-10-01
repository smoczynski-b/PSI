#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

from build_edge_provenance import extract_fragment

ROOT = Path(__file__).resolve().parents[1]
DELTAS = [ROOT / "experiments/m9-agent-a-delta.tsv", ROOT / "experiments/m9-agent-b-delta.tsv"]


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def base_nodes():
    out = set()
    for path in sorted((ROOT / "docs/memory").glob("psi-memory-nodes*.tsv")):
        for row in read_tsv(path):
            if row.get("id"):
                out.add(row["id"])
    return out


def base_edges():
    out = set()
    for path in sorted((ROOT / "docs/memory").glob("psi-memory-edges*.tsv")):
        for row in read_tsv(path):
            if {"from", "relation", "to"}.issubset(row):
                out.add((row["from"], row["relation"], row["to"]))
    return out


def evidence(row):
    path = ROOT / row["path"]
    fragment = extract_fragment(path, row["selector_type"], row["selector"])
    return fragment.decode("utf-8"), hashlib.sha256(fragment).hexdigest(), len(fragment)


def supports_node(row, fragment: str) -> bool:
    if row["subject"] == "BIT-MINIMALITY":
        return "minimalności bitowej" in fragment
    return False


def supports_edge(row, fragment: str) -> bool:
    triple = (row["subject"], row["relation"], row["object"])
    if triple == ("II.9", "DOES_NOT_IMPLY", "BIT-MINIMALITY"):
        return "II.9 nie ustanawia:" in fragment and "minimalności bitowej" in fragment
    if triple == ("II.9", "IMPLIES", "BIT-MINIMALITY"):
        return False
    return False


def run(paths):
    rows = []
    for path in paths:
        rows.extend(read_tsv(path))
    rows = sorted(rows, key=lambda r: r["submission_id"])

    nodes = base_nodes()
    edges = base_edges()
    ledger = {}
    verified_objects = []

    node_groups = {}
    for row in rows:
        if row["kind"] == "NODE":
            node_groups.setdefault(row["subject"], []).append(row)

    for node_id, group in sorted(node_groups.items()):
        if node_id in nodes:
            for row in group:
                ledger[row["submission_id"]] = ("DUPLICATE_VERIFIED", "node already present")
            continue
        signatures = {(r["object_kind"], r["label"], r["path"], r["selector_type"], r["selector"]) for r in group}
        if len(signatures) != 1:
            for row in group:
                ledger[row["submission_id"]] = ("CONFLICT", "competing node definitions")
            continue
        fragment, sha, size = evidence(group[0])
        if not supports_node(group[0], fragment):
            for row in group:
                ledger[row["submission_id"]] = ("UNVERIFIED", "source does not support node identity")
            continue
        verified_objects.append(("NODE", node_id, group[0]["object_kind"], group[0]["label"], sha, str(size)))
        for row in group:
            ledger[row["submission_id"]] = ("COALESCED_VERIFIED", "same candidate node; one canonical identity")

    opposite = {"IMPLIES": "DOES_NOT_IMPLY", "DOES_NOT_IMPLY": "IMPLIES"}
    edge_rows = [r for r in rows if r["kind"] == "EDGE"]
    candidate_triples = {(r["subject"], r["relation"], r["object"]): r for r in edge_rows}

    for row in edge_rows:
        sid = row["submission_id"]
        triple = (row["subject"], row["relation"], row["object"])
        if triple in edges:
            ledger[sid] = ("DUPLICATE_VERIFIED", "relation already present in verified memory")
            continue
        opposite_triple = (row["subject"], opposite.get(row["relation"], ""), row["object"])
        has_conflict = opposite_triple in candidate_triples
        fragment, sha, size = evidence(row)
        if supports_edge(row, fragment):
            verified_objects.append(("EDGE", row["subject"], row["relation"], row["object"], sha, str(size)))
            ledger[sid] = ("VERIFIED", "direct bounded source support" + ("; competing candidate retained" if has_conflict else ""))
        elif has_conflict:
            ledger[sid] = ("CONFLICT_UNVERIFIED", "opposed by competing candidate and source does not license this direction")
        else:
            ledger[sid] = ("UNVERIFIED", "source does not license proposed relation")

    return ledger, sorted(verified_objects)


def main():
    ledger_ab, verified_ab = run(DELTAS)
    ledger_ba, verified_ba = run(list(reversed(DELTAS)))
    assert ledger_ab == ledger_ba, "admission must be independent of agent/file arrival order"
    assert verified_ab == verified_ba, "verified delta must be independent of arrival order"

    expected = {
        "A-N1": "COALESCED_VERIFIED",
        "B-N1": "COALESCED_VERIFIED",
        "A-E1": "VERIFIED",
        "B-E1": "CONFLICT_UNVERIFIED",
        "A-E2": "DUPLICATE_VERIFIED",
        "B-E2": "DUPLICATE_VERIFIED",
    }
    assert {k: v[0] for k, v in ledger_ab.items()} == expected

    new_nodes = [x for x in verified_ab if x[0] == "NODE"]
    new_edges = [x for x in verified_ab if x[0] == "EDGE"]
    assert len(new_nodes) == 1 and new_nodes[0][1] == "BIT-MINIMALITY"
    assert len(new_edges) == 1 and new_edges[0][1:4] == ("II.9", "DOES_NOT_IMPLY", "BIT-MINIMALITY")
    assert all("CANON" not in status for status, _ in ledger_ab.values())

    print("PSI-MEMORY M9 PASS")
    print("write contract: agent output -> CANDIDATE; admission is evidence-gated")
    print("order invariance: PASS")
    print("author identity does not grant authority: PASS")
    print("conflict retained: B-E1=CONFLICT_UNVERIFIED")
    print("duplicate suppression: A-E2/B-E2=DUPLICATE_VERIFIED")
    print("verified delta objects=2 (1 thin node + 1 relation)")
    for item in verified_ab:
        print("VERIFIED\t" + "\t".join(item))
    for sid in sorted(ledger_ab):
        print("LEDGER\t" + sid + "\t" + ledger_ab[sid][0] + "\t" + ledger_ab[sid][1])


if __name__ == "__main__":
    main()
