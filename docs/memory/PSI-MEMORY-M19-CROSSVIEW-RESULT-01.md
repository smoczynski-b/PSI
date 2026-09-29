# PSI-MEMORY-M19-CROSSVIEW-RESULT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36635237991` executed M1–M19 successfully.

M19 adds a read-only cross-object relation view to the experimental memory.

For selected object set `X` and relation family set `R`, the forward projection is

\[
\boxed{
\operatorname{Profile}_{R}(x)=\{(r,y):r\in R,\ x\xrightarrow r y\}.
}
\]

The inverse projection is

\[
\boxed{
\operatorname{Dist}_{r,X}(y)=\{x\in X:x\xrightarrow r y\}.
}
\]

Thus the memory can now be viewed both object-first and relation-first.

## 2. World-domain witness

Across the 24-object M17 domain, CrossView recovered:

- `POSITION`: `4` values with `6` objects each;
- `MECHANISM`: `2` values with `12` objects each;
- `FUNCTION`: `3` values with `8` objects each;
- `MEASURES=TIME`: `24/24` objects.

The same source relations can therefore be inspected as a matrix over objects or as grouped distributions over relation values.

## 3. Native PSI memory witness

The operator also runs over native memory edges. For `HARD_DEPENDS_ON` it exposes, among others,

\[
II.9\to II.7,
\qquad
II.7\to II.4,
\qquad
C58\to C57.
\]

The inverted view makes shared dependency targets directly visible:

\[
y\mapsto\{x:x\xrightarrow{HARD\_DEPENDS\_ON}y\}.
\]

This avoids reconstructing the same cross-object pattern separately from each node-local view.

## 4. Multi-relation matrix

For selected objects, CrossView can project several relation families simultaneously. This yields a relational comparison matrix in which rows are objects and columns are relation families, while the inverse representation groups objects by common relation targets/values.

## 5. Architectural consequence

The memory now has two complementary observational orientations:

\[
\boxed{
\text{OBJECT}\to\text{RELATIONS}
}
\]

and

\[
\boxed{
\text{RELATION}\to\text{DISTRIBUTION ACROSS OBJECTS}.
}
\]

No new memory fact is created. CrossView is a projection over already stored relations.

## 6. Boundary

Counts and shares are descriptive relative to the selected finite domain:

\[
\boxed{
\text{frequency}\neq\text{truth strength}\neq\text{causal strength}.
}
\]

M19 does not yet aggregate uncertain M18 fibres, temporal versions, weighted relations or continuous measurements.
