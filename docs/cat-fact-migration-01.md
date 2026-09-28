# PRINCIPIA — CAT / ADEQ / FACT MIGRATION 01

**Status:** `PHYSICAL CANON BOUND / CURRENT ROLE MIGRATION PASS`  
**Date:** 2026-09-28  
**Physical target:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Pinned source:** `smoczynski-b/psi-model@7e64ec8ad766623ffeede3daa4bb68dee15135c1`  
**Path:** `psi-agent/canon/PSI-R3-CONSOLIDATED-CANON-03.md`

## 0. Migration rule

Physical CANON-03 has priority over older CAT/FACT sources.

Therefore this migration distinguishes:

\[
\boxed{
\text{CURRENT CANONICAL DEFINITION}
\mid
\text{COMPATIBLE DERIVED EXTENSION}
\mid
\text{HISTORICAL/DOMAIN POLICY}.
}
\]

Older typed detail is retained only where it does not overwrite the current physical canon.

---

# 1. Catalog adequacy

## Current canonical content

Physical CANON-03 freezes the logical order

\[
\boxed{
\text{ADEQUACY OF CATALOG}
\to
\text{FIBRE}
\to
\text{LOCAL IDENTIFIABILITY}
\to
\text{GLOBAL IDENTIFIABILITY}
\to
\text{PROTOCOL DESIGN}.
}
\]

It does not make one particular scalar metric `D_ADEQ^cat` a CORE primitive.

## Older derived adapter

Older sources define, when a data pseudometric/loss and manifested behavior family are part of the contract,

\[
D_{\rm ADEQ}^{\rm beh}(\mathcal B;P,Y)
=
\inf_{b\in\mathcal B}d_{\mathcal Y}(\operatorname{Obs}_{P}(b),Y),
\]

\[
D_{\rm ADEQ}^{\rm cat}(Q;P,Y)
=
D_{\rm ADEQ}^{\rm beh}(\widetilde{\mathcal B}^{P}_{Q};P,Y),
\]

or an equivalent distance-to-closure form under the same topology.

These remain valid **contract-specific adequacy adapters** when their metric/loss assumptions are declared.

They are not a universal foundational definition required by V1.

### Migration verdict

\[
\boxed{
D_{ADEQ}^{cat}=\mathrm{DERIVED\ ADAPTER},
\quad
\text{not universal CORE definition}.
}
\]

This resolves the former `V1-GAP-01` by scope correction.

---

# 2. PSI-CAT

## Current canonical definition

Physical CANON-03 states:

- `PSI-ID` studies identifiability inside a fixed catalog;
- `PSI-CAT` studies whether data/protocol justify a catalog change and, if so, which class of changes is justified;
- `PSI-CAT^D` adds domain-admissibility conditions `ADM_D`;
- domain constraints may eliminate illegal hypotheses but are not new empirical observations.

It freezes

\[
\boxed{\mathrm{PSI-ID}\neq\mathrm{PSI-CAT}.}
\]

This is the current canonical CAT definition for V1/V2.

## Compatible older derived calculus

The older taxonomy

\[
\mathsf{ISO}_{CAT},\quad
\mathsf{HOR}_{CAT},\quad
\mathsf{REF}_{CAT},\quad
\mathsf{CRS}_{CAT}
\]

with gauge/recode/refine-split-birth/merge-death distinctions is compatible as a **derived typed calculus**.

Likewise

\[
\mathrm{GEN}\neq\mathrm{TEST}\neq\mathrm{SELECT}
\]

is a useful derived workflow discipline.

Neither taxonomy is promoted as an exhaustive theorem that all possible catalog changes must belong to exactly those named classes.

Older promotion thresholds, persistence/feedback criteria and birth/death hysteresis remain domain/protocol policy unless separately justified.

### Migration verdict

\[
\boxed{
\mathrm{PSI-CAT\ CURRENT}=\mathrm{PHYSICAL\ CANON\ DEFINITION};
\quad
\mathrm{OLDER\ CALCULUS}=\mathrm{DERIVED}.
}
\]

---

# 3. Observation and gauge descent

A separate older TRANS source states the correct descent condition: if a group acts on realizations, quotient observation requires invariance/equivariance of the observation contract.

