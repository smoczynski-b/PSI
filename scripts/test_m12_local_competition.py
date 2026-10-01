#!/usr/bin/env python3
"""M12 regression: runtime retrieval is implemented in memory_retrieval."""
from memory_retrieval import (
    ROOT, ANCHOR, RADIUS, EDGE_BUDGET, CONTRACT, TABLES, M9,
    read_tsv, git_blob, load_attested_edges, local_pool, load_policy, select, triples,
)


def main():
    edges = load_attested_edges()
    nodes, pool, dist = local_pool(edges)
    policy = load_policy()
    selected = select(pool, policy)
    selected_reverse_input = select(list(reversed(pool)), policy)

    pool_t = triples(pool)
    selected_t = triples(selected)
    selected_reverse_t = triples(selected_reverse_input)

    # M12 stress condition: meaningful local competition, not a tiny star.
    assert len(pool) >= 25, f"local pool too small for competition test: {len(pool)}"
    assert len(nodes) >= 15, f"local node pool too small: {len(nodes)}"
    assert len(selected) <= EDGE_BUDGET
    assert selected_t == selected_reverse_t, "selection depends on input ordering"

    # Alternate routes already present in the real mapped history sector.
    assert ("II.9", "USES_DEFINITION", "C57") in pool_t
    assert ("II.9", "HARD_DEPENDS_ON", "II.7") in pool_t
    assert ("II.7", "USES_DEFINITION", "C57") in pool_t
    assert ("II.9", "USES_LEMMA", "C58") in pool_t
    assert ("II.7", "USES_LEMMA", "C58") in pool_t

    # Frozen task coverage: proof prerequisites plus explicit theorem boundaries.
    required = {
        ("II.9", "HARD_DEPENDS_ON", "II.7"),
        ("II.9", "USES_DEFINITION", "C57"),
        ("II.9", "USES_LEMMA", "C58"),
        ("II.9", "NOT_DEPENDS_ON", "II.8"),
        ("II.9", "DOES_NOT_IMPLY", "FINITE-MEMORY"),
        ("II.9", "DOES_NOT_IMPLY", "COMPUTABILITY"),
        ("II.9", "DOES_NOT_IMPLY", "EFFICIENCY"),
        ("II.9", "DOES_NOT_IMPLY", "BIT-MINIMALITY"),
        ("II.7", "HARD_DEPENDS_ON", "II.4"),
        ("II.7", "USES_DEFINITION", "C57"),
        ("II.7", "USES_LEMMA", "C58"),
        ("C58", "HARD_DEPENDS_ON", "C57"),
    }
    assert selected_t == required, (selected_t, required)

    # Terminal relation semantics prevent irrelevant expansion through II.8/properties.
    assert not any(e["from"] == "II.8" for e in selected)
    assert not any(e["relation"] in {"ANALOGY_TO", "EVIDENCE_FOR", "EXEMPLIFIES", "CONTAINS", "CONTRASTS_WITH", "REGRESSION_FOR"} for e in selected)

    selected_nodes = {ANCHOR}
    for e in selected:
        selected_nodes.add(e["from"])
        selected_nodes.add(e["to"])

    # Budget is genuinely selective relative to nearby, source-attested structure.
    assert len(selected) < len(pool) * 0.60, (len(selected), len(pool))
    assert len(selected_nodes) < len(nodes)

    valid_fragment = sum(1 for e in selected if e["attestation"] == "VALID_FRAGMENT_CERT")
    routing_attested = len(selected) - valid_fragment
    print("PSI-MEMORY M12 PASS_WITH_BOUNDARY")
    print(f"anchor={ANCHOR} local_radius={RADIUS} edge_budget={EDGE_BUDGET}")
    print(f"local_pool_nodes={len(nodes)} local_pool_edges={len(pool)}")
    print(f"selected_nodes={len(selected_nodes)} selected_edges={len(selected)}")
    print(f"edge_selection_ratio={len(selected)/len(pool):.4f}")
    print(f"selected VALID_FRAGMENT_CERT={valid_fragment} ROUTING_ATTESTED={routing_attested}")
    print("input-order invariance=PASS")
    print("alternate routes to C57/C58 present=PASS")
    print("terminal boundary non-expansion=PASS")
    print("BOUNDARY: ROUTING_ATTESTED checks current mapped/source provenance, not theorem-level re-proof")
    for e in selected:
        print("SELECTED\t" + "\t".join([e["from"], e["relation"], e["to"], e["attestation"]]))


if __name__ == "__main__":
    main()
