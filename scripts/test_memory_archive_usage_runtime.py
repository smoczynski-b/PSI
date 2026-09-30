#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import json

from active_memory import Workspace
from access_steward_runtime import (
    AccessStewardRuntime,
    CostVector,
    GuardianAccessPolicy,
    MapState,
    MovementRequest,
    OUTSIDE,
    PolicyRule,
    TelemetryQuery,
    CAP_ENTER,
    CAP_TELEMETRY,
    CAP_TRANSIT,
)
from durable_shared_memory import DurableSharedMemoryRuntime
from memory_archive_runtime import ArchiveManifest, MemoryArchiveRuntime
from memory_archive_usage_runtime import MemoryArchiveUsageRuntime, UsageArchiveError
from servant_runtime import ServantRuntime

ROOT = "ACCESS_PRESENCE_ROOT"


class PolicyStore:
    def __init__(self, policy: GuardianAccessPolicy):
        self.policy = policy

    def lookup(self, version: str):
        return self.policy if version == self.policy.version else None

    def current_version(self):
        return self.policy.version


def cv(value: float) -> CostVector:
    return CostVector(compute=value)


def movement(rid: str, operation: str, map_from: str, map_to: str, cap: str) -> MovementRequest:
    return MovementRequest(
        request_id=rid,
        session_id="session-1",
        actor_id="agent-A",
        operation=operation,
        map_from=map_from,
        map_to=map_to,
        declared_purpose="solve-task",
        requested_capability=cap,
        policy_version="G-1",
        budget=cv(10),
        estimated_cost=cv(1),
        event_time="2026-09-30T17:10:00Z",
    )


def no_views(shared):
    return None


def make_policy() -> GuardianAccessPolicy:
    return GuardianAccessPolicy("G-1", (
        PolicyRule("agent-A", "session-1", "ENTER", OUTSIDE, "M1", "solve-task", CAP_ENTER),
        PolicyRule("agent-A", "session-1", "TRANSIT", "M1", "M2", "solve-task", CAP_TRANSIT),
        PolicyRule(
            "agent-A", "session-1", "VIEW_TELEMETRY", "M2", "M2", "audit",
            CAP_TELEMETRY, ("T2_AUDIT_DURABLE", "T3_AGGREGATED"),
        ),
    ))


def map_workspace() -> Workspace:
    return Workspace(
        contract_id="MAP-M2-CONTRACT",
        contract_digest="map-m2-contract-v1",
        anchor="M2",
    )


def publish_map_version(archive: MemoryArchiveRuntime, *, version_id="version:M2:1", object_id="M2"):
    ws = map_workspace()
    archive.store_snapshot("snapshot:M2:0", ws)
    manifest = ArchiveManifest(
        version_id=version_id,
        object_id=object_id,
        parent_version_ids=(),
        base_snapshot_id="snapshot:M2:0",
        delta_ids=(),
        content_digest=ws.state_digest,
        contract_id=ws.contract_id,
        contract_digest=ws.contract_digest,
        provenance_refs=("source:map-M2", "contract:MAP-M2-CONTRACT"),
        epistemic_status_ref="VALID",
        access_policy_ref="policy:G-1",
        lifecycle_state="ACTIVE",
        created_at="2026-09-30T17:10:01Z",
    )
    archive.publish_version(manifest)
    archive.publish_current(object_id, version_id)
    return manifest


