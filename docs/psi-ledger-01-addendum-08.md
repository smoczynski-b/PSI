# PSI — DECISION / EPISTEMIC LEDGER ADDENDUM 08

**Status:** `CURRENT SOP-11E SECTOR CLOSURE / P9 HANDOFF`  
**Date:** 2026-09-29  
**Base ledger:** `psi-ledger-01.md`  
**Previous addendum:** `psi-ledger-01-addendum-07.md`

---

# A. Epistemic updates

## E055 — general SOP-11E P2 remains PARTIAL

The source gate reconciles two historical statements:

- local operator-energy/Hessian stability is canonical in the 2026-07-26A typed sector;
- general existence/uniqueness/continuous dependence for
  \(D_t\psi=-\nabla_{G(\psi)}L(\psi)+Z\) remains PARTIAL in KANON2.

No contradiction remains after scope separation.

## E056 — smooth globally controlled SOP-11E sector is well posed

For fixed bounded coercive \(G\), globally Lipschitz \(\nabla L\), and \(Z\in L^1_{loc}\), III.10 proves global existence, uniqueness and quantitative continuous dependence.

Bare \(C^2\) regularity is insufficient; \(L(x)=-x^3/3\) yields finite-time blow-up through \(\dot x=x^2\).

## E057 — convex subdifferential sector is closed by nonlinear semigroup theory

For proper lsc convex \(L\) and constant forcing \(z\), the operator \(-\partial(L-\langle z,\cdot\rangle)\) is m-dissipative and generates a nonlinear contraction semigroup.

This is a classical import, not a PSI-authorship claim.

## E058 — nonautonomous forcing changes the evolution object

Genuinely time-dependent forcing produces an evolution family \(U(t,s)\), not automatically an autonomous semigroup. Therefore III.9 semigroup projectability cannot be copied word-for-word to that sector.

## E059 — III.9–III.10 composition PASS

The composition audit verifies that well-posedness, semigroup type, projectability and local Hessian stability remain separate gates.

---

# B. Decision updates

## D030 — do not close general P2 from closed subclasses

Permanent rule:

\[
\boxed{\text{closed typed subclasses}\not\Rightarrow\text{general SOP-11E problem closed}.}
\]

General P2 remains PARTIAL.

## D031 — do not infer compact attractors from coercivity alone

The older working synthesis overstated `coercivity => compact global attractor`. Infinite-dimensional compactness requires additional compactness/asymptotic-compactness structure.

## D032 — keep nonlinear and linear generator calculi separated

III.9.A applies to nonlinear semigroups as maps. III.9.B is restricted to bounded linear intertwiners between linear C0-semigroups. Do not transfer its generator criterion to maximal-monotone nonlinear flows without a separate theorem.

## D033 — next front is P9 migration, not automatic theorem prose

MOST/HCube has separated spectral, resolvent and semigroup-norm information, but it has not proved the historical Hessian-to-transient bridge.

Therefore:

\[
\boxed{\mathrm{NEXT}=\mathrm{P9\ HESSIAN\!-
TRANSIENT\ MIGRATION\ GATE}.}
\]

---

# C. Current handoff

\[
\boxed{
\mathrm{III.9\ DOM\!-\!LOGOS\ PASS}
\to
\mathrm{III.10\ SOP\!-\!11E\ SECTOR\ PASS}
\to
\mathrm{P9\ MIGRATION\ GATE\ NEXT}.
}
\]

Current control:

- `principia-v3-theorem-map-06.md`;
- `work-map-07.md`;
- `sop11e-wellposedness-migration-01.md`;
- `principia-v3-10-sop11e-wellposedness-sectors.md`;
- `principia-v3-sop11e-dom-logos-crosscheck-01.md`.

No CORE5 change and no Agent v03 witness.