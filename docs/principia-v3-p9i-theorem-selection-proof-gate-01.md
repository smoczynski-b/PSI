# PRINCIPIA SEMANTICA — P9-I THEOREM-SELECTION / PROOF GATE 01

**Status:** `SELECTION PASS / PROOF PASS RELATIVE TO CLASSICAL GPH LEMMA / CROSS-CHECK PASS / III.13 PROMOTION NOT YET PERFORMED`  
**Date:** 2026-10-01  
**Parent:** `p9i-infinite-dimensional-resolvent-growth-source-gate-01.md`, `principia-v3-theorem-map-09.md`  
**General P9 status:** `OPEN / CENTRAL`  
**Does not modify:** CORE5, CANON-03, III.11, III.12.

---

# 1. Selection

The gate selects exactly one statement from the source-gated P9-I ladder:

\[
\boxed{
X=\mathcal H\text{ complex Hilbert},
\qquad
\omega_0(T)=s_0(A).
}
\]

No Kreiss, polynomial-decay, m-accretive, Banach-space or peak-amplification statement is bundled into this unit.

The result is classical Gearhart–Prüss–Huang theory, adapted to the P9 observable separation. No `PSI-NEW` theorem claim is made.

---

# 2. Typed contract

Let \(\mathcal H\) be a complex Hilbert space and

\[
A:D(A)\subset\mathcal H\to\mathcal H
\]

be the densely defined closed generator of a strongly continuous semigroup

\[
T(t),\qquad t\ge0.
\]

Define the growth-admissible set

\[
\mathcal G(T)
:=
\left\{\gamma\in\mathbb R:
\exists M\ge1\ \forall t\ge0,
\ \|T(t)\|\le Me^{\gamma t}
\right\}
\]

and the growth bound

\[
\boxed{
\omega_0(T):=\inf\mathcal G(T).
}
\]

Define

\[
s(A):=\sup\{\Re z:z\in\sigma(A)\}
\]

with the usual extended-real convention if the spectrum is empty, and define the uniform-resolvent admissible set

\[
\mathcal S(A)
:=
\left\{a>s(A):
\sup_{\Re z\ge a}\|R(z,A)\|<\infty
\right\},
\]

where

\[
R(z,A):=(zI-A)^{-1}.
\]

Then

\[
\boxed{
s_0(A):=\inf\mathcal S(A).
}
\]

Both \(\mathcal G(T)\) and \(\mathcal S(A)\) are upward closed. Every \(C_0\)-semigroup is exponentially bounded, so \(\mathcal G(T)\neq\varnothing\). The Laplace resolvent estimate below then also gives \(\mathcal S(A)\neq\varnothing\).

The operator domain is retained throughout. In particular, the shift

\[
B:=A-aI
\]

has

\[
D(B)=D(A).
\]

---

# 3. Imported classical lemma — right-half-plane Gearhart–Prüss–Huang

For a \(C_0\)-semigroup \(U(t)\) on a complex Hilbert space with generator \(B\), the following right-half-plane condition implies exponential stability:

\[
\boxed{
\{\Re\mu\ge0\}\subset\rho(B),
\qquad
\sup_{\Re\mu\ge0}\|R(\mu,B)\|<\infty
}
\]

\[
\Longrightarrow
\]

\[
\boxed{
\exists C\ge1,\ \eta>0:\quad
\|U(t)\|\le Ce^{-\eta t}
\quad(t\ge0).
}
\]

The converse follows from the Laplace representation of the resolvent.

**Source status:** `CLASSICAL / IMPORTED`. See Gearhart (1978), Prüss (1984), Huang (1985) and the source gate. This proof gate does not re-prove the full Gearhart–Prüss–Huang theorem; it uses that sourced theorem as a lemma and proves the selected equality from it.

---

# 4. The selected theorem

## P9-I/H candidate theorem

Under the contract of §2,

\[
\boxed{
\omega_0(T)=s_0(A).
}
\]

The equality is understood in the extended-real sense; for ordinary exponentially bounded non-nilpotent cases both sides are finite real numbers.

---

# 5. Proof — first inequality

We prove

\[
\boxed{s_0(A)\le\omega_0(T)}.
\]

Take arbitrary

\[
\beta>\omega_0(T).
\]

Because \(\mathcal G(T)\) is upward closed and has infimum \(\omega_0(T)\), choose

\[
\gamma\in\mathcal G(T),
\qquad
\omega_0(T)<\gamma<\beta.
\]

Then for some \(M\ge1\),

\[
\|T(t)\|\le Me^{\gamma t}.
\]

For every \(z\) with \(\Re z>\gamma\), the standard Laplace representation gives

