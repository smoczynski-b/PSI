# PSI — claim registry 05

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-04.md` as current public registry  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`

This version adds `LAZARUS-AGENCY-01`, corrects the loose “same information / different agency” slogan, and keeps CORE5 unchanged.

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
| C26 | `ρ_F(H)=F_t(H)` is task-insufficient whenever equal fibres support different future task behaviour | CLASSICAL factorization consequence + PSI BRIDGE | REPRESENTATION ADEQUACY | `ker ρ_F ⊄ ≡_T` witness |
| C27 | Separate marginals of world state and operational composition can lose task-relevant correlation | BRIDGE / PRESSURE RESULT | LAZARUS D3 / REPRESENTATION BENCHMARK | joint-state requirement |
| C28 | LAZARUS agency pressure does not require a new CORE primitive | BRIDGE / PRESSURE RESULT | CORE BENCHMARK | candidate/task/dynamics reduction; no loss witness |

---

## C25 — precise agency statement

The historically useful slogan

\[
\text{same information}\not\Rightarrow\text{same agency}
\]

is too broad.

Let

\[
\rho_F(H)=F_t(H)
\]

map a history to the current compatible world-state fibre. Then Lazarus D2 supplies the correct pattern:

\[
\boxed{
F_t(H)=F_t(H')
\not\Rightarrow
H\equiv_{\mathcal T,t}H'.
}
\]

Equal current-state uncertainty can coexist with different legal/executable action sets or different future task trees when history/operational composition differs.

This is not equality of full task-relevant information.

---

## C26 — representation inadequacy

If

\[
F_t(H)=F_t(H')
\]

but

\[
\operatorname{Beh}_{\mathcal T}(H)
\not\cong
\operatorname{Beh}_{\mathcal T}(H'),
\]

then `(H,H')` belongs to `ker_eq ρ_F` but not to task equivalence. Therefore

\[
\boxed{
\ker_{eq}\rho_F
\not\subseteq
\equiv_{\mathcal T,t}.
}
\]

By the ordinary factorization criterion, `ρ_F` cannot be sufficient for the task quotient.

The repair is a richer representation/history state satisfying

\[
\ker_{eq}\rho
\subseteq
\equiv_{\mathcal T,t}.
\]

---

## C27 — correlation / D3

Let world state and operational composition after an experiment be jointly uncertain:

\[
(x_{t+1},\Gamma_{t+1}).
\]

Knowing only separate marginals does not in general determine the joint admissible set. Hence

\[
\boxed{
\text{world marginal} + \text{agency marginal}
\not\Rightarrow
\text{joint task state}.}
\]

If future legal actions depend on the correlation, the candidate/representation must preserve the joint structure.

This is the same general failure mode as D1/D2:

\[
\ker\rho\not\subseteq\equiv_{\mathcal T}.
\]

---

## C28 — CORE5 pressure verdict

The agency witness reduces into existing roles:

- histories / operational state → candidate choice;
- `Γ_t` → candidate/contract operational component;
- executable action set → task observable;
- execution predicate → task observable / compatibility;
- future task tree → task closure through dynamics;
- experiment-induced `(x,Γ)` update → joint dynamics;
- insufficiency of `F_t` → representation adequacy failure.

No typed task distinction remains unrepresentable. Therefore

\[
\boxed{
\mathrm{LAZARUS\!-\!AGENCY\!-\!01}:
\mathrm{CORE5\ SURVIVES}.}
\]

This is a pressure result, not a claim that every operational system should explicitly store `Γ_t`.

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