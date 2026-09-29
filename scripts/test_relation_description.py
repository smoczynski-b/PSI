#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEM = ROOT / "docs" / "memory"

NODE_FILES = [
    MEM / "psi-memory-nodes-01.tsv",
    MEM / "psi-memory-nodes-history-01.tsv",
    MEM / "psi-memory-nodes-bridges-01.tsv",
    MEM / "psi-memory-nodes-relational-01.tsv",
]
EDGE_FILES = [
    MEM / "psi-memory-edges-history-01.tsv",
    MEM / "psi-memory-edges-bridges-01.tsv",
    MEM / "psi-memory-edges-relational-01.tsv",
]


def read_nodes() -> dict[str, dict[str, str]]:
    nodes: dict[str, dict[str, str]] = {}
    for path in NODE_FILES:
        with path.open(encoding="utf-8", newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                node_id = row["id"].strip()
                assert node_id and node_id not in nodes, f"bad/duplicate node id: {node_id}"
                nodes[node_id] = row
    return nodes


def read_edges() -> list[dict[str, str]]:
    edges: list[dict[str, str]] = []
    for path in EDGE_FILES:
        with path.open(encoding="utf-8", newline="") as fh:
            edges.extend(csv.DictReader(fh, delimiter="\t"))
    return edges


def relation_profile(node_id: str, edges: list[dict[str, str]]) -> set[tuple[str, str, str]]:
    """Return structural description using only direction, relation and neighbor id.

    Deliberately ignores prose labels, edge notes and source summaries.
    """
    profile: set[tuple[str, str, str]] = set()
    for edge in edges:
        if edge["from"] == node_id:
            profile.add(("OUT", edge["relation"], edge["to"]))
        if edge["to"] == node_id:
            profile.add(("IN", edge["relation"], edge["from"]))
    return profile


def require(profile: set[tuple[str, str, str]], expected: set[tuple[str, str, str]], name: str) -> None:
    missing = expected - profile
    assert not missing, f"{name} missing relational description facets: {sorted(missing)}"


def main() -> None:
    nodes = read_nodes()
    edges = read_edges()

    for edge in edges:
        assert edge["from"] in nodes, f"unknown source node: {edge['from']}"
        assert edge["to"] in nodes, f"unknown target node: {edge['to']}"

    # Object 1: II.9. The relation profile must reconstruct its proof role,
    # structural analogy, explicit non-dependency, outputs and scope boundary.
    ii9 = relation_profile("II.9", edges)
    require(ii9, {
        ("OUT", "HARD_DEPENDS_ON", "II.7"),
        ("OUT", "USES_DEFINITION", "C57"),
        ("OUT", "USES_LEMMA", "C58"),
        ("OUT", "ANALOGY_TO", "II.6"),
        ("OUT", "NOT_DEPENDS_ON", "II.8"),
        ("OUT", "EVIDENCE_FOR", "C45"),
        ("OUT", "EVIDENCE_FOR", "C59"),
        ("OUT", "DOES_NOT_IMPLY", "FINITE-MEMORY"),
        ("OUT", "DOES_NOT_IMPLY", "COMPUTABILITY"),
        ("OUT", "DOES_NOT_IMPLY", "EFFICIENCY"),
        ("IN", "CLAIM_DEPENDS_ON", "C45"),
        ("IN", "CLAIM_DEPENDS_ON", "C59"),
        ("IN", "REGRESSION_FOR", "GO-MEMORY-REGRESSION"),
        ("IN", "EXEMPLIFIES", "II.11.PSI-BRIDGE"),
    }, "II.9")
    assert ("OUT", "HARD_DEPENDS_ON", "II.8") not in ii9

    # Object 2: GO-G4. Its meaning in shared memory is not 'a Go note';
    # relations recover its task contract, failed representation, sufficient
    # repair and role inside the regression bank.
    g4 = relation_profile("GO-G4", edges)
    require(g4, {
        ("OUT", "MEMBER_OF", "GO-MEMORY-REGRESSION"),
        ("OUT", "REQUIRES_CONTRACT", "SSK-CONTRACT"),
        ("OUT", "FALSIFIES", "PSK-MEMORY"),
        ("OUT", "SUPPORTS", "SSK-MEMORY"),
    }, "GO-G4")

    # Object 3: PSI/Myhill-Nerode bridge. Keep the classical theorem distinct
    # while recovering the PSI dependencies, contract, exact identification,
    # recursive-update example and registry consequence.
    nerode = relation_profile("II.11.PSI-BRIDGE", edges)
    require(nerode, {
        ("OUT", "BRIDGE_DEPENDS_ON", "II.7"),
        ("OUT", "BRIDGE_DEPENDS_ON", "II.8"),
        ("OUT", "EXEMPLIFIES", "II.9"),
        ("OUT", "EVIDENCE_FOR", "C18"),
        ("OUT", "REQUIRES_CONTRACT", "NERODE-LANGUAGE-CONTRACT"),
        ("OUT", "IDENTIFIES_WITH", "NERODE-EQUIVALENCE"),
        ("IN", "CONTAINS", "II.11"),
        ("IN", "CLAIM_DEPENDS_ON", "C18"),
    }, "II.11.PSI-BRIDGE")
    classical = relation_profile("II.11.CLASSICAL", edges)
    assert ("OUT", "BRIDGE_DEPENDS_ON", "II.7") not in classical
    assert ("OUT", "REQUIRES_CONTRACT", "NERODE-LANGUAGE-CONTRACT") not in classical

    # The experiment deliberately does not claim that structural relations
    # replace the mathematical proposition/formula inside a theorem node.
    assert nodes["II.9"]["kind"] == "THEOREM"
    assert nodes["GO-G4"]["kind"] == "REGRESSION_CASE"
    assert nodes["II.11.PSI-BRIDGE"]["kind"] == "BRIDGE_ASPECT"

    print("PSI-MEMORY M6-REL PASS_WITH_BOUNDARY")
    print(f"II.9 relational facets={len(ii9)}")
    print(f"GO-G4 relational facets={len(g4)}")
    print(f"II.11.PSI-BRIDGE relational facets={len(nerode)}")
    print("BOUNDARY: relation profile reconstructs structural role/context, not internal mathematical content")


if __name__ == "__main__":
    main()
