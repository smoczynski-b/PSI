# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Reviewed implementation:** `5f30ae6a1ac58c4d3ef346445c5ba9057d3d0a24`  
**Independent R8 gate:** `36778081234`  
**Scope:** current work selection for an explicitly selected memory / PSI task.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**NEXT: bounded full PSI memory run on real PSI records.**

The correctness-hardening sequence R6 -> R7 -> R8 is closed. The next step is
not another local repair but one bounded integration run that exercises the
already hardened memory path across stale-premise handling, interruption and
restart. R5 remains open and is required before F4.4, but the visual front stays
deferred until this memory run is complete.

Closed repair units:

- R1 journal continuation — `PASS_WITH_BOUNDARY`;
- R2 cross-journal result reconciliation — `PASS_WITH_BOUNDARY`;
- R3 visual digest verification — `PASS_WITH_BOUNDARY`;
- R4 complete status redaction — `PASS_WITH_BOUNDARY`;
- R6 cost semantics — `PASS_WITH_BOUNDARY`;
- R7 consumed-version receipt — `PASS_WITH_BOUNDARY`;
- R8 no-proposal observation identity — `PASS_WITH_BOUNDARY`.

Evidence:

- [`PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md`](PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md);
- [`PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md`](PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md);
- [`PSI-VIZ-R3-DIGEST-INTEGRITY-01.md`](PSI-VIZ-R3-DIGEST-INTEGRITY-01.md);
- [`PSI-VIZ-R4-STATUS-REDACTION-01.md`](PSI-VIZ-R4-STATUS-REDACTION-01.md);
- [`PSI-MEMORY-R6-COST-SEMANTICS-01.md`](PSI-MEMORY-R6-COST-SEMANTICS-01.md);
- [`PSI-MEMORY-R7-CONSUMED-VERSION-01.md`](PSI-MEMORY-R7-CONSUMED-VERSION-01.md);
- [`PSI-MEMORY-R8-NO-PROPOSAL-IDENTITY-01.md`](PSI-MEMORY-R8-NO-PROPOSAL-IDENTITY-01.md).

R8 was reproduced before correction by workflow `36777747371`, job
`110099835492`: after a below-threshold `OBS-R8` left no durable record, the
same identifier with changed metrics could be accepted and cross the proposal
threshold. Implementation `ea4e1b7e0837a7769f9edfbb780f051c4cc5221e`
persists a bounded, Servant-gated `NO_PROPOSAL` identity for every first-seen
below-threshold observation. Acceptance revision
`5f30ae6a1ac58c4d3ef346445c5ba9057d3d0a24` passed the dedicated R8 gate
`36778081234`, independent F3.0-F3.3/access/Servant/institution integration gate
`36778081173`, and independent R1/WAL gate `36778081276`.

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
no proposal != not observed
unknown cost != zero cost
visible relation != necessarily visible direction
```

Each stronger claim must be tested at the downstream consumer where it is used.

## Ordered correction / validation front

| Unit | Status / dependency | Stop condition |
|---|---|---|
| R0 current instructions | DONE | current pointers agree |
| R1 journal continuation | DONE / PASS_WITH_BOUNDARY | torn-tail continuation and affected regressions pass |
| R2 result reconciliation | DONE / PASS_WITH_BOUNDARY | COMMIT / SERVANT / ACCESS projections reconcile without duplicate mutation or metering |
| R3 visual digest verification | DONE / PASS_WITH_BOUNDARY | stale hashes and contradictory duplicated bindings fail closed at consumers; real render passes |
| R4 complete status redaction | DONE / PASS_WITH_BOUNDARY | hidden node/edge status absent downstream; explicitly allowed status preserved in declared channels |
| R6 cost semantics | DONE / PASS_WITH_BOUNDARY | over-budget quote retained; quote/incurred/unknown distinguished; units and scalarization explicit |
| R7 consumed-version receipt | DONE / PASS_WITH_BOUNDARY | association and exact returned version are distinct; wrong same-map version rejected for verified claim; restart preserves receipt |
| R8 no-proposal observation identity | DONE / PASS_WITH_BOUNDARY | all evaluated observation IDs are durable; changed payload rejected before/after restart |
| **full PSI memory run** | **NEXT** | one bounded run on real PSI records passes stale-premise, interruption and restart checks with receipts/reconciliation preserved |
| F5 model comparison | after full run | fixed-task comparison: ordinary context vs simple retrieval vs PSI memory; measure correctness, stale refusal, rereads, calls/tokens and end-to-end latency |
| R5 directed visual relations | DEFERRED / before F4.4 | reversing a directed edge is visibly distinguishable in SVG and actual animation; symmetry explicit |
| F4.4 typed SPLIT adapter | DEFERRED_AFTER_R5 | typed semantic before/after diff and real render pass |

No new repair number is created for the full run unless that run exposes a new
separating defect. Do not create a parallel audit registry.

## Full PSI memory run handoff

### Object

Local hardening tests now cover journal continuation, cross-journal
reconciliation, cost semantics, exact archive-version consumption and Curator
observation identity. They still do not by themselves prove that one bounded
end-to-end memory episode preserves these guarantees when composed.

The next run must therefore use an actual bounded PSI record set rather than a
new synthetic component fixture.

### Required episode

At minimum the episode must contain:

```text
A. a valid premise/version consumed through the typed archive path;
B. a later record that invalidates or supersedes one relevant premise;
C. an interruption/restart boundary after durable writes;
D. a resumed read/action that must not silently reuse the stale premise;
E. exact archive-consumption and movement/result bindings after restart;
F. at least one Curator observation whose no-proposal/proposal identity remains
   stable across replay.
