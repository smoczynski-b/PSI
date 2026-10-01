#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

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
)
from durable_shared_memory import DurableSharedMemoryRuntime
from memory_archive_runtime import ArchiveManifest, MemoryArchiveRuntime
from memory_archive_usage_runtime import (
    EVIDENCE_MAP_ASSOCIATION,
    EVIDENCE_VERIFIED_CONSUMPTION,
    MemoryArchiveUsageRuntime,
    UsageArchiveError,
)
from servant_runtime import ServantRuntime

ROOT = "ACCESS_PRESENCE_ROOT"


def cv(value: float) -> CostVector:
    return CostVector(compute=value)


def manifest(version_id: str, snapshot_id: str, ws: Workspace, parents=()) -> ArchiveManifest:
    return ArchiveManifest(
        version_id=version_id,
        object_id="M2",
        parent_version_ids=tuple(parents),
        base_snapshot_id=snapshot_id,
        delta_ids=(),
        content_digest=ws.state_digest,
        contract_id=ws.contract_id,
        contract_digest=ws.contract_digest,
        provenance_refs=(f"source:{version_id}",),
        epistemic_status_ref="VALID",
        access_policy_ref="policy:G-R7",
        lifecycle_state="ACTIVE",
        created_at="2026-09-30T20:59:00Z",
    )


def make_policy() -> GuardianAccessPolicy:
    return GuardianAccessPolicy("G-R7", (
        PolicyRule("agent-A", "session-1", "ENTER", OUTSIDE, "M2", "solve", CAP_ENTER),
        PolicyRule(
            "agent-A", "session-1", "VIEW_TELEMETRY", "M2", "M2", "audit",
            CAP_TELEMETRY, ("T2_AUDIT_DURABLE",),
        ),
    ))


