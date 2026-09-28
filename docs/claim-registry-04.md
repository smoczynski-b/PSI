# PSI — claim registry 04

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-03.md` as current public registry  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`

This version adds `CLOSED-FRAME-01` and resolves the earlier closed-loop gate without changing CORE5.

| ID | Claim / object | Status | Role | Evidence / next gate |
|---|---|---|---|---|
| C01 | Contract-relative CORE5 `P_c=(Ω_c,Ψ_c,K_c,O_T,c,δ_c)` | PSI-NEW architecture | CORE | canonical definition |
| C02 | Compatible fibre `F_c(Y)=Ψ_c^{-1}(K_c^Y)` | PSI-NEW role / classical set operation | CORE | definition |
| C03 | Task closure `R_T,c=Cl^T_{δ_c}(O_T,c)` | PSI-NEW architecture | CORE | contract must specify admitted transports/operations |
| C04 | Exact kernel `ker_eq R={(x,y):R(x)=R(y)}` | CLASSICAL | ADAPTED | elementary definition |
| C05 | Task equivalence and quotient `E_T,c`, `M_T,c=Ω_c/E_T,c` | PSI-NEW architecture / classical quotient machinery | CORE | definition + classical equivalence facts |
| C06 | Exact task-level decidability | CLASSICAL quotient fact | ADAPTED / central criterion | elementary proof |
| C07 | Kernel factorization criterion | CLASSICAL | ADAPTED | elementary proof |
| C08 | Global task sufficiency `E_Ψ⊆E_T iff q_T=f∘Ψ` | BRIDGE | CORE | specialization of C07 |
| C09 | Representation adequacy `ker_eq ρ⊆E_T` | BRIDGE | CORE / ADAPTED | factorization interpretation |
| C10 | Deterministic quotient dynamics iff `xEy => δ(x)Eδ(y)` | CLASSICAL | BENCHMARK / ADAPTED | elementary quotient proof |
| C11 | Catalog → fibre → local → global → protocol | POLICY | CORE discipline | methodological rule |
| C12 | New primitive only when semantic role changes | POLICY | architecture governance | R4 gate |
| C13 | Markov lumpability bridge | CLASSICAL condition + PSI BRIDGE | BENCHMARK | requires equal transition mass to every quotient block |
| C14 | Finite partition refinement / Paige–Tarjan | CLASSICAL algorithmic lineage | BENCHMARK | reuse/compare under matching finite hypotheses |
| C15 | Historical `T/R/E/χ`, `χ_multi`, `Δψ` | POLICY classification | GENEALOGICAL / LAB | protocol observables, not CORE primitives |
| C16 | STPψ/GTPψ, TAO/SMOK, universal semantic-field core | SUPERSEDED | GENEALOGICAL | genealogy / typed realizations only |
| C17 | SOP-11b resonance claims | OPEN / POLICY | LAB / BENCHMARK | strong thresholds require calibration/proof |
| C18 | Nerode equivalence as future-test PSI realization | CLASSICAL theorem + exact PSI realization under stated contract | BENCHMARK / ADAPTED | future-test construction |
| C19 | `CAT–FACT–NORM–MINI-01` exact interval Frenet/Bishop normal class | BRIDGE / MINI | LAB / BENCHMARK | termination + confluence modulo gauge + exact reconstruction |
| C20 | In MINI-01, Frenet failure at `κ=0` while regular is recode/domain repair, not `birth` | BRIDGE | CAT/FRAME BENCHMARK | legal Bishop recode preserves external behaviour |
| C21 | Closed-loop extension requires explicit holonomy/periodicity treatment | RESOLVED / SUPERSEDED BY C22-C23 | BENCHMARK / PRESSURE TEST | `CLOSED-FRAME-01` |
| C22 | For a closed curve, Bishop/RMF return holonomy `H_γ∈SO(2)` is a global transport datum; periodic RMF iff `H_γ=I`; on the Frenet-valid periodic-binormal domain `H_γ=R_{-∫τds}` up to sign convention | CLASSICAL geometry + PSI BRIDGE | FRAME / BENCHMARK | Bishop/RMF theory; Brander–Gravesen periodicity criterion |
| C23 | CLOSED-FRAME pressure result: loop holonomy is representable inside candidate/transport/task/compatibility roles and does not require a sixth CORE primitive | BRIDGE / PRESSURE RESULT | CORE BENCHMARK | explicit CORE5 reduction table; no task-relevant loss witness |
| C24 | Constant initial normal-frame gauge cannot remove nontrivial `SO(2)` holonomy; periodic gauge changes preserve the holonomy conjugacy class | CLASSICAL / ADAPTED | FRAME BENCHMARK | return-map/gauge calculation |

## C19 — CAT–FACT–NORM–MINI

For an exactly observed regular `C^3` curve on an interval with fixed time parameter, the finite Frenet/Bishop grammar reduces to one Bishop normal class under the declared recode/gluing rules.

The reduced datum is

\[
N_{FB}(\gamma)=\bigl(v(t),[k_1(s),k_2(s)]_{SO(2)}\bigr).
\]

Define raw compatible realizations `RawFact` first and only then quotient by the declared realization gauge to obtain `Fact`; do not quotient the same gauge twice.

---

## C22 — CLOSED-FRAME holonomy

For a regular oriented closed curve, choose an initial oriented normal pair and transport it relatively parallel once around the loop. The returned pair differs by

\[
H_\gamma\in SO(2).
\]

Changing the initial normal pair by a constant rotation conjugates the return map. Since `SO(2)` is abelian, `H_γ` is independent of that initial-basis choice.

A periodic rotation-minimizing/Bishop frame exists iff

\[
\boxed{H_\gamma=I.}
\]

On the positive-curvature domain where the Frenet frame/binormal is periodic,

\[
\boxed{
H_\gamma=R_{-\Theta_\gamma},
\qquad
\Theta_\gamma=\int_0^L\tau(s)\,ds
\pmod{2\pi},
}
\]

up to the sign convention for the normal-plane rotation. Thus periodicity is equivalent to total torsion being an integer multiple of `2π`.

This geometry is classical; PSI claims no novelty for it.

---

## C23 — CORE5 pressure verdict

When periodic framing matters, use the task observable

\[
R_H(\gamma)=H_\gamma
\]

and compatibility condition

\[
H_\gamma=I.
\]

The datum is generated by declared normal transport around the loop. Therefore it is representable through the existing roles:

\[
\text{candidate}
\to
\text{transport-derived observable}
\to
\text{task/compatibility decision}.
\]

No typed loss witness remains after this reduction, so

\[
\boxed{\mathrm{CLOSED\!-\!FRAME\!-01}\text{ does not trigger R4}.}
\]

This does not prejudge higher-fibre or Lazarus-agency pressure tests.

---

## C24 — gauge boundary

A constant normal-frame change `R_α` acts by

\[
H_\gamma\mapsto R_\alpha^{-1}H_\gamma R_\alpha=H_\gamma.
\]

A nonperiodic frame rotation on a cut interval is not a single-valued gauge transformation on the closed base `S^1`; it moves the obstruction into the endpoint mismatch rather than removing it.

Hence

\[
\boxed{\text{local frame trivialization}\neq\text{global periodic trivialization}.}
\]

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

For dual-use material add

\[
\mathrm{PUBLIC}\mid\mathrm{REVIEW}\mid\mathrm{WITHHOLD}.
\]

Future versions grow by verified claim/status change, not narrative rewrite.