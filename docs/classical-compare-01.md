# PSI — classical comparison 01

**Status:** CURRENT COMPARISON MAP / SOURCE-BOUND / NO UNIVERSAL EQUIVALENCE CLAIM  
**Depends on:** `docs/core.md`, `docs/claim-registry-12.md`, `docs/proof-source-migration-audit-01.md`, `docs/principia-v2-own-layer-crosscheck-02.md`  
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

This is a classical congruence / quotient well-definedness condition.

**Relation to PSI:** `COINCIDENCE UNDER THE STATED DETERMINISTIC HYPOTHESES`.

PSI does not claim this condition as new. PSI-specific structure enters through how the task relation `E_T` is generated from the observation/task contract.

---

## 3. Markov-chain lumpability

Let a finite Markov chain have transition matrix `P` and let `E` partition the state space into blocks. Strong lumpability requires, for every `xEy` and every quotient block `C`,

\[
\sum_{z\in C}P(x,z)
=
\sum_{z\in C}P(y,z).
\]

Equivalently, the distribution of the next quotient block depends only on the current quotient block and not on the representative.

### Comparison verdict

A PSI task partition `E_T` is **not automatically lumpable**.

Only after adding stochastic block stability do we obtain an autonomous quotient Markov chain:

\[
\boxed{
E_{\mathcal T}
+
\text{block-transition stability}
\Rightarrow
\text{lumpable PSI quotient}.
}
\]

Without that condition the roles differ: PSI identifies which distinctions matter to the task; lumpability asks whether a partition supports autonomous stochastic dynamics.

### Classical source bind

J. G. Kemeny and J. L. Snell, *Finite Markov Chains*, Chapter VI, especially the standard lumpability criterion traditionally cited as Theorem 6.3.2 in reprint editions.

**Registry:** C13.  
**Audit status:** `PASS WITH SOURCE BIND`.

---

## 4. Probabilistic bisimulation

For a labelled probabilistic transition system, strong probabilistic bisimulation requires related states to assign equal transition probability to every equivalence class for every relevant action/label. Schematically:

\[
xEy
\Rightarrow
\tau(x,a,C)=\tau(y,a,C)
\quad
\forall a,\forall C\in\Omega/E.
\]

### Comparison verdict

When the PSI task closure contains exactly the future behavioural tests encoded by these action-conditioned block probabilities, the induced PSI equivalence can reproduce the chosen probabilistic bisimulation relation.

In general no unconditional equality is licensed: a PSI task may forget distinctions that full bisimulation preserves, or it may contain observables outside a particular bisimulation signature.

### Classical source bind

K. G. Larsen and A. Skou, “Bisimulation through probabilistic testing,” *Information and Computation* 94(1), 1991, 1–28, DOI `10.1016/0890-5401(91)90030-6`.

**Registry:** no dedicated current C-ID by deliberate Claim Registry v12 decision.  
**Audit status:** `SOURCE PASS / COMPARISON-ONLY / NO CURRENT C-ID REQUIRED`.

No frozen V1/V2 theorem depends essentially on probabilistic bisimulation. If a later theorem does, ordinary claim/source promotion must be performed at that time.

---

## 5. Myhill–Nerode equivalence

For a formal language `L⊆Σ*`, define

\[
u\equiv_L v
\iff
\forall w\in\Sigma^*:
uw\in L\Longleftrightarrow vw\in L.
\]

Take in PSI:

- candidates = histories/prefixes;
- admissible transports = right concatenations `w∈Σ*`;
- task observable = acceptance indicator `1_L`;
- task closure = all future-pulled acceptance tests
  \[
  R_w(u)=1_L(uw).
  \]

Then directly from the definitions

\[
\boxed{
E_{\mathcal T}
=
\bigcap_{w\in\Sigma^*}\ker_{\rm eq}R_w
=
\equiv_L.
}
\]

This equality is a self-contained PSI realization proof.

The additional finite-index/minimal-automaton result is classical and is not claimed by PSI.

### Classical source bind

- J. Myhill, *Finite Automata and the Representation of Events*, WADC Technical Report 57-624, 1957;
- A. Nerode, “Linear Automaton Transformations,” *Proceedings of the American Mathematical Society* 9 (1958), 541–544, DOI `10.1090/S0002-9939-1958-0135681-9`.

**Registry:** C18.  
**Audit status:** `PASS WITH SOURCE BIND`.

---

## 6. Partition refinement / Paige–Tarjan

Paige–Tarjan algorithms compute coarsest stable partitions for specific finite relational structures.

### Comparison verdict

Partition refinement is an **algorithmic benchmark**, not a synonym for PSI task-equivalence.

