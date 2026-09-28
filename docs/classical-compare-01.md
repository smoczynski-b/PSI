# PSI — classical comparison 01

**Status:** FIRST COMPARISON MAP / NO UNIVERSAL EQUIVALENCE CLAIM  
**Depends on:** `docs/core.md`, `docs/claim-registry-01.md`  
**Purpose:** identify where PSI task-equivalence coincides with, refines, or differs from classical quotient/equivalence constructions.

The comparison rule is deliberately conservative:

\[
\boxed{\text{DEFINE}\to\text{MATCH HYPOTHESES}\to\text{COMPARE}.}
\]

Similarity of diagrams is not enough to claim equivalence.

---

## 1. PSI reference object

For a contract `c` and task `T`, PSI forms

\[
E_{\mathcal T,c}
=
\bigcap_{R\in\mathscr R_{\mathcal T,c}}\ker_{\rm eq}R.
\]

Thus

\[
xE_{\mathcal T,c}y
\iff
\forall R\in\mathscr R_{\mathcal T,c}:R(x)=R(y).
\]

The important feature is **task relativity**: changing the family of task-relevant observables or admitted transports can change the equivalence relation without changing the underlying system.

---

## 2. Deterministic quotient dynamics

For deterministic `δ:Ω→Ω`, a quotient map

\[
\bar\delta:\Omega/E\to\Omega/E
\]

is well-defined iff

\[
xEy\Rightarrow\delta(x)E\delta(y).
\]

### Comparison verdict

This is a classical congruence / quotient well-definedness condition.

**Relation to PSI:** `COINCIDENCE UNDER THE STATED DETERMINISTIC HYPOTHESES`.

PSI does not claim this condition as new. PSI-specific structure enters through how the task relation `E_T` is generated from the observation/task contract.

---

## 3. Markov-chain lumpability

Let a finite Markov chain have transition matrix `P` and let `E` partition the state space into blocks. Classical strong lumpability requires, for every two states `xEy` and every block `C`,

\[
\sum_{z\in C}P(x,z)
=
\sum_{z\in C}P(y,z).
\]

Equivalently, the distribution of the **next quotient block** depends only on the present quotient block, not on the representative chosen inside it.

### Comparison verdict

A PSI task partition `E_T` is **not automatically lumpable**.

The relations coincide operationally only after adding the stochastic stability requirement

\[
xE_{\mathcal T}y
\Rightarrow
P(x,[z]_{E_{\mathcal T}})
=
P(y,[z]_{E_{\mathcal T}})
\quad\forall [z]_{E_{\mathcal T}}.
\]

Therefore:

\[
\boxed{
E_{\mathcal T}\text{ task-equivalence}
+
\text{stochastic block stability}
\Rightarrow
\text{lumpable PSI quotient}.
}
\]

Without the block-stability condition the comparison is `INCOMPARABLE AS ROLES`: PSI answers which distinctions matter for a task; lumpability answers whether a proposed partition supports autonomous Markov dynamics.

Classical reference: J. G. Kemeny and J. L. Snell, *Finite Markov Chains*; see also the standard condition restated in later lumpability literature.

---

## 4. Probabilistic bisimulation

For a labelled probabilistic transition system, a strong probabilistic bisimulation requires related states to assign equal transition probability to every equivalence class for every relevant action/label.

Schematic condition:

\[
xEy
\Rightarrow
\tau(x,a,C)=\tau(y,a,C)
\quad
\forall a,\forall C\in\Omega/E.
\]

### Comparison verdict

When the PSI task closure contains exactly the future behavioural tests encoded by those action-conditioned block probabilities, the induced PSI equivalence can reproduce probabilistic bisimulation.

But PSI permits a smaller or different task family. Hence in general:

\[
E_{\rm bisim}
\subseteq E_{\mathcal T}
\]

may occur when the task forgets distinctions that full bisimulation preserves.

The reverse inclusion can also fail if the task observables distinguish features outside the behavioural signature used by the chosen bisimulation model.

Thus there is **no unconditional equality theorem**.

Classical reference: K. G. Larsen and A. Skou, “Bisimulation through probabilistic testing,” *Information and Computation* 94(1), 1991, DOI `10.1016/0890-5401(91)90030-6`.

