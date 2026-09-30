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
    CAP_ENTER,
)
from durable_shared_memory import DurableSharedMemoryRuntime
from memory_archive_runtime import ArchiveManifest, MemoryArchiveRuntime
from memory_archive_usage_runtime import MemoryArchiveUsageRuntime, UsageArchiveError
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


def main() -> None:
    with TemporaryDirectory() as td:
        root = Path(td)
        seed = Workspace("ACCESS-PRESENCE-01", "presence-v1", ROOT)
        durable = DurableSharedMemoryRuntime(seed, root / "shared.wal", lambda shared: None)
        servant = ServantRuntime(
            durable,
            root / "servant.wal",
            authorized_runbooks=("CURATOR-ARCHIVE-01",),
        )
        policy = GuardianAccessPolicy("G-R7", (
            PolicyRule("agent-A", "session-1", "ENTER", OUTSIDE, "M2", "solve", CAP_ENTER),
        ))
        steward = AccessStewardRuntime(
            servant,
            root / "access.wal",
            presence_anchor=ROOT,
            policy_lookup=lambda version: policy if version == policy.version else None,
            current_policy_version=lambda: policy.version,
            map_state_lookup=lambda map_id: MapState("M2") if map_id == "M2" else None,
            cost_meter=lambda request: request.estimated_cost,
        )
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

        # The consumer actually reconstructs v1. The old F3.2 bridge does not
        # record that read, so it can still attribute the same movement to v2.
        consumed = archive.reconstruct("version:M2:1")
        assert consumed.workspace.state_digest == v1_ws.state_digest
        assert v1_ws.state_digest != v2_ws.state_digest

        try:
            usage.link_movement(
                "usage-wrong-version",
                "version:M2:2",
                "enter-M2",
                created_at="2026-09-30T20:59:02Z",
            )
        except UsageArchiveError:
            pass
        else:
            raise AssertionError(
                "unconsumed archive version was accepted as usage merely because it names the same map"
            )

    print("PSI-MEMORY-R7-CONSUMED-VERSION separating witness PASS")


if __name__ == "__main__":
    main()
