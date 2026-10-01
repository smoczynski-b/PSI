#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "docs/memory/psi-map-genealogy-sources-01.tsv"
NODES = ROOT / "docs/memory/psi-map-genealogy-nodes-01.tsv"
EDGES = ROOT / "docs/memory/psi-map-genealogy-edges-01.tsv"

ALLOWED_RELATIONS = {
    "PRECURSOR_OF",
    "CONTRIBUTES_ROLE_TO",
    "ANALOGOUS_ROLE",
    "NOT_EQUIVALENT_TO",
    "CONTEMPORARY_PARALLEL_TO",
    "REALIZES_PART_OF",
    "SUPPORTS",
    "CURATES",
    "GATES",
    "MONITORS_TRANSITIONS_OF",
    "MONITORS_PATHOLOGY_OF",
    "CONSTRAINS",
    "EXCHANGED_ON",
}

CANDIDATE_ROLES = {
    "PSI-GUARDIAN",
    "PSI-SERVANT",
    "PSI-IMMUNE",
    "PSI-CURATOR",
    "PSI-MAP-OBJECT",
    "PSI-MAP-EXCHANGE",
}

HISTORICAL = {
    "HII-1977",
    "BB1-1985",
    "KM-2003",
    "AMELI-2004",
    "MAPEK-2005",
    "NANOPUB-2010",
    "DDNA-2012",
    "AIS-FDDR-2015",
}


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> None:
    sources = read_tsv(SOURCES)
    nodes = read_tsv(NODES)
    edges = read_tsv(EDGES)

    source_ids = [r["source_id"] for r in sources]
    assert len(source_ids) == len(set(source_ids)), "source ids must be unique"
    source_set = set(source_ids)

    node_ids = [r["id"] for r in nodes]
    assert len(node_ids) == len(set(node_ids)), "node ids must be unique"
    by_id = {r["id"]: r for r in nodes}

    assert CANDIDATE_ROLES <= set(node_ids)
    assert HISTORICAL <= set(node_ids)
    assert by_id["PSI-MAP-EXCHANGE"]["status"] == "UNRESOLVED_NOVELTY"
    assert by_id["PSI-TASK-GATE"]["status"] == "REPO_VERIFIED"
    assert by_id["PSI-SHARED-MEMORY"]["status"] == "PASS_WITH_BOUNDARY"
    assert by_id["PSI-DURABLE-MEMORY"]["status"] == "PASS_WITH_BOUNDARY"

    for node in nodes:
        assert node["source_id"] in source_set, f"unknown source for node {node['id']}"

    for edge in edges:
        assert edge["from"] in by_id, f"unknown edge source: {edge['from']}"
        assert edge["to"] in by_id, f"unknown edge target: {edge['to']}"
        assert edge["source_id"] in source_set, f"unknown edge source id: {edge['source_id']}"
        assert edge["relation"] in ALLOWED_RELATIONS, f"unknown genealogy relation: {edge['relation']}"
        assert "DEPENDS_ON" not in edge["relation"], "genealogy must not become proof dependency"

    # Historical vocabulary discipline: old systems may point to current roles,
    # but are never relabelled as current PSI roles or current execution results.
    for hid in HISTORICAL:
        assert by_id[hid]["kind"].startswith("HISTORICAL_")
        assert by_id[hid]["status"] == "SOURCE_VERIFIED"

    # Required nearest-neighbour witnesses.
    required = {
        ("HII-1977", "PRECURSOR_OF", "PSI-SHARED-MEMORY"),
        ("BB1-1985", "CONTRIBUTES_ROLE_TO", "PSI-SERVANT"),
        ("AMELI-2004", "CONTRIBUTES_ROLE_TO", "PSI-GUARDIAN"),
        ("AIS-FDDR-2015", "ANALOGOUS_ROLE", "PSI-IMMUNE"),
        ("KM-2003", "PRECURSOR_OF", "PSI-MAP-EXCHANGE"),
        ("DDNA-2012", "PRECURSOR_OF", "PSI-MAP-OBJECT"),
        ("NANOPUB-2010", "PRECURSOR_OF", "PSI-MAP-OBJECT"),
        ("PSI-TASK-GATE", "CONSTRAINS", "PSI-MAP-EXCHANGE"),
    }
    actual = {(e["from"], e["relation"], e["to"]) for e in edges}
    assert required <= actual

    # Non-equivalence guards prevent role resemblance from being silently
    # promoted to identity of architectures.
    assert ("BB1-1985", "NOT_EQUIVALENT_TO", "PSI-SERVANT") in actual
    assert ("AMELI-2004", "NOT_EQUIVALENT_TO", "PSI-GUARDIAN") in actual
    assert ("AIS-FDDR-2015", "NOT_EQUIVALENT_TO", "PSI-IMMUNE") in actual

    # Current candidate roles remain non-canonical/candidate in this artifact.
    for cid in CANDIDATE_ROLES - {"PSI-MAP-EXCHANGE"}:
        assert by_id[cid]["status"] == "CANDIDATE"

    print("PSI-MAP-GENEALOGY-01 REGISTRY_CONSISTENCY_PASS")
    print(f"sources={len(sources)} nodes={len(nodes)} edges={len(edges)}")
    print("historical_resemblance_not_proof_dependency=PASS")
    print("back_projection_of_PSI_vocabulary=BLOCKED")
    print("candidate_roles_remain_noncanonical=PASS")
    print("novelty_status=UNRESOLVED_NOVELTY")


if __name__ == "__main__":
    main()
