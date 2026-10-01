#!/usr/bin/env python3
from __future__ import annotations

import copy
import csv
from pathlib import Path
from tempfile import TemporaryDirectory

from active_memory import Edge, MemoryEvent, Workspace
from access_steward_runtime import (
    AccessStewardRuntime,
    CAP_ENTER,
    CAP_TELEMETRY,
    COST_EVIDENCE_PREEXECUTION_QUOTE,
    CostVector,
    GuardianAccessPolicy,
    MapState,
    MovementRequest,
    OUTSIDE,
    PolicyRule,
    TelemetryQuery,
)
from curator_planner_runtime import (
    CuratorPlanningError,
    CuratorPlanningPolicy,
    CuratorPlannerRuntime,
    DistrictObservation,
    PlanningRule,
)
from durable_shared_memory import DurableSharedMemoryRuntime
from memory_archive_runtime import ArchiveManifest, MemoryArchiveRuntime
from memory_archive_usage_runtime import (
    EVIDENCE_MAP_ASSOCIATION,
    EVIDENCE_VERIFIED_CONSUMPTION,
    MemoryArchiveUsageRuntime,
)
from mvcc_workspace import MVCCProposal, MVCCWorkspace
from servant_runtime import ServantCommand, ServantRuntime

ROOT = "ACCESS_PRESENCE_ROOT"
MAP_ID = "PSI:P9-I-GATE"
SOURCE_VIEW = "source:P9-I"
RESULT_VIEW = "result:P9-I-gate"
RESULT_ANCHOR = "RESULT:P9-I-GATE"
SESSION = "session-full-psi"
ACTOR = "agent-full-psi"
ACCESS_POLICY = "G-FULL-PSI-01"
PLANNER_POLICY = "PLAN-FULL-PSI-01"
REAL_NODES = Path("docs/memory/psi-memory-nodes-01.tsv")
REAL_EDGES = Path("docs/memory/psi-memory-edges-01.tsv")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def real_slice() -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    nodes = {row["id"]: row for row in read_tsv(REAL_NODES)}
    edges = read_tsv(REAL_EDGES)
    assert "P9-I" in nodes, "real PSI memory map lacks P9-I"
    assert "III.13" in nodes, "real PSI memory map lacks III.13"
    p9 = nodes["P9-I"]
    iii13 = nodes["III.13"]
    gate = next(
        row for row in edges
        if row["from"] == "P9-I"
        and row["relation"] == "GATE_FOR"
        and row["to"] == "III.13"
    )
    # This bounded run is intentionally pinned to the actual state reviewed on
    # 2026-09-30. A future legitimate canon/control change must force review of
    # the fixture rather than silently changing the premise under the test.
    assert p9["status"] == "OPEN"
    assert p9["source"] == "docs/control-state.json"
    assert iii13["status"] == "UNAUTHORIZED"
    assert iii13["source"] == "docs/control-state.json"
    assert gate["source"] == "docs/control-state.json"
    return p9, iii13, gate


def build_seeds():
    p9, iii13, gate = real_slice()
    real_edge = Edge(
        gate["from"], gate["relation"], gate["to"], gate["source"], "ADMITTED_REAL_RECORD",
    )
    source = Workspace(
        contract_id="PSI-REAL-P9-I-SLICE-01",
        contract_digest="psi-real-p9-i-slice-2026-09-30",
        anchor="P9-I",
        edges={real_edge.triple: real_edge},
        node_status={"P9-I": p9["status"], "III.13": iii13["status"]},
    )
    result = Workspace(
        contract_id="PSI-P9-I-DERIVED-RESULT-01",
        contract_digest="psi-p9-i-derived-result-v1",
        anchor=RESULT_ANCHOR,
    )
    authoritative = Workspace(
        contract_id="PSI-FULL-MEMORY-RUN-01",
        contract_digest="psi-full-memory-run-v1",
        anchor=ROOT,
        edges={
            real_edge.triple: real_edge,
            (ROOT, "CONTAINS", "P9-I"): Edge(ROOT, "CONTAINS", "P9-I", "integration:harness"),
            (ROOT, "CONTAINS", RESULT_ANCHOR): Edge(ROOT, "CONTAINS", RESULT_ANCHOR, "integration:harness"),
        },
        node_status={"P9-I": p9["status"], "III.13": iii13["status"]},
    )
    return authoritative, source, result, gate


