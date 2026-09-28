# PSI — claim registry 02

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-01.md` as current public registry  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`

This registry records the current public claim layer after `CLASSICAL-COMPARE-01` and the first falsifier pass.

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
| C18 | Nerode equivalence as future-test PSI realization | CLASSICAL theorem + exact PSI realization under stated contract | BENCHMARK / ADAPTED | proved by choosing histories, right-concatenation transports, and acceptance observables |

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

Thus task-equivalence alone is not lumpability. The added block-transition stability is the classical requirement.

## C18 — Nerode realization

Let candidates be prefixes `u∈Σ*`, admissible transports be right concatenations by all `w∈Σ*`, and let the task observable be language acceptance. Define

\[
R_w(u)=1_L(uw).
\]

Then

\[
E_{\mathcal T}
=\bigcap_{w\in\Sigma^*}\ker_{\rm eq}R_w
=\equiv_L.
\]

Hence Nerode equivalence is an exact realization of the PSI pattern **under this contract**. The Myhill–Nerode theorem remains classical mathematics; PSI does not claim it as new.

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