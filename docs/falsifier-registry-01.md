# PSI — falsifier registry 01

**Status:** ACTIVE / TEST GOVERNANCE  
**Purpose:** bind claims to the kind of observation, counterexample or implementation failure that can actually weaken them.

This registry prevents PASS inflation. A successful run may certify only the object that its oracle puts at risk.

## 1. Schema

Each entry records:

- `TARGET` — claim / policy / implementation under test;
- `FALSIFIER` — observation that would contradict the target under its stated hypotheses;
- `ORACLE` — rule deciding PASS/FAIL;
- `SCOPE` — what a result does and does not establish;
- `REGRESSION` — whether the case must remain in the permanent test bank.

General rule:

\[
\boxed{\text{CLAIM}\to\text{FALSIFIER}\to\text{TEST}\to\text{ORACLE}\to\text{VERDICT}}
\]

A test with no possible target failure is not a falsification test.

---

## F01 — CORE5 sufficiency

**TARGET:** current five-role contract architecture is sufficient for the present PSI canon.

**FALSIFIER:** a typed counterexample in which a necessary semantic role cannot be represented by changing contract, observable family, dynamics/transports, quotient, frame or derived fibre structure without introducing a genuinely new primitive role.

**ORACLE:** if every legal encoding preserves the wrong distinction or loses a distinction required by the task, the witness is a candidate `R4` trigger.

**SCOPE:** inconvenience, notation growth or a new application domain is not enough.

**REGRESSION:** YES — any accepted R4 witness becomes permanent.

Current status: `NO ACCEPTED WITNESS`.

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

**SCOPE:** this is an elementary quotient fact. A failed software fixture refutes the fixture/implementation first, not automatically the mathematics.

**REGRESSION:** YES.

---

## F03 — factorization / global sufficiency

**TARGET:** set-level factorization through a representation when its equivalence kernel refines the target kernel.

**FALSIFIER:** maps `ρ,R` satisfying the stated kernel inclusion for which no well-defined set map `g` on `im ρ` exists with `R=g∘ρ`.

**ORACLE:** representative-independence of `g([x])=R(x)`.

**SCOPE:** measurable, continuous or smooth factorization requires extra hypotheses; a failure of regularity does not refute the bare set-theoretic statement.

**REGRESSION:** YES.

---

## F04 — task-closure specification

**TARGET:** a declared contract determines the task closure used to construct `E_T`.

**FALSIFIER:** two materially different closure families are both legal under the same written contract and produce different task equivalences.

**ORACLE:** explicit construction of two admissible closures with different induced kernels.

**VERDICT:** `CONTRACT / SPECIFICATION FAIL`, not automatically a failure of CORE5.

**REGRESSION:** YES.

---

## F05 — deterministic quotient dynamics

**TARGET:** `δ` descends to `Ω/E` when `E` is dynamically stable.

**FALSIFIER:** `xEy` but `δ(x)` and `δ(y)` belong to different `E`-classes while a quotient dynamics is nevertheless claimed well-defined.

**ORACLE:** representative dependence of the proposed quotient map.

**SCOPE:** classical quotient condition; PSI-specific novelty is not claimed.

**REGRESSION:** YES.

---

## F06 — stochastic/lumpability bridge

**TARGET:** a PSI task partition supports autonomous Markov quotient dynamics under the added block-transition stability condition.

**FALSIFIER:** states in one task class assign different transition mass to some quotient block.

**ORACLE:** compare

\[
P(x,C)\quad\text{and}\quad P(y,C)
\]

for `xE_Ty` and quotient blocks `C`.

**SCOPE:** this refutes a lumpability bridge for that contract, not task equivalence itself.

**REGRESSION:** YES.

---

## F07 — FRAME / higher fibre / PSI-FACT core pressure

**TARGET:** FRAME, higher fibres and factorization fibres remain derived structures rather than new CORE5 primitives.

**FALSIFIER:** a concrete witness where the relevant identifiability question cannot be represented as a candidate space plus observation/compatibility/task/dynamics contract without loss of the semantic role under investigation.

**ORACLE:** explicit failed reduction to current roles, not merely an analogy argument.

**SCOPE:** until such a witness exists, these modules do not justify R4.

**REGRESSION:** YES if found.

---

## F08 — model-to-model handoff invariant

**TARGET:** model change preserves epistemic status unless the receiving model performs a new explicit verification.

**FALSIFIER:** a transferred `HYPOTHESIS`, `OPEN`, `POLICY` or source-derived claim silently becomes `KNOWN`, theorem or fact after handoff.

**ORACLE:** compare source handoff status with successor output and its cited verification path.

**VERDICT:** `AGENT / HANDOFF FAIL`.

**REGRESSION:** YES.

---

## F09 — same information implies same agency

**TARGET:** any claim that information-equivalent states/representations automatically have equal executable action structure.

**FALSIFIER:** two cases in the same relevant observation/task fibre but with different legal or executable actions.

**ORACLE:** compare action sets / execution conditions while holding the information relation fixed.

**STATUS:** historical Lazarus/D2-type witness already shows this implication is unsafe.

**REGRESSION:** YES.

---

## F10 — PSI-TRAFFIC G0D semantics

**TARGET:** the public apparatus measures aggregate outbound research **clicks**.

**FALSIFIER:** documentation or summary claims confirmed arrival, traversal, comprehension or contribution from the click event alone.

**ORACLE:** instrumentation occurs on source-page click before any destination-side confirmation.

**STATUS:** `REGRESSION FOUND AND CORRECTED 2026-09-28`.

**REGRESSION:** YES.

Invariant:

\[
\boxed{\text{outbound click}\neq\text{confirmed destination arrival}.}
\]

---

## F11 — PSI–JEV RUN-01

**TARGET:** Jev adapter conforms to a frozen synthetic separating-test oracle.

**FALSIFIER:** adapter/model output fails to select the frozen oracle action or wrapper collapses model confidence into PSI identifiability.

**ORACLE:** pre-registered fixture.

**SCOPE:** PASS/FAIL concerns the adapter/conformance run only. It does not confirm or falsify PSI core.

**REGRESSION:** YES once a live run result exists.

---

## 2. PASS inflation rule

For every run report write both:

`WHAT FAILED / PASSED`

and

`WHAT THIS RESULT DOES NOT TEST`.

If the second field is absent, the report is incomplete.

## 3. Promotion gate

A claim may move from `OPEN/BRIDGE` toward stable theorem status only if its test/proof has:

\[
\boxed{\text{typed hypotheses}+\text{real falsifier}+\text{oracle}+\text{regression witness}.}
\]

Where the statement is a classical theorem, proof and provenance take precedence over manufacturing an empirical pseudo-falsification.