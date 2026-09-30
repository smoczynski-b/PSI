#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from active_memory import MemoryEvent, apply_delta, compile_workspace
from durable_shared_memory import DurableSharedMemoryRuntime
from memory_archive_runtime import (
    ArchiveCorruption,
    ArchiveError,
    ArchiveManifest,
    MemoryArchiveRuntime,
)
from servant_runtime import ServantRuntime

CONTRACT = {
    "status": "COMPILED",
    "contract_id": "PSI-MEMORY-ARCHIVE-F3.1-TEST",
    "anchor": "ROOT",
    "task": "test versioned archive reconstruction",
}

RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "ROOT",
    "edges": [
        {"from": "ROOT", "relation": "BASE", "to": "A", "source": "seed:A", "status": "ADMITTED"},
    ],
}


def seed():
    return compile_workspace(CONTRACT, RETRIEVAL)


def no_views(shared):
    return None


def make_stack(root: Path, *, authorize: bool = True):
    durable = DurableSharedMemoryRuntime(seed(), root / "memory.wal", no_views)
    servant = ServantRuntime(
        durable,
        root / "servant.wal",
        authorized_runbooks=(("CURATOR-ARCHIVE-01",) if authorize else ()),
    )
    archive = MemoryArchiveRuntime(
        servant,
        root / "archive.wal",
        runbook_id="CURATOR-ARCHIVE-01",
    )
    return durable, servant, archive


def event_supports() -> MemoryEvent:
    return MemoryEvent(
        event_id="archive-delta-event-1",
        kind="EDGE_UPSERT",
        event_time="2026-09-30T16:56:00Z",
        ingest_time="2026-09-30T16:56:00.001000Z",
        payload={
            "from": "A",
            "relation": "SUPPORTS",
            "to": "P",
            "source": "source:proof-P",
            "status": "ADMITTED",
        },
    )


def manifest(
    *,
    version_id: str,
    content_digest: str,
    parents=(),
    deltas=(),
    status="VALID",
    access="policy:guardian:v1",
    lifecycle="ACTIVE",
):
    base = seed()
    return ArchiveManifest(
        version_id=version_id,
        object_id="map:alpha",
        parent_version_ids=tuple(parents),
        base_snapshot_id="snapshot:alpha:0",
        delta_ids=tuple(deltas),
        content_digest=content_digest,
        contract_id=base.contract_id,
        contract_digest=base.contract_digest,
        provenance_refs=("source:seed-A", "contract:archive-test"),
        epistemic_status_ref=status,
        access_policy_ref=access,
        lifecycle_state=lifecycle,
        created_at="2026-09-30T16:56:01Z",
    )


