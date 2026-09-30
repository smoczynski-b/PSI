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
    TelemetryQuery,
    CAP_ACT,
    CAP_ENTER,
    CAP_EXPORT,
    CAP_TELEMETRY,
    CAP_TRANSIT,
)

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


def request(
    rid: str,
    *,
    operation: str,
    map_from: str,
    map_to: str,
    capability: str,
    policy_version: str,
    purpose: str = "solve-task",
    budget: CostVector | None = None,
    estimated: CostVector | None = None,
) -> MovementRequest:
    return MovementRequest(
        request_id=rid,
        session_id="session-1",
        actor_id="agent-A",
        operation=operation,
        map_from=map_from,
        map_to=map_to,
        declared_purpose=purpose,
        requested_capability=capability,
        policy_version=policy_version,
        budget=budget or cv(10),
        estimated_cost=estimated or cv(1),
        event_time="2026-09-30T16:40:00Z",
    )


def movement_count(steward: AccessStewardRuntime) -> int:
    return sum(1 for row in steward.chronicle.records() if row.get("kind") == "ACCESS_MOVEMENT")


def main() -> None:
    rules_v1 = (
        PolicyRule("agent-A", "session-1", "ENTER", OUTSIDE, "M1", "solve-task", CAP_ENTER),
    )
    rules_v2 = (
        PolicyRule("agent-A", "session-1", "TRANSIT", "M1", "M2", "solve-task", CAP_TRANSIT),
        PolicyRule("agent-A", "session-1", "TRANSIT", "M1", "MQ", "solve-task", CAP_TRANSIT),
        PolicyRule("agent-A", "session-1", "EXIT", "M2", OUTSIDE, "leave-task", CAP_TRANSIT),
        PolicyRule(
            "agent-A", "session-1", "VIEW_TELEMETRY", "M2", "M2", "audit",
            CAP_TELEMETRY, ("T2_AUDIT_DURABLE", "T3_AGGREGATED"),
        ),
    )
    p1 = GuardianAccessPolicy("G-1", rules_v1)
    p2 = GuardianAccessPolicy("G-2", rules_v2)
    store = PolicyStore((p1, p2), "G-1")

    maps = {
        "M1": MapState("M1"),
        "M2": MapState("M2"),
        "MQ": MapState("MQ", health_gate_open=False),
    }
    actual_costs: dict[str, CostVector] = {
        "actual-over": cv(3),
        "actual-zero": cv(0),
    }

    def meter(req: MovementRequest) -> CostVector:
        return actual_costs.get(req.request_id, req.estimated_cost)

    with TemporaryDirectory() as td:
        root = Path(td)
        seed = Workspace(
            contract_id="ACCESS-PRESENCE-01",
            contract_digest="guardian-access-presence-v1",
            anchor=ROOT_ANCHOR,
        )

        def durable_runtime():
            return DurableSharedMemoryRuntime(
                seed,
                root / "shared.wal.jsonl",
                lambda shared: None,
            )

        durable = durable_runtime()
        servant = ServantRuntime(durable, root / "servant.jsonl")
        steward = AccessStewardRuntime(
            servant,
            root / "access.jsonl",
            presence_anchor=ROOT_ANCHOR,
            policy_lookup=store.lookup,
            current_policy_version=store.current_version,
            map_state_lookup=maps.get,
            cost_meter=meter,
        )

        # Valid entry under Guardian policy. Presence becomes durable only via SERVANT.
        enter = request(
            "enter-1", operation="ENTER", map_from=OUTSIDE, map_to="M1",
            capability=CAP_ENTER, policy_version="G-1",
        )
        d = steward.handle(enter)
        assert d.disposition == "ALLOW_MOVEMENT", d
        assert d.reason_code == "MOVEMENT_COMMITTED_VIA_SERVANT"
        assert d.servant_disposition == "ACK_TRANSITION"
        assert steward.location("session-1") == "M1"
        assert movement_count(steward) == 1

        # Entry does not imply action, export, or telemetry visibility.
        ok, reason = steward.check_capability(
            actor_id="agent-A", session_id="session-1", capability=CAP_ACT,
            purpose="solve-task", policy_version="G-1",
        )
        assert not ok and reason == "NO_MATCHING_GUARDIAN_RULE"
        ok, reason = steward.check_capability(
            actor_id="agent-A", session_id="session-1", capability=CAP_EXPORT,
            purpose="solve-task", policy_version="G-1", map_to="M2",
        )
        assert not ok and reason == "NO_MATCHING_GUARDIAN_RULE"
        q = steward.view_telemetry(TelemetryQuery(
            "agent-A", "session-1", "T2_AUDIT_DURABLE", "audit", "G-1"
        ))
        assert q["status"] == "DENIED"

        # Guardian changes policy. Old version is not silently reinterpreted.
        store.current = "G-2"
        old_policy_move = request(
            "old-policy", operation="TRANSIT", map_from="M1", map_to="M2",
            capability=CAP_TRANSIT, policy_version="G-1",
        )
        d = steward.handle(old_policy_move)
        assert d.disposition == "DENY_ACCESS"
        assert d.reason_code == "POLICY_VERSION_NOT_CURRENT"
        assert steward.location("session-1") == "M1"

        # Missing policy fails closed.
        store.current = "G-missing"
        missing = request(
            "missing-policy", operation="TRANSIT", map_from="M1", map_to="M2",
            capability=CAP_TRANSIT, policy_version="G-missing",
        )
        d = steward.handle(missing)
        assert d.disposition == "STOP_ESCALATE"
        assert d.reason_code == "GUARDIAN_POLICY_ABSENT"
        assert steward.location("session-1") == "M1"
        store.current = "G-2"

        # Location mismatch blocks logical teleportation.
        mismatch = request(
            "mismatch", operation="TRANSIT", map_from="M2", map_to="M1",
            capability=CAP_TRANSIT, policy_version="G-2",
        )
        d = steward.handle(mismatch)
        assert d.disposition == "DENY_ACCESS"
        assert d.reason_code == "SESSION_LOCATION_MISMATCH"

        # Unknown target and closed health gate fail closed without releasing quarantine.
        unknown = request(
            "unknown-target", operation="TRANSIT", map_from="M1", map_to="UNKNOWN",
            capability=CAP_TRANSIT, policy_version="G-2",
        )
        d = steward.handle(unknown)
        assert d.disposition == "STOP_ESCALATE"
        assert d.reason_code == "UNKNOWN_TARGET_MAP"
        quarantined = request(
            "quarantine-target", operation="TRANSIT", map_from="M1", map_to="MQ",
            capability=CAP_TRANSIT, policy_version="G-2",
        )
        d = steward.handle(quarantined)
        assert d.disposition == "DENY_ACCESS"
        assert d.reason_code == "TARGET_HEALTH_GATE_CLOSED"
        assert steward.location("session-1") == "M1"

        # Cross-map movement has explicit positive cost and hard budget.
        zero_estimate = request(
            "zero-estimate", operation="TRANSIT", map_from="M1", map_to="M2",
            capability=CAP_TRANSIT, policy_version="G-2", estimated=cv(0),
        )
        d = steward.handle(zero_estimate)
        assert d.disposition == "STOP_ESCALATE"
        assert d.reason_code == "CROSS_MAP_ZERO_ESTIMATED_COST"

        estimated_over = request(
            "estimate-over", operation="TRANSIT", map_from="M1", map_to="M2",
            capability=CAP_TRANSIT, policy_version="G-2", budget=cv(0.5), estimated=cv(1),
        )
        d = steward.handle(estimated_over)
        assert d.disposition == "DENY_ACCESS"
        assert d.reason_code == "ESTIMATED_COST_EXCEEDS_BUDGET"

        actual_over = request(
            "actual-over", operation="TRANSIT", map_from="M1", map_to="M2",
            capability=CAP_TRANSIT, policy_version="G-2", budget=cv(2), estimated=cv(1),
        )
        d = steward.handle(actual_over)
        assert d.disposition == "DENY_ACCESS"
        assert d.reason_code == "ACTUAL_COST_EXCEEDS_BUDGET"

        actual_zero = request(
            "actual-zero", operation="TRANSIT", map_from="M1", map_to="M2",
            capability=CAP_TRANSIT, policy_version="G-2", estimated=cv(1),
        )
        d = steward.handle(actual_zero)
        assert d.disposition == "STOP_ESCALATE"
        assert d.reason_code == "CROSS_MAP_ZERO_ACTUAL_COST"
        assert steward.location("session-1") == "M1"

        # Valid transit. No export capability is inferred from movement.
        transit = request(
            "transit-ok", operation="TRANSIT", map_from="M1", map_to="M2",
            capability=CAP_TRANSIT, policy_version="G-2", estimated=cv(1),
        )
        d = steward.handle(transit)
        assert d.disposition == "ALLOW_MOVEMENT", d
        assert steward.location("session-1") == "M2"
        assert d.actual_cost.l1 > 0
        assert movement_count(steward) == 2
        ok, reason = steward.check_capability(
            actor_id="agent-A", session_id="session-1", capability=CAP_EXPORT,
            purpose="solve-task", policy_version="G-2", map_to="M1",
        )
        assert not ok and reason == "NO_MATCHING_GUARDIAN_RULE"

        # Telemetry requires its own capability and class. Aggregation reveals no identities.
        full = steward.view_telemetry(TelemetryQuery(
            "agent-A", "session-1", "T2_AUDIT_DURABLE", "audit", "G-2"
        ))
        assert full["status"] == "ALLOWED"
        assert len(full["records"]) == 2
        aggregate = steward.view_telemetry(TelemetryQuery(
            "agent-A", "session-1", "T3_AGGREGATED", "audit", "G-2"
        ))
        assert aggregate["status"] == "ALLOWED"
        assert "records" not in aggregate
        assert sum(aggregate["counts"].values()) == 2

        # Durable shared WAL contains the movement transactions issued through SERVANT.
        wal = durable.wal.read_valid_prefix().records
        committed = {r["txid"] for r in wal if r.get("kind") == "COMMIT"}
        assert "access:enter-1" in committed
        assert "access:transit-ok" in committed
        servant_records = servant.chronicle.records()
        accepted = [
            r for r in servant_records
            if r.get("kind") == "SERVANT_RESULT"
            and str(r.get("payload", {}).get("reason_code", "")) == "COMMIT_ACCEPTED"
        ]
        assert len(accepted) >= 2

        # Process-style restart/replay reconstructs presence from authoritative durable state.
        movements_before_restart = movement_count(steward)
        durable2 = durable_runtime()
        servant2 = ServantRuntime(durable2, root / "servant.jsonl")
        steward2 = AccessStewardRuntime(
            servant2,
            root / "access.jsonl",
            presence_anchor=ROOT_ANCHOR,
            policy_lookup=store.lookup,
            current_policy_version=store.current_version,
            map_state_lookup=maps.get,
            cost_meter=meter,
        )
        assert steward2.location("session-1") == "M2"
        replay = steward2.handle(transit)
        assert replay.disposition == "ALLOW_MOVEMENT"
        assert replay.reason_code.startswith("IDEMPOTENT_REPLAY:")
        assert steward2.location("session-1") == "M2"
        assert movement_count(steward2) == movements_before_restart

        # Same request id with another meaning is a collision, never a second movement.
        collision = request(
            "transit-ok", operation="TRANSIT", map_from="M1", map_to="M2",
            capability=CAP_TRANSIT, policy_version="G-2", purpose="different-purpose",
        )
        d = steward2.handle(collision)
        assert d.disposition == "STOP_ESCALATE"
        assert d.reason_code == "REQUEST_ID_COLLISION"
        assert steward2.location("session-1") == "M2"
        assert movement_count(steward2) == movements_before_restart

        # Legal exit removes durable presence; restart does not create phantom presence.
        exit_req = request(
            "exit-ok", operation="EXIT", map_from="M2", map_to=OUTSIDE,
            capability=CAP_TRANSIT, policy_version="G-2", purpose="leave-task",
        )
        d = steward2.handle(exit_req)
        assert d.disposition == "ALLOW_MOVEMENT"
        assert steward2.location("session-1") == OUTSIDE

        durable3 = durable_runtime()
        servant3 = ServantRuntime(durable3, root / "servant.jsonl")
        steward3 = AccessStewardRuntime(
            servant3,
            root / "access.jsonl",
            presence_anchor=ROOT_ANCHOR,
            policy_lookup=store.lookup,
            current_policy_version=store.current_version,
            map_state_lookup=maps.get,
            cost_meter=meter,
        )
        assert steward3.location("session-1") == OUTSIDE

        # Source-level guard: F2.1 contains no direct durable.commit bypass.
        source = (Path(__file__).resolve().parent / "access_steward_runtime.py").read_text(encoding="utf-8")
        assert "durable.commit(" not in source
        assert "self.servant.handle(command)" in source
        assert "DECLARE_DOMAIN_TRUTH" not in source

    print("PSI-MEMORY-ACCESS-STEWARD-F2.1 PASS_WITH_BOUNDARY")
    print("guardian_policy_execution_only=PASS")
    print("session_presence_single_location=PASS")
    print("enter_act_export_telemetry_separation=PASS")
    print("cross_map_cost_and_budget=PASS")
    print("target_health_gate_fail_closed=PASS")
    print("durable_presence_via_servant_mvcc_wal=PASS")
    print("movement_audit_append_only=PASS")
    print("restart_reconstructs_presence=PASS")
    print("idempotent_request_replay=PASS")
    print("request_id_collision_stop=PASS")
    print("telemetry_visibility_and_aggregation=PASS")
    print("semantic_truth_authority=ABSENT")
    print("BOUNDARY: deterministic single-process reference runtime over supplied Guardian policy; no Guardian policy authoring/runtime, no distributed concurrency, no live FORUM routing, no autonomous anomaly detection, no semantic map mutation")


if __name__ == "__main__":
    main()
