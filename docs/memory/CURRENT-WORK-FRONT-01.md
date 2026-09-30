# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Reviewed implementation:** `7d76308bf7ae63f43606f58c50d7948c89f2860b`  
**Scope:** current work selection for an explicitly selected memory / PSI-VIZ task.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**NEXT: R5 — retain task-required direction in visible relations.**

Closed repair units:

- R1 journal continuation — `PASS_WITH_BOUNDARY`;
- R2 cross-journal result reconciliation — `PASS_WITH_BOUNDARY`;
- R3 visual digest verification — `PASS_WITH_BOUNDARY`;
- R4 complete status redaction — `PASS_WITH_BOUNDARY`.

Evidence:

- [`PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md`](PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md);
- [`PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md`](PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md);
- [`PSI-VIZ-R3-DIGEST-INTEGRITY-01.md`](PSI-VIZ-R3-DIGEST-INTEGRITY-01.md);
- [`PSI-VIZ-R4-STATUS-REDACTION-01.md`](PSI-VIZ-R4-STATUS-REDACTION-01.md).

R4 was reproduced before correction by run `36773765562`: a hidden visual
contract still carried `node_status`. The projection was corrected at
`7d76308bf7ae63f43606f58c50d7948c89f2860b`. R4 gate `36773865796`, R3 gate
`36773865827`, F4.0 `36773865836`, F4.2 `36773865817` and real-Manim gate
`36773865882` subsequently passed. The real-Manim job rendered and verified a
real MP4 after the projection change.

## Auditor rule — Semantica Rozmowy 03

The audit layer remains binding:

\[
P_i(S)\not\Rightarrow S.
\]

Operationally:

```text
component PASS != system PASS
stored digest != verified consumed payload
hidden edge status != complete status redaction
visible relation != necessarily visible direction
```

Each repair is tested at the downstream consumer where its claim is used.

## Ordered repair front

| Unit | Status / dependency | Stop condition |
|---|---|---|
| R0 current instructions | DONE | current pointers agree |
| R1 journal continuation | DONE / PASS_WITH_BOUNDARY | torn-tail continuation and affected regressions pass |
| R2 result reconciliation | DONE / PASS_WITH_BOUNDARY | COMMIT / SERVANT / ACCESS projections reconcile without duplicate mutation or metering |
| R3 visual digest verification | DONE / PASS_WITH_BOUNDARY | stale hashes and contradictory duplicated bindings fail closed at frame, keyframe, timeline and plan consumers; real render passes |
| R4 complete status redaction | DONE / PASS_WITH_BOUNDARY | hidden node/edge status absent downstream; explicitly allowed status preserved in declared status-bearing channels |
| **R5 directed visual relations** | **P1 / NEXT** | reversing a directed edge is visibly distinguishable in SVG and actual animation; symmetric relations may remain undirected only by declared relation contract |
| R6 cost semantics | P1 / before cost-benefit claims | over-budget measured evidence retained; quote/actual/unknown separated; units and scalarization explicit |
| R7 consumed-version receipt | P2 | association distinguished from verified version consumption |
| R8 no-proposal observation identity | P2 | ID scope defined and below-threshold changed-payload replay tested across restart |

R7/R8 block only their stronger claims. Do not create a parallel audit registry.

## R5 handoff

### Object

Current SVG and executable Manim renderers encode visible relations using
undirected line primitives. For fixed node positions the viewer therefore
cannot reliably distinguish

```text
A DEPENDS_ON B
```

from

```text
B DEPENDS_ON A
```

when relation text and geometry are otherwise the same. Different opaque asset
identifiers do not constitute visible direction.

### Required distinction

A relation contract must state whether its visible relation type is directed or
symmetric.

For directed relation types:

\[
A\to B \neq B\to A
\]

must survive the visual projection and be readable by the viewer in every
claimed visual consumer.

For symmetric relation types an undirected mark is legal only when the relation
contract declares symmetry.

### Separating witness

Construct two checked states/frames with fixed node positions and otherwise
identical visible data:

```text
W_forward: A DEPENDS_ON B
W_reverse: B DEPENDS_ON A
```

Required tests:

1. the directed/symmetric property is explicit and typed, not inferred from the
   spelling or screen geometry;
2. SVG output for the pair is visibly distinguishable by a declared direction
   mark;
3. executable Manim output uses the same declared direction semantics;
4. an actual rendered animation frame distinguishes the reversed pair;
5. a relation declared symmetric may use an undirected mark and remains stable
   under endpoint reversal;
6. R3 integrity and R4 status-redaction regressions remain green.

Separately declare which status/provenance fields the animation channel exposes.
Do not silently reconstruct metadata omitted by the checked projection.

### Correction constraint

Fix the typed visual-relation contract and its consumers. Do not infer relation
direction from layout, asset-id ordering or relation-name heuristics.

### Stop

Stop R5 when the reversed-edge separating witness, symmetric control, affected
F4.0–F4.3 regressions and one actual rendered-frame check pass. Do not begin
F4.4 inside the same repair unit.

## Recorded implementation state

```text
F0   PASS_WITH_BOUNDARY
F1   PASS_WITH_BOUNDARY
F2.0 CONTRACT_PASS
R1   PASS_WITH_BOUNDARY
R2   PASS_WITH_BOUNDARY
R3   PASS_WITH_BOUNDARY
R4   PASS_WITH_BOUNDARY
F2.1 PASS_WITH_BOUNDARY; R6 OPEN
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

## R4 boundary retained

R4 guarantees status redaction at the checked projection and downstream
consumers. It does not claim that animation exposes every explicitly allowed
status/provenance field; the current `ManimPlan` may omit such metadata. That
exposure declaration is handled with R5 or a later typed channel contract.

## Preserved F4.4 specification

**FIRST TYPED SEMANTIC ADAPTER — SPLIT.**

After R5 is closed:

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
