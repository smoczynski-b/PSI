#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
import copy
import hashlib
import json

from active_memory import MemoryEvent, compile_workspace
from active_memory_runtime import semantic_digest
from durable_shared_memory import DurableSharedMemoryRuntime
from mvcc_workspace import MVCCProposal, MVCCWorkspace
from servant_runtime import ServantCommand, ServantRuntime


SOURCE_CONTRACT = {
    "status": "COMPILED",
    "contract_id": "F1-SOURCE-A-01",
    "anchor": "SOURCE:A",
    "task": "bounded source view for Agent A",
}
RESULT_CONTRACT = {
    "status": "COMPILED",
    "contract_id": "F1-RESULT-A-01",
    "anchor": "RESULT:A",
    "task": "reuse Agent A result only while declared source dependency remains valid",
}
AUTHORITATIVE_CONTRACT = {
    "status": "COMPILED",
    "contract_id": "F1-AUTHORITATIVE-01",
    "anchor": "MEMORY",
    "task": "durable source-bound result reuse",
}


class SourceOracle:
    """One-shot source reader used only to construct the initial bounded view."""

    def __init__(self):
        self.reads = 0
        self.locked = False

    def read(self):
        if self.locked:
            raise AssertionError("Agent B attempted to reconstruct/read source A")
        self.reads += 1
        return {
            "status": "RETRIEVED",
            "anchor": "SOURCE:A",
            "edges": [
                {
                    "from": "SOURCE:A",
                    "relation": "STATE",
                    "to": "VALUE:V1",
                    "source": "artifact:A:v1",
                    "status": "ADMITTED",
                }
            ],
        }

    def lock(self):
        self.locked = True


@dataclass(frozen=True)
class ReuseDecision:
    disposition: str
    reason: str
    answer: str = ""
    provenance: str = ""
    workspace_revision: int = 0


def _hash(value) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def make_seeds(oracle: SourceOracle):
    source_retrieval = oracle.read()
    source_view = compile_workspace(SOURCE_CONTRACT, source_retrieval)
    result_view = compile_workspace(
        RESULT_CONTRACT,
        {
            "status": "RETRIEVED",
            "anchor": "RESULT:A",
            "edges": [
                {
                    "from": "RESULT:A",
                    "relation": "KIND",
                    "to": "DERIVED_RESULT",
                    "source": "contract:F1-RESULT-A-01",
                    "status": "ADMITTED",
                }
            ],
        },
    )
    source_edge = next(iter(source_view.edges.values())).as_dict()
    authoritative = compile_workspace(
        AUTHORITATIVE_CONTRACT,
        {
            "status": "RETRIEVED",
            "anchor": "MEMORY",
            "edges": [
                {
                    "from": "MEMORY",
                    "relation": "CONTAINS",
                    "to": "SOURCE:A",
                    "source": "seed:catalog",
                    "status": "ADMITTED",
                },
                {
                    "from": "MEMORY",
                    "relation": "CONTAINS",
                    "to": "RESULT:A",
                    "source": "seed:catalog",
                    "status": "ADMITTED",
                },
                source_edge,
            ],
        },
    )
    return authoritative, source_view, result_view


def register_factory(source_view, result_view):
    def register(shared):
        shared.register("sourceA", copy.deepcopy(source_view))
        shared.register(
            "resultA",
            copy.deepcopy(result_view),
            extra_dependencies=("workspace:sourceA",),
        )
    return register


def result_proposal(base_revision: int) -> MVCCProposal:
    return MVCCProposal(
        proposal_id="F1-P-A-RESULT",
        actor_id="agent:A",
        base_revision=base_revision,
        read_set=(MVCCWorkspace.edge_token("SOURCE:A", "STATE", "VALUE:V1"),),
        event=MemoryEvent(
            event_id="F1-E-A-RESULT",
            kind="EDGE_UPSERT",
            event_time="2026-09-30T16:10:00Z",
            ingest_time="2026-09-30T16:10:00.001000Z",
            payload={
                "from": "RESULT:A",
                "relation": "ANSWER",
                "to": "VALUE:ALPHA",
                "source": "agent:A|source=artifact:A:v1|contract=F1-RESULT-A-01",
                "status": "ADMITTED",
            },
        ),
    )


