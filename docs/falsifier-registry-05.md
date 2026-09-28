# PSI — falsifier registry 05

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-04.md` as current public registry.

General rule:

\[
\boxed{\text{CLAIM}\to\text{FALSIFIER}\to\text{TEST}\to\text{ORACLE}\to\text{VERDICT}.}
\]

Retain F01–F24 from v04 without semantic change, including the corrected F09 (`same current-state fibre` rather than `same full information`).

---

## F25 — coarse strict fibre versus weak fibre

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

**TARGET:** any inference

\[
\text{higher fibre contains more information}
\Rightarrow
\text{new CORE primitive}.
\]

**FALSIFIER / CHECK:** show that the additional information can be represented as structured candidate/task data and evaluated by the existing adequacy criterion.

**VERDICT:** more information alone is insufficient evidence for a new semantic role.

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