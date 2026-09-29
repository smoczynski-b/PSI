#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEM = ROOT / "docs" / "memory"

NODE_FILES = [
    MEM / "psi-memory-nodes-01.tsv",
    MEM / "psi-memory-nodes-history-01.tsv",
]
EDGE_FILE = MEM / "psi-memory-edges-history-01.tsv"

PROPAGATING = {"VALIDITY", "BRIDGE_VALIDITY"}


def read_nodes() -> set[str]:
    ids: set[str] = set()
    for path in NODE_FILES:
        with path.open(encoding="utf-8", newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                node_id = row["id"].strip()
                assert node_id, f"empty node id in {path}"
                assert node_id not in ids, f"duplicate node id: {node_id}"
                ids.add(node_id)
    return ids


def read_edges() -> list[dict[str, str]]:
    with EDGE_FILE.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def prerequisite_closure(root: str, edges: list[dict[str, str]]) -> set[str]:
    # Edge direction is dependent -> prerequisite.
    by_source: dict[str, list[str]] = defaultdict(list)
    for e in edges:
        if e["effect"] in PROPAGATING:
            by_source[e["from"]].append(e["to"])

    seen: set[str] = set()
    todo = [root]
    while todo:
        current = todo.pop()
        for prereq in by_source.get(current, []):
            if prereq not in seen:
                seen.add(prereq)
                todo.append(prereq)
    return seen


def stale_closure(revoked: set[str], edges: list[dict[str, str]]) -> set[str]:
    # Reverse dependency traversal: prerequisite -> dependent.
    dependents: dict[str, list[str]] = defaultdict(list)
    for e in edges:
        if e["effect"] in PROPAGATING:
            dependents[e["to"]].append(e["from"])

    stale: set[str] = set()
    queue = deque(revoked)
    visited = set(revoked)
    while queue:
        prerequisite = queue.popleft()
        for dependent in dependents.get(prerequisite, []):
            if dependent not in visited:
                visited.add(dependent)
                stale.add(dependent)
                queue.append(dependent)
    return stale


def main() -> None:
    nodes = read_nodes()
    edges = read_edges()

    # Structural integrity.
    for e in edges:
        assert e["from"] in nodes, f"unknown source node: {e['from']}"
        assert e["to"] in nodes, f"unknown target node: {e['to']}"
        assert e["effect"] in {"VALIDITY", "BRIDGE_VALIDITY", "NONE"}, (
            f"unknown effect: {e['effect']}"
        )

    # M1: validity ancestry of II.9 must not absorb analogy/editorial order.
    ii9 = prerequisite_closure("II.9", edges)
    required = {"II.7", "II.4", "C57", "C58"}
    forbidden = {"II.6", "II.8"}
    assert required <= ii9, f"II.9 missing required ancestry: {required - ii9}"
    assert not (forbidden & ii9), f"II.9 acquired false ancestry: {forbidden & ii9}"

    # Classical theorem and PSI bridge are different validity atoms.
    classical = prerequisite_closure("II.11.CLASSICAL", edges)
    bridge = prerequisite_closure("II.11.PSI-BRIDGE", edges)
    assert classical == set(), f"classical Myhill-Nerode gained PSI prerequisites: {classical}"
    assert {"II.7", "II.8"} <= bridge, "PSI/Nerode bridge lost its PSI architecture prerequisites"

    # M2: simulate C57 revocation.
    stale = stale_closure({"C57"}, edges)
    expected_stale = {
        "C58",
        "II.7",
        "C42",
        "II.8",
        "C44",
        "II.9",
        "C45",
        "C59",
        "II.11.PSI-BRIDGE",
        "C18",
    }
    assert expected_stale <= stale, f"missing stale descendants: {expected_stale - stale}"

    expected_unaffected = {
        "II.6",
        "II.10.CLASSICAL",
        "II.10.PSI-BRIDGE",
        "II.11.CLASSICAL",
        "II.12.CLASSICAL",
        "II.12.PSI-GATE",
        "C13",
        "C14",
    }
    bad = expected_unaffected & stale
    assert not bad, f"invalidation leaked into unrelated/classical nodes: {bad}"

    print("PSI-MEMORY M1 PASS")
    print("PSI-MEMORY M2 PASS")
    print("II.9 validity ancestry:", ", ".join(sorted(ii9)))
    print("C57 stale descendants:", ", ".join(sorted(stale)))


if __name__ == "__main__":
    main()
