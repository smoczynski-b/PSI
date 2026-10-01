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
    return workspace("IMMUNE-REBIND-AUTH", "ROOT", "A")


def main() -> None:
    with TemporaryDirectory() as td:
        base = Path(td)
        registry_state = {"include_late": False}

        def register_views(shared):
            shared.register("proof", workspace("VIEW-PROOF", "ROOT", "A"))
            if registry_state["include_late"]:
                shared.register(
                    "late",
                    workspace("VIEW-LATE", "LROOT", "L"),
                    extra_dependencies=("workspace:proof",),
                )

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
            budget=ReactionBudget(max_actions=8, max_rechecks=4),
        )

        shared_handle = durable.shared
        views_handle = durable.shared.views
        assert immune.views is views_handle
        assert not views_handle.has_workspace("late")

        # Recovery rebuilds the registered map set. Long-lived institutional
        # components must retain a live handle to the rebuilt view index.
        registry_state["include_late"] = True
        durable.recover()

        assert durable.shared is shared_handle, "recovery replaced the public shared handle"
        assert durable.shared.views is views_handle, "recovery replaced the public views handle"
        assert immune.views is views_handle, "IMMUNE lost its live views binding"
        assert views_handle.has_workspace("late"), "old handle cannot see recovered view registry"
        assert views_handle.direct_dependents("workspace:proof") == ("late",)

        decision = immune.observe(ImmuneObservation(
            observation_id="OBS-REBIND",
            signature_id="IMM-INVALIDATION-FANOUT",
            observation_kind="INVALIDATION_FANOUT",
            subject_workspace="proof",
            admission_state="ADMITTED",
            value=8,
        ))
        assert decision.status == "POST_QUARANTINED"
        assert decision.requested_rechecks == ("late",)
        assert decision.examined_dependency_links == 1
        assert immune.health("proof") == "POST_QUARANTINED"

    print("PSI-MEMORY-IMMUNE-RECOVERY-BINDING-01 PASS")
    print("shared_handle_identity_after_recover=PASS")
    print("views_handle_identity_after_recover=PASS")
    print("immune_sees_recovered_view_registry=PASS")
    print("recovered_dependency_routing=PASS")


if __name__ == "__main__":
    main()
