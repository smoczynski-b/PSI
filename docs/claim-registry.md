# PSI — current claim registry

**Control role:** `claim-registry`  
**Status:** CURRENT / MATERIALIZED / PUBLIC DERIVATIVE  
**Materialized:** 2026-09-29 from claim-registry-01 through 13.  
**Authority:** [CANON-03 source bind](canon03-source-bind-01.md), subject to [Freeze Errata 01](principia-v1-v2-freeze-01-errata-01.md).

All 67 entries are present below; historical registries are provenance, not required recursive imports. Update this stable file in place. A historical status is not a fresh test result. The registry is the public C/F layer; Volume III theorem units and PHISICA PF regressions remain in their linked maps and dedicated registry.

C19-v3 replaces C19-v2. C60 qualifies C09/C32/C37; C62–C66 govern the current CAT/FACT scope. C21 is retained as resolved genealogy. No new claim is promoted by this consolidation.

## C01 — contract-relative CORE5

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **PSI-NEW architecture**; role: CORE.

**CLAIM**

\[
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
\]

The meaning of candidate, observation, compatibility, task distinction and admissible evolution is relative to the declared contract `c`.

**STATUS:** `PSI-NEW` as PSI architecture; components may be classical.  
**ROLE:** `CORE`  
**DEPENDENCIES:** typed sets/maps/relations.  
**EVIDENCE:** canonical definition, not a theorem.  
**PRINCIPIA:** `V1`.

---

## C02 — compatible fiber

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **PSI-NEW role / classical set operation**; role: CORE.

For observed data `Y`,

\[
\mathcal K_c^Y=\{b:(b,Y)\in\mathcal K_c\},
\qquad
F_c(Y)=\Psi_c^{-1}(\mathcal K_c^Y).
\]

**STATUS:** `PSI-NEW` as architectural role; inverse-image/set construction is classical.  
**ROLE:** `CORE`  
**DEPENDENCIES:** `C01`.  
**EVIDENCE:** definition.  
**PRINCIPIA:** `V1`.

Interpretive restriction:

\[
\boxed{\text{observation}\neq\text{identified hidden object}.}
\]

This is a `POLICY`/methodological consequence, not a separate mathematical theorem.

---

## C03 — task closure

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **PSI-NEW architecture**; role: CORE.

\[
\mathscr R_{\mathcal T,c}
=
\operatorname{Cl}^{\mathcal T}_{\delta_c}(\mathscr O_{\mathcal T,c})
\]

is the smallest family containing the declared task observables and closed under the task operations/transports admitted by contract `c`.

**STATUS:** `PSI-NEW` as contract-relative construction.  
**ROLE:** `CORE`  
**DEPENDENCIES:** `C01`.  
**EVIDENCE:** definition; every concrete realization must specify its admitted operations/transports.  
**PRINCIPIA:** `V1`.

Open boundary: stochastic transition kernels require their own typed realization; deterministic notation must not be silently reused.

---

## C04 — exact equivalence kernel

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL**; role: ADAPTED.

For `R:Ω→W`,

\[
\ker_{\rm eq}R=\{(x,y)\in\Omega^2:R(x)=R(y)\}.
\]

**STATUS:** `CLASSICAL`  
**ROLE:** `ADAPTED`  
**DEPENDENCIES:** equality in codomain `W`.  
**EVIDENCE:** elementary definition.  
**PRINCIPIA:** `V1/V4` provenance note.

---

## C05 — task equivalence and quotient

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **PSI-NEW architecture / classical quotient machinery**; role: CORE.

\[
E_{\mathcal T,c}
=
\bigcap_{R\in\mathscr R_{\mathcal T,c}}
\ker_{\rm eq}R,
\qquad
M_{\mathcal T,c}=\Omega_c/E_{\mathcal T,c}.
\]

**STATUS:** `PSI-NEW` as task-relative architecture; intersection/quotient constructions are classical.  
**ROLE:** `CORE`  
**DEPENDENCIES:** `C03`, `C04`.  
**EVIDENCE:** each `ker_eq R` is an equivalence relation; intersection of equivalence relations is an equivalence relation.  
**PRINCIPIA:** `V1/V2`.

---

## C06 — exact task-level decidability

