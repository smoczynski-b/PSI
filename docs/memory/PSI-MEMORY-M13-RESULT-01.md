# PSI-MEMORY-M13-RESULT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

M13 closes the first deterministic task-to-retrieval-contract path:

\[
\boxed{
\text{natural task}
\to
\mathcal T
\to
\mathfrak R_{\mathcal T,B}(\mathcal M).
}
\]

The primary Polish task

> `sprawdź przesłanki dowodu II.9 i jego granice`

is compiled by `M13-LEXICAL-01` to:

- anchor `II.9`;
- intents `PROOF_PREREQUISITE` and `BOUNDARY`;
- local radius `2`;
- edge budget `12`;
- expanding relations `HARD_DEPENDS_ON`, `USES_DEFINITION`, `USES_LEMMA`;
- terminal relations `NOT_DEPENDS_ON`, `DOES_NOT_IMPLY`;
- stop condition `EDGE_BUDGET_OR_FRONTIER_EXHAUSTED`.

This generated contract reproduces the manually frozen M12 relation policy and its 12-edge selected task view.

## 2. Paraphrase invariance

The second formulation

> `dla II.9 pokaż zależności dowodowe oraz czego twierdzenie nie implikuje`

compiles to the same executable contract.

Thus for the frozen witness:

\[
\boxed{
\operatorname{Compile}(T_1)
=
\operatorname{Compile}(T_2).
}
\]

The equality covers anchor, intents, relation policy, expansion semantics, radius, edge budget, stop condition and attestation mode.

## 3. Monotone narrowing

The narrower task

> `pokaż tylko przesłanki dowodowe II.9`

compiles only the proof-prerequisite family and selects 7 edges. No `NOT_DEPENDS_ON` or `DOES_NOT_IMPLY` relation is included.

Therefore the experiment satisfies the desired narrowing property on this witness:

\[
\boxed{
T_{narrow}\subset T_{broad}
\Longrightarrow
C_{narrow}\subset C_{broad}.
}
\]

## 4. Fail-closed controls

The ambiguous task

> `opisz II.9`

returns `NEEDS_CONTRACT` with `NO_RETRIEVAL`.

The task

> `sprawdź przesłanki dowodu`

returns `NEEDS_ANCHOR` with `NO_RETRIEVAL`.

Hence unrecognized task semantics or a missing anchor do not silently broaden the memory request.

## 5. Regression found during M13

The first M13 CI run (`36629502017`) failed while M1–M12 remained green. The task `przesłanki dowodu II.9 i jego granice` was miscompiled as boundary-only.

Cause: Unicode NFKD normalization does not decompose Polish `ł` into ASCII `l`. The lexical marker `przeslanki dowodu` therefore did not match.

The normalization layer was corrected explicitly for Polish l-stroke, without changing the test contract or expected result. The following run (`36629605030`) passed M1–M13.

This is itself an architectural finding:

\[
\boxed{
\text{task compiler is part of the trusted retrieval path and requires its own regressions}.
}
\]

## 6. Boundary

`M13-LEXICAL-01` is not general natural-language understanding. It is a narrow deterministic compiler for two frozen intent families:

- `PROOF_PREREQUISITE`;
- `BOUNDARY`.

It does not yet infer arbitrary task semantics, resolve implicit anchors, optimize budgets, or compile requests for analogy, evidence, regression, comparison, provenance or model search.

Therefore M13 establishes architectural feasibility of

\[
\text{TASK}\to\text{explicit contract},
\]

not a general language-to-memory compiler.

## 7. Next unresolved problem

The next test should concern **contract ambiguity and composition** rather than adding more lexical synonyms: one task may legitimately request several relation families, competing anchors or different budget priorities.

A useful M14 target is therefore typed contract composition with explicit conflict detection, e.g. proof prerequisites + analogies + strict evidence-only mode, while preserving fail-closed behavior.
