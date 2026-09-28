# PSI — claim registry 06

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-05.md` as current public registry  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`

This version adds `HIGHER-FIBRE-01`, sharpens gauge legality, and leaves CORE5 unchanged.

| ID | Claim / object | Status | Role | Evidence / next gate |
|---|---|---|---|---|
| C01 | Contract-relative CORE5 `P_c=(Ω_c,Ψ_c,K_c,O_T,c,δ_c)` | PSI-NEW architecture | CORE | canonical definition |
| C02 | Compatible fibre `F_c(Y)=Ψ_c^{-1}(K_c^Y)` | PSI-NEW role / classical set operation | CORE | definition |
| C03 | Task closure `R_T,c=Cl^T_{δ_c}(O_T,c)` | PSI-NEW architecture | CORE | typed contract/transport required |
| C04 | Exact kernel `ker_eq R` | CLASSICAL | ADAPTED | elementary definition |
| C05 | Task equivalence / quotient `E_T,c`, `M_T,c` | PSI-NEW architecture / classical quotient machinery | CORE | definition |
| C06 | Exact task-level decidability | CLASSICAL quotient fact | ADAPTED / central criterion | elementary proof |
| C07 | Kernel factorization criterion | CLASSICAL | ADAPTED | elementary proof |
| C08 | Global task sufficiency | BRIDGE | CORE | specialization of C07 |
| C09 | Representation adequacy `ker_eq ρ⊆E_T` | BRIDGE | CORE / ADAPTED | factorization interpretation |
| C10 | Deterministic quotient dynamics | CLASSICAL | BENCHMARK / ADAPTED | quotient well-definedness |
| C11 | Catalog → fibre → local → global → protocol | POLICY | CORE discipline | methodological rule |
| C12 | New primitive only when semantic role changes | POLICY | architecture governance | R4 gate |
| C13 | Markov lumpability bridge | CLASSICAL condition + PSI BRIDGE | BENCHMARK | block-transition stability required |
| C14 | Finite partition refinement / Paige–Tarjan | CLASSICAL | BENCHMARK | finite algorithmic reference |
| C15 | Historical `T/R/E/χ`, `χ_multi`, `Δψ` | POLICY classification | GENEALOGICAL / LAB | not CORE primitives |
| C16 | STPψ/GTPψ, TAO/SMOK as universal core | SUPERSEDED | GENEALOGICAL | genealogy / typed realization only |
| C17 | SOP-11b strong resonance claims | OPEN / POLICY | LAB / BENCHMARK | calibration/proof required |
| C18 | Nerode as future-test PSI realization | CLASSICAL theorem + exact realization | BENCHMARK / ADAPTED | future-test construction |
| C19 | `CAT–FACT–NORM–MINI-01` interval Frenet/Bishop normal class | BRIDGE / MINI | LAB / BENCHMARK | exact interval result |
| C20 | Frenet failure at `κ=0` while regular is recode/domain repair, not `birth` | BRIDGE | CAT/FRAME BENCHMARK | MINI-01 |
| C21 | Closed-loop extension gate | RESOLVED / SUPERSEDED BY C22-C23 | BENCHMARK | CLOSED-FRAME-01 |
| C22 | Bishop/RMF closed-loop holonomy and periodicity | CLASSICAL geometry + PSI BRIDGE | FRAME / BENCHMARK | classical geometry |
| C23 | CLOSED-FRAME pressure result: no sixth primitive | BRIDGE / PRESSURE RESULT | CORE BENCHMARK | CORE5 reduction table |
| C24 | Periodic gauge cannot remove nontrivial holonomy | CLASSICAL / ADAPTED | FRAME BENCHMARK | return-map calculation |
| C25 | Same current world-state fibre does not imply same task agency | BRIDGE / PRESSURE RESULT | LAZARUS / REPRESENTATION BENCHMARK | D2 + factorization criterion |
| C26 | `ρ_F(H)=F_t(H)` can be task-insufficient | CLASSICAL factorization consequence + PSI BRIDGE | REPRESENTATION ADEQUACY | `ker ρ_F ⊄ ≡_T` witness |
| C27 | Separate world/operational marginals can lose task-relevant correlation | BRIDGE / PRESSURE RESULT | LAZARUS D3 | joint-state requirement |
| C28 | LAZARUS agency pressure does not require a new CORE primitive | BRIDGE / PRESSURE RESULT | CORE BENCHMARK | CORE5 reduction |
| C29 | `*→B Z_2←*`: strict object-set pullback has one point while weak/2-pullback has two witness objects | CLASSICAL groupoid fact + PSI BENCHMARK | HIGHER-FIBRE | explicit weak-pullback calculation |
| C30 | Coarse truncation before compatibility fibre can lose task-relevant witness data | BRIDGE / PRESSURE RESULT | REPRESENTATION BENCHMARK | C29 + factorization criterion |
| C31 | Stabilizer-sensitive tasks are not generally adequate under `π_0`/coarse-orbit representation | CLASSICAL structure + PSI BRIDGE | HIGHER-FIBRE / GAUGE | `B1` vs `B Z_2` witness |
| C32 | Gauge/coarse quotient is legal only if its quotient map is task-adequate: `ker q_G⊆E_T` | BRIDGE / CORE CLARIFICATION | CORE / GAUGE DISCIPLINE | specialization of C09 |
| C33 | HIGHER-FIBRE pressure result: richer groupoid/homotopy data may be required in the candidate representation but do not force a sixth CORE role | BRIDGE / PRESSURE RESULT | CORE BENCHMARK | explicit CORE5 reduction table |

