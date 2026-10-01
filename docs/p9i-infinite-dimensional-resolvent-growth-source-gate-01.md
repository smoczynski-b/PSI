# P9-I — INFINITE-DIMENSIONAL RESOLVENT / GROWTH SOURCE GATE 01

**Status:** `SOURCE GATE PASS / HILBERT LADDER IDENTIFIED / GENERAL P9 REMAINS OPEN / III.13 NOT YET A THEOREM`  
**Date:** 2026-10-01  
**Parent control:** `principia-v3-theorem-map-08.md`, `work-map-09.md`  
**Scope:** unbounded generators, continuous spectrum, resolvent-to-semigroup growth and decay in infinite dimension.  
**Does not modify:** CORE5, CANON-03, III.11, III.12.

---

# 1. Source hierarchy

The current project map explicitly leaves

\[
P9_{\rm general}=OPEN/CENTRAL
\]

and names the next legal unit as the P9-I infinite-dimensional resolvent/growth source gate.

Current project parents:

1. `p9-hessian-transient-migration-01.md` — repairs the Hessian / dissipative-part and raw-resolvent / Kreiss confusions;
2. `principia-v3-11-p9-metric-gradient-bridge.md` — closes the finite-dimensional metric-gradient sector P9-G;
3. `principia-v3-12-hypocoercive-modified-energy-bridge.md` — closes conditionally the bounded-coercive Lyapunov-metric sector P9-H;
4. `principia-v3-p9h-composition-crosscheck-01.md` — identifies genuinely infinite-dimensional resolvent/growth as the next unresolved class;
5. `principia-v3-09-semigroup-projectability-dom-logos.md` — freezes domain-before-formal-algebra for unbounded generators.

External classical sources used by this gate:

- L. Gearhart, *Spectral theory for contraction semigroups on Hilbert space*, Trans. Amer. Math. Soc. 236 (1978), 385–394, DOI `10.1090/S0002-9947-1978-0461206-1`;
- J. Prüss, *On the spectrum of C0-semigroups*, Trans. Amer. Math. Soc. 284 (1984), 847–857, DOI `10.1090/S0002-9947-1984-0743749-9`;
- F. L. Huang, *Characteristic conditions for exponential stability of linear dynamical systems in Hilbert spaces*, Ann. Differential Equations 1 (1985), 43–56;
- A. Borichev, Y. Tomilov, *Optimal polynomial decay of functions and operator semigroups*, Math. Ann. 347 (2010), 455–478, DOI `10.1007/s00208-009-0439-0`;
- L. Arnold, *Behavior of Kreiss bounded C0-semigroups on a Hilbert space*, Adv. Oper. Theory 7, 62 (2022), DOI `10.1007/s43036-022-00223-z`;
- D. Wei, *Diffusion and mixing in fluid flow via the resolvent estimate*, Sci. China Math. 64 (2021), 507–518, DOI `10.1007/s11425-018-9461-8`.

All results imported from these sources are `CLASSICAL / ADAPTED`, not `PSI-NEW`.

---

# 2. Bronsztejn contract — object first

Let \(X\) be a complex Banach space and let

\[
A:D(A)\subset X\to X
\]

be a densely defined closed operator generating a strongly continuous semigroup

\[
T(t),\qquad t\ge0.
\]

For the Hilbert theorems below we explicitly strengthen

\[
X=\mathcal H
\]

to a complex Hilbert space.

The primary operator object is therefore **the generator with its domain**, not a formal matrix symbol.

The resolvent is

\[
R(\lambda,A):=(\lambda I-A)^{-1},
\qquad \lambda\in\rho(A).
\]

No formula involving \(Ax\) is legal outside \(D(A)\).

---

# 3. Three different exponential-level quantities

Define the spectral bound

\[
\boxed{
s(A):=\sup\{\Re\lambda:\lambda\in\sigma(A)\}.
}
\]

Define the semigroup growth bound

