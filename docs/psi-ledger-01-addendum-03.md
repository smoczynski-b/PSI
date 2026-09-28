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

This closes the old hidden jump from pointwise `B(x),C(x)` to one-dimensional `B(lambda),C(lambda)`.

Permanent witness:

\[
\Lambda(x,y)=x+y^2
\]

is a regular submersion but is not operator-projectable.

Result: `III.1 PASS`.

## E035 — PHISICA local falsifier bank

`phisica-falsifier-registry-01.md` freezes PF01–PF11, including:

- regular coordinate != projectable operator;
- formal expression != self-adjoint realization;
- weight measure != spectral measure;
- eigenvalues alone != complete representation;
- Hellmann–Feynman requires perturbation hypotheses;
- integrating-factor weight != geometric pushforward without an additional coarea/integration contract.

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

This gives formal symmetry on compactly supported test functions but not self-adjointness.

Second, under a proper-submersion/coarea contract, the geometric pushforward

\[
\Lambda_*(d\mathrm{vol}_g)=m(\lambda)d\lambda
\]

has density

\[
m(\lambda)
=\int_{\Lambda^{-1}(\lambda)}|\nabla\Lambda|^{-1}dA_\lambda
\]

and Green's identity plus III.1 projectability gives

\[
\boxed{(mB)'=mC.}
\]

Hence on connected `I`, `m=K rho`; after normalization,

\[
\boxed{
\rho d\lambda=\Lambda_*(d\mathrm{vol}_g).
}
\]

This fixes the geometric normalization and makes `T_Lambda` an isometry onto the fibre-constant Hilbert subspace.

Permanent boundary:

\[
\boxed{
\text{Hilbert weight}\neq\text{spectral measure}.
}
\]

Result: `III.2 PASS`.

---

# B. Decision updates

## D015 — do not migrate PHISICA chapter order directly

**Observation:** historical PHISICA mixes pointwise differential identities, formal one-dimensional reductions, operator domains, spectral claims and perturbation claims without always separating their hypotheses.

**Alternatives:** copy old chapter sequence / rebuild by operator legality.

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

**Result:** III.1 and III.2 pass; III.3 released.

## D016 — keep historical PSI-13 / DNA / broad LOGOS claims in genealogy

Until they pass the new gates, do not promote:

- historical PSI-13 central theorem;
- `LOGOS=(B,C,rho)` as complete dynamics;
- eigenvalue sequence as complete model signature;
- domain-free self-adjointness or perturbative stability.

These remain Volume IV/source genealogy or unresolved Volume III material.

## D017 — separate weight construction from geometric and spectral measures

**Observation:** the historical source uses the same `rho` language for the integrating factor, Hilbert weight and a claimed spectral measure.

**Action:** keep three levels separate:

1. integrating-factor/Hilbert weight from `(rho B)'=rho C`;
2. geometric pushforward only after coarea/integration hypotheses;
3. spectral measure only after a specified self-adjoint realization and the spectral theorem.

**Result:** III.2 passes without promoting any spectral-measure claim. PF11 added.

---

# C. Current handoff

\[
\boxed{
\mathrm{III.1\ PASS}
\to
\mathrm{III.2\ PASS}
\to
\mathrm{III.3\ DOMAIN/SELF\!\!-\!ADJOINT\ NEXT}.
}
\]

No CORE5 change and no Agent v03.
