#!/usr/bin/env python3
from __future__ import annotations

from itertools import permutations
from statistics import median
from time import perf_counter_ns

from active_memory import MemoryEvent, compile_workspace
from concurrent_workspace import ConcurrentWorkspace, Proposal
from mvcc_workspace import MVCCWorkspace, MVCCProposal

CONTRACT = {
    "status": "COMPILED",
    "contract_id": "ACTIVE-MEMORY-MVCC-01",
    "anchor": "ROOT",
    "task": "test local optimistic MVCC over active memory",
}
BASE_RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "ROOT",
    "edges": [
        {"from": "ROOT", "relation": "BASE", "to": "A", "source": "seed:A", "status": "ADMITTED"},
        {"from": "ROOT", "relation": "BASE", "to": "B", "source": "seed:B", "status": "ADMITTED"},
    ],
}
SIZES = (128, 1024, 8192, 32768)
REPEATS = 5


def fresh(retrieval=None):
    return MVCCWorkspace(compile_workspace(CONTRACT, retrieval or BASE_RETRIEVAL))


def event(pid: str, relation: str, target: str, source: str):
    return MemoryEvent(
        event_id=f"event:{pid}",
        kind="EDGE_UPSERT",
        event_time="2026-09-30T11:35:00Z",
        ingest_time="2026-09-30T11:35:00.001000Z",
        payload={
            "from": "ROOT",
            "relation": relation,
            "to": target,
            "source": source,
            "status": "ADMITTED",
        },
    )


def upsert(pid: str, actor: str, base: int, relation: str, target: str, source: str, reads=()):
    return MVCCProposal(
        proposal_id=pid,
        actor_id=actor,
        base_revision=base,
        event=event(pid, relation, target, source),
        read_set=tuple(reads),
    )


def reference_proposal(p: MVCCProposal):
    return Proposal(
        proposal_id=p.proposal_id,
        actor_id=p.actor_id,
        base_revision=p.base_revision,
        event=p.event,
    )


def noise_retrieval(n: int):
    edges = list(BASE_RETRIEVAL["edges"])
    for i in range(n):
        edges.append({
            "from": "ROOT",
            "relation": f"NOISE_{i:06d}",
            "to": f"N{i:06d}",
            "source": f"noise:{i:06d}",
            "status": "ADMITTED",
        })
    return {"status": "RETRIEVED", "anchor": "ROOT", "edges": edges}