A finite PSI instance may be reduced to established refinement algorithms when:

1. the state space is finite;
2. task observations induce an initial partition;
3. admissible transitions define the stability operator;
4. the desired quotient is the coarsest refinement stable under that operator.

Outside those hypotheses no direct algorithmic identity is asserted.

### Classical source bind

R. Paige and R. E. Tarjan, “Three Partition Refinement Algorithms,” *SIAM Journal on Computing* 16(6), 1987, 973–989, DOI `10.1137/0216062`.

**Registry:** C14.  
**Audit status:** `PASS / BENCHMARK`.

---

## 7. Rewrite confluence / Newman

For the finite Frenet/Bishop MINI rewrite, the imported classical theorem is Newman's lemma:

> termination plus local confluence implies confluence.

PSI does not claim this theorem. MINI must first establish that its rewrite is well-defined on the relevant gauge classes and that all critical overlaps are locally joinable.

### Classical source bind

M. H. A. Newman, “On theories with a combinatorial definition of equivalence,” *Annals of Mathematics* 43 (1942), 223–243.

**Registry:** C19-v2 uses it only after quotient-rewrite well-definedness and local-confluence checks.  
**Audit status:** `PASS WITH FORMALIZATION CORRECTION`.

---

## 8. Bishop / RMF geometry

The Bishop frame itself and the closed-loop rotation-minimizing-frame geometry are classical.

### Source bind

- R. L. Bishop, “There Is More than One Way to Frame a Curve,” *American Mathematical Monthly* 82(3), 1975, 246–251, DOI `10.1080/00029890.1975.11993807`;
- D. Brander and J. Gravesen, “Monge surfaces and planar geodesic foliations,” *Journal of Geometry* 109 (2018);
- R. T. Farouki, S. H. Kim and H. P. Moon, “Construction of periodic adapted orthonormal frames on closed space curves,” *Computer Aided Geometric Design* 76 (2020), 101802, DOI `10.1016/j.cagd.2019.101802`.

### Comparison verdict

Use the global return holonomy as the primary datum. Total torsion is a coordinate for that datum only on the stronger Frenet-valid subdomain where the relevant periodic Frenet data exist.

**Registry:** C22/C24.  
**Audit status:** `PASS WITH SOURCE BIND`.

---

## 9. Weak/2-pullback terminology

The HIGHER-FIBRE witness uses the standard iso-comma / weak 2-pullback construction for groupoids: an object of the pullback carries a compatibility isomorphism.

For

\[
*\to B\mathbb Z_2\leftarrow *,
\]

the compatibility isomorphism is one of the two elements of `Z_2`, while the coarse component pullback is a singleton.

The concrete calculation is self-contained; only the terminology and general construction are imported.

**Registry:** C29/C30.  
**Audit status:** `PASS / TERMINOLOGY SOURCE BIND REQUIRED IN FINAL BIBLIOGRAPHY`.

---

## 10. Comparison table

| Classical construction | What fixes the equivalence? | Relation to PSI | Verdict |
|---|---|---|---|
| deterministic congruence | invariance under `δ` | quotient-dynamics condition | exact coincidence under deterministic hypotheses |
| Markov lumpability | equal transition mass to quotient blocks | adds stochastic stability to a PSI partition | conditional coincidence |
| probabilistic bisimulation | action-labelled future transition behaviour | obtainable when task closure contains exactly these tests | conditional; comparison-only at current freeze |
| Nerode | all future continuations + acceptance | exact future-test PSI realization | exact realization under stated contract |
| Paige–Tarjan refinement | finite relational stability operator | algorithmic method for eligible finite PSI instances | benchmark, not identity |
| Newman | terminating locally confluent rewrite | imported theorem used after PSI-specific quotient rewrite audit | classical theorem, scoped use |
| Bishop/RMF | curve/frame transport | realization/FRAME benchmark | classical geometry + PSI task packaging |

---

## 11. Main structural conclusion

The recurring classical pattern is

\[
\boxed{
\text{equivalence}
=
\text{indistinguishability under a declared family of tests / futures}.
}
\]

PSI does **not** own that pattern.

The PSI-specific architectural move is to make the family explicit and task-relative:

\[
(c,\mathcal T,\mathscr O_{\mathcal T},\delta)
\mapsto
\mathscr R_{\mathcal T}
\mapsto
E_{\mathcal T}
\mapsto
M_{\mathcal T},
\]

and then combine it with the compatible observation fibre `F(Y)` to ask what conclusions are licensed by the actually available observation.

Comparison with classical equivalences must therefore be made by matching hypotheses and generated test families, not by diagrammatic resemblance.