This is consistent with physical CANON-03, which defines `Omega_c` only after a **legal** realization quotient when the contract requires it, and defines PSI-FACT gauge only when the contract establishes it.

Therefore:

\[
\boxed{
\text{geometric symmetry}
\not\Rightarrow
\text{automatic gauge of a fixed observation fibre}.
}
\]

The corrected MINI C19-v2 is the permanent witness.

---

# 4. PSI-FACT

## Current canonical definition

For domain `D`, protocol `P`, tolerance `epsilon` and data `Y`, physical CANON-03 defines

\[
\boxed{
\operatorname{Fact}^{\varepsilon}_{D,P}(Y)
}
\]

as the fibre of factorizations compatible with observation and protocol.

Objects must satisfy:

- `ADM_D`;
- the fixed external interface;
- the declared data-compatibility criterion.

Realization equivalence/gauge is quotiented **if the contract establishes it**.

The canon also freezes

\[
\boxed{
\text{realization equivalence}
\neq
\text{behavioural recoding}.
}
\]

A one-way recoding need not be an equivalence.

This is the current canonical FACT definition for V2.

## Older structured extension

Older typed sources introduce:

- a factorization groupoid with structural isomorphisms/stabilizers;
- a weak/homotopy ADEQ compatibility fibre preserving witness multiplicity.

These are compatible **derived extensions** when the contract/task needs stabilizers, compatibility witnesses or higher/groupoid structure.

They are not the minimal physical CANON-03 definition and must not be inserted into V2 as if the canon universally required a homotopy fibre.

The HIGHER-FIBRE regression supplies the boundary:

\[
\boxed{
\text{coarse truncation is illegal when discarded higher data are task-relevant}.}
\]

### Relation to MINI

The corrected Frenet/Bishop MINI uses a restricted finite set-level grammar fibre. It is legal precisely because, under its frozen contract, the omitted structured data are not needed for the tested task.

### Migration verdict

\[
\boxed{
\mathrm{PSI-FACT\ CURRENT}=\mathrm{PHYSICAL\ CANON\ DEFINITION};
\quad
\mathrm{GROUPOID/HOMOTOPY\ FACT}=\mathrm{DERIVED\ EXTENSION}.
}
\]

---

# 5. Birth versus recode

The current canon explicitly separates realization equivalence from behavioural recoding. Older CAT material and MINI further supply a useful derived distinction between recode and catalog birth.

The safe V1/V2 statement is:

\[
\boxed{
\text{failure of one representation}
\not\Rightarrow
\text{necessity of catalog birth}.
}
\]

A birth claim requires the CAT contract to establish that no legal existing representation/recode preserves the relevant external/task semantics.

Frenet failure at zero curvature remains the fixed MINI boundary witness.

---

# 6. Placement in Principia

## V1

Canonical:
- PSI-ID versus PSI-CAT;
- catalog adequacy as a prior gate, without imposing one universal metric;
- domain admissibility is not new observation;
- legal gauge requires the contract to establish the equivalence.

Derived/boundary boxes:
- older scalar `D_ADEQ` adapter;
- observation/gauge descent example.

## V2

Canonical:
- `Fact^epsilon_{D,P}(Y)` definition;
- realization-equivalence versus recoding distinction;
- corrected MINI exact theorem.

Derived extensions:
- CAT `ISO/HOR/REF/CRS` calculus;
- factorization groupoid/homotopy compatibility object;
- HIGHER-FIBRE boundary on coarse truncation.

## V3

- domain-specific promotion policies;
- detailed factorization grammars;
- CAT/FACT laboratories.

---

# 7. What remains noncanonical

Do not promote as universal current canon without a new explicit theorem:

1. completeness of the older CAT morphism taxonomy;
2. universal `D_ADEQ` metric independent of protocol topology/loss;
3. universal birth/death thresholds or hysteresis;
4. universal necessity of homotopy/groupoid FACT;
5. arbitrary higher-categorical dynamics.

---

# 8. Final migration verdict

The physical source bind removes the previous provenance hold.

\[
\boxed{
\mathrm{CAT/ADEQ/FACT\ MIGRATION\ 01}=\mathrm{PASS}
}
\]

with the status split:

\[
\boxed{
\text{physical CANON-03 minimal definitions}
\;>\;
\text{compatible older derived machinery}.
}
\]

No CORE5 change is required.
