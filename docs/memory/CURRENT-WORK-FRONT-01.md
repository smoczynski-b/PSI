# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Reviewed implementation:** `de68f872362979ae3d4aaf825eb377772727ac8c`  
**Independent R6 gate:** `36776058130`  
**Scope:** current work selection for an explicitly selected memory / PSI task.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**NEXT: R7 — distinguish archive association from verified consumption of a specific version.**

The user explicitly reprioritized correctness tests and repairs over the visual
front. R5 remains open and is required before F4.4, but it is not the current
repair unit.

Closed repair units:

- R1 journal continuation — `PASS_WITH_BOUNDARY`;
- R2 cross-journal result reconciliation — `PASS_WITH_BOUNDARY`;
- R3 visual digest verification — `PASS_WITH_BOUNDARY`;
- R4 complete status redaction — `PASS_WITH_BOUNDARY`;
- R6 cost semantics — `PASS_WITH_BOUNDARY`.

Evidence:

- [`PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md`](PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md);
- [`PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md`](PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md);
- [`PSI-VIZ-R3-DIGEST-INTEGRITY-01.md`](PSI-VIZ-R3-DIGEST-INTEGRITY-01.md);
- [`PSI-VIZ-R4-STATUS-REDACTION-01.md`](PSI-VIZ-R4-STATUS-REDACTION-01.md);
- [`PSI-MEMORY-R6-COST-SEMANTICS-01.md`](PSI-MEMORY-R6-COST-SEMANTICS-01.md).

R6 was first reproduced by workflow run `36775291249`, job `110091543666`:
`cost_meter` returned `compute=3` for a request with estimated `compute=1` and
budget `compute=2`, but the denial result recorded zero cost evidence. The
correction at `de68f872362979ae3d4aaf825eb377772727ac8c` preserves that vector
as a typed `PREEXECUTION_QUOTE`, keeps unmeasured incurred cost as `None`,
declares normalized reference units and requires an explicit scalarization
contract. Independent permanent gate `36776058130` passed the R6 witness, F2.1
ACCESS_STEWARD regression and R2 reconciliation regression.

## Auditor rule — Semantica Rozmowy 03

The audit layer remains binding:

\[
P_i(S)\not\Rightarrow S.
\]

Operationally:

```text
component PASS != system PASS
stored digest != verified consumed payload
archive association != verified version consumption
unknown cost != zero cost
visible relation != necessarily visible direction
```

Each repair is tested at the downstream consumer where its claim is used.

## Ordered correction front

| Unit | Status / dependency | Stop condition |
|---|---|---|
| R0 current instructions | DONE | current pointers agree |
| R1 journal continuation | DONE / PASS_WITH_BOUNDARY | torn-tail continuation and affected regressions pass |
| R2 result reconciliation | DONE / PASS_WITH_BOUNDARY | COMMIT / SERVANT / ACCESS projections reconcile without duplicate mutation or metering |
| R3 visual digest verification | DONE / PASS_WITH_BOUNDARY | stale hashes and contradictory duplicated bindings fail closed at consumers; real render passes |
| R4 complete status redaction | DONE / PASS_WITH_BOUNDARY | hidden node/edge status absent downstream; explicitly allowed status preserved in declared channels |
| R6 cost semantics | DONE / PASS_WITH_BOUNDARY | over-budget quote retained; quote/incurred/unknown distinguished; units and scalarization explicit |
| **R7 consumed-version receipt** | **P2 / NEXT** | association distinguished from verified version consumption; two-version witness rejects attribution to the unconsumed version and survives restart |
| R8 no-proposal observation identity | P2 / after R7 | ID scope defined and below-threshold changed-payload replay tested across restart |
| full PSI memory run | after R7/R8 | one bounded run on real PSI records passes stale-premise, interruption and restart checks |
| F5 model comparison | after hardening/full run | fixed-task comparison: ordinary context vs simple retrieval vs PSI memory; measure correctness, stale refusal, rereads, calls/tokens and end-to-end latency |
| R5 directed visual relations | DEFERRED / before F4.4 | reversing a directed edge is visibly distinguishable in SVG and actual animation; symmetry explicit |
| F4.4 typed SPLIT adapter | DEFERRED_AFTER_R5 | typed semantic before/after diff and real render pass |

R7/R8 block only their stronger claims. Do not create a parallel audit registry.

## R7 handoff

### Object

Current usage validation can establish that an archive manifest names the map
associated with a movement. The movement record does not prove which historical
archive version/revision the consumer actually read.

Therefore the current legal claim is only:

```text
movement associated with archive map M
```

and not yet:

```text
consumer used archive version V of M
```

### Separating witness

Construct two historical versions of the same map:

```text
M@v1  digest = H1
M@v2  digest = H2
```

with one verified read/use action consuming exactly one of them.

Required tests:

1. the use receipt binds map id, version/revision and content digest;
2. attribution to the actually consumed version is accepted;
3. attribution to the other historical version is rejected;
4. restart preserves the binding;
5. telemetry/access restrictions still apply after restart;
6. association-only records remain labelled as association-only rather than
   silently upgraded to verified consumption.

### Correction constraint

Do not infer version consumption from current map identity, CURRENT pointers or
movement destination alone. Stronger attribution requires a verified receipt at
the read/use boundary.

### Stop

Stop R7 when the two-version witness and affected archive/access/restart
regressions pass. Do not begin R8 in the same repair unit.

## Recorded implementation state

```text
F0   PASS_WITH_BOUNDARY
F1   PASS_WITH_BOUNDARY
F2.0 CONTRACT_PASS
R1   PASS_WITH_BOUNDARY
R2   PASS_WITH_BOUNDARY
R3   PASS_WITH_BOUNDARY
R4   PASS_WITH_BOUNDARY
R6   PASS_WITH_BOUNDARY
F2.1 PASS_WITH_BOUNDARY; R6 CLOSED
F3.0 CONTRACT_PASS
F3.1 PASS_WITH_BOUNDARY
F3.2 PASS_WITH_BOUNDARY; R7 OPEN
F3.3 PASS_WITH_BOUNDARY; R8 OPEN
F3   REFERENCE_CASES_PASS; HARDENING_OPEN
F4.0 CONTRACT_PASS
F4.1 PASS_WITH_BOUNDARY
F4.2 PASS_WITH_BOUNDARY; R5 OPEN
F4.3 PASS_WITH_BOUNDARY; R5 OPEN
F4.4 DEFERRED_AFTER_R5
F5   NOT_RUN
```

## R6 boundary retained

The current meter runs before durable movement. Its returned vector is therefore
a `PREEXECUTION_QUOTE`, not a measurement of work already incurred by commit,
fsync and telemetry. `incurred_cost=None` means unmeasured, not zero.

The declared cost units are normalized reference units. Scalar comparison uses
a named `CostScalarization` contract. No cumulative allocation/debit ledger is
claimed. R6 is sufficient to prevent the earlier semantic collapse, not to
establish a full economic evaluation of PSI.

## Visual front retained but deferred

R5 remains necessary because current visible relations do not yet guarantee that
`A -> B` and `B -> A` are distinguishable to the viewer in every claimed visual
consumer. R4 guarantees status redaction but does not close directionality.

When the correction front R7/R8 and bounded full memory run are complete, the
visual sequence can resume:

```text
R5 -> F4.4 SPLIT
```

F5 remains a separate model-efficacy experiment. It must not be replaced by a
successful render or by infrastructure regression tests.
