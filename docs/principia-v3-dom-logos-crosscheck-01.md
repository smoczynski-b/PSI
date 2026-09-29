# PRINCIPIA SEMANTICA — VOLUME III / DOM-LOGOS CROSSCHECK 01

**Status:** `GLOBAL/COMPOSITION CROSSCHECK PASS`  
**Date:** 2026-09-29  
**Scope:** `III.9` against `II.6` and `III.1–III.6`  
**Inputs:** `dom-logos-source-bind-01.md`, `principia-v3-09-semigroup-projectability-dom-logos.md`, `principia-v2-06-deterministic-quotient-dynamics.md`, PHISICA operator block.

---

## 1. Question

Does III.9 migrate the recovered semigroup/domain LOGOS source without:

1. duplicating or contradicting II.6;
2. confusing state-semigroup projectability with operator-on-observables projectability;
3. using unbounded generators outside their domains;
4. turning a nonlinear infinitesimal identity into a global reduction theorem without well-posedness;
5. re-promoting LOGOS to the PSI core?

---

## 2. Result

\[
\boxed{
\mathrm{III.9\ DOM\!-
LOGOS}
=
\mathrm{COMPOSITION\ PASS}.
}
\]

No theorem-level errata are required.

---

## 3. Relation to II.6

II.6 proves for one deterministic map \(\delta\) and one equivalence relation \(E\):

\[
xEy\Rightarrow\delta(x)E\delta(y)
\]

iff the dynamics descends uniquely to the quotient.

III.9.A applies the same logic to every member of a semigroup:

\[
\Lambda x=\Lambda y
\Rightarrow
\Lambda S(t)x=\Lambda S(t)y
\quad\forall t\ge0.
\]

This is equivalent to existence of a unique induced semigroup on \(\operatorname{im}\Lambda\).

Thus:

\[
\boxed{
\mathrm{III.9.A}
=
\text{time-indexed semigroup realization of the II.6 congruence principle}.
}
\]

II.6 explicitly did not assert existence of a continuous-time semigroup or generator, so III.9 is not a duplicate theorem.

The shared permanent boundary survives:

\[
\boxed{
\text{static task adequacy}
\not\Rightarrow
\text{dynamic projectability}.
}
\]

---

## 4. Relation to III.1–III.6 PHISICA

III.1 considers an operator acting on pullbacks of functions:

\[
T_\Lambda\Phi=\Phi\circ\Lambda,
\qquad
\Delta_gT_\Lambda=T_\Lambda L_\Lambda.
\]

III.9 considers state-space dynamics:

\[
\Lambda S(t)=\widetilde S(t)\Lambda.
\]

These statements have different types and variance.

Therefore:

\[
\boxed{
\text{operator-on-observables projectability}
\neq
\text{state-semigroup projectability}.
}
\]

A concrete bridge may exist in a declared Koopman/transfer/state-observable framework, but no such bridge is imported silently here.

PHISICA III.2–III.6 add weighted Hilbert realization, self-adjoint domains, spectral theory, Liouville transformation and perturbation under progressively stronger contracts. None of those properties follows automatically from III.9 semigroup projectability alone.

---

## 5. Generator/domain audit

For linear bounded \(T:X\to Y\) between \(C_0\)-semigroups, III.9.B proves exactly:

\[
TS(t)=\bar S(t)T
\quad\forall t\ge0
\]

iff

\[
T(D(A))\subseteq D(\bar A),
\qquad
\bar ATx=TAx
\quad(x\in D(A)).
\]

The domain inclusion is explicit and indispensable.

For nonlinear \(\Lambda\), III.9.D uses the generator identity only for

\[
x\in D(A),
\qquad
\Lambda(x)\in D(\bar A),
\]

with Fréchet differentiability at \(x\).

No domain-free use of \(A\) or \(\bar A\) occurs.

---

## 6. Nonlinear converse boundary

The recovered source makes semigroup projectability primary and the differential identity derivative.

III.9 preserves that direction:

\[
\boxed{
\Lambda S(t)=\bar S(t)\Lambda
\Longrightarrow
D\Lambda(x)Ax=\bar A\Lambda(x)
}
\]

under the declared domain/differentiability hypotheses.

It does not claim the converse for nonlinear \(\Lambda\).

A nonlinear converse would require, at minimum, a well-posed reduced evolution and uniqueness sufficient to identify

\[
t\mapsto\Lambda(S(t)x)
\]

with the reduced solution from the same initial reduced state.

Permanent lock:

\[
\boxed{
\text{infinitesimal compatibility}
\not\Rightarrow
\text{global nonlinear reduction without well-posedness}.
}
\]

---

## 7. Image discipline

III.9.A determines the induced semigroup uniquely only on

\[
\operatorname{im}\Lambda.
\]

No arbitrary extension to a larger codomain is claimed unique.

This matches the general PSI factorization rule: uniqueness is on the image unless an extension contract is separately supplied.

---

## 8. CORE status

DOM-LOGOS is a realization of dynamic projectability and kernel/factorization logic.

It introduces no new semantic role beyond CORE5.

\[
\boxed{
\mathrm{CORE5\ CHANGE}=NONE.
}
\]

No Agent v03 witness is produced.

---

## 9. Verdict and next dependency

\[
\boxed{
\mathrm{DOM\!-
LOGOS\ SOURCE\ BIND}=PASS,
\qquad
\mathrm{III.9}=PASS,
\qquad
\mathrm{COMPOSITION\ CHECK}=PASS.
}
\]

The unresolved condition exposed by III.9 is no longer domain syntax but **well-posedness of the nonlinear/reduced evolution**.

Therefore the next legal front is:

\[
\boxed{
\mathrm{SOP\!-
11E\ WELL\!-
POSEDNESS\ MIGRATION\ GATE}.
}

No III.10 theorem number is assigned until that source/status audit is completed.
