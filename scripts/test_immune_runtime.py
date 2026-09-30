#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from active_memory import compile_workspace
from durable_shared_memory import DurableSharedMemoryRuntime
from immune_runtime import ImmuneObservation, ImmuneRuntime, ReactionBudget, load_signatures
from servant_runtime import ServantRuntime

ROOT = Path(__file__).resolve().parents[1]
SIGNATURES = ROOT / "docs/memory/psi-memory-immune-signatures-01.tsv"

BASE_CONTRACT = {
    "status": "COMPILED",
    "contract_id": "IMMUNE-01-AUTH",
    "anchor": "ROOT",
    "task": "test bounded immune response",
}
BASE_RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "ROOT",
    "edges": [
        {"from": "ROOT", "relation": "BASE", "to": "A", "source": "seed:A", "status": "ADMITTED"},
    ],
}


def workspace(contract_id: str, anchor: str, node: str):
    return compile_workspace(
        {"status": "COMPILED", "contract_id": contract_id, "anchor": anchor, "task": contract_id},
        {
            "status": "RETRIEVED",
            "anchor": anchor,
            "edges": [
                {"from": anchor, "relation": "BASE", "to": node, "source": f"seed:{node}", "status": "ADMITTED"}
            ],
        },
    )


def authoritative_seed():
    return compile_workspace(BASE_CONTRACT, BASE_RETRIEVAL)


def register_views(shared):
    shared.register("proof", workspace("VIEW-PROOF", "ROOT", "A"))
    shared.register("down1", workspace("VIEW-D1", "D1ROOT", "D1"), extra_dependencies=("workspace:proof",))
    shared.register("down2", workspace("VIEW-D2", "D2ROOT", "D2"), extra_dependencies=("workspace:down1",))
    shared.register("unrelated", workspace("VIEW-U", "UROOT", "U"))


def make_stack(td: str, *, budget: ReactionBudget):
    base = Path(td)
    durable = DurableSharedMemoryRuntime(
        authoritative_seed(),
        base / "memory.wal",
        register_views,
    )
    servant = ServantRuntime(
        durable,
        base / "servant.wal",
        authorized_runbooks=("IMMUNE-01",),
    )
    immune = ImmuneRuntime(
        durable.shared.views,
        servant,
        base / "immune.wal",
        load_signatures(SIGNATURES),
        budget=budget,
    )
    return durable, servant, immune


def obs(oid: str, signature_id: str, kind: str, subject: str, value, admission: str = "ADMITTED"):
    return ImmuneObservation(
        observation_id=oid,
        signature_id=signature_id,
        observation_kind=kind,
        subject_workspace=subject,
        admission_state=admission,
        value=value,
    )


