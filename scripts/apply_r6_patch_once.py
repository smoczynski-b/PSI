#!/usr/bin/env python3
from pathlib import Path

p = Path("scripts/access_steward_runtime.py")
text = p.read_text(encoding="utf-8")


def one(old: str, new: str, label: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, got {count}")
    text = text.replace(old, new, 1)


one(
    "from typing import Callable, Iterable\n",
    "from typing import Callable, Iterable, Mapping\n",
    "typing import",
)

marker = "\n\n@dataclass(frozen=True)\nclass CostVector:\n"
if text.count(marker) != 1:
    raise SystemExit("CostVector marker mismatch")
contract = '''

COST_COMPONENTS = (
    "compute", "transfer", "context", "latency", "disclosure",
    "synchronization", "risk",
)
COST_COMPONENT_UNITS = {
    "compute": "normalized_compute_unit",
    "transfer": "normalized_transfer_unit",
    "context": "normalized_context_unit",
    "latency": "normalized_latency_unit",
    "disclosure": "normalized_disclosure_unit",
    "synchronization": "normalized_synchronization_unit",
    "risk": "normalized_risk_unit",
}
COST_EVIDENCE_UNMEASURED = "UNMEASURED"
COST_EVIDENCE_PREEXECUTION_QUOTE = "PREEXECUTION_QUOTE"


@dataclass(frozen=True)
class CostScalarization:
    """Explicit normalization/weighting contract for heterogeneous cost axes."""

    contract_id: str
    normalization: Mapping[str, float]
    weights: Mapping[str, float]

    def __post_init__(self):
        cid = str(self.contract_id).strip()
        if not cid:
            raise ValueError("cost scalarization contract_id is required")
        object.__setattr__(self, "contract_id", cid)
        normalization = {str(k): float(v) for k, v in self.normalization.items()}
        weights = {str(k): float(v) for k, v in self.weights.items()}
        if set(normalization) != set(COST_COMPONENTS) or set(weights) != set(COST_COMPONENTS):
            raise ValueError("cost scalarization must cover every cost component exactly once")
        for key in COST_COMPONENTS:
            if not math.isfinite(normalization[key]) or normalization[key] <= 0:
                raise ValueError(f"normalization[{key}] must be finite and positive")
            if not math.isfinite(weights[key]) or weights[key] < 0:
                raise ValueError(f"weights[{key}] must be finite and non-negative")
        object.__setattr__(self, "normalization", dict(normalization))
        object.__setattr__(self, "weights", dict(weights))


DEFAULT_COST_SCALARIZATION = CostScalarization(
    contract_id="ACCESS-COST-NORM-01",
    normalization={key: 1.0 for key in COST_COMPONENTS},
    weights={key: 1.0 for key in COST_COMPONENTS},
)
'''
text = text.replace(marker, contract + marker, 1)

one(
    '''    @property
    def l1(self) -> float:
        return sum(self.as_dict().values())

    def as_dict(self) -> dict[str, float]:
''',
    '''    def is_zero(self) -> bool:
        return all(value == 0.0 for value in self.as_dict().values())

    def scalar_total(self, contract: CostScalarization) -> float:
        if not isinstance(contract, CostScalarization):
            raise TypeError("scalar_total requires CostScalarization")
        values = self.as_dict()
        return sum(
            contract.weights[key] * values[key] / contract.normalization[key]
            for key in COST_COMPONENTS
        )

    @property
    def l1(self) -> float:
        # Compatibility shorthand under an explicit normalization/weighting
        # contract. It is not a claim about physical total cost.
        return self.scalar_total(DEFAULT_COST_SCALARIZATION)

    @staticmethod
    def units() -> dict[str, str]:
        return dict(COST_COMPONENT_UNITS)

    def as_dict(self) -> dict[str, float]:
''',
    "CostVector scalarization",
)

one(
    '''class MovementDecision:
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
''',
    '''class MovementDecision:
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
    cost_evidence_kind: str = COST_EVIDENCE_UNMEASURED
    incurred_cost: CostVector | None = None

    @property
    def quoted_cost(self) -> CostVector | None:
        if self.cost_evidence_kind == COST_EVIDENCE_PREEXECUTION_QUOTE:
            return self.actual_cost
        return None
''',
    "MovementDecision evidence",
)

one(
    '''class CompletedRequest:
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
''',
    '''class CompletedRequest:
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
    cost_evidence_kind: str = COST_EVIDENCE_UNMEASURED
    incurred_cost: CostVector | None = None
''',
    "CompletedRequest evidence",
)

one(
    '''                    txid=str(payload.get("txid", "")),
                )
''',
    '''                    txid=str(payload.get("txid", "")),
                    cost_evidence_kind=str(payload.get("cost_evidence_kind", COST_EVIDENCE_UNMEASURED)),
                    incurred_cost=(
                        CostVector(**payload["incurred_cost"])
                        if isinstance(payload.get("incurred_cost"), dict)
                        else None
                    ),
                )
''',
    "load completed cost evidence",
)

one(
    '''                    "actual_cost": dict(payload["actual_cost"]),
                    "result": "MOVED",
''',
    '''                    "actual_cost": dict(payload["actual_cost"]),
                    "cost_evidence_kind": str(payload.get("cost_evidence_kind", COST_EVIDENCE_PREEXECUTION_QUOTE)),
                    "incurred_cost": payload.get("incurred_cost"),
                    "cost_units": dict(COST_COMPONENT_UNITS),
                    "scalarization_contract_id": DEFAULT_COST_SCALARIZATION.contract_id,
                    "result": "MOVED",
''',
    "reconcile movement evidence",
)

one(
    '''                "actual_cost": actual.as_dict(),
                "servant_disposition": servant_result.disposition,
''',
    '''                "actual_cost": actual.as_dict(),
                "cost_evidence_kind": str(payload.get("cost_evidence_kind", COST_EVIDENCE_PREEXECUTION_QUOTE)),
                "incurred_cost": payload.get("incurred_cost"),
                "cost_units": dict(COST_COMPONENT_UNITS),
                "scalarization_contract_id": DEFAULT_COST_SCALARIZATION.contract_id,
                "servant_disposition": servant_result.disposition,
''',
    "reconcile result evidence",
)

one(
    '''                txid=txid,
            )

    def _observed''',
    '''                txid=txid,
                cost_evidence_kind=str(payload.get("cost_evidence_kind", COST_EVIDENCE_PREEXECUTION_QUOTE)),
                incurred_cost=(
                    CostVector(**payload["incurred_cost"])
                    if isinstance(payload.get("incurred_cost"), dict)
                    else None
                ),
            )

    def _observed''',
    "reconcile completed evidence",
)

one(
    '''            "estimated_cost": request.estimated_cost.as_dict(),
            "actual_cost": actual.as_dict(),
            "location_before": before,
''',
    '''            "estimated_cost": request.estimated_cost.as_dict(),
            "actual_cost": actual.as_dict(),
            "cost_evidence_kind": COST_EVIDENCE_PREEXECUTION_QUOTE,
            "incurred_cost": None,
            "cost_units": dict(COST_COMPONENT_UNITS),
            "scalarization_contract_id": DEFAULT_COST_SCALARIZATION.contract_id,
            "location_before": before,
''',
    "prepared quote semantics",
)

one(
    '''        actual_cost: CostVector | None = None,
        servant_disposition: str = "",
''',
    '''        actual_cost: CostVector | None = None,
        cost_evidence_kind: str = COST_EVIDENCE_UNMEASURED,
        incurred_cost: CostVector | None = None,
        servant_disposition: str = "",
''',
    "finish signature evidence",
)

one(
    '''            actual_cost=actual,
            servant_disposition=servant_disposition,
''',
    '''            actual_cost=actual,
            cost_evidence_kind=cost_evidence_kind,
            incurred_cost=incurred_cost,
            servant_disposition=servant_disposition,
''',
    "decision evidence fields",
)

one(
    '''            "estimated_cost": request.estimated_cost.as_dict(),
            "actual_cost": actual.as_dict(),
            "servant_disposition": servant_disposition,
''',
    '''            "estimated_cost": request.estimated_cost.as_dict(),
            "actual_cost": actual.as_dict(),
            "cost_evidence_kind": cost_evidence_kind,
            "incurred_cost": incurred_cost.as_dict() if incurred_cost is not None else None,
            "cost_units": dict(COST_COMPONENT_UNITS),
            "scalarization_contract_id": DEFAULT_COST_SCALARIZATION.contract_id,
            "servant_disposition": servant_disposition,
''',
    "result payload evidence",
)

one(
    '''                actual_cost=actual,
                servant_disposition=servant_disposition,
''',
    '''                actual_cost=actual,
                cost_evidence_kind=cost_evidence_kind,
                incurred_cost=incurred_cost,
                servant_disposition=servant_disposition,
''',
    "completed evidence fields",
)

one(
    '''            actual_cost=prior.actual_cost,
            servant_disposition=prior.servant_disposition,
''',
    '''            actual_cost=prior.actual_cost,
            cost_evidence_kind=prior.cost_evidence_kind,
            incurred_cost=prior.incurred_cost,
            servant_disposition=prior.servant_disposition,
''',
    "replay evidence",
)

one(
    '''    def _deny(self, request: MovementRequest, before: str, reason: str) -> MovementDecision:
        return self._finish(
            request,
            disposition="DENY_ACCESS",
            reason_code=reason,
            before=before,
            after=before,
        )
''',
    '''    def _deny(
        self,
        request: MovementRequest,
        before: str,
        reason: str,
        *,
        cost_evidence: CostVector | None = None,
        cost_evidence_kind: str = COST_EVIDENCE_UNMEASURED,
    ) -> MovementDecision:
        return self._finish(
            request,
            disposition="DENY_ACCESS",
            reason_code=reason,
            before=before,
            after=before,
            actual_cost=cost_evidence,
            cost_evidence_kind=cost_evidence_kind,
        )
''',
    "deny evidence",
)

one(
    '''    def _stop(self, request: MovementRequest, before: str, reason: str, *, remember: bool = True) -> MovementDecision:
        self.chronicle.append("ESCALATE", request.request_id, {
''',
    '''    def _stop(
        self,
        request: MovementRequest,
        before: str,
        reason: str,
        *,
        remember: bool = True,
        cost_evidence: CostVector | None = None,
        cost_evidence_kind: str = COST_EVIDENCE_UNMEASURED,
    ) -> MovementDecision:
        self.chronicle.append("ESCALATE", request.request_id, {
''',
    "stop signature evidence",
)

one(
    '''            after=before,
            remember=remember,
        )

    @staticmethod
''',
    '''            after=before,
            actual_cost=cost_evidence,
            cost_evidence_kind=cost_evidence_kind,
            remember=remember,
        )

    @staticmethod
''',
    "stop finish evidence",
)

one(
    "        if changed_location and request.estimated_cost.l1 <= 0:\n",
    "        if changed_location and request.estimated_cost.is_zero():\n",
    "estimated zero check",
)

one(
    '''        if changed_location and actual.l1 <= 0:
            return self._stop(request, before, "CROSS_MAP_ZERO_ACTUAL_COST")
        if not actual.within(request.budget):
            return self._deny(request, before, "ACTUAL_COST_EXCEEDS_BUDGET")
''',
    '''        if changed_location and actual.is_zero():
            return self._stop(
                request, before, "CROSS_MAP_ZERO_QUOTED_COST",
                cost_evidence=actual,
                cost_evidence_kind=COST_EVIDENCE_PREEXECUTION_QUOTE,
            )
        if not actual.within(request.budget):
            return self._deny(
                request, before, "QUOTED_COST_EXCEEDS_BUDGET",
                cost_evidence=actual,
                cost_evidence_kind=COST_EVIDENCE_PREEXECUTION_QUOTE,
            )
''',
    "quote budget semantics",
)

one(
    '''                actual_cost=actual,
                servant_disposition=servant_decision.disposition,
''',
    '''                actual_cost=actual,
                cost_evidence_kind=COST_EVIDENCE_PREEXECUTION_QUOTE,
                servant_disposition=servant_decision.disposition,
''',
    "servant reject quote evidence",
)

one(
    '            return self._stop(request, before, "DURABLE_PRESENCE_DIVERGENCE")\n',
    '''            return self._stop(
                request, before, "DURABLE_PRESENCE_DIVERGENCE",
                cost_evidence=actual,
                cost_evidence_kind=COST_EVIDENCE_PREEXECUTION_QUOTE,
            )
''',
    "presence divergence quote evidence",
)

one(
    '''            "estimated_cost": request.estimated_cost.as_dict(),
            "actual_cost": actual.as_dict(),
            "result": "MOVED",
''',
    '''            "estimated_cost": request.estimated_cost.as_dict(),
            "actual_cost": actual.as_dict(),
            "cost_evidence_kind": COST_EVIDENCE_PREEXECUTION_QUOTE,
            "incurred_cost": None,
            "cost_units": dict(COST_COMPONENT_UNITS),
            "scalarization_contract_id": DEFAULT_COST_SCALARIZATION.contract_id,
            "result": "MOVED",
''',
    "movement quote semantics",
)

one(
    '''            actual_cost=actual,
            servant_disposition=servant_decision.disposition,
            servant_reason=servant_decision.reason_code,
            txid=command.txid,
        )

    def check_capability''',
    '''            actual_cost=actual,
            cost_evidence_kind=COST_EVIDENCE_PREEXECUTION_QUOTE,
            servant_disposition=servant_decision.disposition,
            servant_reason=servant_decision.reason_code,
            txid=command.txid,
        )

    def check_capability''',
    "allow quote evidence",
)

p.write_text(text, encoding="utf-8")

q = Path("scripts/test_access_steward_runtime.py")
t = q.read_text(encoding="utf-8")
replacements = {
    'assert d.reason_code == "ACTUAL_COST_EXCEEDS_BUDGET"':
        'assert d.reason_code == "QUOTED_COST_EXCEEDS_BUDGET"',
    'assert d.reason_code == "CROSS_MAP_ZERO_ACTUAL_COST"':
        'assert d.reason_code == "CROSS_MAP_ZERO_QUOTED_COST"',
    'assert d.actual_cost.l1 > 0':
        'assert d.quoted_cost is not None and not d.quoted_cost.is_zero()',
}
for old, new in replacements.items():
    if t.count(old) != 1:
        raise SystemExit(f"F2.1 test replacement mismatch: {old!r}")
    t = t.replace(old, new, 1)
q.write_text(t, encoding="utf-8")

r = Path("scripts/test_access_cost_semantics_r6.py")
u = r.read_text(encoding="utf-8")
if "COST_COMPONENT_UNITS" not in u:
    u = u.replace(
        "    CAP_ENTER,\n)",
        "    CAP_ENTER,\n    COST_COMPONENT_UNITS,\n    COST_EVIDENCE_PREEXECUTION_QUOTE,\n    DEFAULT_COST_SCALARIZATION,\n)",
        1,
    )
u = u.replace(
    'assert decision.reason_code == "ACTUAL_COST_EXCEEDS_BUDGET", decision',
    'assert decision.reason_code == "QUOTED_COST_EXCEEDS_BUDGET", decision',
    1,
)
u = u.replace(
    "        assert decision.actual_cost.compute == 3, decision\n",
    "        assert decision.actual_cost.compute == 3, decision\n"
    "        assert decision.cost_evidence_kind == COST_EVIDENCE_PREEXECUTION_QUOTE\n"
    "        assert decision.quoted_cost is not None\n"
    "        assert decision.quoted_cost.compute == 3\n"
    "        assert decision.incurred_cost is None\n"
    "        assert CostVector.units() == COST_COMPONENT_UNITS\n"
    "        assert cv(2).scalar_total(DEFAULT_COST_SCALARIZATION) == 2.0\n",
    1,
)
u = u.replace(
    '        assert result_rows[0]["payload"]["actual_cost"]["compute"] == 3\n',
    '        payload = result_rows[0]["payload"]\n'
    '        assert payload["actual_cost"]["compute"] == 3\n'
    '        assert payload["cost_evidence_kind"] == COST_EVIDENCE_PREEXECUTION_QUOTE\n'
    '        assert payload["incurred_cost"] is None\n'
    '        assert payload["cost_units"] == COST_COMPONENT_UNITS\n'
    '        assert payload["scalarization_contract_id"] == DEFAULT_COST_SCALARIZATION.contract_id\n',
    1,
)
r.write_text(u, encoding="utf-8")

print("R6 bounded patch applied")
