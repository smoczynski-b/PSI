#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import json

from active_memory import MemoryEvent, compile_workspace
from durable_shared_memory import DurableSharedMemoryRuntime, SimulatedCrash, WALCorruption
from mvcc_workspace import MVCCProposal
from servant_runtime import ServantCommand, ServantRuntime

CONTRACT = {
    "status": "COMPILED",
    "contract_id": "PSI-MEMORY-SERVANT-01",
    "anchor": "ROOT",
    "task": "test deterministic procedural servant",
}

RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "ROOT",
    "edges": [
        {"from": "ROOT", "relation": "BASE", "to": "A", "source": "seed:A", "status": "ADMITTED"},
    ],
}


def seed():
    return compile_workspace(CONTRACT, RETRIEVAL)


def view(anchor: str, node: str):
    contract = dict(CONTRACT)
    contract["contract_id"] = f"VIEW-{anchor}-{node}"
    contract["anchor"] = anchor
    retrieval = {
        "status": "RETRIEVED",
        "anchor": anchor,
        "edges": [
            {"from": anchor, "relation": "BASE", "to": node, "source": f"seed:{node}", "status": "ADMITTED"},
        ],
    }
    return compile_workspace(contract, retrieval)


def register_views(shared):
    shared.register("proof", view("ROOT", "A"))
    shared.register("downstream", view("DROOT", "D"), extra_dependencies=("workspace:proof",))


def make_durable(path: Path, *, recover: bool = True):
    return DurableSharedMemoryRuntime(seed(), path, register_views, recover=recover)


def upsert(pid: str, base: int = 0):
    return MVCCProposal(
        proposal_id=pid,
        actor_id="agent:proof",
        base_revision=base,
        event=MemoryEvent(
            event_id=f"event:{pid}",
            kind="EDGE_UPSERT",
            event_time="2026-09-30T13:00:00Z",
            ingest_time="2026-09-30T13:00:00.001000Z",
            payload={
                "from": "A",
                "relation": "SUPPORTS",
                "to": "P",
                "source": "forum:OID-P",
                "status": "ADMITTED",
            },
        ),
    )


def remove(pid: str, base: int):
    return MVCCProposal(
        proposal_id=pid,
        actor_id="servant:runbook",
        base_revision=base,
        event=MemoryEvent(
            event_id=f"event:{pid}",
            kind="EDGE_REMOVE",
            event_time="2026-09-30T13:00:01Z",
            ingest_time="2026-09-30T13:00:01.001000Z",
            payload={"from": "A", "relation": "SUPPORTS", "to": "P"},
        ),
    )


def chronicle_kinds(servant: ServantRuntime):
    return [r["kind"] for r in servant.chronicle.records()]


