# PSI — claim registry 03

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-02.md` as current public registry  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`

This version adds the first full dual-operator mathematical run: `CAT–FACT–NORM–MINI-01`.

| ID | Claim / object | Status | Role | Evidence / next gate |
|---|---|---|---|---|
| C01 | Contract-relative CORE5 `P_c=(Ω_c,Ψ_c,K_c,O_T,c,δ_c)` | PSI-NEW architecture | CORE | canonical definition |
| C02 | Compatible fibre `F_c(Y)=Ψ_c^{-1}(K_c^Y)` | PSI-NEW role / classical set operation | CORE | definition |
| C03 | Task closure `R_T,c=Cl^T_{δ_c}(O_T,c)` | PSI-NEW architecture | CORE | contract must specify admitted transports/operations |
| C04 | Exact kernel `ker_eq R={(x,y):R(x)=R(y)}` | CLASSICAL | ADAPTED | elementary definition |
| C05 | Task equivalence and quotient `E_T,c`, `M_T,c=Ω_c/E_T,c` | PSI-NEW architecture / classical quotient machinery | CORE | definition + classical equivalence facts |
| C06 | Exact task-level decidability | CLASSICAL quotient fact | ADAPTED / central criterion | elementary proof; PSI content lies in `F` and `E_T` |
| C07 | Kernel factorization criterion | CLASSICAL | ADAPTED | elementary proof |
| C08 | Global task sufficiency `E_Ψ⊆E_T iff q_T=f∘Ψ` | BRIDGE | CORE | specialization of C07 |
| C09 | Representation adequacy `ker_eq ρ⊆E_T` | BRIDGE | CORE / ADAPTED | factorization interpretation |
| C10 | Deterministic quotient dynamics iff `xEy => δ(x)Eδ(y)` | CLASSICAL | BENCHMARK / ADAPTED | elementary quotient proof |
| C11 | Catalog → fibre → local → global → protocol | POLICY | CORE discipline | methodological rule |
| C12 | New primitive only when semantic role changes | POLICY | architecture governance | R4 gate |
| C13 | Markov lumpability bridge | CLASSICAL condition + PSI BRIDGE | BENCHMARK | coincidence only when task classes satisfy equal transition mass to every quotient block |
| C14 | Finite partition refinement / Paige–Tarjan | CLASSICAL algorithmic lineage | BENCHMARK | reuse/compare when finite PSI instance matches stability hypotheses |
| C15 | Historical `T/R/E/χ`, `χ_multi`, `Δψ` | POLICY classification | GENEALOGICAL / LAB | protocol observables, not CORE primitives |
| C16 | STPψ/GTPψ, TAO/SMOK, universal semantic-field core | SUPERSEDED | GENEALOGICAL | may survive only as genealogy or independently typed realization |
| C17 | SOP-11b resonance claims | OPEN / POLICY | LAB / BENCHMARK | fixed universal thresholds require stochastic assumptions/calibration/proof |
| C18 | Nerode equivalence as future-test PSI realization | CLASSICAL theorem + exact PSI realization under stated contract | BENCHMARK / ADAPTED | future-test construction |
| C19 | `CAT–FACT–NORM–MINI-01`: finite Frenet/Bishop grammar on a regular time-parametrized interval curve reduces to one Bishop factorization class modulo `SE(3)×SO(2)` | BRIDGE / MINI | LAB / BENCHMARK | termination + local confluence modulo gauge + exact reconstruction under stated hypotheses |
| C20 | In MINI-01, failure of the Frenet frame at `κ=0` while the curve remains regular is a recode/domain event, not catalog `birth` | BRIDGE | CAT/FRAME BENCHMARK | follows from legal `F→B` recode preserving external curve behaviour |
| C21 | Closed-loop extension of MINI-01 requires explicit holonomy/periodicity treatment | OPEN | BENCHMARK / PRESSURE TEST | do not extrapolate the interval theorem to `S^1` |

## C06 — exact task-level decidability

\[
\boxed{
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)^2\subseteq E_{\mathcal T,c}
}
\]

No originality claim is made for this set-theoretic equivalence.

## C13 — lumpability refinement

For a Markov kernel / matrix `P`, task equivalence supports autonomous quotient Markov dynamics only if

\[
\boxed{
xE_{\mathcal T}y
\Rightarrow
P(x,C)=P(y,C)
\quad\forall C\in\Omega/E_{\mathcal T}.
}
\]

Thus task-equivalence alone is not lumpability.

## C18 — Nerode realization

Let candidates be prefixes `u∈Σ*`, admissible transports be right concatenations by `w∈Σ*`, and let

\[
R_w(u)=1_L(uw).
\]

Then

\[
E_{\mathcal T}=\bigcap_w\ker_{\rm eq}R_w=\equiv_L.
\]

The Myhill–Nerode theorem remains classical mathematics.

## C19 — CAT–FACT–NORM–MINI

For an exactly observed `C^3` regular curve

\[
\gamma:[0,T]\to\mathbb R^3,
\qquad \|\dot\gamma(t)\|>0,
\]

with fixed time parameter, use the finite grammar

\[
\mathcal L_{FB}=\{F,B\}
\]

of legal Frenet and Bishop segments.

The rewrites are:

\[
F_I\to B_I
\]

and, after normal-plane gauge alignment,

\[
B_{I_1}\oplus B_{I_2}\to B_{I_1\cup I_2}.
\]

With

\[
\mu(X)=(n_F(X),n_{seg}(X))
\]

in lexicographic order, the system terminates. Critical pairs are joinable modulo the declared `SO(2)` normal-plane gauge, giving local confluence modulo gauge. Therefore each legal finite Frenet/Bishop segmentation reduces to one Bishop normal class.

Exact observation determines

\[
v(t)=\|\dot\gamma(t)\|
\]

and the Bishop curvature vector modulo one constant normal-plane rotation. Conversely those data reconstruct the curve modulo the initial Euclidean frame. Hence

\[
\boxed{
\left|
\operatorname{Fact}^{0}_{FB,P_0}(Y)/(SE(3)\times SO(2))
\right|=1.
}
\]

This is a PSI bridge/mini-realization built from classical differential geometry, not a novelty claim for Bishop or Frenet theory.

## C20 — Frenet singularity verdict

Within the C19 contract, if curvature reaches zero while the curve remains regular, the Frenet chart/atom ceases to be legal but the Bishop representation remains legal. Because the external curve behaviour is preserved under the recode,

\[
\boxed{F\to B\text{ is recode/domain repair, not catalog birth.}}
\]

The statement is contract-relative and must not be generalized to unrelated representation failures.

## C21 — closed-loop gate

The C19 proof is for an interval. For a closed parameter domain, normal-plane parallel transport may carry a nontrivial return rotation. Any periodic/global normal-form statement must therefore carry a holonomy/monodromy datum or prove it trivial under additional hypotheses.

Current status:

\[
\boxed{\mathrm{CLOSED\!-\!FRAME}=OPEN.}
\]

## Promotion rule

A claim enters the stable theorem layer only after

\[
\boxed{
\text{TYPE}
\land
\text{SOURCE}
\land
\text{STATUS}
\land
\text{PROOF/TEST}
\land
\text{FALSIFIER CHECK}
\land
\text{CANON COMPATIBILITY}.
}
\]

Where dual-use matters, add

\[
\mathrm{PUBLIC}\mid\mathrm{REVIEW}\mid\mathrm{WITHHOLD}.
\]

Future registry versions grow by claim and verified status change, not by narrative rewrite.