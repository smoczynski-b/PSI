# PSI — claim registry 01

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`  
**Purpose:** keep mathematical claims, imported results, policies and open bridges type-separated during the Principia redaction.

This registry is deliberately small. It records only claims already needed by the public core. It is not a complete inventory of the internal project.

## Registry schema

Each entry has:

- `ID` — stable public identifier;
- `CLAIM` — the mathematical or methodological statement;
- `STATUS` — `CLASSICAL | BRIDGE | PSI-NEW | POLICY | OPEN`;
- `ROLE` — `ADAPTED | GENEALOGICAL | BENCHMARK | CORE | —`;
- `DEPENDENCIES` — earlier claims / definitions;
- `EVIDENCE` — proof status or source class;
- `PRINCIPIA` — intended destination.

`STATUS` and `ROLE` are independent axes.

---

## C01 — contract-relative CORE5

**CLAIM**

\[
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
\]

The meaning of candidate, observation, compatibility, task distinction and admissible evolution is relative to the declared contract `c`.

**STATUS:** `PSI-NEW` as PSI architecture; components may be classical.  
**ROLE:** `CORE`  
**DEPENDENCIES:** typed sets/maps/relations.  
**EVIDENCE:** canonical definition, not a theorem.  
**PRINCIPIA:** `V1`.

---

## C02 — compatible fiber

For observed data `Y`,

\[
\mathcal K_c^Y=\{b:(b,Y)\in\mathcal K_c\},
\qquad
F_c(Y)=\Psi_c^{-1}(\mathcal K_c^Y).
\]

**STATUS:** `PSI-NEW` as architectural role; inverse-image/set construction is classical.  
**ROLE:** `CORE`  
**DEPENDENCIES:** `C01`.  
**EVIDENCE:** definition.  
**PRINCIPIA:** `V1`.

Interpretive restriction:

\[
\boxed{\text{observation}\neq\text{identified hidden object}.}
\]

This is a `POLICY`/methodological consequence, not a separate mathematical theorem.

---

## C03 — task closure

\[
\mathscr R_{\mathcal T,c}
=
\operatorname{Cl}^{\mathcal T}_{\delta_c}(\mathscr O_{\mathcal T,c})
\]

is the smallest family containing the declared task observables and closed under the task operations/transports admitted by contract `c`.

**STATUS:** `PSI-NEW` as contract-relative construction.  
**ROLE:** `CORE`  
**DEPENDENCIES:** `C01`.  
**EVIDENCE:** definition; every concrete realization must specify its admitted operations/transports.  
**PRINCIPIA:** `V1`.

Open boundary: stochastic transition kernels require their own typed realization; deterministic notation must not be silently reused.

---

## C04 — exact equivalence kernel

For `R:Ω→W`,

\[
\ker_{\rm eq}R=\{(x,y)\in\Omega^2:R(x)=R(y)\}.
\]

**STATUS:** `CLASSICAL`  
**ROLE:** `ADAPTED`  
**DEPENDENCIES:** equality in codomain `W`.  
**EVIDENCE:** elementary definition.  
**PRINCIPIA:** `V1/V4` provenance note.

---

## C05 — task equivalence and quotient

\[
E_{\mathcal T,c}
=
\bigcap_{R\in\mathscr R_{\mathcal T,c}}
\ker_{\rm eq}R,
\qquad
M_{\mathcal T,c}=\Omega_c/E_{\mathcal T,c}.
\]

**STATUS:** `PSI-NEW` as task-relative architecture; intersection/quotient constructions are classical.  
**ROLE:** `CORE`  
**DEPENDENCIES:** `C03`, `C04`.  
**EVIDENCE:** each `ker_eq R` is an equivalence relation; intersection of equivalence relations is an equivalence relation.  
**PRINCIPIA:** `V1/V2`.

---

## C06 — exact task-level decidability

\[
\boxed{
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)^2\subseteq E_{\mathcal T,c}.
}
\]

**STATUS:** `CLASSICAL` as an elementary quotient fact; PSI-specific content lies in how `F` and `E_T` are constructed.  
**ROLE:** `ADAPTED` / central PSI criterion  
**DEPENDENCIES:** `C02`, `C05`.  
**EVIDENCE:** elementary quotient proof.  
**PRINCIPIA:** `V2`.

No novelty claim is made for the set-theoretic equivalence itself.

---

## C07 — elementary factorization criterion

For maps `ρ:Ω→Z`, `R:Ω→W`,

\[
\boxed{
\ker_{\rm eq}\rho\subseteq\ker_{\rm eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,
\quad R=g\circ\rho.
}
\]

**STATUS:** `CLASSICAL`  
**ROLE:** `ADAPTED`  
**DEPENDENCIES:** `C04`.  
**EVIDENCE:** elementary factorization through fibers/equivalence classes.  
**PRINCIPIA:** `V2/V4` provenance.

Measurable/topological/smooth variants require their own hypotheses and are not implied by this bare set-theoretic statement.

---

## C08 — global task sufficiency

Let

\[
E_{\Psi}=\ker_{\rm eq}\Psi.
\]

Then

\[
\boxed{
E_{\Psi}\subseteq E_{\mathcal T}
\iff
\exists!\,f:\operatorname{im}\Psi\to M_{\mathcal T},
\quad q_{\mathcal T}=f\circ\Psi.
}
\]

**STATUS:** `BRIDGE` / PSI formulation of `C07` for the observation-task architecture.  
**ROLE:** `CORE`  
**DEPENDENCIES:** `C05`, `C07`.  
**EVIDENCE:** direct specialization of `C07`.  
**PRINCIPIA:** `V2`.

---

## C09 — representation adequacy

For a representation `ρ`, exact task adequacy is

\[
\boxed{\ker_{\rm eq}\rho\subseteq E_{\mathcal T}.}
\]

**STATUS:** `BRIDGE`  
**ROLE:** `CORE` / `ADAPTED`  
**DEPENDENCIES:** `C05`, `C07`.  
**EVIDENCE:** factorization interpretation.  
**PRINCIPIA:** `V2`.

---

## C10 — deterministic quotient dynamics

For deterministic `δ:Ω→Ω` and equivalence relation `E`, a unique map

\[
\bar\delta:\Omega/E\to\Omega/E,
\qquad
\bar\delta\circ q=q\circ\delta,
\]

exists iff

\[
\boxed{xEy\Rightarrow\delta(x)E\delta(y).}
\]

**STATUS:** `CLASSICAL`  
**ROLE:** `BENCHMARK` / `ADAPTED`  
**DEPENDENCIES:** quotient well-definedness.  
**EVIDENCE:** elementary proof.  
**PRINCIPIA:** `V2/V4` provenance.

Stochastic aggregation is not licensed by this condition; lumpability is the classical reference case.

---

## C11 — logical order of PSI work

\[
\boxed{
\text{catalog adequacy}
\to
\text{fiber}
\to
\text{local identifiability}
\to
\text{global identifiability}
\to
\text{protocol design}
}
\]

**STATUS:** `POLICY`  
**ROLE:** `CORE` working discipline  
**DEPENDENCIES:** `C01–C09`.  
**EVIDENCE:** methodological rule, not theorem.  
**PRINCIPIA:** `V1`.

---

## C12 — conservative primitive rule

\[
\boxed{\text{new primitive only when the semantic role truly changes}.}
\]

**STATUS:** `POLICY`  
**ROLE:** architecture governance  
**DEPENDENCIES:** none.  
**EVIDENCE:** project rule.  
**PRINCIPIA:** editorial preface / `V1`.

This rule blocks automatic promotion of higher fibers, frame changes, memory, factorization spaces, operator models or domain laboratories into CORE5.

---

## C13 — stochastic equivalence / lumpability bridge

**CLAIM:** precise coincidence conditions between PSI task-equivalence under stochastic dynamics and classical lumpability remain to be stated case-by-case.

**STATUS:** `OPEN`  
**ROLE:** `BENCHMARK`  
**DEPENDENCIES:** `C03`, `C05`, `C10`.  
**EVIDENCE:** classical lumpability lineage exists; no universal coincidence theorem is asserted here.  
**PRINCIPIA:** `V2/V4` when resolved.

---

## C14 — finite partition-refinement bridge

**CLAIM:** finite algorithms advertised as computing a coarsest dynamically stable PSI partition must be compared with classical partition-refinement methods (e.g. Paige–Tarjan) under explicit hypotheses.

**STATUS:** `OPEN` / `POLICY` until a concrete theorem/algorithm is fixed.  
**ROLE:** `BENCHMARK`  
**DEPENDENCIES:** `C05`, `C10`.  
**EVIDENCE:** classical algorithmic lineage.  
**PRINCIPIA:** `V2/V3/V4` depending result.

---

## C15 — old Model ψ metrics

**CLAIM:** `T/R/E/χ`, `χ_multi`, `Δψ` are historical protocol-level observables derived from selected embedding representations; they are not current PSI primitives.

**STATUS:** `POLICY` (classification of historical material)  
**ROLE:** `GENEALOGICAL` / laboratory observable  
**DEPENDENCIES:** migration registry.  
**EVIDENCE:** historical Principia implementations.  
**PRINCIPIA:** `V3/V4`.

---

## C16 — old field ontologies

**CLAIM:** STPψ/GTPψ, TAO/SMOK and universal semantic-field formulations do not define the current PSI core. They may be retained as genealogy or independently typed realizations.

**STATUS:** `POLICY` (supersession statement)  
**ROLE:** `GENEALOGICAL`  
**DEPENDENCIES:** `C01`, migration registry.  
**EVIDENCE:** later CANON-03 priority.  
**PRINCIPIA:** `V4`; selected realizations may enter `V3`.

---

## C17 — SOP-11b resonance claims

**CLAIM:** reproducible preprocessing/provenance machinery may be retained as a laboratory protocol, while fixed-threshold or universal resonance assertions require explicit stochastic assumptions, calibration and proof before theorem status.

**STATUS:** `OPEN` / `POLICY`  
**ROLE:** laboratory / `BENCHMARK`  
**DEPENDENCIES:** migration registry.  
**EVIDENCE:** historical Universalia protocol; theorem-strength claims not imported automatically.  
**PRINCIPIA:** `V3/V4`.

---

## Promotion rule

A new entry may be promoted into the current theorem layer only after:

\[
\boxed{
\text{TYPE}
\land
\text{SOURCE}
\land
\text{STATUS}
\land
\text{PROOF/TEST}
\land
\text{CANON-COMPATIBILITY}
}
\]

For dual-use material add the publication gate:

\[
\mathrm{PUBLIC}\mid\mathrm{REVIEW}\mid\mathrm{WITHHOLD}.
\]

This registry should grow by claim, not by document.