#!/usr/bin/env python3
from active_memory import (
    MemoryEvent,
    apply_delta,
    compile_sparse_planes,
    compile_workspace,
    consolidate_workspace,
    forum_object_to_event,
    restore_workspace,
    snapshot_stale,
)

CONTRACT = {
    "status": "COMPILED",
    "contract_id": "ACTIVE-MEMORY-TEST",
    "anchor": "II.9",
    "task": "preserve typed local relations under incremental updates",
}
RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "II.9",
    "edges": [
        {"from": "II.9", "relation": "DEPENDS_ON", "to": "II.7", "source": "doc:a"},
        {"from": "II.9", "relation": "ANALOGY_TO", "to": "II.6", "source": "doc:b"},
        {"from": "II.9", "relation": "NOT_DEPENDS_ON", "to": "II.8", "source": "doc:c"},
    ],
}


def ev(eid, kind, payload):
    return MemoryEvent(
        event_id=eid,
        kind=kind,
        event_time="2026-09-30T10:00:00Z",
        ingest_time="2026-09-30T10:00:01Z",
        payload=payload,
    )


def main():
    ws0 = compile_workspace(CONTRACT, RETRIEVAL)
    assert ws0.revision == 0
    assert len(ws0.edges) == 3

    planes = compile_sparse_planes(ws0)
    assert planes["shape"] == [4, 4]
    assert set(planes["relations"]) == {"DEPENDS_ON", "ANALOGY_TO", "NOT_DEPENDS_ON"}
    assert sum(len(v) for v in planes["relations"].values()) == 3

    unrelated = ev("u1", "EDGE_UPSERT", {
        "from": "X", "relation": "SUPPORT", "to": "Y", "source": "forum:x"
    })
    r0 = apply_delta(ws0, [unrelated])
    assert r0.workspace.state_digest == ws0.state_digest
    assert r0.ignored_events == ("u1",)

    related = ev("r1", "EDGE_UPSERT", {
        "from": "II.7", "relation": "REFINES", "to": "II.5", "source": "forum:r1"
    })
    r1 = apply_delta(ws0, [related])
    assert r1.workspace.revision == 1
    assert r1.affected_nodes == ("II.5", "II.7")
    assert ("II.7", "REFINES", "II.5") in r1.workspace.edges

    r2 = apply_delta(r1.workspace, [related])
    assert r2.workspace.state_digest == r1.workspace.state_digest
    assert r2.ignored_events == ("r1",)

    snap = consolidate_workspace(r1.workspace)
    restored = restore_workspace(snap)
    assert restored.state_digest == r1.workspace.state_digest
    assert not snapshot_stale(snap, {"source:unrelated"})
    assert snapshot_stale(snap, {"source:forum:r1"})

    claim = forum_object_to_event(
        "OID-CLAIM",
        {"kind": "CLAIM", "payload": {"text": "x"}},
        event_time="2026-09-30T10:01:00Z",
    )
    c = apply_delta(r1.workspace, [claim])
    assert c.workspace.state_digest == r1.workspace.state_digest

    relation_obj = {
        "kind": "RELATION",
        "payload": {"from": "II.5", "relation": "SUPPORT", "to": "II.4"},
    }
    relation_seen = forum_object_to_event(
        "OID-REL", relation_obj, event_time="2026-09-30T10:02:00Z"
    )
    seen = apply_delta(r1.workspace, [relation_seen])
    assert seen.workspace.state_digest == r1.workspace.state_digest

    relation = forum_object_to_event(
        "OID-REL",
        relation_obj,
        event_time="2026-09-30T10:02:00Z",
        admitted=True,
    )
    f = apply_delta(r1.workspace, [relation])
    assert ("II.5", "SUPPORT", "II.4") in f.workspace.edges
    assert "source:forum:OID-REL" in f.workspace.dependencies

    fp = compile_sparse_planes(f.workspace)
    assert "SUPPORT" in fp["relations"]
    assert "REFINES" in fp["relations"]
    assert len(fp["nodes"]) == 6

    try:
        MemoryEvent("bad-time", "FORUM_OBJECT_SEEN", "2026-09-30T10:00:00", "2026-09-30T10:00:01Z", {})
        raise AssertionError("naive event time accepted")
    except ValueError:
        pass

    print("PSI-ACTIVE-MEMORY-01 PASS")
    print(f"baseline_edges={len(ws0.edges)}")
    print(f"updated_edges={len(f.workspace.edges)}")
    print(f"affected_related={len(r1.affected_edges)}")
    print(f"snapshot={snap['id']}")


if __name__ == "__main__":
    main()