\[
\boxed{
\omega_0(T)
:=\inf\{\omega\in\mathbb R:\exists M\ge1\ \forall t\ge0,
\ \|T(t)\|\le Me^{\omega t}\}.
}
\]

Define the abscissa of uniform resolvent boundedness

\[
\boxed{
s_0(A)
:=\inf\{\omega>s(A):
\sup_{\Re\lambda\ge\omega}\|R(\lambda,A)\|<\infty\}.
}
\]

For a general Banach-space \(C_0\)-semigroup one has only

\[
\boxed{
s(A)\le s_0(A)\le\omega_0(T),
}
\]

and strict gaps can occur.

Therefore the spectral location alone does not determine the norm-growth bound in the unrestricted infinite-dimensional catalogue.

---

# 4. P9-I/H — Gearhart–Prüss–Huang level

For a \(C_0\)-semigroup on a complex Hilbert space,

\[
\boxed{
\omega_0(T)=s_0(A).
}
\]

Consequently,

\[
\boxed{
T(t)\text{ exponentially stable}
\iff
s_0(A)<0.
}
\]

A safe right-half-plane formulation is:

\[
\boxed{
\{\Re\lambda\ge0\}\subset\rho(A)
\quad\text{and}\quad
\sup_{\Re\lambda\ge0}\|R(\lambda,A)\|<\infty
}
\]

if and only if \(T\) is exponentially stable.

For a semigroup already known to be bounded (in particular a contraction semigroup), this reduces to the familiar imaginary-axis criterion

\[
\boxed{
i\mathbb R\subset\rho(A),
\qquad
\sup_{\beta\in\mathbb R}\|R(i\beta,A)\|<\infty.
}
\]

This distinction is permanent. The imaginary-axis condition is **not** imported without the bounded-semigroup / equivalent spectral-side hypothesis.

---

# 5. Falsifier GP-01 — why the boundedness clause cannot disappear

Take any nonzero Hilbert space and

\[
A=I.
\]

Then

\[
T(t)=e^{t}I,
\]

so \(T\) is exponentially unstable.

Nevertheless

\[
i\mathbb R\subset\rho(A)
\]

and

\[
\|R(i\beta,A)\|
=
\frac{1}{|i\beta-1|}
=
\frac1{\sqrt{1+\beta^2}},
\]

hence

\[
\boxed{
\sup_{\beta\in\mathbb R}\|R(i\beta,A)\|=1.
}
\]

Therefore

\[
\boxed{
\text{uniform imaginary-axis resolvent bound alone}
\not\Rightarrow
\text{exponential stability}.
}
\]

This falsifies the hypothesis-free imaginary-axis formulation present in older AX-003 working material.

---

# 6. Kreiss is a different observable contract

For a generator whose open right half-plane belongs to the resolvent set, define

\[
\boxed{
\mathcal K(A)
:=
\sup_{\Re z>0}
(\Re z)\|R(z,A)\|.
}
\]

This is not the same quantity as

\[
\sup_{\Re z\ge0}\|R(z,A)\|
\]

and not the same as \(s_0(A)\).

In finite dimension, for a Hurwitz-stable \(n\times n\) matrix, the continuous-time Kreiss matrix theorem gives the dimension-dependent estimate

\[
\boxed{
\mathcal K(A)
\le
\sup_{t\ge0}\|e^{tA}\|
\le
en\,\mathcal K(A).
}
\]

The factor depends on \(n\). There is no legal passage \(n\to\infty\) that turns this into a dimension-free infinite-dimensional theorem.

---

# 7. Falsifier K-I-01 — infinite-dimensional Kreiss does not imply bounded semigroup

The infinite-dimensional Kreiss condition is strictly weaker than uniform semigroup boundedness.

Arnold (2022) proves for Kreiss-bounded \(C_0\)-semigroups on Hilbert space the general growth estimate

