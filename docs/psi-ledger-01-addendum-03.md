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

`phisica-falsifier-registry-01.md` currently freezes PF01–PF14. New high-value locks include:

- PF05: bounded similarity != unitary equivalence;
- PF08: Hellmann–Feynman requires a perturbation contract;
- PF09: small coefficient deformation != automatic spectral stability;
- PF11: integrating-factor weight != geometric pushforward without an integration/coarea contract;
- PF12: vanishing Green boundary form != self-adjointness without maximal boundary/adjoint-domain control;
- PF13: self-adjointness != compact resolvent/discrete spectrum;
- PF14: stable eigenvalues != stable eigenvectors / stable spectral-DNA labels.

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

is algebraically correct but is not automatically a unitary equivalence.

The canonical repair is the unitary Liouville transform

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
UHU^{-1}
=-\frac12\partial_x^2
+V(\lambda(x))+\frac{s_{xx}}{2s}.
}
\]

Result: `III.5 PASS`.

## E040 — perturbation theory and Hellmann–Feynman repaired by a fixed-space contract

Historical PHISICA writes a coefficient-level deformation and then applies

\[
\delta E_n=\langle\phi_n,W\phi_n\rangle
\]

without first fixing the Hilbert space, operator domain, branch regularity or degeneracy structure.

III.6 introduces the canonical sector

\[
H(t)=H_0+W(t),
\qquad
D(H(t))=D(H_0),
\]

with bounded self-adjoint norm-`C^1` perturbation on a fixed Hilbert space after legal unitary trivialization.

Self-adjointness and compact resolvent persist. Ordered eigenvalues satisfy

\[
\boxed{
|E_n(t)-E_n(s)|\le\|W(t)-W(s)\|.
}
\]

For a simple isolated eigenvalue branch, the eigenvector is taken `C^1` in the graph norm of the common domain and

\[
\boxed{
E'(t)=\langle\phi(t),W'(t)\phi(t)\rangle.
}
\]

At a degenerate eigenvalue, first-order splitting is governed by the compressed perturbation on the eigenspace. Raw structural deformations of `Lambda` require a prior unitary/fixed-form trivialization because `B`, `rho`, the Liouville coordinate, interval and boundary domain may all vary.

Result: `III.6 LOCAL PASS`.

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

**Result:** III.1–III.6 have local PASS; whole-block cross-check is mandatory before global PASS.

## D016 — keep historical PSI-13 / DNA / broad LOGOS claims in genealogy

Until they pass the repaired gates, do not promote historical PSI-13 central theorem, LOGOS as complete dynamics, eigenvalue sequence as complete model signature, or domain-free perturbative stability.

## D017 — separate weight construction from geometric and spectral measures

Keep three levels separate: integrating-factor/Hilbert weight, geometric pushforward after coarea hypotheses, and spectral measure only after a specified self-adjoint realization and spectral theorem.

## D018 — self-adjointness requires a boundary realization

Use `H_min`, `H_max`, Green boundary form and maximal isotropic boundary subspaces.

## D019 — recover discrete spectrum only through compactness

Derive compact resolvent from compact form-domain embedding after III.3; do not infer discreteness from self-adjointness alone.

## D020 — replace formal gauge rhetoric by two explicit operator transports

Distinguish bounded similarity with exact domain transport from the unitary Liouville transformation with coordinate change, amplitude and transported domain.

## D021 — perturb only after fixing the operator comparison space

**Observation:** a deformation of `Lambda` changes coefficient data and may also change Hilbert measure, Liouville coordinate, interval length and boundary realization.

**Action:** require a fixed Hilbert/domain perturbation family or a controlled closed-form/unitary trivialization before applying perturbation theory. Use scalar Hellmann–Feynman only on a differentiable simple isolated branch; use compressed matrix perturbation at degeneracy.

**Result:** III.6 passes locally. The old blanket statement “small LOGOS deformation => stable spectral DNA” is not retained. PF14 added.

---

# C. Current handoff

\[
\boxed{
\mathrm{III.1:III.6\ LOCAL\ PASS}
\to
\mathrm{PHISICA\ WHOLE\!\!-\!BLOCK\ CROSSCHECK\ 01\ NEXT}.
}
\]

A sequence of local PASS results is not a global PHISICA PASS.

No CORE5 change and no Agent v03.
