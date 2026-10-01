#!/usr/bin/env python3
from __future__ import annotations

from active_memory import MemoryEvent, compile_workspace
from active_memory_runtime import semantic_digest
from mvcc_workspace import MVCCProposal
from shared_memory_runtime import SharedMemoryRuntime

CONTRACT = {
    "status": "COMPILED",
    "contract_id": "ACTIVE-MEMORY-SHARED-01",
    "anchor": "ROOT",
    "task": "test shared MVCC-to-workspace propagation",
}

GLOBAL_RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "ROOT",
    "edges": [
        {"from": "ROOT", "relation": "BASE", "to": "A", "source": "seed:A", "status": "ADMITTED"},
        {"from": "ROOT", "relation": "BASE", "to": "C", "source": "seed:C", "status": "ADMITTED"},
    ],
}


def view(anchor: str, node: str, source: str):
    contract = dict(CONTRACT)
    contract["contract_id"] = f"VIEW-{anchor}-{node}"
    contract["anchor"] = anchor
    retrieval = {
        "status": "RETRIEVED",
        "anchor": anchor,
        "edges": [
            {"from": anchor, "relation": "BASE", "to": node, "source": source, "status": "ADMITTED"},
        ],
    }
    return compile_workspace(contract, retrieval)


def upsert(pid: str, actor: str, base: int, source_node: str, relation: str, target: str, provenance: str):
    return MVCCProposal(
        proposal_id=pid,
        actor_id=actor,
        base_revision=base,
        event=MemoryEvent(
            event_id=f"event:{pid}",
            kind="EDGE_UPSERT",
            event_time="2026-09-30T11:45:00Z",
            ingest_time="2026-09-30T11:45:00.001000Z",
            payload={
                "from": source_node,
                "relation": relation,
                "to": target,
                "source": provenance,
                "status": "ADMITTED",
            },
        ),
    )


def fresh() -> SharedMemoryRuntime:
    shared = SharedMemoryRuntime(compile_workspace(CONTRACT, GLOBAL_RETRIEVAL))
    shared.register("proof", view("ROOT", "A", "seed:A"))
    shared.register("chem", view("ROOT", "C", "seed:C"))
    shared.register(
        "downstream",
        view("DROOT", "D", "seed:D"),
        extra_dependencies=("workspace:proof",),
    )
    return shared


def main():
    # Two agents commit one atomic shared-memory transaction. Each accepted
    # event is routed only into the local view whose active node it touches.
    shared = fresh()
    proof_before = semantic_digest(shared.workspace("proof"))
    chem_before = semantic_digest(shared.workspace("chem"))
    down_before = semantic_digest(shared.workspace("downstream"))

    p1 = upsert("P1", "agent:proof", 0, "A", "SUPPORTS", "P", "forum:OID-P")
    p2 = upsert("P2", "agent:chem", 0, "C", "TRANSFORMS", "Q", "sensor:CHEM-Q")
    result = shared.commit((p1, p2))

    assert result.status == "COMMITTED"
    assert result.base_revision == 0 and result.new_revision == 1
    assert set(result.applied_proposals) == {"P1", "P2"}
    assert set(result.delivered_workspaces) == {"proof", "chem"}
    assert result.examined_workspaces == 2
    assert len(result.routed_patches) == 2
    assert ("A", "SUPPORTS", "P") in shared.workspace("proof").edges
    assert ("C", "TRANSFORMS", "Q") in shared.workspace("chem").edges
    assert semantic_digest(shared.workspace("proof")) != proof_before
    assert semantic_digest(shared.workspace("chem")) != chem_before
    assert semantic_digest(shared.workspace("downstream")) == down_before
    assert shared.status("proof") == "VALID"
    assert shared.status("chem") == "VALID"
    assert shared.status("downstream") == "NEEDS_RECHECK"
    assert result.invalidated_workspaces == ("downstream",)
    assert result.examined_dependency_links == 1

    # A rejected FORUM observation is stopped at the MVCC boundary and therefore
    # cannot route or invalidate anything downstream.
    proof_after = semantic_digest(shared.workspace("proof"))
    down_after = semantic_digest(shared.workspace("downstream"))
    forum_seen = MVCCProposal(
        proposal_id="F1",
        actor_id="agent:observer",
        base_revision=shared.revision,
        event=MemoryEvent(
            event_id="event:F1",
            kind="FORUM_OBJECT_SEEN",
            event_time="2026-09-30T11:45:01Z",
            ingest_time="2026-09-30T11:45:01.001000Z",
            payload={"oid": "OID-UNADMITTED", "kind": "RELATION"},
        ),
    )
    rejected = shared.commit((forum_seen,))
    assert rejected.status == "INVALID_BATCH"
    assert rejected.delivered_workspaces == ()
    assert rejected.invalidated_workspaces == ()
    assert rejected.examined_workspaces == 0
    assert semantic_digest(shared.workspace("proof")) == proof_after
    assert semantic_digest(shared.workspace("downstream")) == down_after

    # Scaling witness: thousands of unrelated workspaces do not increase the
    # number of routed views or dependency links examined for one local event.
    noise = SharedMemoryRuntime(compile_workspace(CONTRACT, GLOBAL_RETRIEVAL))
    noise.register("proof", view("ROOT", "A", "seed:A"))
    noise.register(
        "downstream",
        view("DROOT", "D", "seed:D"),
        extra_dependencies=("workspace:proof",),
    )
    for i in range(4096):
        noise.register(f"noise:{i}", view(f"NROOT:{i}", f"N:{i}", f"noise:{i}"))

    local = upsert("S1", "agent:proof", 0, "A", "REFINES", "S", "source:scale")
    scaled = noise.commit((local,))
    assert scaled.status == "COMMITTED"
    assert scaled.delivered_workspaces == ("proof",)
    assert scaled.invalidated_workspaces == ("downstream",)
    assert scaled.examined_workspaces == 1
    assert scaled.examined_dependency_links == 1
    assert scaled.examined_versions == 1

    print("PSI-ACTIVE-MEMORY-SHARED-01 PASS_WITH_BOUNDARY")
    print("mvcc_commit_to_selective_routing=PASS")
    print("multiagent_atomic_commit=PASS")
    print("direct_views_updated=PASS")
    print("downstream_workspace_invalidation=PASS")
    print("unrelated_workspace_semantic_digest=PASS")
    print("forum_observation_stops_before_routing=PASS")
    print("scaling_examined_versions=1")
    print("scaling_examined_workspaces=1")
    print("scaling_examined_dependency_links=1")
    print("BOUNDARY: single-process crash-free integration; local view propagation follows authoritative commit but is not yet protected by durable WAL/two-phase recovery, threads/processes, distributed consensus, live FORUM writes, or GPU execution")


if __name__ == "__main__":
    main()