```

### Required checks

1. stale premise is refused, invalidated or explicitly marked non-current rather
   than silently reused;
2. restart reconstructs the same legal durable state without duplicate mutation,
   movement, metering, proposal or no-proposal observation record;
3. a verified archive-consumption claim names the exact returned version/digest;
4. association-only evidence is not upgraded to verified consumption;
5. quote/incurred/unknown cost semantics remain intact;
6. Curator same-ID/different-payload reuse remains blocked;
7. the final system-level claim is no stronger than the composed evidence.

### Stop

Stop the full run when one bounded episode and its restart replay pass all listed
checks. If a separating failure appears, classify it and open a repair unit only
for that new defect. Do not begin F5 or R5 in the same unit.

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
R8   PASS_WITH_BOUNDARY
F2.1 PASS_WITH_BOUNDARY; R6 CLOSED
F3.0 CONTRACT_PASS
F3.1 PASS_WITH_BOUNDARY
F3.2 PASS_WITH_BOUNDARY; R7 CLOSED
F3.3 PASS_WITH_BOUNDARY; R8 CLOSED
F3   REFERENCE_CASES_PASS; LOCAL_HARDENING_CLOSED; FULL_RUN_NEXT
F4.0 CONTRACT_PASS
F4.1 PASS_WITH_BOUNDARY
F4.2 PASS_WITH_BOUNDARY; R5 OPEN
F4.3 PASS_WITH_BOUNDARY; R5 OPEN
F4.4 DEFERRED_AFTER_R5
F5   NOT_RUN
```

## R8 boundary retained

`observation_id` now identifies every successfully evaluated observation within
one Curator chronicle. The fingerprint binds district, metrics, observation time
and planning-policy version. A durable `NO_PROPOSAL` record proves that this
payload was evaluated under the current planner contract and produced no
proposal. It does not prove sensor authenticity, metric truth, threshold wisdom
or distributed uniqueness of the identifier.

## R7 boundary retained

`VERIFIED_CONSUMPTION` proves that the typed archive read path returned the
specified version/revision/content digest and that its durable receipt is bound
to the same movement. It does not prove downstream semantic understanding or
causal use in reasoning.

## R6 boundary retained

The current meter runs before durable movement. Its returned vector is a
`PREEXECUTION_QUOTE`, not a measurement of work already incurred by commit,
fsync and telemetry. `incurred_cost=None` means unmeasured, not zero. No
cumulative allocation/debit ledger is claimed.

## Visual front retained but deferred

R5 remains necessary because current visible relations do not yet guarantee that
`A -> B` and `B -> A` are distinguishable to the viewer in every claimed visual
consumer. R4 guarantees status redaction but does not close directionality.

After the bounded full memory run, the next selection is made explicitly among:

```text
F5 model comparison
R5 -> F4.4 SPLIT visual sequence
```

A successful infrastructure run does not substitute for F5 efficacy comparison.