---

## C29 — weak fibre witness

For the one-object groupoid `B Z_2` and terminal maps

\[
*\to B\mathbb Z_2\leftarrow *,
\]

the strict pullback after forgetting morphisms is a singleton. The weak/2-pullback has objects

\[
(*,*,\alpha),\qquad \alpha\in\mathbb Z_2=\{e,s\},
\]

and is equivalent here to the discrete two-element groupoid. Hence

\[
\boxed{
\left|\pi_0(*\times^h_{B\mathbb Z_2}*)\right|=2
\neq
1=
\left|*\times_{\pi_0(B\mathbb Z_2)}*\right|.
}
\]

This is classical categorical/homotopy structure; PSI claims no novelty for it.

---

## C30 — truncation-order pressure

If the task distinguishes the witness `alpha`, define

\[
R_\alpha(e)=e,
\qquad
R_\alpha(s)=s.
\]

The coarse representation

\[
\rho_{\rm coarse}:\{e,s\}\to\{*\}
\]

fails

\[
\ker\rho_{\rm coarse}\subseteq\ker R_\alpha.
\]

Therefore coarse truncation before fibre formation can be task-insufficient.

The safe operational order is:

\[
\boxed{
\text{preserve witness/higher compatibility data}
\to
\text{apply only task-legal truncation}.
}
\]

---

## C31 — stabilizer sensitivity

`B1` and `B Z_2` each have one connected component, but

\[
\operatorname{Aut}_{B1}(*)=1,
\qquad
\operatorname{Aut}_{B\mathbb Z_2}(*)\cong\mathbb Z_2.
\]

Thus `pi_0` is insufficient for any task that distinguishes isotropy/stabilizer structure.

This does not imply that stabilizers are relevant for every task.

---

## C32 — gauge legality criterion

A declared gauge reduction

\[
q_G:\Omega\to\Omega/G
\]

is task-legal only if

\[
\boxed{
\ker_{\rm eq}q_G\subseteq E_{\mathcal T}.
}
\]

Therefore `gauge quotient` must not be read as `always replace a groupoid/stack-like object by its coarse orbit set`.

If stabilizers, witness multiplicity or higher coherence are task-relevant, they must remain represented before the task quotient is formed.

C32 is a direct use of C09, not a sixth primitive.

---

## C33 — CORE5 verdict

HIGHER-FIBRE data reduce into existing roles:

- witness/stabilizer/homotopy data → structured candidate representation;
- coarse or enriched readout → observation contract;
- witness-sensitive distinction → task observable;
- witness compatibility → candidate decoration or enriched observation/compatibility;
- evolution of structured data → declared dynamics/transport;
- admissible truncation/gauge → representation adequacy check.

No task-relevant distinction remains unrepresentable after this reduction. Therefore

\[
\boxed{
\mathrm{HIGHER\!-\!FIBRE\!-01}:
\mathrm{CORE5\ SURVIVES}.}
\]

This is not a claim that all higher mathematics reduces computationally to a simple finite set representation.

---

## Promotion rule

A claim enters the stable theorem layer only after

\[
\boxed{
\text{TYPE}\land
\text{SOURCE}\land
\text{STATUS}\land
\text{PROOF/TEST}\land
\text{FALSIFIER CHECK}\land
\text{CANON COMPATIBILITY}.
}
\]

Future versions grow by verified claim/status change, not narrative rewrite.