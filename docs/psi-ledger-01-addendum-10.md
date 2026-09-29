# PSI — DECISION / EPISTEMIC LEDGER ADDENDUM 10

**Status:** `CURRENT P9-H CLOSURE / P9-I HANDOFF`  
**Date:** 2026-09-29  
**Base ledger:** `psi-ledger-01.md`  
**Previous addendum:** `psi-ledger-01-addendum-09.md`

---

# A. Epistemic updates

## E065 — hypocoercivity is not transient amplification

For

\[
A=S+N,
\quad S=S^*\le0,
\quad N^*=-N,
\]

the ambient norm is non-increasing. Modified energies recover a strict exponential rate from degenerate dissipation; they do not imply unavoidable transient growth.

## E066 — DMS source requires H1–H4

The DMS modified-entropy theorem depends on microscopic coercivity, macroscopic coercivity, \(\Pi T\Pi=0\), and bounded auxiliary operators. Generic bracket slogans are not an adequate replacement for these typed hypotheses.

## E067 — bounded coercive Lyapunov metrics give a full operator bridge

If

\[
mI\le Q\le MI,
\qquad
A^*Q+QA\le-2\lambda Q,
\]

then III.12 proves:

\[
\|e^{tA}\|_Q\le e^{-\lambda t},
\]

\[
\|(zI-A)^{-1}\|_Q\le(\Re z+\lambda)^{-1},
\]

\[
\mathcal K_Q(A)=1,
\]

and explicit ambient-norm / pseudospectral bounds through \(\sqrt{\kappa(Q)}\).

## E068 — Kreiss constant does not encode decay rate

Even with different strict rates \(\lambda>0\), the modified-norm continuous-time Kreiss constant remains \(1\). The decay margin is encoded in the shifted resolvent half-plane, not in \(\mathcal K\) alone.

## E069 — III.11 is a special case of III.12

For \(A=-G^{-1}H\), choose \(Q=G\). Then

\[
A^*G+GA=-2H\le-2\mu_GG.
\]

III.11 remains stronger in that subclass because it has a self-adjoint normal form and exact spectral-distance formulas.

---

# B. Decision updates

## D038 — label all norm-sensitive observables by their norm contract

Pseudospectra, resolvent norms, numerical abscissae and transient amplification must be indexed by the declared metric/norm whenever more than one equivalent norm is in play.

## D039 — do not infer transient growth from hypocoercivity

Permanent rule:

\[
\boxed{
\text{hypocoercivity}
\not\Rightarrow
\text{ambient-norm transient amplification}.
}
\]

## D040 — do not use Kreiss as a decay-rate surrogate

Permanent rule:

\[
\boxed{
\mathcal K(A)
\neq
\text{spectral/growth margin}.
}
\]

## D041 — next front is P9-I

The next source gate is the genuinely infinite-dimensional relation between resolvent control and semigroup growth, including Gearhart–Prüss scope and failures of finite-dimensional Kreiss equivalence.

No III.13 number is assigned before that gate.

---

# C. Current handoff

\[
\boxed{
\mathrm{III.11\ P9\!-
G\ PASS}
\to
\mathrm{III.12\ P9\!-
H\ PASS}
\to
\mathrm{P9\!-
I\ SOURCE\ GATE\ NEXT}.
}
\]

Current control:

- `p9u-hypocoercive-source-contract-01.md`;
- `principia-v3-12-hypocoercive-modified-energy-bridge.md`;
- `principia-v3-p9h-composition-crosscheck-01.md`;
- `principia-v3-theorem-map-08.md`;
- `work-map-09.md`.

No CORE5 change and no Agent v03 witness.