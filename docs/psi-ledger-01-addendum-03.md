# PSI — DECISION / EPISTEMIC LEDGER ADDENDUM 03

**Status:** `CURRENT VOLUME III PHISICA ADDENDUM`  
**Date:** 2026-09-29  
**Base ledger:** `psi-ledger-01.md`  
**Previous addendum:** `psi-ledger-01-addendum-02.md`

---

# A. Epistemic updates

## E033 — PHISICA operator source audit

Historical `PHISICA — NEW.pdf` was re-read against current operator-domain discipline.

Result: the source contains a valid chain-rule identity for

\[
\Delta(\Phi\circ\Lambda),
\]

but several later claims require repairs before migration:

- one-dimensional projectability of `B,C` was assumed rather than proved;
- self-adjointness lacked a full domain/boundary realization;
- `rho dlambda` was called spectral measure although it is a Hilbert/weight measure at this stage;
- formal multiplicative drift removal was treated as automatically isospectral;
- eigenvalue sequence was over-promoted as complete model information;
- perturbation/Hellmann–Feynman claims lacked fixed-space/domain hypotheses.

Outcome:

\[
\boxed{
\mathrm{PHISICA\ OPERATOR\ MIGRATION\ 01}
=\mathrm{REPAIR\ MAP\ ESTABLISHED}.
}
\]

No CORE change.

## E034 — exact Lambda projectability criterion

The first rebuilt PHISICA theorem establishes

\[
\boxed{
\Delta_g\operatorname{im}T_\Lambda
\subseteq\operatorname{im}T_\Lambda
\iff
|\nabla\Lambda|^2=B\circ\Lambda
\land
\Delta_g\Lambda=C\circ\Lambda.
}
\]

For `H=-1/2 Delta + V`, exact reduction additionally requires

\[
V=V_\Lambda\circ\Lambda.
\]

Permanent witness:

\[
\Lambda(x,y)=x+y^2
\]

is a regular submersion but is not operator-projectable.

Result: `III.1 PASS`.

## E035 — PHISICA local falsifier bank

`phisica-falsifier-registry-01.md` now freezes PF01–PF12, including:

- regular coordinate != projectable operator;
- formal expression != self-adjoint realization;
- weight measure != spectral measure;
- eigenvalues alone != complete representation;
- Hellmann–Feynman requires perturbation hypotheses;
- integrating-factor weight != geometric pushforward without an additional coarea/integration contract;
- vanishing Green boundary form != self-adjointness without maximal boundary/adjoint-domain control.

These are migration guards, not new PSI primitives.

## E036 — weighted realization and geometric pushforward

III.2 separates two statements previously conflated in PHISICA.

First, for projectable coefficients with `B>0`,

\[
\boxed{(\rho B)'=\rho C}
\]

defines a positive Sturm–Liouville/Hilbert weight uniquely up to positive scale and yields

\[
\boxed{
L_\Lambda
=\rho^{-1}\partial_\lambda(\rho B\partial_\lambda).
}
\]

Second, under a proper-submersion/coarea contract, the geometric pushforward

\[
\Lambda_*(d\mathrm{vol}_g)=m(\lambda)d\lambda
\]

has density satisfying

\[
\boxed{(mB)'=mC.}
\]

Hence after normalization,

\[
\boxed{
\rho d\lambda=\Lambda_*(d\mathrm{vol}_g).
}
\]

Result: `III.2 PASS`.

## E037 — domain and self-adjoint realization

III.3 replaces the historical domain-free self-adjointness statement by a regular finite-interval operator theorem.

For

\[
p=\rho B,
\qquad
\tau u=-\frac1{2\rho}(pu')'+Vu,
\]

one defines the maximal domain by

\[
u,pu'\in AC([a,b]),
\qquad
\tau u\in L^2(I,\rho d\lambda).
\]

The Green–Lagrange boundary form is

\[
\boxed{
\mathfrak b(u,v)
=\frac12[u\overline{pv'}-(pu')\overline v]_a^b.
}
\]

The regular minimal/maximal pair satisfies

\[
\boxed{H_{\min}^*=H_{\max}.}
\]

Separated Robin boundary conditions select maximal isotropic boundary trace subspaces and yield

\[
\boxed{H_{\alpha,\beta}=H_{\alpha,\beta}^*.}
\]

Dirichlet, Neumann/quasi-Neumann and mixed separated cases are recovered as special cases.

Permanent boundary:

\[
\boxed{
\text{formal symmetry}\not\Rightarrow\text{self-adjointness}.
}
\]

Result: `III.3 PASS`.

---

# B. Decision updates

## D015 — do not migrate PHISICA chapter order directly

**Action:** rebuild Volume III PHISICA in the order

\[
\boxed{
\mathrm{PROJECTABILITY}
\to
\mathrm{WEIGHT/STURM\!-\!LIOUVILLE}
\to
\mathrm{DOMAIN/SA}
\to
\mathrm{SPECTRUM}
\to
\mathrm{NORMAL\ FORM}
\to
\mathrm{PERTURBATION}.
}
\]

**Result:** III.1–III.3 pass; III.4 released.

## D016 — keep historical PSI-13 / DNA / broad LOGOS claims in genealogy

Until they pass the new gates, do not promote:

- historical PSI-13 central theorem;
- `LOGOS=(B,C,rho)` as complete dynamics;
- eigenvalue sequence as complete model signature;
- domain-free self-adjointness or perturbative stability.

These remain Volume IV/source genealogy or unresolved Volume III material.

## D017 — separate weight construction from geometric and spectral measures

Keep three levels separate:

1. integrating-factor/Hilbert weight from `(rho B)'=rho C`;
2. geometric pushforward only after coarea/integration hypotheses;
3. spectral measure only after a specified self-adjoint realization and the spectral theorem.

## D018 — self-adjointness requires a boundary realization, not only a formal expression

**Observation:** the historical source listed candidate domains and boundary conditions after a general statement of self-adjoint extension existence.

**Action:** rebuild the regular operator through `H_min`, `H_max`, Green boundary form and maximal isotropic boundary subspaces. Use separated Robin conditions as the current canonical regular family.

**Result:** III.3 passes; compact-resolvent/discrete-spectrum claims are now legally released for III.4.

---

# C. Current handoff

\[
\boxed{
\mathrm{III.1\ PASS}
\to
\mathrm{III.2\ PASS}
\to
\mathrm{III.3\ PASS}
\to
\mathrm{III.4\ COMPACT\ RESOLVENT/SPECTRUM\ NEXT}.
}
\]

No CORE5 change and no Agent v03.
