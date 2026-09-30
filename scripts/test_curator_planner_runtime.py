#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from active_memory import Workspace
from curator_planner_runtime import (
    CuratorPlanningError,
    CuratorPlanningPolicy,
    CuratorPlannerRuntime,
    DistrictObservation,
    PlanningRule,
)
from durable_shared_memory import DurableSharedMemoryRuntime
from servant_runtime import ServantRuntime


class PolicyStore:
    def __init__(self, policies, current: str):
        self.policies = {p.version: p for p in policies}
        self.current = current

    def lookup(self, version: str):
        return self.policies.get(version)

    def current_version(self) -> str:
        return self.current


def seed() -> Workspace:
    return Workspace(
        contract_id="CURATOR-PLANNER-TEST",
        contract_digest="curator-planner-test-v1",
        anchor="ROOT",
    )


def policy(version="PLAN-1", threshold=0.90, cost=12.0):
    return CuratorPlanningPolicy(
        version=version,
        rules=(
            PlanningRule(
                rule_id="CAPACITY-HIGH",
                operation="EXPAND",
                metric="capacity_utilization",
                comparator="GTE",
                threshold=threshold,
                expected_benefit="restore administrative headroom",
                estimated_cost=cost,
                risk="migration may temporarily increase retrieval latency",
                information_loss_risk="none intended; representation must remain task-equivalent",
                required_dependencies=("budget:memory", "guardian:access-review"),
                rollback_requirement="retain pre-change snapshot and route",
                required_test="same task answer before/after execution plus capacity below threshold",
            ),
        ),
    )


def observation(oid="OBS-1", utilization=0.95, version="PLAN-1"):
    return DistrictObservation(
        observation_id=oid,
        district_id="district:alpha",
        metrics={
            "capacity_utilization": utilization,
            "retrieval_cost": 3.0,
            "transition_cost": 1.0,
        },
        observed_at="2026-09-30T20:05:00+02:00",
        policy_version=version,
    )


def make_stack(root: Path, store: PolicyStore, *, authorize=True):
    durable = DurableSharedMemoryRuntime(seed(), root / "memory.wal", lambda shared: None)
    servant = ServantRuntime(
        durable,
        root / "servant.wal",
        authorized_runbooks=(("CURATOR-PLANNER-01",) if authorize else ()),
    )
    planner = CuratorPlannerRuntime(
        servant,
        root / "curator-planner.wal",
        policy_lookup=store.lookup,
        current_policy_version=store.current_version,
    )
    return durable, servant, planner