---

## 5. Myhill–Nerode equivalence

For a formal language `L⊆Σ*`, Nerode equivalence is

\[
u\equiv_L v
\iff
\forall w\in\Sigma^*:
uw\in L\Longleftrightarrow vw\in L.
\]

Two histories are equivalent exactly when **no future continuation** distinguishes their acceptance behaviour.

### PSI realization

Take:
- candidates = histories/prefixes;
- admissible transports = right concatenations `w∈Σ*`;
- task observable = acceptance indicator `1_L`;
- task closure = all future-pulled acceptance tests
  \[
  R_w(u)=1_L(uw).
  \]

Then

\[
E_{\mathcal T}
=
\bigcap_{w\in\Sigma^*}\ker_{\rm eq}R_w
=
\equiv_L.
\]

### Comparison verdict

﻿
\[
\boxed{\text{Nerode equivalence is an exact PSI realization under this contract.}}
\]

The Myhill–Nerode theorem adds the classical finite-index result: `L` is regular iff this equivalence has finite index, and its classes form the states of the minimal DFA.

PSI does not claim that theorem. The useful bridge is architectural: Nerode is a canonical example of **future-test closure generating the coarsest task-sufficient quotient**.

---

## 6. Partition refinement / Paige–Tarjan

Paige–Tarjan algorithms compute relational coarsest stable partitions for specific finite relational structures.

### Comparison verdict

Partition refinement is an **algorithmic benchmark**, not a synonym for PSI task-equivalence.

A finite PSI problem may be reducible to classical refinement when:

1. the state space is finite;
2. task observations induce an initial partition;
3. admissible dynamics/transitions define the stability operator;
4. the desired `E_T` is the coarsest refinement stable under that operator.

Under those hypotheses, a PSI implementation should reuse or compare against established refinement algorithms rather than rediscovering them under new notation.

Outside them, especially for continuous spaces, higher fibres, tolerances or non-relational protocols, no direct algorithmic identity is asserted.

Classical reference: R. Paige and R. E. Tarjan, “Three Partition Refinement Algorithms,” *SIAM Journal on Computing* 16(6), 1987, DOI `10.1137/0216062`.

---

## 7. Comparison table

| Classical construction | What fixes the equivalence? | Relation to PSI | Verdict |
|---|---|---|---|
| deterministic congruence | invariance under `δ` | quotient-dynamics condition | exact coincidence under deterministic hypotheses |
| Markov lumpability | equal transition mass to quotient blocks | adds stochastic stability to a PSI partition | conditional coincidence |
| probabilistic bisimulation | action-labelled future transition behaviour | obtainable when task closure contains exactly these tests | conditional; no universal equality |
| Nerode | all future continuations + acceptance | exact future-test PSI realization | exact realization under the stated contract |
| Paige–Tarjan refinement | finite relational stability operator | algorithmic method for eligible finite PSI instances | benchmark, not identity |

---

## 8. Main structural conclusion

The recurring classical pattern is

\[
\boxed{
\text{equivalence}
=
\text{indistinguishability under a declared family of tests / futures}.
}
\]

PSI does **not** own that pattern.

The PSI-specific architectural move is to make the family itself explicit and task-relative:

\[
(c,\mathcal T,\mathscr O_{\mathcal T},\delta)
\mapsto
\mathscr R_{\mathcal T}
\mapsto
E_{\mathcal T}
\mapsto
M_{\mathcal T},
\]

and then combine it with the observation fibre `F(Y)` to ask what conclusions are licensed by the actually available observation.

That is the point at which comparison with classical equivalences should be made: not by notation, but by matching the generated test family and stability conditions.

---

## 9. Registry consequences

- `C10` remains `CLASSICAL / BENCHMARK-ADAPTED`.
- `C13` can be sharpened: lumpability coincidence is conditional on block-transition stability of `E_T`.
- add a Nerode bridge as a proved realization, not an originality claim.
- `C14` remains an algorithmic benchmark statement.
- no universal claim `PSI equivalence = bisimulation/lumpability/Nerode` is licensed.

The next comparison should be chosen only when a concrete PSI module requires it.