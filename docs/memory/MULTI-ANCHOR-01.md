# MULTI-ANCHOR-01

**Status:** EXPERIMENTAL / NON-CANONICAL  
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

Expected symmetry:

\[
\mathrm{COMPARE}(A,B)\cong\mathrm{COMPARE}(B,A)
\]

up to the left/right presentation order.

### INTERSECT

\[
\mathrm{INTERSECT}(A,B)=C_A\cap C_B
\]

using exact edge identity after two independently executed retrievals under the same contract and equal per-anchor budget.

Therefore:

\[
C_\cap\subseteq C_A,\qquad C_\cap\subseteq C_B,
\]

and

\[
\mathrm{INTERSECT}(A,B)=\mathrm{INTERSECT}(B,A).
\]

The implementation does not infer a "shared concept" from semantic similarity; an edge is common only if it is actually present in both retrieved views.

### TRANSFER

\[
\mathrm{TRANSFER}(A\to B)=\bigl(P_{A\to B},C_B\bigr)
\]

only if a directed path \(P_{A\to B}\) exists under the expandable relation policy and the declared route budget.

The route is checked **before** the target view is retrieved. Failure returns `NO_ROUTE`; the implementation does not invert edges and does not fall back to a merged local neighborhood.

For the frozen witness:

\[
II.9\xrightarrow{\mathrm{HARD\_DEPENDS\_ON}}II.7
\]

is legal, while the reverse transfer under the same proof-prerequisite contract is not.

## Budget contract

`COMPARE` and `INTERSECT` use `EQUAL_PER_ANCHOR`: both operands receive the same `per_anchor_edge_budget`. This is explicit; the total work allowance is twice the per-anchor allowance.

`TRANSFER` has a separate finite `route_budget`. Only after a legal route is found is the destination retrieval executed with the ordinary per-anchor budget.

## Evidence contract

All operand views call the existing `scripts/memory_retrieval.py` runtime. Therefore the Conversation-04 corrections remain binding:

- current fragment/source revalidation;
- no stale-certificate fallback;
- declared attestation mode;
- declared anchor and radius;
- explicit budget truncation.

`VALID_FRAGMENT_CERT_ONLY` propagates to both comparison/intersection operands and to every transfer-route edge.

## Language surface

The compiler is deliberately narrow. Current Polish operator markers are bounded fixtures (`porównaj`, `wspólne`, `przenieś`). This unit tests the algebra and execution contract, not general natural-language understanding.

## Regressions

`scripts/test_multi_anchor_retrieval.py` verifies:

1. two anchors without an operator fail closed;
2. `COMPARE` is symmetric up to anchor labels;
3. `INTERSECT` is commutative and introduces no edge absent from either operand;
4. `TRANSFER(II.9→II.7)` follows the stored direction;
5. `TRANSFER(II.7→II.9)` returns `NO_ROUTE` and does not fabricate an inverse dependency;
6. strict evidence mode propagates through operands and routes;
7. the three operators produce distinct output structures rather than aliases for one merged neighborhood;
8. malformed budgets are rejected.

## Boundary

This is an executable retrieval algebra over the current finite memory graph. It does not prove a general categorical algebra of contexts, does not solve arbitrary multi-anchor language, and does not authorize new PSI primitives.

The ordinary single-anchor runtime and M1–M19 remain unchanged.
