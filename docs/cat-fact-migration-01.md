# PRINCIPIA — CAT / ADEQ / FACT MIGRATION 01

**Status:** `ALIGNMENT / REVIEW — NOT CANON-03 FREEZE`  
**Date:** 2026-09-28  
**Target:** current public CANON-03 derivative (`docs/core.md`) + Claim Registry v11  
**Source family:** `PSI_KANON_MATEMATYCZNY_STRICT_2026-07-16`, `PSI_KANON_NADRZEDNY_TRANS_vNEXT_2026-07-19`, `PRINCIPIA_SEMANTICA_KANON_SCALONY_2026-07-26A`.

## 0. Scope and source warning

This file performs a role-preserving migration comparison between strong older typed CAT/FACT sources and the current **public derivative** of CANON-03.

The physical authoritative CANON-03 artifact is not presently bound in this repository audit. Therefore this document may establish:

- compatibility with the current public core roles;
- definitions suitable for provisional V1/V2 units;
- conflicts that must not be reintroduced;

but it does **not** claim line-by-line identity with the missing physical CANON-03 source.

\[
\boxed{
\text{older source}\to\text{public-core alignment}
\neq
\text{canonical migration freeze}.
}
\]

---

# 1. Catalog adequacy

Older sources define a protocol-relative manifested behavior family

\[
\widetilde{\mathcal B}^{\mathcal P}_Q
\]

and a deterministic catalog defect in one of two equivalent notational forms when the same data pseudometric/topology is used:

\[
D_{\rm ADEQ}^{\rm beh}(\mathcal B;\mathcal P,Y)
=
\inf_{b\in\mathcal B}d_{\mathcal Y}(\operatorname{Obs}_{\mathcal P}(b),Y),
\]

\[
D_{\rm ADEQ}^{\rm cat}(Q;\mathcal P,Y)
=
D_{\rm ADEQ}^{\rm beh}(\widetilde{\mathcal B}^{\mathcal P}_Q;\mathcal P,Y),
\]

or

\[
D_{\rm ADEQ}(Q;\mathcal P,Y)
=
\operatorname{dist}
\left(Y,\overline{\widetilde{\mathcal B}^{\mathcal P}_Q}\right).
\]

A tolerance-relative adequacy predicate is

\[
\boxed{
\operatorname{ADEQ}_{\rm cat}(Q;\mathcal P,Y,\varepsilon)=1
\iff
D_{\rm ADEQ}^{\rm cat}(Q;\mathcal P,Y)\le\varepsilon.
}
\]

### Role alignment

This object is **not** a sixth CORE5 role. It is a derived test on a proposed candidate catalog under an observation protocol.

The current public core already requires the logical order

\[
\text{catalog adequacy}\to\text{fibre}\to\text{identifiability}.
\]

Therefore the older definition is role-compatible with current architecture, provided:

1. the data space / pseudometric is typed;
2. `Obs_P` is explicit;
3. nuisance closure is explicit if used;
4. `epsilon` is part of the contract;
5. the definition is not confused with task identification inside an already adequate catalog.

### Migration verdict

\[
\boxed{
\mathrm{ADEQ}_{cat}=\mathrm{ROLE\ COMPATIBLE / PROVISIONAL\ MIGRATION}.
}
\]

Canonical freeze remains pending physical CANON-03 source binding.

---

# 2. CAT — what survives

The older typed CAT calculus separates:

\[
\mathsf{ISO}_{\rm CAT}
=
\{\text{realization/port gauge}\},
\]

\[
\mathsf{HOR}_{\rm CAT}
=
\{\mathrm{recode}\},
\]

\[
\mathsf{REF}_{\rm CAT}
=
\{\mathrm{refine},\mathrm{split}_{\oplus},\mathrm{split}_{K},\mathrm{birth}\},
\]

\[
\mathsf{CRS}_{\rm CAT}
=
\{\mathrm{merge}_{\oplus},\mathrm{merge}_{K},\mathrm{death}\}.
\]

The crucial semantic statement is:

\[
\boxed{
\text{gauge is an isomorphism relation, not a catalog-changing morphism}.}
\]

The source also separates

\[
\boxed{\mathrm{GEN}\neq\mathrm{TEST}\neq\mathrm{SELECT}.}
\]

### Role alignment

Under the current public core, CAT is a **meta-level candidate/catalog problem**. One chooses an appropriate candidate class of catalogs/realizations and applies the same observation/compatibility/task discipline at that level.

Therefore the CAT calculus can migrate as a **derived typed module**, not as an enlargement of CORE5.

### What does not migrate automatically

The older promotion predicate containing fixed collections of novelty, persistence, LOGOS, feedback and risk conditions is not promoted wholesale. Such criteria remain protocol/domain policy until independently justified.

Likewise the historical hysteresis choice

\[
\tau_{birth}>\tau_{death}
\]

is a useful update policy, not a universal PSI theorem.

### Migration verdict

