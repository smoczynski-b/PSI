# PRINCIPIA SEMANTICA — VOLUME III / P9-I COMPOSITION CROSSCHECK 01

**Status:** `COMPOSITION CROSSCHECK PASS`  
**Date:** 2026-10-01  
**Scope:** `III.7–III.13`, with permanent locks F63–F64  
**Promoted unit:** `principia-v3-13-p9i-hilbert-resolvent-growth-bridge.md`

---

# 1. Question

Does promoted III.13

\[
\omega_0(T)=s_0(A)
\]

compose with MOST, HCube, DOM-LOGOS, SOP-11E, P9-G and P9-H without turning one Hilbert-space exponential-level theorem into:

- a universal resolvent-to-transient theorem;
- a well-posedness/generation theorem;
- a Banach-space theorem;
- a nonlinear-semigroup theorem;
- a dimension-free Kreiss theorem;
- or a closure of general P9?

---

# 2. Result

\[
\boxed{
\mathrm{III.7:III.13}
=
\mathrm{COMPOSITION\ PASS}.
}
\]

No theorem-level errata are required.

The general statuses remain

\[
\boxed{P9_{\rm general}=OPEN/CENTRAL},
\qquad
\boxed{P2_{\rm general}=PARTIAL}.
\]

---

# 3. MOST / III.7

III.7 treats information order as a factorization order of declared representations, not as a universal ranking of observables. III.13 is consistent with this discipline because it connects exactly two coarse exponential-level quantities on one typed catalogue:

\[
\rho_{growth}(A)=\omega_0(T),
\qquad
\rho_{uabsc}(A)=s_0(A),
\]

for generators of linear \(C_0\)-semigroups on complex Hilbert space.

It does **not** identify the full resolvent profile

\[
z\mapsto\|R(z,A)\|
\]

with the full semigroup-norm profile

\[
t\mapsto\|T(t)\|.
\]

Thus a factorization/equality at the scalar abscissa level does not collapse the richer MOST representations.

Permanent distinction:

\[
\boxed{
\text{equal exponential abscissae}
\neq
\text{equivalent full dynamical/resolvent representations}.
}
\]

**MOST cross-check:** `PASS`.

---

# 4. HCube / III.8 — exact composition witness

The frozen HCube pair is

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=
\begin{pmatrix}
2&0&0\\
0&1&1\\
0&0&0
\end{pmatrix}.
\]

III.8 proves

\[
\|e^{tA}\|_2=\|e^{tB}\|_2=e^{2t}
\qquad(t\ge0),
\]

but their resolvent-norm profiles differ; for example at \(z=1/2\),

\[
\|R(1/2,A)\|_2=2,
\]

while

\[
\|R(1/2,B)\|_2=2(1+\sqrt2).
\]

Therefore

\[
\omega_0(A)=\omega_0(B)=2.
\]

In finite dimension the uniform-resolvent abscissa equals the spectral bound, so

\[
s_0(A)=s_0(B)=2.
\]

Hence III.13 gives the same coarse equality for both operators while HCube still distinguishes their richer resolvent geometry:

\[
\boxed{
\omega_0(A)=s_0(A)=\omega_0(B)=s_0(B)=2
}
\]

and simultaneously

\[
\boxed{
\rho_r(A)\neq\rho_r(B).
}
\]

This is an exact witness that III.13 does not erase the HCube information separation.

**HCube cross-check:** `PASS`.

---

# 5. DOM-LOGOS / III.9

III.9 asks whether an already defined evolution descends through a representation. III.13 asks, for an already defined linear Hilbert \(C_0\)-semigroup, whether its exponential growth abscissa equals its uniform-resolvent abscissa.

These gates are independent:

\[
\boxed{
\text{projectability}
\neq
\text{exponential stability/growth control}.
}
\]

The proof of III.13 uses the legal shift

\[
B=A-aI,
\qquad
D(B)=D(A),
\]

so the unbounded-generator domain is preserved.

If III.13 is applied after a DOM-LOGOS reduction, the reduced evolution must first be shown to be a linear \(C_0\)-semigroup with a legitimate generator. Projectability alone does not supply the III.13 hypotheses.

**DOM-LOGOS cross-check:** `PASS`.

---

# 6. SOP-11E / III.10

III.10 proves well-posedness only in typed sectors and explicitly distinguishes autonomous semigroups from nonautonomous evolution families.

III.13 begins **after** generation/well-posedness:

\[
A:D(A)\subset\mathcal H\to\mathcal H
\]

is already assumed to generate a strongly continuous **linear** semigroup.

Therefore the legal order is

\[
\boxed{
\text{well-posedness / generation}
\to
\text{linear }C_0\text{-semigroup + generator domain}
\to
\mathrm{III.13}.
}
\]

III.13 does not prove that a formal differential operator generates a semigroup.

It also cannot be silently applied to the nonlinear contraction semigroup of III.10 Sector C merely because both objects are called semigroups. A separate linearization or linear-semigroup contract is required.

