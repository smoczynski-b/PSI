#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NODES = ROOT / "docs/memory/arch-lang-lineage-nodes-01.tsv"
EDGES = ROOT / "docs/memory/arch-lang-lineage-edges-01.tsv"
RECOVERY = ROOT / "docs/memory/arch-lang-source-recovery-01.tsv"

ALLOWED_RELATIONS = {
    "PRECURSOR_OF",
    "SURVIVES_AS",
    "SUPERSEDED_AS_FORMALISM",
    "REFINED_BY",
    "SCALED_BY",
    "ORTHOGONAL_VIEW_EXTENDED_BY",
}

ARCHIVE_EDGE_STATUSES = {
    "ARCHIVE_ATTESTED",
    "CONVERSATION_RECOVERED",
}

CURRENT_DOCS = {
    "M15-LANG": ROOT / "docs/memory/PSI-MEMORY-M15-LANG-RESULT-01.md",
    "M16": ROOT / "docs/memory/PSI-MEMORY-M16-RESULT-01.md",
    "M17": ROOT / "docs/memory/PSI-MEMORY-M17-RESULT-01.md",
    "M19-CROSSVIEW": ROOT / "docs/memory/PSI-MEMORY-M19-CROSSVIEW-RESULT-01.md",
}

RECOVERED_THREE = {
    "ARCH-2025-11-25-DENOTATION-LAYERS",
    "ARCH-2026-06-01-OBJECT-RELATIONAL-IDENTITY",
    "ARCH-2026-09-06-PSI-LANG",
}


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> None:
    nodes = read_tsv(NODES)
    edges = read_tsv(EDGES)
    recovery = read_tsv(RECOVERY)

    ids = [row["id"] for row in nodes]
    assert len(ids) == len(set(ids)), "lineage node ids must be unique"
    by_id = {row["id"]: row for row in nodes}

    recovery_ids = [row["archive_id"] for row in recovery]
    assert len(recovery_ids) == len(set(recovery_ids)), "source recovery ids must be unique"
    recovered_by_id = {row["archive_id"]: row for row in recovery}

    for current_id, path in CURRENT_DOCS.items():
        assert current_id in by_id, f"missing current lineage node: {current_id}"
        assert by_id[current_id]["source_status"] == "REPO_VERIFIED"
        assert path.exists(), f"missing mapped result document: {path}"

    for archive_id in RECOVERED_THREE:
        assert archive_id in by_id, f"missing recovered archive node: {archive_id}"
        assert by_id[archive_id]["kind"] == "ARCHIVE-IDEA"
        assert by_id[archive_id]["source_status"] == "CONVERSATION_RECOVERED"
        assert archive_id in recovered_by_id, f"missing source recovery row: {archive_id}"
        assert recovered_by_id[archive_id]["provenance_level"] == "CONVERSATION_RECOVERED"

    for edge in edges:
        assert edge["from"] in by_id, f"unknown edge source: {edge['from']}"
        assert edge["to"] in by_id, f"unknown edge target: {edge['to']}"
        assert edge["relation"] in ALLOWED_RELATIONS, f"unknown genealogy relation: {edge['relation']}"
        assert by_id[edge["from"]]["source_status"] != "NEEDS_SOURCE_RECOVERY", (
            "unrecovered archive candidate must not generate active genealogy edges: " + edge["from"]
        )
        if edge["source_status"] in ARCHIVE_EDGE_STATUSES:
            assert by_id[edge["from"]]["kind"] == "ARCHIVE-IDEA"
            assert edge["from"] in recovered_by_id, f"active archive source lacks recovery registry: {edge['from']}"
        if edge["source_status"] == "REPO_VERIFIED":
            assert by_id[edge["from"]]["kind"] == "CURRENT-RESULT"

    candidates = [row for row in nodes if row["source_status"] == "NEEDS_SOURCE_RECOVERY"]
    active_sources = {edge["from"] for edge in edges}
    assert all(row["id"] not in active_sources for row in candidates)
    assert not (RECOVERED_THREE & {row["id"] for row in candidates})

    # Exact recovered source roles must now participate in active genealogy.
    assert any(e["from"] == "ARCH-2025-11-25-DENOTATION-LAYERS" and e["to"] == "M15-LANG" for e in edges)
    assert any(e["from"] == "ARCH-2026-06-01-OBJECT-RELATIONAL-IDENTITY" and e["to"] == "M19-CROSSVIEW" for e in edges)
    assert any(e["from"] == "ARCH-2026-09-06-PSI-LANG" and e["to"] == "M15-LANG" for e in edges)
    assert any(e["from"] == "ARCH-2026-09-06-PSI-LANG" and e["to"] == "M16" for e in edges)

    # The genealogy must reach all four current executable stages without
    # treating historical resemblance as proof dependency.
    assert any(e["to"] == "M15-LANG" and e["relation"] == "PRECURSOR_OF" for e in edges)
    assert any(e["to"] == "M16" and e["relation"] == "SURVIVES_AS" for e in edges)
    assert any(e["to"] == "M17" and e["relation"] == "PRECURSOR_OF" for e in edges)
    assert any(e["to"] == "M19-CROSSVIEW" and e["relation"] == "PRECURSOR_OF" for e in edges)
    assert not any("DEPENDS" in e["relation"] for e in edges)

    raw_hashed = sum(r["provenance_level"] == "RAW_ARCHIVE_HASHED" for r in recovery)
    conv_recovered = sum(r["provenance_level"] == "CONVERSATION_RECOVERED" for r in recovery)

    print("ARCH-LANG-LINEAGE-01 REGISTRY_CONSISTENCY_PASS")
    print(f"nodes={len(nodes)} edges={len(edges)} recovery_rows={len(recovery)}")
    print(f"raw_archive_hashed={raw_hashed} conversation_recovered={conv_recovered}")
    print(f"source_recovery_candidates={len(candidates)} active_candidate_edges=0")
    print("recovered Nov-2025 denotation lineage=ACTIVE")
    print("recovered Jun-2026 relational-object lineage=ACTIVE")
    print("recovered Sep-2026 PSI-LANG lineage=ACTIVE")
    print("historical resemblance != proof dependency=PASS")
    print("surviving role != surviving formalism=PASS")
    print("BOUNDARY: recovered conversation provenance remains weaker than fragment-addressable repository certificates")
    print("NOT_CHECKED: archived source bytes, speaker attribution, exact quotations, historical precedence")


if __name__ == "__main__":
    main()
