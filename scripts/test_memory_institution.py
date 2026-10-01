#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROLES = ROOT / "docs/memory/psi-memory-institution-roles-01.tsv"
AUTHORITIES = ROOT / "docs/memory/psi-memory-institution-authorities-01.tsv"
CONFLICTS = ROOT / "docs/memory/psi-memory-institution-conflicts-01.tsv"

EXPECTED_ROLES = {"GUARDIAN", "SERVANT", "IMMUNE", "CURATOR"}
FORBIDDEN_EPISTEMIC = "DECLARE_DOMAIN_TRUTH"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> None:
    roles = read_tsv(ROLES)
    authorities = read_tsv(AUTHORITIES)
    conflicts = read_tsv(CONFLICTS)

    role_ids = [r["role"] for r in roles]
    assert set(role_ids) == EXPECTED_ROLES
    assert len(role_ids) == len(set(role_ids)) == 4

    by_role = {r["role"]: r for r in roles}
    for role in EXPECTED_ROLES:
        forbidden = set(filter(None, by_role[role]["must_not"].split(";")))
        assert FORBIDDEN_EPISTEMIC in forbidden, f"{role} gained domain-truth authority"
        assert "CHANGE_CONSTITUTION" in forbidden, f"{role} may self-modify constitution"

    servant = by_role["SERVANT"]
    assert "PARTICIPATE_IN_FORUM_DEBATE" in servant["must_not"].split(";")
    assert "machine audit/status events only" == servant["output_surface"]

    authority_actions = [a["action"] for a in authorities]
    assert len(authority_actions) == len(set(authority_actions)), "authority actions must be unique"
    authority = {a["action"]: a for a in authorities}

    assert authority["ADMIT_NEW_OBJECT"]["authority"] == "GUARDIAN"
    assert authority["ACK_TRANSITION"]["authority"] == "SERVANT"
    assert authority["POST_QUARANTINE"]["authority"] == "IMMUNE"
    assert authority["ARCHIVE"]["authority"] == "CURATOR"
    assert authority["CHANGE_CONSTITUTION"]["authority"] == "NONE_RUNTIME"

    # Two-key actions remain multi-party; one institutional role cannot release
    # quarantine or promote a reusable map on its own.
    assert authority["RELEASE_POST_QUARANTINE"]["authority"] == "GUARDIAN+IMMUNE"
    assert authority["RELEASE_POST_QUARANTINE"]["forbidden_shortcut"] == "one_role_release"
    assert authority["PROMOTE_REUSABLE_MAP"]["authority"] == "GUARDIAN+CURATOR+PSI_GATE"
    assert "usage_count_or_reputation" == authority["PROMOTE_REUSABLE_MAP"]["forbidden_shortcut"]

    cases = {c["case"]: c for c in conflicts}
    required_cases = {
        "malformed_or_untyped_input",
        "explicitly_illegal_transition",
        "schema_valid_but_anomalous_after_admission",
        "quarantine_release",
        "supersession_of_quarantined_object",
        "rollback_after_durable_commit",
        "newer_version_without_supersedes_relation",
        "role_detects_own_constitution_problem",
        "semantic_truth_dispute",
        "forum_popularity_or_import_count",
    }
    assert required_cases <= set(cases)

    assert cases["malformed_or_untyped_input"]["invariant"] == "boundary_fault_is_not_pathology"
    assert cases["explicitly_illegal_transition"]["invariant"] == "known_illegality_is_not_anomaly_detection"
    assert cases["schema_valid_but_anomalous_after_admission"]["invariant"] == "admission_legality_is_not_health"
    assert cases["quarantine_release"]["invariant"] == "two_key_release"
    assert cases["rollback_after_durable_commit"]["invariant"] == "append_only_history"
    assert cases["role_detects_own_constitution_problem"]["invariant"] == "no_self_constitution"
    assert cases["semantic_truth_dispute"]["invariant"] == "procedure_is_not_truth"
    assert cases["forum_popularity_or_import_count"]["invariant"] == "frequency_is_not_epistemic_strength"

    # No role may be assigned permanent deletion of durable/provenance history.
    all_may = ";".join(r["may_act"] for r in roles)
    assert "PERMANENT_DELETE" not in all_may
    assert "DELETE_HISTORY" not in all_may

    print("PSI-MEMORY-INSTITUTION-01 CONTRACT_PASS")
    print("roles=4")
    print(f"authorities={len(authorities)} conflicts={len(conflicts)}")
    print("procedural_role_not_epistemic_authority=PASS")
    print("servant_typed_machine_surface_only=PASS")
    print("two_key_quarantine_release=PASS")
    print("constitution_self_modification=BLOCKED")
    print("durable_history_rewrite=BLOCKED")
    print("forum_popularity_not_epistemic_licence=PASS")


if __name__ == "__main__":
    main()