def main():
    with TemporaryDirectory() as td:
        root = Path(td)
        durable, servant, archive = make_stack(root)
        base = seed()
        event = event_supports()
        target = apply_delta(base, (event,)).workspace

        # One base snapshot and one ordered delta can support multiple versions.
        archive.store_snapshot("snapshot:alpha:0", base)
        archive.store_delta("delta:alpha:1", event)

        v1 = manifest(version_id="version:alpha:1", content_digest=base.state_digest)
        v2 = manifest(
            version_id="version:alpha:2",
            content_digest=target.state_digest,
            parents=("version:alpha:1",),
            deltas=("delta:alpha:1",),
            status="NEEDS_RECHECK",
        )
        archive.publish_version(v1)
        archive.publish_version(v2)

        # CURRENT is lifecycle routing only: it may point at NEEDS_RECHECK.
        archive.publish_current("map:alpha", "version:alpha:1")
        archive.publish_current("map:alpha", "version:alpha:2")
        assert archive.current("map:alpha") == "version:alpha:2"
        assert archive.manifest("version:alpha:2").epistemic_status_ref == "NEEDS_RECHECK"

        restored = archive.reconstruct("version:alpha:2")
        assert restored.reconstruction_steps == 1
        assert restored.workspace.state_digest == target.state_digest
        assert ("A", "SUPPORTS", "P") in restored.workspace.edges
        assert restored.manifest.epistemic_status_ref == "NEEDS_RECHECK"

        # Candidate restore is read-only: no admission/status/pointer side effect.
        records_before_candidate = archive.counts()["records"]
        candidate = archive.restore_candidate("version:alpha:1")
        assert candidate.workspace.state_digest == base.state_digest
        assert archive.current("map:alpha") == "version:alpha:2"
        assert archive.counts()["records"] == records_before_candidate

        # Repeating identical materialization is idempotent and does not copy
        # another snapshot/version record.
        counts_before_replay = archive.counts()
        archive.store_snapshot("snapshot:alpha:0", base)
        archive.store_delta("delta:alpha:1", event)
        archive.publish_version(v1)
        archive.publish_version(v2)
        archive.publish_current("map:alpha", "version:alpha:2")
        assert archive.counts() == counts_before_replay
        assert archive.counts()["snapshots"] == 1
        assert archive.counts()["deltas"] == 1
        assert archive.counts()["versions"] == 2

        # Missing delta fails closed before manifest publication.
        missing = manifest(
            version_id="version:alpha:missing-delta",
            content_digest=target.state_digest,
            parents=("version:alpha:2",),
            deltas=("delta:not-there",),
        )
        try:
            archive.publish_version(missing)
            raise AssertionError("missing delta was accepted")
        except ArchiveError as exc:
            assert "missing delta" in str(exc)

        # Digest mismatch fails closed.
        bad_digest = manifest(
            version_id="version:alpha:bad-digest",
            content_digest="0" * 64,
            parents=("version:alpha:2",),
            deltas=("delta:alpha:1",),
        )
        try:
            archive.publish_version(bad_digest)
            raise AssertionError("digest mismatch was accepted")
        except ArchiveError as exc:
            assert "content digest mismatch" in str(exc)

        # Stable version identity: the same version_id cannot name new content
        # or metadata.
        collision = manifest(
            version_id="version:alpha:2",
            content_digest=target.state_digest,
            parents=("version:alpha:1",),
            deltas=("delta:alpha:1",),
            status="VALID",
        )
        try:
            archive.publish_version(collision)
            raise AssertionError("version id collision was accepted")
        except ArchiveError as exc:
            assert "version id collision" in str(exc)

        # CURRENT cannot target an unknown or foreign-object version.
        try:
            archive.publish_current("map:alpha", "version:not-there")
            raise AssertionError("unknown CURRENT target was accepted")
        except ArchiveError as exc:
            assert "unknown version" in str(exc)
        try:
            archive.publish_current("map:other", "version:alpha:2")
            raise AssertionError("cross-object CURRENT pointer was accepted")
        except ArchiveError as exc:
            assert "object/version mismatch" in str(exc)

        # Every persistent archive record was preceded by a SERVANT institution
        # gate; the authoritative semantic memory itself was not silently edited.
        assert durable.revision == 0
        archive_records = archive.counts()["records"]
        servant_results = [
            r for r in servant.chronicle.records()
            if r.get("kind") == "SERVANT_RESULT"
            and str(r.get("payload", {}).get("reason_code", "")).startswith("INSTITUTION_ACTION_ACCEPTED:NOTICE")
        ]
        assert len(servant_results) == archive_records

        # Process-style restart recovers manifests, pointer and NEEDS_RECHECK.
        durable2 = DurableSharedMemoryRuntime(seed(), root / "memory.wal", no_views)
        servant2 = ServantRuntime(
            durable2,
            root / "servant.wal",
            authorized_runbooks=("CURATOR-ARCHIVE-01",),
        )
        archive2 = MemoryArchiveRuntime(servant2, root / "archive.wal")
        assert archive2.current("map:alpha") == "version:alpha:2"
        assert archive2.manifest("version:alpha:2").epistemic_status_ref == "NEEDS_RECHECK"
        restored2 = archive2.reconstruct("version:alpha:2")
        assert restored2.workspace.state_digest == target.state_digest
        assert archive2.counts()["snapshots"] == 1
        assert archive2.counts()["versions"] == 2

        # Semantic corruption in an otherwise hash-valid archive fails closed on
        # restart: inject a manifest with a missing delta directly as a fault.
        corrupt_manifest = manifest(
            version_id="version:alpha:corrupt",
            content_digest=target.state_digest,
            parents=("version:alpha:2",),
            deltas=("delta:missing-after-crash",),
        )
        archive2.chronicle.wal.append(
            "ARCHIVE_VERSION",
            "version:alpha:corrupt",
            {"manifest": corrupt_manifest.as_dict(), "manifest_digest": "fault-injection"},
        )
        try:
            MemoryArchiveRuntime(servant2, root / "archive.wal")
            raise AssertionError("semantically corrupt archive was accepted")
        except ArchiveCorruption as exc:
            assert "missing delta" in str(exc)

    # No authorized Curator archive runbook => no persistent archive mutation.
    with TemporaryDirectory() as td:
        root = Path(td)
        _, _, blocked_archive = make_stack(root, authorize=False)
        try:
            blocked_archive.store_snapshot("snapshot:blocked", seed())
            raise AssertionError("archive write bypassed SERVANT runbook gate")
        except ArchiveError as exc:
            assert "SERVANT gate rejected" in str(exc)
        assert blocked_archive.counts()["records"] == 0

    print("PSI-MEMORY-ARCHIVE-F3.1-01 PASS_WITH_BOUNDARY")
    print("snapshot_delta_reconstruction=PASS")
    print("content_digest_verification=PASS")
    print("stable_version_identity=PASS")
    print("current_pointer_durable_and_auditable=PASS")
    print("current_not_truth_or_reuse_authority=PASS")
    print("needs_recheck_preserved_across_restart=PASS")
    print("candidate_restore_is_read_only=PASS")
    print("missing_delta_fail_closed=PASS")
    print("semantic_archive_corruption_fail_closed=PASS")
    print("servant_runbook_gate_before_persistent_archive_write=PASS")
    print("no_full_snapshot_copy_per_version=PASS")
    print("BOUNDARY: single-process reference archive; existing SERVANT NOTICE action is used as procedural gate, not an archive-specific authority; no live Guardian restore admission, restricted telemetry materialization, distributed object store, compaction policy, or Curator planning runtime")


if __name__ == "__main__":
    main()
