# PSI-MEMORY-M18-RESULT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36634954513` executed M1–M18 successfully.

M18 generalized exact conjunctive fibre refinement to finite set-valued observations and an explicit integer conflict budget without introducing scores or candidate ranking.

For observation supports `S_i` and tolerance `b >= 0`:

\[
\boxed{
F^{(b)}(O_1,\ldots,O_n)
=
\{x\in F_0:\#\{i:x\notin S_i\}\le b\}.
}
\]

For `b=0`, M16/M17 exact intersection is recovered.

## 2. Exact recovery

Clean singleton-valued observations with `b=0` produced:

\[
\boxed{24\to6\to3\to1}
\]

and status `IDENTIFIED_EXACT`.

## 3. Set-valued uncertainty

Allowing the position observation to mean either `WRIST` or `TABLE` produced:

\[
\boxed{24\to12\to6\to2}
\]

and the final state remained `UNRESOLVED`.

The resolver did not choose one of the two compatible objects.

## 4. Explicit tolerance without ranking

With four observations and `b=1`, the admissible fibre contained two objects. Both were returned. No score or preferred candidate was introduced.

For the same noisy five-observation packet:

- `b=0` -> empty fibre / `INCONSISTENT`;
- `b=1` -> singleton / `IDENTIFIED_WITH_TOLERANCE`;
- `b=2` -> wider multi-object fibre / `UNRESOLVED`.

Thus increasing tolerance changes the contract rather than adding evidence.

## 5. Monotonicity and order

For fixed `b`, every tested observation update was non-expansive:

\[
F_{k+1}^{(b)}\subseteq F_k^{(b)}.
\]

All `120` permutations of the five-observation `b=1` packet produced the same final singleton.

## 6. State separation

The experiment preserves distinct states:

- `NO_LEXICAL_FIBRE` — no language-relative candidate fibre exists;
- `INCONSISTENT` — a known fibre has no candidate satisfying the current contract;
- `UNRESOLVED` — several candidates remain compatible;
- `IDENTIFIED_EXACT` — singleton with zero violations;
- `IDENTIFIED_WITH_TOLERANCE` — singleton only under the explicit nonzero conflict budget.

## 7. Boundary

M18 uncertainty is deliberately non-probabilistic: finite categorical value sets plus an integer conflict budget. It does not implement likelihoods, weights, Bayesian inference, continuous errors, sensor models or learned confidence.

The result is operational:

\[
\boxed{
\text{partial/noisy evidence can preserve candidate-set semantics without nearest-match ranking.}
}
\]
