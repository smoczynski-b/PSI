# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Validated implementation:** `98dab44c1af3238c4f342413afc99d1d421f3e90`  
**Full bounded acceptance run:** `36781418888`  
**Acceptance job:** `110112332931`  
**Scope:** current work selection for PSI memory / model efficacy / visualization.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**F5 — MODEL EFFICACY: SELECTED.**

The user explicitly selected F5 after the bounded full memory run. R5 remains open and is still required before F4.4, but visualization is deferred while F5 is active.

Current state:

```text
FULL_BOUNDED_RUN = PASS_WITH_BOUNDARY
R9 = NOT_CREATED
F5 = SELECTED / PREPARED / MODEL_RUN_PENDING
R5 = OPEN / DEFERRED
F4.4 = DEFERRED_AFTER_R5
```

Primary F5 contract:

- [`PSI-MEMORY-F5-MODEL-EFFICACY-01.md`](PSI-MEMORY-F5-MODEL-EFFICACY-01.md)

## F5 question

F5 must test the stronger claim not established by infrastructure tests:

```text
does PSI memory improve model answers compared with
A ordinary bounded context
B simple lexical retrieval
C PSI memory retrieval
```

under fixed source revision, fixed tasks, fixed model/settings, fixed evaluator and equal input-budget rules.

A cheaper incorrect answer is not a successful memory optimization.

## Calibration vs held-out

Existing `M4b-ABC-CALIBRATION` remains calibration only. Its Go G4 task was used during memory construction and therefore cannot establish generalization.

The held-out F5 set is built from later R6/R7/R8/full-run problems:

```text
H1 cost semantics: PREEXECUTION_QUOTE / incurred UNKNOWN / zero
H2 archive semantics: MAP_ASSOCIATION vs VERIFIED_CONSUMPTION
H3 Curator identity: NO_PROPOSAL / same-ID changed-payload collision after restart
H4 stale premise: historical availability vs current authority / NEEDS_RECHECK
```

## F5 arms

All three arms must be generated before model execution from one frozen corpus and common hard prompt-size limit.

```text
A ORDINARY_BOUNDED_CONTEXT
  deterministic naive manifest-order context; no PSI graph; no BM25

B BM25_BASELINE
  same corpus; task-text-only lexical ranking; no graph/gold/manual boosts

C PSI_MEMORY
  existing task compiler + typed PSI retrieval + attestation + exact sources
```

No manual source repair after seeing an answer is allowed.

The external runner currently exposes a 100000-character prompt ceiling. The F5 working cap is therefore <=80000 characters per complete prompt so truncation is detectable and avoidable. The historical M4b A input (~206 kB) must not be silently truncated and relabelled as the same experiment.

## Measurements

Record separately:

```text
correct core claims
correct boundary statements
correct stale refusal
unsupported claims
wrongly accepted stale claims
source-locator accuracy
input/output tokens (UNKNOWN if unavailable)
end-to-end latency (UNKNOWN if unavailable)
external tool calls
source rereads
```

Do not synthesize one quality/cost score by choosing weights after results are visible.

## Execution gate

Next legal work inside F5:

1. freeze held-out manifest and file/content hashes;
2. implement reproducible A/B/C input builder;
3. verify common prompt budget and no silent truncation;
4. freeze blind scoring rubric and answer-ID randomization;
5. then execute 12 independent model runs: `4 tasks x 3 arms`;
6. score blind; only then unblind A/B/C.

Independent model executions may consume Brainbase credits. Preparation is not evidence of model efficacy. Until actual runs are executed:

```text
F5 != PASS
F5 = MODEL_RUN_PENDING
```

## Auditor rule — Semantica Rozmowy 03

The binding rule remains:

\[
P_i(S)\not\Rightarrow S.
\]

For F5 in particular:

```text
retrieved source != model understood source
verified consumption != causal use in reasoning
smaller context != better answer
lower latency != epistemic success
calibration success != held-out generalization
one successful answer != system-level efficacy
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
F5   SELECTED / PREPARED / MODEL_RUN_PENDING
```

## Stop

Do not return to R5 or start F4.4 inside this unit. Do not claim F5 efficacy from prompt preparation. If live execution is blocked by cost/model access, freeze the reproducible benchmark and report `MODEL_RUN_BLOCKED`, not `PASS`.
