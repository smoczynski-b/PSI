#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROLE_REGISTRY = ROOT / "docs/memory/psi-memory-institution-roles-01.tsv"
CONTRACT = ROOT / "docs/memory/psi-memory-access-steward-contract-01.tsv"
CONFLICTS = ROOT / "docs/memory/psi-memory-access-steward-conflicts-01.tsv"
DOC = ROOT / "docs/memory/PSI-MEMORY-ACCESS-STEWARD-01.md"


def rows(path: Path):
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def contract_values(contract_rows, field: str) -> set[str]:
    return {r["value"] for r in contract_rows if r["field"] == field}


def main() -> None:
    role_rows = rows(ROLE_REGISTRY)
    role_names = {r["role"] for r in role_rows}
    assert role_names == {"GUARDIAN", "SERVANT", "IMMUNE", "CURATOR"}, role_names
    assert "ACCESS_STEWARD" not in role_names

    contract = rows(CONTRACT)
    assert contract_values(contract, "constitutional_status") == {"SUBORDINATE_EXECUTOR"}
    assert contract_values(contract, "parent_authority") == {"GUARDIAN"}
    assert contract_values(contract, "policy_owner") == {"GUARDIAN"}
    assert contract_values(contract, "executor") == {"ACCESS_STEWARD"}
    assert contract_values(contract, "presence_key") == {"SESSION_ID"}
    assert contract_values(contract, "single_session_location") == {"AT_MOST_ONE_MAP"}

    capabilities = contract_values(contract, "capability")
    required_caps = {
        "ENTER_MAP",
        "TRANSIT_TO_MAP",
        "ACT_IN_MAP",
        "EXPORT_FROM_MAP",
        "VIEW_TELEMETRY",
    }
    assert capabilities == required_caps, capabilities

    legal_conditions = contract_values(contract, "legal_condition")
    assert legal_conditions == {
        "POLICY", "PURPOSE", "CAPABILITY", "SOURCE_LOCATION", "TARGET_STATE", "BUDGET"
    }, legal_conditions

    cost_components = contract_values(contract, "cost_component")
    assert cost_components == {
        "COMPUTE", "TRANSFER", "CONTEXT", "LATENCY", "DISCLOSURE", "SYNCHRONIZATION", "RISK"
    }
    assert contract_values(contract, "cross_map_cost") == {"POSITIVE_L1"}

    telemetry = contract_values(contract, "telemetry_class")
    assert telemetry == {
        "T0_SESSION_LOCAL", "T1_SECURITY_RESTRICTED", "T2_AUDIT_DURABLE", "T3_AGGREGATED"
    }

    forbidden = contract_values(contract, "must_not")
    required_forbidden = {
        "MINT_POLICY",
        "MODIFY_POLICY",
        "SELF_AUTHORIZE",
        "DECLARE_DOMAIN_TRUTH",
        "EDIT_MAP_SEMANTIC_CONTENT",
        "BYPASS_SERVANT_DURABLE_MUTATION",
        "CLEAR_IMMUNE_QUARANTINE",
        "REWRITE_MOVEMENT_HISTORY",
        "DISCLOSE_RESTRICTED_TELEMETRY_WITHOUT_CAPABILITY",
        "INFER_ACT_FROM_ENTER",
        "INFER_EXPORT_FROM_TRANSIT",
        "INFER_AUTHORIZATION_FROM_REACHABILITY",
        "APPROVE_CURATOR_RESTRUCTURE",
    }
    assert required_forbidden <= forbidden, required_forbidden - forbidden

    conflict_rows = rows(CONFLICTS)
    cases = {r["case"] for r in conflict_rows}
    required_cases = {
        "guardian_policy_absent",
        "physically_reachable_but_not_authorized",
        "enter_without_act",
        "enter_without_telemetry_view",
        "move_without_export",
        "insufficient_budget",
        "unknown_target_map",
        "session_location_mismatch",
        "same_session_simultaneous_maps",
        "policy_version_changed",
        "curator_migration_proposal",
        "repeated_legal_but_pathological_movement",
        "semantic_truth_dispute",
        "telemetry_requested_without_capability",
        "transition_record_after_restart",
        "cross_map_zero_cost",
        "persistent_movement_write_without_servant",
    }
    assert required_cases <= cases, required_cases - cases

    invariants = {r["invariant"] for r in conflict_rows}
    assert "enter_does_not_imply_action" in invariants
    assert "enter_does_not_imply_telemetry" in invariants
    assert "movement_does_not_imply_export" in invariants
    assert "cross_map_transition_has_cost" in invariants
    assert "no_silent_policy_reinterpretation" in invariants

    doc = DOC.read_text(encoding="utf-8")
    for needle in (
        "GUARDIAN \\triangleright ACCESS\\_STEWARD",
        "policy\\_owner=GUARDIAN",
        "MOVE(agent,M_i\\to M_j)\\neq EXPORT(data,M_i\\to M_j)",
        "M_i\\neq M_j\\Rightarrow \\|\\kappa(\\tau)\\|_1>0",
    ):
        assert needle in doc, needle

    print("PSI-MEMORY-ACCESS-STEWARD-F2.0 CONTRACT_PASS")
    print("constitutional_roles_remain_four=PASS")
    print("access_steward_subordinate_to_guardian=PASS")
    print("guardian_policy_owner_steward_executor=PASS")
    print("enter_act_export_telemetry_separated=PASS")
    print("cross_map_positive_cost=PASS")
    print("telemetry_visibility_classes=PASS")
    print("no_self_authorization_or_truth_authority=PASS")
    print("conflict_registry=PASS")
    print("BOUNDARY: contract only; no ACCESS_STEWARD runtime, durable presence log, movement execution, or Guardian runtime yet")


if __name__ == "__main__":
    main()
