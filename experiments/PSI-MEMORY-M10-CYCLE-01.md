# PSI-MEMORY-M10-CYCLE-01 — READ → WORK → ADMIT → READ′

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## Question

Does an admitted M9 delta change ordinary task retrieval exactly where its verified relation becomes reachable, while leaving audit-only conflict outside usable context?

## Frozen witness

Anchor: `GO-G4`.

M9 admitted:

\[
\mathrm{II.9}\xrightarrow{\mathrm{DOES\_NOT\_IMPLY}}\mathrm{BIT\!\!-
MINIMALITY}.
\]

The competing candidate

\[
\mathrm{II.9}\xrightarrow{\mathrm{IMPLIES}}\mathrm{BIT\!\!-
MINIMALITY}
\]

remains `CONFLICT_UNVERIFIED` in the audit ledger.

## Predictions

Because `II.9` is at distance 2 from `GO-G4`, the admitted object is at distance 3.

Therefore:

1. radius 2: pre-M9 and post-M9 usable views are identical;
2. radius 3: post-M9 adds exactly one node and one edge;
3. the `CONFLICT_UNVERIFIED` edge never enters normal retrieval;
4. if M9 evidence becomes `STALE` or `SOURCE_DRIFT`, strict retrieval reverts exactly to the pre-M9 view.

## Boundary

M10 tests composition of already-existing read and admission machinery. It does not claim that the M9 semantic verifier is general, nor does it measure LLM answer quality.
