# PSI — current falsifier registry

**Control role:** `falsifier-registry`  
**Status:** CURRENT / MATERIALIZED / TEST GOVERNANCE  
**Materialized:** 2026-09-29 from falsifier-registry-01 through 12.  
**Authority:** [CANON-03 source bind](canon03-source-bind-01.md), subject to [Freeze Errata 01](principia-v1-v2-freeze-01-errata-01.md).

All 62 entries are present below; historical registries are provenance, not required recursive imports. Update this stable file in place. A historical status is not a fresh test result. The registry is the public C/F layer; Volume III theorem units and PHISICA PF regressions remain in their linked maps and dedicated registry.

F12 is narrowed to the C19-v3 normal-form contract by F62 and Freeze Errata 01. A PASS tests only the stated target, never the whole theory.

## F01 — CORE5 sufficiency

**Record source:** [falsifier-registry-04.md](falsifier-registry-04.md).

**TARGET:** current five-role architecture is sufficient unless a typed loss witness forces a new semantic role.

**FALSIFIER:** every legal encoding in candidate/observation/compatibility/task/dynamics/contract roles loses a task-relevant distinction preserved by a proposed new role.

**STATUS:** `NO ACCEPTED R4 WITNESS`.

---

## F02 — exact task-level decidability

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:**

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing\land F(Y)^2\subseteq E_{\mathcal T}.
\]

**FALSIFIER:** a correctly typed non-empty fibre for which one side holds and the other does not.

**ORACLE:** direct set/quotient calculation.

---

## F03 — factorization / global sufficiency

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** set-level factorization through `rho` under kernel inclusion.

**FALSIFIER:** maps satisfying the kernel inclusion for which no representative-independent factor map exists.

---

## F04 — task-closure specification

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** the written contract determines the closure used to construct `E_T`.

**FALSIFIER:** two materially different closure families are both legal under the same written contract and induce different task equivalences.

**VERDICT:** contract/specification failure.

---

## F05 — deterministic quotient dynamics

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** `delta` descends to `Omega/E` under dynamic stability.

**FALSIFIER:** `xEy` but `delta(x)` and `delta(y)` lie in different `E`-classes while quotient dynamics is claimed well-defined.

---

## F06 — stochastic/lumpability bridge

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** a PSI task partition supports autonomous Markov quotient dynamics under block-transition stability.

**FALSIFIER:** `xE_Ty` but `P(x,C) != P(y,C)` for some quotient block `C`.

---

## F07 — derived-structure core pressure

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** FRAME, higher fibres and factorization fibres remain derived under CORE5 unless a typed loss witness shows otherwise.

**FALSIFIER:** every legal encoding in candidate/observation/compatibility/task/dynamics/contract roles destroys a task-relevant distinction preserved by the proposed new structure.

**ORACLE:** failed reduction table + loss witness + minimality of the proposed role.

---

## F08 — model-to-model handoff invariant

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** model change preserves epistemic status unless new verification is performed.

**FALSIFIER:** inherited `OPEN/HYPOTHESIS/POLICY` silently becomes fact/theorem after handoff.

---

## F09 — CURRENT-STATE FIBRE VERSUS TASK AGENCY

**Record source:** [falsifier-registry-04.md](falsifier-registry-04.md).

**Corrected target:** any claim that equality of the current world-state fibre

