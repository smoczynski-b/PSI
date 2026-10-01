# PSI-VIZ-F4.4-01 — TYPED SEMANTIC SPLIT

**Status:** `PASS_WITH_BOUNDARY`  
**Date:** 2026-10-01  
**Branch:** `psi-memory-map-01`  
**Scope:** first bounded typed semantic adapter for PSI-VIZ.  
**Does not modify:** CORE5, CANON-03, theorem status, PSI relation truth, live FORUM state.

## 1. Problem

F4.3 left semantic animation adapters deliberately unimplemented. The first candidate was `SPLIT`.

The pre-F4.4 generic transition classifier admitted every non-`REPOSITION` motion whenever only this coarse predicate held:

```text
before.semantic_digest != after.semantic_digest
```

That predicate establishes that some projected semantics changed. It does **not** establish that the change is a split.

The separating witness therefore asked whether an unrelated semantic delta could be relabelled `SPLIT`.

### FAIL-before

Workflow:

```text
run: 36790115371
job: 110140769727
```

failed exactly with:

```text
AssertionError: generic semantic change was incorrectly accepted as SPLIT
```

The counterexample was a real source delta adding an unrelated relation/object. This separated:

```text
semantic change
!=
typed SPLIT
```

## 2. Correction

Generic motion classification no longer owns `SPLIT`. `SPLIT` is handled only by the dedicated typed adapter in:

```text
scripts/psi_viz_split_adapter.py
```

The adapter introduces:

```text
SplitEventSpec
SplitTimeline
ExecutableSplitScene
compile_split_timeline(...)
verify_split_timeline(...)
compile_executable_split_scene(...)
```

For the bounded F4.4 shape a legal split requires all of the following:

```text
1. both source VisualFrame objects pass integrity verification;
2. visual/task/source contract identity is preserved;
3. source revision advances by exactly one;
4. source_state_digest changes;
5. semantic_digest changes;
6. the declared source object exists before and after;
7. exactly one new object appears and no object disappears;
8. all pre-existing node statuses remain unchanged;
9. all pre-existing relation rows remain unchanged;
10. exactly one new relation appears;
11. that relation exactly matches
      source_object_id -- separating_relation --> new_object_id;
12. the separating relation is explicitly typed DIRECTED;
13. positions of all pre-existing objects remain unchanged;
14. the new object is placed visibly apart from its source.
```

Hence the adapter refuses both a generic semantic change and a `SPLIT` that attempts to smuggle a simultaneous `REPOSITION` of old objects.

## 3. Positive witness

The executed witness uses an actual `MemoryEvent` and `apply_delta`:

```text
x2 --SEPARATED_BY_OBSERVATION--> x2'
```

The original object `x2` survives. A single new distinguishable object `x2'` appears with one explicitly directed separating relation.

The source-only gate checks:

```text
generic_false_split_fail_closed=PASS
typed_split_exact_delta=PASS
split_source_survives=PASS
split_adds_exactly_one_object_and_relation=PASS
split_cannot_smuggle_reposition=PASS
executable_split_scene=PASS
```

Source-only acceptance run:

```text
36790864284
```

The final typed timeline digest is:

```text
5c9962d6bcf83c0bf379adcc3d3ad281057c5712d1f6911ac1241058ba6294d7
```

Generated Manim scene source digest:

```text
db3a33ce119e1e53c734a71d3a0dfccd9d230adc541d78dc98a5e0f276ac93e2
```

## 4. Static and real-animation outputs

The same verified semantic transition generates:

```text
before.svg
after.svg
split-timeline.json
split-scene.py
psi-viz-split.mp4
```

The static outputs differ and the post-split SVG contains both `x2'` and the explicitly typed directed `SEPARATED_BY_OBSERVATION` relation.

Real Manim execution:

```text
run: 36791415147
job: 110144932999
conclusion: success
Manim: 0.19.0
codec: h264
resolution: 854 x 480
duration: 1.733333 s
decoded frames: 26
video size: 32281 bytes
changed RGB pixels, first vs last: 11592
```

Thus the executable consumer produces a nontrivial visible state change; this is not merely a source-code assertion or PNG-container difference.

Artifact:

```text
id: 11131048847
name: psi-viz-f4.4-typed-split
size: 1072417 bytes
sha256:66e3c5d735bbf18ac30ed9b211e74c17693d2cf81043c893db2c2455514f43fc
```

Manifest bindings:

```text
revision: 0 -> 1
state digest:
  b77b5424d60ba8689dfd449171ff7ca4eb9ecef4d5aeb58ef791379fa57e03de
  ->
  0254afd8f9d97764ee6c3585cc1bfed865a70d26cc9d66375814bdab7805919c

semantic digest:
  dcf9c139b42287302f40eb3a4e02ba9445572fe98e9c2b7059a7e1ca2533d0dd
  ->
  14c140ee61243d33a28c766ccf1aa1648a95d2a5641b0ead24e72ef81dc75d5e

SVG digest:
  cbf81a5c797f21e853cccc717c65775bf67d547e3b4c4206887dc4be13a10cce
  ->
  f61e62c1c37a6950dc22d1d1185c39b845deed8299ef64e50c4af601461440be
```

## 5. Regression gate

The same final run re-passed the affected visual guarantees:

```text
R3   digest/binding integrity              PASS
R4   status redaction                      PASS
F4.0 visual projection contract            PASS
F4.1 output packets                        PASS_WITH_BOUNDARY
F4.2 SVG / Manim-plan renderer             PASS_WITH_BOUNDARY
F4.3 executable Manim scene                PASS / existing boundary
R5   typed relation direction source       PASS_WITH_BOUNDARY
R5   real rendered direction pixels        PASS_WITH_BOUNDARY
```

No regression was accepted merely by source inspection.

## 6. Legal claim

F4.4 establishes only:

```text
TYPED_SPLIT_VISIBLE
```

for the bounded structural contract above.

That means: the exact verified source transition matches the declared split shape, its timeline is digest-bound to the exact before/after frames, and the real renderer emits a visible split corresponding to that transition.

It does **not** establish any of the following:

```text
arbitrary semantic change is a SPLIT;
the separating relation is true in the world;
the viewer or model understands the animation;
the animation improves inference or learning;
the visual composition is aesthetically optimal;
all possible mathematical notions of splitting share this adapter;
PSI now has a complete semantic-event algebra;
F4.4 changes CORE5 or CANON-03.
```

## 7. Boundary

The implemented `SPLIT` is intentionally narrow:

```text
one surviving source object
+
exactly one new object
+
exactly one new directed separating relation
+
no other semantic rewrite
+
no repositioning of pre-existing objects.
```

Legibility/hierarchy are covered only by the existing renderer and F4.3 technical guards and by the concrete static/animation witness. F4.4 contains no human-subject comprehension test and no comparative design-quality experiment.

Therefore:

```text
F4.4 = PASS_WITH_BOUNDARY
```

and no untested successor is inferred from that result.