\[
R(z,A)x
=
\int_0^\infty e^{-zt}T(t)x\,dt.
\]

Hence for \(\Re z\ge\beta\),

\[
\|R(z,A)\|
\le
\int_0^\infty
Me^{-(\Re z-\gamma)t}\,dt
\le
\frac{M}{\beta-\gamma}.
\]

Thus

\[
\beta\in\mathcal S(A)
\]

and therefore

\[
s_0(A)\le\beta.
\]

Since \(\beta>\omega_0(T)\) was arbitrary,

\[
\boxed{s_0(A)\le\omega_0(T)}.
\]

No Hilbert-space geometry is used in this direction; it is the general Laplace/Hille–Yosida side.

---

# 6. Proof — reverse inequality

We prove

\[
\boxed{\omega_0(T)\le s_0(A)}.
\]

Take arbitrary

\[
a>s_0(A).
\]

Since \(\mathcal S(A)\) is upward closed with infimum \(s_0(A)\),

\[
a\in\mathcal S(A).
\]

Thus

\[
\{\Re z\ge a\}\subset\rho(A)
\]

and there is \(C_a<\infty\) such that

\[
\sup_{\Re z\ge a}\|R(z,A)\|\le C_a.
\]

Define the shifted generator

\[
B:=A-aI,
\qquad
D(B)=D(A),
\]

which generates

\[
U(t):=e^{-at}T(t).
\]

For every \(\mu\) with \(\Re\mu\ge0\),

\[
R(\mu,B)
=
(\mu I-A+aI)^{-1}
=
R(\mu+a,A).
\]

Therefore

\[
\{\Re\mu\ge0\}\subset\rho(B)
\]

and

\[
\sup_{\Re\mu\ge0}\|R(\mu,B)\|
\le C_a<\infty.
\]

The imported right-half-plane Gearhart–Prüss–Huang lemma applies. Hence there exist

\[
M_a\ge1,
\qquad
\eta_a>0
\]

such that

\[
\|U(t)\|
\le
M_a e^{-\eta_a t}.
\]

Returning to \(T(t)\),

\[
\|T(t)\|
\le
M_a e^{(a-\eta_a)t}.
\]

Thus

\[
a-\eta_a\in\mathcal G(T),
\]

so

\[
\omega_0(T)
\le
a-\eta_a
<a.
\]

Because \(a>s_0(A)\) was arbitrary,

\[
\boxed{\omega_0(T)\le s_0(A)}.
\]

Combining §§5–6,

\[
\boxed{
\omega_0(T)=s_0(A).
}
\]

\(\square\)

---

# 7. Corollary — exponential stability

The equality immediately gives

\[
\boxed{
T(t)\text{ exponentially stable}
\iff
s_0(A)<0.
}
\]

This corollary is about the uniform-resolvent abscissa, not about the imaginary-axis resolvent alone.

---

# 8. F63 regression — exact separating witness

Take any nonzero Hilbert space and

\[
A=I.
\]

Then

\[
T(t)=e^tI,
\qquad
\omega_0(T)=1.
\]

The spectrum is \(\{1\}\), hence \(s(A)=1\). For every \(a>1\),

\[
\sup_{\Re z\ge a}\|R(z,A)\|
=
\sup_{\Re z\ge a}\frac1{|z-1|}
=
\frac1{a-1}<\infty.
\]

Therefore

\[
\boxed{s_0(A)=1=\omega_0(T)}.
\]

At the same time,

\[
\sup_{\beta\in\mathbb R}\|R(i\beta,A)\|=1.
\]

Hence the selected theorem survives the F63 witness precisely because

\[
\boxed{
\text{imaginary-axis boundedness}
\neq
s_0(A)<0.
}
\]

The theorem does not smuggle the missing spectral/right-half-plane condition back into the conclusion.

**F63:** `PASS`.

---

# 9. F64 regression — Kreiss remains a different observable

The selected theorem contains no implication

\[
\mathcal K(A)<\infty
\Rightarrow
\sup_t\|T(t)\|<\infty.
\]

Indeed, an infinite-dimensional Hilbert semigroup may have subexponential but unbounded growth. For any such example with genuine positive polynomial lower growth and a sublinear/polynomial upper bound,

\[
\omega_0(T)=0,
\]

while

\[
\sup_{t\ge0}\|T(t)\|=\infty.
\]

The selected theorem then says only

\[
s_0(A)=0.
\]

There is no contradiction: exponential growth rate zero is not uniform boundedness.

Therefore

\[
\boxed{
\omega_0=s_0
\not\Rightarrow
\text{Kreiss peak/boundedness theorem}.
}
\]

**F64:** `PASS`.

---

# 10. Cross-check with III.11 / P9-G

