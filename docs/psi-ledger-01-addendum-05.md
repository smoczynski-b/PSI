# PSI — DECISION / EPISTEMIC LEDGER ADDENDUM 05

**Status:** `CURRENT MOST / HCUBE HANDOFF`  
**Date:** 2026-09-29  
**Base ledger:** `psi-ledger-01.md`  
**Previous addendum:** `psi-ledger-01-addendum-04.md`

---

# A. Epistemic updates

## E044 — source status of MOST versus MOS clarified

The physical project source strongly binds the MOS/P9 operator lesson:

\[
\boxed{
\text{nonnormal stability may require resolvent and semigroup information beyond spectrum}.
}
\]

The exact expansion of the historical acronym `MOST` is not physically source-bound strongly enough to canonize. `MOST` is therefore retained only as the established project label for the operator-information layer.

No semantic analogy is promoted without a concrete operator.

## E045 — exact spectral/resolvent information factorization

For finite-dimensional operators with fixed norm, III.7 defines

\[
\rho_\sigma(A)=\sigma(A),
\]

\[
r_A(z)=\|(zI-A)^{-1}\|
\]

with value `+infinity` on the spectrum, and the full pseudospectral family

\[
\rho_{ps}(A)=\bigl(\sigma_\varepsilon(A)\bigr)_{\varepsilon>0}.
\]

Result:

\[
\boxed{
\ker_{eq}\rho_r
=
\ker_{eq}\rho_{ps}
\subseteq
\ker_{eq}\rho_\sigma.
}
\]

Thus the full pseudospectral family and the full resolvent-norm profile are equivalent representations under the declared convention, while the spectrum is a coarser factor.

## E046 — strictness witnesses

HCube / Regression R01 establishes

\[
\boxed{
\text{spectrum + operator norm}
\not\Rightarrow
\text{resolvent-task adequacy}.
}
\]

III.7 also adds a basis-sensitive directional witness:

\[
A=\operatorname{diag}(0,1),
\qquad
B=\operatorname{diag}(1,0).
\]

The complete resolvent-norm profiles agree, but

\[
\langle e_1,(2I-A)^{-1}e_1\rangle=1/2,
\qquad
\langle e_1,(2I-B)^{-1}e_1\rangle=1.
\]

This witness is legal only in a contract where unitary similarity is not gauge.

## E047 — no total scalar order between resolvent and transient-growth summaries

III.7 records the branched information diagram

\[
A\to\mathcal R_A(\cdot)\to r_A(\cdot)
\leftrightarrow\rho_{ps}(A)\to\rho_\sigma(A),
\]

and separately

\[
A\to e^{tA}\to\|e^{tA}\|.
\]

No unproved factorization between the scalar resolvent-norm profile and the scalar semigroup-norm profile is inserted.

---

# B. Decision updates

## D024 — define MOST by PSI adequacy, not by one privileged representation

MOST is not promoted as a new primitive or as a fixed universal data structure.

The controlling rule is

\[
\boxed{
\ker_{eq}\rho\subseteq E_{\mathcal T}.
}
\]

Operationally:

\[
\boxed{
\text{retain the coarsest operator-information representation that preserves the declared task distinctions}.
}
\]

## D025 — keep MOS/P9 and MOST scopes distinct

Import from MOS only typed operator facts actually supported by source and theorem.

Do not import as theorem:

- semantic resolvent analogies;
- global MOS composition closure;
- a universal Hessian-to-Kreiss theorem;
- a total resolvent-to-semigroup scalar information order.

## D026 — release HCube as III.8 laboratory

Next unit:

\[
\boxed{
\mathrm{III.8\ —\ HCUBE\ NONNORMAL/RESOLVENT\ LAB}.
}
\]

III.8 must classify the frozen HCube witness against the representation levels of III.7 and build an explicit task/representation PASS-FAIL matrix. Repeating only the arithmetic from Regression R01 is insufficient.

---

# C. Current handoff

\[
\boxed{
\mathrm{PHISICA\ III.1:III.6\ GLOBAL\ PASS}
\to
\mathrm{III.7\ MOST\ PASS}
\to
\mathrm{III.8\ HCUBE\ NEXT}.
}
\]

Current control:

- `principia-v3-theorem-map-03.md`;
- `work-map-04.md`;
- `principia-v3-07-spectral-information-hierarchy-most.md`.

No CORE5 change and no Agent v03 witness.