Likewise a genuinely nonautonomous evolution family \(U(t,s)\) is outside III.13 as stated.

Permanent distinctions:

\[
\boxed{
\text{well-posedness}
\neq
\text{resolvent/growth equality},
}
\]

\[
\boxed{
\text{nonlinear semigroup}
\neq
\text{linear }C_0\text{-semigroup generator calculus}.
}
\]

**SOP-11E cross-check:** `PASS`.

---

# 7. P9-G / III.11

III.11 restricts to the metric-gradient class

\[
A=-G^{-1}H,
\qquad
G=G^*>0,
\quad
H=H^*>0,
\]

and obtains a common self-adjoint normal form in the adapted metric. It therefore controls much more than the exponential abscissa: exact finite-time norm decay, exact resolvent geometry and metric distortion bounds.

III.13 is broader in catalogue but coarser in conclusion.

Thus

\[
\boxed{
\text{III.13 broader class / weaker observable conclusion}
}
\]

coexists with

\[
\boxed{
\text{III.11 narrower class / stronger finite-time geometry}.
}
\]

No P9-G result is superseded.

**P9-G cross-check:** `PASS`.

---

# 8. P9-H / III.12

III.12 assumes a bounded coercive Lyapunov metric \(Q\) with

\[
A^*Q+QA\le-2\lambda Q.
\]

It proves

\[
\|T(t)\|\le\sqrt{\kappa(Q)}e^{-\lambda t}
\]

and a matching half-plane resolvent estimate. Therefore

\[
\omega_0(T)\le-\lambda,
\qquad
s_0(A)\le-\lambda.
\]

III.13 identifies these two exponential-level abscissae:

\[
\boxed{
\omega_0(T)=s_0(A)\le-\lambda.
}
\]

But III.13 supplies no converse certificate:

\[
\boxed{
s_0(A)<0
\not\Rightarrow
\text{III.13 constructs }Q.
}
\]

Nor does it recover \(\kappa(Q)\), the transient prefactor or the pseudospectral-edge estimate of III.12.

**P9-H cross-check:** `PASS`.

---

# 9. F63 regression

The exact witness

\[
A=I,
\qquad
T(t)=e^tI
\]

has

\[
\sup_{\beta\in\mathbb R}\|(i\beta I-I)^{-1}\|=1
\]

but

\[
\omega_0(T)=s_0(A)=1.
\]

Therefore III.13 does not convert imaginary-axis boundedness into stability without the missing side contract.

**F63:** `PASS`.

---

# 10. F64 regression

III.13 says nothing of the form

\[
\mathcal K(A)<\infty
\Rightarrow
\sup_t\|T(t)\|<\infty.
\]

A semigroup may be subexponentially but unboundedly growing and satisfy

\[
\omega_0(T)=s_0(A)=0.
\]

Thus exponential abscissa zero is not a peak/boundedness theorem.

**F64:** `PASS`.

---

# 11. Norm / representation boundary

Equivalent Hilbert norms differ by fixed multiplicative constants. Such constants do not change the exponential growth bound \(\omega_0(T)\). They also preserve the property that a resolvent family is uniformly bounded on a fixed half-plane, and therefore do not change \(s_0(A)\).

By contrast, finite-time norms, resolvent constants, pseudospectral level sets and Kreiss-type quantities are norm-sensitive.

Hence III.13 is compatible with the existing P9 rule:

\[
\boxed{
\text{exponential abscissa invariance under equivalent norms}
\not\Rightarrow
\text{finite-time geometry invariance}.
}
\]

---

# 12. What the composition PASS does not mean

The composition result does not establish:

1. general Banach equality \(\omega_0=s_0\);
2. equality \(\omega_0=s(A)\) in general infinite dimension;
3. full-resolvent-profile reconstruction from semigroup growth data;
4. transient peak reconstruction from \(s_0\);
5. a dimension-free Kreiss theorem;
6. generation or well-posedness of arbitrary operators;
7. applicability to nonlinear semigroups or nonautonomous evolution families without a new contract;
8. existence of a coercive Lyapunov metric;
9. closure of unrestricted P9;
10. a new PSI primitive.

---

# 13. CORE / Agent impact

No missing semantic role appears. The whole result is expressed through existing catalogue, representation, task-observable, domain and dynamics roles.

\[
\boxed{\mathrm{CORE5\ CHANGE}=NONE},
\qquad
\boxed{\mathrm{AGENT\ v03\ WITNESS}=NONE}.
\]

---

# 14. Verdict

\[
\boxed{
\mathrm{III.7:III.13}
=
\mathrm{COMPOSITION\ PASS}.
}
\]

III.13 is therefore eligible to move from `COMPOSITION GATE PENDING` to a closed numbered Volume III theorem unit.

The unrestricted P9 front remains open, but this cross-check does not define an automatic III.14 candidate.
