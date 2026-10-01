#!/usr/bin/env python3
from __future__ import annotations

from itertools import permutations

from active_memory import MemoryEvent, compile_workspace
from concurrent_workspace import ConcurrentWorkspace, Proposal

CONTRACT = {
    "status": "COMPILED",
    "contract_id": "ACTIVE-MEMORY-CONCURRENCY-01",
    "anchor": "ROOT",
    "task": "test optimistic concurrent proposal semantics",
}
RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "ROOT",
    "edges": [
        {"from": "ROOT", "relation": "BASE", "to": "A", "source": "seed:A", "status": "ADMITTED"},
        {"from": "ROOT", "relation": "BASE", "to": "B", "source": "seed:B", "status": "ADMITTED"},
    ],
}


def fresh():
    return ConcurrentWorkspace(compile_workspace(CONTRACT, RETRIEVAL))


def upsert(pid: str, actor: str, base: int, relation: str, target: str, source: str):
    return Proposal(
        proposal_id=pid,
        actor_id=actor,
        base_revision=base,
        event=MemoryEvent(
            event_id=f"event:{pid}",
            kind="EDGE_UPSERT",
            event_time="2026-09-30T11:25:00Z",
            ingest_time="2026-09-30T11:25:00.001000Z",
            payload={
                "from": "ROOT",
                "relation": relation,
                "to": target,
                "source": source,
                "status": "ADMITTED",
            },
        ),
    )


def remove(pid: str, actor: str, base: int, relation: str, target: str):
    return Proposal(
        proposal_id=pid,
        actor_id=actor,
        base_revision=base,
        event=MemoryEvent(
            event_id=f"event:{pid}",
            kind="EDGE_REMOVE",
            event_time="2026-09-30T11:25:01Z",
            ingest_time="2026-09-30T11:25:01.001000Z",
            payload={"from": "ROOT", "relation": relation, "to": target},
        ),
    )


def main():
    # Independent proposals authored against the same revision commute and are
    # published atomically as one new workspace revision.
    p1 = upsert("P1", "agent:alpha", 0, "SUPPORTS", "X", "agent:alpha")
    p2 = upsert("P2", "agent:beta", 0, "REFINES", "Y", "agent:beta")
    digests = set()
    for order in permutations((p1, p2)):
        tx = fresh()
        result = tx.commit(order)
        assert result.status == "COMMITTED"
        assert result.base_revision == 0
        assert result.new_revision == 1
        assert set(result.applied_proposals) == {"P1", "P2"}
        assert len(result.sparse_patches) == 2
        assert ("ROOT", "SUPPORTS", "X") in tx.workspace.edges
        assert ("ROOT", "REFINES", "Y") in tx.workspace.edges
        digests.add(tx.state_digest)
    assert len(digests) == 1

    # Identical concurrent intents coalesce. Actor identity confers no extra
    # authority and does not cause duplicate semantic mutations.
    d1 = upsert("D1", "agent:senior", 0, "SUPPORTS", "Z", "shared:source")
    d2 = upsert("D2", "agent:junior", 0, "SUPPORTS", "Z", "shared:source")
    tx = fresh()
    duplicate = tx.commit((d2, d1))
    assert duplicate.status == "COMMITTED"
    assert duplicate.new_revision == 1
    assert duplicate.applied_proposals == ("D1",)
    assert duplicate.duplicate_proposals == ("D2",)
    assert len(duplicate.sparse_patches) == 1

    # Two contradictory intents for the same semantic slot are not resolved by
    # actor name, arrival order, or last-writer-wins. The whole batch is atomic.
    c1 = upsert("C1", "agent:alpha", 0, "CLAIMS", "Q", "source:alpha")
    c2 = upsert("C2", "agent:omega", 0, "CLAIMS", "Q", "source:omega")
    independent = upsert("C3", "agent:third", 0, "INDEPENDENT", "R", "source:third")
    conflict_digests = set()
    for order in ((c1, c2, independent), (independent, c2, c1)):
        tx = fresh()
        before = tx.state_digest
        result = tx.commit(order)
        assert result.status == "CONFLICT"
        assert result.new_revision == 0
        assert result.state_digest_before == before == result.state_digest_after
        assert tx.state_digest == before
        assert ("ROOT", "INDEPENDENT", "R") not in tx.workspace.edges
        assert result.conflict_targets == ("EDGE|ROOT|CLAIMS|Q",)
        conflict_digests.add(tx.state_digest)
    assert len(conflict_digests) == 1

    # SET vs REMOVE on one existing edge is also an explicit conflict.
    tx = fresh()
    r1 = remove("R1", "agent:alpha", 0, "BASE", "A")
    r2 = upsert("R2", "agent:beta", 0, "BASE", "A", "replacement:beta")
    before = tx.state_digest
    result = tx.commit((r1, r2))
    assert result.status == "CONFLICT"
    assert tx.state_digest == before
    assert ("ROOT", "BASE", "A") in tx.workspace.edges

    # Old revisions never commit silently after another transaction succeeds.
    tx = fresh()
    first = tx.commit((upsert("F1", "agent:first", 0, "STEP", "N1", "source:first"),))
    assert first.status == "COMMITTED"
    assert tx.revision == 1
    stale_before = tx.state_digest
    stale = tx.commit((upsert("S1", "agent:late", 0, "STEP", "N2", "source:late"),))
    assert stale.status == "REBASE_REQUIRED"
    assert stale.new_revision == 1
    assert tx.state_digest == stale_before
    assert ("ROOT", "STEP", "N2") not in tx.workspace.edges

    # Non-admitted FORUM observation cannot hitchhike inside an otherwise valid
    # transaction. The complete batch fails closed and leaves no partial write.
    tx = fresh()
    forum_seen = Proposal(
        proposal_id="G1",
        actor_id="agent:observer",
        base_revision=0,
        event=MemoryEvent(
            event_id="event:G1",
            kind="FORUM_OBJECT_SEEN",
            event_time="2026-09-30T11:25:02Z",
            ingest_time="2026-09-30T11:25:02.001000Z",
            payload={"oid": "OID-X", "kind": "RELATION"},
        ),
    )
    valid = upsert("G2", "agent:writer", 0, "SAFE", "T", "source:safe")
    before = tx.state_digest
    invalid = tx.commit((valid, forum_seen))
    assert invalid.status == "INVALID_BATCH"
    assert tx.state_digest == before
    assert ("ROOT", "SAFE", "T") not in tx.workspace.edges

    print("PSI-ACTIVE-MEMORY-CONCURRENCY-01 PASS_WITH_BOUNDARY")
    print("independent_same_revision_atomic_commit=PASS")
    print("proposal_order_invariance=PASS")
    print("identical_intent_coalescing=PASS")
    print("actor_identity_no_priority=PASS")
    print("conflict_fail_closed_no_partial_write=PASS")
    print("stale_revision_requires_rebase=PASS")
    print("forum_observation_cannot_hitchhike=PASS")
    print("BOUNDARY: deterministic single-process transaction oracle using deep-copy publish; no threads, distributed consensus, crash recovery, MVCC, or live FORUM writes")


if __name__ == "__main__":
    main()
