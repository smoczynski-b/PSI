#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from active_memory import Workspace
from durable_shared_memory import DurableSharedMemoryRuntime
from servant_runtime import ServantCommand, ServantRuntime
from access_steward_runtime import (
    AccessStewardRuntime,
    CostVector,
    GuardianAccessPolicy,
    MapState,
    MovementRequest,
    OUTSIDE,
    PolicyRule,
    CAP_ENTER,
    CAP_TRANSIT,
)
from test_servant_runtime import make_durable, upsert

ROOT_ANCHOR = "ACCESS_PRESENCE_ROOT"


class PolicyStore:
    def __init__(self, policies, current: str):
        self.policies = {p.version: p for p in policies}
        self.current = current

    def lookup(self, version: str):
        return self.policies.get(version)

    def current_version(self) -> str:
        return self.current


def cv(value: float = 0.0) -> CostVector:
    return CostVector(compute=value)


def req(
    rid: str,
    *,
    operation: str,
    map_from: str,
    map_to: str,
    capability: str,
    policy_version: str,
) -> MovementRequest:
    return MovementRequest(
        request_id=rid,
        session_id="session-r2",
        actor_id="agent-r2",
        operation=operation,
        map_from=map_from,
        map_to=map_to,
        declared_purpose="solve-r2",
        requested_capability=capability,
        policy_version=policy_version,
        budget=cv(10),
        estimated_cost=cv(1),
        event_time="2026-09-30T20:30:00Z",
    )


def committed_txids(durable) -> set[str]:
    return {
        str(r["txid"])
        for r in durable.wal.read_valid_prefix().records
        if r.get("kind") == "COMMIT"
    }


def movement_count(steward: AccessStewardRuntime, request_id: str) -> int:
    return sum(
        1
        for r in steward.chronicle.records()
        if r.get("kind") == "ACCESS_MOVEMENT"
        and str(r.get("payload", {}).get("request_id", "")) == request_id
    )


def result_count(steward: AccessStewardRuntime, request_id: str) -> int:
    return sum(
        1
        for r in steward.chronicle.records()
        if r.get("kind") == "ACCESS_RESULT"
        and str(r.get("payload", {}).get("request_id", "")) == request_id
    )


def access_fixture(root: Path):
    p1 = GuardianAccessPolicy(
        "G-R2",
        (
            PolicyRule("agent-r2", "session-r2", "ENTER", OUTSIDE, "M1", "solve-r2", CAP_ENTER),
            PolicyRule("agent-r2", "session-r2", "TRANSIT", "M1", "M2", "solve-r2", CAP_TRANSIT),
        ),
    )
    store = PolicyStore((p1,), "G-R2")
    maps = {"M1": MapState("M1"), "M2": MapState("M2")}
    meter_calls = {"n": 0}

    def meter(request: MovementRequest) -> CostVector:
        meter_calls["n"] += 1
        return request.estimated_cost

    seed = Workspace(
        contract_id="ACCESS-R2",
        contract_digest="access-r2-v1",
        anchor=ROOT_ANCHOR,
    )

    def durable_runtime():
        return DurableSharedMemoryRuntime(seed, root / "shared.wal", lambda shared: None)

    def make_stack():
        durable = durable_runtime()
        servant = ServantRuntime(durable, root / "servant.wal")
        steward = AccessStewardRuntime(
            servant,
            root / "access.wal",
            presence_anchor=ROOT_ANCHOR,
            policy_lookup=store.lookup,
            current_policy_version=store.current_version,
            map_state_lookup=maps.get,
            cost_meter=meter,
        )
        return durable, servant, steward

    return make_stack, meter_calls


def simulate_access_committed_before_movement(steward: AccessStewardRuntime, request: MovementRequest) -> None:
    # Exact post-PREPARED boundary from R2: ACCESS observed and measured the
    # request, persisted the historical binding, SERVANT committed durable
    # presence, but ACCESS_MOVEMENT/RESULT were not yet written.
    steward._observed(request)
    actual = steward.cost_meter(request)
    assert actual.l1 > 0
    command = steward._servant_command(request)
    before = steward.location(request.session_id)
    expected_after = request.map_to if request.operation != "EXIT" else OUTSIDE
    steward._prepared(
        request,
        command,
        before=before,
        after=expected_after,
        actual=actual,
    )
    out = steward.servant.handle(command)
    assert out.disposition == "ACK_TRANSITION"
    assert command.txid in committed_txids(steward.servant.durable)


