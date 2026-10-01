# PSI — falsifier registry 13

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-12.md` as current public versioned registry.

Retain F01–F62 from v12 without semantic change.

---

## F63 — imaginary-axis resolvent / exponential-stability conflation

**TARGET:** any inference of the form

\[
i\mathbb R\subset\rho(A),
\qquad
\sup_{\beta\in\mathbb R}\|R(i\beta,A)\|<\infty
\Longrightarrow
\text{exponential stability of }T(t)
\]

for an arbitrary \(C_0\)-semigroup on a Hilbert space, without the bounded-semigroup / contraction hypothesis or an equivalent right-half-plane contract.

**FALSIFIER:** take any nonzero Hilbert space and

\[
A=I.
\]

Then

\[
T(t)=e^tI
\]

is exponentially unstable, while

\[
i\mathbb R\subset\rho(A)
\]

and

\[
\|R(i\beta,A)\|
=
\frac1{|i\beta-1|}
=
\frac1{\sqrt{1+\beta^2}},
\]

so

\[
\sup_{\beta\in\mathbb R}\|R(i\beta,A)\|=1.
\]

**ORACLE:** use the correctly typed Gearhart–Prüss–Huang contract. For a general Hilbert-space \(C_0\)-semigroup, exponential stability is tested by uniform resolvent control on the closed right half-plane (equivalently \(s_0(A)<0\)); the imaginary-axis-only formulation requires the additional bounded-semigroup / contraction-side hypothesis.

**FIXED APPLICATION:** `p9i-infinite-dimensional-resolvent-growth-source-gate-01.md`, §§4–5.

**REGRESSION:** YES.

---

## F64 — finite-dimensional Kreiss / infinite-dimensional boundedness export

**TARGET:** any dimension-free inference of the form

\[
\mathcal K(A)
:=
\sup_{\Re z>0}(\Re z)\|R(z,A)\|<\infty
\Longrightarrow
\sup_{t\ge0}\|T(t)\|<\infty
\]

for arbitrary infinite-dimensional \(C_0\)-semigroups.

**FALSIFIER:** infinite-dimensional Hilbert-space Kreiss-bounded semigroups need not be uniformly bounded. Arnold (2022) proved the general estimate

\[
\|T(t)\|=O\!\left(\frac{t}{\sqrt{\log t}}\right).
\]

A 2026 Arnold preprint strengthens the upper side to a genuine polynomial gap below linear growth,

\[
\boxed{
\|T(t)\|\le C(1+t)^{1-\varepsilon_K}
}
\]

with \(\varepsilon_K>0\) depending on the Kreiss constant. The same work notes examples of Eisner and Zwart with growth arbitrarily close to linear, so no universal positive gap exponent exists for the whole class. In particular, the stronger 2026 result still does **not** imply uniform boundedness.

**ORACLE:** keep the catalogue explicit.

- finite-dimensional Hurwitz matrices: continuous-time Kreiss matrix theorem gives a dimension-dependent comparison, with upper factor \(en\);
- infinite-dimensional Hilbert generators: current resolvent theory gives sublinear-growth restrictions depending on the Kreiss constant, not a dimension-free uniform boundedness theorem.

**SOURCE STATUS:** Arnold 2022 is peer-reviewed; the 2026 polynomial-gap strengthening is a current preprint and is not used as the sole basis of F64.

**FIXED APPLICATION:** `p9i-infinite-dimensional-resolvent-growth-source-gate-01.md`, §§6–7.

**REGRESSION:** YES.

---

## PASS inflation rule

Every run report must contain both:

`WHAT FAILED / PASSED`

and

`WHAT THIS RESULT DOES NOT TEST`.
