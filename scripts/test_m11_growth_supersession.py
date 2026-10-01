#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

from build_m8_context import ROOT, build_context
from test_m10_read_write_cycle import admitted_delta, build_post_context

SEQUENCE = ROOT / "experiments/m11-record-sequence.tsv"
M9_DELTA = ROOT / "docs/memory/psi-memory-m9-verified-delta-01.tsv"
SEMANTIC = ("II.9", "DOES_NOT_IMPLY", "BIT-MINIMALITY")


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def context_nodes(ctx):
    out = set()
    for n in ctx["nodes"]:
        out.add(n["id"] if isinstance(n, dict) else n)
    return out


def context_edges(ctx):
    return {(e["from"], e["relation"], e["to"]) for e in ctx["edges"]}


def canonical_context(ctx):
    payload = {
        "nodes": sorted(context_nodes(ctx)),
        "edges": sorted([list(x) for x in context_edges(ctx)]),
        "evidence": sorted([
            [e["evidence_id"], e["fragment_sha256"], int(e["fragment_bytes"])]
            for e in ctx["evidence"]
        ]),
    }
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return payload, text.encode("utf-8")


def base_graph_records():
    nodes = set()
    edges = set()
    for path in sorted((ROOT / "docs/memory").glob("psi-memory-nodes*.tsv")):
        for row in read_tsv(path):
            if row.get("id"):
                nodes.add(row["id"])
    for path in sorted((ROOT / "docs/memory").glob("psi-memory-edges*.tsv")):
        rows = read_tsv(path)
        if not rows:
            continue
        if {"from", "relation", "to"}.issubset(rows[0].keys()):
            for row in rows:
                edges.add((row["from"], row["relation"], row["to"]))
    for row in read_tsv(M9_DELTA):
        if row["status"] != "VERIFIED":
            continue
        if row["object_kind"] == "NODE":
            nodes.add(row["id_or_from"])
        elif row["object_kind"] == "EDGE":
            edges.add((row["id_or_from"], row["relation_or_kind"], row["to_or_label"]))
    return nodes, edges


def derived_record_status(records, record_id):
    r = records[record_id]
    superseded = {x["supersedes"] for x in records.values() if x.get("supersedes")}
    if r["status"] == "REVOKED":
        return "REVOKED_SUPERSEDED" if record_id in superseded else "REVOKED"
    if record_id in superseded:
        return "SUPERSEDED"
    if r["status"] == "VERIFIED":
        return "ACTIVE_VERIFIED"
    return r["status"]


def active_semantic_records(records):
    return [
        r for rid, r in records.items()
        if derived_record_status(records, rid) == "ACTIVE_VERIFIED"
        and (r["subject"], r["relation"], r["object"]) == SEMANTIC
    ]


def source_is_valid():
    _, _, evidence = admitted_delta()
    return bool(evidence) and all(e["status"] == "VALID" for e in evidence.values())


def usable_context(records):
    active = active_semantic_records(records)
    assert len(active) <= 1, "one semantic edge may not be activated by multiple record versions"
    if active and source_is_valid():
        return build_post_context("GO-G4", 3)
    return build_context("GO-G4", 3)


def global_record_count(base_nodes, base_edges, records, audit_supersedes, load_nodes, load_edges):
    return (
        len(base_nodes)
        + len(base_edges)
        + len(records)
        + len(audit_supersedes)
        + len(load_nodes)
        + len(load_edges)
    )


