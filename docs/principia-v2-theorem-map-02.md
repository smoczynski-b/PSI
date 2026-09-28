# PRINCIPIA SEMANTICA — V2 THEOREM MAP 02

**Status:** `CURRENT / CLASSICAL-BRIDGE GLOBAL PASS / CAT-FACT-FRAME-HIGHER NEXT`  
**Date:** 2026-09-29  
**Supersedes for control:** `principia-v2-theorem-map-01.md`  
**Canonical source:** physical `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Claim source:** `claim-registry-12.md`  
**Falsifier source:** `falsifier-registry-11.md`  
**Regression source:** `regression-bank-01.md`  
**Freeze:** `principia-v1-v2-freeze-01.md`  
**Own-layer audit:** `principia-v2-own-layer-crosscheck-02.md` + `principia-v2-own-layer-crosscheck-02-errata-01.md`  
**Classical-layer audit:** `principia-v2-classical-bridges-crosscheck-01.md`

---

## 0. Reguła mapy

Każda jednostka musi rozdzielać:

`SOURCE/RESULT ID | PROOF DEPENDENCY | STRUCTURAL ANALOGY | DOWNSTREAM USE`.

Nie wolno sumować tych relacji do jednego `DEPENDS ON`, ponieważ tworzy to sztuczny blast radius i może wytworzyć pozorne samoodwołanie.

---

# A. Własny kręgosłup PSI — II.1–II.9

## II.1 — C06 Exact task-level decidability

\[
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)^2\subseteq E_{\mathcal T,c}.
\]

`PASS / classical elementary quotient fact / PSI-adapted criterion`.

## II.2 — C07 Kernel factorization

\[
\ker_{eq}\rho\subseteq\ker_{eq}R
\iff
\exists!g:\operatorname{im}\rho\to W,
\quad R=g\circ\rho.
\]

`PASS / classical elementary lemma`; F60: unikalność tylko na `im rho`.

## II.3 — C08 Global observer sufficiency

\[
\ker_{eq}\Psi_c\subseteq E_{\mathcal T,c}
\iff
q_{\mathcal T,c}=f\circ\Psi_c
\text{ on }\operatorname{im}\Psi_c.
\]

`PASS`; proof dependency II.2; global map property, nie per-record decidability.

## II.4 — C09 Representation adequacy

\[
\ker_{eq}\rho\subseteq E_{\mathcal T,c}.
\]

`PASS`; proof dependency II.2; F57: task-information adequacy != full contract legality.

## II.5 — C32/C37 Reduction/quotient task-information legality

\[
\ker_{eq}q\subseteq E_{\mathcal T,c}.
\]

`PASS`; proof dependency II.4; F55/F57 mandatory boundaries.

## II.6 — C10 Deterministic quotient dynamics

\[
xEy\Rightarrow\delta(x)E\delta(y)
\]

iff deterministic dynamics descends to \(\Omega/E\).

`PASS / classical congruence fact`; not stochastic lumpability.

## II.7 — C42 + C57/C58 Exact history-memory adequacy

\[
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)\cong\operatorname{Beh}_{\mathcal T}(H'),
\]

\[
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
\]

`PASS`; exact adequacy criterion / II.4 specialization.

## II.8 — C44 Coarsest exact history quotient

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}.
\]

For every exact memory:

\[
q_{\mathcal T,t}=f_t\circ\rho_t
\quad\text{on }\operatorname{im}\rho_t.
\]

`PASS`; coarsest in quotient order, not bit/dimension/compute minimality.

## II.9 — C45/C59 Recursive history quotient update

\[
U_{\mathcal T,t}([H],\varepsilon,y)
=
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}.
\]

**SOURCE/RESULT IDS:** C45+C59.  
**STRICT PROOF DEPENDENCY:** II.7 / C57-C58 + typed legal-extension definitions.  
**STRUCTURAL ANALOGY:** II.6.  
**NOT A PROOF PREREQUISITE:** II.8.  
**BOUNDARY:** F43.

The Six handoff audit remains mathematically valid with `principia-v2-own-layer-crosscheck-02-errata-01.md` correcting its residual C59 dependency classification.

### Own-layer verdict

\[
\boxed{
\mathrm{II.1:II.9\ OWN\ LAYER}
=\mathrm{GLOBAL\ CROSSCHECK\ PASS}.
}
\]

---

# B. Klasyczne mosty — II.10–II.12

## II.10 — C13 Strong Markov lumpability

For finite homogeneous Markov chains:

\[
\boxed{
xEy\Rightarrow P(x,C)=P(y,C)
\quad\forall C\in S/E
}
\]

iff the quotient transition law is representative-independent and the block process is Markov for every initial distribution.

`PASS / CLASSICAL THEOREM + PSI BRIDGE`.

Permanent boundary F61:

\[
\boxed{
\text{task quotient}\not\Rightarrow\text{Markov lumpability}.
}
\]

## II.11 — C18 Myhill–Nerode exact realization

For

\[
\Omega=\Sigma^*,
\qquad
R_w(u)=\mathbf1_L(uw),
\quad w\in\Sigma^*,
\]

\[
\boxed{
E_{\mathcal T,L}
=
\bigcap_w\ker_{eq}R_w
=
\equiv_L.
}
\]

`PASS / CLASSICAL THEOREM + EXACT PSI REALIZATION`.

Boundary:

\[
\boxed{
\text{arbitrary task equivalence}\neq\text{Nerode equivalence}
}
\]

without the full continuation-test contract.

## II.12 — C14 Paige–Tarjan benchmark

For finite \((S,R,\Pi_0)\), classical relational coarsest partition computes the coarsest \(R\)-stable refinement \(\Pi_*\).

PSI applicability requires PT1–PT4, in particular

\[
E_{\mathcal T,c}=E_{\Pi_*}.
\]

`PASS / CLASSICAL ALGORITHM + PSI BENCHMARK`.

Complexity scope:

- standard literature refinement bound: \(O(m\log n)\);
- space: \(O(n+m)\);
- Principia explicit full-input accounting: linear initialization + refinement, conservatively \(O(n+m\log n)\).

Boundary:

\[
\boxed{
\text{finite PSI instance}\not\Rightarrow\text{Paige–Tarjan applicability}
}
\]

without a reduction proof.

### Classical-layer verdict

From `principia-v2-classical-bridges-crosscheck-01.md`:

\[
\boxed{
\mathrm{II.10:II.12\ CLASSICAL\ BRIDGES}
=\mathrm{GLOBAL\ CROSSCHECK\ PASS}.
}
\]

No automatic chain `Nerode -> Paige–Tarjan -> lumpability` is licensed; the three bridges have distinct types.

---

# C. Next derived layers

## CAT / FACT / NORM

Current definitions: C62/C63; corrected MINI: C19-v2/C20; older structured apparatus only under C66.

**STATUS:** `NEXT`.

## FRAME / transport

C22–C24 closed-frame holonomy; return holonomy primary, total torsion only on stronger Frenet-valid domain.

**STATUS:** `QUEUED`.

## Structured / higher compatibility

C29–C33; preserve witness/stabilizer data only when task-relevant; no universal homotopy-fibre claim.

**STATUS:** `QUEUED`.

---

# D. Current execution order

\[
\boxed{
\mathrm{V1\ NORMALIZED\ PASS}
\to
\mathrm{II.1:II.9\ GLOBAL\ PASS}
\to
\mathrm{II.10:II.12\ CLASSICAL\ GLOBAL\ PASS}
\to
\mathrm{CAT/FACT/NORM}
\to
\mathrm{FRAME}
\to
\mathrm{HIGHER\ COMPATIBILITY}
\to
\mathrm{V2\ WHOLE\ CROSSCHECK}.
}
\]

No new primitive or Agent version is licensed.
