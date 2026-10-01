# PRINCIPIA SEMANTICA — VOLUME III.14

## P9-POLY — polynomial resolvent growth and regularized orbit decay

**Status:** `THEOREM PROSE PASS 01 / ADAPTED PROOF-SPINE PASS / COMPOSITION PASS`  
**Date:** 2026-10-01  
**Classification:** `CLASSICAL / ADAPTED`  
**Source:** A. Borichev, Y. Tomilov, *Optimal polynomial decay of functions and operator semigroups*, Math. Ann. 347 (2010), 455–478, Theorem 2.4, DOI `10.1007/s00208-009-0439-0`.

---

# 1. Contract

Let \(\mathcal H\) be a complex Hilbert space. Let
\[
A:D(A)\subset\mathcal H\to\mathcal H
\]
generate a bounded linear \(C_0\)-semigroup \(T(t)\), and assume
\[
\sup_{t\ge0}\|T(t)\|<\infty,
\qquad
i\mathbb R\subset\rho(A),
\qquad
\alpha>0.
\]
Then \(0\in\rho(A)\), hence \(A^{-1}\) is bounded.

---

# 2. Theorem III.14.A — Borichev–Tomilov

Under the contract above, the following conditions are equivalent:

\[
\|R(is,A)\|=O(|s|^\alpha),\qquad s\to+\infty,
\]

\[
\|T(t)(-A)^{-\alpha}\|=O(t^{-1}),
\]

\[
\|T(t)(-A)^{-\alpha}x\|=o(t^{-1})
\quad\text{for every }x\in\mathcal H,
\]

\[
\|T(t)A^{-1}\|=O(t^{-1/\alpha}),
\]

and

\[
\|T(t)A^{-1}x\|=o(t^{-1/\alpha})
\quad\text{for every }x\in\mathcal H.
\]

The source states the resolvent asymptotic as \(s\to+\infty\). A two-sided condition \(|s|\to\infty\) is a stronger contract and is not silently substituted for the source statement.

This theorem is classical; PSI does not claim authorship of the equivalence.

---

# 3. Adapted proof spine

Set
\[
B=(-A)^{-\alpha}
\]
and define on \(\mathcal H\oplus\mathcal H\)
\[
\mathcal A=
\begin{pmatrix}
A&B\\
0&A
\end{pmatrix},
\qquad
D(\mathcal A)=D(A)\oplus D(A).
\]
The generated semigroup is
\[
\boxed{
\mathcal T(t)=
\begin{pmatrix}
T(t)&tT(t)B\\
0&T(t)
\end{pmatrix}.
}
\]
For \(R_\lambda=R(\lambda,A)\),
\[
R(\lambda,\mathcal A)=
\begin{pmatrix}
R_\lambda&R_\lambda B R_\lambda\\
0&R_\lambda
\end{pmatrix}.
\]

Borichev–Tomilov's smoothed resolvent estimate, together with the Hilbert-space square-function criterion for the generator and its adjoint, yields boundedness of the lifted semigroup:
\[
\sup_{t\ge0}\|\mathcal T(t)\|<\infty.
\]
Reading the upper-right block gives
\[
\sup_{t\ge0}t\|T(t)(-A)^{-\alpha}\|<\infty,
\]
hence
\[
\|T(t)(-A)^{-\alpha}\|=O(t^{-1}).
\]
The classical strong-stability step for the lifted semigroup then gives, for every \(x\in\mathcal H\),
\[
tT(t)(-A)^{-\alpha}x\to0,
\]
which is the pointwise \(o(t^{-1})\) statement.

The remaining implications are imported from the classical proof: uniform boundedness, the converse resolvent estimate, and moment/fractional-power interpolation.

---

# 4. Permanent boundary

The measured dynamics is regularized:
\[
\boxed{T(t)A^{-1}\neq T(t).}
\]
The theorem does not infer polynomial decay of the raw semigroup norm. Boundedness of \(T(t)\) is an input hypothesis.

The legal information flow is
\[
\boxed{
\text{high-frequency resolvent growth}
\to
\text{regularization}
\to
\text{polynomial decay of regularized orbits}.
}
\]
It is not a reconstruction of the full transient profile.

The sharp rate is Hilbert-specific. General Banach-space results may incur a logarithmic loss, so the Hilbert conclusion is not exported without a new contract.

---

# 5. Relation to III.13 and MOST/HCube

III.13 identifies the exponential quantities
\[
\omega_0(T)=s_0(A).
\]
III.14 concerns different information: high-frequency polynomial resolvent growth and polynomial decay after regularization. Neither theorem subsumes the other.

MOST/HCube therefore remains intact: III.14 creates a class-relative and task-relative bridge, not a universal equivalence between full resolvent and full semigroup representations.

---

# 6. Falsifier locks

Do not:

1. replace \(T(t)A^{-1}\) by \(T(t)\);
2. remove boundedness of the semigroup;
3. remove \(i\mathbb R\subset\rho(A)\);
4. identify operator-norm \(O\) with pointwise \(o\) without the stability step;
5. export the sharp Hilbert rate to arbitrary Banach spaces;
6. treat the matrix lift as a new PSI primitive;
7. classify the theorem as `PSI-NEW`.

The F63 witness \(A=I\), \(T(t)=e^tI\), remains a direct obstruction to dropping the bounded-semigroup hypothesis.

---

# 7. Verdict

\[
\boxed{
\mathrm{III.14\ P9\!-\!POLY}
=
\mathrm{THEOREM\ PROSE\ PASS\ 01 / ADAPTED\ PROOF\!-
SPINE\ PASS / COMPOSITION\ PASS}.
}
\]

with
\[
P9_{\rm general}=OPEN/CENTRAL,
\qquad
CORE5\ CHANGE=NONE.
\]
