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

**FALSIFIER:** infinite-dimensional Hilbert-space Kreiss-bounded semigroups need not be uniformly bounded. The cited infinite-dimensional theory permits positive growth; Arnold (2022) proves a general upper estimate

\[
\|T(t)\|=O\!\left(\frac{t}{\sqrt{\log t}}\right)
\]

for Kreiss-bounded Hilbert-space semigroups and records examples with positive polynomial lower growth.

**ORACLE:** keep the catalogue explicit.

- finite-dimensional Hurwitz matrices: continuous-time Kreiss matrix theorem gives a dimension-dependent comparison, with upper factor \(en\);
- infinite-dimensional generators: no dimension-free passage from finite Kreiss constant to uniform semigroup boundedness is licensed.

**FIXED APPLICATION:** `p9i-infinite-dimensional-resolvent-growth-source-gate-01.md`, §§6–7.

**REGRESSION:** YES.

---

## PASS inflation rule

Every run report must contain both:

`WHAT FAILED / PASSED`

and

`WHAT THIS RESULT DOES NOT TEST`.
