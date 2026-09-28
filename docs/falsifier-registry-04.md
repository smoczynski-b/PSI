# PSI — falsifier registry 04

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-03.md` as current public registry.  
**Purpose:** bind substantive claims to observations, counterexamples or implementation failures that can actually weaken them.

General rule:

\[
\boxed{\text{CLAIM}\to\text{FALSIFIER}\to\text{TEST}\to\text{ORACLE}\to\text{VERDICT}.}
\]

A successful run certifies only the object put at risk by its oracle.

---

## F01 — CORE5 sufficiency

**TARGET:** current five-role architecture is sufficient unless a typed loss witness forces a new semantic role.

**FALSIFIER:** every legal encoding in candidate/observation/compatibility/task/dynamics/contract roles loses a task-relevant distinction preserved by a proposed new role.

**STATUS:** `NO ACCEPTED R4 WITNESS`.

---

## F02–F08 — existing core / handoff regressions

Retain without change:

- F02 exact task decidability;
- F03 factorization/global sufficiency;
- F04 task-closure specification;
- F05 deterministic quotient dynamics;
- F06 lumpability bridge;
- F07 derived-structure pressure;
- F08 model-handoff epistemic status.

---

## F09 — CURRENT-STATE FIBRE VERSUS TASK AGENCY

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

## F10–F19 — retained regressions

Retain without semantic change:

- F10 traffic click ≠ confirmed arrival;
- F11 JEV adapter conformance only;
- F12 MINI exact uniqueness;
- F13 Frenet singularity ≠ automatic birth;
- F14 CLOSED-FRAME holonomy gate;
- F15 FS-STAT noise/stability gate;
- F16 CLOSED-FRAME R4 pressure;
- F17 holonomy versus gauge;
- F18 bundle triviality versus connection holonomy;
- F19 closed-loop numerical fixture.

---

## F20 — LAZARUS agency CORE5 pressure

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

**TARGET:** `Γ_t` is the active composition/operational state, not a generic resource, scalar score or automatically independent primitive.

**FALSIFIER:** a later derivation silently changes the type or role of `Γ_t` without an explicit new contract.

**ORACLE:** type audit against `Comp(R_t)` and the declared execution signature.

**REGRESSION:** YES.

---

## F24 — oracle decision versus information policy

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

## PASS inflation rule

Every run report must contain both:

`WHAT FAILED / PASSED`

and

`WHAT THIS RESULT DOES NOT TEST`.

## Promotion gate

A non-classical claim may move toward stable theorem status only after

\[
\boxed{\text{typed hypotheses}+\text{proof/test}+\text{real falsifier}+\text{oracle}+\text{scope}.}
\]

For classical theorems, proof and provenance take precedence over manufactured pseudo-falsification.