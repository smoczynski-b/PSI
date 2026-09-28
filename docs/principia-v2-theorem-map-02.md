# PRINCIPIA SEMANTICA — V2 THEOREM MAP 02

**Status:** `CURRENT / CLASSICAL-BRIDGE LAYER IN PROGRESS`  
**Date:** 2026-09-29  
**Supersedes for control:** `principia-v2-theorem-map-01.md`  
**Canonical source:** physical `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Claim source:** `claim-registry-12.md`  
**Falsifier source:** `falsifier-registry-11.md`  
**Regression source:** `regression-bank-01.md`  
**Freeze:** `principia-v1-v2-freeze-01.md`  
**Early spine audit:** `principia-v2-spine-crosscheck-01.md` (`II.1–II.4`)  
**Whole-own-layer audit:** `principia-v2-own-layer-crosscheck-02.md` (`II.1–II.9`)  
**Handoff errata:** `principia-v2-own-layer-crosscheck-02-errata-01.md`

---

## 0. Zasada mapy

Mapa v01 pozostaje dokumentem genealogicznym. Mapa v02 odzwierciedla stan po związaniu fizycznego CANON-03, Claim Registry v12, migracji RED-1/CAT/FACT, V1 Normalized Pass, niezależnym handoff-cross-checku II.1–II.9, jego erracie grafu zależności oraz bieżącej klasycznej warstwie mostów.

Każda jednostka V2 ma mieć:

`TYPE | HYPOTHESES | STATEMENT | PROOF/SOURCE | SCOPE | FALSIFIER/REGRESSION | STATUS`.

Obowiązuje rozdział:

`PROOF DEPENDENCY | SOURCE/RESULT ID | STRUCTURAL ANALOGY | DOWNSTREAM USE`.

Nie wolno wpisywać tych relacji zbiorczo jako `DEPENDS ON`, ponieważ sztucznie zwiększa to blast radius i może tworzyć pozorne samoodwołanie.

---

## 1. Kręgosłup elementarny — wykonany

### II.1 — C06 Exact task-level decidability

\[
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)^2\subseteq E_{\mathcal T,c}.
\]

**STATUS:** `PASS`  
**CLASS:** classical elementary quotient fact / PSI-adapted central criterion.  
**BOUNDARY:** empty fibre gives cardinality 0.

### II.2 — C07 Kernel factorization

\[
\ker_{eq}\rho\subseteq\ker_{eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,
\quad R=g\circ\rho.
\]

**STATUS:** `PASS`  
**CLASS:** classical elementary factorization lemma / PSI-adapted tool.  
**FALSIFIER:** F60 — uniqueness only on `im rho`.

### II.3 — C08 Global observer sufficiency

\[
\ker_{eq}\Psi_c\subseteq E_{\mathcal T,c}
\iff
\exists!\,f:\operatorname{im}\Psi_c\to M_{\mathcal T,c},
\quad q_{\mathcal T,c}=f\circ\Psi_c.
\]

**STATUS:** `PASS`  
**CLASS:** PSI structural bridge / direct factorization corollary.  
**PROOF DEPENDENCY:** II.2.  
**BOUNDARY:** global map property, not per-record decidability; not statistical sufficiency.

### II.4 — C09 Representation adequacy

\[
\ker_{eq}\rho\subseteq E_{\mathcal T,c}
\iff
\exists!\,g:\operatorname{im}\rho\to M_{\mathcal T,c},
\quad q_{\mathcal T,c}=g\circ\rho.
\]

**STATUS:** `PASS`  
**CLASS:** PSI central structural bridge.  
**PROOF DEPENDENCY:** II.2.  
**BOUNDARY:** F57 — task-information adequacy is not full contract legality.  
**REGRESSION:** R01/R02 direct; R03 scope boundary.

### Spine verdict

\[
\boxed{\mathrm{V2.1:V2.4}=\mathrm{PASS}.}
\]

---

## 2. Wniosek redukcyjny — wykonany

### II.5 — C32/C37 Task-information legality of reduction / quotient

For proposed reduction

\[
q:\Omega_c\to Z,
\]

exact preservation of task information is equivalent to

\[
\boxed{\ker_{eq}q\subseteq E_{\mathcal T,c}.}
\]

Equivalently the task quotient factors uniquely through `q` on `im q`.

**STATUS:** `PASS`.  
**PROOF DEPENDENCY:** II.4.  
**MANDATORY BOUNDARIES:** F57 and F55.  
**REGRESSION:** HIGHER-FIBRE and R02 direct; corrected MINI gauge-observation case as scope warning.

---

## 3. Dynamic / history quotient layer — wykonany i globalnie sprawdzony

### II.6 — C10 Deterministic quotient dynamics

For

\[
\delta:\Omega\to\Omega,
\]

equivalence `E` and quotient map `q_E`, a unique

\[
\bar\delta:\Omega/E\to\Omega/E,
\qquad
\bar\delta\circ q_E=q_E\circ\delta
\]

exists iff

\[
\boxed{xEy\Rightarrow\delta(x)E\delta(y).}
\]

**STATUS:** `PASS`.  
**CLASS:** classical congruence criterion / PSI-adapted dynamic quotient.  
**BOUNDARIES:** static task adequacy does not imply dynamic descent; deterministic theorem is not stochastic lumpability.  
**PSI NOTE:** if `R∈R_T,c => R∘delta_c∈R_T,c` for all task quantities, then `E_T,c` is automatically a congruence for `delta_c`.

### II.7 — C42 + C57/C58 Exact history-memory adequacy

Future-task equivalence is defined by

\[
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H'),
\]

where the rooted-tree isomorphism preserves root, node labels, edge labels and parent-child structure. C58 establishes that this is an equivalence relation.

For

\[
\rho_t:\mathcal H_t\to Z_t,
\]

exact history-memory adequacy is

\[
\boxed{\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.}
\]

Equivalently the history task quotient factors uniquely through `rho_t` on `im rho_t`.

**STATUS:** `PASS`.  
**CLASS:** exact adequacy criterion / II.4 specialization + factorization corollary.  
**PROOF DEPENDENCY:** II.4 + C57/C58.  
**REGRESSION:** R02 Go; LAZARUS current-fibre insufficiency witness.  
**BOUNDARY:** full history is not asserted to be bit-, state-, dimension-, storage- or computation-minimal.

### II.8 — C44 Coarsest exact history quotient

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}.
\]

Every exact memory \(\rho_t:\mathcal H_t\to Z_t\) with

\[
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}
\]

factors uniquely on its image:

\[
\boxed{
q_{\mathcal T,t}=f_t\circ\rho_t,
\qquad
f_t:\operatorname{im}\rho_t\twoheadrightarrow M_{\mathcal T,t}.
}
\]

For quotient representations `q_Q`, exactness is equivalent to `Q⊆equiv_T,t`; hence `equiv_T,t` is the maximum admissible equivalence relation and `M_T,t` the coarsest exact quotient in quotient order.

**STATUS:** `PASS`.  
**PROOF DEPENDENCY:** II.7; the factorization statement uses II.2/II.7.  
**BOUNDARIES:** quotient-order coarseness is not bit/dimension/storage/compute minimality; F60 applies to `im rho_t`, not unused codomain points.  
**REGRESSION:** R02/LAZARUS as scope witnesses only.

### II.9 — C45 + C59 Recursive quotient update

Let

\[
D_t\subseteq\mathcal H_t\times\mathcal E_t\times\mathcal Y_{t+1},
\qquad
\delta_t:D_t\to\mathcal H_{t+1}
\]

be the typed legal extension map. Literal-label-preserving future-tree equivalence from II.7 implies representative-invariant legality and successor class.

Hence the quotient-domain

\[
\overline D_t
\subseteq
M_{\mathcal T,t}\times\mathcal E_t\times\mathcal Y_{t+1}
\]

is well-defined and there is a unique

\[
\boxed{
U_{\mathcal T,t}:\overline D_t\to M_{\mathcal T,t+1}
}
\]

with

\[
\boxed{
U_{\mathcal T,t}([H],\varepsilon,y)
=
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}.
}
\]

**STATUS:** `PASS`.  
**SOURCE / RESULT IDS:** C45 + C59.  
**STRICT PROOF DEPENDENCY:** II.7, specifically C57/C58 plus the typed legal-extension definitions.  
**STRUCTURAL ANALOGY:** II.6 (general deterministic quotient descent).  
**NOT A PROOF PREREQUISITE:** II.8 (coarsest/minimal quotient result).  
**BOUNDARIES:** domain invariance and successor-class invariance are both required; mathematical recurrence does not imply finite memory, computability, representative-free algorithmics or efficiency.  
**REGRESSION:** R02 / F43.  
**AUDIT NOTE:** `principia-v2-own-layer-crosscheck-02-errata-01.md` corrects the Six handoff dependency classification.

### Own-layer verdict

After `principia-v2-own-layer-crosscheck-02.md` plus Errata 01:

\[
\boxed{
\mathrm{II.1:II.9\ OWN\ LAYER}
=\mathrm{GLOBAL\ CROSSCHECK\ PASS}.
}
\]

No Freeze 01 erratum was required.

---

## 4. Classical bridge layer — in progress

### II.10 — C13 Strong Markov lumpability

For a finite homogeneous Markov chain `(S,P)` and equivalence `E`, the Kemeny–Snell block-stability condition

\[
\boxed{
xEy\Rightarrow P(x,C)=P(y,C)\quad\forall C\in S/E
}
\]

is equivalent to a representative-independent quotient transition matrix and strong lumpability for every initial distribution.

**STATUS:** `PASS / CLASSICAL THEOREM + PSI BRIDGE`.  
**SOURCE:** Kemeny–Snell, *Finite Markov Chains*, Ch. VI §6.3, Thm. 6.3.2.  
**PSI BRIDGE:** task equivalence identifies allowed forgetting; lumpability tests stochastic dynamic autonomy after forgetting.  
**FALSIFIER:** F61.  
**UNIT:** `principia-v2-10-strong-lumpability-bridge.md`.

### II.11 — C18 Myhill–Nerode exact future-test realization

For `L⊆Σ*`, candidates `Σ*`, right-continuation transports `T_w(u)=uw` and acceptance tests

\[
R_w(u)=\mathbf 1_L(uw),
\]

with all `w∈Σ*`,

\[
\boxed{
E_{\mathcal T,L}
=
\bigcap_{w\in\Sigma^*}\ker_{eq}R_w
=
\equiv_L.
}
\]

**STATUS:** `PASS / CLASSICAL THEOREM + EXACT PSI REALIZATION`.  
**SOURCE:** Myhill (1957), Nerode (1958).  
**CLASSICAL BOUNDARY:** finite index iff regular language; index equals state count of minimal DFA.  
**PSI BOUNDARY:** arbitrary task equivalence is not Nerode equivalence without the full continuation-test contract.  
**UNIT:** `principia-v2-11-myhill-nerode-bridge.md`.

### II.12 — Paige–Tarjan — C14

Classical finite partition-refinement algorithmic benchmark only, not PSI theorem.

**STATUS:** `NEXT`.

### Probabilistic bisimulation

Remains explanatory comparison without C-ID because no frozen theorem depends on it.

**STATUS:** `COMPARISON-ONLY / NO CURRENT C-ID REQUIRED`.

---

## 5. CAT / FACT / FRAME / higher structure

Current canonical definitions are C62/C63. Older richer groupoid/homotopy structures are derived extensions under C66.

- CAT/FACT MINI C19-v2 remains a scoped theorem/benchmark after gauge-observation repair;
- CLOSED-FRAME and HIGHER-FIBRE remain typed pressure/representation results;
- higher/groupoid information is retained only when task/contract requires it;
- no old source is automatically promoted to current canon (F58/F59).

---

## 6. Current execution order

\[
\boxed{
\mathrm{II.1:II.9\ GLOBAL\ PASS}
\to
\mathrm{II.10\ LUMPABILITY\ PASS}
\to
\mathrm{II.11\ MYHILL\!\!-\!NERODE\ PASS}
\to
\mathrm{II.12\ PAIGE\!\!-\!TARJAN\ NEXT}
\to
\mathrm{CAT/FACT/FRAME/HIGHER}
\to
\mathrm{V2\ WHOLE\ CROSSCHECK}.
}
\]

No new primitive or Agent version is licensed by this map. The classical bridges remain imported mathematics with PSI-specific typing/placement only.
