# MULTI-ANCHOR-01

**Status:** PASS_WITH_BOUNDARY / EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30

## Purpose

Close the Conversation-04 open item **multi-node composition** without opening a new numbered M-series experiment and without changing PSI core.

The rule is fail-closed:

\[
\boxed{\text{two anchors without an explicit operator}\Rightarrow\mathrm{NEEDS\_ANCHOR\_POLICY}.}
\]

A multi-anchor task must name exactly one of the supported operators and exactly two anchors.

## Operators

For a single-anchor certified retrieval \(R_{\mathcal T,B}(a)\):

### COMPARE

\[
\mathrm{COMPARE}(A,B)=\bigl(C_A,C_B,E_\times\bigr),
\]

where

\[
C_A=R_{\mathcal T,B}(A),\qquad C_B=R_{\mathcal T,B}(B),
\]

and \(E_\times\) contains only direct typed relations between the two anchors that are legal under the same relation/evidence contract.

The two views remain separate. `COMPARE` does not merge neighborhoods.

Regression result:

\[
\boxed{\mathrm{COMPARE}(A,B)\cong\mathrm{COMPARE}(B,A)}
\]

up to presentation order. For `II.9` and `II.7`, the stored cross-edge

\[
II.9\xrightarrow{\mathrm{HARD\_DEPENDS\_ON}}II.7
\]

remains directed inside the symmetric comparison object.

### INTERSECT

\[
\mathrm{INTERSECT}(A,B)=C_A\cap C_B
\]

using exact edge identity after two independently executed retrievals under the same contract and equal per-anchor budget.

The regressions establish for the frozen witness:

\[
C_\cap\subseteq C_A,\qquad C_\cap\subseteq C_B,
\]

\[
\boxed{\mathrm{INTERSECT}(A,B)=\mathrm{INTERSECT}(B,A)}.
\]

The implementation does not infer a "shared concept" from semantic similarity; an edge is common only if it is actually present in both retrieved views.

### TRANSFER

\[
\mathrm{TRANSFER}(A\to B)=\bigl(P_{A\to B},C_B\bigr)
\]

only if a directed path \(P_{A\to B}\) exists under the expandable relation policy and the declared route budget.

The route is checked **before** the target view is retrieved. Failure returns `NO_ROUTE`; the implementation does not invert edges and does not fall back to a merged local neighborhood.

Frozen witness:

\[
\boxed{\mathrm{TRANSFER}(II.9\to II.7)=\mathrm{RETRIEVED}}
\]

through the exact path

\[
II.9\xrightarrow{\mathrm{HARD\_DEPENDS\_ON}}II.7,
\]

while

\[
\boxed{\mathrm{TRANSFER}(II.7\to II.9)=\mathrm{NO\_ROUTE}}.
\]

Thus no inverse proof dependency is fabricated.

## Budget contract

`COMPARE` and `INTERSECT` use `EQUAL_PER_ANCHOR`: both operands receive the same `per_anchor_edge_budget`. This is explicit; the total work allowance is twice the per-anchor allowance.

`TRANSFER` has a separate finite `route_budget`. Only after a legal route is found is the destination retrieval executed with the ordinary per-anchor budget.

Malformed, negative or Boolean budgets are rejected.

## Evidence contract

All operand views call the existing `scripts/memory_retrieval.py` runtime. Therefore the Conversation-04 corrections remain binding:

- current fragment/source revalidation;
- no stale-certificate fallback;
- declared attestation mode;
- declared anchor and radius;
- explicit budget truncation.

`VALID_FRAGMENT_CERT_ONLY` is part of the contract, not a post-hoc filter.

This produced an important fail-closed witness. The pair `II.9 + II.7` under proof-prerequisite intent and strict evidence mode is **not jointly executable**, because the current memory has no non-empty fragment-certified proof-prerequisite view rooted at `II.7`. Therefore:

\[
\boxed{
\mathrm{STRICT}(II.9,II.7)
\Rightarrow
\mathrm{CONTRACT\_CONFLICT}
}
\]

with `STRICT_CERT_NO_EXECUTABLE_VIEW:II.7`; no empty strict view is reported as successful retrieval.

A positive strict control uses `II.9 + C58`: both operands have executable fragment-certified proof-prerequisite views, and every returned edge is `VALID_FRAGMENT_CERT`.

This preserves the M14 rule:

\[
\boxed{
\text{requested semantics not realizable under requested evidence}
\Rightarrow
\text{explicit contract conflict}.
}
\]

## Language surface

The compiler is deliberately narrow. Current Polish operator markers are bounded fixtures (`porównaj`, `wspólne`, `przenieś`). During regression the natural genitive form `przesłanek dowodu` exposed a missing lexical marker; the frozen proof-intent adapter now recognizes both nominative/accusative and genitive fixtures. This is a bounded parser correction, not a claim of general Polish understanding.

## Regression result

`scripts/test_multi_anchor_retrieval.py` verifies:

1. two anchors without an operator fail closed;
2. `COMPARE` is symmetric up to anchor labels;
3. `INTERSECT` is commutative and introduces no edge absent from either operand;
4. `TRANSFER(II.9→II.7)` follows the stored direction;
5. `TRANSFER(II.7→II.9)` returns `NO_ROUTE` and does not fabricate an inverse dependency;
6. strict evidence with an uncovered operand gives `CONTRACT_CONFLICT`;
7. strict evidence succeeds when both operand views are actually covered (`II.9 + C58`);
8. the three operators produce distinct output structures rather than aliases for one merged neighborhood;
9. malformed budgets are rejected.

GitHub Actions run `36643521416` passed the complete memory workflow: M1–M19, archive lineage/certification, Conversation-04 adversarial regressions and the multi-anchor regressions.

## Boundary

This is an executable retrieval algebra over the current finite memory graph. It does not prove a general categorical algebra of contexts, does not solve arbitrary multi-anchor language, and does not authorize new PSI primitives.

The ordinary single-anchor runtime and M1–M19 remain unchanged. `main` remains unchanged.
