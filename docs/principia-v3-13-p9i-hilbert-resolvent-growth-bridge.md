# PRINCIPIA SEMANTICA — VOLUME III.13

## P9-I — Hilbert resolvent / exponential-growth bridge

**Status:** `THEOREM PROSE PASS / PROOF PASS RELATIVE TO CLASSICAL GPH / COMPOSITION PASS`  
**Date:** 2026-10-01  
**Proof source:** `principia-v3-p9i-theorem-selection-proof-gate-01.md`  
**Composition:** `principia-v3-p9i-composition-crosscheck-01.md`  
**Source gate:** `p9i-infinite-dimensional-resolvent-growth-source-gate-01.md`  
**Classification:** `CLASSICAL / ADAPTED`  
**General P9 status:** `OPEN / CENTRAL`  
**Does not modify:** CORE5, CANON-03, III.9–III.12.

---

# 1. Contract

Let \(\mathcal H\) be a complex Hilbert space and let

\[
A:D(A)\subset\mathcal H\to\mathcal H
\]

be the densely defined closed generator of a strongly continuous **linear** semigroup

\[
T(t),\qquad t\ge0.
\]

Define the semigroup growth bound

\[
\boxed{
\omega_0(T)
:=
\inf\left\{\gamma\in\mathbb R:
\exists M\ge1\ \forall t\ge0,
\ \|T(t)\|\le Me^{\gamma t}
\right\}
}
\]

and, with

\[
s(A):=\sup\{\Re z:z\in\sigma(A)\},
\]

define the uniform-resolvent abscissa

\[
\boxed{
s_0(A)
:=
\inf\left\{a>s(A):
\sup_{\Re z\ge a}\|(zI-A)^{-1}\|<\infty
\right\}.
}
\]

The domain \(D(A)\) is part of the object.

---

# 2. Theorem III.13

Under the contract of §1,

\[
\boxed{
\omega_0(T)=s_0(A).
}
\]

Consequently,

\[
\boxed{
T(t)\text{ is exponentially stable}
\iff
s_0(A)<0.
}
\]

This is the classical Gearhart–Prüss–Huang bridge adapted to the P9 separation of observables. It is not a `PSI-NEW` theorem.

---

# 3. Proof basis

The detailed proof is frozen in `principia-v3-p9i-theorem-selection-proof-gate-01.md`.

The first inequality

\[
\boxed{s_0(A)\le\omega_0(T)}
\]

comes from the Laplace representation: if

\[
\|T(t)\|\le Me^{\gamma t},
\]

then for every \(\beta>\gamma\),

\[
\sup_{\Re z\ge\beta}\|R(z,A)\|
\le
\frac{M}{\beta-\gamma}.
\]

For the reverse inequality take \(a>s_0(A)\) and shift

\[
B:=A-aI,
\qquad
D(B)=D(A).
\]

Then \(B\) generates

\[
U(t):=e^{-at}T(t),
\]

and the uniform resolvent bound for \(A\) on \(\Re z\ge a\) becomes a uniform bound for \(B\) on the closed right half-plane. The classical right-half-plane Gearhart–Prüss–Huang theorem gives exponential stability of \(U\), hence

\[
\omega_0(T)<a.
\]

Since \(a>s_0(A)\) was arbitrary,

\[
\boxed{\omega_0(T)\le s_0(A)}.
\]

Thus \(\omega_0(T)=s_0(A)\).

The full Gearhart–Prüss–Huang theorem is imported as a classical lemma; III.13 does not claim a new proof of that theorem from first principles.

---

# 4. Permanent falsifier locks

## F63

For

\[
A=I,
\qquad
T(t)=e^tI,
\]

one has

\[
\omega_0(T)=s_0(A)=1
\]

while

\[
\sup_{\beta\in\mathbb R}\|(i\beta I-I)^{-1}\|=1.
\]

Therefore

\[
\boxed{
\text{imaginary-axis resolvent boundedness alone}
\not\Rightarrow
\text{exponential stability}.
}
\]

The imaginary-axis-only formulation requires its additional bounded-semigroup / equivalent side contract.

## F64

III.13 contains no implication

\[
\mathcal K(A)<\infty
\Rightarrow
\sup_{t\ge0}\|T(t)\|<\infty.
\]

In particular,

\[
\boxed{
\omega_0(T)=s_0(A)=0
\not\Rightarrow
\sup_{t\ge0}\|T(t)\|<\infty.
}
\]

Thus equality of exponential abscissae is not a dimension-free Kreiss or peak-amplification theorem.

---

# 5. Composition

`principia-v3-p9i-composition-crosscheck-01.md` establishes

\[
\boxed{
\mathrm{III.7:III.13}
=
\mathrm{COMPOSITION\ PASS}.
}
\]

The exact HCube separator is especially important: its two frozen matrices satisfy

\[
\omega_0(A)=s_0(A)=\omega_0(B)=s_0(B)=2,
\]

while their full resolvent-norm profiles differ. Hence III.13 identifies two coarse exponential abscissae without collapsing the richer MOST/HCube representations.

The composition check also preserves:

\[
\text{projectability}\neq\text{stability},
\]

\[
\text{well-posedness/generation}\neq\text{III.13},
\]

and

\[
\text{linear }C_0\text{-semigroup}
\neq
\text{nonlinear semigroup/evolution family}.
\]

III.11 remains stronger on the metric-gradient subclass. III.12 remains stronger as a coercive Lyapunov-metric certificate.

---

# 6. Boundary

III.13 does **not** prove:

1. \(\omega_0=s_0\) on arbitrary Banach spaces;
2. \(\omega_0=s(A)\) for arbitrary infinite-dimensional generators;
3. imaginary-axis boundedness alone implies stability;
4. finite Kreiss constant implies uniform semigroup boundedness;
5. \(s_0\) determines \(\sup_t\|T(t)\|\);
6. polynomial resolvent growth gives polynomial operator-norm decay of \(T(t)\);
7. a coercive Lyapunov metric exists;
8. applicability to nonlinear semigroups or nonautonomous evolution families without a new contract;
9. closure of \(P9_{\rm general}\);
10. any new PSI primitive.

Therefore

\[
\boxed{
\mathrm{III.13\ P9\!-\!I}
=
\mathrm{THEOREM\ PROSE\ PASS / PROOF\ PASS / COMPOSITION\ PASS}
}
\]

with

\[
\boxed{P9_{\rm general}=OPEN/CENTRAL}.
\]

No automatic III.14 candidate is created by this closure.