\[
\boxed{
\|T(t)\|=O\!\left(\frac{t}{\sqrt{\log t}}\right),
}
\]

and records examples of Kreiss-bounded semigroups with positive polynomial lower growth.

Thus

\[
\boxed{
\mathcal K(A)<\infty
\not\Rightarrow
\sup_{t\ge0}\|T(t)\|<\infty
}
\]

in the unrestricted infinite-dimensional setting.

Therefore the finite-dimensional Kreiss equivalence is not a legal P9-I bridge without an additional class contract.

---

# 8. P9-I/R — polynomial resolvent growth gives regularized-orbit decay on Hilbert space

Let \((T(t))_{t\ge0}\) be a **bounded** \(C_0\)-semigroup on a Hilbert space with generator \(A\), assume

\[
i\mathbb R\subset\rho(A),
\]

and let \(\alpha>0\).

Borichev–Tomilov identifies the sharp Hilbert-space rate bridge

\[
\boxed{
\|R(is,A)\|=O(|s|^\alpha)
\quad(|s|\to\infty)
}
\]

if and only if

\[
\boxed{
\|T(t)A^{-1}\|=O(t^{-1/\alpha})
\quad(t\to\infty).
}
\]

The target is deliberately

\[
T(t)A^{-1},
\]

not \(T(t)\) in operator norm.

This is essential: a polynomial stability theorem is a statement about regularized orbits / data with generator regularity, not a polynomial operator-norm decay theorem for the whole semigroup.

General Banach spaces do not inherit this Hilbert-sharp equivalence verbatim; the Banach-space theory has weaker rate transfers and logarithmic losses in the general case.

---

# 9. P9-I/A — quantitative m-accretive subclass

Let \(H:D(H)\subset\mathcal H\to\mathcal H\) be m-accretive on a Hilbert space and define

\[
\Psi(H)
:=
\inf_{\lambda\in\mathbb R}
\inf_{\substack{f\in D(H)\\\|f\|=1}}
\|(H-i\lambda)f\|.
\]

Wei's quantitative Gearhart–Prüss-type estimate gives

\[
\boxed{
\|e^{-tH}\|
\le
\exp\!\left(-t\Psi(H)+\frac\pi2\right).
}
\]

When the imaginary-axis inverse is everywhere defined and uniformly bounded,

\[
\Psi(H)
=
\left(
\sup_{\lambda\in\mathbb R}
\|(H-i\lambda)^{-1}\|
\right)^{-1}.
\]

This is a useful explicit subclass but depends crucially on m-accretivity. It is not a quantitative theorem for arbitrary nonnormal generators.

The older working estimate with an unexplained prefactor \(e\) is therefore not migrated as stated; the sourced Wei estimate uses \(e^{\pi/2}\) under the m-accretive contract.

---

# 10. Historical AX-003 audit

The earlier AX-003 layer is classified as follows.

## 10.1 Laplace / Hille–Yosida direction

If

\[
\|T(t)\|\le Me^{\omega t},
\]

then for \(\Re z>\omega\),

\[
R(z,A)x
=
\int_0^\infty e^{-zt}T(t)x\,dt
\]

and

\[
\boxed{
\|R(z,A)\|\le\frac{M}{\Re z-\omega}.
}
\]

Verdict: `KEEP / CLASSICAL`, with the growth-bound half-plane explicit.

## 10.2 Hypothesis-free imaginary-axis Gearhart statement

Verdict: `SUPERSEDE` by §4–5.

## 10.3 Old \(\ell^\infty\) left-shift counterexample

The working text simultaneously states that the generator/operator spectrum is the closed unit disk and that

\[
i\mathbb R\subset\rho(A).
\]

These statements are incompatible because the closed unit disk intersects \(i\mathbb R\).

Verdict: `GENEALOGY / INVALID AS STATED`.

It is not needed: GP-01 supplies a simpler exact falsifier for the missing boundedness hypothesis.

## 10.4 Finite-dimensional Kreiss constant