def register_factory(source: Workspace, result: Workspace):
    def register(shared):
        shared.register(SOURCE_VIEW, copy.deepcopy(source))
        shared.register(RESULT_VIEW, copy.deepcopy(result), extra_dependencies=(f"workspace:{SOURCE_VIEW}",))
    return register


def cv(value: float) -> CostVector:
    return CostVector(compute=value)


def access_policy() -> GuardianAccessPolicy:
    return GuardianAccessPolicy(
        ACCESS_POLICY,
        (
            PolicyRule(ACTOR, SESSION, "ENTER", OUTSIDE, MAP_ID, "inspect-p9-gate", CAP_ENTER),
            PolicyRule(
                ACTOR, SESSION, "VIEW_TELEMETRY", MAP_ID, MAP_ID, "audit-full-run",
                CAP_TELEMETRY, ("T2_AUDIT_DURABLE",),
            ),
        ),
    )


def planner_policy() -> CuratorPlanningPolicy:
    return CuratorPlanningPolicy(
        version=PLANNER_POLICY,
        rules=(
            PlanningRule(
                rule_id="GATE-PRESSURE-HIGH",
                operation="REINDEX",
                metric="gate_pressure",
                comparator="GTE",
                threshold=2.0,
                expected_benefit="review bounded gate representation",
                estimated_cost=1.0,
                risk="bounded integration fixture only",
                information_loss_risk="none intended",
                required_dependencies=("source:docs/control-state.json",),
                rollback_requirement="discard integration fixture",
                required_test="full bounded PSI memory restart witness",
            ),
        ),
    )


def observation(value: float = 0.5) -> DistrictObservation:
    return DistrictObservation(
        observation_id="OBS:P9-I:FULL-RUN",
        district_id="district:P9-I",
        metrics={"gate_pressure": value},
        observed_at="2026-09-30T21:20:00Z",
        policy_version=PLANNER_POLICY,
    )


def archive_manifest(
    version_id: str,
    snapshot_id: str,
    ws: Workspace,
    gate_source: str,
    *,
    parents: tuple[str, ...] = (),
    epistemic_status_ref: str,
) -> ArchiveManifest:
    return ArchiveManifest(
        version_id=version_id,
        object_id=MAP_ID,
        parent_version_ids=parents,
        base_snapshot_id=snapshot_id,
        delta_ids=(),
        content_digest=ws.state_digest,
        contract_id=ws.contract_id,
        contract_digest=ws.contract_digest,
        provenance_refs=(
            f"source:{gate_source}",
            "source:docs/memory/psi-memory-nodes-01.tsv",
            "source:docs/memory/psi-memory-edges-01.tsv",
        ),
        epistemic_status_ref=epistemic_status_ref,
        access_policy_ref=f"policy:{ACCESS_POLICY}",
        lifecycle_state="ACTIVE",
        created_at="2026-09-30T21:20:00Z",
    )


def result_proposal(base_revision: int) -> MVCCProposal:
    return MVCCProposal(
        proposal_id="FULL-P-RESULT-V1",
        actor_id=ACTOR,
        base_revision=base_revision,
        read_set=(MVCCWorkspace.edge_token("P9-I", "GATE_FOR", "III.13"),),
        event=MemoryEvent(
            event_id="FULL-E-RESULT-V1",
            kind="EDGE_UPSERT",
            event_time="2026-09-30T21:20:10Z",
            ingest_time="2026-09-30T21:20:10.001000Z",
            payload={
                "from": RESULT_ANCHOR,
                "relation": "ANSWER",
                "to": "III.13:UNAUTHORIZED_WHILE_P9-I_OPEN",
                "source": "docs/control-state.json|P9-I:GATE_FOR:III.13",
                "status": "ADMITTED_DERIVED_RESULT",
            },
        ),
    )


def premise_change_proposal(base_revision: int) -> MVCCProposal:
    # This is an isolated hypothetical update derived from the real P9-I record.
    # It does not edit docs/control-state.json or claim that P9-I actually passed.
    return MVCCProposal(
        proposal_id="FULL-P-P9-I-HYPOTHETICAL-PASS",
        actor_id="integration:source-update",
        base_revision=base_revision,
        event=MemoryEvent(
            event_id="FULL-E-P9-I-HYPOTHETICAL-PASS",
            kind="NODE_STATUS_SET",
            event_time="2026-09-30T21:21:00Z",
            ingest_time="2026-09-30T21:21:00.001000Z",
            payload={"node": "P9-I", "status": "PASSED_INTEGRATION_TEST"},
        ),
    )


