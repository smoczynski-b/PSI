# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-10-01  
**Full bounded acceptance run:** `36781418888`  
**F5 preparation run:** `36784242295`  
**Scope:** current work selection for PSI memory / model efficacy / visualization.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**F5 — MODEL EFFICACY: PREPARED / MODEL_RUN_BLOCKED.**

The user selected F5 and authorized cautious credit use with an explicit reserve. Preparation is complete; no model-efficacy result exists yet.

Current state:

```text
FULL_BOUNDED_RUN = PASS_WITH_BOUNDARY
R9 = NOT_CREATED
F5_PREPARATION = PASS
F5_MODEL_EFFICACY = NOT_RUN
F5_EXECUTION = BLOCKED_BY_ZERO_ALLOCATED_CREDITS
R5 = OPEN / DEFERRED
F4.4 = DEFERRED_AFTER_R5
```

Primary evidence:

- [`PSI-MEMORY-F5-MODEL-EFFICACY-01.md`](PSI-MEMORY-F5-MODEL-EFFICACY-01.md)
- `experiments/f5-evaluation-contract.json`
- `scripts/prepare_f5_evaluation.py`

## Frozen F5-HOLDOUT-V1

Preflight rejected the initial R6/R7/R8/full-run task set for the comparative arm C because those objects are not covered by the existing automatic `build_memory_pack.py` routing path. They were not manually adapted.

The frozen held-out set was corrected **before any model answer was obtained** to three existing automatically routable units:

```text
H10 = II.10 strong lumpability bridge
H11 = II.11 Myhill-Nerode bridge
H12 = II.12 Paige-Tarjan benchmark
```

M4b/G4 remains calibration only.

### Arms

```text
A = full frozen II.10-II.12 corpus
B = BM25 task-text-only, source budget matched to C
C = frozen existing build_memory_pack.py semantics
```

No source may be manually added after seeing an answer.

## Preparation evidence

Workflow `36784242295`, job `110121688788`: `success`.

The generated artifact `f5-prepared-inputs` is frozen as artifact ID `11128514047`, digest:

```text
sha256:1a8a10cbb4aa32ac90a563d29911ac5aad61b142e551d2565146ffac9bfc289c
```

Prompt sizes:

```text
H10 A 27710 chars   B 10172   C 10544
H11 A 27669 chars   B  9505   C  9861
H12 A 27656 chars   B  8541   C  8940
```

All are below the 80000-character F5 cap. For each task B stays at or below C's source-context byte budget.

## Credit-conserving execution plan

The first planned paid stage is only:

```text
pilot H10: C first
if technically valid -> A + B
blind score the 3-arm pilot
only then decide whether H11/H12 justify more credits
```

A dedicated clean runner was created with `kafka_cloud`, fixed model `claude-sonnet-4-6`, no MCP, no skills and no project memory.

The first real H10-C attempt reached the billing gate before inference and returned:

```text
CREDITS_EXHAUSTED
allocated = 0
used = 0
HTTP 402
```

Therefore no F5 model answer exists and no Brainbase credits were consumed by the pilot.

## Resume point

When model credits become available, resume **without rebuilding or retuning**:

```text
1. rerun frozen H10-C (blind id ANS-25E4942F7A3F)
2. if technical run succeeds, run frozen H10-A and H10-B
3. blind-score H10
4. decide whether to spend further credits on H11/H12
```

Do not run all nine responses automatically. Preserve a reserve.

## Auditor rule — Semantica Rozmowy 03

\[
P_i(S)\not\Rightarrow S.
\]

For F5:

```text
prepared prompts != model efficacy
retrieved source != semantic understanding
smaller context != better answer
one pilot answer != comparative result
calibration != held-out generalization
billing failure != model failure
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
F5   PREPARATION_PASS / MODEL_RUN_BLOCKED
```

## Stop

Do not claim F5 `PASS`. Do not substitute answers produced in this conversation for independent runner executions. R5 remains deferred while F5 is the selected front; if F5 remains blocked, a later explicit selection may return to R5 without invalidating the frozen F5 benchmark.