Verdict: `KEEP ONLY WITH FINITE-DIMENSIONAL TYPE`.

The safe modern continuous-time bound used here is \(en\mathcal K(A)\). The older `(e/2)n` claim is not migrated by this gate.

## 10.5 Infinite-dimensional “Kreiss analogue”

Verdict: `REFORMULATE`.

There is no direct dimension-free replacement of the finite-dimensional peak-amplification theorem. Infinite-dimensional theory instead branches by observable and class: Gearhart–Prüss for exponential growth bounds on Hilbert spaces, Borichev–Tomilov for regularized polynomial decay, and weaker Kreiss-growth estimates for Kreiss-bounded semigroups.

---

# 11. P9-I information geometry

The source gate rejects the idea that there is one scalar quantity called “the resolvent information” that universally determines “the dynamics”.

At minimum the following tasks are different:

\[
\boxed{
\begin{array}{rcl}
\text{spectral location} &:& s(A),\\
\text{exponential norm growth} &:& \omega_0(T),\\
\text{uniform resolvent abscissa} &:& s_0(A),\\
\text{peak/transient amplification} &:& \sup_t\|T(t)\|,\\
\text{Kreiss amplification index} &:& \mathcal K(A),\\
\text{regularized decay rate} &:& \|T(t)A^{-1}\|.
\end{array}
}
\]

The legal bridges depend on the catalogue:

\[
\boxed{
\text{catalogue}
+
\text{norm/space type}
+
\text{generator domain}
+
\text{resolvent observable}
\longrightarrow
\text{permitted dynamical conclusion}.
}
\]

This is consistent with MOST/HCube: representation order is task-relative and class-relative.

---

# 12. What the source gate does not authorize

This gate does **not** establish:

1. a universal scalar function \(\Phi\) controlling all infinite-dimensional nonnormal transient growth;
2. a Banach-space version of the Hilbert equality \(\omega_0=s_0\);
3. a dimension-free Kreiss matrix theorem;
4. polynomial decay of \(\|T(t)\|\) from polynomial imaginary-axis resolvent growth;
5. a general construction of a coercive Lyapunov metric from resolvent data;
6. a continuous-spectrum theorem beyond the cited semigroup results;
7. any new PSI primitive.

In particular, the source literature does **not** justify the historical slogan

\[
\text{“resolvent bound”}\Rightarrow\text{“transient bound”}
\]

without specifying which resolvent bound, which semigroup quantity, and which operator catalogue.

---

# 13. Source-gate verdict

The source search and counterexample audit identify a stable P9-I ladder:

\[
\boxed{
\begin{array}{ll}
\text{Hilbert / exponential:} & \omega_0(T)=s_0(A),\\[2mm]
\text{bounded Hilbert / imaginary axis:} & \text{Gearhart–Prüss–Huang criterion},\\[2mm]
\text{bounded Hilbert / polynomial rates:} & \text{Borichev–Tomilov on }T(t)A^{-1},\\[2mm]
\text{m-accretive Hilbert:} & \text{Wei quantitative bound},\\[2mm]
\text{finite-dimensional transient:} & \text{Kreiss matrix theorem},\\[2mm]
\text{infinite-dimensional Kreiss:} & \text{no boundedness implication in general}.
\end{array}
}
\]

Therefore

\[
\boxed{
\mathrm{P9\!-
I\ SOURCE/CONTRACT\ GATE}=PASS.
}
\]

with

\[
\boxed{
P9_{\rm general}=OPEN/CENTRAL.
}
\]

The gate does **not** itself create III.13. The next legal step is a theorem-selection/proof gate choosing one explicitly typed P9-I statement, with the most conservative candidate being the Hilbert exponential-growth layer

\[
\omega_0(T)=s_0(A)
\]

plus its exact boundary against Kreiss and Banach-space export.

`CORE5 CHANGE = NONE`.  
`AGENT v03 WITNESS = NONE`.