def source_change_proposals(base_revision: int) -> tuple[MVCCProposal, MVCCProposal]:
    remove_old = MVCCProposal(
        proposal_id="F1-P-SOURCE-REMOVE-V1",
        actor_id="source:update",
        base_revision=base_revision,
        event=MemoryEvent(
            event_id="F1-E-SOURCE-REMOVE-V1",
            kind="EDGE_REMOVE",
            event_time="2026-09-30T16:20:00Z",
            ingest_time="2026-09-30T16:20:00.001000Z",
            payload={
                "from": "SOURCE:A",
                "relation": "STATE",
                "to": "VALUE:V1",
            },
        ),
    )
    add_new = MVCCProposal(
        proposal_id="F1-P-SOURCE-ADD-V2",
        actor_id="source:update",
        base_revision=base_revision,
        event=MemoryEvent(
            event_id="F1-E-SOURCE-ADD-V2",
            kind="EDGE_UPSERT",
            event_time="2026-09-30T16:20:00Z",
            ingest_time="2026-09-30T16:20:00.001000Z",
            payload={
                "from": "SOURCE:A",
                "relation": "STATE",
                "to": "VALUE:V2",
                "source": "artifact:A:v2",
                "status": "ADMITTED",
            },
        ),
    )
    return remove_old, add_new


def agent_b_reuse(durable: DurableSharedMemoryRuntime) -> ReuseDecision:
    """Reuse only durable memory metadata and the result workspace; never source A."""
    if durable.status("resultA") != "VALID":
        return ReuseDecision(
            "NEEDS_RECHECK",
            f"resultA status={durable.status('resultA')}",
            workspace_revision=durable.workspace("resultA").revision,
        )
    ws = durable.workspace("resultA")
    if ws.contract_id != RESULT_CONTRACT["contract_id"]:
        return ReuseDecision("BLOCK", "contract mismatch", workspace_revision=ws.revision)
    deps = durable.shared.views.dependency_tokens("resultA")
    if "workspace:sourceA" not in deps:
        return ReuseDecision("BLOCK", "missing declared source workspace dependency", workspace_revision=ws.revision)
    answers = [
        edge for edge in ws.edges.values()
        if edge.source == "RESULT:A" and edge.relation == "ANSWER"
    ]
    if len(answers) != 1:
        return ReuseDecision("BLOCK", "result fibre is not singleton", workspace_revision=ws.revision)
    edge = answers[0]
    return ReuseDecision(
        "REUSE_ALLOWED",
        "result is durable, contract-matched and dependency status is VALID",
        answer=edge.target,
        provenance=edge.provenance,
        workspace_revision=ws.revision,
    )


def state_digest(durable: DurableSharedMemoryRuntime) -> str:
    payload = {
        "revision": durable.revision,
        "authoritative": durable.shared.memory.semantic_digest,
        "commit_chain": durable.shared.memory.commit_chain_digest,
        "sourceA": semantic_digest(durable.workspace("sourceA")),
        "resultA": semantic_digest(durable.workspace("resultA")),
        "sourceA_status": durable.status("sourceA"),
        "resultA_status": durable.status("resultA"),
        "resultA_dependencies": sorted(durable.shared.views.dependency_tokens("resultA")),
    }
    return _hash(payload)


def new_runtime(authoritative, wal: Path, register):
    return DurableSharedMemoryRuntime(
        copy.deepcopy(authoritative),
        wal,
        register,
        recover=True,
    )


