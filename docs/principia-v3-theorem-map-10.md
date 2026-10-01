# PRINCIPIA SEMANTICA — VOLUME III THEOREM MAP 10

**Status:** `CURRENT / III.1:III.12 CLOSED AS PREVIOUSLY / P9-I THEOREM-SELECTION+PROOF PASS / III.13 PROMOTION-COMPOSITION GATE NEXT`  
**Date:** 2026-10-01  
**Supersedes for control:** `principia-v3-theorem-map-09.md`

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

# 2. P9-I theorem-selection/proof gate

The proof unit

`principia-v3-p9i-theorem-selection-proof-gate-01.md`

has passed.

Exactly one statement was selected:

\[
\boxed{
\mathcal H\text{ complex Hilbert},
\quad
A:D(A)\subset\mathcal H\to\mathcal H
\text{ generator of a }C_0\text{-semigroup }T
\Longrightarrow
\omega_0(T)=s_0(A).
}
\]

The statement is `CLASSICAL / ADAPTED`, not `PSI-NEW`.

---

# 3. Proof basis

The proof is split into the two legal directions:

\[
\boxed{s_0(A)\le\omega_0(T)}
\]

from the Laplace resolvent representation, and

\[
\boxed{\omega_0(T)\le s_0(A)}
\]

from the generator shift

\[
B=A-aI,
\qquad
D(B)=D(A),
\]

plus the imported classical right-half-plane Gearhart–Prüss–Huang stability theorem.

Thus the proof does not treat the full Gearhart–Prüss–Huang theorem as newly derived; it derives the selected P9-I equality from that sourced classical lemma.

---

# 4. Regression and composition status

The proof gate records:

- **F63 PASS:** for \(A=I\), \(\omega_0=s_0=1\) although the imaginary-axis resolvent is uniformly bounded; hence axis boundedness is not silently substituted for \(s_0<0\);
- **F64 PASS:** \(\omega_0=s_0\) concerns exponential abscissae and does not imply uniform boundedness or a dimension-free Kreiss theorem;
- **III.9 PASS:** the shift preserves the generator domain;
- **III.11 PASS:** P9-I is weaker than the exact metric-gradient finite-time norm/resolvent geometry;
- **III.12 PASS:** a coercive Lyapunov metric implies \(\omega_0=s_0\le-\lambda\), but P9-I does not construct the metric or its constants.

---

# 5. Permanent boundary

The passed statement does not imply

\[
\omega_0(T)=s(A)
\]

in general infinite dimension, and does not identify

\[
\sup_t\|T(t)\|,
\qquad
\mathcal K(A),
\qquad
\|T(t)A^{-1}\|.
\]

In particular,

\[
\boxed{
\omega_0(T)=0
\not\Rightarrow
\sup_{t\ge0}\|T(t)\|<\infty.
}
\]

No Banach-space export is authorized.

---

# 6. Current open front

The selected candidate is now eligible for theorem promotion, but this map does not itself create III.13.

A promotion/composition unit must:

1. decide whether the classical adapted equality deserves a numbered Volume III bridge;
2. if yes, materialize the theorem unit without widening its contract;
3. cross-link III.9, III.11, III.12 and F63–F64;
4. preserve \(P9_{\rm general}=OPEN/CENTRAL\);
5. avoid any claim of a universal resolvent-to-transient theorem.

Therefore the next legal state is

\[
\boxed{
\mathrm{III.13\ PROMOTION/COMPOSITION\ GATE\ NEXT}.
}
\]

No CORE5 change.  
No Agent v03 witness.
