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

# 1. Role

III.13 promotes exactly one source-gated and proof-gated statement. It extends the numbered Volume III realization layer from special finite-dimensional / coercive-metric P9 subclasses to the general class of strongly continuous linear semigroups on complex Hilbert spaces, but only at the level of the exponential growth abscissa.

No claim of PSI novelty is made for the theorem itself.

---

# 2. Contract

Let \(\mathcal H\) be a complex Hilbert space and let

\[
A:D(A)\subset\mathcal H\to\mathcal H
\]

be the densely defined closed generator of a strongly continuous semigroup

\[
T(t),\qquad t\ge0.
\]

Define

\[
\omega_0(T)
:=
\inf\left\{\gamma\in\mathbb R:
\exists M\ge1\ \forall t\ge0,
\ \|T(t)\|\le Me^{\gamma t}
\right\}.
\]

Let

\[
s(A):=\sup\{\Re z:z\in\sigma(A)\}
\]

and define

\[
s_0(A)
:=
\inf\left\{a>s(A):
\sup_{\Re z\ge a}\|(zI-A)^{-1}\|<\infty
\right\}.
\]

These are distinct observables: \(\omega_0(T)\) is a semigroup growth bound; \(s_0(A)\) is the abscissa beyond which the resolvent is uniformly bounded.

---

# 3. Theorem III.13 — Hilbert equality of exponential and uniform-resolvent abscissae

Under the contract of §2,

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

The theorem is the classical Gearhart–Prüss–Huang bridge in the P9 observable separation.

---

# 4. Proof basis

The full project proof is in `principia-v3-p9i-theorem-selection-proof-gate-01.md`. Its two directions are intentionally separated.

## 4.1 Laplace direction

If

\[
\|T(t)\|\le Me^{\gamma t},
\]

then for \(\Re z>\gamma\),

\[
R(z,A)x
=
\int_0^\infty e^{-zt}T(t)x\,dt,
\]

and therefore for every \(\beta>\gamma\),

\[
\sup_{\Re z\ge\beta}\|R(z,A)\|
\le
\frac{M}{\beta-\gamma}.
\]

Taking infima yields

\[
\boxed{s_0(A)\le\omega_0(T)}.
\]

This direction does not require Hilbert geometry.

## 4.2 Hilbert / Gearhart–Prüss–Huang direction

Take \(a>s_0(A)\) and set

\[
B:=A-aI,
\qquad
D(B)=D(A),
\]

so that

\[
U(t):=e^{-at}T(t)
\]

has generator \(B\). Uniform resolvent boundedness of \(A\) on \(\Re z\ge a\) becomes uniform resolvent boundedness of \(B\) on the closed right half-plane. The classical right-half-plane Gearhart–Prüss–Huang theorem then gives exponential stability of \(U\), hence

\[
\omega_0(T)<a.
\]

Since \(a>s_0(A)\) is arbitrary,

\[
\boxed{\omega_0(T)\le s_0(A)}.
\]

Thus \(\omega_0(T)=s_0(A)\).

The full Gearhart–Prüss–Huang theorem is imported as a classical lemma; III.13 does not claim to re-prove it from first principles.

---

# 5. F63 lock — imaginary axis is not enough without its side contract

For any nonzero Hilbert space let

\[
A=I,
\qquad
T(t)=e^tI.
\]

Then

\[
\omega_0(T)=s_0(A)=1,
\]

while

\[
\sup_{\beta\in\mathbb R}
\|(i\beta I-I)^{-1}\|=1.
\]

Therefore III.13 preserves

\[
\boxed{
\text{uniform imaginary-axis resolvent boundedness}
\neq
s_0(A)<0.
}
\]

The imaginary-axis-only stability formulation requires its bounded-semigroup / equivalent side contract.

---

# 6. F64 lock — Kreiss and peak amplification remain separate

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

Thus equality of exponential abscissae is not a dimension-free Kreiss theorem and does not control finite-time peak amplification.

---

# 7. Relation to III.11 and III.12

III.11 is stronger on the finite-dimensional metric-gradient subclass because it supplies an adapted metric and exact finite-time semigroup/resolvent laws.

III.12 is stronger on the bounded-coercive Lyapunov-metric subclass because it supplies the certificate

\[
A^*Q+QA\le-2\lambda Q
\]

and hence explicit decay, resolvent and pseudospectral bounds. Within that subclass III.13 only identifies the two exponential-level quantities:

\[
\boxed{
\omega_0(T)=s_0(A)\le-\lambda.
}
\]

III.13 does not construct \(Q\), \(\lambda\), \(\kappa(Q)\), a transient prefactor or a pseudospectral edge.

---

# 8. Permanent boundary

III.13 does **not** prove:

1. \(\omega_0=s_0\) on arbitrary Banach spaces;
2. \(\omega_0=s(A)\) for arbitrary infinite-dimensional generators;
3. imaginary-axis resolvent boundedness alone implies exponential stability;
4. finite Kreiss constant implies uniform semigroup boundedness;
5. \(s_0\) determines \(\sup_t\|T(t)\|\);
6. polynomial resolvent growth gives polynomial operator-norm decay of \(T(t)\);
7. a coercive Lyapunov metric exists;
8. a universal scalar description of nonnormal or continuous-spectrum dynamics;
9. closure of \(P9_{\rm general}\);
10. any new PSI primitive.

---

# 9. Composition witness and verdict

The full cross-check `principia-v3-p9i-composition-crosscheck-01.md` establishes

\[
\boxed{
\mathrm{III.7:III.13}=\mathrm{COMPOSITION\ PASS}.
}
\]

In particular, the frozen HCube pair supplies an exact separator: both members have

\[
\omega_0=s_0=2,
\]

while their full resolvent-norm profiles differ. Therefore the scalar equality of III.13 does not collapse the richer MOST/HCube information hierarchy.

The final status is

\[
\boxed{
\mathrm{III.13\ P9\!-\!I}
=\mathrm{THEOREM\ PROSE\ PASS / PROOF\ PASS / COMPOSITION\ PASS}.
}
\]

with

\[
\boxed{P9_{\rm general}=OPEN/CENTRAL}.
\]

No automatic III.14 theorem candidate is created by this closure.
