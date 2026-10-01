# PSI-MEMORY-M14-RESULT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36630363560` executed M1–M14 successfully.

M14 tests typed composition of task intents, evidence constraints and anchors.

The core result is:

\[
\boxed{
\operatorname{Compose}(c_1,\ldots,c_n)
\neq
c_1\cup\cdots\cup c_n
}
\]

unless the components are jointly executable.

## 2. Compatible composition

Task:

> `dla II.9 pokaż przesłanki dowodu, granice i analogie`

compiled to one contract containing:

- `PROOF_PREREQUISITE`;
- `BOUNDARY`;
- `ANALOGY`;
- anchor `II.9`;
- local radius `2`;
- edge budget `14`;
- ordinary mixed attestation mode.

The resulting task view selected `13` edges and included all three requested semantic families, including:

\[
II.9\xrightarrow{\mathrm{ANALOGY\_TO}}II.6.
\]

## 3. Evidence/intention conflict

Task:

> `dla II.9 pokaż przesłanki dowodu i analogie, tylko pełne certyfikaty`

requests strict evidence mode:

\[
\mathrm{VALID\_FRAGMENT\_CERT\_ONLY}.
\]

The local graph contains an analogy candidate, but there is no fragment-certified `ANALOGY_TO` edge. Therefore the analogy intent has zero eligible coverage under the requested evidence contract.

The compiler returns:

\[
\boxed{
\mathrm{CONTRACT\_CONFLICT}
\to
\mathrm{NO\_RETRIEVAL}.
}
\]

It does not silently remove the analogy request and proceed with a weaker task.

## 4. Multiple-anchor conflict

Task:

> `sprawdź przesłanki dowodu II.9 i II.11.PSI-BRIDGE`

contains two explicit anchors.

Without a declared multi-anchor operation, the compiler returns:

\[
\boxed{
\mathrm{NEEDS\_ANCHOR\_POLICY}
\to
\mathrm{NO\_RETRIEVAL}.
}
\]

It does not choose the first, shortest or highest-priority anchor implicitly.

## 5. Strict mode is not itself a conflict

Task:

> `dla II.9 pokaż granice, tylko pełne certyfikaty`

is executable.

The strict selector returned `4` boundary edges, all belonging to the fragment-certified set, with:

\[
\boxed{\text{routing-attested leakage}=0}.
\]

Thus the evidence constraint is treated as a typed component of the contract rather than as a global error condition.

## 6. Architectural consequence

After M14 a retrieval contract has at least three independently typed components:

\[
\boxed{
\mathcal T=(A,I,E,B,S)
}
\]

where:

- \(A\) — anchor policy;
- \(I\) — requested semantic intent families;
- \(E\) — admissible evidence/attestation regime;
- \(B\) — retrieval budget;
- \(S\) — stopping rule.

Composition is legal only if these components admit a jointly executable interpretation.

This gives the stronger fail-closed rule:

\[
\boxed{
\text{requested semantics not realizable under requested evidence}
\Rightarrow
\text{explicit contract conflict},
}
\]

not silent task weakening.

## 7. Boundary

M14 still uses narrow lexical intent detection. It does not implement a general semantic parser or a multi-anchor execution algebra. In particular, requests such as comparison, intersection, transfer or synchronization between two anchors still require an explicit anchor-composition operator.

The next unresolved problem is therefore **multi-anchor semantics**, not another relation keyword: define typed operators such as `COMPARE(A,B)`, `INTERSECT(A,B)` or `TRANSFER(A→B)` and verify that they produce different, controlled retrievals rather than one merged neighbourhood.
