# PRINCIPIA SEMANTICA — VOLUME III / P9-H COMPOSITION CROSSCHECK 01

**Status:** `COMPOSITION CROSSCHECK PASS`  
**Date:** 2026-09-29  
**Scope:** `III.7–III.12`

---

# 1. Result

\[
\boxed{
\mathrm{III.7:III.12}
=
\mathrm{COMPOSITION\ PASS}.
}
\]

No theorem-level errata are required.

The unrestricted P9 problem remains

\[
\boxed{P9_{\rm general}=OPEN/CENTRAL.}
\]

---

# 2. III.11 is a special case of III.12

For the metric-gradient sector

\[
A=-G^{-1}H,
\qquad G,H>0,
\]

we have

\[
A^*G+GA=-2H.
\]

If

\[
\mu_G
=
\inf_{x\ne0}
\frac{\langle Hx,x\rangle}{\langle Gx,x\rangle},
\]

then

\[
H\ge\mu_G G,
\]

so

\[
\boxed{
A^*G+GA\le-2\mu_GG.
}
\]

Thus III.11 is contained in III.12 with

\[
Q=G,
\qquad
\lambda=\mu_G.
\]

III.11 is stronger inside that subclass because the transformed generator is self-adjoint and therefore gives exact spectral-distance resolvent formulas. III.12 only requires strict dissipativity in an equivalent metric and therefore gives bounds rather than a normal spectral formula.

---

# 3. MOST compatibility

Pseudospectra and resolvent norms are norm-dependent. III.12 therefore keeps separate:

\[
\sigma_\varepsilon^{(Q)}(A)
\]

and the pseudospectrum in the ambient norm.

The bounds are connected only through the norm-equivalence constant

\[
c_Q=\sqrt{\kappa(Q)}.
\]

This is compatible with III.7 MOST: changing the norm changes the representation contract. No statement identifies pseudospectra computed in inequivalent declared norms.

Permanent rule:

\[
\boxed{
\text{modified metric}
\Rightarrow
\text{new norm-sensitive operator representation}.
}
\]

---

# 4. Kreiss constant versus decay rate

III.12 proves

\[
\mathcal K_Q(A)=1
\]

for every strictly \(Q\)-dissipative rate \(\lambda>0\).

Therefore the normalized continuous-time Kreiss constant does **not** encode the decay rate.

The rate appears instead in

\[
\|(zI-A)^{-1}\|_Q
\le
\frac1{\Re z+\lambda}
\]

and in the pseudospectral right edge

\[
\sup\Re\sigma_\varepsilon^{(Q)}(A)
\le
-\lambda+\varepsilon.
\]

Permanent distinction:

\[
\boxed{
\text{Kreiss amplification index}
\neq
\text{spectral/growth margin}.
}
\]

This is consistent with the earlier scalar witness \(A=-\mu I\), where \(\mathcal K(A)=1\) for all \(\mu>0\).

---

# 5. Hypocoercivity versus transient growth

For a standard hypocoercive decomposition

\[
A=S+N,
\quad S=S^*\le0,
\quad N^*=-N,
\]

the ambient norm is non-increasing.

Thus III.12 is a bridge from degenerate dissipation to a strict exponential rate in an adapted norm. It is not a theorem asserting amplification in the original norm.

The finite-dimensional witness

\[
A=
\begin{pmatrix}0&1\\-1&-1\end{pmatrix}
\]

makes this explicit: the ambient norm is contractive, while a coercive \(Q\) supplies a strict exponential Lyapunov estimate.

---

# 6. DMS / Villani source boundary

DMS supplies a constructive modified entropy only under its typed kinetic assumptions H1–H4. Villani-style commutator methods likewise require structural hypotheses.

Neither source licenses:

\[
\boxed{
\forall\ A\text{ nonnormal exponentially stable}
\quad
\exists\text{ explicit useful }Q
}
\]

as a universal constructive theorem.

III.12 is conditional on the existence of the declared bounded coercive Lyapunov metric.

---

# 7. Updated P9 taxonomy

## P9-G — metric-gradient

`CLOSED` as III.11; exact normal form after metric transport.

## P9-H — hypocoercive / Lyapunov-metric

`CLOSED CONDITIONALLY` as III.12: once a bounded coercive \(Q\) satisfying the Lyapunov inequality is constructed, semigroup, resolvent, Kreiss and pseudospectral bounds follow.

DMS provides a constructive source for important kinetic subclasses.

## P9-J — Jordan / defective local laboratory

`CLOSED LOCAL LABORATORY`.

## P9-U — unrestricted nonnormal generators

`OPEN / CENTRAL`.

---

# 8. CORE / Agent impact

No new semantic role appears. The modified metric is part of the realization/representation contract and all conclusions remain task- and norm-relative.

Thus

\[
\boxed{\mathrm{CORE5\ CHANGE}=NONE},
\]

\[
\boxed{\mathrm{AGENT\ v03\ WITNESS}=NONE}.
\]

---

# 9. Verdict

\[
\boxed{
\mathrm{III.7:III.12}
=
\mathrm{COMPOSITION\ PASS}.
}
\]

A further theorem unit requires a new typed unresolved subclass. The most natural remaining gate is the genuinely infinite-dimensional resolvent-to-growth problem, where finite-dimensional Kreiss equivalence fails and Gearhart–Prüss supplies only class-specific Hilbert-space control.