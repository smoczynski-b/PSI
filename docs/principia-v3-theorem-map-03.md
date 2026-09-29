# PRINCIPIA SEMANTICA — VOLUME III THEOREM MAP 03

**Status:** `CURRENT / PHISICA GLOBAL PASS / III.7 MOST PASS / III.8 HCUBE NEXT`  
**Date:** 2026-09-29  
**Supersedes for control:** `principia-v3-theorem-map-02.md`  
**Upstream:** `principia-v3-phisica-whole-crosscheck-01.md`, `regression-bank-01.md`

---

# 1. Closed PHISICA operator block

The repaired PHISICA chain remains globally passed:

\[
\boxed{
\mathrm{III.1\ PROJECTABILITY}
\to
\mathrm{III.2\ WEIGHTED\ REALIZATION}
\to
\mathrm{III.3\ SELF\!\!-\!ADJOINT\ REALIZATION}
\to
\mathrm{III.4\ COMPACT\ SPECTRAL\ THEORY}
\to
\mathrm{III.5\ UNITARY\ LIOUVILLE\ NORMAL\ FORM}
\to
\mathrm{III.6\ PERTURBATION/HF}.
}
\]

Whole-block result:

\[
\boxed{
\mathrm{III.1:III.6}
=
\mathrm{GLOBAL\ PASS\ AFTER\ LOCAL\ ERRATA\ 01}.
}
\]

The arrows denote progressively stronger typed contracts, not one blanket implication chain.

---

# 2. III.7 — MOST / spectral information hierarchy

## Exact finite-dimensional contract

For \(A\in M_n(\mathbb C)\) with fixed operator norm define

\[
\rho_\sigma(A)=\sigma(A),
\]

\[
r_A(z)=
\begin{cases}
\|(zI-A)^{-1}\|,&z\notin\sigma(A),\\
+\infty,&z\in\sigma(A),
\end{cases}
\]

and

\[
\rho_{ps}(A)=\bigl(\sigma_\varepsilon(A)\bigr)_{\varepsilon>0},
\qquad
\sigma_\varepsilon(A)=\{z:r_A(z)>\varepsilon^{-1}\}.
\]

III.7 proves

\[
\boxed{
\ker_{eq}\rho_r
=
\ker_{eq}\rho_{ps}
\subseteq
\ker_{eq}\rho_\sigma.
}
\]

Thus the full pseudospectral family and the complete resolvent-norm profile are equivalent representations under the fixed convention, while the spectrum is their quotient.

## HCube strictness

Regression R01 gives matrices with equal characteristic polynomial and equal operator norm but unequal resolvent norm at \(z=1/2\). Therefore

\[
\boxed{
\text{spectrum + operator norm}
\not\Rightarrow
\text{resolvent-task adequacy}.
}
\]

## Operator-valued resolvent

With

\[
\mathcal R_A(z)=(zI-A)^{-1},
\]

one has

\[
r_A(z)=\|\mathcal R_A(z)\|.
\]

At a common legal resolvent point \(z_0\),

\[
\boxed{
A=z_0I-\mathcal R_A(z_0)^{-1}.
}
\]

Hence the operator-valued resolvent can preserve directional information lost by its norm.

The explicit basis-sensitive witness

\[
A=\operatorname{diag}(0,1),
\qquad
B=\operatorname{diag}(1,0)
\]

has identical resolvent-norm profiles but

\[
\langle e_1,(2I-A)^{-1}e_1\rangle=1/2,
\qquad
\langle e_1,(2I-B)^{-1}e_1\rangle=1.
\]

This witness is legal only when unitary change of basis is not declared gauge.

## Semigroup branch

Define

\[
S_A(t)=e^{tA},
\qquad
g_A(t)=\|e^{tA}\|.
\]

III.7 does **not** assert an unproved factorization between scalar resolvent and scalar semigroup profiles.

The current information graph is

\[
\boxed{
A
\to
\mathcal R_A(\cdot)
\to
r_A(\cdot)
\leftrightarrow
\rho_{ps}(A)
\to
\rho_\sigma(A),
}
\]

with the separate branch

\[
\boxed{
A\to S_A(\cdot)\to g_A(\cdot).
}
\]

Any bridge between those scalar branches requires its own theorem and contract.

## PSI bind

MOST is not one privileged representation. The governing rule is the existing PSI adequacy condition

\[
\boxed{
\ker_{eq}\rho\subseteq E_{\mathcal T}.
}
\]

Equivalently: retain the coarsest operator-information representation that still preserves every distinction required by the declared task.

**STATUS:** `PROOF PASS / LOCAL CROSS-CHECK PASS`  
**SOURCE:** `principia-v3-07-spectral-information-hierarchy-most.md`  
**REGRESSION:** `Regression Bank R01 / HCube`.

---

# 3. Source-status lock for MOST/MOS

`MOST` is retained as the established project label for the operator-information layer. No unsourced expansion of the acronym is canonized.

The physical MOS source supports the typed lesson that nonnormal stability can require resolvent and semigroup information beyond spectrum. It does not license as theorem:

- semantic identification of a resolvent with a “propagator of sense”;
- a universal Hessian-to-Kreiss bridge;
- global closure of the MOS microlocal calculus;
- a total information order between resolvent-norm and semigroup-norm profiles.

---

# 4. Current execution order

\[
\boxed{
\mathrm{PHISICA\ III.1:III.6\ GLOBAL\ PASS}
\to
\mathrm{III.7\ MOST\ PASS}
\to
\mathrm{III.8\ HCUBE\ NEXT}.
}
\]

III.8 is not allowed to merely repeat R01 arithmetic. It must classify the fixed HCube pair against the representation levels of III.7 and state exactly which task contracts each level passes or fails.

No CORE5 change and no Agent v03 witness.