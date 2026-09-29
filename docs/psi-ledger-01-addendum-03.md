# PSI — DECISION / EPISTEMIC LEDGER ADDENDUM 03

**Status:** `CURRENT VOLUME III PHISICA ADDENDUM`  
**Date:** 2026-09-29  
**Base ledger:** `psi-ledger-01.md`  
**Previous addendum:** `psi-ledger-01-addendum-02.md`

---

# A. Epistemic updates

## E033 — PHISICA operator source audit

Historical `PHISICA — NEW.pdf` was re-read against current operator-domain discipline.

Result: several historical claims require repair before migration, especially operator projectability, domain/self-adjointness, spectral-measure terminology, drift-removal equivalence and perturbation hypotheses.

No CORE change.

## E034 — exact Lambda projectability criterion

III.1 establishes

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

Result: `III.1 PASS`.

## E035 — PHISICA local falsifier bank

`phisica-falsifier-registry-01.md` currently freezes PF01–PF13. PF05 has been strengthened after III.5:

\[
\boxed{
\text{bounded similarity}\not\Rightarrow\text{unitary equivalence}.
}
\]

These are migration guards, not new PSI primitives.

## E036 — weighted realization and geometric pushforward

III.2 separates the positive integrating-factor/Hilbert weight from the geometric pushforward. Under the proper-submersion/coarea contract,

\[
\boxed{
\rho d\lambda=\Lambda_*(d\mathrm{vol}_g)
}
\]

after normalization.

Result: `III.2 PASS`.

## E037 — domain and self-adjoint realization

III.3 replaces the historical domain-free self-adjointness statement by a regular finite-interval operator theorem:

\[
\boxed{H_{\min}^*=H_{\max}},
\]

and separated Robin boundary conditions give self-adjoint realizations.

Result: `III.3 PASS`.

## E038 — compact resolvent and recovered discrete spectrum

III.4 derives compact resolvent from compact embedding of the regular form domain. Consequently the regular separated realizations have discrete real spectrum with finite multiplicities and a complete orthonormal eigenbasis.

Permanent boundary:

\[
\boxed{
\text{self-adjointness}\not\Rightarrow\text{compact resolvent/discrete spectrum}.
}
\]

Result: `III.4 PASS`.

## E039 — historical drift removal repaired by operator similarity and unitary Liouville transform

The historical substitution

\[
\psi=e^\beta\phi,
\qquad
\beta'=-\frac{C}{2B}
\]

is algebraically correct and, because

\[
\beta=-\frac12\log(\rho B)+\mathrm{const},
\]

its multiplier is bounded and boundedly invertible in the regular compact sector.

However, spectral invariance is licensed only after the domain is transported and the transformed operator is defined by similarity.

The canonical operator repair is the unitary Liouville transform

\[
\boxed{
x(\lambda)=\int_a^\lambda B(\mu)^{-1/2}d\mu,
}
\]

\[
\boxed{
(Uu)(x)=s(\lambda(x))u(\lambda(x)),
\qquad
s=\rho^{1/2}B^{1/4}.
}
\]

Then

\[
\boxed{
U:L^2(I,\rho d\lambda)\to L^2(J,dx)
\text{ is unitary}
}
\]

and

\[
\boxed{
UHU^{-1}
=-\frac12\partial_x^2
+V(\lambda(x))+\frac{s_{xx}}{2s}.
}
\]

The domain and separated boundary conditions are transported explicitly; self-adjointness and all spectral data from III.4 are therefore preserved by unitary equivalence.

Result: `III.5 PASS`.

---

# B. Decision updates

## D015 — do not migrate PHISICA chapter order directly

Rebuild Volume III PHISICA in the order

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

**Result:** III.1–III.5 pass; III.6 released.

## D016 — keep historical PSI-13 / DNA / broad LOGOS claims in genealogy

Until they pass the new gates, do not promote historical PSI-13 central theorem, LOGOS as complete dynamics, eigenvalue sequence as complete model signature, or domain-free perturbative stability.

## D017 — separate weight construction from geometric and spectral measures

Keep three levels separate: integrating-factor/Hilbert weight, geometric pushforward after coarea hypotheses, and spectral measure only after a specified self-adjoint realization and spectral theorem.

## D018 — self-adjointness requires a boundary realization

Use `H_min`, `H_max`, Green boundary form and maximal isotropic boundary subspaces.

## D019 — recover discrete spectrum only through compactness

Derive compact resolvent from compact form-domain embedding after III.3; do not infer discreteness from self-adjointness alone.

## D020 — replace formal gauge rhetoric by two explicit operator transports

**Observation:** the historical multiplier removes drift but does not by itself define a unitary transformation of the self-adjoint problem.

**Action:** distinguish:

1. bounded similarity under `M_beta` with exact domain transport;
2. unitary Liouville transformation with coordinate change, amplitude and transported domain.

**Result:** the historical effective-potential algebra is retained, but the canonical spectral statement is attached to the unitary Liouville operator. III.5 passes and III.6 may work on a fixed standard Hilbert space.

---

# C. Current handoff

\[
\boxed{
\mathrm{III.1:III.5\ PASS}
\to
\mathrm{III.6\ PERTURBATION/HELLMANN\!-\!FEYNMAN\ NEXT}.
}
\]

No CORE5 change and no Agent v03.
