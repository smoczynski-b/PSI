# PRINCIPIA SEMANTICA — V2 THEOREM MAP 02

**Status:** `CURRENT / POST-SPINE-CROSSCHECK CONTROL MAP`  
**Date:** 2026-09-28  
**Supersedes for control:** `principia-v2-theorem-map-01.md`  
**Canonical source:** physical `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Claim source:** `claim-registry-12.md`  
**Falsifier source:** `falsifier-registry-10.md`  
**Regression source:** `regression-bank-01.md`  
**Freeze:** `principia-v1-v2-freeze-01.md`  
**Spine audit:** `principia-v2-spine-crosscheck-01.md`

---

## 0. Zasada mapy

Mapa v01 pozostaje dokumentem genealogicznym. Mapa v02 odzwierciedla stan po:

- związaniu fizycznego CANON-03;
- Claim Registry v12;
- zamknięciu RED-1 C57–C59;
- migracji CAT/FACT C62–C66;
- Proof/Source/Migration Audit 01;
- V1 Normalized Pass;
- wykonaniu i cross-checku V2.1–V2.4.

Każda jednostka V2 ma mieć:

`TYPE | HYPOTHESES | STATEMENT | PROOF/SOURCE | SCOPE | FALSIFIER/REGRESSION | STATUS`.

---

## 1. Kręgosłup elementarny — wykonany

### II.1 — C06 Exact task-level decidability

\[
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)^2\subseteq E_{\mathcal T,c}.
\]

**STATUS:** `PASS`  
**CLASS:** classical elementary quotient fact / PSI-adapted central criterion.  
**BOUNDARY:** empty fibre gives cardinality 0.

### II.2 — C07 Kernel factorization

\[
\ker_{eq}\rho\subseteq\ker_{eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,
\quad R=g\circ\rho.
\]

**STATUS:** `PASS`  
**CLASS:** classical elementary factorization lemma / PSI-adapted tool.  
**FALSIFIER:** F60 — uniqueness only on `im rho`.

### II.3 — C08 Global observer sufficiency

\[
\ker_{eq}\Psi_c\subseteq E_{\mathcal T,c}
\iff
\exists!\,f:\operatorname{im}\Psi_c\to M_{\mathcal T,c},
\quad q_{\mathcal T,c}=f\circ\Psi_c.
\]

**STATUS:** `PASS`  
**CLASS:** PSI structural bridge / direct factorization corollary.  
**BOUNDARY:** global map property, not per-record decidability; not statistical sufficiency.

### II.4 — C09 Representation adequacy

\[
\ker_{eq}\rho\subseteq E_{\mathcal T,c}
\iff
\exists!\,g:\operatorname{im}\rho\to M_{\mathcal T,c},
\quad q_{\mathcal T,c}=g\circ\rho.
\]

**STATUS:** `PASS`  
**CLASS:** PSI central structural bridge.  
**BOUNDARY:** F57 — task-information adequacy is not full contract legality.  
**REGRESSION:** R01/R02 direct; R03 scope boundary.

### Spine verdict

\[
\boxed{
\mathrm{V2.1:V2.4}=\mathrm{PASS}.
}
\]

No Freeze 01 erratum required.

---

## 2. Następne corollarium — obowiązkowe przed dynamiką

### II.5 — C32/C37 Task-information legality of reduction / quotient

For proposed reduction

\[
q:\Omega_c\to Z,
\]

exact preservation of task information requires

\[
\boxed{
\ker_{eq}q\subseteq E_{\mathcal T,c}.
}
\]

Equivalently the task quotient factors through `q` on `im q`.

**DEPENDS ON:** II.4.  
**STATUS:** `NEXT / READY`.  
**MANDATORY BOUNDARY:** F57.  
**INTERPRETATION:** `task-information legal`, not automatically `fully contract-legal`.  
**REGRESSION:** HIGHER-FIBRE; R02; corrected MINI gauge-observation case as scope warning.

---

## 3. Dynamic / history quotient layer

### II.6 — C10 Deterministic quotient dynamics

For `delta:Omega->Omega`, equivalence `E`, quotient map `q`, a unique

\[
\bar\delta:\Omega/E\to\Omega/E,
\qquad
\bar\delta\circ q=q\circ\delta
\]

exists iff

\[
xEy\Rightarrow\delta(x)E\delta(y).
\]

**STATUS:** `READY AFTER II.5`.  
**CLASS:** classical congruence criterion / PSI-adapted dynamic quotient.  
**BOUNDARY:** deterministic theorem; stochastic kernels require separate lumpability conditions.

### II.7 — C42 Exact history-memory adequacy

With future-task equivalence C57/C58:

\[
\boxed{
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
}
\]

**STATUS:** `READY`; former V2-GAP-01 is closed by C57–C59.  
**DEPENDS ON:** II.4 + registered history equivalence.  
**REGRESSION:** R02.

### II.8 — C44 Coarsest exact history quotient

\[
M_{\mathcal T,t}
=
\mathcal H_t/\!\equiv_{\mathcal T,t}
\]

and every exact sufficient `rho_t` factors uniquely to it on `im rho_t`.

**STATUS:** `READY`.  
**DEPENDS ON:** II.2, II.7.  
**BOUNDARY:** coarsest exact quotient in quotient order; not minimum bits/dimension/storage/compute.

### II.9 — C45 Recursive quotient update

For a typed legal update and congruence of history equivalence:

\[
U_{\mathcal T,t}([H_t],\varepsilon_t,y_{t+1})
=
[\delta_t(H_t,\varepsilon_t,y_{t+1})]_{\mathcal T,t+1}
\]

is well-defined.

**STATUS:** `READY WITH EXPLICIT DOMAIN TYPING`.  
**BOUNDARY:** mathematical recurrence does not imply finite memory, computability or efficiency.  
**REGRESSION:** R02 / F43.

---

## 4. Classical bridge layer — after own quotient results

### Lumpability — C13

Strong lumpability remains a classical theorem plus conditional PSI bridge. Task equivalence alone does not imply stochastic lumpability.

**STATUS:** `SOURCE-BOUND / DEFER UNTIL AFTER II.9`.

### Myhill–Nerode — C18

PSI future-test equivalence realizes Nerode equivalence under continuation-test closure.

**STATUS:** `BRIDGE READY / CLASSICAL ATTRIBUTION REQUIRED`.

### Paige–Tarjan — C14

Classical algorithmic benchmark only, not PSI theorem.

### Probabilistic bisimulation

Remains explanatory comparison without C-ID because no frozen theorem depends on it.

---

## 5. CAT / FACT / FRAME / higher structure

Current canonical definitions are C62/C63. Older richer groupoid/homotopy structures are derived extensions under C66.

- CAT/FACT MINI C19-v2 remains a scoped theorem/benchmark after gauge-observation repair;
- CLOSED-FRAME and HIGHER-FIBRE remain typed pressure/representation results;
- higher/groupoid information is retained only when task/contract requires it;
- no old source is automatically promoted to current canon (F58/F59).

These units come after the elementary and dynamic/history quotient spine.

---

## 6. Current execution order

\[
\boxed{
\mathrm{II.1:II.4\ PASS}
\to
\mathrm{II.5\ REDUCTION/QUOTIENT}
\to
\mathrm{II.6\ DYNAMICS}
\to
\mathrm{II.7:II.9\ HISTORY}
\to
\mathrm{CLASSICAL\ BRIDGES}
\to
\mathrm{CAT/FACT/FRAME/HIGHER}.
}
\]

No new primitive, Agent version or benchmark is licensed by this map. It coordinates already frozen material.
