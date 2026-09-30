# PSI-VIZ-R5-RELATION-DIRECTION-01

**Status:** `PASS_WITH_BOUNDARY`  
**Date:** 2026-10-01  
**Branch:** `psi-memory-map-01`  
**Scope:** explicit relation semantics and visible direction in supported PSI-VIZ SVG / Manim paths.  
**Does not modify:** CORE5, CANON-03, theorem status.

## 1. Defect

Before R5, a PSI-VIZ edge carried endpoints and a relation name, but the visual contract did not type whether that relation was directed or symmetric. SVG and executable Manim therefore had no contractual basis for displaying direction.

The forbidden inference was:

```text
relation name or endpoint ordering
=> guessed visual direction semantics
```

The required distinction is now explicit:

```text
UNSPECIFIED
DIRECTED
SYMMETRIC
```

`UNSPECIFIED` remains a legal compatibility state and is never upgraded by a relation-name heuristic.

## 2. Separating witness — FAIL before correction

The R5 witness was added first. The pre-correction run failed before rendering because the visual contract could not even accept typed relation semantics:

```text
run: 36785432919
job: 110125601406
VisualContract.__init__(): unexpected keyword argument 'relation_semantics'
```

This establishes the original boundary failure rather than inferring it from source inspection.

## 3. Correction

Relevant repair commits:

```text
bc627515da9f6dedca66d6a4d1a73d65f964d089  Add R5 relation-direction separating witness
bca93d48beeb3acf19d354fcdcd1b790505f8b9d  Add R5 relation-direction CI gate
9d2980963e83866de06f07ba074fa34efea7dcbc  Type relation direction in PSI-VIZ projection
5cae7e3e57b44b6ade2ab71b2338b9e932de2f2d  Carry typed relation direction into PSI-VIZ outputs
99bd18c4a21d75acba1fe3e0824c96d0ea8983f2  Render typed directed relations in SVG and Manim plans
8e01b500e995b04a60c4d7c60c107db414593a87  Render typed directed relations in executable Manim
9ff66cf9af74793ab7359ff99d4ce3f116ea4018  Add real Manim pixel witness for R5 relation direction
a7a133a951d95515df4e0619c802b9e8400354f1  Add real Manim R5 relation-direction gate
```

The typed relation semantics are propagated through:

```text
VisualContract
-> VisualFrame
-> print keyframe
-> SVG / Manim plan
-> executable Manim scene
-> rendered pixels
```

Rendering rule:

```text
DIRECTED  -> arrow primitive
SYMMETRIC -> undirected line with canonicalized endpoint order
UNSPECIFIED -> no asserted direction
```

No renderer infers direction from names such as `DEPENDS_ON`.

## 4. Real-render acceptance witness

A dedicated real-Manim gate generates four scenes from the production PSI-VIZ pipeline:

```text
A DEPENDS_ON B
B DEPENDS_ON A
A PEER_WITH B
B PEER_WITH A
```

The scenes are rendered by Manim 0.19.0 as static final frames. The test decodes each PNG to RGBA and compares raw pixel bytes, not source strings, filenames or PNG metadata.

Acceptance condition:

\[
\operatorname{pixels}(A\to B) \ne \operatorname{pixels}(B\to A),
\]

\[
\operatorname{pixels}(A\leftrightarrow B) = \operatorname{pixels}(B\leftrightarrow A).
\]

Executed evidence:

```text
workflow run: 36788563749
job:          110135733341
conclusion:   success
```

Decoded RGBA witnesses (`854 x 480` each):

```text
directed-ab  f8a2b30ec2e0bf38c9d5076ca99b2790fdef2a476e9cbacd368e3fadcd1d75d5
directed-ba  a69490c0daf199df32530f2cd52661fc94f1480aade43aa56c489cbf20f131ea
symmetric-ab f40b88cc86b7d7e4997c7a4d3e2786fa1fe104dc4616814a13038bf8cb92511d
symmetric-ba f40b88cc86b7d7e4997c7a4d3e2786fa1fe104dc4616814a13038bf8cb92511d
```

Thus the directed reversal changes the actual image, while symmetric reversal is pixel-identical.

Evidence artifact:

```text
artifact id: 11130852811
name: psi-viz-r5-real-relation-direction
artifact sha256: 33ae524c11e200a99217b41e10ab0620d9640f55ba9851e2b94312b07d353ed7
```

## 5. Regression gate

The same successful real-render job re-ran and passed:

```text
R3   PSI-VIZ digest integrity
R4   status redaction
F4.0 projection contract
F4.1 output contract
F4.2 renderer contract
F4.3 executable Manim scene source
```

Therefore R5 is not closed by a component-only source test.

## 6. Legal claim

R5 permits the bounded claim:

```text
For relations explicitly typed DIRECTED in the supported PSI-VIZ path,
reversing endpoints produces a different rendered Manim image carrying visible direction.
For relations explicitly typed SYMMETRIC, endpoint reversal canonicalizes to the same rendered image.
```

It does **not** permit:

```text
UNSPECIFIED => directed or symmetric
visible arrow => relation is true
rendered direction => semantic understanding by a viewer/model
one tested renderer/configuration => universal perceptual/accessibility guarantee
R5 PASS => F4.4 aesthetic/design quality PASS
```

## 7. Result

```text
R5 = PASS_WITH_BOUNDARY
F4.2 = PASS_WITH_BOUNDARY; R5 CLOSED
F4.3 = PASS_WITH_BOUNDARY; R5 CLOSED
F4.4 = NEXT / NOT_RUN
```

R5 is an implementation/audit repair unit. It does not create a new PSI canon version.
