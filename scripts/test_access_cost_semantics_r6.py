#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from active_memory import Workspace
from durable_shared_memory import DurableSharedMemoryRuntime
from servant_runtime import ServantRuntime
from access_steward_runtime import (
    AccessStewardRuntime,
    CostVector,
    GuardianAccessPolicy,
    MapState,
    MovementRequest,
    OUTSIDE,
    PolicyRule,
    CAP_ENTER,
)

ROOT_ANCHOR = "ACCESS_PRESENCE_ROOT"


def cv(value: float = 0.0) -> CostVector:
    return CostVector(compute=value)


def main() -> None:
    policy = GuardianAccessPolicy("G-R6", (
        PolicyRule(
            "agent-A", "session-1", "ENTER", OUTSIDE, "M1",
            "solve-task", CAP_ENTER,
        ),
    ))
    maps = {"M1": MapState("M1")}

    with TemporaryDirectory() as td:
        root = Path(td)
        seed = Workspace(
            contract_id="ACCESS-R6-01",
            contract_digest="access-r6-cost-semantics-v1",
            anchor=ROOT_ANCHOR,
        )
        durable = DurableSharedMemoryRuntime(seed, root / "shared.wal.jsonl", lambda shared: None)
        servant = ServantRuntime(durable, root / "servant.jsonl")
        steward = AccessStewardRuntime(
            servant,
            root / "access.jsonl",
            presence_anchor=ROOT_ANCHOR,
            policy_lookup=lambda version: policy if version == policy.version else None,
            current_policy_version=lambda: policy.version,
            map_state_lookup=maps.get,
            cost_meter=lambda request: cv(3),
        )

        req = MovementRequest(
            request_id="r6-over-budget",
            session_id="session-1",
            actor_id="agent-A",
            operation="ENTER",
            map_from=OUTSIDE,
            map_to="M1",
            declared_purpose="solve-task",
            requested_capability=CAP_ENTER,
            policy_version=policy.version,
            budget=cv(2),
            estimated_cost=cv(1),
            event_time="2026-09-30T20:45:00Z",
        )
        decision = steward.handle(req)

        assert decision.disposition == "DENY_ACCESS", decision
        assert decision.reason_code == "ACTUAL_COST_EXCEEDS_BUDGET", decision
        assert steward.location("session-1") == OUTSIDE

        # R6 separating witness: cost_meter returned 3. The denial must not
        # silently replace that evidence with a zero vector.
        assert decision.actual_cost.compute == 3, decision

        result_rows = [
            row for row in steward.chronicle.records()
            if row.get("kind") == "ACCESS_RESULT"
            and row.get("payload", {}).get("request_id") == req.request_id
        ]
        assert len(result_rows) == 1
        assert result_rows[0]["payload"]["actual_cost"]["compute"] == 3

        commits = [
            row for row in durable.wal.read_valid_prefix().records
            if row.get("kind") == "COMMIT"
        ]
        assert not commits

    print("PSI-MEMORY-R6-COST-SEMANTICS separating witness PASS")


if __name__ == "__main__":
    main()
