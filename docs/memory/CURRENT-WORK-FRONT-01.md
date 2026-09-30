# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Validated implementation:** `98dab44c1af3238c4f342413afc99d1d421f3e90`  
**Full bounded acceptance run:** `36781418888`  
**Acceptance job:** `110112332931`  
**Scope:** current work selection for an explicitly selected PSI memory / visualization task.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**FULL BOUNDED PSI MEMORY RUN: DONE / `PASS_WITH_BOUNDARY`.**

No new separating system defect was found. Therefore:

```text
R9 = NOT_CREATED
```

The next front is **not selected automatically**. The next explicit choice is between:

```text
F5 — model-efficacy comparison
R5 — directed visual relations -> F4.4 SPLIT
```

Do not begin either front as a continuation of the completed integration unit without an explicit selection. R5 remains required before F4.4.

## Closed correctness / integration sequence

| Unit | Status |
|---|---|
| R1 journal continuation | `PASS_WITH_BOUNDARY` |
| R2 cross-journal reconciliation | `PASS_WITH_BOUNDARY` |
| R3 visual digest verification | `PASS_WITH_BOUNDARY` |
| R4 status redaction | `PASS_WITH_BOUNDARY` |
| R6 cost semantics | `PASS_WITH_BOUNDARY` |
| R7 consumed-version receipt | `PASS_WITH_BOUNDARY` |
| R8 no-proposal observation identity | `PASS_WITH_BOUNDARY` |
| full bounded PSI memory run | `PASS_WITH_BOUNDARY` |

Primary evidence:

- [`PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md`](PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md)
- [`PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md`](PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md)
- [`PSI-VIZ-R3-DIGEST-INTEGRITY-01.md`](PSI-VIZ-R3-DIGEST-INTEGRITY-01.md)
- [`PSI-VIZ-R4-STATUS-REDACTION-01.md`](PSI-VIZ-R4-STATUS-REDACTION-01.md)
- [`PSI-MEMORY-R6-COST-SEMANTICS-01.md`](PSI-MEMORY-R6-COST-SEMANTICS-01.md)
- [`PSI-MEMORY-R7-CONSUMED-VERSION-01.md`](PSI-MEMORY-R7-CONSUMED-VERSION-01.md)
- [`PSI-MEMORY-R8-NO-PROPOSAL-IDENTITY-01.md`](PSI-MEMORY-R8-NO-PROPOSAL-IDENTITY-01.md)
- [`PSI-MEMORY-FULL-BOUNDED-RUN-01.md`](PSI-MEMORY-FULL-BOUNDED-RUN-01.md)

## Full-run witness

The accepted episode is pinned to actual project records from:

```text
docs/memory/psi-memory-nodes-01.tsv
docs/memory/psi-memory-edges-01.tsv
```

with the real source state:

```text
P9-I   status = OPEN
P9-I   GATE_FOR   III.13
III.13 status = UNAUTHORIZED
source = docs/control-state.json
```

The episode then exercised, in one composed run:

```text
real V1
-> ACCESS_STEWARD
-> VERIFIED_CONSUMPTION(V1)
-> derived result
-> Curator NO_PROPOSAL identity
-> isolated hypothetical premise change
-> result NEEDS_RECHECK
-> V2 current
-> interruption/restart
-> historical V1 receipt preserved
-> old result remains NEEDS_RECHECK
-> no duplicate movement/COMMIT
-> telemetry still gated
-> Curator replay idempotent / changed payload rejected
```

Acceptance workflow `36781418888`, job `110112332931`, passed the full episode and the R1/R2/R6/R7/R8/F3.3 regressions in the same job.

Two earlier failures during construction of the witness were classified as harness defects, not system counterexamples:

1. an invalid assertion against `ServantDecision` fields belonging to another layer;
2. mutable workspace seeds reused across restart instead of fresh `deepcopy` seeds.

After correcting witness instrumentation/isolation, no system failure remained. Details are frozen in `PSI-MEMORY-FULL-BOUNDED-RUN-01.md`.

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
historical availability != current authority
stored stale result != permission to reuse it
returned payload != semantic understanding
no proposal != not observed
unknown cost != zero cost
visible relation != necessarily visible direction
```

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
FULL PASS_WITH_BOUNDARY
R9   NOT_CREATED
F2.1 PASS_WITH_BOUNDARY; R6 CLOSED
F3.0 CONTRACT_PASS
F3.1 PASS_WITH_BOUNDARY
F3.2 PASS_WITH_BOUNDARY; R7 CLOSED
F3.3 PASS_WITH_BOUNDARY; R8 CLOSED
F3   REFERENCE_CASES_PASS; LOCAL_HARDENING_CLOSED; BOUNDED_COMPOSITION_PASS
F4.0 CONTRACT_PASS
F4.1 PASS_WITH_BOUNDARY
F4.2 PASS_WITH_BOUNDARY; R5 OPEN
F4.3 PASS_WITH_BOUNDARY; R5 OPEN
F4.4 DEFERRED_AFTER_R5
F5   NOT_RUN
```

## Full-run boundary retained

The integration result is one deterministic single-process episode seeded from real PSI records. The `P9-I -> PASSED_INTEGRATION_TEST` transition exists only inside the test runtime and is not a mathematical or canonical status change. Historical versions intentionally remain explicitly retrievable. The guarantee is that stale/current status and dependent invalidation prevent silent reuse, not that history is erased.

The run does not establish live-model understanding, causal use of returned memory, comparative answer quality, total economic advantage, distributed exactly-once semantics or correctness for every possible PSI record. Those stronger efficacy questions belong to F5 or later dedicated tests.

## Selection gate

After this completed unit, choose explicitly:

### F5 — model efficacy

Compare fixed tasks under:

```text
ordinary context
simple retrieval baseline
PSI memory
```

with fixed source revision/model settings/evaluator and separate calibration/held-out sets. Measure correct reuse, correct stale refusal, incorrect accepted answers, source rereads, calls/tokens and end-to-end latency. A cheaper incorrect answer is not a success.

### R5 — visual relation direction

Return to PSI-VIZ. Require explicit typed direction/symmetry so `A -> B` and `B -> A` are visibly distinguishable in SVG and real animation, while symmetric relations remain invariant. R5 remains the gate before F4.4 SPLIT.

No default selection is implied by this pointer.
