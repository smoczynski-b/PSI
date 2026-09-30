# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Reviewed implementation:** `06d9202272f4c73a9ebe55f12131b0f5760402ed`  
**Scope:** current work selection for an explicitly selected memory / PSI-VIZ task.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**NEXT: R4 — complete status redaction for nodes and edges across the whole PSI-VIZ chain.**

Closed repair units:

- R1 journal continuation — `PASS_WITH_BOUNDARY`;
- R2 cross-journal result reconciliation — `PASS_WITH_BOUNDARY`;
- R3 visual digest verification — `PASS_WITH_BOUNDARY`.

Evidence:

- [`PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md`](PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md);
- [`PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md`](PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md);
- [`PSI-VIZ-R3-DIGEST-INTEGRITY-01.md`](PSI-VIZ-R3-DIGEST-INTEGRITY-01.md).

R3 was first reproduced as an executable defect: run `36771827933` accepted all
11 stale/contradictory visual packets. After correction, source gate
`36772347053` and real-Manim gate `36772347262` both passed. F4.0–F4.3 therefore
retain their previous functional status with stale-hash resistance added.

## Auditor rule — Semantica Rozmowy 03

The audit layer remains binding:

\[
P_i(S)\not\Rightarrow S.
\]

A correct local projection does not certify the global state. Operationally:

```text
component PASS != system PASS
stored digest != verified consumed payload
hidden edge status != complete status redaction
visible relation != necessarily visible direction
```

Each repair must therefore be tested at the downstream consumer where the claim
is used, not only at its producer.

## Ordered repair front

| Unit | Status / dependency | Stop condition |
|---|---|---|
| R0 current instructions | DONE | current pointers agree |
| R1 journal continuation | DONE / PASS_WITH_BOUNDARY | torn-tail continuation and affected regressions pass |
| R2 result reconciliation | DONE / PASS_WITH_BOUNDARY | COMMIT / SERVANT / ACCESS projections reconcile without duplicate mutation or metering |
| R3 visual digest verification | DONE / PASS_WITH_BOUNDARY | stale hashes and contradictory duplicated bindings fail closed at frame, keyframe, timeline and plan consumers; real render passes |
| **R4 complete status redaction** | **P1 / NEXT** | hidden node and edge status is absent from frame, output packet, SVG, Manim plan/executable channel; explicitly allowed status remains available |
| R5 directed visual relations | P1 / after R4 | reversing a directed edge is visibly distinguishable in SVG and actual animation; symmetric relations may remain undirected only by declared relation contract |
| R6 cost semantics | P1 / before cost-benefit claims | over-budget measured evidence retained; quote/actual/unknown separated; units and scalarization explicit |
| R7 consumed-version receipt | P2 | association distinguished from verified version consumption |
| R8 no-proposal observation identity | P2 | ID scope defined and below-threshold changed-payload replay tested across restart |

R7/R8 block only their stronger claims. Do not create a parallel audit registry.

## R4 handoff

### Object

Current defect identified by the 04 audit:

```text
compile_visual_frame:
edge.status -> copied only when "status" in visible_metadata
node_status -> copied unconditionally
```

Hence a contract with `visible_metadata=()` can still expose a node status such
as `NEEDS_RECHECK`; `compile_print_keyframe` then copies it and SVG can render it.

### Separating witness

Construct a workspace containing at least one non-empty node status, for example:

```text
X.status = NEEDS_RECHECK
```

and two visual contracts over the same state:

```text
C_hidden.visible_metadata = ()
C_visible.visible_metadata = ("status",)
```

Required tests:

1. hidden contract: no node status and no edge status in `VisualFrame`;
2. hidden contract: forbidden status absent from `PrintKeyframe`;
3. hidden contract: forbidden status absent from SVG text/metadata;
4. hidden contract: forbidden status absent from `ManimPlan` and executable
   scene source or any visual channel derived from that hidden value;
5. visible contract: status remains explicitly available and renderable;
6. R3 integrity checks remain valid after the redaction change.

### Correction constraint

Repair the **projection contract**, not Guardian policy and not renderer-side
filtering. Downstream renderers may only consume what the checked projection
contains; they must not reconstruct hidden metadata from Workspace or another
source.

### Stop

Stop R4 when the separating witness and affected F4.0–F4.3 source/real-render
regressions pass. Do not begin R5 inside the same repair commit.

## Recorded implementation state

```text
F0   PASS_WITH_BOUNDARY
F1   PASS_WITH_BOUNDARY
F2.0 CONTRACT_PASS
R1   PASS_WITH_BOUNDARY
R2   PASS_WITH_BOUNDARY
R3   PASS_WITH_BOUNDARY
F2.1 PASS_WITH_BOUNDARY; R6 OPEN
F3.0 CONTRACT_PASS
F3.1 PASS_WITH_BOUNDARY
F3.2 PASS_WITH_BOUNDARY; R7 OPEN
F3.3 PASS_WITH_BOUNDARY; R8 OPEN
F3   REFERENCE_CASES_PASS; HARDENING_OPEN
F4.0 CONTRACT_PASS; R4 OPEN
F4.1 PASS_WITH_BOUNDARY; R4 OPEN
F4.2 PASS_WITH_BOUNDARY; R4/R5 OPEN
F4.3 PASS_WITH_BOUNDARY; R4/R5 OPEN
F4.4 DEFERRED_AFTER_R4_R5
F5   NOT_RUN
```

## Preserved F4.3 witness

The authoritative F4.3 report remains `docs/memory/PSI-VIZ-F4.3-01.md`.
The earlier real witness established:

```text
VisualFrame
-> PrintKeyframe + AnimationTimeline
-> ManimPlan
-> executable Manim scene
-> real MP4
```

with layout-only `REPOSITION`, invariant semantic digest, typed edges following
moving nodes, one shared parallel movement interval and fail-closed unsupported
schedules. R3 subsequently re-ran this real path successfully in workflow
`36772347262` after adding packet-integrity verification.

## F4.4 — preserved deferred specification

**FIRST TYPED SEMANTIC ADAPTER — SPLIT.**

After R4 and R5 are closed:

1. begin from the checked compatible `x1,x2` F4.0 state;
2. apply one real admitted memory event that separates a case;
3. compile a new `VisualFrame` at the new revision with changed
   `semantic_digest`;
4. declare `SPLIT`, never infer it from screen geometry;
5. require a typed before/after diff naming exactly the objects/relations/status
   changes;
6. missing/inconsistent diff or unexpected change type -> fail closed;
7. render one real short film and verify the semantic-digest transition against
   the source state;
8. do not generalize yet to arbitrary `SEMANTIC_EVENT`.

Only then may the first PSI-VIZ vertical slice be called complete and F5 begin.
R6 must precede any end-to-end cost claim or F5 cost comparison. GPU and live
FORUM work remain outside this selected front.
