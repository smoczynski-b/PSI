#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import json

from active_memory import MemoryEvent, compile_workspace
from active_memory_runtime import semantic_digest
from durable_shared_memory import DurableSharedMemoryRuntime, SimulatedCrash, WALCorruption
from mvcc_workspace import MVCCProposal

CONTRACT = {
    "status": "COMPILED",
    "contract_id": "ACTIVE-MEMORY-WAL-01",
    "anchor": "ROOT",
    "task": "test durable shared-memory recovery",
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


def authoritative_seed():
    return compile_workspace(CONTRACT, GLOBAL_RETRIEVAL)


def register_views(shared):
    shared.register("proof", view("ROOT", "A", "seed:A"))
    shared.register("chem", view("ROOT", "C", "seed:C"))
    shared.register(
        "downstream",
        view("DROOT", "D", "seed:D"),
        extra_dependencies=("workspace:proof",),
    )


def upsert(pid: str, actor: str, base: int, source_node: str, relation: str, target: str, provenance: str):
    return MVCCProposal(
        proposal_id=pid,
        actor_id=actor,
        base_revision=base,
        event=MemoryEvent(
            event_id=f"event:{pid}",
            kind="EDGE_UPSERT",
            event_time="2026-09-30T12:00:00Z",
            ingest_time="2026-09-30T12:00:00.001000Z",
            payload={
                "from": source_node,
                "relation": relation,
                "to": target,
                "source": provenance,
                "status": "ADMITTED",
            },
        ),
    )


def make_runtime(path: Path):
    return DurableSharedMemoryRuntime(authoritative_seed(), path, register_views)


def main():
    p1 = upsert("P1", "agent:proof", 0, "A", "SUPPORTS", "P", "forum:OID-P")
    p2 = upsert("P2", "agent:chem", 0, "C", "TRANSFORMS", "Q", "sensor:CHEM-Q")

    # Clean commit establishes the reference state and survives a full restart.
    with TemporaryDirectory() as td:
        wal = Path(td) / "memory.wal"
        live = make_runtime(wal)
        clean = live.commit("TX-CLEAN", (p1, p2))
        assert clean.wal_state == "ACK"
        assert clean.result.status == "COMMITTED"
        assert live.revision == 1
        proof_ref = semantic_digest(live.workspace("proof"))
        chem_ref = semantic_digest(live.workspace("chem"))
        down_ref = semantic_digest(live.workspace("downstream"))
        assert live.status("downstream") == "NEEDS_RECHECK"

        restarted = make_runtime(wal)
        assert restarted.revision == 1
        assert semantic_digest(restarted.workspace("proof")) == proof_ref
        assert semantic_digest(restarted.workspace("chem")) == chem_ref
        assert semantic_digest(restarted.workspace("downstream")) == down_ref
        assert restarted.status("downstream") == "NEEDS_RECHECK"
        kinds = [r["kind"] for r in restarted.wal.read_valid_prefix().records]
        assert kinds == ["PREPARE", "COMMIT", "ACK"]

    # PREPARE without COMMIT is not authoritative after recovery.
    with TemporaryDirectory() as td:
        wal = Path(td) / "prepare.wal"
        live = make_runtime(wal)
        proof_before = semantic_digest(live.workspace("proof"))
        try:
            live.commit("TX-PREPARE", (p1,), crash_at="AFTER_PREPARE")
            raise AssertionError("crash injection did not fire")
        except SimulatedCrash:
            pass
        recovered = make_runtime(wal)
        assert recovered.revision == 0
        assert semantic_digest(recovered.workspace("proof")) == proof_before
        assert ("A", "SUPPORTS", "P") not in recovered.workspace("proof").edges
        assert [r["kind"] for r in recovered.wal.read_valid_prefix().records] == ["PREPARE"]

    # COMMIT is authoritative even when propagation never started; recovery
    # replays it into local views and appends a recovered ACK.
    with TemporaryDirectory() as td:
        wal = Path(td) / "commit.wal"
        live = make_runtime(wal)
        proof_before = semantic_digest(live.workspace("proof"))
        try:
            live.commit("TX-COMMIT", (p1,), crash_at="AFTER_COMMIT")
            raise AssertionError("crash injection did not fire")
        except SimulatedCrash:
            pass
        assert live.revision == 1
        assert semantic_digest(live.workspace("proof")) == proof_before
        recovered = make_runtime(wal)
        assert recovered.revision == 1
        assert ("A", "SUPPORTS", "P") in recovered.workspace("proof").edges
        assert recovered.status("downstream") == "NEEDS_RECHECK"
        records = recovered.wal.read_valid_prefix().records
        assert [r["kind"] for r in records] == ["PREPARE", "COMMIT", "ACK"]
        assert records[-1]["payload"].get("recovered") is True

    # Real partial propagation: proof receives P1, chem does not receive P2 and
    # downstream invalidation has not run. Restart must converge to clean state.
    with TemporaryDirectory() as td:
        wal = Path(td) / "mid.wal"
        live = make_runtime(wal)
        chem_before = semantic_digest(live.workspace("chem"))
        try:
            live.commit("TX-MID", (p1, p2), crash_at="MID_PROPAGATE")
            raise AssertionError("crash injection did not fire")
        except SimulatedCrash:
            pass
        assert ("A", "SUPPORTS", "P") in live.workspace("proof").edges
        assert semantic_digest(live.workspace("chem")) == chem_before
        assert live.status("downstream") == "VALID"

        recovered = make_runtime(wal)
        assert recovered.revision == 1
        assert ("A", "SUPPORTS", "P") in recovered.workspace("proof").edges
        assert ("C", "TRANSFORMS", "Q") in recovered.workspace("chem").edges
        assert recovered.status("downstream") == "NEEDS_RECHECK"
        assert [r["kind"] for r in recovered.wal.read_valid_prefix().records] == ["PREPARE", "COMMIT", "ACK"]

    # A torn final record is treated as crash tail, removed, and the valid
    # committed prefix is replayed. Internal corruption fails closed.
    with TemporaryDirectory() as td:
        wal = Path(td) / "tail.wal"
        live = make_runtime(wal)
        try:
            live.commit("TX-TAIL", (p1,), crash_at="AFTER_COMMIT")
        except SimulatedCrash:
            pass
        with wal.open("ab") as fh:
            fh.write(b'{"seq":2,"broken"')
        recovered = make_runtime(wal)
        assert recovered.revision == 1
        assert ("A", "SUPPORTS", "P") in recovered.workspace("proof").edges
        assert not recovered.wal.read_valid_prefix().tail_truncated

        lines = wal.read_text(encoding="utf-8").splitlines()
        first = json.loads(lines[0])
        first["payload"]["proposals"][0]["actor_id"] = "tampered"
        lines[0] = json.dumps(first, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        wal.write_text("\n".join(lines) + "\n", encoding="utf-8")
        try:
            make_runtime(wal)
            raise AssertionError("corruption was not detected")
        except WALCorruption:
            pass

    # Rejected FORUM observation is durable as REJECT but never becomes COMMIT
    # and therefore cannot reappear after recovery as knowledge.
    with TemporaryDirectory() as td:
        wal = Path(td) / "forum.wal"
        live = make_runtime(wal)
        forum_seen = MVCCProposal(
            proposal_id="F1",
            actor_id="agent:observer",
            base_revision=0,
            event=MemoryEvent(
                event_id="event:F1",
                kind="FORUM_OBJECT_SEEN",
                event_time="2026-09-30T12:00:01Z",
                ingest_time="2026-09-30T12:00:01.001000Z",
                payload={"oid": "OID-UNADMITTED", "kind": "RELATION"},
            ),
        )
        rejected = live.commit("TX-FORUM", (forum_seen,))
        assert rejected.result.status == "INVALID_BATCH"
        assert rejected.wal_state == "REJECT"
        recovered = make_runtime(wal)
        assert recovered.revision == 0
        assert [r["kind"] for r in recovered.wal.read_valid_prefix().records] == ["PREPARE", "REJECT"]

    print("PSI-ACTIVE-MEMORY-WAL-01 PASS_WITH_BOUNDARY")
    print("clean_restart_equivalence=PASS")
    print("prepare_without_commit_aborts_on_recovery=PASS")
    print("commit_before_propagation_recovers=PASS")
    print("partial_propagation_recovers=PASS")
    print("torn_tail_repaired=PASS")
    print("internal_corruption_fail_closed=PASS")
    print("forum_reject_not_replayed=PASS")
    print("txid_hot_path_index=O1_membership")
    print("BOUNDARY: fsync-backed single-process JSONL WAL with deterministic baseline replay; no durable checkpoint store, OS/power-loss hardware guarantee, concurrent processes, distributed consensus, live FORUM writes, or GPU execution")


if __name__ == "__main__":
    main()