def main():
    with TemporaryDirectory() as td:
        root = Path(td)
        seed = Workspace("ACCESS-PRESENCE-01", "presence-v1", ROOT)
        durable = DurableSharedMemoryRuntime(seed, root / "shared.wal", no_views)
        servant = ServantRuntime(
            durable,
            root / "servant.wal",
            authorized_runbooks=("CURATOR-ARCHIVE-01",),
        )
        policy = make_policy()
        store = PolicyStore(policy)
        maps = {"M1": MapState("M1"), "M2": MapState("M2")}
        steward = AccessStewardRuntime(
            servant,
            root / "access.wal",
            presence_anchor=ROOT,
            policy_lookup=store.lookup,
            current_policy_version=store.current_version,
            map_state_lookup=maps.get,
            cost_meter=lambda req: req.estimated_cost,
        )
        archive = MemoryArchiveRuntime(servant, root / "archive.wal")
        publish_map_version(archive)
        usage = MemoryArchiveUsageRuntime(archive, steward, root / "archive-usage.wal")

        # Session enters M1, then legally moves to M2 under Guardian policy.
        assert steward.handle(movement("enter-1", "ENTER", OUTSIDE, "M1", CAP_ENTER)).disposition == "ALLOW_MOVEMENT"
        transit = steward.handle(movement("transit-1", "TRANSIT", "M1", "M2", CAP_TRANSIT))
        assert transit.disposition == "ALLOW_MOVEMENT"
        assert transit.actual_cost.l1 == 1.0

        # L2 binds the exact archived map version to the exact committed movement.
        ref = usage.link_movement(
            "usage-1", "version:M2:1", "transit-1", created_at="2026-09-30T17:10:02Z"
        )
        assert ref.version_id == "version:M2:1"
        assert ref.session_id == "session-1"
        assert ref.map_from == "M1" and ref.map_to == "M2"
        assert ref.actual_cost.l1 == 1.0
        assert ref.telemetry_class == "T2_AUDIT_DURABLE"
        assert usage.counts() == {"usage_refs": 1, "records": 1}

        # Replay of the same L2 binding is idempotent.
        before = usage.counts()
        replay = usage.link_movement(
            "usage-1", "version:M2:1", "transit-1", created_at="2026-09-30T17:10:02Z"
        )
        assert replay == ref
        assert usage.counts() == before

        # L2 is reference-oriented: it does not copy actor/purpose/transaction internals.
        raw = usage.chronicle.records()[0]["payload"]
        raw_text = json.dumps(raw, sort_keys=True)
        for forbidden in ("actor_id", "declared_purpose", "estimated_cost", "servant_command_id", "txid"):
            assert forbidden not in raw_text
        assert "movement_digest" in raw_text
        assert "actual_cost" in raw_text

        # No telemetry capability => archive read remains denied and leaks no usage body.
        denied = usage.view_usage(
            "usage-1",
            TelemetryQuery("agent-A", "session-1", "T2_AUDIT_DURABLE", "wrong-purpose", "G-1"),
        )
        assert denied["status"] == "DENIED"
        assert "usage" not in denied and "session_id" not in denied

        # Exact T2 authorization exposes only the bounded archive usage view.
        allowed = usage.view_usage(
            "usage-1",
            TelemetryQuery("agent-A", "session-1", "T2_AUDIT_DURABLE", "audit", "G-1"),
        )
        assert allowed["status"] == "ALLOWED"
        assert allowed["usage"]["version_id"] == "version:M2:1"
        assert allowed["usage"]["movement_request_id"] == "transit-1"
        assert allowed["usage"]["actual_cost"]["compute"] == 1.0
        assert "actor_id" not in allowed["usage"] and "declared_purpose" not in allowed["usage"]

        # T3 authorization returns aggregate only; no session or movement identifiers.
        aggregate = usage.view_usage(
            "usage-1",
            TelemetryQuery("agent-A", "session-1", "T3_AGGREGATED", "audit", "G-1"),
        )
        assert aggregate == {
            "status": "ALLOWED",
            "class": "T3_AGGREGATED",
            "version_id": "version:M2:1",
            "usage_count": 1,
            "total_cost_l1": 1.0,
        }

        # A movement into M2 cannot be attached to a version whose object is M1.
        foreign = ArchiveManifest(
            version_id="version:M1:1",
            object_id="M1",
            parent_version_ids=(),
            base_snapshot_id="snapshot:M2:0",
            delta_ids=(),
            content_digest=map_workspace().state_digest,
            contract_id=map_workspace().contract_id,
            contract_digest=map_workspace().contract_digest,
            provenance_refs=("source:map-M1",),
            epistemic_status_ref="VALID",
            access_policy_ref="policy:G-1",
            lifecycle_state="ACTIVE",
            created_at="2026-09-30T17:10:03Z",
        )
        archive.publish_version(foreign)
        try:
            usage.link_movement("usage-wrong-map", "version:M1:1", "transit-1", created_at="2026-09-30T17:10:04Z")
            raise AssertionError("cross-map usage linkage was accepted")
        except UsageArchiveError as exc:
            assert "version/map mismatch" in str(exc)

        try:
            usage.link_movement("usage-missing", "version:M2:1", "movement-not-there", created_at="2026-09-30T17:10:05Z")
            raise AssertionError("missing movement was accepted")
        except UsageArchiveError as exc:
            assert "resolve exactly once" in str(exc)

        # Process-style restart recovers presence, map version and L2 binding.
        durable2 = DurableSharedMemoryRuntime(seed, root / "shared.wal", no_views)
        servant2 = ServantRuntime(
            durable2,
            root / "servant.wal",
            authorized_runbooks=("CURATOR-ARCHIVE-01",),
        )
        steward2 = AccessStewardRuntime(
            servant2,
            root / "access.wal",
            presence_anchor=ROOT,
            policy_lookup=store.lookup,
            current_policy_version=store.current_version,
            map_state_lookup=maps.get,
            cost_meter=lambda req: req.estimated_cost,
        )
        archive2 = MemoryArchiveRuntime(servant2, root / "archive.wal")
        usage2 = MemoryArchiveUsageRuntime(archive2, steward2, root / "archive-usage.wal")
        assert steward2.location("session-1") == "M2"
        recovered = usage2.usage("usage-1")
        assert recovered.version_id == "version:M2:1"
        assert recovered.actual_cost.l1 == 1.0
        allowed2 = usage2.view_usage(
            "usage-1",
            TelemetryQuery("agent-A", "session-1", "T2_AUDIT_DURABLE", "audit", "G-1"),
        )
        assert allowed2["status"] == "ALLOWED"

        # L2 writes cannot bypass the Curator archive runbook gate.
        blocked_servant = ServantRuntime(durable2, root / "servant-blocked.wal", authorized_runbooks=())
        blocked_archive = MemoryArchiveRuntime(blocked_servant, root / "archive.wal")
        blocked_usage = MemoryArchiveUsageRuntime(blocked_archive, steward2, root / "archive-usage-blocked.wal")
        try:
            blocked_usage.link_movement(
                "usage-blocked", "version:M2:1", "transit-1", created_at="2026-09-30T17:10:06Z"
            )
            raise AssertionError("L2 usage write bypassed SERVANT runbook gate")
        except UsageArchiveError as exc:
            assert "SERVANT gate rejected" in str(exc)
        assert blocked_usage.counts() == {"usage_refs": 0, "records": 0}

    print("PSI-MEMORY-ARCHIVE-F3.2-01 PASS_WITH_BOUNDARY")
    print("version_movement_cost_binding=PASS")
    print("restricted_telemetry_reference_not_copy=PASS")
    print("view_telemetry_gate_reused=PASS")
    print("unauthorized_archive_read_leak=ABSENT")
    print("t3_aggregate_no_session_identity=PASS")
    print("restart_recovers_usage_binding=PASS")
    print("cross_map_binding=BLOCKED")
    print("servant_runbook_gate=PASS")
    print("semantic_truth_authority=ABSENT")
    print("BOUNDARY: single-process L2 reference bridge; movement telemetry remains authoritative in ACCESS_STEWARD; no distributed telemetry store, retention policy engine, or autonomous Curator planning runtime")


if __name__ == "__main__":
    main()
