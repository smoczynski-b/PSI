# PSI-MEMORY-R6-COST-SEMANTICS-01

**Status:** `PASS_WITH_BOUNDARY`  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Implementation:** `de68f872362979ae3d4aaf825eb377772727ac8c`  
**Independent verification:** workflow run `36776058130`

## Object

R6 repairs the semantics of cost evidence in `ACCESS_STEWARD`.

Before R6 the runtime called `cost_meter` before durable movement but labelled
its return as `actual_cost`. When that returned vector exceeded the request
budget, the denial path discarded it and `_finish` wrote a zero vector. The
same type also exposed `l1` as an unqualified sum of seven heterogeneous cost
components.

The repair does not introduce a cumulative budget ledger and does not claim to
measure the complete end-to-end cost of a movement.

## FAIL-before witness

The separating case was executed before correction:

```text
estimated compute = 1
budget compute    = 2
cost_meter return = 3
```

Expected boundary behaviour:

```text
DENY
location unchanged
no durable movement COMMIT
returned cost evidence retained
```

Workflow run `36775291249`, job `110091543666`, failed exactly because the
returned decision contained:

```text
actual_cost.compute = 0
```

although `cost_meter` had returned `compute=3`.

This establishes the R6 defect by execution rather than source inspection.

## Correction

### 1. Cost evidence is typed by meaning

The pre-movement meter return is now explicitly classified as:

```text
PREEXECUTION_QUOTE
```

It is not treated as proof of cost already incurred by commit/fsync/telemetry.
For compatibility the historical `actual_cost` vector remains present, but its
meaning is carried by `cost_evidence_kind`; `quoted_cost` exposes it only when
that kind is `PREEXECUTION_QUOTE`.

A separate field:

```text
incurred_cost
```

is `None` when incurred work has not been measured. Therefore:

```text
unknown != zero
```

### 2. Over-budget evidence is preserved

For the separating witness the corrected result is:

```text
DENY_ACCESS
QUOTED_COST_EXCEEDS_BUDGET
quoted_cost.compute = 3
incurred_cost = None
location = OUTSIDE
no movement COMMIT
```

The same evidence is retained in the durable ACCESS result record.

### 3. Zero checks no longer depend on scalar addition

Cross-map zero checks use componentwise zero detection rather than the old
unqualified `l1 <= 0` scalar test.

### 4. Units and scalarization are explicit

Every cost component now has a declared reference unit. The present reference
runtime uses normalized units:

```text
compute         normalized_compute_unit
transfer        normalized_transfer_unit
context         normalized_context_unit
latency         normalized_latency_unit
disclosure      normalized_disclosure_unit
synchronization normalized_synchronization_unit
risk            normalized_risk_unit
```

Scalar totals require an explicit `CostScalarization` contract containing a
normalization factor and weight for every component. The reference compatibility
contract is named:

```text
ACCESS-COST-NORM-01
```

The retained `CostVector.l1` is only a shorthand under that declared reference
contract; it is not presented as a physical or universal total-cost metric.

## Verification

The independent permanent R6 workflow run `36776058130` completed successfully.
Its job executed and passed:

1. `R6 separating witness`;
2. `F2.1 access steward regression`;
3. `R2 reconciliation regression`.

Thus the R6 correction did not regress the established ACCESS_STEWARD behaviour
or the cross-journal reconciliation repair.

## Boundary

R6 establishes a coherent reference semantics for the available cost evidence;
it does **not** establish complete cost measurement.

Still outside the claim:

- post-execution measurement of durable commit, fsync and telemetry work;
- physical calibration of the normalized units;
- a universal weighting of heterogeneous cost axes;
- cumulative allocation/debit accounting across requests or sessions;
- distributed execution or multi-process accounting;
- model-quality or cost-benefit superiority of PSI memory.

Therefore F5 may use R6 only with the stated evidence classes and declared
scalarization. A full end-to-end cost claim requires additional measurement,
not reinterpretation of the pre-execution quote.

## Result

```text
R6 = PASS_WITH_BOUNDARY
```

The next non-visual hardening unit is R7: distinguish archive-map association
from verified consumption of a specific version/revision and content digest.
