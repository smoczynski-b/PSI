# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Reviewed implementation:** `1b1d3ed636f7839af6088b6e54374adc962df458`  
**Independent R7 gate:** `36777234075`  
**Scope:** current work selection for an explicitly selected memory / PSI task.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**NEXT: R8 — define durable identity for observations that produce no proposal.**

The user explicitly reprioritized correctness tests and repairs over the visual
front. R5 remains open and is required before F4.4, but it is not the current
repair unit.

Closed repair units:

- R1 journal continuation — `PASS_WITH_BOUNDARY`;
- R2 cross-journal result reconciliation — `PASS_WITH_BOUNDARY`;
- R3 visual digest verification — `PASS_WITH_BOUNDARY`;
- R4 complete status redaction — `PASS_WITH_BOUNDARY`;
- R6 cost semantics — `PASS_WITH_BOUNDARY`;
- R7 consumed-version receipt — `PASS_WITH_BOUNDARY`.

Evidence:

- [`PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md`](PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md);
- [`PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md`](PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md);
- [`PSI-VIZ-R3-DIGEST-INTEGRITY-01.md`](PSI-VIZ-R3-DIGEST-INTEGRITY-01.md);
- [`PSI-VIZ-R4-STATUS-REDACTION-01.md`](PSI-VIZ-R4-STATUS-REDACTION-01.md);
- [`PSI-MEMORY-R6-COST-SEMANTICS-01.md`](PSI-MEMORY-R6-COST-SEMANTICS-01.md);
- [`PSI-MEMORY-R7-CONSUMED-VERSION-01.md`](PSI-MEMORY-R7-CONSUMED-VERSION-01.md).

R7 was reproduced before correction by run `36776680607`, job `110096241121`:
a read of `version:M2:1` could still be attributed as usage of `version:M2:2`
merely because both versions named map `M2`. The implementation at
`77d67e3fa3c433f99a9db01ded271ef96d3d2fa8` introduced typed
`MAP_ASSOCIATION` versus `VERIFIED_CONSUMPTION` evidence and durable consumption
receipts carrying version, content digest and source revision. Acceptance
revision `1b1d3ed636f7839af6088b6e54374adc962df458` passed the R7 witness, F3.2
and archive runtime in `36777234075`; independent F3.0–F3.2/access/Servant/
institution regressions passed in `36777234008`, and R1/WAL regressions in
`36777234023`.

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
returned payload != semantic understanding
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
| R7 consumed-version receipt | DONE / PASS_WITH_BOUNDARY | association and exact returned version are distinct; wrong same-map version rejected for verified claim; restart preserves receipt |
| **R8 no-proposal observation identity** | **P2 / NEXT** | ID scope defined and below-threshold changed-payload replay tested before/after restart |
| full PSI memory run | after R8 | one bounded run on real PSI records passes stale-premise, interruption and restart checks |
| F5 model comparison | after hardening/full run | fixed-task comparison: ordinary context vs simple retrieval vs PSI memory; measure correctness, stale refusal, rereads, calls/tokens and end-to-end latency |
| R5 directed visual relations | DEFERRED / before F4.4 | reversing a directed edge is visibly distinguishable in SVG and actual animation; symmetry explicit |
| F4.4 typed SPLIT adapter | DEFERRED_AFTER_R5 | typed semantic before/after diff and real render pass |

R8 blocks only the stronger observation-identity claim. Do not create a parallel
audit registry.

## R8 handoff

### Object

The Curator currently has a stronger collision guarantee for observations that
produce a proposal than for observations that remain below threshold. The audit
found that a below-threshold observation can leave no durable identity record;
therefore reuse of the same observation identifier with changed metrics may be
accepted later if the changed payload crosses a proposal threshold.

The unresolved question is the scope of the identifier:

```text
Does observation_id identify every evaluated observation,
or only observations that produce proposals?
```

The runtime contract must choose one interpretation explicitly. It must not claim
the stronger first interpretation while persisting identity only for the second.

### Separating witness

Use one observation identifier `O`:

```text
1. O + payload A -> below threshold -> no proposal
2. same O + payload B, B != A -> evaluate again
3. restart
4. replay same-id cases
```

Required tests if `observation_id` identifies **all** observations:

1. the first below-threshold evaluation leaves a bounded durable outcome;
2. same ID + same payload is idempotent;
3. same ID + changed payload is rejected before restart;
4. restart preserves the fingerprint/outcome;
5. same ID + changed payload is still rejected after restart;
6. no-proposal persistence does not create a proposal, execute restructuring or
   enlarge Curator authority.

If instead the identifier is intentionally proposal-only, narrow and rename the
contract so that no stronger collision guarantee is stated for all observations.

### Correction constraint

Do not turn a below-threshold observation into a proposal merely to obtain
identity. Preserve the distinction:

```text
observed + no proposal
!=
not observed
!=
proposal emitted
```

### Stop

Stop R8 when the selected ID semantics, separating witness, restart case and
affected Curator/WAL regressions pass. Do not begin the full PSI memory run in
the same repair unit.

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
R7   PASS_WITH_BOUNDARY
F2.1 PASS_WITH_BOUNDARY; R6 CLOSED
F3.0 CONTRACT_PASS
F3.1 PASS_WITH_BOUNDARY
F3.2 PASS_WITH_BOUNDARY; R7 CLOSED
F3.3 PASS_WITH_BOUNDARY; R8 OPEN
F3   REFERENCE_CASES_PASS; HARDENING_OPEN
F4.0 CONTRACT_PASS
F4.1 PASS_WITH_BOUNDARY
F4.2 PASS_WITH_BOUNDARY; R5 OPEN
F4.3 PASS_WITH_BOUNDARY; R5 OPEN
F4.4 DEFERRED_AFTER_R5
F5   NOT_RUN
```

## R7 boundary retained

`VERIFIED_CONSUMPTION` proves that the typed archive read path returned the
specified version/revision/content digest and that its durable receipt is bound
to the same movement. It does **not** prove that a downstream model inspected
every field, understood the payload, relied on it in reasoning or improved an
answer because of it. Those are later efficacy claims.

## R6 boundary retained

The current meter runs before durable movement. Its returned vector is therefore
a `PREEXECUTION_QUOTE`, not a measurement of work already incurred by commit,
fsync and telemetry. `incurred_cost=None` means unmeasured, not zero. No
cumulative allocation/debit ledger is claimed.

## Visual front retained but deferred

R5 remains necessary because current visible relations do not yet guarantee that
`A -> B` and `B -> A` are distinguishable to the viewer in every claimed visual
consumer. R4 guarantees status redaction but does not close directionality.

After R8 and the bounded full memory run, the visual sequence may resume:

```text
R5 -> F4.4 SPLIT
```

F5 remains a separate model-efficacy experiment. It must not be replaced by a
successful render or by infrastructure regression tests.
