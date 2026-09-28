# PSI — claim registry 09

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-08.md` as current public registry  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`

This version adds `GO-MEMORY-REGRESSION-01`. CORE5 and Agent Architecture v02 remain unchanged.

## Retained claims C01–C41

Retain C01–C41 from `claim-registry-08.md` without semantic change.

---

## C42 — exact memory adequacy criterion

For a history representation

\[
\rho_t:\mathcal H_t\to R_t,
\]

exact task sufficiency is

\[
\boxed{
\ker_{eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

Equivalently,

\[
\rho_t(H)=\rho_t(H')
\Rightarrow
H\equiv_{\mathcal T,t}H'.
\]

A single counterexample pair with equal representation and different future task semantics falsifies sufficiency.

**STATUS:** `BRIDGE / REPRESENTATION-ADEQUACY SPECIALIZATION`  
**ROLE:** `MEMORY / HISTORY QUOTIENT`.

---

## C43 — recovered Go representation ladder

The recovered frozen Go tests give:

### No ko

\[
\rho_0(H_t)=(B_t,\sigma_t),
\qquad
\ker\rho_0\subseteq\equiv_{\mathcal T_{\rm no\,ko}}.
\]

### Simple ko

\[
\ker\rho_0\not\subseteq\equiv_{\mathcal T_{\rm ko}},
\]

while

\[
\rho_K(H_t)=(B_t,\sigma_t,B_{t-1}),
\qquad
\ker\rho_K\subseteq\equiv_{\mathcal T_{\rm ko}}.
\]

### Positional superko

\[
\ker\rho_K\not\subseteq\equiv_{\mathcal T_{\rm PSK}},
\]

while

\[
\rho_{\rm PSK}(H_t)=(B_t,\sigma_t,V_t),
\qquad
V_t=\{B_0,\ldots,B_t\},
\]

is sufficient under the frozen positional-superko contract.

### Situational superko

\[
\ker\rho_{\rm PSK}\not\subseteq\equiv_{\mathcal T_{\rm SSK}},
\]

while

\[
\rho_{\rm SSK}(H_t)=(B_t,\sigma_t,U_t),
\qquad
U_t=\{(B_i,\sigma_i):i\le t\},
\]

is sufficient under the frozen situational-superko contract.

**STATUS:** `EXACT FINITE REGRESSION / LAB BENCHMARK`.

---

## C44 — canonical history quotient

Let

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t},
\qquad
q_{\mathcal T,t}:\mathcal H_t\to M_{\mathcal T,t}.
\]

For every exact task-sufficient representation `rho_t`, there exists a unique

\[
f_t:\operatorname{im}\rho_t\to M_{\mathcal T,t}
\]

such that

\[
\boxed{q_{\mathcal T,t}=f_t\circ\rho_t.}
\]

Therefore `M_T,t` is the **coarsest exact quotient of histories** relative to the task.

This minimality is with respect to quotient order, not dimension, bit count, storage or computational complexity.

**STATUS:** `CLASSICAL FACTORIZATION + PSI TASK-HISTORY BRIDGE`.

---

## C45 — mathematical recursive update

When the history equivalence is a congruence for the declared update, the quotient admits a well-defined partial update

\[
\boxed{
U_{\mathcal T,t}
([H_t],\varepsilon_t,y_{t+1})
=
[\delta_t(H_t,\varepsilon_t,y_{t+1})]_{\mathcal T,t+1}.
}
\]

Hence the exact task state is recursively updateable mathematically without reconstructing the full representative history.

This does **not** prove finite memory, effective computability or algorithmic efficiency.

**STATUS:** `BRIDGE / DYNAMIC QUOTIENT RESULT`.

---

## C46 — Go memory changes are task-relative representation changes

The progression

\[
(B_t,\sigma_t)
\to
(B_t,\sigma_t,B_{t-1})
\to
(B_t,\sigma_t,V_t)
\to
(B_t,\sigma_t,U_t)
\]

does not represent primitive growth.

It represents successive candidate memories `rho_t` required by different rule/task contracts.

\[
\boxed{
\text{change of required memory}\neq\text{new PSI primitive}.
}
\]

**STATUS:** `PRESSURE/REGRESSION RESULT`  
**ROLE:** `MEMORY REPRESENTATION BENCHMARK`.

---

## C47 — G1 provenance gap

The presently recovered RED-1 source freezes `G0`, `G2`, `G3`, `G4` but does not supply a separate `G1` statement.

Therefore no mathematical content is assigned to `G1` in the current public regression without recovery of its actual source.

**STATUS:** `SOURCE GAP / GOVERNANCE`.

---

## Current phase

\[
\boxed{
\mathrm{HCube\ DONE}
\to
\mathrm{Go\ DONE}
\to
\mathrm{FS\!-\!STAT}
\to
\mathrm{regression\ bank}
\to
\mathrm{Principia\ migration/freeze}.
}
\]