\[
F_t(H)=F_t(H')
\]

is by itself sufficient to guarantee equal task-relevant agency / future action structure.

**FALSIFIER:** histories `H,H'` with

\[
F_t(H)=F_t(H')
\]

but

\[
\operatorname{Beh}_{\mathcal T}(H)
\not\cong
\operatorname{Beh}_{\mathcal T}(H')
\]

or different legal/executable action sets.

**ORACLE:** compute the task-future/action semantics under the frozen history and operational composition.

**STATUS:** `HISTORICAL LAZARUS D2 WITNESS; NORMALIZED 2026-09-28`.

**IMPORTANT CORRECTION:** do **not** label this witness “same full information, different agency”. Different histories/operational states mean the full task-relevant information can differ. The exact statement is:

\[
\boxed{\text{same current-state fibre}\not\Rightarrow\text{same task agency}.}
\]

**REGRESSION:** YES.

---

## F10 — PSI-TRAFFIC G0D semantics

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** apparatus measures aggregate outbound research clicks.

**FALSIFIER:** click event alone is reported as confirmed arrival, traversal, comprehension or contribution.

**STATUS:** regression found and corrected 2026-09-28.

---

## F11 — PSI–JEV RUN-01

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** Jev adapter conforms to the frozen synthetic separating-test oracle.

**FALSIFIER:** adapter/model output disagrees with the frozen oracle or wrapper collapses model confidence into PSI identifiability.

**SCOPE:** adapter conformance only.

---

## F12 — CAT–FACT–NORM–MINI normal-form uniqueness

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** under either typed exact interval contract of C19-v3, every legal finite Frenet/Bishop term reduces to the same Bishop normal class.

**FALSIFIER:** nontermination, a nonjoinable critical pair modulo the legal gauge, or two distinct normal classes for the same admissible observation.

**ORACLE:** termination, gauge well-definedness and confluence for the frozen grammar; compare normal classes, not pre-normal factorizations.

**SCOPE:** distinct gauge-only factorizations are allowed; segmentation alone does not refute normal-form uniqueness. F62 rejects the withdrawn stronger inference.

**REGRESSION:** YES.

**Correction basis:** C19-v3, F62, [Freeze Errata 01](principia-v1-v2-freeze-01-errata-01.md).

---

## F13 — CAT birth versus frame/recode confusion

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** in MINI-01, vanishing Frenet curvature while the curve remains regular does not require catalog `birth`.

**FALSIFIER:** a regular exact-protocol case where crossing the Frenet singularity creates a genuinely new external behavioural sector not represented by Bishop recode while preserving the interface.

**REGRESSION:** YES.

---

## F14 — CLOSED-FRAME extension gate

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** any claim that interval Bishop normalization extends to a closed loop without a return-holonomy/periodicity condition.

**PRESSURE WITNESS:** a closed curve with nontrivial Bishop/RMF return rotation.

**ORACLE:** parallel-transport an initial oriented normal pair around the loop and compute

\[
H_\gamma\in SO(2).
\]

If

\[
H_\gamma\neq I,
\]

there is no periodic RMF with that connection.

On the Frenet-valid periodic-binormal domain this is equivalent, up to sign convention, to

\[
\int\tau ds\notin2\pi\mathbb Z.
\]

**STATUS:** `WITNESS CLASS FIXED / GATE RESOLVED 2026-09-28`.

**REGRESSION:** YES.

---

## F15 — FS-STAT stability gate

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** any future claim that MINI-01 remains statistically stable under finite sampling/noise.

**FALSIFIER:** admissible perturbations under the declared error model produce unstable curvature/frame/factorization classes beyond tolerance.

**STATUS:** `OPEN`.

---

## F16 — CLOSED-FRAME R4 pressure

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** the claim that closed-loop holonomy is representable inside current CORE5 roles rather than requiring a sixth primitive.

**FALSIFIER:** a closed-frame task for which:

1. enriching the candidate with framed/connection structure fails;
2. adding `H_gamma` as a task observable fails;
3. expressing periodicity as compatibility `H_gamma=I` fails;
4. loop transport cannot generate the needed datum;
5. a task-relevant distinction is still lost;
6. the proposed new primitive role is minimal.

**ORACLE:** complete failed-reduction table against CORE5.

**CURRENT RESULT:** `NO WITNESS`; `CLOSED-FRAME-01` reduces cleanly.

**REGRESSION:** YES.

---

## F17 — holonomy versus gauge

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** nontrivial normal holonomy is not removable by the allowed constant/periodic normal-frame gauge.

**FALSIFIER:** a legal periodic gauge transformation on `S^1` that changes a nonidentity holonomy element to identity while preserving the same connection/transport problem.

**ORACLE:** gauge transformation of the return map. For constant gauge,

\[
H\mapsto R_\alpha^{-1}HR_\alpha=H
\]

because `SO(2)` is abelian. More generally periodic gauge preserves the holonomy conjugacy class.

**REGRESSION:** YES.

---

## F18 — bundle/connection confusion

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

**TARGET:** any inference `normal bundle trivial => Bishop holonomy trivial`.

**FALSIFIER:** a trivializable normal bundle equipped with the normal transport of a closed space curve having nonidentity return map.

**VERDICT:** the implication is invalid; bundle triviality and connection holonomy are different properties.

**REGRESSION:** YES.

---

## F19 — concrete closed-loop numerical fixture

**Record source:** [falsifier-registry-03.md](falsifier-registry-03.md).

Use

\[
\gamma(t)=((2+\tfrac12\cos3t)\cos2t,(2+\tfrac12\cos3t)\sin2t,\tfrac12\sin3t),
\quad t\in[0,2\pi].
\]

It is regular and has nonzero curvature everywhere. High-precision numerical quadrature gives

\[
\int\tau ds\approx0.7970800677641300.
\]

**USE:** computational regression for nontrivial return rotation.

**SCOPE:** numerical fixture only; the general existence and periodicity criterion are classical and do not depend on this numeric value.

---

## F20 — LAZARUS agency CORE5 pressure

**Record source:** [falsifier-registry-04.md](falsifier-registry-04.md).

**TARGET:** D2/D3 agency distinctions are representable through existing CORE5 roles.

**FALSIFIER:** exhibit a frozen decision task for which all of the following fail:

1. representing relevant history/operational state in the candidate object;
2. exposing legal/executable actions as task observables;
3. representing execution constraints through compatibility/task predicates;
4. propagating world + operational composition through joint dynamics;
5. preserving the required distinction with any representation `ρ` satisfying the current adequacy criterion.

Then show a minimal sixth semantic role that preserves the lost distinction.

**ORACLE:** explicit failed-reduction table + task-relevant loss witness + minimality argument.

**CURRENT RESULT:** `NO WITNESS`; `LAZARUS-AGENCY-01` reduces inside CORE5.

**REGRESSION:** YES.

---

## F21 — world fibre versus task quotient

**Record source:** [falsifier-registry-04.md](falsifier-registry-04.md).

**TARGET:** prevent the definitional identification

\[
F_t = M_{\mathcal T,t}.
\]

**FALSIFIER / REGRESSION WITNESS:** D2 supplies equal current-state fibres with different future task semantics.

**ORACLE:** compare types:

\[
F_t(H)\subseteq X_t,
\qquad
M_{\mathcal T,t}=\mathcal H_t/\equiv_{\mathcal T,t}.
\]

The objects may factor or become isomorphic in a special model, but they are not definitionally equal.

**VERDICT:** `IDENTIFICATION PROHIBITED IN GENERAL`.

---

## F22 — marginals versus joint agency state

**Record source:** [falsifier-registry-04.md](falsifier-registry-04.md).

**TARGET:** any claim that separate uncertainty sets/marginals for world state and operational composition determine the joint task state.

**FALSIFIER:** two admissible joint relations/distributions on

\[
X_t\times\operatorname{Comp}(\mathcal R_t)
\]

with the same marginals but different task-relevant correlations and different legal/future action semantics.

**ORACLE:** compute the joint admissible pairs and induced action/future tree.

**STATUS:** historical D3 pattern.

**REGRESSION:** YES.

---

## F23 — Γ typing

**Record source:** [falsifier-registry-04.md](falsifier-registry-04.md).

**TARGET:** `Γ_t` is the active composition/operational state, not a generic resource, scalar score or automatically independent primitive.

**FALSIFIER:** a later derivation silently changes the type or role of `Γ_t` without an explicit new contract.

**ORACLE:** type audit against `Comp(R_t)` and the declared execution signature.

**REGRESSION:** YES.

---

## F24 — oracle decision versus information policy

**Record source:** [falsifier-registry-04.md](falsifier-registry-04.md).

**TARGET:** preserve

\[
D^*:X_t\to\mathcal A_t
\]

versus

\[
\pi_t:\mathcal H_t\to\mathcal A_t
\]

or the equivalent information-state policy.

**FALSIFIER:** a derivation substitutes hidden-state oracle choice for a policy based only on available information.

**VERDICT:** type/epistemic failure.

**REGRESSION:** YES.

---

## F25 — coarse strict fibre versus weak fibre

**Record source:** [falsifier-registry-05.md](falsifier-registry-05.md).

**TARGET:** any claim that forgetting morphisms/stabilizers before forming compatibility fibres is harmless.

**WITNESS:**

\[
*\to B\mathbb Z_2\leftarrow *.
\]

**ORACLE:** compare

\[
*\times_{\pi_0(B\mathbb Z_2)}*=*
\]

with

\[
*\times^h_{B\mathbb Z_2}*\simeq\mathbb Z_2^{\rm disc}.
\]

**VERDICT:** the coarse-first construction loses witness multiplicity.

**REGRESSION:** YES.

---

## F26 — truncation-order regression

**Record source:** [falsifier-registry-05.md](falsifier-registry-05.md).

**TARGET:** any inference

\[
\text{truncate inputs first}\Rightarrow\text{same task fibre as higher pullback first}.
\]

**FALSIFIER:** a diagram for which

\[
\pi_0(A\times_C^hB)
\not\cong
\pi_0(A)\times_{\pi_0(C)}\pi_0(B).
\]

**FIXED WITNESS:** F25.

**REGRESSION:** YES.

---

## F27 — stabilizer erasure

**Record source:** [falsifier-registry-05.md](falsifier-registry-05.md).

**TARGET:** any claim that `pi_0` / coarse orbit data are sufficient for every task.

**WITNESS:**

\[
B1,\qquad B\mathbb Z_2
\]

have equal component sets but different automorphism groups.

**ORACLE:** choose a task observable sensitive to stabilizer/isotropy type.

**VERDICT:** coarse representation is task-insufficient for that task.

**REGRESSION:** YES.

---

## F28 — gauge quotient legality

**Record source:** [falsifier-registry-05.md](falsifier-registry-05.md).

**TARGET:** any unconditional rule `gauge first = coarse orbit set first`.

**FALSIFIER:** a declared quotient map

\[
q_G:\Omega\to\Omega/G
\]

with

\[
\ker q_G\not\subseteq E_{\mathcal T}.
\]

**ORACLE:** representation-adequacy test.

**VERDICT:** the proposed gauge reduction is illegal for that task/contract.

**REGRESSION:** YES.

---

## F29 — HIGHER-FIBRE CORE5 pressure

**Record source:** [falsifier-registry-05.md](falsifier-registry-05.md).

**TARGET:** higher/groupoid/homotopy data remain representable through current CORE5 roles when task-relevant.

**FALSIFIER:** exhibit a frozen higher-structure task for which all of the following fail:

1. structured/witness-decorated candidate representation;
2. enriched or coarse observation contract;
3. task observables on stabilizers/witnesses/coherence;
4. compatibility encoding through candidate/observation structure;
5. dynamics/transport on structured candidates;
6. task-legal gauge/truncation constrained by representation adequacy;

and then show a minimal sixth semantic role preserving the lost distinction.

**CURRENT RESULT:** `NO WITNESS`; the `B Z_2` witness is absorbed by candidate enrichment + adequacy-controlled truncation.

**REGRESSION:** YES.

---

## F30 — higher-information inflation

**Record source:** [falsifier-registry-05.md](falsifier-registry-05.md).

**TARGET:** any inference

\[
\text{higher fibre contains more information}
\Rightarrow
\text{new CORE primitive}.
\]

**FALSIFIER / CHECK:** show that the additional information can be represented as structured candidate/task data and evaluated by the existing adequacy criterion.

**VERDICT:** more information alone is insufficient evidence for a new semantic role.

---

## F31 — candidate-stuffing / anti-tautology regression

**Record source:** [falsifier-registry-06.md](falsifier-registry-06.md).

**TARGET:** any argument of the form

\[
\text{“CORE5 is sufficient because we can put the missing answer/structure into }\Omega\text{.”}
\]

**FALSIFIER / FAILURE CONDITION:** the proposed enrichment changes the semantic role of the candidate by importing:

- the observed answer itself;
- a task verdict;
- inaccessible oracle information;
- an arbitrary lookup table whose only purpose is to force factorization.

**ORACLE:** role-preservation audit against candidate / observation / compatibility / task / dynamics / contract semantics.

**VERDICT:** such stuffing does not count as a legal CORE5 reduction.

**REGRESSION:** YES.

---

## F32 — R4 reopen gate

**Record source:** [falsifier-registry-06.md](falsifier-registry-06.md).

**TARGET:** current primitive-growth freeze.

R4 may reopen only if a new typed witness shows all of:

1. failure of candidate-role representation;
2. failure of observation-role representation;
3. failure of compatibility-role representation;
4. failure of task-observable representation;
5. failure of dynamics/transport representation;
6. failure of contract/gauge enrichment;
7. unavoidable task-relevant information loss;
8. minimality of a proposed new semantic role.

Symbolically:

\[
\boxed{
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
}
\]

**CURRENT STATUS:** `NO SUCH WITNESS` after CAT/FACT, CLOSED-FRAME, LAZARUS-AGENCY and HIGHER-FIBRE.

---

## F33 — pressure-result inflation

**Record source:** [falsifier-registry-06.md](falsifier-registry-06.md).

**TARGET:** any inference

\[
\text{four current pressure tests passed}
\Rightarrow
\text{CORE5 universally complete}.
\]

**FALSIFIER / CORRECTION:** the pressure court ranges only over the current counterexample set. A future new semantic-role witness may reopen R4.

**VERDICT:** universal completeness claim prohibited.

---

## F34 — spectrum-plus-norm sufficiency

**Record source:** [falsifier-registry-07.md](falsifier-registry-07.md).

**TARGET:** any claim that

\[
\rho_0(A)=(\chi_A,\|A\|_2)
\]

is sufficient for resolvent-sensitive tasks.

**FIXED WITNESS:**

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=\begin{pmatrix}2&0&0\\0&1&1\\0&0&0\end{pmatrix}.
\]

**ORACLE:** compare

\[
R_{1/2}(X)=\left\|\left(\tfrac12I-X\right)^{-1}\right\|_2.
\]

**VERDICT:**

\[
R_{1/2}(A)=2,
\qquad
R_{1/2}(B)=2(1+\sqrt2).
\]

Hence

\[
\ker\rho_0\not\subseteq\ker R_{1/2}.
\]

**REGRESSION:** YES.

---

## F35 — HCube inflation

**Record source:** [falsifier-registry-07.md](falsifier-registry-07.md).

**TARGET:** any inference

\[
\text{HCube separates one nonnormal pair}
\Rightarrow
\text{HCube is necessary/minimal/universal or a CORE primitive}.
\]

**ORACLE:** check whether the declared task is already separated by another legal observable/representation and whether any new semantic role is actually required.

**CURRENT VERDICT:** prohibited. In the fixed pair the ordinary resolvent already separates the task exactly.

---

## F36 — P9/HCube conflation

**Record source:** [falsifier-registry-07.md](falsifier-registry-07.md).

**TARGET:** any derivation identifying state amplification

\[
x\mapsto e^{tA}x
\]

with similarity-action conditioning

\[
X\mapsto e^{tA}Xe^{-tA}.
\]

**ORACLE:** type/domain audit and comparison of the actual observables used.

**VERDICT:** bridge does not imply identity of tasks.

**REGRESSION:** YES.

---

## F37 — norm/metric substitution

**Record source:** [falsifier-registry-07.md](falsifier-registry-07.md).

**TARGET:** comparison of pseudospectral, numerical-abscissa or HCube quantities computed in inconsistent geometries.

**FALSIFIER:** the declared norm/metric changes between compared diagnostics without lawful transport.

**ORACLE:** `METRIC-ID -> P10 -> P9/HCube` discipline.

**VERDICT:** comparison invalid until geometry is aligned.

---

## F38 — generic memory sufficiency

**Record source:** [falsifier-registry-08.md](falsifier-registry-08.md).

**TARGET:** any history/memory representation

\[
\rho_t:\mathcal H_t\to R_t
\]

claimed sufficient for task `T`.

**FALSIFIER:** histories `H,H'` with

\[
\rho_t(H)=\rho_t(H')
\]

but

\[
H\not\equiv_{\mathcal T,t}H'.
\]

**ORACLE:** future task semantics / legality under the frozen contract.

**VERDICT:** one such pair completely falsifies exact sufficiency.

---

## F39 — simple-ko present-state collapse

**Record source:** [falsifier-registry-08.md](falsifier-registry-08.md).

**TARGET:**

\[
\rho_0(H_t)=(B_t,\sigma_t)
\]

as sufficient memory for simple ko.

**FIXED WITNESS STATUS:** recovered G2 contains histories with equal current situation and different legality of the same move.

**VERDICT:**

\[
\ker\rho_0\not\subseteq\equiv_{\mathcal T_{\rm ko}}.
\]

**REPAIR UNDER FROZEN CONTRACT:**

\[
\rho_K=(B_t,\sigma_t,B_{t-1}).
\]

---

## F40 — positional-superko short-memory collapse

**Record source:** [falsifier-registry-08.md](falsifier-registry-08.md).

**TARGET:** simple-ko memory `rho_K` as sufficient for positional superko.

**FROZEN VERDICT:**

\[
\ker\rho_K\not\subseteq\equiv_{\mathcal T_{\rm PSK}}.
\]

**REPAIR:** retain the visited-board set

\[
V_t=\{B_0,\ldots,B_t\}.
\]

---

## F41 — situational-superko positional-history collapse

**Record source:** [falsifier-registry-08.md](falsifier-registry-08.md).

**TARGET:**

\[
\rho_{\rm PSK}=(B_t,\sigma_t,V_t)
\]

as sufficient for situational superko.

**FROZEN VERDICT:**

\[
\ker\rho_{\rm PSK}\not\subseteq\equiv_{\mathcal T_{\rm SSK}}.
\]

**REPAIR:** retain the visited-situation set

\[
U_t=\{(B_i,\sigma_i):i\le t\}.
\]

---

## F42 — quotient-minimality inflation

**Record source:** [falsifier-registry-08.md](falsifier-registry-08.md).

**TARGET:** any inference

\[
M_{\mathcal T,t}\text{ is the coarsest exact quotient}
\Rightarrow
M_{\mathcal T,t}\text{ minimizes dimension/bits/storage/compute}.
\]

**VERDICT:** prohibited.

The proved minimality concerns the partial order of exact quotients only.

---

## F43 — recursive-update inflation

**Record source:** [falsifier-registry-08.md](falsifier-registry-08.md).

**TARGET:** any inference

\[
U_{\mathcal T,t}\text{ is mathematically well-defined}
\Rightarrow
\text{finite-memory or efficient online algorithm exists}.
\]

**VERDICT:** prohibited.

Mathematical recurrency does not establish finite memory, computability or complexity bounds.

---

## F44 — absolute memory ladder inflation

**Record source:** [falsifier-registry-08.md](falsifier-registry-08.md).

**TARGET:** treating

\[
\rho_0\to\rho_K\to\rho_{\rm PSK}\to\rho_{\rm SSK}
\]

as a universal order of increasingly correct states independent of task.

**ORACLE:** restore the frozen rule/task contract.

**VERDICT:** each representation is judged relative to its task. Extra history can be irrelevant under a weaker rule system.

---

## F45 — G1 source fabrication

**Record source:** [falsifier-registry-08.md](falsifier-registry-08.md).

**TARGET:** any attempt to assign a board witness, memory representation or theorem to `GO-PSI G1` using only the currently recovered RED-1 source.

**ORACLE:** provenance check.

**CURRENT VERDICT:** blocked; the recovered source explicitly states G0/G2/G3/G4 but no separate G1 content.

**REOPEN:** only after recovery of the actual G1 source.

---

## F46 — exact-to-stable inflation

**Record source:** [falsifier-registry-09.md](falsifier-registry-09.md).

**TARGET:** any inference

\[
\mathrm{ID}_{\rm exact}
\Rightarrow
\mathrm{ID}_{\rm stable}.
\]

**FALSIFIER:** a perturbation family for which exact parameters remain mathematically defined away from the boundary but their recovery condition number diverges.

**FIXED WITNESS:** the low-curvature helix family in `FS-STAT-01`.

**VERDICT:** exact uniqueness alone does not license finite-sample stability.

---

## F47 — low-curvature torsion stability

**Record source:** [falsifier-registry-09.md](falsifier-registry-09.md).

**TARGET:** any claim of uniform torsion stability over a class allowing `κ→0`.

**FIXED WITNESS:**

\[
\gamma_{\varepsilon,\omega}(s)
=(s,\varepsilon\cos\omega s,\varepsilon\sin\omega s).
\]

As `ε→0`, `γ_{ε,ω}` converges in `C^3` to a line while `τ_{ε,ω}→ω`.

**VERDICT:** no continuous torsion extension / no uniform stable recovery through the zero-curvature stratum.

**REGRESSION:** YES.

---

## F48 — dense-sampling finite-difference inflation

**Record source:** [falsifier-registry-09.md](falsifier-registry-09.md).

**TARGET:** any inference

\[
\Delta\downarrow0
\Rightarrow
\text{raw derivative estimation improves at fixed observation noise}.
\]

**ORACLE:** finite-difference noise amplification.

For derivative order `r`, the raw noise term scales like a negative power of the stencil step; in the explicit stencils used by FS-STAT:

\[
\operatorname{Var}(\widehat d_1)\propto h^{-2},
\quad
\operatorname{Var}(\widehat d_2)\propto h^{-4},
\quad
\operatorname{Var}(\widehat d_3)\propto h^{-6}.
\]

**VERDICT:** smoothing/bandwidth selection is required.

---

## F49 — universal curvature threshold

**Record source:** [falsifier-registry-09.md](falsifier-registry-09.md).

**TARGET:** any hard-coded universal rule such as

`if κ < constant then switch to Bishop`

without reference to sampling, noise, derivative uncertainty or task tolerance.

**ORACLE:** require a certified denominator/error budget.

**VERDICT:** universal threshold prohibited; switch must be protocol-relative.

---

## F50 — confidence-without-probability-model

**Record source:** [falsifier-registry-09.md](falsifier-registry-09.md).

**TARGET:** a claimed confidence level under only deterministic bounded noise.

**FALSIFIER:** no declared sampling distribution / probability law from which coverage is defined.

**VERDICT:** confidence claim invalid. Use deterministic uncertainty bounds instead.

---

## F51 — torsion-test outside Frenet gate

**Record source:** [falsifier-registry-09.md](falsifier-registry-09.md).

**TARGET:** pointwise or global `H0: τ=0` inference when `||γ'×γ''||` is not certified away from zero.

**VERDICT:** blocked. Failure to identify torsion is not evidence of zero torsion.

---

## F52 — pointwise-to-global flatness inflation

**Record source:** [falsifier-registry-09.md](falsifier-registry-09.md).

**TARGET:** inference

\[
\text{pointwise non-rejection/rejection pattern}
\Rightarrow
\tau\equiv0\text{ or }\tau\not\equiv0\text{ globally}
\]

without simultaneous/global error control.

**VERDICT:** prohibited. Global planarity needs a simultaneous band or global statistic.

---

## F53 — Bishop-is-noiseless inflation

**Record source:** [falsifier-registry-09.md](falsifier-registry-09.md).

**TARGET:** any inference

\[
\text{Bishop avoids Frenet singularity}
\Rightarrow
\text{Bishop estimation is immune to sampling/noise}.
\]

**VERDICT:** prohibited. Bishop removes the singular division by curvature but still depends on estimated tangent/transport data.

---

## F54 — quotient-confidence inflation

**Record source:** [falsifier-registry-09.md](falsifier-registry-09.md).

**TARGET:** coordinatewise confidence intervals claimed to imply valid coverage of the quotient class `[k]_{SO(2)}`.

**ORACLE:** require an explicit quotient metric/alignment plus bootstrap/asymptotic coverage proof.

**CURRENT VERDICT:** OPEN; not supplied by FS-STAT-01.

---

## F55 — gauge / observation mismatch

**Record source:** [falsifier-registry-10.md](falsifier-registry-10.md).

**TARGET:** any claim that a geometrically natural transformation group `G` can automatically be quotiented inside a compatible fibre over fixed observation `Y`.

**FALSIFIER:** find `g∈G` and candidate `x` such that

\[
\Psi(g\cdot x)\neq\Psi(x)
\]

under a contract that keeps `Y` fixed and has no corresponding action/equivariance on the observation side.

**FIXED WITNESS:** corrected `CAT–FACT–NORM–MINI-01`:

\[
Y_{abs}=\gamma(t),
\qquad
G=SE(3).
\]

For nontrivial `g`, generally `gγ(t)≠γ(t)`, so `SE(3)` does not act inside the same fixed-coordinate observation fibre.

**REPAIR:** either remove the external quotient from the absolute-coordinate contract or replace observation by an explicitly `SE(3)`-invariant/equivariant shape observation.

**REGRESSION:** YES.

---

## F56 — quotient rewrite before gauge well-definedness

**Record source:** [falsifier-registry-10.md](falsifier-registry-10.md).

**TARGET:** invocation of confluence modulo gauge without defining the induced rewrite on gauge classes or proving raw-rewrite equivariance.

**FALSIFIER:** two gauge-equivalent raw representatives for which a claimed rewrite step fails to descend to one quotient step/class.

**ORACLE:** either:

1. define the rewrite relation directly on quotient/gauge classes; or
2. prove equivariance/representative independence before invoking quotient confluence.

**FIXED APPLICATION:** `CAT–FACT–NORM–MINI-01` now states the rewrite theorem on constant-normal-`SO(2)` gauge classes.

**REGRESSION:** YES.

---

## F57 — task adequacy / full contract legality conflation

**Record source:** [falsifier-registry-10.md](falsifier-registry-10.md).

**TARGET:** any inference

\[
\ker q\subseteq E_{\mathcal T}
\Rightarrow
q\text{ is fully legal under the whole contract}
\]

without checking the remaining contract requirements.

**VERDICT:** prohibited.

Kernel inclusion proves exact preservation of task distinctions. Full contract legality may also require domain/codomain typing, observation compatibility/equivariance, admissible gauge/action and hard domain constraints.

**REGRESSION:** C60 / MINI gauge-observation correction.

---

## F58 — old-source automatic promotion

**Record source:** [falsifier-registry-10.md](falsifier-registry-10.md).

**TARGET:** any inference

`older typed source contains definition/theorem`

\[
\Rightarrow
\]

`definition/theorem is current CANON-03 material`.

**ORACLE:** migration gate:

`TYPE | STATUS | SOURCE | PROOF/TEST | CANON COMPATIBILITY`.

**FIXED CASES:** catalog ADEQ and the general CAT/FACT groupoid/homotopy layer have strong older sources but remain migration-pending until explicitly reconciled with CANON-03.

---

## F59 — MINI set model / general PSI-FACT conflation

**Record source:** [falsifier-registry-10.md](falsifier-registry-10.md).

**TARGET:** treating

\[
\operatorname{Fact}^{0}_{FB,P_0}(Y)
\]

from the finite Frenet/Bishop grammar as the general definition of PSI-FACT.

**FALSIFIER:** a task in which stabilizers, compatibility witnesses, nontrivial diagram type or higher/groupoid structure are relevant and are lost by a coarse set quotient.

**ORACLE:** general PSI-FACT source layer uses a factorization groupoid / weak-homotopy ADEQ fibre when required by the contract.

**VERDICT:** MINI is a restricted set-level benchmark only.

---

## F60 — uniqueness beyond representation image

**Record source:** [falsifier-registry-10.md](falsifier-registry-10.md).

**TARGET:** from

\[
R=g\circ\rho
\]

claiming a unique map `g:Z→W` when `rho:Omega→Z` is not surjective.

**ORACLE:** uniqueness from the kernel-factorization lemma holds only on

\[
\operatorname{im}\rho.
\]

Any extension outside the image requires additional structure/choice and need not be unique.

---

## F61 — task quotient / Markov lumpability conflation

**Record source:** [falsifier-registry-11.md](falsifier-registry-11.md).

**TARGET:** any inference of the form

\[
\text{a partition/quotient is exact for the declared task}
\Longrightarrow
\text{the quotient carries an autonomous Markov dynamics}
\]

without checking block-transition stability.

For a finite Markov chain with transition matrix `P`, equivalence relation `E`, quotient `S/E` and a block `C`, define

\[
P(x,C)=\sum_{z\in C}P(x,z).
\]

**ORACLE:** strong/Kemeny–Snell lumpability requires

\[
\boxed{
 xEy
 \Longrightarrow
 P(x,C)=P(y,C)
 \quad\forall C\in S/E.
}
\]

Task adequacy and stochastic projectability are distinct gates.

### Fixed witness

Let

\[
S=\{a,b,c\},
\qquad
E=\{\{a,b\},\{c\}\},
\]

and

\[
P(a,a)=1,
\qquad
P(b,c)=1,
\qquad
P(c,c)=1.
\]

For the block `A={a,b}`:

\[
P(a,A)=1,
\qquad
P(b,A)=0.
\]

Thus `aEb` may be legal for a static task that does not distinguish `a` from `b`, while the partition is not lumpable.

**VERDICT:**

\[
\boxed{
\text{task quotient}
\not\Rightarrow
\text{Markov lumpability}.
}
\]

**REPAIR:** either add the block-transition stability condition, or refine/change the task/contract so that the dynamically relevant distinction is retained.

**REGRESSION:** `principia-v2-10-strong-lumpability-bridge.md`, §7.

---

## F62 — normal-form uniqueness / factorization-fibre singleton conflation

**Record source:** [falsifier-registry-12.md](falsifier-registry-12.md).

**TARGET:** any inference of the form

\[
\text{rewrite terminates and is confluent modulo gauge}
\Rightarrow
|\operatorname{RawFact}(Y)/G|=1.
\]

**FALSIFIER:** choose a regular interval curve admitting a Bishop representation and an interior cut `a`. Then

\[
B_{[0,L]}
\]

and

\[
B_{[0,a]}\oplus B_{[a,L]}
\]

are distinct grammar factorizations. A constant legal gauge rotation does not remove the segmentation boundary, so they need not be equal in the gauge-only quotient.

Nevertheless both reduce to the same Bishop normal class.

**ORACLE:** distinguish three objects:

1. raw grammar factorizations;
2. gauge-only factorization candidate classes;
3. task/normal-form quotient induced by equality of normal form.

Confluence licenses

\[
|\operatorname{im}\operatorname{NF}|=1
\]

or equivalently

\[
|\mathfrak F(Y)/\!\equiv_{NF}|=1,
\]

not literal singleton cardinality of `RawFact/G`.

**FIXED APPLICATION:** `cat-fact-norm-mini-02.md`, Freeze 01 Errata 01, C19-v3.

**REGRESSION:** YES.

---
