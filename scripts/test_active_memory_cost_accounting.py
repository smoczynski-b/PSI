#!/usr/bin/env python3
from __future__ import annotations

from active_memory import MemoryEvent, compile_workspace
from multiworkspace_runtime import MultiWorkspaceRuntime


def workspace_with_edges(n: int, *, history: int = 0):
    contract = {
        "status": "COMPILED",
        "contract_id": f"COST-{n}-{history}",
        "anchor": "ROOT",
        "task": "measure hidden local update work",
    }
    retrieval = {
        "status": "RETRIEVED",
        "anchor": "ROOT",
        "edges": [
            {
                "from": "ROOT",
                "relation": "BASE",
                "to": f"N{i}",
                "source": f"seed:{i}",
                "status": "ADMITTED",
            }
            for i in range(n)
        ],
    }
    ws = compile_workspace(contract, retrieval)
    ws.processed_events = tuple(f"old:{i}" for i in range(history))
    return ws


def event(tag: str):
    return MemoryEvent(
        event_id=f"delta:{tag}",
        kind="EDGE_UPSERT",
        event_time="2026-09-30T16:00:00Z",
        ingest_time="2026-09-30T16:00:00.001000Z",
        payload={
            "from": "ROOT",
            "relation": "DELTA",
            "to": "NEW",
            "source": "bench:delta",
            "status": "ADMITTED",
        },
    )


def one_update(edge_count: int, history_count: int):
    hub = MultiWorkspaceRuntime()
    hub.register("target", workspace_with_edges(edge_count, history=history_count))
    result = hub.dispatch(event(f"{edge_count}:{history_count}"))

    assert result.candidate_workspaces == ("target",)
    assert result.delivered_workspaces == ("target",)
    assert result.examined_workspaces == 1
    assert result.examined_events == 1
    assert result.mutations == 1
    assert result.history_items_appended == 1

    # After the delta the workspace has edge_count+1 edges. Current refresh
    # materializes `nodes` once and `dependencies` once, hence two full scans.
    assert result.index_refresh_edge_visits == 2 * (edge_count + 1)

    # The delta adds one node plus two dependency tokens: edge identity and
    # provenance. This local index-diff work stays bounded even though discovery
    # of the diff currently requires the full edge scans above.
    assert result.index_node_membership_updates == 1
    assert result.index_dependency_membership_updates == 2
    assert result.index_membership_updates == 3

    # Tuple-backed processed_events recopies the whole previous history.
    assert result.history_items_copied == history_count
    return result


def main():
    # Edge-size witness reproduces the hidden cost observed in audit 04:
    # one selected workspace, yet refresh work grows with its local edge count.
    small = one_update(8, 0)
    large = one_update(1024, 0)
    assert small.index_refresh_edge_visits == 18
    assert large.index_refresh_edge_visits == 2050
    assert small.examined_workspaces == large.examined_workspaces == 1
    assert large.index_refresh_edge_visits > 100 * small.index_refresh_edge_visits

    # History-size witness is independent of graph size: one new event still
    # recopies every old event id under the present tuple representation.
    short_history = one_update(1, 8)
    long_history = one_update(1, 1024)
    assert short_history.index_refresh_edge_visits == long_history.index_refresh_edge_visits == 4
    assert short_history.history_items_copied == 8
    assert long_history.history_items_copied == 1024
    assert long_history.history_items_copied == 128 * short_history.history_items_copied

    # Unrelated global workspaces are not scanned by routing; the discovered
    # non-locality is inside the selected workspace/history, not across all views.
    hub = MultiWorkspaceRuntime()
    hub.register("target", workspace_with_edges(8))
    for i in range(2048):
        contract = {
            "status": "COMPILED",
            "contract_id": f"NOISE-{i}",
            "anchor": f"Z{i}",
            "task": "noise",
        }
        retrieval = {
            "status": "RETRIEVED",
            "anchor": f"Z{i}",
            "edges": [{
                "from": f"Z{i}",
                "relation": "NOISE",
                "to": f"Q{i}",
                "source": f"noise:{i}",
                "status": "ADMITTED",
            }],
        }
        hub.register(f"noise:{i}", compile_workspace(contract, retrieval))
    routed = hub.dispatch(event("global-noise"))
    assert hub.workspace_count == 2049
    assert routed.examined_workspaces == 1
    assert routed.index_refresh_edge_visits == 18

    print("PSI-ACTIVE-MEMORY-COST-ACCOUNTING-01 PASS_WITH_BOUNDARY")
    print("selective_global_routing=PASS")
    print("examined_workspaces=1_with_2049_total")
    print("local_index_refresh_edge_visits_8_edges=18")
    print("local_index_refresh_edge_visits_1024_edges=2050")
    print("history_items_copied_8=8")
    print("history_items_copied_1024=1024")
    print("CLAIM_CORRECTION: routing is selective across workspaces, but the current full local update path is not O(|delta|); index refresh is O(|E_workspace|) and tuple-backed event-history append is O(|history|)")
    print("BOUNDARY: counters expose deterministic logical work in the present reference implementation; they are not CPU-cycle or memory-bandwidth measurements")


if __name__ == "__main__":
    main()
