#!/usr/bin/env python3
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import csv
import hashlib
import json

from durable_shared_memory import JSONLWAL
from multiworkspace_runtime import MultiWorkspaceRuntime
from servant_runtime import ServantCommand, ServantRuntime


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _fingerprint(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _as_bool(value: str) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


@dataclass(frozen=True)
class LicensedSignature:
    signature_id: str
    observation_kind: str
    min_value: float
    quarantine: bool
    request_recheck: bool
    clear: bool
    runbook_id: str

    def __post_init__(self):
        if not self.signature_id or not self.observation_kind or not self.runbook_id:
            raise ValueError("licensed signature requires id, observation kind and runbook")
        if self.min_value < 0:
            raise ValueError("min_value must be non-negative")
        if self.quarantine and self.clear:
            raise ValueError("signature cannot quarantine and clear in one step")


def load_signatures(path: str | Path) -> tuple[LicensedSignature, ...]:
    rows: list[LicensedSignature] = []
    with Path(path).open("r", encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            rows.append(LicensedSignature(
                signature_id=str(row["signature_id"]).strip(),
                observation_kind=str(row["observation_kind"]).strip(),
                min_value=float(row["min_value"]),
                quarantine=_as_bool(row["quarantine"]),
                request_recheck=_as_bool(row["request_recheck"]),
                clear=_as_bool(row["clear"]),
                runbook_id=str(row["runbook_id"]).strip(),
            ))
    ids = [row.signature_id for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("signature ids must be unique")
    return tuple(rows)


@dataclass(frozen=True)
class ImmuneObservation:
    observation_id: str
    signature_id: str
    observation_kind: str
    subject_workspace: str
    admission_state: str
    value: float

    def __post_init__(self):
        if not str(self.observation_id).strip():
            raise ValueError("observation_id is required")
        if not str(self.signature_id).strip():
            raise ValueError("signature_id is required")
        if not str(self.observation_kind).strip():
            raise ValueError("observation_kind is required")
        if not str(self.subject_workspace).strip():
            raise ValueError("subject_workspace is required")
        object.__setattr__(self, "observation_id", str(self.observation_id).strip())
        object.__setattr__(self, "signature_id", str(self.signature_id).strip())
        object.__setattr__(self, "observation_kind", str(self.observation_kind).strip())
        object.__setattr__(self, "subject_workspace", str(self.subject_workspace).strip())
        object.__setattr__(self, "admission_state", str(self.admission_state).strip().upper())
        object.__setattr__(self, "value", float(self.value))

    def fingerprint(self) -> str:
        return _fingerprint({
            "signature_id": self.signature_id,
            "observation_kind": self.observation_kind,
            "subject_workspace": self.subject_workspace,
            "admission_state": self.admission_state,
            "value": self.value,
        })


@dataclass(frozen=True)
class ReactionBudget:
    max_actions: int = 8
    max_rechecks: int = 4

    def __post_init__(self):
        if self.max_actions < 1 or self.max_rechecks < 0:
            raise ValueError("reaction budget must be non-negative and allow at least one action")


@dataclass(frozen=True)
class ImmuneAction:
    action: str
    subject_id: str
    servant_disposition: str
    servant_reason: str


@dataclass(frozen=True)
class ImmuneDecision:
    observation_id: str
    status: str
    signature_id: str
    health_before: str
    health_after: str
    actions: tuple[ImmuneAction, ...]
    requested_rechecks: tuple[str, ...]
    budget_exhausted: bool
    examined_dependency_links: int
    signature_count: int
    reason_code: str = ""


class ImmuneMemory:
    """Append-only immune observation/decision memory backed by hash-chained JSONL."""

    def __init__(self, path: str | Path):
        self.wal = JSONLWAL(path)

    def append_observation(self, observation: ImmuneObservation) -> None:
        self.wal.append("IMMUNE_OBSERVATION", observation.observation_id, {
            "observation_id": observation.observation_id,
            "observation_fingerprint": observation.fingerprint(),
            "signature_id": observation.signature_id,
            "observation_kind": observation.observation_kind,
            "subject_workspace": observation.subject_workspace,
            "admission_state": observation.admission_state,
            "value": observation.value,
        })

    def append_decision(self, observation: ImmuneObservation, decision: ImmuneDecision) -> None:
        self.wal.append("IMMUNE_DECISION", observation.observation_id, {
            "observation_id": observation.observation_id,
            "observation_fingerprint": observation.fingerprint(),
            "status": decision.status,
            "signature_id": decision.signature_id,
            "health_before": decision.health_before,
            "health_after": decision.health_after,
            "actions": [
                {
                    "action": action.action,
                    "subject_id": action.subject_id,
                    "servant_disposition": action.servant_disposition,
                    "servant_reason": action.servant_reason,
                }
                for action in decision.actions
            ],
            "requested_rechecks": list(decision.requested_rechecks),
            "budget_exhausted": decision.budget_exhausted,
            "examined_dependency_links": decision.examined_dependency_links,
            "signature_count": decision.signature_count,
            "reason_code": decision.reason_code,
        })

    def records(self):
        return self.wal.read_valid_prefix().records


class ImmuneRuntime:
    """Deterministic post-admission pathology detector with bounded response.

    The runtime recognizes only licensed signatures. It never declares domain
    truth, never deletes objects, never releases quarantine into active exchange,
    and never directly changes epistemic workspace status. REQUEST_RECHECK is a
    typed request only. Every institutional action is gated/chronicled by SERVANT.
    """

    def __init__(
        self,
        views: MultiWorkspaceRuntime,
        servant: ServantRuntime,
        memory_path: str | Path,
        signatures: Iterable[LicensedSignature],
        *,
        budget: ReactionBudget = ReactionBudget(),
    ):
        self.views = views
        self.servant = servant
        self.memory = ImmuneMemory(memory_path)
        self.signatures = {sig.signature_id: sig for sig in signatures}
        if not self.signatures:
            raise ValueError("at least one licensed immune signature is required")
        self.budget = budget
        self._health: dict[str, str] = {}
        self._signature_counts: dict[tuple[str, str], int] = {}
        self._completed: dict[str, tuple[str, ImmuneDecision]] = {}
        self._restore_memory()

    def _restore_memory(self) -> None:
        for record in self.memory.records():
            if record.get("kind") != "IMMUNE_DECISION":
                continue
            p = record.get("payload", {})
            obs_id = str(p.get("observation_id", ""))
            fp = str(p.get("observation_fingerprint", ""))
            if not obs_id or not fp:
                continue
            actions = tuple(
                ImmuneAction(
                    action=str(a["action"]),
                    subject_id=str(a["subject_id"]),
                    servant_disposition=str(a["servant_disposition"]),
                    servant_reason=str(a["servant_reason"]),
                )
                for a in p.get("actions", ())
            )
            decision = ImmuneDecision(
                observation_id=obs_id,
                status=str(p.get("status", "")),
                signature_id=str(p.get("signature_id", "")),
                health_before=str(p.get("health_before", "NORMAL")),
                health_after=str(p.get("health_after", "NORMAL")),
                actions=actions,
                requested_rechecks=tuple(str(x) for x in p.get("requested_rechecks", ())),
                budget_exhausted=bool(p.get("budget_exhausted", False)),
                examined_dependency_links=int(p.get("examined_dependency_links", 0)),
                signature_count=int(p.get("signature_count", 0)),
                reason_code=str(p.get("reason_code", "")),
            )
            self._completed[obs_id] = (fp, decision)
            if decision.health_after:
                # The subject is recoverable from action records when health changed.
                subject = next((a.subject_id for a in actions if a.action in {"POST_QUARANTINE", "CLEAR_ANOMALY"}), "")
                if subject:
                    self._health[subject] = decision.health_after
            if decision.signature_id and decision.signature_count:
                subject = next((a.subject_id for a in actions if a.action in {"NOTICE", "POST_QUARANTINE", "CLEAR_ANOMALY"}), "")
                if subject:
                    self._signature_counts[(decision.signature_id, subject)] = max(
                        decision.signature_count,
                        self._signature_counts.get((decision.signature_id, subject), 0),
                    )

    def health(self, workspace_id: str) -> str:
        return self._health.get(str(workspace_id).strip(), "NORMAL")

    def signature_count(self, signature_id: str, workspace_id: str) -> int:
        return self._signature_counts.get((str(signature_id).strip(), str(workspace_id).strip()), 0)

    def _bounded_dependents(self, subject_workspace: str) -> tuple[tuple[str, ...], bool, int]:
        max_rechecks = min(self.budget.max_rechecks, max(0, self.budget.max_actions - 2))
        queue = deque([f"workspace:{subject_workspace}"])
        visited_tokens: set[str] = set()
        dependents: set[str] = set()
        examined_links = 0

        while queue:
            token = queue.popleft()
            if token in visited_tokens:
                continue
            visited_tokens.add(token)
            direct = self.views.direct_dependents(token)
            examined_links += len(direct)
            for wid in direct:
                if wid in dependents:
                    continue
                dependents.add(wid)
                if len(dependents) > max_rechecks:
                    return tuple(), True, examined_links
                queue.append(f"workspace:{wid}")
        return tuple(sorted(dependents)), False, examined_links

    def _servant_action(
        self,
        observation: ImmuneObservation,
        signature: LicensedSignature,
        action: str,
        subject_id: str,
        ordinal: int,
    ) -> ImmuneAction:
        command = ServantCommand(
            command_id=f"immune:{observation.observation_id}:{ordinal}:{action}:{subject_id}",
            kind="INSTITUTION_ACTION",
            runbook_id=signature.runbook_id,
            institution_action=action,
            subject_id=subject_id,
        )
        decision = self.servant.handle(command)
        return ImmuneAction(
            action=action,
            subject_id=subject_id,
            servant_disposition=decision.disposition,
            servant_reason=decision.reason_code,
        )

    def _record(self, observation: ImmuneObservation, decision: ImmuneDecision) -> ImmuneDecision:
        self.memory.append_decision(observation, decision)
        self._completed[observation.observation_id] = (observation.fingerprint(), decision)
        return decision

    def observe(self, observation: ImmuneObservation) -> ImmuneDecision:
        if not isinstance(observation, ImmuneObservation):
            raise TypeError("IMMUNE accepts ImmuneObservation only")

        prior = self._completed.get(observation.observation_id)
        if prior is not None:
            if prior[0] == observation.fingerprint():
                return prior[1]
            return ImmuneDecision(
                observation_id=observation.observation_id,
                status="STOP_ESCALATE_OBSERVATION_ID_COLLISION",
                signature_id=observation.signature_id,
                health_before=self.health(observation.subject_workspace),
                health_after=self.health(observation.subject_workspace),
                actions=(),
                requested_rechecks=(),
                budget_exhausted=False,
                examined_dependency_links=0,
                signature_count=self.signature_count(observation.signature_id, observation.subject_workspace),
                reason_code="OBSERVATION_ID_COLLISION",
            )

        self.memory.append_observation(observation)
        health_before = self.health(observation.subject_workspace)

        if observation.admission_state != "ADMITTED":
            return self._record(observation, ImmuneDecision(
                observation_id=observation.observation_id,
                status="OUTSIDE_IMMUNE_SCOPE",
                signature_id=observation.signature_id,
                health_before=health_before,
                health_after=health_before,
                actions=(),
                requested_rechecks=(),
                budget_exhausted=False,
                examined_dependency_links=0,
                signature_count=self.signature_count(observation.signature_id, observation.subject_workspace),
                reason_code="BOUNDARY_BEFORE_IMMUNE",
            ))

        if not self.views.has_workspace(observation.subject_workspace):
            return self._record(observation, ImmuneDecision(
                observation_id=observation.observation_id,
                status="STOP_ESCALATE_UNKNOWN_SUBJECT",
                signature_id=observation.signature_id,
                health_before=health_before,
                health_after=health_before,
                actions=(),
                requested_rechecks=(),
                budget_exhausted=False,
                examined_dependency_links=0,
                signature_count=0,
                reason_code="UNKNOWN_WORKSPACE",
            ))

        signature = self.signatures.get(observation.signature_id)
        if signature is None or signature.observation_kind != observation.observation_kind:
            return self._record(observation, ImmuneDecision(
                observation_id=observation.observation_id,
                status="NO_LICENSED_SIGNATURE",
                signature_id=observation.signature_id,
                health_before=health_before,
                health_after=health_before,
                actions=(),
                requested_rechecks=(),
                budget_exhausted=False,
                examined_dependency_links=0,
                signature_count=0,
                reason_code="SIGNATURE_NOT_LICENSED_FOR_OBSERVATION",
            ))

        if observation.value < signature.min_value:
            return self._record(observation, ImmuneDecision(
                observation_id=observation.observation_id,
                status="NO_ANOMALY",
                signature_id=signature.signature_id,
                health_before=health_before,
                health_after=health_before,
                actions=(),
                requested_rechecks=(),
                budget_exhausted=False,
                examined_dependency_links=0,
                signature_count=self.signature_count(signature.signature_id, observation.subject_workspace),
                reason_code="SIGNATURE_THRESHOLD_NOT_MET",
            ))

        key = (signature.signature_id, observation.subject_workspace)
        count = self._signature_counts.get(key, 0) + 1
        self._signature_counts[key] = count

        if signature.clear and health_before != "POST_QUARANTINED":
            return self._record(observation, ImmuneDecision(
                observation_id=observation.observation_id,
                status="NO_ACTIVE_ANOMALY_TO_CLEAR",
                signature_id=signature.signature_id,
                health_before=health_before,
                health_after=health_before,
                actions=(),
                requested_rechecks=(),
                budget_exhausted=False,
                examined_dependency_links=0,
                signature_count=count,
                reason_code="CLEAR_REQUIRES_POST_QUARANTINED",
            ))

        planned_rechecks: tuple[str, ...] = ()
        budget_exhausted = False
        examined_links = 0
        if signature.request_recheck:
            planned_rechecks, budget_exhausted, examined_links = self._bounded_dependents(
                observation.subject_workspace
            )

        base_actions: list[tuple[str, str]] = [("NOTICE", observation.subject_workspace)]
        if signature.quarantine:
            base_actions.append(("POST_QUARANTINE", observation.subject_workspace))
        if signature.clear:
            base_actions.append(("CLEAR_ANOMALY", observation.subject_workspace))

        if len(base_actions) > self.budget.max_actions:
            return self._record(observation, ImmuneDecision(
                observation_id=observation.observation_id,
                status="BUDGET_EXHAUSTED_ESCALATE",
                signature_id=signature.signature_id,
                health_before=health_before,
                health_after=health_before,
                actions=(),
                requested_rechecks=(),
                budget_exhausted=True,
                examined_dependency_links=examined_links,
                signature_count=count,
                reason_code="MINIMUM_RESPONSE_EXCEEDS_BUDGET",
            ))

        # All-or-none recheck fanout: if closure exceeds the budget, quarantine
        # the source and escalate, but do not mark an arbitrary prefix for recheck.
        if budget_exhausted:
            planned_rechecks = ()

        action_plan = list(base_actions)
        action_plan.extend(("REQUEST_RECHECK", wid) for wid in planned_rechecks)
        if len(action_plan) > self.budget.max_actions:
            budget_exhausted = True
            action_plan = list(base_actions)
            planned_rechecks = ()

        actions: list[ImmuneAction] = []
        for ordinal, (action, subject) in enumerate(action_plan):
            actions.append(self._servant_action(observation, signature, action, subject, ordinal))

        servant_blocked = any(action.servant_disposition != "ACK_TRANSITION" for action in actions)
        health_after = health_before
        if not servant_blocked:
            if signature.quarantine:
                health_after = "POST_QUARANTINED"
                self._health[observation.subject_workspace] = health_after
            elif signature.clear:
                health_after = "RECOVERED"
                self._health[observation.subject_workspace] = health_after

        if servant_blocked:
            status = "SERVANT_BLOCKED"
        elif budget_exhausted:
            status = "BUDGET_EXHAUSTED_ESCALATE"
        elif signature.clear:
            status = "ANOMALY_CLEARED_NEEDS_GUARDIAN_RELEASE"
        else:
            status = "POST_QUARANTINED" if signature.quarantine else "NOTICE_ONLY"

        accepted_rechecks = tuple(
            action.subject_id
            for action in actions
            if action.action == "REQUEST_RECHECK" and action.servant_disposition == "ACK_TRANSITION"
        )

        return self._record(observation, ImmuneDecision(
            observation_id=observation.observation_id,
            status=status,
            signature_id=signature.signature_id,
            health_before=health_before,
            health_after=health_after,
            actions=tuple(actions),
            requested_rechecks=accepted_rechecks,
            budget_exhausted=budget_exhausted,
            examined_dependency_links=examined_links,
            signature_count=count,
            reason_code=("REACTION_BUDGET_LIMIT" if budget_exhausted else "LICENSED_SIGNATURE_MATCH"),
        ))
