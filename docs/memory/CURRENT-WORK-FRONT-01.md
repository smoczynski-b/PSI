# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-10-01  
**Full bounded acceptance run:** `36781418888`  
**F5 preparation run:** `36784242295`  
**R5 real-render run:** `36788563749`  
**F4.4 typed-SPLIT run:** `36791415147`  
**Scope:** current work selection across mathematical, memory-efficacy and visualization fronts.  
**Does not modify:** CORE5, CANON-03, live FORUM gateway.

## Current decision

**P9-I — THEOREM-SELECTION / PROOF GATE `PASS`. NEXT: III.13 promotion / composition gate.**

The user selected the mathematical front. F4.4 remains closed and F5 remains frozen; neither is automatically resumed.

Current state:

```text
P9_GENERAL = OPEN / CENTRAL
P9_I_SOURCE_GATE = PASS
P9_I_THEOREM_SELECTION_PROOF = PASS
P9_I_SELECTED_STATEMENT = omega_0(T) = s_0(A) on complex Hilbert C0-semigroups
III.13 = NOT_YET_ASSIGNED
NEXT = III.13 PROMOTION / COMPOSITION GATE

FULL_BOUNDED_RUN = PASS_WITH_BOUNDARY
R9 = NOT_CREATED
R5 = PASS_WITH_BOUNDARY
F4.4 = PASS_WITH_BOUNDARY
F5_PREPARATION = PASS
F5_MODEL_EFFICACY = NOT_RUN
F5_EXECUTION = BLOCKED_BY_ZERO_ALLOCATED_CREDITS
```

Primary mathematical evidence:

- `docs/p9i-infinite-dimensional-resolvent-growth-source-gate-01.md`
- `docs/principia-v3-p9i-theorem-selection-proof-gate-01.md`
- `docs/principia-v3-theorem-map-10.md`
- `docs/work-map-11.md`
- `docs/falsifier-registry-13.md`

---

## P9-I proved candidate

The selected typed statement is

\[
\boxed{
\mathcal H\text{ complex Hilbert},
\quad
A:D(A)\subset\mathcal H\to\mathcal H
\text{ generator of a }C_0\text{-semigroup }T(t)
\Longrightarrow
\omega_0(T)=s_0(A).
}
\]

Here

\[
\omega_0(T)
=
\inf\{\gamma:\exists M\ge1,\ \|T(t)\|\le Me^{\gamma t}\},
\]

while

\[
s_0(A)
=
\inf\left\{a>s(A):
\sup_{\Re z\ge a}\|R(z,A)\|<\infty
\right\}.
\]

The two proof directions are separated:

```text
s_0 <= omega_0
    Laplace resolvent representation + exponential semigroup bound

omega_0 <= s_0
    shift B = A - aI, D(B)=D(A)
    + right-half-plane Gearhart-Pruss-Huang stability theorem
```

The Gearhart–Prüss–Huang theorem is imported as classical source material; the P9-I unit does not claim a new proof of that theorem or PSI novelty.

---

## F63 exact regression

For

\[
A=I,
\qquad
T(t)=e^tI,
\]

one has

\[
\omega_0(T)=1.
\]

Also, for every \(a>1\),

\[
\sup_{\Re z\ge a}\|(zI-I)^{-1}\|
=
\frac1{a-1},
\]

so

\[
\boxed{s_0(A)=1=\omega_0(T)}.
\]

Yet

\[
\sup_{\beta\in\mathbb R}\|(i\beta I-I)^{-1}\|=1.
\]

Therefore the passed theorem preserves the permanent distinction

\[
\boxed{
\text{imaginary-axis boundedness}
\neq
s_0(A)<0.
}
\]

F63 passes.

---

## F64 boundary

The theorem compares exponential abscissae. It does not assert

\[
\mathcal K(A)<\infty
\Rightarrow
\sup_t\|T(t)\|<\infty.
\]

Subexponential but unbounded growth is compatible with

\[
\omega_0(T)=s_0(A)=0.
\]

Therefore

\[
\boxed{
\omega_0=s_0
\not\Rightarrow
\text{uniform boundedness or peak-amplification control}.
}
\]

F64 passes.

---

## Composition with III.9 / III.11 / III.12

### III.9 DOM-LOGOS

The proof uses only

\[
A\mapsto A-aI,
\qquad
D(A-aI)=D(A),
\]

so no unbounded-generator domain is erased.

### III.11 P9-G

For the finite-dimensional metric-gradient subclass, III.11 is stronger: it gives exact adapted-metric semigroup and resolvent laws, not only the exponential abscissa. P9-I does not replace it.

### III.12 P9-H

A coercive Lyapunov metric yields

\[
\omega_0(T)\le-\lambda,
\qquad
s_0(A)\le-\lambda,
\]

and P9-I identifies the two exponential-level quantities:

\[
\omega_0(T)=s_0(A)\le-\lambda.
\]

P9-I does not construct \(Q\), \(\lambda\), a condition number, a pseudospectral edge or a transient prefactor.

---

## Permanent boundary

The proof gate does not establish:

```text
Hilbert equality -> Banach equality
omega_0 = s_0 -> omega_0 = s(A)
omega_0 = 0 -> uniform semigroup boundedness
s_0 -> peak transient amplification
s_0 -> Kreiss theorem
s_0 -> coercive Lyapunov metric
polynomial resolvent growth -> polynomial norm decay of T(t)
P9-I proof PASS -> P9 general closure
classical theorem -> PSI novelty
```

Thus

\[
\boxed{P9_{\rm general}=OPEN/CENTRAL}
\]

is unchanged.

---

## Next mathematical unit

The candidate is now eligible for a separate numbering/promotion step.

The next unit must decide whether to materialize

\[
\boxed{\omega_0(T)=s_0(A)}
\]

as **III.13**, and if it does, it must preserve exactly the Hilbert-space generator contract and cross-link III.9, III.11, III.12, F63 and F64 without widening the conclusion.

The current automatic next step is therefore only:

```text
III.13 PROMOTION / COMPOSITION GATE
```

No III.13 file has yet been created.

---

## F4.4 / R5 frozen visual state

F4.4 remains `PASS_WITH_BOUNDARY`; R5 remains `PASS_WITH_BOUNDARY`. No F4.5 or other automatic visual successor is defined.

No visual work is resumed while P9-I is the selected front.

---

## Frozen F5-HOLDOUT-V1

F5 remains unchanged. The held-out set is still:

```text
H10 = II.10 strong lumpability bridge
H11 = II.11 Myhill-Nerode bridge
H12 = II.12 Paige-Tarjan benchmark
```

Resume plan, only when model credits exist:

```text
1. H10-C, blind id ANS-25E4942F7A3F
2. H10-A and H10-B if C executes technically
3. blind-score H10
4. only then decide on H11/H12
```

No F5 prompt, corpus, source selection or evaluator state is to be rebuilt because of the P9-I work.

---

## Auditor rule — Semantica Rozmowy 03

\[
P_i(S)\not\Rightarrow S.
\]

Current applications:

```text
P9-I source PASS != theorem proof PASS
P9-I proof PASS != III.13 promotion PASS
Hilbert theorem != Banach theorem
imaginary-axis bound != stability without the correct side contract
finite-dimensional Kreiss != infinite-dimensional boundedness
exponential abscissa != transient peak
classical bridge != PSI novelty
F4.4 PASS != general visual semantics
prepared F5 != model efficacy
```

## Stop

The current automatic next step is only the **III.13 promotion / composition gate**. Do not resume F4.x or F5 without an explicit front change or the F5 credit condition being met.