**Record source:** [claim-registry-03.md](claim-registry-03.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL quotient fact**; role: ADAPTED / central criterion.

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

---

## C07 — elementary factorization criterion

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL**; role: ADAPTED.

For maps `ρ:Ω→Z`, `R:Ω→W`,

\[
\boxed{
\ker_{\rm eq}\rho\subseteq\ker_{\rm eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,
\quad R=g\circ\rho.
}
\]

**STATUS:** `CLASSICAL`  
**ROLE:** `ADAPTED`  
**DEPENDENCIES:** `C04`.  
**EVIDENCE:** elementary factorization through fibers/equivalence classes.  
**PRINCIPIA:** `V2/V4` provenance.

Measurable/topological/smooth variants require their own hypotheses and are not implied by this bare set-theoretic statement.

---

## C08 — global task sufficiency

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE**; role: CORE.

Let

\[
E_{\Psi}=\ker_{\rm eq}\Psi.
\]

Then

\[
\boxed{
E_{\Psi}\subseteq E_{\mathcal T}
\iff
\exists!\,f:\operatorname{im}\Psi\to M_{\mathcal T},
\quad q_{\mathcal T}=f\circ\Psi.
}
\]

**STATUS:** `BRIDGE` / PSI formulation of `C07` for the observation-task architecture.  
**ROLE:** `CORE`  
**DEPENDENCIES:** `C05`, `C07`.  
**EVIDENCE:** direct specialization of `C07`.  
**PRINCIPIA:** `V2`.

---

## C09 — representation adequacy

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE**; role: CORE / ADAPTED.

For a representation `ρ`, exact task adequacy is

\[
\boxed{\ker_{\rm eq}\rho\subseteq E_{\mathcal T}.}
\]

**STATUS:** `BRIDGE`  
**ROLE:** `CORE` / `ADAPTED`  
**DEPENDENCIES:** `C05`, `C07`.  
**EVIDENCE:** factorization interpretation.  
**PRINCIPIA:** `V2`.

**Scope qualification (C60):** the kernel inclusion tests exact task-information adequacy. It is necessary for a legal reduction, but does not replace observation/gauge compatibility, admissibility, domain or regularity checks.

---

## C10 — deterministic quotient dynamics

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL**; role: BENCHMARK / ADAPTED.

For deterministic `δ:Ω→Ω` and equivalence relation `E`, a unique map

\[
\bar\delta:\Omega/E\to\Omega/E,
\qquad
\bar\delta\circ q=q\circ\delta,
\]

exists iff

\[
\boxed{xEy\Rightarrow\delta(x)E\delta(y).}
\]

**STATUS:** `CLASSICAL`  
**ROLE:** `BENCHMARK` / `ADAPTED`  
**DEPENDENCIES:** quotient well-definedness.  
**EVIDENCE:** elementary proof.  
**PRINCIPIA:** `V2/V4` provenance.

Stochastic aggregation is not licensed by this condition; lumpability is the classical reference case.

---

## C11 — logical order of PSI work

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **POLICY**; role: CORE discipline.

\[
\boxed{
\text{catalog adequacy}
\to
\text{fiber}
\to
\text{local identifiability}
\to
\text{global identifiability}
\to
\text{protocol design}
}
\]

**STATUS:** `POLICY`  
**ROLE:** `CORE` working discipline  
**DEPENDENCIES:** `C01–C09`.  
**EVIDENCE:** methodological rule, not theorem.  
**PRINCIPIA:** `V1`.

---

## C12 — conservative primitive rule

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **POLICY**; role: architecture governance.

\[
\boxed{\text{new primitive only when the semantic role truly changes}.}
\]

**STATUS:** `POLICY`  
**ROLE:** architecture governance  
**DEPENDENCIES:** none.  
**EVIDENCE:** project rule.  
**PRINCIPIA:** editorial preface / `V1`.

This rule blocks automatic promotion of higher fibers, frame changes, memory, factorization spaces, operator models or domain laboratories into CORE5.

---

## C13 — lumpability refinement

**Record source:** [claim-registry-03.md](claim-registry-03.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL condition + PSI BRIDGE**; role: BENCHMARK.

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

---

## C14 — finite partition-refinement bridge

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL**; role: BENCHMARK.

**CLAIM:** finite algorithms advertised as computing a coarsest dynamically stable PSI partition must be compared with classical partition-refinement methods (e.g. Paige–Tarjan) under explicit hypotheses.

**STATUS:** `CLASSICAL`.
**ROLE:** `BENCHMARK`  
**DEPENDENCIES:** `C05`, `C10`.  
**EVIDENCE:** classical algorithmic lineage.  
**PRINCIPIA:** `V2/V3/V4` depending result.

---

## C15 — old Model ψ metrics

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **POLICY classification**; role: GENEALOGICAL / LAB.

**CLAIM:** `T/R/E/χ`, `χ_multi`, `Δψ` are historical protocol-level observables derived from selected embedding representations; they are not current PSI primitives.

**STATUS:** `POLICY` (classification of historical material)  
**ROLE:** `GENEALOGICAL` / laboratory observable  
**DEPENDENCIES:** migration registry.  
**EVIDENCE:** historical Principia implementations.  
**PRINCIPIA:** `V3/V4`.

---

## C16 — old field ontologies

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **SUPERSEDED**; role: GENEALOGICAL.

**CLAIM:** STPψ/GTPψ, TAO/SMOK and universal semantic-field formulations do not define the current PSI core. They may be retained as genealogy or independently typed realizations.

**STATUS:** `SUPERSEDED`.
**ROLE:** `GENEALOGICAL`  
**DEPENDENCIES:** `C01`, migration registry.  
**EVIDENCE:** later CANON-03 priority.  
**PRINCIPIA:** `V4`; selected realizations may enter `V3`.

---

## C17 — SOP-11b resonance claims

**Record source:** [claim-registry-01.md](claim-registry-01.md). Classification from [claim-registry-06.md](claim-registry-06.md): **OPEN / POLICY**; role: LAB / BENCHMARK.

**CLAIM:** reproducible preprocessing/provenance machinery may be retained as a laboratory protocol, while fixed-threshold or universal resonance assertions require explicit stochastic assumptions, calibration and proof before theorem status.

**STATUS:** `OPEN` / `POLICY`  
**ROLE:** laboratory / `BENCHMARK`  
**DEPENDENCIES:** migration registry.  
**EVIDENCE:** historical Universalia protocol; theorem-strength claims not imported automatically.  
**PRINCIPIA:** `V3/V4`.

---

## C18 — Nerode realization

**Record source:** [claim-registry-03.md](claim-registry-03.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL theorem + exact realization**; role: BENCHMARK / ADAPTED.

Let candidates be prefixes `u∈Σ*`, admissible transports be right concatenations by `w∈Σ*`, and let

\[
R_w(u)=1_L(uw).
\]

Then

\[
E_{\mathcal T}=\bigcap_w\ker_{\rm eq}R_w=\equiv_L.
\]

The Myhill–Nerode theorem remains classical mathematics.

---

## C19-v3 — CAT–FACT–NORM–MINI corrected normal-form theorem

**Record source:** [claim-registry-13.md](claim-registry-13.md).

Let

\[
\gamma:[0,T]\to\mathbb R^3
\]

be `C^3` and regular with fixed time parameter. Use the finite grammar `{F,B}` and constant Bishop normal-plane gauge `SO(2)`.

Two exact observation contracts remain legal:

### Absolute-coordinate contract

\[
P_0^{abs}:Y_{abs}=\gamma(t),
\qquad
G_{abs}=SO(2)_{normal}.
\]

### Shape contract

\[
P_0^{shape}:Y_{shape}=[\gamma]_{SE(3)},
\qquad
G_{shape}=SE(3)\times SO(2)_{normal}.
\]

For either correctly typed contract:

1. the rewrite `F→B` plus Bishop merge is well-defined on legal gauge classes;
2. it terminates;
3. it is locally confluent and hence confluent by Newman's lemma;
4. every legal finite Frenet/Bishop grammar factorization has the same Bishop normal class;
5. the normalization map
   \[
   \operatorname{NF}:\mathfrak F^{0}_{FB,P}(Y)\to\mathcal N_{FB,P}(Y)
   \]
   has singleton image:
   \[
   \boxed{|\operatorname{im}\operatorname{NF}|=1};
   \]
6. equivalently, the task quotient by equality of normal form has one class:
   \[
   \boxed{
   |\mathfrak F^{0}_{FB,P}(Y)/\!\equiv_{NF}|=1.
   }
   \]

Here

\[
\mathfrak F^{0}_{FB,P}(Y)
=
\operatorname{RawFact}^{0}_{FB,P}(Y)/G_P
\]

is the **gauge-only factorization candidate space**.

No singleton claim is made for this candidate space itself.

**STATUS:** `BRIDGE / EXACT MINI / PASS AFTER FREEZE ERRATA 01`  
**ROLE:** `CAT/FACT/NORM NORMAL-FORM BENCHMARK`  
**SOURCE:** `cat-fact-norm-mini-02.md`  
**FALSIFIER:** F62.

---

## C20 — Frenet singularity verdict

**Record source:** [claim-registry-03.md](claim-registry-03.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE**; role: CAT/FRAME BENCHMARK.

Within the C19 contract, if curvature reaches zero while the curve remains regular, the Frenet chart/atom ceases to be legal but the Bishop representation remains legal. Because the external curve behaviour is preserved under the recode,

\[
\boxed{F\to B\text{ is recode/domain repair, not catalog birth.}}
\]

The statement is contract-relative and must not be generalized to unrelated representation failures.

---

## C21 — closed-loop gate

**Record source:** [claim-registry-03.md](claim-registry-03.md). Classification from [claim-registry-06.md](claim-registry-06.md): **RESOLVED / SUPERSEDED BY C22-C23**; role: BENCHMARK.

The C19 proof is for an interval. For a closed parameter domain, normal-plane parallel transport may carry a nontrivial return rotation. Any periodic/global normal-form statement must therefore carry, quotient or otherwise account for the return-rotation/holonomy datum, or prove it trivial under additional hypotheses.

**Current status:** `RESOLVED / SUPERSEDED BY C22–C23`. The interval-to-loop extension requires the holonomy conditions recorded in C22; the original OPEN status is historical.

---

## C22 — CLOSED-FRAME holonomy

**Record source:** [claim-registry-04.md](claim-registry-04.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL geometry + PSI BRIDGE**; role: FRAME / BENCHMARK.

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

**Record source:** [claim-registry-04.md](claim-registry-04.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE / PRESSURE RESULT**; role: CORE BENCHMARK.

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

**Record source:** [claim-registry-04.md](claim-registry-04.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL / ADAPTED**; role: FRAME BENCHMARK.

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

## C25 — precise agency statement

**Record source:** [claim-registry-05.md](claim-registry-05.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE / PRESSURE RESULT**; role: LAZARUS / REPRESENTATION BENCHMARK.

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

**Record source:** [claim-registry-05.md](claim-registry-05.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL factorization consequence + PSI BRIDGE**; role: REPRESENTATION ADEQUACY.

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

**Record source:** [claim-registry-05.md](claim-registry-05.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE / PRESSURE RESULT**; role: LAZARUS D3.

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

**Record source:** [claim-registry-05.md](claim-registry-05.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE / PRESSURE RESULT**; role: CORE BENCHMARK.

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

## C29 — weak fibre witness

**Record source:** [claim-registry-06.md](claim-registry-06.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL groupoid fact + PSI BENCHMARK**; role: HIGHER-FIBRE.

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

**Record source:** [claim-registry-06.md](claim-registry-06.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE / PRESSURE RESULT**; role: REPRESENTATION BENCHMARK.

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

**Record source:** [claim-registry-06.md](claim-registry-06.md). Classification from [claim-registry-06.md](claim-registry-06.md): **CLASSICAL structure + PSI BRIDGE**; role: HIGHER-FIBRE / GAUGE.

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

**Record source:** [claim-registry-06.md](claim-registry-06.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE / CORE CLARIFICATION**; role: CORE / GAUGE DISCIPLINE.

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

**Scope qualification (C60):** the kernel inclusion tests exact task-information adequacy. It is necessary for a legal reduction, but does not replace observation/gauge compatibility, admissibility, domain or regularity checks.

---

## C33 — CORE5 verdict

**Record source:** [claim-registry-06.md](claim-registry-06.md). Classification from [claim-registry-06.md](claim-registry-06.md): **BRIDGE / PRESSURE RESULT**; role: CORE BENCHMARK.

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

## C34 — R4 PRESSURE COURT 01

**Record source:** [claim-registry-07.md](claim-registry-07.md).

Across the accepted pressure witnesses

\[
\mathrm{CAT/FACT},
\quad
\mathrm{CLOSED\!-\!FRAME},
\quad
\mathrm{LAZARUS\ AGENCY},
\quad
\mathrm{HIGHER\ FIBRE},
\]

no case exhibits a task-relevant distinction that survives all role-preserving reductions through

\[
\Omega,
\Psi,
\mathcal K,
\mathscr O_{\mathcal T},
\delta,
\text{contract}.
\]

Therefore

\[
\boxed{
\mathrm{R4\ PRESSURE\ COURT\ 01}
=
\mathrm{NO\ R4\ WITNESS}.
}
\]

**STATUS:** `PRESSURE RESULT / FREEZE CONFIRMATION`  
**ROLE:** `CORE GOVERNANCE / BENCHMARK`  
**EVIDENCE:** four independent pressure branches + explicit reduction table.  
**SCOPE:** current counterexample set only; not a universal completeness theorem.

---

## C35 — role-preservation / anti-tautology rule

**Record source:** [claim-registry-07.md](claim-registry-07.md).

A reduction does not count as evidence for CORE5 sufficiency merely because arbitrary data can be packed into the candidate object.

A legal reduction must preserve semantic roles:

- candidate = what may be the case / inferred realization;
- observation = accessible readout;
- compatibility = consistency relation/object between prediction and report;
- task observables = distinctions relevant to the declared task;
- dynamics/transport = admissible evolution/update;
- contract = typing and legality conditions, not a hidden answer key.

Thus

\[
\boxed{
\text{candidate stuffing}\neq\text{valid CORE reduction}.
}
\]

**STATUS:** `POLICY / CORE PRESSURE DISCIPLINE`  
**ROLE:** `ANTI-TAUTOLOGY`.

---

## C36 — primitive-growth stop

**Record source:** [claim-registry-07.md](claim-registry-07.md).

Given C34, primitive growth is frozen until a new witness satisfies the R4 admission criterion:

\[
\mathrm{FAIL}_{\Omega}
\land
\mathrm{FAIL}_{\Psi}
\land
\mathrm{FAIL}_{\mathcal K}
\land
\mathrm{FAIL}_{\mathscr O}
\land
\mathrm{FAIL}_{\delta}
\land
\mathrm{FAIL}_{c}
\land
\mathrm{LOSS}
\land
\mathrm{MINIMALITY}.
\]

**STATUS:** `POLICY / FREEZE`.

This does not block richer representations, stronger theorems, derived modules, laboratories or documentation corrections.

---

## C37 — quotient/reduction adequacy

**Record source:** [claim-registry-07.md](claim-registry-07.md).

The four pressure branches jointly strengthen the project rule:

\[
\boxed{
\text{a quotient/reduction is legal only when its map is task-adequate}.}
\]

For a reduction `q`,

\[
\ker_{\rm eq}q\subseteq E_{\mathcal T}
\]

is the exact set-level adequacy test.

This applies to:

- realization gauge;
- representation reduction;
- coarse orbit/component truncation;
- memory compression;
- other task-relative quotienting.

**STATUS:** `BRIDGE / CORE CLARIFICATION`; specialization of the existing representation-adequacy criterion, not a new theorem.

**Scope qualification (C60):** the kernel inclusion tests exact task-information adequacy. It is necessary for a legal reduction, but does not replace observation/gauge compatibility, admissibility, domain or regularity checks.

---

## C38 — exact HCube paired witness

**Record source:** [claim-registry-08.md](claim-registry-08.md).

Let

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=\begin{pmatrix}2&0&0\\0&1&1\\0&0&0\end{pmatrix}.
\]

Then

\[
\chi_A=\chi_B=\lambda(\lambda-1)(\lambda-2)
\]

and

\[
\|A\|_2=\|B\|_2=2.
\]

At `z=1/2`, however,

\[
\left\|\left(\tfrac12I-A\right)^{-1}\right\|_2=2,
\]

while

\[
\left\|\left(\tfrac12I-B\right)^{-1}\right\|_2
=2(1+\sqrt2).
\]

**STATUS:** `CLASSICAL MATRIX FACT / EXACT BENCHMARK`  
**ROLE:** `HCUBE / REPRESENTATION REGRESSION`.

---

## C39 — coarse spectral-summary insufficiency

**Record source:** [claim-registry-08.md](claim-registry-08.md).

For

\[
\rho_0(X)=\left(\chi_X,\|X\|_2\right)
\]

and

\[
R_{1/2}(X)=\left\|\left(\tfrac12I-X\right)^{-1}\right\|_2,
\]

C38 gives

\[
\rho_0(A)=\rho_0(B)
\]

but

\[
R_{1/2}(A)\neq R_{1/2}(B).
\]

Therefore

\[
\boxed{
\ker_{eq}\rho_0
\not\subseteq
\ker_{eq}R_{1/2}.
}
\]

Thus `rho_0` is task-insufficient for the declared resolvent-sensitive task.

**STATUS:** `BRIDGE / REPRESENTATION-ADEQUACY REGRESSION`.

---

## C40 — HCube separator status

**Record source:** [claim-registry-08.md](claim-registry-08.md).

For the same pair, the classical bridge

\[
\|e^{t\operatorname{ad}_X}\|_{HS}
=\kappa_2(e^{tX})
\]

also separates the matrices. At `t=1`:

\[
\kappa_2(e^A)=e^2\approx7.38905610,
\]

while

\[
\kappa_2(e^B)\approx8.86992603.
\]

This establishes HCube as a valid diagnostic separator for this benchmark, not as a unique/minimal representation and not as a CORE primitive.

**STATUS:** `CLASSICAL BRIDGE + LAB BENCHMARK`.

---

## C41 — P9/HCube separation retained

**Record source:** [claim-registry-08.md](claim-registry-08.md).

The project must preserve the distinction between:

\[
x\mapsto e^{tA}x
\]

and

\[
X\mapsto e^{tA}Xe^{-tA}.
\]

The exact bridge between the similarity-action norm and `kappa(e^{tA})` does not imply that pseudospectra of `ad_A` predict state transient growth.

**STATUS:** `POLICY / CLASSICAL-SCOPE DISCIPLINE`.

---

## C42 — exact memory adequacy criterion

**Record source:** [claim-registry-09.md](claim-registry-09.md).

For a history representation

\[
\rho_t:\mathcal H_t\to R_t,
\]

exact task sufficiency is

\[
\boxed{
\ker_{eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

Equivalently,

\[
\rho_t(H)=\rho_t(H')
\Rightarrow
H\equiv_{\mathcal T,t}H'.
\]

A single counterexample pair with equal representation and different future task semantics falsifies sufficiency.

**STATUS:** `BRIDGE / REPRESENTATION-ADEQUACY SPECIALIZATION`  
**ROLE:** `MEMORY / HISTORY QUOTIENT`.

---

## C43 — recovered Go representation ladder

**Record source:** [claim-registry-09.md](claim-registry-09.md).

The recovered frozen Go tests give:

### No ko

\[
\rho_0(H_t)=(B_t,\sigma_t),
\qquad
\ker\rho_0\subseteq\equiv_{\mathcal T_{\rm no\,ko}}.
\]

### Simple ko

\[
\ker\rho_0\not\subseteq\equiv_{\mathcal T_{\rm ko}},
\]

while

\[
\rho_K(H_t)=(B_t,\sigma_t,B_{t-1}),
\qquad
\ker\rho_K\subseteq\equiv_{\mathcal T_{\rm ko}}.
\]

### Positional superko

\[
\ker\rho_K\not\subseteq\equiv_{\mathcal T_{\rm PSK}},
\]

while

\[
\rho_{\rm PSK}(H_t)=(B_t,\sigma_t,V_t),
\qquad
V_t=\{B_0,\ldots,B_t\},
\]

is sufficient under the frozen positional-superko contract.

### Situational superko

\[
\ker\rho_{\rm PSK}\not\subseteq\equiv_{\mathcal T_{\rm SSK}},
\]

while

\[
\rho_{\rm SSK}(H_t)=(B_t,\sigma_t,U_t),
\qquad
U_t=\{(B_i,\sigma_i):i\le t\},
\]

is sufficient under the frozen situational-superko contract.

**STATUS:** `EXACT FINITE REGRESSION / LAB BENCHMARK`.

---

## C44 — canonical history quotient

**Record source:** [claim-registry-09.md](claim-registry-09.md).

Let

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t},
\qquad
q_{\mathcal T,t}:\mathcal H_t\to M_{\mathcal T,t}.
\]

For every exact task-sufficient representation `rho_t`, there exists a unique

\[
f_t:\operatorname{im}\rho_t\to M_{\mathcal T,t}
\]

such that

\[
\boxed{q_{\mathcal T,t}=f_t\circ\rho_t.}
\]

Therefore `M_T,t` is the **coarsest exact quotient of histories** relative to the task.

This minimality is with respect to quotient order, not dimension, bit count, storage or computational complexity.

**STATUS:** `CLASSICAL FACTORIZATION + PSI TASK-HISTORY BRIDGE`.

---

## C45 — mathematical recursive update

**Record source:** [claim-registry-09.md](claim-registry-09.md).

When the history equivalence is a congruence for the declared update, the quotient admits a well-defined partial update

\[
\boxed{
U_{\mathcal T,t}
([H_t],\varepsilon_t,y_{t+1})
=
[\delta_t(H_t,\varepsilon_t,y_{t+1})]_{\mathcal T,t+1}.
}
\]

Hence the exact task state is recursively updateable mathematically without reconstructing the full representative history.

This does **not** prove finite memory, effective computability or algorithmic efficiency.

**STATUS:** `BRIDGE / DYNAMIC QUOTIENT RESULT`.

---

## C46 — Go memory changes are task-relative representation changes

**Record source:** [claim-registry-09.md](claim-registry-09.md).

The progression

\[
(B_t,\sigma_t)
\to
(B_t,\sigma_t,B_{t-1})
\to
(B_t,\sigma_t,V_t)
\to
(B_t,\sigma_t,U_t)
\]

does not represent primitive growth.

It represents successive candidate memories `rho_t` required by different rule/task contracts.

\[
\boxed{
\text{change of required memory}\neq\text{new PSI primitive}.
}
\]

**STATUS:** `PRESSURE/REGRESSION RESULT`  
**ROLE:** `MEMORY REPRESENTATION BENCHMARK`.

---

## C47 — G1 provenance gap

**Record source:** [claim-registry-09.md](claim-registry-09.md).

The presently recovered RED-1 source freezes `G0`, `G2`, `G3`, `G4` but does not supply a separate `G1` statement.

Therefore no mathematical content is assigned to `G1` in the current public regression without recovery of its actual source.

**STATUS:** `SOURCE GAP / GOVERNANCE`.

---

## C48 — finite-difference derivative conditioning

**Record source:** [claim-registry-10.md](claim-registry-10.md).

For uniformly sampled noisy trajectory data with bounded deterministic observation error `||ε_j||≤δ`, the centered derivative stencils satisfy, at interior points,

\[
\|\widehat d_1-\gamma'\|
\le
\frac{M_3}{6}h^2+\frac{\delta}{h},
\]

\[
\|\widehat d_2-\gamma''\|
\le
\frac{M_4}{12}h^2+\frac{4\delta}{h^2},
\]

\[
\|\widehat d_3-\gamma'''\|
\le
\frac{M_5}{4}h^2+\frac{3\delta}{h^3}.
\]

**STATUS:** `CLASSICAL NUMERICAL-ANALYSIS FACT / EXACT REGRESSION`  
**ROLE:** `FS-STAT CONDITIONING`.

---

## C49 — low-curvature torsion instability

**Record source:** [claim-registry-10.md](claim-registry-10.md).

For

\[
\gamma_{\varepsilon,\omega}(s)
=
(s,\varepsilon\cos\omega s,\varepsilon\sin\omega s),
\]

\[
\kappa_{\varepsilon,\omega}
=
\frac{\varepsilon\omega^2}{1+\varepsilon^2\omega^2},
\qquad
\tau_{\varepsilon,\omega}
=
\frac{\omega}{1+\varepsilon^2\omega^2}.
\]

As `ε→0`, the curves converge in `C^3` on compact intervals to the same straight line and `κ→0`, while `τ→ω`.

Thus classical Frenet torsion has no continuous extension through the zero-curvature straight-line stratum and cannot be uniformly stably recovered over classes allowing `κ→0`.

**STATUS:** `EXACT COUNTEREXAMPLE / STABILITY BOUNDARY`.

---

## C50 — uncertainty-driven Frenet/Bishop gate

**Record source:** [claim-registry-10.md](claim-registry-10.md).

A Frenet/torsion representation is licensed only when the protocol certifies the cross-product denominator away from zero strongly enough for the task error tolerance.

If derivative errors satisfy

\[
\|\widehat d_1-\gamma'\|\le\eta_1,
\qquad
\|\widehat d_2-\gamma''\|\le\eta_2,
\]

a conservative lower bound can be formed from

\[
\widehat w=\|\widehat d_1\times\widehat d_2\|
\]

and a cross-product error radius. If the certified lower bound is inadequate for the requested torsion precision, the legal status is

\[
\boxed{\mathrm{FRENET\ UNRESOLVED}\to\mathrm{BISHOP}.}
\]

This is not evidence that true curvature is exactly zero.

**STATUS:** `POLICY / STABLE-IDENTIFIABILITY GATE`.

---

## C51 — exact/stable/confidence distinction

**Record source:** [claim-registry-10.md](claim-registry-10.md).

The project must distinguish

\[
\boxed{
\mathrm{ID}_{\rm exact}
\mid
\mathrm{ID}_{\rm stable}
\mid
\mathrm{CONF}_{1-\alpha}.
}
\]

Exact uniqueness does not imply perturbation stability, and perturbation stability does not by itself supply probabilistic confidence coverage.

**STATUS:** `CORE-ADJACENT POLICY / STATISTICAL DISCIPLINE`.

---

## C52 — confidence requires a probability contract

**Record source:** [claim-registry-10.md](claim-registry-10.md).

Under bounded deterministic noise alone, no frequentist confidence statement is licensed.

Under an explicit probabilistic model such as iid Gaussian coordinate noise, regularized derivative estimators may carry model-relative covariance/confidence statements after bias control.

**STATUS:** `CLASSICAL STATISTICAL DISCIPLINE / POLICY`.

---

## C53 — local polynomial derivative layer is imported classical machinery

**Record source:** [claim-registry-10.md](claim-registry-10.md).

Local polynomial regression provides regularized derivative estimates with classical bias/variance and asymptotic-normality theory under standard smoothness/design assumptions.

`FS-STAT-01` uses this machinery but does not claim it as new PSI mathematics.

**STATUS:** `CLASSICAL / ADAPTED`  
**ROLE:** `FS-STAT ESTIMATION LAYER`.

---

## C54 — flatness test boundary

**Record source:** [claim-registry-10.md](claim-registry-10.md).

A pointwise test `H0,t: τ(t)=0` is legal only in a certified Frenet sector after bias and variance control.

Failure of the Frenet gate is not evidence for `τ=0`.

A global interval claim

\[
H_0:\tau\equiv0
\]

requires simultaneous/global inference and remains OPEN in the current FS-STAT layer.

**STATUS:** `PARTIAL / OPEN`.

---

## C55 — quotient-level confidence remains open

**Record source:** [claim-registry-10.md](claim-registry-10.md).

A confidence set on Bishop normal classes modulo `SO(2)` is a legitimate PSI-STAT target, but coordinatewise intervals do not automatically induce valid quotient-level coverage.

Coverage on the quotient requires a separate asymptotic/bootstrap argument, especially near singular orbit strata.

**STATUS:** `OPEN / BRIDGE`.

---

## C56 — FS-STAT hardening verdict

**Record source:** [claim-registry-10.md](claim-registry-10.md).

`CAT–FACT–NORM–MINI-01` remains exact, but transport to sampled/noisy data requires additional conditioning/statistical hypotheses.

No CORE primitive or Agent control primitive is added.

**STATUS:** `HARDENING RESULT / NO CORE CHANGE`.

---

## C57 — future task tree and history equivalence

**Record source:** [claim-registry-11.md](claim-registry-11.md).

For a history space `H_t`, define

\[
\operatorname{Beh}_{\mathcal T}(H)
\]

as the rooted tree of all legal future extensions of `H`, with node labels carrying the declared task information and edge labels carrying the literal experiment/outcome pair.

Define

\[
\boxed{
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H')
}
\]

through a root-preserving isomorphism preserving node labels, edge labels and the parent-child relation.

**STATUS:** `DEFINITION / CURRENT MIGRATION OF RED-1`  
**ROLE:** `HISTORY / FUTURE-TASK SEMANTICS`.

---

## C58 — history equivalence is an equivalence relation

**Record source:** [claim-registry-11.md](claim-registry-11.md).

The relation `≡_{T,t}` from C57 is reflexive, symmetric and transitive because identity, inverse and composition preserve the required labelled rooted-tree structure.

No finite-horizon assumption is required.

\[
\boxed{\equiv_{\mathcal T,t}\text{ is an equivalence relation}.}
\]

**STATUS:** `THEOREM / RED-1 PASS`.

---

## C59 — congruence and recursive task-state update

**Record source:** [claim-registry-11.md](claim-registry-11.md).

Under the RED-1 literal-label future-tree contract, if

\[
H\equiv_{\mathcal T,t}H'
\]

and a labelled extension `(epsilon,y)` is legal from `H`, the matching root edge exists from `H'`; corresponding successor subtrees remain equivalent.

Therefore `≡_{T,t}` is a congruence for legal history extension and the partial map

\[
\boxed{
U_{\mathcal T,t}
([H],\varepsilon,y)
=
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}
}
\]

is well-defined on its legal domain.

This establishes mathematical recursive update only; it does not imply finite memory, effective computability or efficient implementation.

**STATUS:** `THEOREM / BRIDGE / RED-1 PASS`.

---

## C60 — exact task adequacy versus full contract legality

**Record source:** [claim-registry-11.md](claim-registry-11.md).

For a representation

\[
\rho:\Omega\to Z,
\]

\[
\boxed{
\ker_{eq}\rho\subseteq E_{\mathcal T}
}
\]

is the exact criterion that `rho` preserves every distinction required by the task quotient.

For a proposed reduction/gauge/truncation map `q`, this condition is therefore the exact **task-information adequacy** test.

However it is not, by itself, the complete contract-legality test. A contract can additionally require:

- correct domain/codomain;
- admissible gauge/action;
- observation compatibility or equivariance;
- hard domain constraints;
- other declared protocol conditions.

Thus

\[
\boxed{
\text{task-adequate reduction}
\neq
\text{fully contract-legal reduction}
}
\]

in general.

C09 remains valid. C32/C37 are exact task-adequacy gates and necessary components of contract legality, not an exhaustive replacement for all contract checks.

**STATUS:** `CORE CLARIFICATION / SCOPE CORRECTION`.

---

## C61 — observation-compatible gauge condition

**Record source:** [claim-registry-11.md](claim-registry-11.md).

A transformation group `G` may be quotiented inside a fixed compatible observation problem only when the observation/compatibility contract descends appropriately through that action.

In the simplest invariant case:

\[
\Psi(g\cdot x)=\Psi(x)
\qquad\forall g\in G.
\]

More generally an explicitly equivariant observation may require simultaneous action on the observation space and a correspondingly typed compatibility relation.

Therefore:

\[
\boxed{
\text{geometric symmetry}
\not\Rightarrow
\text{legal gauge of a fixed observation fibre}.
}
\]

The gauge correction first recorded in C19-v2 and retained in C19-v3 is the fixed regression witness: fixed-coordinate trajectory observation does not automatically permit an `SE(3)` quotient over the same `Y`.

**STATUS:** `CONTRACT / GAUGE DISCIPLINE`.

---

## C62 — current canonical PSI-CAT definition

**Record source:** [claim-registry-12.md](claim-registry-12.md).

`PSI-CAT` asks whether the data and protocol justify a change of the candidate catalog and, if so, which class of changes is justified.

`PSI-CAT^D` adds domain-admissibility conditions `ADM_D`.

Domain restrictions can eliminate inadmissible hypotheses but are not themselves new empirical observations.

The current physical canon freezes

\[
\boxed{\mathrm{PSI-ID}\neq\mathrm{PSI-CAT}.}
\]

`PSI-ID` concerns identifiability inside a fixed catalog; `PSI-CAT` concerns justification for changing that catalog.

**STATUS:** `CANONICAL DEFINITION / PHYSICAL CANON-03`  
**ROLE:** `DERIVED META-IDENTIFICATION MODULE, NOT CORE6`.

The older `ISO/HOR/REF/CRS` and `GEN/TEST/SELECT` calculi remain compatible derived machinery, not the minimal current definition.

---

## C63 — current canonical PSI-FACT definition

**Record source:** [claim-registry-12.md](claim-registry-12.md).

For realization domain `D`, protocol `P`, tolerance `epsilon` and data `Y`, `PSI-FACT` studies

\[
\boxed{\operatorname{Fact}^{\varepsilon}_{D,P}(Y),}
\]

the fibre of factorizations compatible with observation and protocol.

Objects must satisfy:

- `ADM_D`;
- the declared external interface;
- the declared data-compatibility criterion.

Realization gauge is quotiented **if the contract establishes it**.

The physical canon distinguishes:

\[
\boxed{
\text{realization equivalence}
\neq
\text{behavioural recoding}.
}
\]

A one-way behavioural recoding need not be an equivalence.

**STATUS:** `CANONICAL DEFINITION / PHYSICAL CANON-03`  
**ROLE:** `DERIVED FACTORIZATION IDENTIFIABILITY MODULE`.

The older factorization groupoid / homotopy-ADEQ fibre remains a derived structured extension when stabilizers or compatibility witnesses are task-relevant; it is not the universal minimal definition of current PSI-FACT.

---

## C64 — catalog adequacy is a prior gate, not one universal metric

**Record source:** [claim-registry-12.md](claim-registry-12.md).

The physical canon freezes the logical order

\[
\boxed{
\text{catalog adequacy}
\to
\text{fibre}
\to
\text{local identifiability}
\to
\text{global identifiability}
\to
\text{protocol design}.
}
\]

It does **not** make one scalar expression `D_ADEQ^cat` a universal CORE primitive.

Older constructions such as

\[
D_{ADEQ}^{cat}(Q;P,Y)
\]

remain valid contract-specific adapters when their observation map, data metric/loss, topology, tolerance and nuisance treatment are declared.

Therefore:

\[
\boxed{
\text{catalog adequacy is canonical as a required prior question,}
\quad
D_{ADEQ}^{cat}\text{ is adapter-dependent}.
}
\]

**STATUS:** `CANONICAL SCOPE CLARIFICATION`.

This resolves former `V1-GAP-01` without adding a new core definition.

---

## C65 — physical CANON-03 source bind

**Record source:** [claim-registry-12.md](claim-registry-12.md).

The current authoritative physical source is:

- repository `smoczynski-b/psi-model`;
- commit `7e64ec8ad766623ffeede3daa4bb68dee15135c1`;
- path `psi-agent/canon/PSI-R3-CONSOLIDATED-CANON-03.md`;
- version `1.0.0`;
- Git blob SHA `72d711a40c65376ee932809802622f3985ecb02a`.

It identifies itself as `CURRENT / SUPERIOR PHYSICAL CANON SOURCE` and explicitly establishes its precedence over earlier compatible typed sources.

**STATUS:** `PROVENANCE / CURRENT CANON POINTER`.

Historical missing originals remain genealogy gaps only and are not represented as recovered.

---

## C66 — older structured CAT/FACT apparatus status

**Record source:** [claim-registry-12.md](claim-registry-12.md).

The following older structures are retained only at their audited scopes:

- `ISO/HOR/REF/CRS` — derived typed CAT calculus;
- `GEN/TEST/SELECT` — derived workflow discipline;
- fixed birth/death thresholds or hysteresis — domain/update policy unless separately justified;
- factorization groupoid and homotopy/weak ADEQ fibre — derived structured extension when required by the task/contract;
- scalar `D_ADEQ^cat` — protocol-specific adapter.

None of these overrides the smaller physical CANON-03 definitions C62–C64.

**STATUS:** `DERIVED / GENEALOGY-COMPATIBLE / NOT CORE`.

---

## C67 — normal-form identifiability is weaker than literal factorization uniqueness

**Record source:** [claim-registry-13.md](claim-registry-13.md).

For a rewrite-normalization problem, distinguish:

\[
\boxed{
\text{gauge-only factorization candidate space}
\mid
\text{normalization map}
\mid
\text{task quotient by normal form}.
}
\]

A unique normal form does not imply that distinct pre-normal factorizations are gauge-equivalent.

Therefore:

\[
\boxed{
|\operatorname{im}\operatorname{NF}|=1
\not\Rightarrow
|\operatorname{RawFact}/G|=1.
}
\]

This is a permanent representation/factorization discipline and the abstract content of F62.

**STATUS:** `SCOPE CORRECTION / FACT DISCIPLINE`.

---