def append_movement_without_result(steward: AccessStewardRuntime, request: MovementRequest) -> None:
    command = steward._servant_command(request)
    steward.chronicle.append("MOVEMENT", request.request_id, {
        "request_id": request.request_id,
        "request_fingerprint": request.fingerprint(),
        "session_id": request.session_id,
        "actor_id": request.actor_id,
        "map_from": request.map_from,
        "map_to": request.map_to,
        "declared_purpose": request.declared_purpose,
        "policy_version": request.policy_version,
        "capabilities_used": [request.requested_capability],
        "event_time": request.event_time,
        "estimated_cost": request.estimated_cost.as_dict(),
        "actual_cost": request.estimated_cost.as_dict(),
        "result": "MOVED",
        "telemetry_class": "T2_AUDIT_DURABLE",
        "servant_command_id": command.command_id,
        "txid": command.txid,
    })


def test_servant_commit_without_result() -> None:
    with TemporaryDirectory() as td:
        root = Path(td)
        memory = root / "memory.wal"
        chronicle = root / "servant.wal"
        durable = make_durable(memory)
        servant = ServantRuntime(durable, chronicle)
        command = ServantCommand(
            "CMD-R2",
            "TRANSACT",
            txid="TX-R2",
            proposals=(upsert("P-R2"),),
        )

        # OBSERVED has been acknowledged, then durable memory reaches COMMIT/ACK,
        # then the process dies before SERVANT_RESULT.
        servant._chronicle_observed(command, durable.revision)
        committed = durable.commit(command.txid, command.proposals)
        assert committed.result.status == "COMMITTED"
        assert committed.wal_state == "ACK"
        wal_count = len(durable.wal.read_valid_prefix().records)

        durable2 = make_durable(memory)
        servant2 = ServantRuntime(durable2, chronicle)
        replay = servant2.handle(command)
        assert replay.disposition == "ACK_TRANSITION", replay
        assert replay.reason_code.startswith("IDEMPOTENT_REPLAY:COMMIT_ACCEPTED"), replay
        assert durable2.revision == 1
        assert len(durable2.wal.read_valid_prefix().records) == wal_count

        collision = ServantCommand(
            "CMD-R2",
            "TRANSACT",
            txid="TX-R2-OTHER",
            proposals=(upsert("P-R2-OTHER", base=1),),
        )
        blocked = servant2.handle(collision)
        assert blocked.reason_code == "COMMAND_ID_COLLISION"
        assert durable2.revision == 1


def test_access_commit_before_movement_and_result() -> None:
    with TemporaryDirectory() as td:
        root = Path(td)
        make_stack, meter_calls = access_fixture(root)
        durable, servant, steward = make_stack()
        enter = req(
            "enter-r2-a",
            operation="ENTER",
            map_from=OUTSIDE,
            map_to="M1",
            capability=CAP_ENTER,
            policy_version="G-R2",
        )
        simulate_access_committed_before_movement(steward, enter)
        assert steward.location("session-r2") == "M1"
        calls_before_restart = meter_calls["n"]
        assert movement_count(steward, enter.request_id) == 0
        assert result_count(steward, enter.request_id) == 0

        durable2, servant2, steward2 = make_stack()
        replay = steward2.handle(enter)
        assert replay.disposition == "ALLOW_MOVEMENT", replay
        assert replay.reason_code.startswith("IDEMPOTENT_REPLAY:MOVEMENT_COMMITTED_VIA_SERVANT"), replay
        assert meter_calls["n"] == calls_before_restart
        assert movement_count(steward2, enter.request_id) == 1
        assert result_count(steward2, enter.request_id) >= 1
        assert steward2.location("session-r2") == "M1"
        assert committed_txids(durable2) == {"access:enter-r2-a"}


