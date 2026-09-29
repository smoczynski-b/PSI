# PSI-MEMORY-M3-01 — distant bridge test

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can a task-local memory view reach a mathematically relevant remote cluster through one source-attested bridge without loading the full PSI repository context?

The selected start node is the frozen Go situational-superko regression `GO-G4`. The remote cluster is the history-memory theory around II.7 and II.9.

This is not a semantic-similarity test. The bridge is admitted only because current sources explicitly bind the Go regression bank to exact history-memory adequacy and recursive quotient-update conditions.

## 1. Source evidence

`docs/go-memory-regression-01.md` states that G0/G2/G3/G4 are finite regressions for the criterion

\[
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t},
\]

and treats the canonical history quotient and recursive update separately from bit/storage/compute minimality.

`docs/principia-v2-07-exact-history-memory-adequacy.md` explicitly names Go R02 as a memory regression.

`docs/principia-v2-09-recursive-history-quotient-update.md` explicitly states that Go R02 tests both class-invariant legality of an action label and representative-independent successor class, i.e. the conditions required for a well-defined quotient update.

Therefore the materialized path is:

```text
GO-G4
  --MEMBER_OF-->
GO-MEMORY-REGRESSION
  --REGRESSION_FOR--> II.7
  --REGRESSION_FOR--> II.9
```

The bridge does not assert that Go proves II.7 or II.9. It says that the frozen Go cases are regression witnesses for those abstract criteria.

## 2. M3 reachability test

Before adding the bridge edge set, `GO-G4` has no path in the memory-theory graph to II.7 or II.9.

After adding the source-attested bridge:

\[
d(GO\!\!-
G4,II.7)=2,
\qquad
d(GO\!\!-
G4,II.9)=2.
\]

For a directed radius-3 view, allow only:

- `MEMBER_OF`;
- `REGRESSION_FOR`;
- `HARD_DEPENDS_ON`;
- `USES_DEFINITION`;
- `USES_LEMMA`.

The expected useful view is bounded to:

```text
GO-G4
GO-MEMORY-REGRESSION
II.7
II.9
II.4
C57
C58
```

`ANALOGY_TO`, `NOT_DEPENDS_ON`, evidence indexing, scheduling and unrelated classical bridges are not pulled into this view.

## 3. Architectural result

M3 tests a property different from embedding similarity:

\[
\boxed{
\text{a sparse explicit bridge can reduce graph distance while preserving a small active context.}
}
\]

The full shared memory may be large, while a task view remains small:

\[
\operatorname{View}_{GO-G4,3}(\mathcal M_{PSI})\ll\mathcal M_{PSI}.
\]

This is the first concrete mechanism by which the proposed memory graph can increase agent reach without requiring full-history loading.

## 4. Scope discipline

- GO-G4 remains a LAB/regression object, not a theorem premise.
- II.7 and II.9 remain independently justified mathematical units.
- The bridge carries `effect=NONE`; revoking GO-G4 must not invalidate II.7 or II.9.
- Conversely, invalidating the abstract criterion may change the interpretation of the regression without altering the historical Go observation itself.

This directional asymmetry is intentional and is another reason typed edges are required.

## 5. Next test

M4 should measure context compression with an actual agent task rather than graph-node count alone: compare broad repository reconstruction against a generated task view for the same Go-memory question.
