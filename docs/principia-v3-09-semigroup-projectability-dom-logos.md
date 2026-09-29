# PRINCIPIA SEMANTICA — VOLUME III.9

## DOM-LOGOS — projektowalność półgrupy, dziedziny generatorów i redukcja dynamiczna

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Source bind:** `dom-logos-source-bind-01.md`  
**Historical source:** `PRINCIPIA_SEMANTICA_KANON_SCALONY_2026-07-26A.tex`  
**Current role:** Volume III realization of dynamic projectability; no new PSI primitive.

---

# 1. Contract and source normalization

The recovered source defines LOGOS dynamically by semigroup intertwining:

\[
\Lambda(S(t)x)=\bar S(t)\Lambda(x).
\]

The current migration keeps this as the primary statement and treats generator identities as derivative or linear-generator forms requiring explicit domains.

Throughout, a semigroup means a family \(S(t)\), \(t\ge0\), satisfying

\[
S(0)=\operatorname{Id},
\qquad
S(t+s)=S(t)S(s).
\]

No continuity is required in the first set-theoretic theorem. Banach-space and \(C_0\)-semigroup hypotheses are introduced only where generators are used.

---

# 2. Theorem III.9.A — exact projectability of a semigroup through a reduction

Let \(X\) be a set, let

\[
S(t):X\to X,
\qquad t\ge0,
\]

be a semigroup of maps, and let

\[
\Lambda:X\to Z
\]

be any representation/reduction.

Define

\[
E_\Lambda:=\ker_{eq}\Lambda.
\]

The following are equivalent.

### (i) Forward congruence of fibres

For every \(t\ge0\),

\[
\boxed{
\Lambda(x)=\Lambda(y)
\Longrightarrow
\Lambda(S(t)x)=\Lambda(S(t)y).
}
\]

Equivalently,

\[
\boxed{
E_\Lambda
\subseteq
\ker_{eq}(\Lambda\circ S(t))
\qquad\forall t\ge0.
}
\]

### (ii) Existence of reduced semigroup on the image

There exists a unique semigroup

\[
\widetilde S(t):\operatorname{im}\Lambda\to\operatorname{im}\Lambda
\]

such that

\[
\boxed{
\Lambda\circ S(t)
=
\widetilde S(t)\circ\Lambda
\qquad\forall t\ge0.
}
\]

## Proof

Assume (i). Define

\[
\widetilde S(t)(\Lambda(x))
:=
\Lambda(S(t)x).
\]

Condition (i) makes this independent of the chosen representative \(x\), so \(\widetilde S(t)\) is well defined on \(\operatorname{im}\Lambda\).

Moreover,

\[
\widetilde S(0)(\Lambda x)
=\Lambda(S(0)x)
=\Lambda x,
\]

and

\[
\widetilde S(t+s)(\Lambda x)
=\Lambda(S(t+s)x)
=\Lambda(S(t)S(s)x)
\]

\[
=\widetilde S(t)(\Lambda(S(s)x))
=\widetilde S(t)\widetilde S(s)(\Lambda x).
\]

Thus \(\widetilde S\) is a semigroup and the intertwining identity holds.

Uniqueness is only on \(\operatorname{im}\Lambda\): if another semigroup \(R(t)\) satisfies the same intertwining relation, then

\[
R(t)(\Lambda x)=\Lambda(S(t)x)=\widetilde S(t)(\Lambda x).
\]

Conversely, if (ii) holds and \(\Lambda x=\Lambda y\), then

\[
\Lambda(S(t)x)
=\widetilde S(t)\Lambda x
=\widetilde S(t)\Lambda y
=\Lambda(S(t)y).
\]

Hence (i). \(\square\)

---

# 3. Interpretation — dynamic quotient, not new primitive

III.9.A is the semigroup/time-indexed form of the existing PSI quotient logic.

A representation \(\Lambda\) supports autonomous reduced dynamics exactly when its fibres are congruent under the original dynamics:

\[
\boxed{
\text{same reduced state now}
\Longrightarrow
\text{same reduced state after every }t.
}
\]

Thus DOM-LOGOS is a realization of dynamic projectability already anticipated by Volume II.6. It does not add a sixth CORE role.

Permanent distinction:

\[
\boxed{
\text{static task adequacy}
\not\Rightarrow
\text{semigroup projectability}.
}
\]

A representation may preserve all current task observables yet fail to support autonomous future dynamics.

