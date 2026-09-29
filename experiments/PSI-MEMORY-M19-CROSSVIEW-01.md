# PSI-MEMORY-M19-CROSSVIEW-01

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can the memory expose the distribution of the same relation families across different objects without changing the underlying graph or confusing frequency with truth or causation?

## 1. Dual read projection

For a selected object set `X` and relation family `R`, define the object-side profile

\[
\operatorname{Profile}_{R}(x)
=
\{(r,y):r\in R,\ x\xrightarrow r y\},
\qquad x\in X.
\]

The inverse distribution view is

\[
\operatorname{Dist}_{r,X}(y)
=
\{x\in X:x\xrightarrow r y\}.
\]

Thus the same edge data can be viewed either per object or per shared relation target.

## 2. Two supported domains

`relation_crossview.py` exposes the same read pattern over:

1. native PSI memory edges (`from`, `relation`, `to`);
2. the M17 relational world table, where columns act as typed relation families.

The operator is read-only. It creates no nodes or edges and does not alter validity states.

## 3. Frozen witnesses

### World distribution

Across the 24-object M17 world:

- `POSITION`: four values, six objects each;
- `MECHANISM`: two values, twelve objects each;
- `FUNCTION`: three values, eight objects each;
- `MEASURES=TIME`: all 24 objects.

This provides a direct cross-object view of discriminating, partially discriminating and globally shared relations.

### Native memory graph

For `HARD_DEPENDS_ON`, the view must include at least:

\[
II.9\to II.7,
\qquad
II.7\to II.4,
\qquad
C58\to C57.
\]

The inverse view groups all subjects sharing a dependency target.

## 4. Interpretation rule

Counts and shares are descriptive properties of the selected finite domain:

\[
\boxed{
\text{frequency in CrossView}\neq\text{truth strength}\neq\text{causal strength}.
}
\]

CrossView is a lens over memory, not an epistemic promotion rule.

## 5. Boundary

The current implementation is exact and categorical. It does not yet aggregate uncertain M18 fibres, temporal change, weighted relations or continuous measurements.
