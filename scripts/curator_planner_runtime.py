#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping
import hashlib
import json
import math

from durable_shared_memory import JSONLWAL
from servant_runtime import ServantCommand, ServantRuntime

OPERATIONS = {
    "EXPAND", "SPLIT", "MERGE", "REINDEX", "MIGRATE",
    "ARCHIVE", "COMPACT", "REBALANCE",
}
COMPARATORS = {"GT", "GTE", "LT", "LTE"}


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _finite_nonnegative(value, field: str) -> float:
    if isinstance(value, bool):
        raise ValueError(f"{field} must be a finite non-negative number")
    out = float(value)
    if not math.isfinite(out) or out < 0:
        raise ValueError(f"{field} must be a finite non-negative number")
    return out


@dataclass(frozen=True)
class PlanningRule:
    rule_id: str
    operation: str
    metric: str
    comparator: str
    threshold: float
    expected_benefit: str
    estimated_cost: float
    risk: str
    information_loss_risk: str
    required_dependencies: tuple[str, ...]
    rollback_requirement: str
    required_test: str

    def __post_init__(self):
        for field in (
            "rule_id", "operation", "metric", "comparator", "expected_benefit",
            "risk", "information_loss_risk", "rollback_requirement", "required_test",
        ):
            value = str(getattr(self, field)).strip()
            if not value:
                raise ValueError(f"{field} is required")
            object.__setattr__(self, field, value.upper() if field in {"operation", "comparator"} else value)
        if self.operation not in OPERATIONS:
            raise ValueError(f"unknown planning operation: {self.operation}")
        if self.comparator not in COMPARATORS:
            raise ValueError(f"unknown comparator: {self.comparator}")
        object.__setattr__(self, "threshold", _finite_nonnegative(self.threshold, "threshold"))
        object.__setattr__(self, "estimated_cost", _finite_nonnegative(self.estimated_cost, "estimated_cost"))
        deps = tuple(sorted({str(x).strip() for x in self.required_dependencies if str(x).strip()}))
        object.__setattr__(self, "required_dependencies", deps)

    def matches(self, value: float) -> bool:
        if self.comparator == "GT":
            return value > self.threshold
        if self.comparator == "GTE":
            return value >= self.threshold
        if self.comparator == "LT":
            return value < self.threshold
        return value <= self.threshold


@dataclass(frozen=True)
class CuratorPlanningPolicy:
    version: str
    rules: tuple[PlanningRule, ...]
    authority: str = "PSI_AGENT"

    def __post_init__(self):
        version = str(self.version).strip()
        authority = str(self.authority).strip().upper()
        if not version:
            raise ValueError("planning policy version is required")
        if authority != "PSI_AGENT":
            raise ValueError("Curator planner accepts PSI_AGENT-owned planning policy only")
        ids = [r.rule_id for r in self.rules]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate planning rule_id")
        object.__setattr__(self, "version", version)
        object.__setattr__(self, "authority", authority)
        object.__setattr__(self, "rules", tuple(self.rules))


@dataclass(frozen=True)
class DistrictObservation:
    observation_id: str
    district_id: str
    metrics: Mapping[str, float]
    observed_at: str
    policy_version: str

    def __post_init__(self):
        for field in ("observation_id", "district_id", "observed_at", "policy_version"):
            value = str(getattr(self, field)).strip()
            if not value:
                raise ValueError(f"{field} is required")
            object.__setattr__(self, field, value)
        clean: dict[str, float] = {}
        for key, value in self.metrics.items():
            name = str(key).strip()
            if not name:
                raise ValueError("metric name is required")
            clean[name] = _finite_nonnegative(value, f"metric:{name}")
        if not clean:
            raise ValueError("at least one administrative metric is required")
        object.__setattr__(self, "metrics", dict(sorted(clean.items())))

    def fingerprint(self) -> str:
        return _digest({
            "district_id": self.district_id,
            "metrics": dict(self.metrics),
            "observed_at": self.observed_at,
            "policy_version": self.policy_version,
        })