III.11 works in the finite-dimensional metric-gradient subclass

\[
A=-G^{-1}H
\]

and proves much more in the adapted \(G\)-metric:

\[
\|e^{tA}\|_G=e^{-\mu_Gt},
\]

plus exact normal-form resolvent geometry and peak control.

For finite-dimensional matrices one has

\[
\omega_0(T)=s(A)=s_0(A),
\]

because polynomial Jordan factors do not alter the exponential growth exponent and the resolvent is uniformly bounded on every closed half-plane strictly to the right of the spectrum.

Thus P9-I is compatible with III.11 but strictly weaker on that subclass:

\[
\boxed{
\text{P9-I identifies the exponential abscissa;}
\quad
\text{III.11 identifies the adapted metric and exact finite-time norm law.}
}
\]

No P9-G result is replaced.

**P9-G cross-check:** `PASS`.

---

# 11. Cross-check with III.12 / P9-H

III.12 assumes a bounded coercive metric

\[
Q=Q^*,
\qquad
mI\le Q\le MI,
\]

with

\[
A^*Q+QA\le-2\lambda Q.
\]

It proves

\[
\|T(t)\|
\le
\sqrt{\kappa(Q)}e^{-\lambda t},
\]

so

\[
\omega_0(T)\le-\lambda.
\]

It also gives, for \(\Re z> -\lambda\),

\[
\|R(z,A)\|
\le
\frac{\sqrt{\kappa(Q)}}{\Re z+\lambda},
\]

hence

\[
s_0(A)\le-\lambda.
\]

The P9-I identity makes these two exponential-level consequences consistent:

\[
\boxed{
\omega_0(T)=s_0(A)\le-\lambda.
}
\]

But the converse direction is **not** imported:

\[
\boxed{
s_0(A)<0
\not\Rightarrow
\text{the P9-I theorem itself constructs a bounded coercive }Q
}
\]

or a sharp \(\lambda\), condition number, pseudospectral edge, or transient prefactor.

III.12 remains the stronger certificate theorem inside its Lyapunov-metric subclass.

**P9-H cross-check:** `PASS`.

---

# 12. DOM-LOGOS / domain cross-check

The proof uses only the legal generator shift

\[
A\mapsto A-aI
\]

with unchanged domain

\[
D(A-aI)=D(A).
\]

No expression \(Ax\) is evaluated for \(x\notin D(A)\), and no bounded-operator matrix algebra is substituted for the unbounded-generator contract.

**III.9 domain cross-check:** `PASS`.

---

# 13. What passed

The following bounded claim has passed the theorem-selection/proof gate:

\[
\boxed{
\mathcal H\text{ complex Hilbert}
+
A\text{ generator of a }C_0\text{-semigroup}
\Longrightarrow
\omega_0(T)=s_0(A).
}
\]

Pass basis:

1. object/domain contract explicit;
2. observables \(\omega_0\) and \(s_0\) separately defined;
3. \(s_0\le\omega_0\) proved directly by Laplace resolvent control;
4. \(\omega_0\le s_0\) proved by shift + imported classical right-half-plane Gearhart–Prüss–Huang theorem;
5. F63 exact witness passed;
6. F64 boundary passed;
7. III.11, III.12 and III.9 composition boundaries passed.

---

# 14. What this result does not test or prove

This gate does **not** prove:

1. \(\omega_0=s_0\) on arbitrary Banach spaces;
2. \(\omega_0=s(A)\) in general infinite dimension;
3. imaginary-axis resolvent boundedness alone implies stability;
4. finite Kreiss constant implies uniform semigroup boundedness;
5. any bound on \(\sup_t\|T(t)\|\) from \(s_0\) alone;
6. polynomial decay of \(T(t)\) from polynomial resolvent growth;
7. construction of a bounded coercive Lyapunov metric \(Q\);
8. a universal scalar summary of continuous-spectrum or nonnormal dynamics;
9. closure of \(P9_{\rm general}\);
10. any new PSI primitive.

In particular,

\[
\boxed{
\omega_0(T)=0
\not\Rightarrow
\sup_{t\ge0}\|T(t)\|<\infty.
}
\]

---

# 15. Gate verdict

\[
\boxed{
\mathrm{P9\!-\!I\ THEOREM\!-
SELECTION/PROOF\ GATE}=PASS.
}
\]

The selected candidate is now mathematically eligible for a separate theorem-promotion decision.

This document deliberately does **not** assign the label `III.13` to it. Promotion must update the Volume III theorem unit and theorem/work maps as one coherent control step.

Current next legal state:

\[
\boxed{
\mathrm{III.13\ PROMOTION/COMPOSITION\ GATE\ NEXT}.
}
\]