\[
\boxed{
\mathrm{CAT\ ROLES}=\mathrm{COMPATIBLE};
\quad
\mathrm{PROMOTION\ POLICY}=\mathrm{CONTRACT/DOMAIN\ SPECIFIC}.
}
\]

---

# 3. Observation and gauge descent

The TRANS source gives the correct prerequisite for quotient observation.

If `G` acts on candidates and

\[
\operatorname{OBS}_{\mathcal P}(g\cdot T)
=
\operatorname{OBS}_{\mathcal P}(T),
\]

then observation descends to the quotient:

\[
\overline{\operatorname{OBS}}_{\mathcal P}:
\mathscr X_{\mathcal P}/G
\to
\mathscr Y_{\mathcal P}.
\]

This is exactly the contract condition exposed by `MINI-GAUGE-OBS-01`.

### Migration verdict

\[
\boxed{
\text{gauge descent requires observation compatibility/equivariance}.}
\]

This is aligned with C60/C61 and current `core.md`.

---

# 4. FACT — general object

The older source states

\[
\boxed{
\mathrm{PSI\!-FACT}
=
\left.\mathrm{PSI\!-CAT}\right|_{\mathsf{FactMorph}}.
}
\]

PSI-FACT studies identifiability of **factorizations compatible with observation**, without assuming the full realization is known in advance.

A domain semantics is typed by

\[
\mathsf{Wire}_{\mathfrak D}
\xrightarrow{\operatorname{Sem}_{\mathfrak D}}
\mathsf{Sys}_{\mathfrak D}
\xrightarrow{\operatorname{Obs}_{\mathcal P}}
\mathsf{Beh}_{\mathcal P}.
\]

The realization-level object is a groupoid

\[
\mathsf{Fact}^{\simeq}_{\mathfrak D}
\]

whose objects are legal factorizations and whose morphisms are structural isomorphisms of factors, ports and diagrams. Stabilizers are retained as

\[
\operatorname{Aut}(F).
\]

The source then forms the compatibility object

\[
\boxed{
\mathfrak F^{\varepsilon}_{\mathfrak D,\mathcal P}(Y)
=
\mathsf{Fact}^{\simeq}_{\mathfrak D}
\times^{h}_{\mathsf{Beh}_{\mathcal P}}
\mathsf{Adeq}^{\varepsilon}_{\mathcal P}(Y),
}
\]

with fixed external-interface condition.

### Role alignment

This is compatible with current PSI only if the structured/higher object is treated as the **representation of the candidate/compatibility problem**, not as a new semantic primitive.

The HIGHER-FIBRE regression additionally forbids replacing this object by a coarse component/orbit set whenever witness multiplicity or stabilizers remain task-relevant.

### Relation to MINI

`CAT–FACT–NORM–MINI-01` uses restricted finite `{F,B}` set-level objects. They are legitimate when the contract makes all omitted higher data task-irrelevant, but they are not the general FACT definition.

### Migration verdict

\[
\boxed{
\mathrm{FACT\ GROUPOID/FIBRE}=\mathrm{ROLE\ COMPATIBLE / PROVISIONAL\ MIGRATION}.
}
\]

Canonical freeze remains pending physical CANON-03 binding.

---

# 5. Birth versus recode

The older typed calculus and the corrected MINI support the stable distinction:

- gauge: invertible realization/presentation equivalence;
- recode: external behavior preserved under a change of representation/realization not necessarily identical as implementation;
- refine/split/merge: factorization/catalog transformations;
- birth: a new semantic sector only when no legal fold/recode into the old catalog preserves the declared external behavior/interface.

Therefore a local representation singularity alone does not license `birth`.

This is exactly the status of the Frenet-to-Bishop repair at zero curvature under the MINI contract.

---

# 6. What remains blocked

The following are **not** resolved by this alignment file:

1. line-by-line comparison with a physical `PSI-R3-CONSOLIDATED-CANON-03` source artifact;
2. a universal theorem that the listed CAT morphism taxonomy is complete;
3. universal promotion thresholds for birth/death;
4. a theorem that every useful FACT problem requires the full homotopy-fibre type;
5. arbitrary higher-categorical dynamics beyond the tested groupoid-level witnesses.

---

# 7. Proposed V1/V2 placement

### V1

- catalog adequacy as a prerequisite and typed definition;
- gauge isomorphism versus catalog change;
- observation-compatible gauge descent principle;
- statement that representation is not the represented object.

### V2

- general FACT groupoid/compatibility object as a derived structured realization;
- exact factorization-identifiability questions;
- MINI as a proved finite benchmark;
- higher-fibre witness as a boundary on coarse truncation.

### V3

- domain-specific CAT promotion policies;
- detailed factorization grammars and laboratories.

---

# 8. Current verdict

Relative to the current public CANON-03 derivative:

\[
\boxed{
\mathrm{ADEQ/CAT/FACT\ ALIGNMENT=PASS\ WITH\ PROVENANCE\ HOLD}.
}
\]

The mathematical/semantic roles align; the remaining blocker is canonical source binding, not a newly discovered role conflict.