---

# 4. Prescribed reduced dynamics and the image boundary

Suppose a larger codomain \(\bar X\) and a prescribed semigroup

\[
\bar S(t):\bar X\to\bar X
\]

are given, with

\[
\Lambda:X\to\bar X.
\]

Then source-level LOGOS legality is the stronger requirement

\[
\boxed{
\Lambda\circ S(t)=\bar S(t)\circ\Lambda.
}
\]

III.9.A shows that if only \(S\) and \(\Lambda\) are given, the induced reduced dynamics is determined uniquely only on

\[
\operatorname{im}\Lambda.
\]

Therefore:

\[
\boxed{
\text{reduced dynamics on }\operatorname{im}\Lambda
\neq
\text{a unique extension to an arbitrary larger codomain}.
}
\]

This is the dynamic analogue of the general PSI rule that factor maps are unique on the image, not automatically outside it.

---

# 5. Theorem III.9.B — bounded linear intertwiner for \(C_0\)-semigroups

Let \(X,Y\) be Banach spaces. Let

\[
S(t):X\to X,
\qquad
\bar S(t):Y\to Y
\]

be strongly continuous semigroups with generators

\[
A:D(A)\subset X\to X,
\qquad
\bar A:D(\bar A)\subset Y\to Y.
\]

Let

\[
T\in\mathcal B(X,Y)
\]

be bounded linear.

Then the following are equivalent.

### (i) Semigroup intertwining

\[
\boxed{
T S(t)=\bar S(t)T
\qquad\forall t\ge0.
}
\]

### (ii) Generator intertwining with domain legality

\[
\boxed{
T(D(A))\subseteq D(\bar A),
\qquad
\bar A T x=T A x
\quad\forall x\in D(A).
}
\]

## Proof: (i) \(\Rightarrow\) (ii)

Take \(x\in D(A)\). Then

\[
\frac{S(t)x-x}{t}\to Ax
\qquad(t\downarrow0).
\]

Because \(T\) is bounded,

\[
\frac{\bar S(t)Tx-Tx}{t}
=
T\frac{S(t)x-x}{t}
\to TAx.
\]

Hence \(Tx\in D(\bar A)\) and

\[
\bar A Tx=TAx.
\]

## Proof: (ii) \(\Rightarrow\) (i)

Choose \(\lambda\) in a common right half-plane contained in the resolvent sets of \(A\) and \(\bar A\). For \(y\in X\), put

\[
x=R(\lambda,A)y\in D(A).
\]

Then by (ii),

\[
(\lambda I-\bar A)Tx
=T(\lambda I-A)x
=Ty.
\]

Therefore

\[
T R(\lambda,A)y
=R(\lambda,\bar A)Ty.
\]

So for every sufficiently large real \(\lambda\),

\[
\boxed{
T R(\lambda,A)
=R(\lambda,\bar A)T.
}
\]

Using the Laplace representation of the resolvent of a \(C_0\)-semigroup,

\[
R(\lambda,A)x
=
\int_0^\infty e^{-\lambda t}S(t)x\,dt,
\]

and likewise for \(\bar A\), we obtain equality of the Laplace transforms of the continuous exponentially bounded functions

\[
t\mapsto TS(t)x
\]

and

\[
t\mapsto\bar S(t)Tx.
\]

Uniqueness of the Laplace transform gives

\[
TS(t)x=\bar S(t)Tx
\qquad\forall t\ge0.
\]

Thus (i). \(\square\)

---

# 6. Corollary III.9.C — the source domain condition is exact in the linear \(C_0\) sector

The recovered historical requirement

\[
T(D(A))\subseteq D(\bar A),
\qquad
TAx=\bar ATx
\]

is not merely a formal infinitesimal heuristic.

Under the precise hypotheses of III.9.B it is equivalent to global semigroup intertwining:

\[
\boxed{
TS(t)=\bar S(t)T
\iff
T(D(A))\subseteq D(\bar A)
\land
\bar AT=TA\text{ on }D(A).
}
\]

The domain clause is essential because \(Ax\) is not defined outside \(D(A)\).

---

# 7. Proposition III.9.D — nonlinear generator identity is a derivative consequence

Let \(X,Y\) be Banach spaces, let \(S(t)\), \(\bar S(t)\) be \(C_0\)-semigroups with generators \(A\), \(\bar A\), and let

\[
\Lambda:X\to Y
\]