@dataclass(frozen=True)
class StructureProposal:
    proposal_id: str
    district_id: str
    observed_problem: str
    supporting_metrics: tuple[tuple[str, float], ...]
    proposed_operation: str
    expected_benefit: str
    estimated_cost: float
    risk: str
    information_loss_risk: str
    required_dependencies: tuple[str, ...]
    rollback_requirement: str
    required_test: str
    policy_version: str
    rule_id: str
    observation_id: str
    status: str = "PROPOSED"

    def as_dict(self) -> dict:
        return {
            "proposal_id": self.proposal_id,
            "district_id": self.district_id,
            "observed_problem": self.observed_problem,
            "supporting_metrics": {k: v for k, v in self.supporting_metrics},
            "proposed_operation": self.proposed_operation,
            "expected_benefit": self.expected_benefit,
            "estimated_cost": self.estimated_cost,
            "risk": self.risk,
            "information_loss_risk": self.information_loss_risk,
            "required_dependencies": list(self.required_dependencies),
            "rollback_requirement": self.rollback_requirement,
            "required_test": self.required_test,
            "policy_version": self.policy_version,
            "rule_id": self.rule_id,
            "observation_id": self.observation_id,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, row: dict) -> "StructureProposal":
        metrics = tuple(sorted((str(k), float(v)) for k, v in dict(row["supporting_metrics"]).items()))
        return cls(
            proposal_id=str(row["proposal_id"]),
            district_id=str(row["district_id"]),
            observed_problem=str(row["observed_problem"]),
            supporting_metrics=metrics,
            proposed_operation=str(row["proposed_operation"]),
            expected_benefit=str(row["expected_benefit"]),
            estimated_cost=float(row["estimated_cost"]),
            risk=str(row["risk"]),
            information_loss_risk=str(row["information_loss_risk"]),
            required_dependencies=tuple(row.get("required_dependencies", ())),
            rollback_requirement=str(row["rollback_requirement"]),
            required_test=str(row["required_test"]),
            policy_version=str(row["policy_version"]),
            rule_id=str(row["rule_id"]),
            observation_id=str(row["observation_id"]),
            status=str(row.get("status", "PROPOSED")),
        )


class CuratorPlanningError(RuntimeError):
    pass


