#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from build_m8_context import ROOT, build_context, render_context, validated_evidence

EXPECTED_EDGES = {
    "E-G4-FALSIFIES-PSK",
    "E-G4-SUPPORTS-SSK",
    "E-G4-REQUIRES-SSK",
    "E-G4-MEMBER",
    "E-GOREG-II7",
    "E-GOREG-II9",
    "E-II9-II7",
    "E-II9-NOT-II8",
    "E-II9-NOFINITE",
    "E-II9-NOCOMPUTE",
    "E-II9-NOEFFICIENT",
}
EXPECTED_EVIDENCE = {
    "EV-G4",
    "EV-GO-II7",
    "EV-GO-II9",
    "EV-II9-DEP",
    "EV-II9-NOTDEP",
    "EV-II9-LIMIT",
}
EXPECTED_NODES = {
    "GO-G4",
    "GO-MEMORY-REGRESSION",
    "PSK-MEMORY",
    "SSK-MEMORY",
    "SSK-CONTRACT",
    "II.7",
    "II.9",
    "II.8",
    "FINITE-MEMORY",
    "COMPUTABILITY",
    "EFFICIENCY",
}


def manifest_bytes(path: Path) -> int:
    total = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        total += (ROOT / line).stat().st_size
    return total


def main():
    ctx = build_context("GO-G4", 3)
    edge_ids = {e["edge_id"] for e in ctx["edges"]}
    evidence_ids = {e["evidence_id"] for e in ctx["evidence"]}
    node_ids = {n["id"] for n in ctx["nodes"]}

    assert edge_ids == EXPECTED_EDGES, (edge_ids, EXPECTED_EDGES)
    assert evidence_ids == EXPECTED_EVIDENCE, (evidence_ids, EXPECTED_EVIDENCE)
    assert node_ids == EXPECTED_NODES, (node_ids, EXPECTED_NODES)
    assert all(n["distance"] <= 3 for n in ctx["nodes"])

    evidence_bytes = sum(e["fragment_bytes"] for e in ctx["evidence"])
    artifact_bytes = len(render_context(ctx).encode("utf-8"))
    broad_bytes = manifest_bytes(ROOT / "experiments/m4-broad-manifest.txt")
    assert evidence_bytes == 2111, evidence_bytes
    assert artifact_bytes < broad_bytes * 0.10, (artifact_bytes, broad_bytes)

    # Strict validity gate: stale remote bridge must prune II.9 and its descendants,
    # while the independently certified Go->II.7 bridge remains usable.
    tampered = validated_evidence()
    tampered["EV-GO-II9"] = dict(tampered["EV-GO-II9"], status="STALE")
    degraded = build_context("GO-G4", 3, evidence_override=tampered)
    degraded_nodes = {n["id"] for n in degraded["nodes"]}
    degraded_edges = {e["edge_id"] for e in degraded["edges"]}
    assert "II.9" not in degraded_nodes
    assert "E-GOREG-II9" not in degraded_edges
    assert "II.7" in degraded_nodes
    assert "E-GOREG-II7" in degraded_edges

    # SOURCE_DRIFT is not falsehood, but strict M8 retrieval admits only VALID edges.
    drifted = validated_evidence()
    drifted["EV-GO-II9"] = dict(drifted["EV-GO-II9"], status="SOURCE_DRIFT")
    drift_ctx = build_context("GO-G4", 3, evidence_override=drifted)
    assert "II.9" not in {n["id"] for n in drift_ctx["nodes"]}

    print("PSI-MEMORY M8 PASS")
    print(f"nodes={len(ctx['nodes'])} edges={len(ctx['edges'])} evidence_fragments={len(ctx['evidence'])}")
    print(f"evidence_bytes={evidence_bytes} context_artifact_bytes={artifact_bytes}")
    print(f"broad_bytes={broad_bytes} artifact/broad={artifact_bytes / broad_bytes:.4f}; reduction={(1-artifact_bytes/broad_bytes)*100:.2f}%")
    print("strict gate: STALE/SOURCE_DRIFT bridge excludes II.9; independent II.7 bridge remains")


if __name__ == "__main__":
    main()