def main():
    sequence = sorted(read_tsv(SEQUENCE), key=lambda r: int(r["step"]))
    base_nodes, base_edges = base_graph_records()
    pre_m9 = build_context("GO-G4", 3)
    post_m9 = build_post_context("GO-G4", 3)
    _, pre_bytes = canonical_context(pre_m9)
    _, post_bytes = canonical_context(post_m9)
    assert SEMANTIC not in context_edges(pre_m9)
    assert SEMANTIC in context_edges(post_m9)

    records = {}
    audit_supersedes = set()
    load_nodes = set()
    load_edges = set()
    snapshots = {}

    for event in sequence:
        kind = event["event"]
        rid = event["record_id"]
        if kind in {"BASELINE", "SUPERSEDE", "REVERIFY"}:
            records[rid] = dict(event)
            if event["supersedes"]:
                assert event["supersedes"] in records, "successor must reference an existing record"
                audit_supersedes.add((rid, "SUPERSEDES", event["supersedes"]))
        elif kind == "REVOKE":
            assert rid in records
            records[rid]["status"] = "REVOKED"
        elif kind == "GROW":
            # Structural load only: a disconnected simulated verified subgraph.
            load_nodes = {f"LOAD-N{i:03d}" for i in range(256)}
            load_edges = {(f"LOAD-N{i:03d}", "NEXT", f"LOAD-N{i+1:03d}") for i in range(255)}
        else:
            raise AssertionError(f"unknown M11 event: {kind}")

        ctx = usable_context(records)
        payload, encoded = canonical_context(ctx)
        snapshots[int(event["step"])] = {
            "event": kind,
            "context": payload,
            "context_bytes": len(encoded),
            "global_records": global_record_count(
                base_nodes, base_edges, records, audit_supersedes, load_nodes, load_edges
            ),
            "active": [r["record_id"] for r in active_semantic_records(records)],
        }
        assert not any(n.startswith("LOAD-") for n in context_nodes(ctx))
        assert not any(rel == "SUPERSEDES" for _, rel, _ in context_edges(ctx))

    # v1 active, then v2 supersedes it with no semantic duplication.
    assert snapshots[0]["active"] == ["REC-BIT-v1"]
    assert snapshots[1]["active"] == ["REC-BIT-v2"]
    assert snapshots[0]["context"] == snapshots[1]["context"]
    assert list(context_edges(post_m9)).count(SEMANTIC) == 1

    # Material global growth must leave task context byte-for-byte stable.
    assert snapshots[2]["active"] == ["REC-BIT-v2"]
    assert snapshots[1]["context"] == snapshots[2]["context"]
    assert snapshots[1]["context_bytes"] == snapshots[2]["context_bytes"]
    growth = snapshots[2]["global_records"] - snapshots[1]["global_records"]
    assert growth == 511, growth

    # Revoking v2 must not silently reactivate superseded v1.
    assert snapshots[3]["active"] == []
    assert snapshots[3]["context"] == canonical_context(pre_m9)[0]
    assert snapshots[3]["context_bytes"] == len(pre_bytes)
    assert derived_record_status(records, "REC-BIT-v1") == "SUPERSEDED"

    # Explicit re-verification creates v3 and restores exactly the prior usable semantics.
    assert snapshots[4]["active"] == ["REC-BIT-v3"]
    assert snapshots[4]["context"] == canonical_context(post_m9)[0]
    assert snapshots[4]["context_bytes"] == len(post_bytes)
    assert derived_record_status(records, "REC-BIT-v2") == "REVOKED_SUPERSEDED"
    assert derived_record_status(records, "REC-BIT-v3") == "ACTIVE_VERIFIED"
    assert audit_supersedes == {
        ("REC-BIT-v2", "SUPERSEDES", "REC-BIT-v1"),
        ("REC-BIT-v3", "SUPERSEDES", "REC-BIT-v2"),
    }

    ratio = snapshots[2]["context_bytes"] / snapshots[2]["global_records"]
    print("PSI-MEMORY M11 PASS")
    print("record versioning: v1 -> v2 -> REVOKED -> v3")
    print("superseded predecessor fallback=BLOCKED")
    print("audit SUPERSEDES relations=2; ordinary-context leakage=0")
    print(f"synthetic disconnected growth records={growth}")
    print(f"global_records_after_growth={snapshots[2]['global_records']}")
    print(f"task_context_bytes_before_growth={snapshots[1]['context_bytes']}")
    print(f"task_context_bytes_after_growth={snapshots[2]['context_bytes']}")
    print(f"context_bytes/global_records={ratio:.4f}")
    print("revocation view=exact pre-M9 context")
    print("reverification view=exact post-M9 context")
    for rid in sorted(records):
        print(f"RECORD\t{rid}\t{derived_record_status(records, rid)}")


if __name__ == "__main__":
    main()
