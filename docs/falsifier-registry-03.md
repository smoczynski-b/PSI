# PSI — falsifier registry 03

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-02.md` as current public registry.  
**Purpose:** bind substantive claims to observations, counterexamples or implementation failures that can actually weaken them.

General rule:

\[
\boxed{\text{CLAIM}\to\text{FALSIFIER}\to\text{TEST}\to\text{ORACLE}\to\text{VERDICT}.}
\]

A successful run certifies only the object put at risk by its oracle.

---

## F01 — CORE5 sufficiency

**TARGET:** current five-role contract architecture is sufficient for the present PSI canon.

**FALSIFIER:** a typed counterexample in which a necessary semantic role cannot be represented by changing candidate object, observation, compatibility, task observables, dynamics/transports or contract without losing a distinction required by the task.

**ORACLE:** explicit failed reductions against all current roles + contract expansion + a minimality argument for the proposed new role.

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

---

## F03 — factorization / global sufficiency

**TARGET:** set-level factorization through `rho` under kernel inclusion.

**FALSIFIER:** maps satisfying the kernel inclusion for which no representative-independent factor map exists.

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

**FALSIFIER:** `xE_Ty` but `P(x,C) != P(y,C)` for some quotient block `C`.

---

## F07 — derived-structure core pressure

**TARGET:** FRAME, higher fibres and factorization fibres remain derived under CORE5 unless a typed loss witness shows otherwise.

**FALSIFIER:** every legal encoding in candidate/observation/compatibility/task/dynamics/contract roles destroys a task-relevant distinction preserved by the proposed new structure.

**ORACLE:** failed reduction table + loss witness + minimality of the proposed role.

---

## F08 — model-to-model handoff invariant

**TARGET:** model change preserves epistemic status unless new verification is performed.

**FALSIFIER:** inherited `OPEN/HYPOTHESIS/POLICY` silently becomes fact/theorem after handoff.

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

---

## F11 — PSI–JEV RUN-01

**TARGET:** Jev adapter conforms to the frozen synthetic separating-test oracle.

**FALSIFIER:** adapter/model output disagrees with the frozen oracle or wrapper collapses model confidence into PSI identifiability.

**SCOPE:** adapter conformance only.

---

## F12 — CAT–FACT–NORM–MINI exact uniqueness

**TARGET:** every legal MINI term reduces to one Bishop factorization class under the exact interval contract.

**FALSIFIER:** infinite rewrite, nonjoinable critical pair modulo gauge, two non-gauge-equivalent normal Bishop classes for the same exact observation, or two non-gauge-equivalent timing/shape factorizations.

**REGRESSION:** YES.

---

## F13 — CAT birth versus frame/recode confusion

**TARGET:** in MINI-01, vanishing Frenet curvature while the curve remains regular does not require catalog `birth`.

**FALSIFIER:** a regular exact-protocol case where crossing the Frenet singularity creates a genuinely new external behavioural sector not represented by Bishop recode while preserving the interface.

**REGRESSION:** YES.

---

## F14 — CLOSED-FRAME extension gate

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

**TARGET:** any future claim that MINI-01 remains statistically stable under finite sampling/noise.

**FALSIFIER:** admissible perturbations under the declared error model produce unstable curvature/frame/factorization classes beyond tolerance.

**STATUS:** `OPEN`.

---

## F16 — CLOSED-FRAME R4 pressure

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

**TARGET:** any inference `normal bundle trivial => Bishop holonomy trivial`.

**FALSIFIER:** a trivializable normal bundle equipped with the normal transport of a closed space curve having nonidentity return map.

**VERDICT:** the implication is invalid; bundle triviality and connection holonomy are different properties.

**REGRESSION:** YES.

---

## F19 — concrete closed-loop numerical fixture

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