def main():
    # Typed legal transition goes through durable MVCC/WAL and is ACKed.
    with TemporaryDirectory() as td:
        root = Path(td)
        durable = make_durable(root / "memory.wal")
        servant = ServantRuntime(
            durable,
            root / "servant.wal",
            authorized_runbooks=("COMPENSATE_COMMITTED_TX",),
        )
        cmd = ServantCommand("CMD-1", "TRANSACT", txid="TX-1", proposals=(upsert("P1"),))
        out = servant.handle(cmd)
        assert out.disposition == "ACK_TRANSITION"
        assert out.reason_code == "COMMIT_ACCEPTED"
        assert durable.revision == 1
        assert ("A", "SUPPORTS", "P") in durable.workspace("proof").edges
        assert durable.status("downstream") == "NEEDS_RECHECK"
        assert [r["kind"] for r in durable.wal.read_valid_prefix().records] == ["PREPARE", "COMMIT", "ACK"]
        assert chronicle_kinds(servant) == ["SERVANT_OBSERVED", "SERVANT_RESULT"]

        # Exact command replay is procedural idempotence: no second memory commit.
        memory_count = len(durable.wal.read_valid_prefix().records)
        replay = servant.handle(cmd)
        assert replay.disposition == "ACK_TRANSITION"
        assert replay.reason_code == "IDEMPOTENT_REPLAY:COMMIT_ACCEPTED"
        assert durable.revision == 1
        assert len(durable.wal.read_valid_prefix().records) == memory_count

        # Correction after durable commit is a new compensating transaction.
        comp = ServantCommand(
            "CMD-2",
            "COMPENSATE",
            txid="TX-2",
            proposals=(remove("P2", base=1),),
            runbook_id="COMPENSATE_COMMITTED_TX",
            compensates_txid="TX-1",
        )
        comp_out = servant.handle(comp)
        assert comp_out.disposition == "ACK_TRANSITION"
        assert comp_out.reason_code == "COMPENSATING_COMMIT_ACCEPTED"
        assert durable.revision == 2
        assert ("A", "SUPPORTS", "P") not in durable.workspace("proof").edges
        records = durable.wal.read_valid_prefix().records
        assert [r["kind"] for r in records] == ["PREPARE", "COMMIT", "ACK", "PREPARE", "COMMIT", "ACK"]
        assert {r["txid"] for r in records if r["kind"] == "COMMIT"} == {"TX-1", "TX-2"}

    # Known illegal transitions are blocked before authoritative WAL mutation.
    with TemporaryDirectory() as td:
        root = Path(td)
        durable = make_durable(root / "memory.wal")
        servant = ServantRuntime(durable, root / "servant.wal")
        for i, kind in enumerate((
            "REWRITE_DURABLE_HISTORY",
            "DELETE_COMMITTED_HISTORY",
            "DIRECT_WORKSPACE_MUTATION",
            "SEMANTIC_VERDICT",
        )):
            out = servant.handle(ServantCommand(f"BLOCK-{i}", kind))
            assert out.disposition == "BLOCK_ILLEGAL_TRANSITION"
            assert out.reason_code == kind
        assert durable.revision == 0
        assert durable.wal.read_valid_prefix().records == ()

        # Replaying a blocked command preserves BLOCK, never becomes ACK.
        blocked = ServantCommand("BLOCK-R", "SEMANTIC_VERDICT")
        first = servant.handle(blocked)
        second = servant.handle(blocked)
        assert first.disposition == second.disposition == "BLOCK_ILLEGAL_TRANSITION"
        assert second.reason_code == "IDEMPOTENT_REPLAY:SEMANTIC_VERDICT"

    # Constitution problems and unknown typed transitions STOP + ESCALATE.
    with TemporaryDirectory() as td:
        root = Path(td)
        durable = make_durable(root / "memory.wal")
        servant = ServantRuntime(durable, root / "servant.wal")
        constitutional = servant.handle(ServantCommand("STOP-1", "CHANGE_CONSTITUTION"))
        unknown = servant.handle(ServantCommand("STOP-2", "UNDECLARED_OPERATION"))
        assert constitutional.disposition == "STOP_ESCALATE_CHRONICLE"
        assert constitutional.reason_code == "CHANGE_CONSTITUTION"
        assert unknown.disposition == "STOP_ESCALATE_CHRONICLE"
        assert unknown.reason_code == "UNKNOWN_TRANSITION_KIND"
        assert durable.wal.read_valid_prefix().records == ()
        assert chronicle_kinds(servant).count("SERVANT_ESCALATE") == 2

        # Same command id with different intent is itself a conflict and cannot
        # overwrite the original remembered verdict.
        collision = servant.handle(ServantCommand("STOP-1", "RECOVER"))
        assert collision.disposition == "STOP_ESCALATE_CHRONICLE"
        assert collision.reason_code == "COMMAND_ID_COLLISION"
        replay_original = servant.handle(ServantCommand("STOP-1", "CHANGE_CONSTITUTION"))
        assert replay_original.disposition == "STOP_ESCALATE_CHRONICLE"
        assert replay_original.reason_code == "IDEMPOTENT_REPLAY:CHANGE_CONSTITUTION"

    # The machine surface is typed: free prose is not parsed or interpreted.
    with TemporaryDirectory() as td:
        root = Path(td)
        servant = ServantRuntime(make_durable(root / "memory.wal"), root / "servant.wal")
        before = len(servant.chronicle.records())
        try:
            servant.handle("please decide whether this theorem is true")  # type: ignore[arg-type]
            raise AssertionError("free-text command was accepted")
        except TypeError:
            pass
        assert len(servant.chronicle.records()) == before

    # A transaction-shaped request can still fail at MVCC; SERVANT records the
    # protocol result and does not reinterpret it as a truth verdict.
    with TemporaryDirectory() as td:
        root = Path(td)
        durable = make_durable(root / "memory.wal")
        servant = ServantRuntime(durable, root / "servant.wal")
        forum_seen = MVCCProposal(
            proposal_id="F1",
            actor_id="agent:observer",
            base_revision=0,
            event=MemoryEvent(
                event_id="event:F1",
                kind="FORUM_OBJECT_SEEN",
                event_time="2026-09-30T13:00:02Z",
                ingest_time="2026-09-30T13:00:02.001000Z",
                payload={"oid": "OID-UNADMITTED", "kind": "RELATION"},
            ),
        )
        out = servant.handle(ServantCommand("CMD-F", "TRANSACT", txid="TX-F", proposals=(forum_seen,)))
        assert out.disposition == "BLOCK_ILLEGAL_TRANSITION"
        assert out.reason_code == "MVCC:INVALID_BATCH"
        assert durable.revision == 0
        assert [r["kind"] for r in durable.wal.read_valid_prefix().records] == ["PREPARE", "REJECT"]

    # Compensation requires an explicitly authorized runbook and a committed target.
    with TemporaryDirectory() as td:
        root = Path(td)
        durable = make_durable(root / "memory.wal")
        servant = ServantRuntime(durable, root / "servant.wal")
        out = servant.handle(ServantCommand(
            "CMD-C0",
            "COMPENSATE",
            txid="TX-C0",
            proposals=(remove("PC0", base=0),),
            runbook_id="COMPENSATE_COMMITTED_TX",
            compensates_txid="TX-NOT-THERE",
        ))
        assert out.disposition == "BLOCK_ILLEGAL_TRANSITION"
        assert out.reason_code == "RUNBOOK_NOT_AUTHORIZED"
        assert durable.wal.read_valid_prefix().records == ()

    # RECOVER is a legal typed transition. A durable COMMIT without propagation
    # is completed by the existing WAL replay machinery, not by ad hoc repair.
    with TemporaryDirectory() as td:
        root = Path(td)
        wal = root / "memory.wal"
        live = make_durable(wal)
        try:
            live.commit("TX-CRASH", (upsert("PX"),), crash_at="AFTER_COMMIT")
            raise AssertionError("crash injection did not fire")
        except SimulatedCrash:
            pass
        cold = make_durable(wal, recover=False)
        assert cold.revision == 0
        servant = ServantRuntime(cold, root / "servant.wal")
        recovered = servant.handle(ServantCommand("CMD-R", "RECOVER"))
        assert recovered.disposition == "ACK_TRANSITION"
        assert recovered.reason_code == "RECOVERY_COMPLETED"
        assert cold.revision == 1
        assert ("A", "SUPPORTS", "P") in cold.workspace("proof").edges
        assert [r["kind"] for r in cold.wal.read_valid_prefix().records] == ["PREPARE", "COMMIT", "ACK"]

    # The servant chronicle itself is hash-chained and fails closed on tampering.
    with TemporaryDirectory() as td:
        root = Path(td)
        memory = root / "memory.wal"
        chronicle = root / "servant.wal"
        servant = ServantRuntime(make_durable(memory), chronicle)
        servant.handle(ServantCommand("STOP-T", "CHANGE_CONSTITUTION"))
        lines = chronicle.read_text(encoding="utf-8").splitlines()
        first = json.loads(lines[0])
        first["payload"]["revision"] = 999
        lines[0] = json.dumps(first, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        chronicle.write_text("\n".join(lines) + "\n", encoding="utf-8")
        try:
            ServantRuntime(make_durable(memory), chronicle)
            raise AssertionError("servant chronicle corruption was not detected")
        except WALCorruption:
            pass

    print("PSI-MEMORY-SERVANT-01 PASS_WITH_BOUNDARY")
    print("typed_machine_surface_only=PASS")
    print("legal_transition_ack=PASS")
    print("known_illegal_transition_block=PASS")
    print("unknown_or_constitution_conflict_stop_escalate=PASS")
    print("verdict_replay_preserves_original_disposition=PASS")
    print("durable_history_rewrite=BLOCKED")
    print("compensation_is_new_auditable_transaction=PASS")
    print("authorized_runbook_gate=PASS")
    print("wal_recovery_delegation=PASS")
    print("servant_chronicle_integrity=PASS")
    print("semantic_truth_authority=ABSENT")
    print("BOUNDARY: deterministic single-process procedural automaton; no anomaly detection, no natural-language deliberation, no constitution mutation, no domain truth adjudication, no distributed coordination")


if __name__ == "__main__":
    main()
