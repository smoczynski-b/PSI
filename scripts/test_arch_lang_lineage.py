#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NODES = ROOT / "docs/memory/arch-lang-lineage-nodes-01.tsv"
EDGES = ROOT / "docs/memory/arch-lang-lineage-edges-01.tsv"

ALLOWED_RELATIONS = {
    "PRECURSOR_OF",
    "SURVIVES_AS",
    "SUPERSEDED_AS_FORMALISM",
    "REFINED_BY",
    "SCALED_BY",
    "ORTHOGONAL_VIEW_EXTENDED_BY",
}

CURRENT_DOCS = {
    "M15-LANG": ROOT / "docs/memory/PSI-MEMORY-M15-LANG-RESULT-01.md",
    "M16": ROOT / "docs/memory/PSI-MEMORY-M16-RESULT-01.md",
    "M17": ROOT / "docs/memory/PSI-MEMORY-M17-RESULT-01.md",
    "M19-CROSSVIEW": ROOT / "docs/memory/PSI-MEMORY-M19-CROSSVIEW-RESULT-01.md",
}


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> None:
    nodes = read_tsv(NODES)
    edges = read_tsv(EDGES)

    ids = [row["id"] for row in nodes]
    assert len(ids) == len(set(ids)), "lineage node ids must be unique"
    by_id = {row["id"]: row for row in nodes}

    for current_id, path in CURRENT_DOCS.items():
        assert current_id in by_id, f"missing current lineage node: {current_id}"
        assert by_id[current_id]["source_status"] == "REPO_VERIFIED"
        assert path.exists(), f"missing mapped result document: {path}"

    for edge in edges:
        assert edge["from"] in by_id, f"unknown edge source: {edge['from']}"
        assert edge["to"] in by_id, f"unknown edge target: {edge['to']}"
        assert edge["relation"] in ALLOWED_RELATIONS, f"unknown genealogy relation: {edge['relation']}"
        assert by_id[edge["from"]]["source_status"] != "NEEDS_SOURCE_RECOVERY", (
            "unrecovered archive candidate must not generate active genealogy edges: " + edge["from"]
        )
        if edge["source_status"] == "ARCHIVE_ATTESTED":
            assert by_id[edge["from"]]["kind"] == "ARCHIVE-IDEA"
        if edge["source_status"] == "REPO_VERIFIED":
            assert by_id[edge["from"]]["kind"] == "CURRENT-RESULT"

    candidates = [row for row in nodes if row["source_status"] == "NEEDS_SOURCE_RECOVERY"]
    active_sources = {edge["from"] for edge in edges}
    assert all(row["id"] not in active_sources for row in candidates)

    # The recovered genealogy must reach all four current executable stages without
    # treating historical resemblance as proof dependency.
    assert any(e["to"] == "M15-LANG" and e["relation"] == "PRECURSOR_OF" for e in edges)
    assert any(e["to"] == "M16" and e["relation"] == "SURVIVES_AS" for e in edges)
    assert any(e["to"] == "M17" and e["relation"] == "PRECURSOR_OF" for e in edges)
    assert any(e["to"] == "M19-CROSSVIEW" and e["relation"] == "PRECURSOR_OF" for e in edges)
    assert not any("DEPENDS" in e["relation"] for e in edges)

    print("ARCH-LANG-LINEAGE-01 PASS_WITH_BOUNDARY")
    print(f"nodes={len(nodes)} edges={len(edges)} archive_attested={sum(r['source_status']=='ARCHIVE_ATTESTED' for r in nodes)}")
    print(f"source_recovery_candidates={len(candidates)} active_candidate_edges=0")
    print("historical resemblance != proof dependency=PASS")
    print("surviving role != surviving formalism=PASS")
    print("BOUNDARY: archive-attested genealogy is weaker than fragment-addressable repository provenance")


if __name__ == "__main__":
    main()
