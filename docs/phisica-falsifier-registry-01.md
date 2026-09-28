# PHISICA — OPERATOR FALSIFIER REGISTRY 01

**Status:** `ACTIVE DURING VOLUME III MIGRATION`  
**Date:** 2026-09-29  
**Source audit:** `phisica-operator-migration-01.md`

This registry is local to the PHISICA/LOGOS migration. It does not modify the global PSI falsifier numbering F01–F62.

---

## PF01 — regular scalar field does not imply operator projectability

A condition

\[
d\Lambda\neq0
\]

does not imply

\[
\Delta\operatorname{im}T_\Lambda
\subseteq\operatorname{im}T_\Lambda.
\]

Permanent witness:

\[
\Lambda(x,y)=x+y^2
\]

on Euclidean `R^2`, for which `dLambda != 0` but

\[
|\nabla\Lambda|^2=1+4y^2
\]

is not constant on level sets.

---

## PF02 — coefficient notation is not projectability

Writing

\[
B(\lambda),C(\lambda)
\]

does not prove that

\[
|\nabla\Lambda|^2=B\circ\Lambda,
\qquad
\Delta\Lambda=C\circ\Lambda.
\]

The factorization must be proved.

---

## PF03 — Hilbert weight is not spectral measure

The measure

\[
\rho(\lambda)d\lambda
\]

used in the weighted Hilbert space is not automatically the spectral measure of the self-adjoint operator.

---

## PF04 — formal differential expression is not an unbounded operator

The expression

\[
-\frac1{2\rho}(\rho Bu')'+Vu
\]

does not determine an operator until the Hilbert space and domain/boundary realization are fixed.

---

## PF05 — formal drift removal is not automatic isospectral unitary equivalence

A multiplicative substitution

\[
\psi=e^\beta\phi
\]

that removes a first-derivative coefficient algebraically does not by itself establish a bounded/unitary equivalence of closed operators or preservation of spectrum.

---

## PF06 — LOGOS coefficient data do not determine full self-adjoint dynamics

`(B,C,rho)` determine at most the kinetic differential expression/weight relation. Full dynamics additionally require at least potential and operator realization data.

---

## PF07 — eigenvalue sequence is not automatically a complete model invariant

\[
\{E_n\}
\]

alone does not in general identify a self-adjoint operator, potential, geometry, or physical model.

HCube is a separate PSI-level reminder of the same representation issue.

---

## PF08 — Hellmann–Feynman requires a perturbation contract

The formula

\[
E_n'=\langle\phi_n,H'\phi_n\rangle
\]

is not licensed without a differentiable self-adjoint family in a controlled fixed-space/domain or form framework and an appropriate eigenvalue branch. Degeneracy requires separate treatment.

---

## PF09 — small coefficient deformation does not automatically imply small spectral deformation

A statement

\[
B,C,V\text{ change slightly}
\Rightarrow
\sigma(H)\text{ changes slightly}
\]

requires a topology and a perturbation theorem (e.g. norm-resolvent/form control). It is not a formal consequence of first-order coefficient expansions.

---

## PF10 — historical PSI-13 conditions do not replace operator projectability

Conditions on density/potential such as

\[
D=D(\Lambda),
\qquad
\nu=U(\Lambda)d\Lambda
\]

do not by themselves imply

\[
|\nabla\Lambda|^2=B\circ\Lambda,
\qquad
\Delta\Lambda=C\circ\Lambda.
\]

Any reuse of the historical central theorem must pass III.1 first.
