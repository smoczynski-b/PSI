# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-10-01  
**Full bounded acceptance run:** `36781418888`  
**F5 preparation run:** `36784242295`  
**R5 real-render run:** `36788563749`  
**F4.4 typed-SPLIT run:** `36791415147`  
**Scope:** current work selection for PSI memory / model efficacy / visualization.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**F4.4 — CLOSED `PASS_WITH_BOUNDARY`. No automatic visual successor is defined.**

F5 remains frozen at `PREPARATION_PASS / MODEL_RUN_BLOCKED`. No F5 prompt, source selection, model answer or evaluator state was rebuilt while R5/F4.4 were executed.

Current state:

```text
FULL_BOUNDED_RUN = PASS_WITH_BOUNDARY
R9 = NOT_CREATED
R5 = PASS_WITH_BOUNDARY
F4.4 = PASS_WITH_BOUNDARY
F5_PREPARATION = PASS
F5_MODEL_EFFICACY = NOT_RUN
F5_EXECUTION = BLOCKED_BY_ZERO_ALLOCATED_CREDITS
NEXT_AUTOMATIC = NONE
NEXT = EXPLICIT_SELECTION_REQUIRED; OR RESUME_F5_WHEN_CREDITS_EXIST
```

Primary evidence:

- [`PSI-VIZ-F4.4-01.md`](PSI-VIZ-F4.4-01.md)
- [`PSI-VIZ-R5-RELATION-DIRECTION-01.md`](PSI-VIZ-R5-RELATION-DIRECTION-01.md)
- [`PSI-MEMORY-F5-MODEL-EFFICACY-01.md`](PSI-MEMORY-F5-MODEL-EFFICACY-01.md)
- `experiments/f5-evaluation-contract.json`
- `scripts/prepare_f5_evaluation.py`

## F4.4 closure

F4.4 implements the first bounded typed semantic adapter:

```text
SPLIT
```

The defect exposed by the separating witness was:

```text
semantic_digest changed
!=
typed SPLIT
```

FAIL-before:

```text
run: 36790115371
job: 110140769727
failure: generic semantic change was incorrectly accepted as SPLIT
```

Correction:

```text
generic transition path no longer owns SPLIT
+
dedicated SplitEventSpec / SplitTimeline adapter
+
exact before/after digest and revision binding
+
one surviving source object
+
exactly one new object
+
exactly one new DIRECTED separating relation
+
no removal/rewrite of old semantics
+
no repositioning of pre-existing objects
```

Positive source-only gate:

```text
run: 36790864284
```

Final real-Manim acceptance:

```text
run: 36791415147
job: 110144932999
conclusion: success
codec: h264
resolution: 854 x 480
duration: 1.733333 s
decoded frames: 26
changed RGB pixels first -> last: 11592
```

Artifact:

```text
id: 11131048847
name: psi-viz-f4.4-typed-split
size: 1072417 bytes
sha256:66e3c5d735bbf18ac30ed9b211e74c17693d2cf81043c893db2c2455514f43fc
```

The final job re-passed R3, R4, F4.0-F4.3 and both source and real-render R5 gates.

Legal scope:

```text
TYPED_SPLIT_VISIBLE
```

only for the bounded one-source/one-new-object/one-separating-relation shape. It does not establish relation truth, universal semantic-event coverage, human/model comprehension, improved reasoning, or aesthetic optimality.

Legibility and hierarchy remain covered only by existing renderer/F4.3 technical guards and this concrete static/animation witness; no human-subject design-quality result is claimed.

## R5 closure

The visual contract types relation semantics explicitly:

```text
UNSPECIFIED | DIRECTED | SYMMETRIC
```

No renderer infers direction from relation names.

Real-Manim acceptance evidence:

```text
run: 36788563749
job: 110135733341
artifact: 11130852811
artifact sha256: 33ae524c11e200a99217b41e10ab0620d9640f55ba9851e2b94312b07d353ed7
```

The gate compares decoded RGBA pixels:

```text
DIRECTED reversal  -> different pixels
SYMMETRIC reversal -> identical pixels
```

R5 closes only the typed visible-direction boundary; it does not establish aesthetic quality, semantic truth or universal human/model comprehension.

## Frozen F5-HOLDOUT-V1

Preflight rejected the initial R6/R7/R8/full-run task set for comparative arm C because those objects are not covered by the existing automatic `build_memory_pack.py` routing path. They were not manually adapted.

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

## F5 preparation evidence

Workflow `36784242295`, job `110121688788`: `success`.

Generated artifact `f5-prepared-inputs`: artifact ID `11128514047`, digest:

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

## Credit-conserving F5 resume plan

When model credits become available, resume **without rebuilding or retuning**:

```text
1. rerun frozen H10-C (blind id ANS-25E4942F7A3F)
2. if technical run succeeds, run frozen H10-A and H10-B
3. blind-score H10
4. decide whether to spend further credits on H11/H12
```

The dedicated clean runner uses `kafka_cloud`, fixed model `claude-sonnet-4-6`, no MCP, no skills and no project memory.

The first real H10-C attempt reached the billing gate before inference and returned:

```text
CREDITS_EXHAUSTED
allocated = 0
used = 0
HTTP 402
```

Therefore no F5 model answer exists and no Brainbase credits were consumed by the pilot.

## Auditor rule — Semantica Rozmowy 03

\[
P_i(S)\not\Rightarrow S.
\]

In particular:

```text
semantic change != typed SPLIT
typed SPLIT visible != relation truth
rendered transition != semantic understanding
F4.4 PASS != design-quality theorem
visible direction != relation truth
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
R5   PASS_WITH_BOUNDARY
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
F4.2 PASS_WITH_BOUNDARY; R5 CLOSED
F4.3 PASS_WITH_BOUNDARY; R5 CLOSED
F4.4 PASS_WITH_BOUNDARY
F5   PREPARATION_PASS / MODEL_RUN_BLOCKED
```

## Stop

F4.4 is closed. No F4.5 or other automatic visual successor is defined in the current work contract. Do not create one merely because F4.4 passed.

Do not claim F5 `PASS`, and do not substitute answers produced in this conversation for independent runner executions. Resume frozen F5 only when model credits are actually available, or wait for an explicit user selection of another project front.
