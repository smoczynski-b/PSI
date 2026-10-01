# PSI-VIZ-R3-DIGEST-INTEGRITY-01

**Status:** PASS_WITH_BOUNDARY  
**Date:** 2026-09-30  
**Branch:** `psi-memory-map-01`  
**Input HEAD:** `008b3cd518bd03db31104a95cf58b122b35a55f2`  
**Separating witness:** `ba0674ae34b095600b4fa3b9c2f64366d8e7e325`  
**R3 gate:** `23e590a93b406f37246397b81338c980026a0f08`  
**VisualFrame verifier:** `bd115090ae92b607d87eecd03042ca8f4c22517b`  
**Output verifier:** `4e5e88994430f0ca431b0c8002dc85f002cf263a`  
**Renderer verifier:** `0159789578e28de62bf09c2a8d5761bb1a7b5703`  
**Executable consumer verifier:** `492a054dc5d84a19eb4cfb923268827f67af4336`  
**Regression separation:** `06d9202272f4c73a9ebe55f12131b0f5760402ed`  
**Failing reproduction:** workflow run `36771827933`  
**Passing source gate:** workflow run `36772347053`  
**Passing real Manim gate:** workflow run `36772347262`

## 1. Object

R3 concerns integrity of representation packets at the instant they are
consumed. The auditor rule inherited from **Semantica Rozmowy — 03** is applied
literally:

```text
stored projection/binding != verified current payload
```

For each packet `P=(p,h,b)` with payload `p`, declared digest `h` and duplicated
binding fields `b`, the consumer must establish both:

```text
H(p) = h
```

and

```text
duplicated internal bindings = external packet bindings.
```

A matching hash proves payload identity/integrity only. It does not prove truth,
admission, authorization or provenance authority.

## 2. Reproduced defect

The witness was executed before the correction. Workflow run `36771827933`
failed because the implementation consumed all eleven stale or contradictory
packets presented by the test:

```text
VisualFrame.semantic_payload -> classify_transition
VisualFrame.semantic_payload -> compile_print_keyframe
VisualFrame.layout_payload -> compile_animation_timeline
PrintKeyframe.payload -> render_svg
PrintKeyframe.payload -> compile_manim_plan
PrintKeyframe duplicated semantic binding
AnimationTimeline.payload -> compile_manim_plan
AnimationTimeline duplicated declared_motion binding
ManimPlan.payload -> render_manim_python
ManimPlan.payload -> compile_executable_manim_scene
ManimPlan duplicated keyframe binding
```

Thus R3 was reproduced as an execution defect at every audited consumer layer.

## 3. Correction

### 3.1 VisualFrame

`verify_visual_frame` recomputes both semantic and layout digests and verifies
source/task/revision/state bindings plus equality of the semantic node set and
layout position domain.

It is called by:

```text
compile_print_keyframe
compile_animation_timeline
classify_transition
```

so direct transition classification cannot trust stale digest fields.

### 3.2 PrintKeyframe and AnimationTimeline

`verify_print_keyframe` recomputes the print payload digest and verifies the
semantic/layout digests duplicated inside `payload.source`.

`verify_animation_timeline` recomputes the timeline payload digest and verifies:

```text
duration
motion kind
semantic_changed
layout_changed
legal transition status
reason code
semantic-event source/target digests where present
```

against the packet's outer bindings.

### 3.3 ManimPlan

`verify_manim_plan` recomputes the plan payload digest and verifies that the
embedded print/timeline payload digests equal the plan's outer source bindings.
It runs in both renderer paths:

```text
render_manim_python
compile_executable_manim_scene
```

and `compile_manim_plan` verifies its keyframe and timeline inputs before
constructing a new plan.

## 4. Separating regression

The earlier F4.3 scheduler test intentionally changed an action interval while
using a fake stale plan digest. After R3 this is correctly rejected first by the
integrity verifier, before scheduler classification.

The test was therefore separated into two independent predicates:

```text
stale payload + old hash -> R3 integrity rejection
hash-consistent unsupported schedule -> F4.3 scheduler rejection
```

No verifier was weakened to preserve the old test ordering.

## 5. Verification

Workflow run `36772347053`, job `digest-integrity-r3`, completed `success`:

```text
R3 separating witness                PASS
F4.0 projection regression           PASS
F4.1 output regression               PASS
F4.2 renderer regression             PASS
F4.3 executable-source regression    PASS
```

The independent real-render workflow run `36772347262` also completed
`success`, including:

```text
F4.0 / F4.1 / F4.2 contract checks
F4.3 executable scene source
Manim runtime installation
real MP4 render
rendered-video verification
finite-representation control
active-memory regression
institutional-constitution regression
artifact upload
```

Hence the correction survives the actual F4.3 rendering path, not only the
source-level test harness.

## 6. Boundary

R3 establishes integrity and consistency of the current in-process PSI-VIZ
packet chain. It does not provide cryptographic authentication, signer identity,
remote transport security, semantic truth, Guardian authorization, or admission.
The packet dictionaries remain mutable Python objects; fail-closed verification
at every audited consumer is therefore the operative guarantee.

R3 does not repair redaction semantics. In particular, node-status leakage is a
separate projection-contract defect and remains R4.

## 7. Verdict

```text
R3 VISUAL DIGEST VERIFICATION = PASS_WITH_BOUNDARY
NEXT = R4 COMPLETE STATUS REDACTION
```

No change to CORE5, CANON-03, theorem status, constitutional role split or live
FORUM state.