def reuse_decision(durable: DurableSharedMemoryRuntime) -> tuple[str, str]:
    ws = durable.workspace(RESULT_VIEW)
    answers = [
        edge for edge in ws.edges.values()
        if edge.source == RESULT_ANCHOR and edge.relation == "ANSWER"
    ]
    if durable.status(RESULT_VIEW) != "VALID":
        return "NEEDS_RECHECK", durable.status(RESULT_VIEW)
    if len(answers) != 1:
        return "BLOCK", "result fibre is not singleton"
    return "REUSE_ALLOWED", answers[0].target


def movement_count(steward: AccessStewardRuntime, request_id: str) -> int:
    return sum(
        1 for row in steward.chronicle.records()
        if row.get("kind") == "ACCESS_MOVEMENT"
        and str(row.get("payload", {}).get("request_id", "")) == request_id
    )


def curator_record_count(planner: CuratorPlannerRuntime) -> int:
    return planner.counts()["records"]


def main() -> None:
    authoritative, source_seed, result_seed, gate = build_seeds()
    access = access_policy()
    planning = planner_policy()

    with TemporaryDirectory() as td:
        root = Path(td)

        def register(shared):
            register_factory(source_seed, result_seed)(shared)

        def durable_runtime():
            return DurableSharedMemoryRuntime(
                authoritative, root / "memory.wal", register, recover=True,
            )

        def servant_runtime(durable):
            return ServantRuntime(
                durable,
                root / "servant.wal",
                authorized_runbooks=("CURATOR-ARCHIVE-01", "CURATOR-PLANNER-01"),
            )

        def steward_runtime(servant):
            return AccessStewardRuntime(
                servant,
                root / "access.wal",
                presence_anchor=ROOT,
                policy_lookup=lambda version: access if version == access.version else None,
                current_policy_version=lambda: access.version,
                map_state_lookup=lambda map_id: MapState(MAP_ID) if map_id == MAP_ID else None,
                cost_meter=lambda request: request.estimated_cost,
            )

        def curator_runtime(servant):
            return CuratorPlannerRuntime(
                servant,
                root / "curator.wal",
                policy_lookup=lambda version: planning if version == planning.version else None,
                current_policy_version=lambda: planning.version,
            )

        durable = durable_runtime()
        servant = servant_runtime(durable)
        steward = steward_runtime(servant)
        archive = MemoryArchiveRuntime(servant, root / "archive.wal")
        usage = MemoryArchiveUsageRuntime(archive, steward, root / "usage.wal")
        curator = curator_runtime(servant)

        # A. Freeze and publish a version built from actual PSI records.
        v1 = durable.workspace(SOURCE_VIEW)
        assert v1.node_status["P9-I"] == "OPEN"
        assert v1.node_status["III.13"] == "UNAUTHORIZED"
        assert ("P9-I", "GATE_FOR", "III.13") in v1.edges
        archive.store_snapshot("snapshot:PSI-P9-I:1", v1)
        archive.publish_version(archive_manifest(
            "version:PSI-P9-I:1", "snapshot:PSI-P9-I:1", v1, gate["source"],
            epistemic_status_ref="P9-I:OPEN",
        ))
        archive.publish_current(MAP_ID, "version:PSI-P9-I:1")

        move = MovementRequest(
            request_id="FULL-ENTER-P9-I",
            session_id=SESSION,
            actor_id=ACTOR,
            operation="ENTER",
            map_from=OUTSIDE,
            map_to=MAP_ID,
            declared_purpose="inspect-p9-gate",
            requested_capability=CAP_ENTER,
            policy_version=access.version,
            budget=cv(10),
            estimated_cost=cv(1),
            event_time="2026-09-30T21:20:01Z",
        )
        moved = steward.handle(move)
        assert moved.disposition == "ALLOW_MOVEMENT"
        assert moved.cost_evidence_kind == COST_EVIDENCE_PREEXECUTION_QUOTE
        assert moved.quoted_cost == cv(1)
        assert moved.incurred_cost is None
        assert steward.location(SESSION) == MAP_ID

        consumed = usage.consume_version(
            "receipt:PSI-P9-I:1",
            "version:PSI-P9-I:1",
            move.request_id,
            created_at="2026-09-30T21:20:02Z",
        )
        assert consumed.workspace.state_digest == v1.state_digest
        verified = usage.link_movement(
            "usage:PSI-P9-I:1",
            "version:PSI-P9-I:1",
            move.request_id,
            created_at="2026-09-30T21:20:03Z",
            consumption_receipt_id="receipt:PSI-P9-I:1",
        )
        assert verified.evidence_kind == EVIDENCE_VERIFIED_CONSUMPTION
        assert verified.content_digest == v1.state_digest
        association = usage.link_movement(
            "association:PSI-P9-I:1",
            "version:PSI-P9-I:1",
            move.request_id,
            created_at="2026-09-30T21:20:04Z",
        )
        assert association.evidence_kind == EVIDENCE_MAP_ASSOCIATION
        assert not association.consumption_receipt_id

        # A derived result is legal while the real P9-I premise remains OPEN.
        result_cmd = ServantCommand(
            command_id="FULL-CMD-RESULT-V1",
            kind="TRANSACT",
            txid="FULL-TX-RESULT-V1",
            proposals=(result_proposal(durable.revision),),
        )
        result_out = servant.handle(result_cmd)
        assert result_out.disposition == "ACK_TRANSITION"
        assert durable.status(RESULT_VIEW) == "VALID"
        assert reuse_decision(durable)[0] == "REUSE_ALLOWED"

        # Curator records a real-episode administrative observation with no
        # proposal; R8 identity must survive the later restart.
        obs = observation()
        assert curator.evaluate(obs) == ()
        assert curator.counts()["no_proposal_observations"] == 1
        curator_records_before = curator_record_count(curator)

        # B. A later isolated event changes the relevant premise. This is a test
        # delta, not a claim about current mathematics or an edit to the source TSV.
        change_cmd = ServantCommand(
            command_id="FULL-CMD-PREMISE-CHANGE",
            kind="TRANSACT",
            txid="FULL-TX-PREMISE-CHANGE",
            proposals=(premise_change_proposal(durable.revision),),
        )
        changed = servant.handle(change_cmd)
        assert changed.disposition == "ACK_TRANSITION"
        assert durable.workspace(SOURCE_VIEW).node_status["P9-I"] == "PASSED_INTEGRATION_TEST"
        assert durable.status(RESULT_VIEW) == "NEEDS_RECHECK"
        # The old answer stays stored as evidence, but presence is not permission.
        assert any(
            edge.source == RESULT_ANCHOR and edge.relation == "ANSWER"
            for edge in durable.workspace(RESULT_VIEW).edges.values()
        )
        assert reuse_decision(durable)[0] == "NEEDS_RECHECK"

        v2 = durable.workspace(SOURCE_VIEW)
        archive.store_snapshot("snapshot:PSI-P9-I:2", v2)
        archive.publish_version(archive_manifest(
            "version:PSI-P9-I:2", "snapshot:PSI-P9-I:2", v2, gate["source"],
            parents=("version:PSI-P9-I:1",),
            epistemic_status_ref="P9-I:PASSED_INTEGRATION_TEST",
        ))
        archive.publish_current(MAP_ID, "version:PSI-P9-I:2")
        assert archive.current(MAP_ID) == "version:PSI-P9-I:2"
        assert consumed.receipt.version_id != archive.current(MAP_ID)

        revision_before_restart = durable.revision
        movement_records_before = movement_count(steward, move.request_id)
        assert movement_records_before == 1
        memory_commits_before = sum(
            1 for row in durable.wal.read_valid_prefix().records if row.get("kind") == "COMMIT"
        )

        # C. Process-style interruption/restart across all composed journals.
        del curator, usage, archive, steward, servant, durable
        durable2 = durable_runtime()
        servant2 = servant_runtime(durable2)
        steward2 = steward_runtime(servant2)
        archive2 = MemoryArchiveRuntime(servant2, root / "archive.wal")
        usage2 = MemoryArchiveUsageRuntime(archive2, steward2, root / "usage.wal")
        curator2 = curator_runtime(servant2)

        assert durable2.revision == revision_before_restart
        assert steward2.location(SESSION) == MAP_ID
        assert archive2.current(MAP_ID) == "version:PSI-P9-I:2"
        receipt2 = usage2.consumption_receipt("receipt:PSI-P9-I:1")
        assert receipt2.version_id == "version:PSI-P9-I:1"
        assert receipt2.content_digest == consumed.receipt.content_digest
        usage_ref2 = usage2.usage("usage:PSI-P9-I:1")
        assert usage_ref2.evidence_kind == EVIDENCE_VERIFIED_CONSUMPTION
        assert usage_ref2.consumption_receipt_id == receipt2.receipt_id
        association2 = usage2.usage("association:PSI-P9-I:1")
        assert association2.evidence_kind == EVIDENCE_MAP_ASSOCIATION
        assert not association2.consumption_receipt_id

        # D. The old archive is explicitly historical, while the derived result
        # remains NEEDS_RECHECK. No old answer is silently upgraded to current.
        historical = archive2.reconstruct("version:PSI-P9-I:1")
        assert historical.workspace.node_status["P9-I"] == "OPEN"
        assert receipt2.version_id != archive2.current(MAP_ID)
        assert durable2.status(RESULT_VIEW) == "NEEDS_RECHECK"
        assert reuse_decision(durable2)[0] == "NEEDS_RECHECK"

        # R2-style replay/reconciliation: no second movement, metering or memory
        # commit is generated for the same completed access request.
        replay_move = steward2.handle(move)
        assert replay_move.disposition == "ALLOW_MOVEMENT"
        assert movement_count(steward2, move.request_id) == movement_records_before
        assert sum(
            1 for row in durable2.wal.read_valid_prefix().records if row.get("kind") == "COMMIT"
        ) == memory_commits_before
        replay_result = servant2.handle(result_cmd)
        assert replay_result.reason_code.startswith("IDEMPOTENT_REPLAY:COMMIT_ACCEPTED")
        assert durable2.status(RESULT_VIEW) == "NEEDS_RECHECK"

        # Restricted usage telemetry remains gated after restart.
        denied = usage2.view_usage(
            "usage:PSI-P9-I:1",
            TelemetryQuery(ACTOR, SESSION, "T2_AUDIT_DURABLE", "wrong", access.version),
        )
        assert denied["status"] == "DENIED"
        allowed = usage2.view_usage(
            "usage:PSI-P9-I:1",
            TelemetryQuery(ACTOR, SESSION, "T2_AUDIT_DURABLE", "audit-full-run", access.version),
        )
        assert allowed["status"] == "ALLOWED"
        assert allowed["usage"]["version_id"] == "version:PSI-P9-I:1"
        assert allowed["usage"]["evidence_kind"] == EVIDENCE_VERIFIED_CONSUMPTION

        # R8 replay is idempotent; changed payload under the same observation ID
        # remains a collision after restart and cannot turn NO_PROPOSAL into a proposal.
        assert curator2.evaluate(obs) == ()
        assert curator_record_count(curator2) == curator_records_before
        try:
            curator2.evaluate(observation(3.0))
        except CuratorPlanningError as exc:
            assert "OBSERVATION_ID_COLLISION" in str(exc)
        else:
            raise AssertionError("changed Curator payload reused a durable observation_id")
        assert curator2.counts()["proposals"] == 0
        assert curator_record_count(curator2) == curator_records_before

    print("PSI-MEMORY-FULL-BOUNDED-RUN-01 PASS_WITH_BOUNDARY")
    print("real_records=P9-I:OPEN|GATE_FOR|III.13:UNAUTHORIZED")
    print("verified_v1_consumption=PASS")
    print("association_not_upgraded=PASS")
    print("hypothetical_premise_change_invalidates_result=PASS")
    print("restart_preserves_current_v2_and_historical_v1_receipt=PASS")
    print("stale_result_reuse=NEEDS_RECHECK")
    print("access_reconciliation_no_duplicate_movement_or_commit=PASS")
    print("cost_quote_unknown_semantics=PASS")
    print("curator_no_proposal_identity_after_restart=PASS")
    print("telemetry_gate_after_restart=PASS")
    print("BOUNDARY: one deterministic single-process integration episode seeded from real PSI TSV records; the P9-I status transition is hypothetical and isolated; historical versions remain explicitly retrievable; no live LLM efficacy, semantic-understanding, distributed-exactly-once or claim that P9-I actually passed")


if __name__ == "__main__":
    main()