def main():
    signatures = load_signatures(SIGNATURES)
    by_id = {s.signature_id: s for s in signatures}
    ids = set(by_id)
    assert {
        "IMM-CONFLICT-BURST",
        "IMM-INVALIDATION-FANOUT",
        "IMM-WAL-CORRUPTION",
        "IMM-CLEAR-RECOVERY",
    } <= ids
    assert by_id["IMM-CONFLICT-BURST"].value_domain == "NONNEGATIVE_INTEGER"
    assert by_id["IMM-INVALIDATION-FANOUT"].value_domain == "NONNEGATIVE_INTEGER"
    assert by_id["IMM-WAL-CORRUPTION"].value_domain == "BINARY_FLAG"
    assert by_id["IMM-CLEAR-RECOVERY"].value_domain == "BINARY_FLAG"

    # F0.2: raw observation boundary admits only finite real numbers and rejects
    # bool/text/NaN/infinities before signature evaluation or immune persistence.
    with TemporaryDirectory() as td:
        durable, servant, immune = make_stack(td, budget=ReactionBudget())
        records_before = len(immune.memory.records())
        bad_values = (float("nan"), float("inf"), float("-inf"), True, False, "3")
        for idx, bad in enumerate(bad_values):
            try:
                obs(
                    f"OBS-RAW-{idx}",
                    "IMM-CONFLICT-BURST",
                    "PROTOCOL_CONFLICT_COUNT",
                    "proof",
                    bad,
                )
                raise AssertionError(f"invalid raw immune value accepted: {bad!r}")
            except ValueError:
                pass
        assert len(immune.memory.records()) == records_before
        assert immune.health("proof") == "NORMAL"
        assert immune.signature_count("IMM-CONFLICT-BURST", "proof") == 0

    # F0.2: finite values still must belong to the signature-declared domain.
    # Domain failure is recorded but cannot trigger NOTICE/quarantine/counting.
    with TemporaryDirectory() as td:
        durable, servant, immune = make_stack(td, budget=ReactionBudget())
        invalid_cases = (
            ("OBS-DOM-NEG", "IMM-CONFLICT-BURST", "PROTOCOL_CONFLICT_COUNT", -1),
            ("OBS-DOM-FRAC", "IMM-CONFLICT-BURST", "PROTOCOL_CONFLICT_COUNT", 1.5),
            ("OBS-DOM-BINARY", "IMM-WAL-CORRUPTION", "WAL_CORRUPTION", 2),
        )
        for oid, sid, kind, value in invalid_cases:
            decision = immune.observe(obs(oid, sid, kind, "proof", value))
            assert decision.status == "INVALID_OBSERVATION_DOMAIN"
            assert decision.reason_code.startswith("VALUE_OUTSIDE_DOMAIN:")
            assert decision.actions == ()
            assert decision.requested_rechecks == ()
            assert decision.signature_count == 0
            assert immune.health("proof") == "NORMAL"
        assert immune.signature_count("IMM-CONFLICT-BURST", "proof") == 0
        assert immune.signature_count("IMM-WAL-CORRUPTION", "proof") == 0

    # F0.2: threshold semantics remain distinct from domain validity.
    with TemporaryDirectory() as td:
        durable, servant, immune = make_stack(td, budget=ReactionBudget())
        below = immune.observe(obs(
            "OBS-THRESH-BELOW", "IMM-CONFLICT-BURST", "PROTOCOL_CONFLICT_COUNT", "proof", 2
        ))
        assert below.status == "NO_ANOMALY"
        assert below.reason_code == "SIGNATURE_THRESHOLD_NOT_MET"
        assert below.actions == ()
        assert immune.signature_count("IMM-CONFLICT-BURST", "proof") == 0
        at = immune.observe(obs(
            "OBS-THRESH-AT", "IMM-CONFLICT-BURST", "PROTOCOL_CONFLICT_COUNT", "proof", 3.0
        ))
        assert at.status == "POST_QUARANTINED"
        assert at.reason_code == "LICENSED_SIGNATURE_MATCH"
        assert immune.signature_count("IMM-CONFLICT-BURST", "proof") == 1
        assert immune.health("proof") == "POST_QUARANTINED"

    # Licensed post-admission anomaly -> NOTICE + POST_QUARANTINE + bounded
    # REQUEST_RECHECK along declared dependencies. Requests do not directly
    # mutate epistemic status.
    with TemporaryDirectory() as td:
        durable, servant, immune = make_stack(td, budget=ReactionBudget(max_actions=8, max_rechecks=4))
        before = {wid: durable.shared.views.status(wid) for wid in ("proof", "down1", "down2", "unrelated")}
        decision = immune.observe(obs(
            "OBS-1", "IMM-INVALIDATION-FANOUT", "INVALIDATION_FANOUT", "proof", 8
        ))
        assert decision.status == "POST_QUARANTINED"
        assert decision.health_before == "NORMAL"
        assert decision.health_after == "POST_QUARANTINED"
        assert decision.requested_rechecks == ("down1", "down2")
        assert decision.examined_dependency_links == 2
        assert {a.action for a in decision.actions} == {"NOTICE", "POST_QUARANTINE", "REQUEST_RECHECK"}
        assert all(a.servant_disposition == "ACK_TRANSITION" for a in decision.actions)
        after = {wid: durable.shared.views.status(wid) for wid in before}
        assert after == before, "immune requests must not directly mutate epistemic workspace status"
        assert immune.health("proof") == "POST_QUARANTINED"
        assert immune.health("down1") == "NORMAL"
        assert immune.health("unrelated") == "NORMAL"

        records_before = len(immune.memory.records())
        replay = immune.observe(obs(
            "OBS-1", "IMM-INVALIDATION-FANOUT", "INVALIDATION_FANOUT", "proof", 8
        ))
        assert replay == decision
        assert len(immune.memory.records()) == records_before

        collision = immune.observe(obs(
            "OBS-1", "IMM-INVALIDATION-FANOUT", "INVALIDATION_FANOUT", "proof", 99
        ))
        assert collision.status == "STOP_ESCALATE_OBSERVATION_ID_COLLISION"
        assert immune.health("proof") == "POST_QUARANTINED"

        clear = immune.observe(obs(
            "OBS-2", "IMM-CLEAR-RECOVERY", "ANOMALY_CLEARED", "proof", 1
        ))
        assert clear.status == "ANOMALY_CLEARED_NEEDS_GUARDIAN_RELEASE"
        assert clear.health_after == "RECOVERED"
        assert clear.requested_rechecks == ()
        assert immune.health("proof") == "RECOVERED"

        restarted = ImmuneRuntime(
            durable.shared.views,
            servant,
            Path(td) / "immune.wal",
            signatures,
            budget=ReactionBudget(max_actions=8, max_rechecks=4),
        )
        assert restarted.health("proof") == "RECOVERED"
        assert restarted.signature_count("IMM-INVALIDATION-FANOUT", "proof") == 1

    # Before-admission faults are outside immune jurisdiction.
    with TemporaryDirectory() as td:
        durable, servant, immune = make_stack(td, budget=ReactionBudget())
        outside = immune.observe(obs(
            "OBS-B", "IMM-WAL-CORRUPTION", "WAL_CORRUPTION", "proof", 1, admission="OBSERVED"
        ))
        assert outside.status == "OUTSIDE_IMMUNE_SCOPE"
        assert outside.actions == ()
        assert immune.health("proof") == "NORMAL"

    # Unknown signature or non-matching type causes no autonomous inference/action.
    with TemporaryDirectory() as td:
        durable, servant, immune = make_stack(td, budget=ReactionBudget())
        unknown = immune.observe(obs("OBS-U", "NOT-LICENSED", "MYSTERY", "proof", 999))
        assert unknown.status == "NO_LICENSED_SIGNATURE"
        assert unknown.actions == ()
        mismatch = immune.observe(obs(
            "OBS-M", "IMM-WAL-CORRUPTION", "PROTOCOL_CONFLICT_COUNT", "proof", 1
        ))
        assert mismatch.status == "NO_LICENSED_SIGNATURE"
        assert mismatch.actions == ()

    # Reaction budget anti-autoimmunity: the dependency closure has two targets
    # but only one recheck slot. No arbitrary prefix is selected. The source may
    # be quarantined, then the incomplete fanout is escalated.
    with TemporaryDirectory() as td:
        durable, servant, immune = make_stack(td, budget=ReactionBudget(max_actions=3, max_rechecks=1))
        budgeted = immune.observe(obs(
            "OBS-BUDGET", "IMM-INVALIDATION-FANOUT", "INVALIDATION_FANOUT", "proof", 8
        ))
        assert budgeted.status == "BUDGET_EXHAUSTED_ESCALATE"
        assert budgeted.budget_exhausted is True
        assert budgeted.requested_rechecks == ()
        assert immune.health("proof") == "POST_QUARANTINED"
        assert durable.shared.views.status("down1") == "VALID"
        assert durable.shared.views.status("down2") == "VALID"
        assert all(a.action != "REQUEST_RECHECK" for a in budgeted.actions)

    # A clear signal without active quarantine cannot manufacture recovery.
    with TemporaryDirectory() as td:
        durable, servant, immune = make_stack(td, budget=ReactionBudget())
        clear = immune.observe(obs(
            "OBS-CLEAR-NONE", "IMM-CLEAR-RECOVERY", "ANOMALY_CLEARED", "proof", 1
        ))
        assert clear.status == "NO_ACTIVE_ANOMALY_TO_CLEAR"
        assert clear.actions == ()
        assert immune.health("proof") == "NORMAL"

    # Immune memory is append-only/hash-chained and therefore self-auditable.
    with TemporaryDirectory() as td:
        durable, servant, immune = make_stack(td, budget=ReactionBudget())
        immune.observe(obs("OBS-I", "IMM-CONFLICT-BURST", "PROTOCOL_CONFLICT_COUNT", "proof", 3))
        records = immune.memory.records()
        assert records
        assert records[0]["kind"] == "IMMUNE_OBSERVATION"
        assert records[-1]["kind"] == "IMMUNE_DECISION"

    print("PSI-MEMORY-IMMUNE-01 PASS_WITH_BOUNDARY")
    print("numeric_domain_boundary=PASS")
    print("nan_inf_bool_text_rejected_pre_signature=PASS")
    print("signature_declared_value_domain=PASS")
    print("invalid_domain_cannot_quarantine_or_increment=PASS")
    print("threshold_boundary_semantics=PASS")
    print("licensed_signatures_only=PASS")
    print("post_admission_scope_only=PASS")
    print("notice_quarantine_recheck_request=PASS")
    print("dependency_scoped_recheck_targets=PASS")
    print("immune_does_not_mutate_epistemic_status=PASS")
    print("reaction_budget_anti_autoimmunity=PASS")
    print("no_arbitrary_partial_fanout=PASS")
    print("clear_requires_active_anomaly=PASS")
    print("clear_does_not_release_active_exchange=PASS")
    print("servant_gates_institution_actions=PASS")
    print("immune_memory_recovery=PASS")
    print("semantic_truth_authority=ABSENT")
    print("BOUNDARY: deterministic licensed signatures over declared finite numeric domains; no learned anomaly model, no natural-language diagnosis, no autonomous threshold changes, no direct epistemic invalidation, no Guardian release, no distributed coordination")


if __name__ == "__main__":
    main()
