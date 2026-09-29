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

`phisica-falsifier-registry-01.md` now freezes PF01–PF13. New high-value locks include:

- PF11: integrating-factor weight != geometric pushforward without an additional coarea/integration contract;
- PF12: vanishing Green boundary form != self-adjointness without maximal boundary/adjoint-domain control;
- PF13: self-adjointness != compact resolvent/discrete spectrum.

These are migration guards, not new PSI primitives.

## E036 — weighted realization and geometric pushforward

III.2 separates the positive integrating-factor/Hilbert weight from the geometric pushforward. For projectable coefficients with `B>0`,

\[
\boxed{(\rho B)'=\rho C}
\]

and under the additional proper-submersion/coarea contract,

\[
\boxed{
\rho d\lambda=\Lambda_*(d\mathrm{vol}_g)
}
\]

after normalization.

Result: `III.2 PASS`.

## E037 — domain and self-adjoint realization

III.3 replaces the historical domain-free self-adjointness statement by a regular finite-interval operator theorem. The minimal/maximal pair satisfies

\[
\boxed{H_{\min}^*=H_{\max},}
\]

and separated Robin boundary conditions give

\[
\boxed{H_{\alpha,\beta}=H_{\alpha,\beta}^*.}
\]

Result: `III.3 PASS`.

## E038 — compact resolvent and recovered discrete spectrum

III.4 recovers the legitimate finite-interval spectral conclusion only after III.3 fixes the self-adjoint realization.

For regular positive coefficients on a bounded interval, the form domain is a closed subspace of `H^1(I)` with equivalent form norm. Rellich compactness gives

\[
\boxed{
\mathcal Q_{\alpha,\beta}\hookrightarrow L^2(I,\rho d\lambda)
\text{ compactly}.
}
\]

Hence every separated self-adjoint realization from III.3 has compact resolvent:

\[
\boxed{(H_{\alpha,\beta}-z)^{-1}\text{ compact}.}
\]

Therefore

\[
\boxed{
\sigma(H_{\alpha,\beta})=\{E_n\},
\qquad E_n\to+\infty,
}
\]

with finite multiplicities and a complete orthonormal eigenbasis.

Permanent boundary:

\[
\boxed{
\text{self-adjointness}\not\Rightarrow\text{compact resolvent/discrete spectrum}.
}
\]

PF07 remains active: the eigenvalue sequence is not a complete model invariant.

Result: `III.4 PASS`.

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

**Result:** III.1–III.4 pass; III.5 released.

## D016 — keep historical PSI-13 / DNA / broad LOGOS claims in genealogy

Until they pass the new gates, do not promote:

- historical PSI-13 central theorem;
- `LOGOS=(B,C,rho)` as complete dynamics;
- eigenvalue sequence as complete model signature;
- domain-free self-adjointness or perturbative stability.

## D017 — separate weight construction from geometric and spectral measures

Keep three levels separate:

1. integrating-factor/Hilbert weight;
2. geometric pushforward after coarea/integration hypotheses;
3. spectral measure only after a specified self-adjoint realization and spectral theorem.

## D018 — self-adjointness requires a boundary realization

Use `H_min`, `H_max`, Green boundary form and maximal isotropic boundary subspaces. Separated Robin conditions are the current canonical regular family.

## D019 — recover discrete spectrum only through compactness

**Observation:** the historical source states discreteness on a bounded interval after only a short Sturm–Liouville appeal.

**Action:** derive compact resolvent from compact form-domain embedding after III.3.

**Result:** discrete spectrum and complete eigenbasis are restored for the regular finite-interval sector without promoting self-adjointness alone to a discreteness criterion. PF13 added.

---

# C. Current handoff

\[
\boxed{
\mathrm{III.1:III.4\ PASS}
\to
\mathrm{III.5\ LIOUVILLE/NORMAL\ FORM\ NEXT}.
}
\]

No CORE5 change and no Agent v03.
