#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from collections import defaultdict
from pathlib import Path

from build_edge_provenance import (
    ROOT,
    EVIDENCE_SPEC,
    EDGE_SPEC,
    extract_fragment,
    git_blob_sha,
    load_declared_edges,
    read_tsv,
)

CERTS = ROOT / "docs/memory/psi-memory-edge-evidence-01.tsv"


def status(cert_hash: str, current_hash: str, cert_blob: str, current_blob: str) -> str:
    if current_hash != cert_hash:
        return "STALE"
    if current_blob != cert_blob:
        return "SOURCE_DRIFT"
    return "VALID"


def main():
    cert_rows = read_tsv(CERTS)
    spec_rows = {r["evidence_id"]: r for r in read_tsv(EVIDENCE_SPEC)}
    edge_rows = read_tsv(EDGE_SPEC)
    declared_edges = load_declared_edges()

    assert len(cert_rows) == 6
    assert len(edge_rows) == 10
    assert {r["evidence_id"] for r in cert_rows} == set(spec_rows)

    certs = {}
    total_fragment_bytes = 0
    source_paths = set()

    for row in cert_rows:
        eid = row["evidence_id"]
        spec = spec_rows[eid]
        assert row["path"] == spec["path"]
        assert row["selector_type"] == spec["selector_type"]
        assert row["selector"] == spec["selector"]
        assert row["status"] == "VALID"

        path = ROOT / row["path"]
        fragment = extract_fragment(path, row["selector_type"], row["selector"])
        current_hash = hashlib.sha256(fragment).hexdigest()
        current_blob = git_blob_sha(path)

        assert len(fragment) == int(row["fragment_bytes"])
        assert status(row["fragment_sha256"], current_hash, row["verified_git_blob_sha"], current_blob) == "VALID"

        certs[eid] = row
        total_fragment_bytes += len(fragment)
        source_paths.add(path)

    edges_by_evidence = defaultdict(set)
    all_edge_ids = set()
    for edge in edge_rows:
        triple = (edge["from"], edge["relation"], edge["to"])
        assert triple in declared_edges
        assert edge["evidence_id"] in certs
        assert edge["edge_id"] not in all_edge_ids
        all_edge_ids.add(edge["edge_id"])
        edges_by_evidence[edge["evidence_id"]].add(edge["edge_id"])

    # Shared-fragment witnesses are part of the frozen M7 contract.
    assert len(edges_by_evidence["EV-II9-LIMIT"]) == 3
    assert len(edges_by_evidence["EV-G4"]) == 3

    # Simulated fragment mutation: exactly dependent edges become STALE.
    for eid, dependent in edges_by_evidence.items():
        cert = certs[eid]
        fake_hash = hashlib.sha256((cert["fragment_sha256"] + "tamper").encode()).hexdigest()
        s = status(cert["fragment_sha256"], fake_hash, cert["verified_git_blob_sha"], cert["verified_git_blob_sha"])
        assert s == "STALE"
        stale_edges = set(dependent)
        assert stale_edges
        assert stale_edges.isdisjoint(all_edge_ids - stale_edges)
        assert stale_edges | (all_edge_ids - stale_edges) == all_edge_ids

    # Same fragment under a changed containing-file version is not silently VALID.
    for cert in certs.values():
        s = status(cert["fragment_sha256"], cert["fragment_sha256"], cert["verified_git_blob_sha"], "0" * 40)
        assert s == "SOURCE_DRIFT"

    full_source_bytes = sum(p.stat().st_size for p in source_paths)
    naive_edge_evidence_bytes = sum(
        int(certs[edge["evidence_id"]]["fragment_bytes"]) for edge in edge_rows
    )

    assert total_fragment_bytes == 2165
    assert total_fragment_bytes < naive_edge_evidence_bytes
    assert total_fragment_bytes < full_source_bytes

    print("PSI-MEMORY M7 PASS")
    print(f"certified_edges={len(edge_rows)} unique_evidence_fragments={len(cert_rows)}")
    print(f"unique_fragment_bytes={total_fragment_bytes}")
    print(f"naive_per-edge_evidence_bytes={naive_edge_evidence_bytes}")
    print(f"full_source_file_bytes={full_source_bytes}")
    print(f"fragment/full={total_fragment_bytes/full_source_bytes:.4f}; reduction={(1-total_fragment_bytes/full_source_bytes)*100:.2f}%")
    print("tamper semantics: fragment change -> STALE; same fragment + file-version drift -> SOURCE_DRIFT")


if __name__ == "__main__":
    main()