def main():
    with TemporaryDirectory() as td:
        root = Path(td)
        p1 = policy()
        store = PolicyStore((p1,), "PLAN-1")
        durable, servant, planner = make_stack(root, store)

        revision_before = durable.revision
        workspace_digest_before = durable.shared.memory.workspace.state_digest

        # Explicit threshold breach produces an auditable proposal only.
        proposals = planner.evaluate(observation())
        assert len(proposals) == 1
        proposal = proposals[0]
        assert proposal.proposed_operation == "EXPAND"
        assert proposal.status == "PROPOSED"
        assert proposal.supporting_metrics == (("capacity_utilization", 0.95),)
        assert proposal.estimated_cost == 12.0
        assert proposal.required_test.startswith("same task answer")
        assert proposal.required_dependencies == ("budget:memory", "guardian:access-review")

        # Proposal is not execution: authoritative memory, budget, access policy
        # and epistemic state are untouched by planner output.
        assert durable.revision == revision_before == 0
        assert durable.shared.memory.workspace.state_digest == workspace_digest_before
        assert not hasattr(planner, "execute")
        assert not hasattr(planner, "apply")
        assert not hasattr(planner, "allocate")

        # Below threshold produces no proposal and no durable record.
        counts_before_low = planner.counts()
        low = planner.evaluate(observation("OBS-LOW", 0.50))
        assert low == ()
        assert planner.counts() == counts_before_low

        # Exact replay is idempotent: no second proposal/gate record.
        counts_before_replay = planner.counts()
        servant_records_before = len(servant.chronicle.records())
        replay = planner.evaluate(observation())
        assert len(replay) == 1
        assert replay[0] == proposal
        assert planner.counts() == counts_before_replay
        assert len(servant.chronicle.records()) == servant_records_before

        # Same observation id with changed metrics fails closed.
        try:
            planner.evaluate(observation("OBS-1", 0.99))
            raise AssertionError("observation id collision was accepted")
        except CuratorPlanningError as exc:
            assert "OBSERVATION_ID_COLLISION" in str(exc)

        # Same policy version/rule id silently changed underneath the planner
        # would imply a different proposal with the same id: fail closed.
        changed = policy(threshold=0.80, cost=99.0)
        store.policies["PLAN-1"] = changed
        try:
            planner.evaluate(observation())
            raise AssertionError("proposal id collision was accepted")
        except CuratorPlanningError as exc:
            assert "PROPOSAL_ID_COLLISION" in str(exc)
        store.policies["PLAN-1"] = p1

        # Old/non-current policy is not silently used.
        store.current = "PLAN-2"
        try:
            planner.evaluate(observation("OBS-OLD", 0.99, "PLAN-1"))
            raise AssertionError("non-current policy was accepted")
        except CuratorPlanningError as exc:
            assert "PLANNING_POLICY_NOT_CURRENT" in str(exc)
        store.current = "PLAN-1"

        # Restart recovers proposal identity and PROPOSED status without touching memory.
        durable2, servant2, planner2 = make_stack(root, store)
        assert durable2.revision == 0
        recovered = planner2.proposal(proposal.proposal_id)
        assert recovered == proposal
        assert recovered.status == "PROPOSED"
        assert planner2.counts()["proposals"] == 1
        replay2 = planner2.evaluate(observation())
        assert replay2 == (proposal,)

        # Planner persistence went through the authorized procedural gate.
        accepted = [
            r for r in servant2.chronicle.records()
            if r.get("kind") == "SERVANT_RESULT"
            and str(r.get("payload", {}).get("reason_code", "")).startswith("INSTITUTION_ACTION_ACCEPTED:NOTICE")
        ]
        assert len(accepted) == 1

    # Without the Curator planning runbook there is no proposal persistence.
    with TemporaryDirectory() as td:
        root = Path(td)
        store = PolicyStore((policy(),), "PLAN-1")
        durable, _, planner = make_stack(root, store, authorize=False)
        try:
            planner.evaluate(observation())
            raise AssertionError("proposal bypassed SERVANT runbook gate")
        except CuratorPlanningError as exc:
            assert "RUNBOOK_NOT_AUTHORIZED" in str(exc)
        assert durable.revision == 0
        assert planner.counts()["records"] == 0

    print("PSI-MEMORY-CURATOR-PLANNER-F3.3-01 PASS_WITH_BOUNDARY")
    print("explicit_threshold_policy=PASS")
    print("proposal_only_no_execution_authority=PASS")
    print("authoritative_memory_unchanged=PASS")
    print("below_threshold_no_proposal=PASS")
    print("replay_idempotent=PASS")
    print("observation_collision_fail_closed=PASS")
    print("proposal_collision_fail_closed=PASS")
    print("non_current_policy_fail_closed=PASS")
    print("restart_recovers_proposed_state=PASS")
    print("servant_runbook_gate=PASS")
    print("semantic_truth_authority=ABSENT")
    print("resource_allocation_authority=ABSENT")
    print("BOUNDARY: deterministic single-process proposal engine over explicit administrative metrics and PSI_AGENT-owned rules; no execution, no self-authored thresholds, no budget allocation, no access-policy mutation, no epistemic-status mutation")


if __name__ == "__main__":
    main()