def main():
    base_a = MVCCWorkspace.edge_token("ROOT", "BASE", "A")
    base_b = MVCCWorkspace.edge_token("ROOT", "BASE", "B")
    x_slot = MVCCWorkspace.edge_token("ROOT", "STEP", "X")

    p1 = upsert("P1", "agent:alpha", 0, "SUPPORTS", "X", "source:alpha", (base_a,))
    p2 = upsert("P2", "agent:beta", 0, "REFINES", "Y", "source:beta", (base_b,))
    digests = set()
    for order in permutations((p1, p2)):
        tx = fresh()
        result = tx.commit(order)
        assert result.status == "COMMITTED"
        assert result.new_revision == 1
        assert set(result.applied_proposals) == {"P1", "P2"}
        assert result.examined_versions == 4
        digests.add(tx.semantic_digest)
    assert len(digests) == 1

    ref = ConcurrentWorkspace(compile_workspace(CONTRACT, BASE_RETRIEVAL))
    mvcc = fresh()
    ref_result = ref.commit((reference_proposal(p1), reference_proposal(p2)))
    mvcc_result = mvcc.commit((p1, p2))
    assert ref_result.status == mvcc_result.status == "COMMITTED"
    assert ref.state_digest == mvcc.semantic_digest

    tx = fresh()
    first = tx.commit((upsert("F1", "agent:first", 0, "STEP", "X", "source:first", (base_a,)),))
    assert first.status == "COMMITTED"
    assert tx.revision == 1
    independent_old_snapshot = upsert(
        "F2", "agent:late-independent", 0, "STEP", "Y", "source:late", (base_b,)
    )
    second = tx.commit((independent_old_snapshot,))
    assert second.status == "COMMITTED"
    assert tx.revision == 2
    assert ("ROOT", "STEP", "Y") in tx.workspace.edges

    tx = fresh()
    assert tx.commit((upsert("S0", "agent:first", 0, "STEP", "X", "source:first", (base_a,)),)).status == "COMMITTED"
    stale_read = upsert("S1", "agent:reader", 0, "OTHER", "Z", "source:z", (x_slot,))
    result = tx.commit((stale_read,))
    assert result.status == "REBASE_REQUIRED"
    assert result.stale_tokens == (x_slot,)
    assert ("ROOT", "OTHER", "Z") not in tx.workspace.edges

    stale_write = upsert("S2", "agent:writer", 0, "STEP", "X", "source:replacement", (base_a,))
    result = tx.commit((stale_write,))
    assert result.status == "REBASE_REQUIRED"
    assert x_slot in result.stale_tokens

    tx = fresh()
    a = upsert("H1", "agent:a", 0, "STEP", "X", "source:a", (base_a,))
    b = upsert("H2", "agent:b", 0, "STEP", "Y", "source:b", (x_slot,))
    before = tx.semantic_digest
    result = tx.commit((a, b))
    assert result.status == "CONFLICT"
    assert result.conflict_tokens == (x_slot,)
    assert tx.semantic_digest == before
    assert ("ROOT", "STEP", "X") not in tx.workspace.edges
    assert ("ROOT", "STEP", "Y") not in tx.workspace.edges

    tx = fresh()
    c1 = upsert("C1", "agent:senior", 0, "CLAIMS", "Q", "source:one", (base_a,))
    c2 = upsert("C2", "agent:junior", 0, "CLAIMS", "Q", "source:two", (base_a,))
    independent = upsert("C3", "agent:third", 0, "OTHER", "R", "source:three", (base_b,))
    before = tx.semantic_digest
    result = tx.commit((c2, independent, c1))
    assert result.status == "CONFLICT"
    assert tx.semantic_digest == before
    assert ("ROOT", "OTHER", "R") not in tx.workspace.edges

    tx = fresh()
    d1 = upsert("D1", "agent:senior", 0, "SUPPORTS", "D", "shared", (base_a,))
    d2 = upsert("D2", "agent:junior", 0, "SUPPORTS", "D", "shared", (base_a,))
    result = tx.commit((d2, d1))
    assert result.status == "COMMITTED"
    assert result.applied_proposals == ("D1",)
    assert result.duplicate_proposals == ("D2",)
    assert result.examined_versions == 4

    tx = fresh()
    forum_seen = MVCCProposal(
        proposal_id="G1",
        actor_id="agent:observer",
        base_revision=0,
        event=MemoryEvent(
            event_id="event:G1",
            kind="FORUM_OBJECT_SEEN",
            event_time="2026-09-30T11:35:01Z",
            ingest_time="2026-09-30T11:35:01.001000Z",
            payload={"oid": "OID-MVCC", "kind": "RELATION"},
        ),
    )
    valid = upsert("G2", "agent:writer", 0, "SAFE", "T", "source:safe", (base_a,))
    before = tx.semantic_digest
    result = tx.commit((valid, forum_seen))
    assert result.status == "INVALID_BATCH"
    assert tx.semantic_digest == before
    assert ("ROOT", "SAFE", "T") not in tx.workspace.edges

    rows = []
    for n in SIZES:
        retrieval = noise_retrieval(n)
        mvcc_times = []
        ref_times = []
        for repeat in range(REPEATS):
            p = upsert(
                f"M{n}-{repeat}",
                "agent:scale",
                0,
                "HOT",
                f"X{repeat}",
                "source:scale",
                (base_a,),
            )

            tx = MVCCWorkspace(compile_workspace(CONTRACT, retrieval))
            t0 = perf_counter_ns()
            result = tx.commit((p,))
            t1 = perf_counter_ns()
            assert result.status == "COMMITTED"
            assert result.examined_versions == 2
            mvcc_times.append(t1 - t0)
            mvcc_digest = tx.semantic_digest

            ref = ConcurrentWorkspace(compile_workspace(CONTRACT, retrieval))
            rp = reference_proposal(p)
            t2 = perf_counter_ns()
            ref_result = ref.commit((rp,))
            t3 = perf_counter_ns()
            assert ref_result.status == "COMMITTED"
            ref_times.append(t3 - t2)
            assert ref.state_digest == mvcc_digest

        mt = int(median(mvcc_times))
        rt = int(median(ref_times))
        rows.append((n, mt, rt))
        print(
            f"noise_edges={n} examined_versions=2 "
            f"mvcc_median_ns={mt} deepcopy_reference_median_ns={rt} "
            f"observed_ratio={rt / max(mt, 1):.2f}"
        )

    assert rows[-1][0] / rows[0][0] == 256

    print("PSI-ACTIVE-MEMORY-MVCC-01 PASS_WITH_BOUNDARY")
    print("same_snapshot_atomic_commit=PASS")
    print("reference_semantic_equivalence=PASS")
    print("independent_stale_snapshot_commit=PASS")
    print("stale_read_rebase=PASS")
    print("stale_write_rebase=PASS")
    print("intra_batch_read_write_conflict=PASS")
    print("conflicting_writes_fail_closed=PASS")
    print("identical_intent_coalescing=PASS")
    print("actor_identity_no_priority=PASS")
    print("forum_observation_cannot_hitchhike=PASS")
    print("indexed_work_accounting=2_version_checks_for_scaling_witness")
    print("timing_claim=MEASURED_NOT_PROOF")
    print(
        "BOUNDARY: single-process crash-free optimistic MVCC with explicit read sets; "
        "no threads, durable WAL, recovery, distributed clocks/consensus, live FORUM writes, or GPU execution"
    )


if __name__ == "__main__":
    main()