class CuratorPlannerRuntime:
    """F3.3 deterministic proposal-only planner.

    It may persist auditable STRUCTURE_PROPOSAL records through an authorized
    SERVANT institution gate. It has no method that mutates memory structure,
    access policy, epistemic status, resource budgets, or the constitution.
    R8 also persists bounded identity/outcome records for observations that
    produce no proposal, so observation IDs cannot be reused with new payloads.
    """

    def __init__(
        self,
        servant: ServantRuntime,
        chronicle_path: str | Path,
        *,
        policy_lookup,
        current_policy_version,
        runbook_id: str = "CURATOR-PLANNER-01",
    ):
        self.servant = servant
        self.wal = JSONLWAL(chronicle_path)
        self.policy_lookup = policy_lookup
        self.current_policy_version = current_policy_version
        self.runbook_id = str(runbook_id).strip()
        if not self.runbook_id:
            raise ValueError("runbook_id is required")
        self._proposals: dict[str, StructureProposal] = {}
        self._observations: dict[str, str] = {}
        self._no_proposal_observations: set[str] = set()
        self._load()

    def _load(self) -> None:
        for record in self.wal.read_valid_prefix().records:
            kind = record.get("kind")
            payload = dict(record.get("payload", {}))
            if kind == "CURATOR_OBSERVATION":
                observation_id = str(payload.get("observation_id", "")).strip()
                fingerprint = str(payload.get("observation_fingerprint", "")).strip()
                outcome = str(payload.get("outcome", "")).strip().upper()
                if not observation_id or not fingerprint:
                    raise CuratorPlanningError("invalid persisted observation identity")
                if outcome != "NO_PROPOSAL":
                    raise CuratorPlanningError(f"unsupported persisted observation outcome: {outcome}")
                observed = self._observations.get(observation_id)
                if observed is not None and observed != fingerprint:
                    raise CuratorPlanningError(f"observation id collision: {observation_id}")
                self._observations.setdefault(observation_id, fingerprint)
                self._no_proposal_observations.add(observation_id)
                continue
            if kind != "CURATOR_PROPOSAL":
                raise CuratorPlanningError(f"unknown curator record kind: {kind}")
            proposal = StructureProposal.from_dict(payload.get("proposal", {}))
            fingerprint = str(payload.get("observation_fingerprint", ""))
            if not fingerprint:
                raise CuratorPlanningError("missing observation fingerprint")
            prior = self._proposals.get(proposal.proposal_id)
            if prior is not None and _canon(prior.as_dict()) != _canon(proposal.as_dict()):
                raise CuratorPlanningError(f"proposal id collision: {proposal.proposal_id}")
            observed = self._observations.get(proposal.observation_id)
            if observed is not None and observed != fingerprint:
                raise CuratorPlanningError(f"observation id collision: {proposal.observation_id}")
            if proposal.observation_id in self._no_proposal_observations:
                raise CuratorPlanningError(
                    f"observation has contradictory persisted outcomes: {proposal.observation_id}"
                )
            self._proposals.setdefault(proposal.proposal_id, proposal)
            self._observations.setdefault(proposal.observation_id, fingerprint)

    def _gate(self, proposal: StructureProposal) -> None:
        digest = _digest(proposal.as_dict())
        decision = self.servant.handle(ServantCommand(
            command_id=f"CURATOR-PLAN:{proposal.proposal_id}:{digest[:20]}",
            kind="INSTITUTION_ACTION",
            runbook_id=self.runbook_id,
            institution_action="NOTICE",
            subject_id=f"STRUCTURE_PROPOSAL:{proposal.proposal_id}:{digest}",
        ))
        if decision.disposition != "ACK_TRANSITION":
            raise CuratorPlanningError(f"SERVANT gate rejected proposal: {decision.reason_code}")

    def _gate_no_proposal(self, observation: DistrictObservation, fingerprint: str) -> None:
        decision = self.servant.handle(ServantCommand(
            command_id=f"CURATOR-OBS:{observation.observation_id}:{fingerprint[:20]}",
            kind="INSTITUTION_ACTION",
            runbook_id=self.runbook_id,
            institution_action="NOTICE",
            subject_id=(
                f"CURATOR_OBSERVATION_NO_PROPOSAL:{observation.observation_id}:{fingerprint}"
            ),
        ))
        if decision.disposition != "ACK_TRANSITION":
            raise CuratorPlanningError(
                f"SERVANT gate rejected observation record: {decision.reason_code}"
            )

    def evaluate(self, observation: DistrictObservation) -> tuple[StructureProposal, ...]:
        if not isinstance(observation, DistrictObservation):
            raise TypeError("CURATOR planner accepts DistrictObservation only")
        active = str(self.current_policy_version()).strip()
        if not active:
            raise CuratorPlanningError("PLANNING_POLICY_ABSENT")
        if observation.policy_version != active:
            raise CuratorPlanningError("PLANNING_POLICY_NOT_CURRENT")
        policy = self.policy_lookup(active)
        if not isinstance(policy, CuratorPlanningPolicy) or policy.authority != "PSI_AGENT":
            raise CuratorPlanningError("PLANNING_POLICY_ABSENT")

        fingerprint = observation.fingerprint()
        prior_fp = self._observations.get(observation.observation_id)
        if prior_fp is not None and prior_fp != fingerprint:
            raise CuratorPlanningError("OBSERVATION_ID_COLLISION")
        if observation.observation_id in self._no_proposal_observations:
            return ()

        out: list[StructureProposal] = []
        for rule in policy.rules:
            if rule.metric not in observation.metrics:
                continue
            value = observation.metrics[rule.metric]
            if not rule.matches(value):
                continue
            proposal_id = f"CURATOR:{observation.district_id}:{rule.rule_id}:{observation.observation_id}"
            proposal = StructureProposal(
                proposal_id=proposal_id,
                district_id=observation.district_id,
                observed_problem=f"{rule.metric} {rule.comparator} {rule.threshold}",
                supporting_metrics=((rule.metric, value),),
                proposed_operation=rule.operation,
                expected_benefit=rule.expected_benefit,
                estimated_cost=rule.estimated_cost,
                risk=rule.risk,
                information_loss_risk=rule.information_loss_risk,
                required_dependencies=rule.required_dependencies,
                rollback_requirement=rule.rollback_requirement,
                required_test=rule.required_test,
                policy_version=policy.version,
                rule_id=rule.rule_id,
                observation_id=observation.observation_id,
            )
            prior = self._proposals.get(proposal_id)
            if prior is not None:
                if _canon(prior.as_dict()) != _canon(proposal.as_dict()):
                    raise CuratorPlanningError("PROPOSAL_ID_COLLISION")
                out.append(prior)
                continue
            self._gate(proposal)
            self.wal.append("CURATOR_PROPOSAL", proposal_id, {
                "proposal": proposal.as_dict(),
                "observation_fingerprint": fingerprint,
            })
            self._proposals[proposal_id] = proposal
            self._observations.setdefault(observation.observation_id, fingerprint)
            out.append(proposal)

        if not out and observation.observation_id not in self._observations:
            self._gate_no_proposal(observation, fingerprint)
            self.wal.append("CURATOR_OBSERVATION", observation.observation_id, {
                "observation_id": observation.observation_id,
                "observation_fingerprint": fingerprint,
                "district_id": observation.district_id,
                "policy_version": observation.policy_version,
                "observed_at": observation.observed_at,
                "outcome": "NO_PROPOSAL",
            })
            self._observations[observation.observation_id] = fingerprint
            self._no_proposal_observations.add(observation.observation_id)
        return tuple(out)

    def proposal(self, proposal_id: str) -> StructureProposal:
        pid = str(proposal_id).strip()
        if pid not in self._proposals:
            raise CuratorPlanningError(f"unknown proposal: {pid}")
        return self._proposals[pid]

    def proposals(self) -> tuple[StructureProposal, ...]:
        return tuple(self._proposals[k] for k in sorted(self._proposals))

    def counts(self) -> dict[str, int]:
        observations_with_proposals = {
            proposal.observation_id for proposal in self._proposals.values()
        }
        return {
            "proposals": len(self._proposals),
            "observations": len(self._observations),
            "observations_with_proposals": len(observations_with_proposals),
            "no_proposal_observations": len(self._no_proposal_observations),
            "records": len(self.wal.read_valid_prefix().records),
        }