satisfy

\[
\Lambda(S(t)x)=\bar S(t)\Lambda(x).
\]

Fix \(x\in D(A)\). Assume:

1. \(\Lambda\) is Fréchet differentiable at \(x\);
2. \(\Lambda(x)\in D(\bar A)\).

Then

\[
\boxed{
D\Lambda(x)Ax
=
\bar A\Lambda(x).
}
\]

## Proof

For \(x\in D(A)\),

\[
S(t)x=x+tAx+o(t)
\]

in \(X\). Fréchet differentiability gives

\[
\Lambda(S(t)x)
=
\Lambda(x)+tD\Lambda(x)Ax+o(t).
\]

Because \(\Lambda(x)\in D(\bar A)\),

\[
\bar S(t)\Lambda(x)
=
\Lambda(x)+t\bar A\Lambda(x)+o(t).
\]

The semigroup intertwining identity equates these expansions, yielding the claim. \(\square\)

---

# 8. Nonlinear converse boundary

III.9.D is stated only in the direction

\[
\boxed{
\text{semigroup intertwining}
\Longrightarrow
\text{generator identity}.
}
\]

For nonlinear \(\Lambda\), this unit does **not** assert the converse from the pointwise identity

\[
D\Lambda(x)Ax=\bar A\Lambda(x)
\]

to global semigroup intertwining.

Such a converse requires additional hypotheses ensuring that \(t\mapsto\Lambda(S(t)x)\) and the reduced evolution solve the same well-posed problem with uniqueness, plus sufficient domain/invariance regularity.

Permanent boundary:

\[
\boxed{
\text{formal infinitesimal compatibility}
\not\Rightarrow
\text{global nonlinear reduction without a well-posedness theorem}.
}
\]

---

# 9. Relation to III.1 geometric projectability

III.1 studied projectability of a differential operator on the pullback algebra generated by a scalar field:

\[
\Delta_g(\Phi\circ\Lambda)
=
(B\Phi''+C\Phi')\circ\Lambda.
\]

III.9 studies projectability of a time-evolution semigroup on state space.

These are related but typed differently:

\[
\boxed{
\text{operator-on-observables projectability}
\neq
\text{state-semigroup projectability}.
}
\]

A bridge requires a declared state/observable picture and the corresponding generator theorem. No silent identification is made.

---

# 10. PSI interpretation

For a dynamic representation \(\Lambda\), the exact autonomous-reduction criterion is

\[
\boxed{
\ker_{eq}\Lambda
\subseteq
\ker_{eq}(\Lambda\circ S(t))
\qquad\forall t\ge0.
}
\]

Thus DOM-LOGOS is a direct realization of the same kernel/factorization logic used throughout PSI.

It answers:

> when may a compressed state carry its own future dynamics without returning to the discarded degrees of freedom?

The answer is dynamic congruence of the representation fibres.

No new primitive is needed.

---

# 11. Local cross-check

### Source bind
`PASS`: the exact semigroup and generator/domain formulas are physically recovered from the 2026-07-26A consolidated source, with the 2026-07-16 strict source as genealogy.

### Set-theoretic projectability
`PASS`: existence and uniqueness of the reduced semigroup on \(\operatorname{im}\Lambda\) are equivalent to forward congruence of fibres.

### Image discipline
`PASS`: uniqueness is not inflated beyond \(\operatorname{im}\Lambda\).

### Unbounded-domain legality
`PASS`: generator formulas are restricted to \(D(A)\) and \(D(\bar A)\).

### Linear \(C_0\) theorem
`PASS`: bounded linear generator intertwining with the domain inclusion is proved equivalent to semigroup intertwining.

### Nonlinear boundary
`PASS`: only the derivative consequence is asserted; the converse is not imported without a well-posedness/uniqueness theorem.

### Relation to existing PSI
`PASS`: III.9 is a realization of dynamic quotient/projectability logic, not CORE growth.

---

# 12. Verdict

\[
\boxed{
\mathrm{III.9\ DOM\!-\!LOGOS}
=
\mathrm{THEOREM\ PROSE\ PASS\ 01 / PROOF\ PASS / LOCAL\ CROSS\!-
CHECK\ PASS}.
}
\]

The source-recovery gate is closed. The next required process step is a control synchronization and a cross-check of III.9 against Volume II.6 and the PHISICA operator chain before opening any further LOGOS/MOS realization.
