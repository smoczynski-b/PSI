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


def seed() -> Workspace:
    return Workspace(
        contract_id="CURATOR-R8-TEST",
        contract_digest="curator-r8-test-v1",
        anchor="ROOT",
    )


def policy() -> CuratorPlanningPolicy:
    return CuratorPlanningPolicy(
        version="PLAN-R8",
        rules=(PlanningRule(
            rule_id="CAPACITY-HIGH",
            operation="EXPAND",
            metric="capacity_utilization",
            comparator="GTE",
            threshold=0.90,
            expected_benefit="restore headroom",
            estimated_cost=1.0,
            risk="bounded test risk",
            information_loss_risk="none intended",
            required_dependencies=("budget:memory",),
            rollback_requirement="retain pre-change snapshot",
            required_test="same task answer before/after",
        ),),
    )


def obs(value: float) -> DistrictObservation:
    return DistrictObservation(
        observation_id="OBS-R8",
        district_id="district:alpha",
        metrics={"capacity_utilization": value, "retrieval_cost": 1.0},
        observed_at="2026-09-30T21:10:00Z",
        policy_version="PLAN-R8",
    )


def make_stack(root: Path):
    p = policy()
    durable = DurableSharedMemoryRuntime(seed(), root / "memory.wal", lambda shared: None)
    servant = ServantRuntime(
        durable,
        root / "servant.wal",
        authorized_runbooks=("CURATOR-PLANNER-01",),
    )
    planner = CuratorPlannerRuntime(
        servant,
        root / "curator.wal",
        policy_lookup=lambda version: p if version == p.version else None,
        current_policy_version=lambda: p.version,
    )
    return durable, servant, planner


def expect_collision(planner: CuratorPlannerRuntime, value: float) -> None:
    try:
        planner.evaluate(obs(value))
    except CuratorPlanningError as exc:
        assert "OBSERVATION_ID_COLLISION" in str(exc)
    else:
        raise AssertionError(
            "same observation_id with changed payload was accepted after a no-proposal observation"
        )


def main() -> None:
    # Same-process witness: a below-threshold observation must reserve its ID.
    with TemporaryDirectory() as td:
        root = Path(td)
        _, _, planner = make_stack(root)
        assert planner.evaluate(obs(0.50)) == ()
        expect_collision(planner, 0.95)

    # Restart witness: the no-proposal identity must be durable, not RAM-only.
    with TemporaryDirectory() as td:
        root = Path(td)
        _, _, planner = make_stack(root)
        assert planner.evaluate(obs(0.50)) == ()
        _, _, planner2 = make_stack(root)
        expect_collision(planner2, 0.95)

    print("PSI-MEMORY-R8-NO-PROPOSAL-IDENTITY separating witness PASS")


if __name__ == "__main__":
    main()
