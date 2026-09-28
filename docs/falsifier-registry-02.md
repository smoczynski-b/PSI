# PSI — falsifier registry 02

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-01.md` as current public registry.  
**Purpose:** bind every substantive claim to an observation, counterexample or implementation failure that can actually weaken it.

General rule:

\[
\boxed{\text{CLAIM}\to\text{FALSIFIER}\to\text{TEST}\to\text{ORACLE}\to\text{VERDICT}.}
\]

A successful run certifies only the object put at risk by its oracle.

---

## F01 — CORE5 sufficiency

**TARGET:** current five-role contract architecture is sufficient for the present PSI canon.

**FALSIFIER:** a typed counterexample in which a necessary semantic role cannot be represented by changing candidate object, observation, compatibility, task observables, dynamics/transports or contract without losing a distinction required by the task.

**ORACLE:** explicit failed reductions against all five current roles plus contract expansion, followed by a minimality argument for the proposed new role.

**SCOPE:** notation growth, inconvenience or a new application domain is not enough.

**STATUS:** `NO ACCEPTED R4 WITNESS`.

---

## F02 — exact task-level decidability

**TARGET:**

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing\land F(Y)^2\subseteq E_{\mathcal T}.
\]

**FALSIFIER:** a correctly typed non-empty fibre for which one side holds and the other does not.

**ORACLE:** direct set/quotient calculation.

**SCOPE:** software failure refutes the fixture/implementation first.

---

## F03 — factorization / global sufficiency

**TARGET:** set-level factorization through `rho` when `ker_eq rho ⊆ ker_eq R`.

**FALSIFIER:** maps satisfying the kernel inclusion for which no well-defined set map on `im rho` exists with `R=g∘rho`.

**ORACLE:** representative-independence.

**SCOPE:** regularity variants require extra hypotheses.

---

## F04 — task-closure specification

**TARGET:** the written contract determines the closure used to construct `E_T`.

**FALSIFIER:** two materially different closure families are both legal under the same written contract and induce different task equivalences.

**VERDICT:** contract/specification failure.

---

## F05 — deterministic quotient dynamics

**TARGET:** `delta` descends to `Omega/E` under dynamic stability.

**FALSIFIER:** `xEy` but `delta(x)` and `delta(y)` lie in different `E`-classes while quotient dynamics is claimed well-defined.

---

## F06 — stochastic/lumpability bridge

**TARGET:** a PSI task partition supports autonomous Markov quotient dynamics under block-transition stability.

**FALSIFIER:** `xE_T y` but for some quotient block `C`,

\[
P(x,C)\neq P(y,C).
\]

**SCOPE:** refutes the lumpability bridge, not task equivalence.

---

## F07 — FRAME / higher fibre / PSI-FACT core pressure

**TARGET:** these structures remain derived under CORE5.

**FALSIFIER:** a typed witness for which every legal encoding in the current candidate/observation/compatibility/task/dynamics/contract roles destroys a task-relevant distinction that the proposed structure preserves.

**ORACLE:** failed reduction table + loss witness + minimality of the proposed role.

---

## F08 — model-to-model handoff invariant

**TARGET:** model change preserves epistemic status unless new verification is performed.

**FALSIFIER:** inherited `OPEN/HYPOTHESIS/POLICY` silently becomes fact/theorem after handoff.

**VERDICT:** agent/handoff failure.

---

## F09 — same information implies same agency

**TARGET:** any claim that information-equivalent cases automatically have equal executable action structure.

**FALSIFIER:** same relevant observation/task fibre but different legal/executable action sets.

**STATUS:** historical Lazarus witness exists.

---

## F10 — PSI-TRAFFIC G0D semantics

**TARGET:** apparatus measures aggregate outbound research clicks.

**FALSIFIER:** click event alone is reported as confirmed arrival, traversal, comprehension or contribution.

**STATUS:** regression found and corrected 2026-09-28.

Invariant:

\[
\boxed{\text{outbound click}\neq\text{confirmed destination arrival}.}
\]

---

## F11 — PSI–JEV RUN-01

**TARGET:** Jev adapter conforms to the frozen synthetic separating-test oracle.

**FALSIFIER:** adapter/model output disagrees with the frozen oracle or wrapper collapses model confidence into PSI identifiability.

**SCOPE:** adapter conformance only; not PSI-core validation.

---

## F12 — CAT–FACT–NORM–MINI exact uniqueness

**TARGET:** under the precise MINI-01 hypotheses — `C^3` regular curve on an interval, fixed time parameter, exact observation, finite legal Frenet/Bishop segmentation, gauge `SE(3)×SO(2)` — every legal term reduces to one Bishop factorization class.

**FALSIFIER:** within those hypotheses, exhibit either:

1. an infinite legal rewrite chain;
2. a critical pair whose branches cannot be joined modulo the declared gauge;
3. two normal Bishop classes reconstructing the same observed curve but not related by `SE(3)×SO(2)`;
4. two non-gauge-equivalent timing/shape factorizations compatible with the exact time-parametrized observation.

**ORACLE:** explicit reduction/reconstruction calculation.

**SCOPE:** a counterexample outside the hypotheses narrows the extension domain; it does not refute MINI-01.

**REGRESSION:** YES.

---

## F13 — CAT birth versus frame/recode confusion

**TARGET:** in MINI-01, vanishing Frenet curvature while the curve remains regular does not require catalog `birth`.

**FALSIFIER:** a regular interval curve and exact protocol for which crossing a Frenet singularity creates an externally observable behavioural sector that cannot be represented by the Bishop recode or by an existing legal factorization while preserving the external interface.

**ORACLE:** compare the pre/post external behaviour classes under the declared protocol and test whether a legal semantic recode/fold exists.

**SCOPE:** this is not a universal claim about all representation failures.

**REGRESSION:** YES.

---

## F14 — CLOSED-FRAME extension gate

**TARGET:** any proposed extension of MINI-01 from an interval to a closed curve without extra data.

**PRESSURE WITNESS:** nontrivial return rotation/holonomy of the normal plane after one circuit.

**ORACLE:** transport an initial Bishop normal pair around the loop and compare the returned pair with the initial pair.

If the return map is a nontrivial `SO(2)` element, a periodic representative is not licensed without carrying or quotienting the holonomy datum.

**VERDICT:** `OPEN EXTENSION / FRAME-HIGHER PRESSURE`, not a refutation of the interval MINI theorem.

**REGRESSION:** YES once a concrete loop witness is fixed.

---

## F15 — FS-STAT stability gate

**TARGET:** any future claim that MINI-01 remains statistically stable under finite sampling/noise.

**FALSIFIER:** two admissible sampled/noisy datasets within the declared error model produce unstable curvature/frame/factorization classes beyond the claimed tolerance, especially near low-curvature regions.

**ORACLE:** pre-registered estimator + perturbation/noise model + held-out adequacy criterion.

**STATUS:** `OPEN`; exact identifiability is not statistical stability.

---

## PASS inflation rule

Every run report must contain:

`WHAT FAILED / PASSED`

and

`WHAT THIS RESULT DOES NOT TEST`.

If the second field is absent, the report is incomplete.

## Promotion gate

A non-classical claim may move toward stable theorem status only after:

\[
\boxed{\text{typed hypotheses}+\text{proof/test}+\text{real falsifier}+\text{oracle}+\text{scope}.}
\]

For classical theorems, proof and provenance take precedence over manufacturing pseudo-falsification.