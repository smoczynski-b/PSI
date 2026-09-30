#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable
import hashlib
import json
import math

from active_memory import MemoryEvent
from durable_shared_memory import JSONLWAL
from mvcc_workspace import MVCCProposal
from servant_runtime import ServantCommand, ServantRuntime

OUTSIDE = "__OUTSIDE__"
CAP_ENTER = "ENTER_MAP"
CAP_TRANSIT = "TRANSIT_TO_MAP"
CAP_ACT = "ACT_IN_MAP"
CAP_EXPORT = "EXPORT_FROM_MAP"
CAP_TELEMETRY = "VIEW_TELEMETRY"
CAPABILITIES = {CAP_ENTER, CAP_TRANSIT, CAP_ACT, CAP_EXPORT, CAP_TELEMETRY}
MOVEMENT_OPERATIONS = {"ENTER", "TRANSIT", "EXIT"}
TELEMETRY_CLASSES = {
    "T0_SESSION_LOCAL",
    "T1_SECURITY_RESTRICTED",
    "T2_AUDIT_DURABLE",
    "T3_AGGREGATED",
}


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _fingerprint(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _finite_nonnegative(value: float, field: str) -> float:
    if isinstance(value, bool):
        raise ValueError(f"{field} must be a finite non-negative number")
    out = float(value)
    if not math.isfinite(out) or out < 0:
        raise ValueError(f"{field} must be a finite non-negative number")
    return out


@dataclass(frozen=True)
class CostVector:
    compute: float = 0.0
    transfer: float = 0.0
    context: float = 0.0
    latency: float = 0.0
    disclosure: float = 0.0
    synchronization: float = 0.0
    risk: float = 0.0

    def __post_init__(self):
        for name in (
            "compute", "transfer", "context", "latency", "disclosure",
            "synchronization", "risk",
        ):
            object.__setattr__(self, name, _finite_nonnegative(getattr(self, name), name))

    @property
    def l1(self) -> float:
        return sum(self.as_dict().values())

    def as_dict(self) -> dict[str, float]:
        return {
            "compute": self.compute,
            "transfer": self.transfer,
            "context": self.context,
            "latency": self.latency,
            "disclosure": self.disclosure,
            "synchronization": self.synchronization,
            "risk": self.risk,
        }

    def within(self, budget: "CostVector") -> bool:
        return all(self.as_dict()[k] <= budget.as_dict()[k] for k in self.as_dict())


@dataclass(frozen=True)
class MapState:
    map_id: str
    exists: bool = True
    accepts_entry: bool = True
    accepts_transit: bool = True
    health_gate_open: bool = True

    def __post_init__(self):
        mid = str(self.map_id).strip()
        if not mid or mid == OUTSIDE:
            raise ValueError("map_id must name a real map")
        object.__setattr__(self, "map_id", mid)


@dataclass(frozen=True)
class PolicyRule:
    actor_id: str
    session_id: str
    operation: str
    map_from: str
    map_to: str
    purpose: str
    capability: str
    telemetry_classes: tuple[str, ...] = ()

    def __post_init__(self):
        for field in ("actor_id", "session_id", "operation", "map_from", "map_to", "purpose", "capability"):
            value = str(getattr(self, field)).strip()
            if not value:
                raise ValueError(f"{field} is required")
            object.__setattr__(self, field, value.upper() if field in {"operation", "capability"} else value)
        if self.capability not in CAPABILITIES:
            raise ValueError(f"unknown capability: {self.capability}")
        classes = tuple(sorted({str(x).strip().upper() for x in self.telemetry_classes if str(x).strip()}))
        if any(x not in TELEMETRY_CLASSES for x in classes):
            raise ValueError("unknown telemetry class")
        object.__setattr__(self, "telemetry_classes", classes)


@dataclass(frozen=True)
class GuardianAccessPolicy:
    version: str
    rules: tuple[PolicyRule, ...]
    authority: str = "GUARDIAN"

    def __post_init__(self):
        version = str(self.version).strip()
        authority = str(self.authority).strip().upper()
        if not version:
            raise ValueError("policy version is required")
        if authority != "GUARDIAN":
            raise ValueError("ACCESS_STEWARD accepts Guardian-owned policy only")
        object.__setattr__(self, "version", version)
        object.__setattr__(self, "authority", authority)
        object.__setattr__(self, "rules", tuple(self.rules))

    def matching_rule(
        self,
        *,
        actor_id: str,
        session_id: str,
        operation: str,
        map_from: str,
        map_to: str,
        purpose: str,
        capability: str,
    ) -> PolicyRule | None:
        needle = (
            actor_id, session_id, operation.upper(), map_from, map_to,
            purpose, capability.upper(),
        )
        for rule in self.rules:
            row = (
                rule.actor_id, rule.session_id, rule.operation,
                rule.map_from, rule.map_to, rule.purpose, rule.capability,
            )
            if row == needle:
                return rule
        return None


@dataclass(frozen=True)
class MovementRequest:
    request_id: str
    session_id: str
    actor_id: str
    operation: str
    map_from: str
    map_to: str
    declared_purpose: str
    requested_capability: str
    policy_version: str
    budget: CostVector
    estimated_cost: CostVector
    event_time: str

    def __post_init__(self):
        for field in (
            "request_id", "session_id", "actor_id", "operation", "map_from",
            "map_to", "declared_purpose", "requested_capability", "policy_version",
            "event_time",
        ):
            value = str(getattr(self, field)).strip()
            if not value:
                raise ValueError(f"{field} is required")
            object.__setattr__(
                self,
                field,
                value.upper() if field in {"operation", "requested_capability"} else value,
            )
        if self.operation not in MOVEMENT_OPERATIONS:
            raise ValueError("movement operation must be ENTER, TRANSIT or EXIT")
        if self.requested_capability not in CAPABILITIES:
            raise ValueError("unknown requested capability")

    def fingerprint(self) -> str:
        return _fingerprint({
            "session_id": self.session_id,
            "actor_id": self.actor_id,
            "operation": self.operation,
            "map_from": self.map_from,
            "map_to": self.map_to,
            "declared_purpose": self.declared_purpose,
            "requested_capability": self.requested_capability,
            "policy_version": self.policy_version,
            "budget": self.budget.as_dict(),
            "estimated_cost": self.estimated_cost.as_dict(),
            "event_time": self.event_time,
        })


@dataclass(frozen=True)
class MovementDecision:
    request_id: str
    disposition: str
    reason_code: str
    policy_version: str
    location_before: str
    location_after: str
    estimated_cost: CostVector
    actual_cost: CostVector
    servant_disposition: str = ""
    servant_reason: str = ""
    txid: str = ""


@dataclass(frozen=True)
class CompletedRequest:
    fingerprint: str
    disposition: str
    reason_code: str
    policy_version: str
    location_before: str
    location_after: str
    estimated_cost: CostVector
    actual_cost: CostVector
    servant_disposition: str
    servant_reason: str
    txid: str


@dataclass(frozen=True)
class TelemetryQuery:
    actor_id: str
    session_id: str
    telemetry_class: str
    purpose: str
    policy_version: str

    def __post_init__(self):
        for field in ("actor_id", "session_id", "telemetry_class", "purpose", "policy_version"):
            value = str(getattr(self, field)).strip()
            if not value:
                raise ValueError(f"{field} is required")
            object.__setattr__(self, field, value.upper() if field == "telemetry_class" else value)
        if self.telemetry_class not in TELEMETRY_CLASSES:
            raise ValueError("unknown telemetry class")


class AccessChronicle:
    """Append-only audit journal. It records movement; it is not authoritative presence."""

    def __init__(self, path: str | Path):
        self.wal = JSONLWAL(path)

    def append(self, kind: str, request_id: str, payload: dict) -> None:
        self.wal.append(f"ACCESS_{kind}", request_id, payload)

    def records(self):
        return self.wal.read_valid_prefix().records


class AccessStewardRuntime:
    """Deterministic F2.1 executor of Guardian-owned access policy.

    Durable session presence is never written directly by this class. Movement
    is materialized as an administrative presence edge only through SERVANT ->
    MVCC -> durable WAL. This runtime owns only the movement audit chronicle.
    """

    def __init__(
        self,
        servant: ServantRuntime,
        chronicle_path: str | Path,
        *,
        presence_anchor: str,
        policy_lookup: Callable[[str], GuardianAccessPolicy | None],
        current_policy_version: Callable[[], str],
        map_state_lookup: Callable[[str], MapState | None],
        cost_meter: Callable[[MovementRequest], CostVector],
    ):
        self.servant = servant
        self.chronicle = AccessChronicle(chronicle_path)
        self.presence_anchor = str(presence_anchor).strip()
        if not self.presence_anchor:
            raise ValueError("presence_anchor is required")
        self.policy_lookup = policy_lookup
        self.current_policy_version = current_policy_version
        self.map_state_lookup = map_state_lookup
        self.cost_meter = cost_meter
        self._completed = self._load_completed()
        self._assert_presence_integrity()

    @property
    def authoritative_workspace(self):
        return self.servant.durable.shared.memory.workspace

    @staticmethod
    def _relation(session_id: str) -> str:
        return f"SESSION_AT::{session_id}"

    def _presence_rows(self, session_id: str) -> list[str]:
        relation = self._relation(session_id)
        return sorted(
            edge.target
            for edge in self.authoritative_workspace.edges.values()
            if edge.source == self.presence_anchor and edge.relation == relation
        )

    def _assert_presence_integrity(self) -> None:
        by_session: dict[str, list[str]] = {}
        prefix = "SESSION_AT::"
        for edge in self.authoritative_workspace.edges.values():
            if edge.source != self.presence_anchor or not edge.relation.startswith(prefix):
                continue
            sid = edge.relation[len(prefix):]
            by_session.setdefault(sid, []).append(edge.target)
        broken = {sid: sorted(rows) for sid, rows in by_session.items() if len(rows) > 1}
        if broken:
            raise RuntimeError(f"presence integrity violation: {broken}")

    def location(self, session_id: str) -> str:
        rows = self._presence_rows(str(session_id).strip())
        if len(rows) > 1:
            raise RuntimeError("same session present in multiple maps")
        return rows[0] if rows else OUTSIDE

    def _load_completed(self) -> dict[str, CompletedRequest]:
        completed: dict[str, CompletedRequest] = {}
        for record in self.chronicle.records():
            if record.get("kind") != "ACCESS_RESULT":
                continue
            payload = record.get("payload", {})
            rid = str(payload.get("request_id", ""))
            if not rid or rid in completed:
                continue
            try:
                completed[rid] = CompletedRequest(
                    fingerprint=str(payload["request_fingerprint"]),
                    disposition=str(payload["disposition"]),
                    reason_code=str(payload["reason_code"]),
                    policy_version=str(payload["policy_version"]),
                    location_before=str(payload["location_before"]),
                    location_after=str(payload["location_after"]),
                    estimated_cost=CostVector(**payload["estimated_cost"]),
                    actual_cost=CostVector(**payload["actual_cost"]),
                    servant_disposition=str(payload.get("servant_disposition", "")),
                    servant_reason=str(payload.get("servant_reason", "")),
                    txid=str(payload.get("txid", "")),
                )
            except (KeyError, TypeError, ValueError) as exc:
                raise RuntimeError(f"invalid ACCESS_RESULT in chronicle: {rid}") from exc
        return completed

    def _observed(self, request: MovementRequest) -> None:
        self.chronicle.append("OBSERVED", request.request_id, {
            "request_id": request.request_id,
            "request_fingerprint": request.fingerprint(),
            "session_id": request.session_id,
            "actor_id": request.actor_id,
            "operation": request.operation,
            "map_from": request.map_from,
            "map_to": request.map_to,
            "declared_purpose": request.declared_purpose,
            "requested_capability": request.requested_capability,
            "policy_version": request.policy_version,
            "event_time": request.event_time,
        })

    def _finish(
        self,
        request: MovementRequest,
        *,
        disposition: str,
        reason_code: str,
        before: str,
        after: str,
        actual_cost: CostVector | None = None,
        servant_disposition: str = "",
        servant_reason: str = "",
        txid: str = "",
        remember: bool = True,
    ) -> MovementDecision:
        actual = actual_cost or CostVector()
        decision = MovementDecision(
            request_id=request.request_id,
            disposition=disposition,
            reason_code=reason_code,
            policy_version=request.policy_version,
            location_before=before,
            location_after=after,
            estimated_cost=request.estimated_cost,
            actual_cost=actual,
            servant_disposition=servant_disposition,
            servant_reason=servant_reason,
            txid=txid,
        )
        self.chronicle.append("RESULT", request.request_id, {
            "request_id": request.request_id,
            "request_fingerprint": request.fingerprint(),
            "disposition": disposition,
            "reason_code": reason_code,
            "policy_version": request.policy_version,
            "location_before": before,
            "location_after": after,
            "estimated_cost": request.estimated_cost.as_dict(),
            "actual_cost": actual.as_dict(),
            "servant_disposition": servant_disposition,
            "servant_reason": servant_reason,
            "txid": txid,
        })
        if remember:
            self._completed[request.request_id] = CompletedRequest(
                fingerprint=request.fingerprint(),
                disposition=disposition,
                reason_code=reason_code,
                policy_version=request.policy_version,
                location_before=before,
                location_after=after,
                estimated_cost=request.estimated_cost,
                actual_cost=actual,
                servant_disposition=servant_disposition,
                servant_reason=servant_reason,
                txid=txid,
            )
        return decision

    def _replay(self, request: MovementRequest, prior: CompletedRequest, before: str) -> MovementDecision:
        return self._finish(
            request,
            disposition=prior.disposition,
            reason_code=f"IDEMPOTENT_REPLAY:{prior.reason_code}",
            before=prior.location_before,
            after=prior.location_after,
            actual_cost=prior.actual_cost,
            servant_disposition=prior.servant_disposition,
            servant_reason=prior.servant_reason,
            txid=prior.txid,
            remember=False,
        )

    def _deny(self, request: MovementRequest, before: str, reason: str) -> MovementDecision:
        return self._finish(
            request,
            disposition="DENY_ACCESS",
            reason_code=reason,
            before=before,
            after=before,
        )

    def _stop(self, request: MovementRequest, before: str, reason: str, *, remember: bool = True) -> MovementDecision:
        self.chronicle.append("ESCALATE", request.request_id, {
            "request_id": request.request_id,
            "reason_code": reason,
            "location": before,
        })
        return self._finish(
            request,
            disposition="STOP_ESCALATE",
            reason_code=reason,
            before=before,
            after=before,
            remember=remember,
        )

    @staticmethod
    def _required_capability(operation: str) -> str:
        return CAP_ENTER if operation == "ENTER" else CAP_TRANSIT

    def _policy(self, version: str) -> GuardianAccessPolicy | None:
        policy = self.policy_lookup(version)
        if policy is None:
            return None
        if not isinstance(policy, GuardianAccessPolicy) or policy.authority != "GUARDIAN":
            raise RuntimeError("policy provider returned non-Guardian policy")
        return policy

    def _target_legal(self, request: MovementRequest) -> str | None:
        if request.operation == "EXIT":
            if request.map_to != OUTSIDE:
                return "EXIT_TARGET_MUST_BE_OUTSIDE"
            return None
        if request.map_to == OUTSIDE:
            return "TARGET_MAP_REQUIRED"
        target = self.map_state_lookup(request.map_to)
        if target is None or not target.exists:
            return "UNKNOWN_TARGET_MAP"
        if not target.health_gate_open:
            return "TARGET_HEALTH_GATE_CLOSED"
        if request.operation == "ENTER" and not target.accepts_entry:
            return "TARGET_REJECTS_ENTRY"
        if request.operation == "TRANSIT" and not target.accepts_transit:
            return "TARGET_REJECTS_TRANSIT"
        return None

    def _presence_events(self, request: MovementRequest) -> tuple[MemoryEvent, ...]:
        events: list[MemoryEvent] = []
        relation = self._relation(request.session_id)
        if request.operation in {"TRANSIT", "EXIT"}:
            events.append(MemoryEvent(
                event_id=f"access:{request.request_id}:remove",
                kind="EDGE_REMOVE",
                event_time=request.event_time,
                ingest_time=request.event_time,
                payload={
                    "from": self.presence_anchor,
                    "relation": relation,
                    "to": request.map_from,
                },
            ))
        if request.operation in {"ENTER", "TRANSIT"}:
            events.append(MemoryEvent(
                event_id=f"access:{request.request_id}:upsert",
                kind="EDGE_UPSERT",
                event_time=request.event_time,
                ingest_time=request.event_time,
                payload={
                    "from": self.presence_anchor,
                    "relation": relation,
                    "to": request.map_to,
                    "source": f"access:{request.request_id}",
                    "status": "ACCESS_PRESENCE",
                },
            ))
        return tuple(events)

    def _servant_command(self, request: MovementRequest) -> ServantCommand:
        base = self.servant.durable.revision
        proposals = tuple(
            MVCCProposal(
                proposal_id=f"access:{request.request_id}:{idx}",
                actor_id="ACCESS_STEWARD",
                base_revision=base,
                event=event,
            )
            for idx, event in enumerate(self._presence_events(request), start=1)
        )
        return ServantCommand(
            command_id=f"access:{request.request_id}",
            kind="TRANSACT",
            txid=f"access:{request.request_id}",
            proposals=proposals,
        )

    def handle(self, request: MovementRequest) -> MovementDecision:
        if not isinstance(request, MovementRequest):
            raise TypeError("ACCESS_STEWARD accepts MovementRequest only")
        before = self.location(request.session_id)
        prior = self._completed.get(request.request_id)
        self._observed(request)
        if prior is not None:
            if prior.fingerprint == request.fingerprint():
                return self._replay(request, prior, before)
            return self._stop(request, before, "REQUEST_ID_COLLISION", remember=False)

        active_version = str(self.current_policy_version()).strip()
        if not active_version:
            return self._stop(request, before, "GUARDIAN_POLICY_ABSENT")
        if request.policy_version != active_version:
            return self._deny(request, before, "POLICY_VERSION_NOT_CURRENT")
        policy = self._policy(request.policy_version)
        if policy is None:
            return self._stop(request, before, "GUARDIAN_POLICY_ABSENT")

        required_cap = self._required_capability(request.operation)
        if request.requested_capability != required_cap:
            return self._deny(request, before, "CAPABILITY_OPERATION_MISMATCH")

        if request.operation == "ENTER":
            if request.map_from != OUTSIDE:
                return self._deny(request, before, "ENTER_SOURCE_MUST_BE_OUTSIDE")
            if before != OUTSIDE:
                return self._deny(request, before, "SESSION_ALREADY_PRESENT")
        else:
            if before != request.map_from:
                return self._deny(request, before, "SESSION_LOCATION_MISMATCH")

        target_fault = self._target_legal(request)
        if target_fault:
            if target_fault == "UNKNOWN_TARGET_MAP":
                return self._stop(request, before, target_fault)
            return self._deny(request, before, target_fault)

        rule = policy.matching_rule(
            actor_id=request.actor_id,
            session_id=request.session_id,
            operation=request.operation,
            map_from=request.map_from,
            map_to=request.map_to,
            purpose=request.declared_purpose,
            capability=request.requested_capability,
        )
        if rule is None:
            return self._deny(request, before, "NO_MATCHING_GUARDIAN_RULE")

        changed_location = request.map_from != request.map_to
        if changed_location and request.estimated_cost.l1 <= 0:
            return self._stop(request, before, "CROSS_MAP_ZERO_ESTIMATED_COST")
        if not request.estimated_cost.within(request.budget):
            return self._deny(request, before, "ESTIMATED_COST_EXCEEDS_BUDGET")

        try:
            actual = self.cost_meter(request)
        except Exception as exc:
            return self._stop(request, before, f"COST_METER_FAILURE:{type(exc).__name__}")
        if not isinstance(actual, CostVector):
            return self._stop(request, before, "COST_METER_INVALID_TYPE")
        if changed_location and actual.l1 <= 0:
            return self._stop(request, before, "CROSS_MAP_ZERO_ACTUAL_COST")
        if not actual.within(request.budget):
            return self._deny(request, before, "ACTUAL_COST_EXCEEDS_BUDGET")

        command = self._servant_command(request)
        servant_decision = self.servant.handle(command)
        if servant_decision.disposition != "ACK_TRANSITION":
            return self._finish(
                request,
                disposition="DENY_ACCESS",
                reason_code="SERVANT_REJECTED_DURABLE_MOVEMENT",
                before=before,
                after=before,
                actual_cost=actual,
                servant_disposition=servant_decision.disposition,
                servant_reason=servant_decision.reason_code,
                txid=command.txid,
            )

        after = self.location(request.session_id)
        expected_after = request.map_to if request.operation != "EXIT" else OUTSIDE
        if after != expected_after:
            return self._stop(request, before, "DURABLE_PRESENCE_DIVERGENCE")

        self.chronicle.append("MOVEMENT", request.request_id, {
            "request_id": request.request_id,
            "session_id": request.session_id,
            "actor_id": request.actor_id,
            "map_from": request.map_from,
            "map_to": request.map_to,
            "declared_purpose": request.declared_purpose,
            "policy_version": request.policy_version,
            "capabilities_used": [request.requested_capability],
            "event_time": request.event_time,
            "estimated_cost": request.estimated_cost.as_dict(),
            "actual_cost": actual.as_dict(),
            "result": "MOVED",
            "telemetry_class": "T2_AUDIT_DURABLE",
            "servant_command_id": command.command_id,
            "txid": command.txid,
        })
        return self._finish(
            request,
            disposition="ALLOW_MOVEMENT",
            reason_code="MOVEMENT_COMMITTED_VIA_SERVANT",
            before=before,
            after=after,
            actual_cost=actual,
            servant_disposition=servant_decision.disposition,
            servant_reason=servant_decision.reason_code,
            txid=command.txid,
        )

    def check_capability(
        self,
        *,
        actor_id: str,
        session_id: str,
        capability: str,
        purpose: str,
        policy_version: str,
        map_to: str | None = None,
    ) -> tuple[bool, str]:
        cap = str(capability).strip().upper()
        if cap not in {CAP_ACT, CAP_EXPORT}:
            return False, "CHECK_CAPABILITY_SUPPORTS_ACT_OR_EXPORT_ONLY"
        active_version = str(self.current_policy_version()).strip()
        if not active_version or policy_version != active_version:
            return False, "POLICY_VERSION_NOT_CURRENT"
        policy = self._policy(policy_version)
        if policy is None:
            return False, "GUARDIAN_POLICY_ABSENT"
        here = self.location(session_id)
        if here == OUTSIDE:
            return False, "SESSION_NOT_PRESENT"
        operation = "ACT" if cap == CAP_ACT else "EXPORT"
        destination = here if cap == CAP_ACT else str(map_to or "").strip()
        if cap == CAP_EXPORT and not destination:
            return False, "EXPORT_TARGET_REQUIRED"
        rule = policy.matching_rule(
            actor_id=actor_id,
            session_id=session_id,
            operation=operation,
            map_from=here,
            map_to=destination,
            purpose=purpose,
            capability=cap,
        )
        return (True, "AUTHORIZED") if rule else (False, "NO_MATCHING_GUARDIAN_RULE")

    def view_telemetry(self, query: TelemetryQuery):
        active_version = str(self.current_policy_version()).strip()
        if not active_version or query.policy_version != active_version:
            return {"status": "DENIED", "reason": "POLICY_VERSION_NOT_CURRENT"}
        policy = self._policy(query.policy_version)
        if policy is None:
            return {"status": "DENIED", "reason": "GUARDIAN_POLICY_ABSENT"}
        here = self.location(query.session_id)
        rule = policy.matching_rule(
            actor_id=query.actor_id,
            session_id=query.session_id,
            operation="VIEW_TELEMETRY",
            map_from=here,
            map_to=here,
            purpose=query.purpose,
            capability=CAP_TELEMETRY,
        )
        if rule is None or query.telemetry_class not in rule.telemetry_classes:
            return {"status": "DENIED", "reason": "TELEMETRY_CAPABILITY_OR_CLASS_MISSING"}

        movement = [r["payload"] for r in self.chronicle.records() if r.get("kind") == "ACCESS_MOVEMENT"]
        if query.telemetry_class == "T0_SESSION_LOCAL":
            rows = [r for r in movement if r.get("session_id") == query.session_id]
            return {"status": "ALLOWED", "class": query.telemetry_class, "records": rows}
        if query.telemetry_class in {"T1_SECURITY_RESTRICTED", "T2_AUDIT_DURABLE"}:
            return {"status": "ALLOWED", "class": query.telemetry_class, "records": movement}

        aggregate: dict[str, int] = {}
        for row in movement:
            key = f"{row.get('map_from')}->{row.get('map_to')}:{row.get('result')}"
            aggregate[key] = aggregate.get(key, 0) + 1
        return {
            "status": "ALLOWED",
            "class": "T3_AGGREGATED",
            "counts": dict(sorted(aggregate.items())),
        }