def main() -> None:
    with TemporaryDirectory() as td:
        root = Path(td)
        seed = Workspace("ACCESS-PRESENCE-01", "presence-v1", ROOT)
        policy = make_policy()

        def durable_runtime():
            return DurableSharedMemoryRuntime(seed, root / "shared.wal", lambda shared: None)

        def steward_runtime(servant: ServantRuntime):
            return AccessStewardRuntime(
                servant,
                root / "access.wal",
                presence_anchor=ROOT,
                policy_lookup=lambda version: policy if version == policy.version else None,
                current_policy_version=lambda: policy.version,
                map_state_lookup=lambda map_id: MapState("M2") if map_id == "M2" else None,
                cost_meter=lambda request: request.estimated_cost,
            )

        durable = durable_runtime()
        servant = ServantRuntime(
            durable,
            root / "servant.wal",
            authorized_runbooks=("CURATOR-ARCHIVE-01",),
        )
        steward = steward_runtime(servant)
        archive = MemoryArchiveRuntime(servant, root / "archive.wal")

        v1_ws = Workspace("MAP-M2-CONTRACT", "map-m2-v1", "M2")
        v2_ws = Workspace(
            "MAP-M2-CONTRACT", "map-m2-v1", "M2",
            node_status={"fact:new": "VALID"}, revision=1,
        )
        archive.store_snapshot("snapshot:M2:1", v1_ws)
        archive.publish_version(manifest("version:M2:1", "snapshot:M2:1", v1_ws))
        archive.store_snapshot("snapshot:M2:2", v2_ws)
        archive.publish_version(manifest("version:M2:2", "snapshot:M2:2", v2_ws, ("version:M2:1",)))
        archive.publish_current("M2", "version:M2:2")

        move = MovementRequest(
            request_id="enter-M2",
            session_id="session-1",
            actor_id="agent-A",
            operation="ENTER",
            map_from=OUTSIDE,
            map_to="M2",
            declared_purpose="solve",
            requested_capability=CAP_ENTER,
            policy_version=policy.version,
            budget=cv(10),
            estimated_cost=cv(1),
            event_time="2026-09-30T20:59:01Z",
        )
        assert steward.handle(move).disposition == "ALLOW_MOVEMENT"
        usage = MemoryArchiveUsageRuntime(archive, steward, root / "usage.wal")

        assert v1_ws.state_digest != v2_ws.state_digest

        # An association may name another version of the same map, but it must
        # remain explicitly weaker than a consumption claim.
        association = usage.link_movement(
            "association-v2",
            "version:M2:2",
            "enter-M2",
            created_at="2026-09-30T20:59:02Z",
        )
        assert association.evidence_kind == EVIDENCE_MAP_ASSOCIATION
        assert association.consumption_receipt_id == ""
        assert association.content_digest == ""
        assert association.source_revision is None

        # The exact read path returns v1 and durably records the consumed
        # version/revision/digest rather than inferring them from map identity.
        consumed = usage.consume_version(
            "receipt-v1",
            "version:M2:1",
            "enter-M2",
            created_at="2026-09-30T20:59:03Z",
        )
        assert consumed.workspace.state_digest == v1_ws.state_digest
        assert consumed.workspace.revision == v1_ws.revision
        assert consumed.receipt.version_id == "version:M2:1"
        assert consumed.receipt.content_digest == v1_ws.state_digest
        assert consumed.receipt.source_revision == v1_ws.revision

        verified = usage.link_movement(
            "usage-v1",
            "version:M2:1",
            "enter-M2",
            created_at="2026-09-30T20:59:04Z",
            consumption_receipt_id="receipt-v1",
        )
        assert verified.evidence_kind == EVIDENCE_VERIFIED_CONSUMPTION
        assert verified.content_digest == v1_ws.state_digest
        assert verified.source_revision == v1_ws.revision

        # The receipt cannot be reassigned to the unconsumed v2 even though both
        # versions name M2.
        try:
            usage.link_movement(
                "usage-wrong-version",
                "version:M2:2",
                "enter-M2",
                created_at="2026-09-30T20:59:05Z",
                consumption_receipt_id="receipt-v1",
            )
        except UsageArchiveError as exc:
            assert "receipt/version mismatch" in str(exc)
        else:
            raise AssertionError("consumption receipt was reassigned to an unconsumed version")

        # Telemetry access remains a separate Guardian-controlled gate.
        denied = usage.view_usage(
            "usage-v1",
            TelemetryQuery("agent-A", "session-1", "T2_AUDIT_DURABLE", "wrong", policy.version),
        )
        assert denied["status"] == "DENIED"
        assert "usage" not in denied

        allowed = usage.view_usage(
            "usage-v1",
            TelemetryQuery("agent-A", "session-1", "T2_AUDIT_DURABLE", "audit", policy.version),
        )
        assert allowed["status"] == "ALLOWED"
        assert allowed["usage"]["evidence_kind"] == EVIDENCE_VERIFIED_CONSUMPTION
        assert allowed["usage"]["version_id"] == "version:M2:1"
        assert allowed["usage"]["content_digest"] == v1_ws.state_digest
        assert allowed["usage"]["source_revision"] == v1_ws.revision

        # Process-style restart must preserve both receipt and verified binding.
        durable2 = durable_runtime()
        servant2 = ServantRuntime(
            durable2,
            root / "servant.wal",
            authorized_runbooks=("CURATOR-ARCHIVE-01",),
        )
        steward2 = steward_runtime(servant2)
        archive2 = MemoryArchiveRuntime(servant2, root / "archive.wal")
        usage2 = MemoryArchiveUsageRuntime(archive2, steward2, root / "usage.wal")
        assert steward2.location("session-1") == "M2"
        receipt2 = usage2.consumption_receipt("receipt-v1")
        assert receipt2.version_id == "version:M2:1"
        assert receipt2.content_digest == v1_ws.state_digest
        verified2 = usage2.usage("usage-v1")
        assert verified2.evidence_kind == EVIDENCE_VERIFIED_CONSUMPTION
        assert verified2.consumption_receipt_id == "receipt-v1"
        denied2 = usage2.view_usage(
            "usage-v1",
            TelemetryQuery("agent-A", "session-1", "T2_AUDIT_DURABLE", "wrong", policy.version),
        )
        assert denied2["status"] == "DENIED"
        allowed2 = usage2.view_usage(
            "usage-v1",
            TelemetryQuery("agent-A", "session-1", "T2_AUDIT_DURABLE", "audit", policy.version),
        )
        assert allowed2["status"] == "ALLOWED"
        assert allowed2["usage"]["version_id"] == "version:M2:1"

    print("PSI-MEMORY-R7-CONSUMED-VERSION PASS_WITH_BOUNDARY")
    print("map_association_distinguished=PASS")
    print("verified_consumption_receipt=PASS")
    print("wrong_same_map_version_rejected=PASS")
    print("restart_preserves_receipt_binding=PASS")
    print("telemetry_gate_preserved=PASS")
    print("BOUNDARY: receipt proves exact archive payload returned by the typed read path; it does not prove semantic understanding or downstream model use")


if __name__ == "__main__":
    main()
