# PRINCIPIA SEMANTICA — VOLUME III THEOREM MAP 09

**Status:** `CURRENT / III.1:III.12 CLOSED AS PREVIOUSLY / P9-I SOURCE GATE PASS / III.13 THEOREM-SELECTION GATE NEXT`  
**Date:** 2026-10-01  
**Supersedes for control:** `principia-v3-theorem-map-08.md`

---

# 1. Closed blocks retained

\[
\boxed{\mathrm{III.1:III.6\ PHISICA}=GLOBAL\ PASS}
\]

\[
\boxed{\mathrm{III.7:III.8\ MOST/HCube}=GLOBAL\ PASS}
\]

\[
\boxed{\mathrm{III.9\ DOM\!-\!LOGOS}=PASS/COMPOSITION\ PASS}
\]

\[
\boxed{\mathrm{III.10\ SOP\!-\!11E}=SECTOR\ PASS}
\]

\[
\boxed{\mathrm{III.11\ P9\!-\!G}=PASS}
\]

\[
\boxed{\mathrm{III.12\ P9\!-\!H}=PASS}
\]

with

\[
\boxed{P2_{\rm general}=PARTIAL},
\qquad
\boxed{P9_{\rm general}=OPEN/CENTRAL}.
\]

No status of III.1–III.12 is changed by this map.

---

# 2. P9-I source/contract gate

The source gate

`p9i-infinite-dimensional-resolvent-growth-source-gate-01.md`

has passed.

Its object is a densely defined closed generator

\[
A:D(A)\subset X\to X
\]

of a strongly continuous semigroup \(T(t)\).

The gate separates the following observables:

\[
\boxed{
\begin{array}{rcl}
s(A) &:& \text{spectral bound},\\
\omega_0(T) &:& \text{semigroup growth bound},\\
s_0(A) &:& \text{uniform-resolvent abscissa},\\
\mathcal K(A) &:& \text{Kreiss index},\\
\sup_t\|T(t)\| &:& \text{peak amplification},\\
\|T(t)A^{-1}\| &:& \text{regularized decay observable}.
\end{array}
}
\]

These are not interchangeable without a class contract.

---

# 3. Legal P9-I ladder

## 3.1 Hilbert exponential-growth layer

For a \(C_0\)-semigroup on a complex Hilbert space, the classical Gearhart–Prüss–Huang theory yields

\[
\boxed{\omega_0(T)=s_0(A)}.
\]

This is the most conservative candidate for a future III.13 bridge.

## 3.2 Bounded-Hilbert polynomial layer

For a bounded \(C_0\)-semigroup on Hilbert space with \(i\mathbb R\subset\rho(A)\), Borichev–Tomilov gives, for \(\alpha>0\),

\[
\|R(is,A)\|=O(|s|^\alpha)
\iff
\|T(t)A^{-1}\|=O(t^{-1/\alpha}).
\]

The target is the regularized observable \(T(t)A^{-1}\), not operator-norm decay of the whole semigroup.

## 3.3 m-accretive quantitative layer

For m-accretive \(H\) on Hilbert space, Wei's quantitative estimate supplies an explicit resolvent/coercivity-to-decay bridge under that restricted class contract.

## 3.4 Kreiss layer

Finite-dimensional continuous-time Kreiss theory is dimension-dependent. Infinite-dimensional Kreiss boundedness does not imply uniform semigroup boundedness in general.

---

# 4. Permanent falsifier locks added by P9-I

Current versioned falsifier registry is `falsifier-registry-13.md`.

New locks:

- **F63:** uniform imaginary-axis resolvent boundedness alone does not imply exponential stability of an arbitrary Hilbert-space \(C_0\)-semigroup;
- **F64:** finite-dimensional Kreiss control cannot be exported as a dimension-free infinite-dimensional boundedness theorem.

The exact scalar witness for F63 is \(A=I\), for which \(T(t)=e^tI\) but

\[
\sup_{\beta\in\mathbb R}\|(i\beta I-I)^{-1}\|=1.
\]

---

# 5. What P9-I source PASS does not mean

The source gate does not prove:

1. a universal scalar resolvent statistic controlling all nonnormal dynamics;
2. \(\omega_0=s_0\) on arbitrary Banach spaces;
3. a dimension-free Kreiss matrix theorem;
4. polynomial operator-norm decay of \(T(t)\) from polynomial imaginary-axis resolvent growth;
5. a general coercive Lyapunov metric constructed from resolvent data;
6. a theorem about every continuous-spectrum generator;
7. a new PSI primitive.

Thus

\[
\boxed{
\mathrm{P9\!-\!I\ SOURCE\ PASS}
\not\Rightarrow
\mathrm{III.13\ THEOREM\ PASS}.
}
\]

---

# 6. Current open front

The next legal unit is a **theorem-selection / proof gate**.

It must select exactly one typed statement from the source-gated ladder, prove or correctly import it under explicit hypotheses, and crosscheck it against F63–F64 plus the P9-G/P9-H boundaries.

The default conservative candidate is

\[
\boxed{
X=\mathcal H,
\qquad
\omega_0(T)=s_0(A).
}
\]

but this map does not itself assign the label III.13 to that candidate.

Therefore the current execution state is

\[
\boxed{
\mathrm{P9\!-\!I\ THEOREM\!-
SELECTION/PROOF\ GATE\ NEXT}.
}
\]

No CORE5 change.  
No Agent v03 witness.  
No III.13 theorem is yet authorized.
