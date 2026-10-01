#!/usr/bin/env python3
from __future__ import annotations

from statistics import median
from time import perf_counter_ns

from active_memory import compile_workspace, forum_object_to_event
from active_memory_runtime import semantic_digest
from multiworkspace_runtime import MultiWorkspaceRuntime


def make_workspace(contract_id: str, anchor: str, relation: str, target: str, source: str):
    contract = {
        "status": "COMPILED",
        "contract_id": contract_id,
        "anchor": anchor,
        "task": f"active workspace {contract_id}",
    }
    retrieval = {
        "status": "RETRIEVED",
        "anchor": anchor,
        "edges": [
            {"from": anchor, "relation": relation, "to": target, "source": source, "status": "ADMITTED"}
        ],
    }
    return compile_workspace(contract, retrieval)


def admitted_forum_relation(oid: str, source_node: str, target_node: str):
    return forum_object_to_event(
        oid,
        {
            "kind": "RELATION",
            "payload": {"from": source_node, "relation": "SUPPORTS", "to": target_node},
        },
        event_time="2026-09-30T11:20:00Z",
        ingest_time="2026-09-30T11:20:00.001000Z",
        admitted=True,
    )


def seen_only_forum_relation(oid: str, source_node: str, target_node: str):
    return forum_object_to_event(
        oid,
        {
            "kind": "RELATION",
            "payload": {"from": source_node, "relation": "SUPPORTS", "to": target_node},
        },
        event_time="2026-09-30T11:19:00Z",
        ingest_time="2026-09-30T11:19:00.001000Z",
        admitted=False,
    )


def semantic_witness():
    hub = MultiWorkspaceRuntime()
    proof = make_workspace("MW-PROOF", "PROOF", "DEPENDS_ON", "A", "doc:proof")
    chemistry = make_workspace("MW-CHEM", "CHEM", "REACTS_WITH", "X", "doc:chem")
    downstream = make_workspace("MW-DOWN", "DOWN", "USES", "Y", "doc:down")

    hub.register("proof", proof)
    hub.register("chemistry", chemistry)
    hub.register("downstream", downstream, extra_dependencies=("workspace:proof",))

    proof_before = semantic_digest(hub.workspace("proof"))
    chem_before = semantic_digest(hub.workspace("chemistry"))
    down_before = semantic_digest(hub.workspace("downstream"))

    seen = seen_only_forum_relation("OID-MW-SEEN", "A", "P2")
    seen_result = hub.dispatch(seen)
    assert seen_result.examined_workspaces == 0
    assert seen_result.mutations == 0
    assert semantic_digest(hub.workspace("proof")) == proof_before

    event = admitted_forum_relation("OID-MW", "A", "P2")
    routed = hub.dispatch(event)
    assert routed.candidate_workspaces == ("proof",)
    assert routed.delivered_workspaces == ("proof",)
    assert routed.examined_workspaces == 1
    assert routed.mutations == 1
    assert len(routed.routed_patches) == 1
    assert routed.routed_patches[0].workspace_id == "proof"
    assert routed.routed_patches[0].patch.relation == "SUPPORTS"
    assert semantic_digest(hub.workspace("proof")) != proof_before
    assert semantic_digest(hub.workspace("chemistry")) == chem_before
    assert semantic_digest(hub.workspace("downstream")) == down_before
    assert "source:forum:OID-MW" in hub.dependency_tokens("proof")

    duplicate = hub.dispatch(event)
    assert duplicate.candidate_workspaces == ("proof",)
    assert duplicate.delivered_workspaces == ()
    assert duplicate.ignored_workspaces == ("proof",)
    assert duplicate.mutations == 0

    invalidated = hub.invalidate(("source:forum:OID-MW",))
    assert invalidated.stale_workspaces == ("downstream", "proof")
    assert invalidated.examined_dependency_links == 2
    assert hub.status("proof") == "NEEDS_RECHECK"
    assert hub.status("downstream") == "NEEDS_RECHECK"
    assert hub.status("chemistry") == "VALID"
    assert semantic_digest(hub.workspace("chemistry")) == chem_before
    assert semantic_digest(hub.workspace("downstream")) == down_before

    unknown = hub.invalidate(("source:not-present",))
    assert unknown.stale_workspaces == ()
    assert unknown.examined_dependency_links == 0


SIZES = (128, 1024, 4096, 16384)
REPEATS = 5


def scaling_witness():
    rows = []
    for n in SIZES:
        times = []
        for rep in range(REPEATS):
            hub = MultiWorkspaceRuntime()
            target = make_workspace("MW-TARGET", "TARGET", "DEPENDS_ON", "A", "doc:target")
            hub.register("target", target)
            for i in range(n):
                wid = f"noise:{i:05d}"
                anchor = f"Z{i:05d}"
                node = f"N{i:05d}"
                ws = make_workspace(f"MW-NOISE-{i}", anchor, "NOISE_REL", node, f"noise:{i}")
                hub.register(wid, ws)

            event = admitted_forum_relation(f"OID-SCALE-{n}-{rep}", "A", "NEW")
            t0 = perf_counter_ns()
            result = hub.dispatch(event)
            t1 = perf_counter_ns()
            times.append(t1 - t0)

            assert hub.workspace_count == n + 1
            assert result.candidate_workspaces == ("target",)
            assert result.delivered_workspaces == ("target",)
            assert result.examined_workspaces == 1
            assert result.mutations == 1
            assert len(result.routed_patches) == 1

        dt = int(median(times))
        rows.append((n, dt))
        print(
            f"noise_workspaces={n} total_workspaces={n + 1} "
            f"candidate_workspaces=1 examined_workspaces=1 "
            f"dispatch_median_ns={dt} naive_scan_workspaces={n + 1}"
        )

    assert rows[-1][0] / rows[0][0] == 128


def main():
    semantic_witness()
    scaling_witness()
    print("PSI-ACTIVE-MEMORY-MULTIWORKSPACE-01 PASS_WITH_BOUNDARY")
    print("selective_event_routing=PASS")
    print("unaffected_workspace_semantic_digest=PASS")
    print("forum_seen_without_admission_no_delivery=PASS")
    print("transitive_workspace_invalidation=PASS")
    print("indexed_work_accounting=1_candidate_workspace")
    print("timing_claim=MEASURED_NOT_PROOF")
    print("BOUNDARY: single-process single-writer coordinator; no concurrent commits, rollback, network transport, live FORUM mutation, or GPU execution")


if __name__ == "__main__":
    main()