def test_access_movement_without_result() -> None:
    with TemporaryDirectory() as td:
        root = Path(td)
        make_stack, meter_calls = access_fixture(root)
        durable, servant, steward = make_stack()
        enter = req(
            "enter-r2-b",
            operation="ENTER",
            map_from=OUTSIDE,
            map_to="M1",
            capability=CAP_ENTER,
            policy_version="G-R2",
        )
        simulate_access_committed_before_movement(steward, enter)
        append_movement_without_result(steward, enter)
        calls_before_restart = meter_calls["n"]
        assert movement_count(steward, enter.request_id) == 1
        assert result_count(steward, enter.request_id) == 0

        _, _, steward2 = make_stack()
        replay = steward2.handle(enter)
        assert replay.disposition == "ALLOW_MOVEMENT", replay
        assert meter_calls["n"] == calls_before_restart
        assert movement_count(steward2, enter.request_id) == 1
        assert result_count(steward2, enter.request_id) >= 1


def test_reconciliation_not_based_on_current_location() -> None:
    with TemporaryDirectory() as td:
        root = Path(td)
        make_stack, meter_calls = access_fixture(root)
        durable, servant, steward = make_stack()
        enter = req(
            "enter-r2-c",
            operation="ENTER",
            map_from=OUTSIDE,
            map_to="M1",
            capability=CAP_ENTER,
            policy_version="G-R2",
        )
        simulate_access_committed_before_movement(steward, enter)
        assert steward.location("session-r2") == "M1"

        # Later independent committed movement changes the current projection.
        transit = req(
            "transit-r2-c",
            operation="TRANSIT",
            map_from="M1",
            map_to="M2",
            capability=CAP_TRANSIT,
            policy_version="G-R2",
        )
        moved = steward.handle(transit)
        assert moved.disposition == "ALLOW_MOVEMENT"
        assert steward.location("session-r2") == "M2"
        calls_before_restart = meter_calls["n"]

        durable2, servant2, steward2 = make_stack()
        assert steward2.location("session-r2") == "M2"
        replay_enter = steward2.handle(enter)
        assert replay_enter.disposition == "ALLOW_MOVEMENT", replay_enter
        assert replay_enter.location_before == OUTSIDE
        assert replay_enter.location_after == "M1"
        assert steward2.location("session-r2") == "M2"
        assert meter_calls["n"] == calls_before_restart
        assert committed_txids(durable2) == {"access:enter-r2-c", "access:transit-r2-c"}

        changed = req(
            "enter-r2-c",
            operation="ENTER",
            map_from=OUTSIDE,
            map_to="M1",
            capability=CAP_ENTER,
            policy_version="G-R2",
        )
        # Same semantic fields above would be the same fingerprint, so alter a
        # field by rebuilding directly to exercise request-id collision.
        changed = MovementRequest(
            request_id=changed.request_id,
            session_id=changed.session_id,
            actor_id=changed.actor_id,
            operation=changed.operation,
            map_from=changed.map_from,
            map_to=changed.map_to,
            declared_purpose="different-r2-purpose",
            requested_capability=changed.requested_capability,
            policy_version=changed.policy_version,
            budget=changed.budget,
            estimated_cost=changed.estimated_cost,
            event_time=changed.event_time,
        )
        collision = steward2.handle(changed)
        assert collision.reason_code == "REQUEST_ID_COLLISION"
        assert steward2.location("session-r2") == "M2"


def main() -> None:
    test_servant_commit_without_result()
    test_access_commit_before_movement_and_result()
    test_access_movement_without_result()
    test_reconciliation_not_based_on_current_location()
    print("PSI-MEMORY-R2-RESULT-RECONCILIATION-01 PASS")
    print("servant_commit_without_result=PASS")
    print("access_commit_before_movement=PASS")
    print("access_movement_without_result=PASS")
    print("later_independent_movement=PASS")
    print("no_duplicate_meter_or_commit=PASS")
    print("id_collision_after_recovery=PASS")


if __name__ == "__main__":
    main()