def main():
    oracle = SourceOracle()
    authoritative, source_view, result_view = make_seeds(oracle)
    assert oracle.reads == 1
    oracle.lock()
    register = register_factory(source_view, result_view)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        wal = root / "memory.jsonl"
        chronicle = root / "servant.jsonl"

        # A. Agent A reads the bounded source once (already frozen above), then
        # commits a result through SERVANT -> MVCC -> WAL -> local result map.
        durable_a = new_runtime(authoritative, wal, register)
        servant_a = ServantRuntime(durable_a, chronicle)
        cmd_a = ServantCommand(
            command_id="F1-CMD-A-RESULT",
            kind="TRANSACT",
            txid="F1-TX-A-RESULT",
            proposals=(result_proposal(durable_a.revision),),
        )
        a = servant_a.handle(cmd_a)
        assert a.disposition == "ACK_TRANSITION"
        assert a.reason_code == "COMMIT_ACCEPTED"
        assert a.durable_state == "ACK"
        assert durable_a.status("resultA") == "VALID"
        assert "workspace:sourceA" in durable_a.shared.views.dependency_tokens("resultA")
        first = agent_b_reuse(durable_a)
        assert first.disposition == "REUSE_ALLOWED"
        assert first.answer == "VALUE:ALPHA"
        assert "artifact:A:v1" in first.provenance
        assert oracle.reads == 1
        assert a.examined_versions >= 2
        assert a.examined_workspaces == 1
        assert a.examined_events == 1
        assert a.index_refresh_edge_visits > 0

        before_clean_restart = state_digest(durable_a)
        revision_after_a = durable_a.revision

        # B. Genuine process-style restart: construct fresh durable and servant
        # instances from the same frozen seed + WAL/chronicle. No source oracle is
        # available or called. Agent B reuses the result only from recovered memory.
        del servant_a, durable_a
        durable_b = new_runtime(authoritative, wal, register)
        servant_b = ServantRuntime(durable_b, chronicle)
        assert state_digest(durable_b) == before_clean_restart
        assert durable_b.revision == revision_after_a
        after_restart = agent_b_reuse(durable_b)
        assert after_restart == first
        assert oracle.reads == 1

        # Replaying Agent A's command after restart is chronicle-idempotent and
        # cannot create a second durable transaction.
        replay = servant_b.handle(cmd_a)
        assert replay.disposition == "ACK_TRANSITION"
        assert replay.reason_code == "IDEMPOTENT_REPLAY:COMMIT_ACCEPTED"
        assert durable_b.revision == revision_after_a
        assert replay.examined_events == 0

        # C. The source premise changes through the same procedural path. The
        # source view updates, while the derived result remains stored but becomes
        # NEEDS_RECHECK through the declared workspace dependency.
        source_cmd = ServantCommand(
            command_id="F1-CMD-SOURCE-V2",
            kind="TRANSACT",
            txid="F1-TX-SOURCE-V2",
            proposals=source_change_proposals(durable_b.revision),
        )
        changed = servant_b.handle(source_cmd)
        assert changed.disposition == "ACK_TRANSITION"
        assert changed.reason_code == "COMMIT_ACCEPTED"
        assert changed.examined_versions >= 2
        assert changed.examined_workspaces == 2  # two source events, one candidate each
        assert changed.examined_events == 2
        assert changed.examined_dependency_links == 1
        assert changed.index_refresh_edge_visits >= 2
        assert durable_b.status("sourceA") == "VALID"
        assert durable_b.status("resultA") == "NEEDS_RECHECK"
        assert ("SOURCE:A", "STATE", "VALUE:V1") not in durable_b.workspace("sourceA").edges
        assert ("SOURCE:A", "STATE", "VALUE:V2") in durable_b.workspace("sourceA").edges
        assert ("RESULT:A", "ANSWER", "VALUE:ALPHA") in durable_b.workspace("resultA").edges
        blocked = agent_b_reuse(durable_b)
        assert blocked.disposition == "NEEDS_RECHECK"
        assert oracle.reads == 1

        before_changed_restart = state_digest(durable_b)
        revision_after_change = durable_b.revision

        # D. Second restart preserves both the result and its invalidated status.
        # Presence of the old answer is not permission to reuse it.
        del servant_b, durable_b
        durable_c = new_runtime(authoritative, wal, register)
        servant_c = ServantRuntime(durable_c, chronicle)
        assert state_digest(durable_c) == before_changed_restart
        assert durable_c.revision == revision_after_change
        assert durable_c.status("resultA") == "NEEDS_RECHECK"
        assert ("RESULT:A", "ANSWER", "VALUE:ALPHA") in durable_c.workspace("resultA").edges
        after_changed_restart = agent_b_reuse(durable_c)
        assert after_changed_restart.disposition == "NEEDS_RECHECK"
        assert oracle.reads == 1

        wal_records = durable_c.wal.read_valid_prefix().records
        assert sum(1 for r in wal_records if r["kind"] == "COMMIT") == 2
        servant_results = [r for r in servant_c.chronicle.records() if r["kind"] == "SERVANT_RESULT"]
        assert any(r["payload"].get("command_id") == "F1-CMD-A-RESULT" for r in servant_results)
        assert any(r["payload"].get("command_id") == "F1-CMD-SOURCE-V2" for r in servant_results)

        print("PSI-MEMORY-F1-END-TO-END-01 PASS_WITH_BOUNDARY")
        print("source_reads_total=1")
        print("agent_b_source_reconstruction=0")
        print("clean_restart_semantic_equivalence=PASS")
        print("clean_restart_reuse=REUSE_ALLOWED")
        print("source_change_invalidates_result=PASS")
        print("changed_restart_preserves_NEEDS_RECHECK=PASS")
        print("stored_answer_does_not_override_status=PASS")
        print(f"result_commit_examined_versions={a.examined_versions}")
        print(f"result_commit_examined_workspaces={a.examined_workspaces}")
        print(f"result_commit_index_refresh_edge_visits={a.index_refresh_edge_visits}")
        print(f"source_change_examined_versions={changed.examined_versions}")
        print(f"source_change_examined_workspaces={changed.examined_workspaces}")
        print(f"source_change_examined_dependency_links={changed.examined_dependency_links}")
        print(f"source_change_index_refresh_edge_visits={changed.index_refresh_edge_visits}")
        print("BOUNDARY: deterministic source-bound reuse witness; no live LLM execution, Guardian admission, Access Steward, Curator archive, network transport, or learned retrieval")


if __name__ == "__main__":
    main()
