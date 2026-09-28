# PSI — CAT–FACT–NORM–MINI 02

**Status:** `CURRENT CORRECTED MINI / EXACT-NOISELESS / NORMAL-FORM IDENTIFIABILITY`  
**Supersedes mathematically:** `cat-fact-norm-mini-01.md` sections claiming gauge-only factorization-fibre cardinality one  
**Scope:** `C^3` regular curves on `[0,T]`; exact observation; fixed time parameter; finite `{F,B}` grammar  
**Reason for v02:** unique normal form was previously conflated with singleton gauge-only factorization fibre.

---

## 1. Contract

Let

\[
\gamma:[0,T]\to\mathbb R^3,
\qquad \gamma\in C^3,
\qquad \|\dot\gamma(t)\|>0.
\]

Time reparameterization is not gauge.

Two exact protocols remain legal:

\[
P_0^{abs}:Y_{abs}=\gamma(t),
\qquad
G_{abs}=SO(2)_{normal},
\]

and

\[
P_0^{shape}:Y_{shape}=[\gamma]_{SE(3)},
\qquad
G_{shape}=SE(3)\times SO(2)_{normal}.
\]

The split between these protocols is unchanged from MINI-01 and remains the F55 regression.

---

## 2. Grammar and rewrite

Use the finite grammar

\[
\mathcal L_{FB}=\{F,B\}.
\]

On Frenet-valid intervals:

\[
F_I=(v,\kappa,\tau)_I
\longrightarrow
B_I=(v,k_1,k_2)_I
\]

through the usual relatively-parallel recode, with the integration constant absorbed by constant normal `SO(2)` gauge.

Adjacent Bishop atoms admit the merge

\[
B_{I_1}\oplus B_{I_2}
\longrightarrow
B_{I_1\cup I_2}
\]

after normal-frame gauge alignment.

The rewrite is formulated on legal gauge classes.

---

## 3. Termination and confluence

For a grammar term `X`, define

\[
\mu(X)=\bigl(n_F(X),n_{seg}(X)\bigr)
\]

with lexicographic order.

`F→B` decreases `n_F`; Bishop merge decreases `n_seg` without increasing `n_F`. Hence every rewrite step strictly decreases `\mu`.

The same overlap analysis as MINI-01 gives local confluence on gauge classes:

- disjoint Frenet recodes commute;
- the two merge orders for three adjacent Bishop atoms agree modulo gauge;
- disjoint recode/merge steps commute.

By Newman's lemma:

\[
\boxed{\text{the rewrite is confluent on legal gauge classes}.}
\]

Therefore every legal grammar term has one Bishop **normal class**.

---

## 4. Gauge-only factorization candidate space

For either protocol `P`, let

\[
\operatorname{RawFact}^{0}_{FB,P}(Y)
\]

be the set of legal finite `{F,B}` grammar terms compatible with the exact observation.

Define the gauge-only candidate space

\[
\boxed{
\mathfrak F^{0}_{FB,P}(Y)
:=
\operatorname{RawFact}^{0}_{FB,P}(Y)/G_P.
}
\]

This is the correct analogue of a factorization candidate fibre modulo the **declared realization/presentation gauge only**.

In general:

\[
\boxed{
|\mathfrak F^{0}_{FB,P}(Y)|\neq 1
\text{ need not hold}.}
\]

Indeed, for any interior cut `a`, the terms

\[
B_{[0,L]}
\quad\text{and}\quad
B_{[0,a]}\oplus B_{[a,L]}
\]

are distinct grammar factorizations. A constant normal rotation does not remove a segmentation boundary. Thus they need not be gauge-equivalent.

This is the fixed counterexample to the former MINI-01 singleton-fibre claim.

---

## 5. Normalization map

Confluence defines a normalization map

\[
\boxed{
\operatorname{NF}_{FB,P,Y}:
\mathfrak F^{0}_{FB,P}(Y)
\to
\mathcal N_{FB,P}(Y),
}
\]

where `\mathcal N_{FB,P}(Y)` is the set of Bishop normal classes compatible with `Y`.

For the exact interval contract:

\[
\boxed{
|\operatorname{im}\operatorname{NF}_{FB,P,Y}|=1.
}
\]

Thus every legal finite Frenet/Bishop factorization of the observed regular curve has the same normal class, although the gauge-only factorization candidate space may contain multiple elements.

---

## 6. Task quotient formulation

Define on `\mathfrak F^{0}_{FB,P}(Y)` the task equivalence

\[
X\equiv_{NF}X'
\iff
\operatorname{NF}(X)=\operatorname{NF}(X').
\]

Then

\[
\boxed{
\left|
\mathfrak F^{0}_{FB,P}(Y)/\!\equiv_{NF}
\right|=1.
}
\]

This is the exact PSI statement licensed by the rewrite theorem.

It is a statement of **normal-form/task identifiability**, not literal uniqueness of the underlying factorization/segmentation modulo gauge.

---

## 7. Why rewrite is not gauge

The correction preserves the canonical distinction

\[
\boxed{
\text{realization equivalence}
\neq
\text{behavioural recoding}.
}
\]

`SO(2)` (and, in the shape protocol, `SE(3)`) is legal gauge.

By contrast,

\[
F\to B
\]

and

\[
B\oplus B\to B
\]

are normalization/recode operations. They may identify terms for the **normal-form task**, but they must not be silently inserted into the realization gauge relation.

This is exactly why the former cardinality-one inference was invalid.

---

## 8. Frenet singularity

If `\kappa=0` while the curve remains regular, Frenet coordinates may cease to be legal while Bishop coordinates remain legal.

Hence, in this MINI:

\[
\boxed{
\text{Frenet failure at }\kappa=0
\to
\text{recode/domain repair},
}
\]

not automatic catalog birth.

This C20 conclusion survives the erratum unchanged.

---

## 9. Boundaries

MINI-02 does not establish:

- uniqueness of raw or gauge-only factorization;
- general PSI-FACT identifiability;
- noisy/statistical stability;
- closed-loop periodic normalization;
- time-reparameterization invariance;
- a canonical Bishop representative rather than a gauge class;
- irrelevance of stabilizers/higher witnesses in other contracts;
- any new Frenet/Bishop theorem.

---

## 10. Corrected verdict

The valid exact result is

\[
\boxed{
\text{all legal finite `{F,B}` grammar factorizations}
\to
\text{one Bishop normal class}.
}
\]

Equivalently:

\[
\boxed{
|\operatorname{im}\operatorname{NF}|=1
}
\]

or

\[
\boxed{
|\mathfrak F^{0}_{FB,P}(Y)/\!\equiv_{NF}|=1.
}
\]

The former statement

\[
|\operatorname{RawFact}^{0}_{FB,P}(Y)/G_P|=1
\]

is withdrawn.
