#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROLES = ROOT / "docs/memory/psi-memory-institution-roles-01.tsv"
ARCHIVE = ROOT / "docs/memory/psi-memory-archive-contract-01.tsv"
CONFLICTS = ROOT / "docs/memory/psi-memory-archive-conflicts-01.tsv"
DOC = ROOT / "docs/memory/PSI-MEMORY-ARCHIVE-F3.0-01.md"
CURATOR_PLAN = ROOT / "docs/memory/PSI-MEMORY-CURATOR-PLANNING-01.md"
ACCESS_STEWARD = ROOT / "docs/memory/psi-memory-access-steward-contract-01.tsv"


def rows(path: Path):
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def values(data, field: str) -> set[str]:
    return {row["value"] for row in data if row["field"] == field}


def main() -> None:
    roles = {r["role"] for r in rows(ROLES)}
    assert roles == {"GUARDIAN", "SERVANT", "IMMUNE", "CURATOR"}, roles

    access = rows(ACCESS_STEWARD)
    assert values(access, "constitutional_status") == {"SUBORDINATE_EXECUTOR"}
    assert values(access, "parent_authority") == {"GUARDIAN"}

    contract = rows(ARCHIVE)
    assert values(contract, "archive_level") == {"L0", "L1", "L2"}
    assert values(contract, "reconstruction_component") == {
        "BASE_SNAPSHOT", "ORDERED_DELTAS", "CONTENT_DIGEST"
    }
    assert values(contract, "version_identity") == {
        "STABLE_VERSION_ID", "EXPLICIT_PARENTS"
    }
    assert values(contract, "manifest_ref") == {
        "CONTRACT_REF",
        "PROVENANCE_REF",
        "ACCESS_POLICY_REF",
        "EPISTEMIC_STATUS_REF",
        "LIFECYCLE_STATE",
    }
    assert values(contract, "current_pointer") == {
        "AUDITABLE_REVERSIBLE", "NOT_TRUTH", "NOT_REUSE_RIGHT"
    }
    assert {
        "NO_STATUS_PROMOTION",
        "RESTORE_NOT_ADMISSION",
        "NO_ACCESS_EXPANSION",
        "NO_HISTORY_DELETE",
    } <= values(contract, "archive_semantics")
    assert values(contract, "telemetry") == {
        "REFERENCE_TYPED", "RESTRICTED_VISIBILITY_PRESERVED"
    }
    assert values(contract, "recursion") == {
        "REFERENCE_NOT_FULL_COPY", "FINITE_MATERIALIZATION_SCOPE"
    }
    authority = values(contract, "role_authority")
    for required in (
        "CURATOR_LINEAGE",
        "CURATOR_CURRENT_POINTER",
        "ACCESS_STEWARD_MOVEMENT",
        "SERVANT_DURABLE_MUTATION",
        "GUARDIAN_ACTIVE_BOUNDARY",
        "PSI_GATE_REPRESENTATION",
    ):
        assert required in authority, required

    curator_limits = values(contract, "curator_limit")
    assert curator_limits == {
        "NO_SELF_EXECUTE_RESTRUCTURE", "NO_SELF_ALLOCATE_RESOURCES"
    }

    costs = values(contract, "cost_metric")
    assert {
        "STORAGE_BYTES",
        "SNAPSHOT_BYTES",
        "DELTA_BYTES",
        "RECONSTRUCTION_STEPS",
        "RECONSTRUCTION_IO",
        "TRANSITION_COST",
    } <= costs

    fail_closed = values(contract, "fail_closed")
    assert {
        "MISSING_BASE_SNAPSHOT",
        "MISSING_DELTA",
        "DIGEST_MISMATCH",
        "VERSION_ID_COLLISION",
        "BROKEN_PARENT_REF",
        "BROKEN_POLICY_REF",
        "INVALID_CURRENT_POINTER",
        "RESTORE_BOUNDARY_BYPASS",
    } <= fail_closed

    conflicts = rows(CONFLICTS)
    cases = {r["case"] for r in conflicts}
    required_cases = {
        "missing_base_snapshot",
        "missing_delta_in_chain",
        "digest_mismatch_after_reconstruction",
        "version_id_collision",
        "newer_version_without_lineage",
        "current_pointer_to_unknown_version",
        "current_pointer_taken_as_truth",
        "current_pointer_taken_as_reuse_right",
        "archive_of_needs_recheck_result",
        "restore_archived_object_to_active",
        "archive_policy_reference_missing",
        "restricted_telemetry_link_in_l2",
        "curator_proposes_compaction",
        "curator_proposes_migration",
        "curator_requests_more_capacity",
        "archive_recursion_explosion",
        "archive_delete_old_versions",
        "restore_changes_epistemic_status",
        "semantic_restructure_drops_distinction",
        "movement_history_used_as_truth",
    }
    assert required_cases <= cases, required_cases - cases

    invariants = {r["invariant"] for r in conflicts}
    for invariant in (
        "stable_version_identity",
        "current_is_not_truth",
        "current_is_not_reuse_right",
        "archive_preserves_epistemic_status",
        "restore_crosses_active_boundary",
        "l2_is_not_telemetry_bypass",
        "reference_not_recursive_full_copy",
        "compression_must_respect_task_equivalence",
    ):
        assert invariant in invariants, invariant

    doc = DOC.read_text(encoding="utf-8")
    for needle in (
        "L0 — zasób źródłowy",
        "L1 — wersjonowane mapy i workspace'y",
        "L2 — pamięć użycia pamięci",
        "R(S_k,\\Delta_{k+1:n})=S_n",
        "CURRENT\\neq TRUE\\neq REUSABLE",
        "RESTORE(x)\\not\\Rightarrow ADMIT(x)",
        "reference}+\\text{digest}+\\text{typed relation",
        "F3.1",
    ):
        assert needle in doc, needle

    curator = CURATOR_PLAN.read_text(encoding="utf-8")
    assert "Kustosz może projektować potrzebę, ale nie ma kluczy do buldożera" in curator
    assert "EXPAND(district, requested_capacity)" in curator

    print("PSI-MEMORY-ARCHIVE-F3.0 CONTRACT_PASS")
    print("l0_l1_l2_separated=PASS")
    print("snapshot_delta_digest_reconstruction=PASS")
    print("stable_version_identity_and_explicit_parents=PASS")
    print("current_pointer_not_truth_or_reuse=PASS")
    print("archive_restore_do_not_promote_status=PASS")
    print("archive_does_not_expand_access=PASS")
    print("restricted_telemetry_not_bypassed_by_l2=PASS")
    print("servant_mvcc_wal_remain_durable_path=PASS")
    print("curator_plans_but_does_not_self_execute=PASS")
    print("reference_based_recursion=PASS")
    print("conflict_registry=PASS")
    print("BOUNDARY: contract only; no archive runtime, snapshot scheduler, compactor, garbage collector, or F3.1 reconstruction engine yet")


if __name__ == "__main__":
    main()
