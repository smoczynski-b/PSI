# PSI — falsifier registry 08

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-07.md` as current public registry.

Retain F01–F37 from v07 without semantic change.

---

## F38 — generic memory sufficiency

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

**TARGET:** treating

\[
\rho_0\to\rho_K\to\rho_{\rm PSK}\to\rho_{\rm SSK}
\]

as a universal order of increasingly correct states independent of task.

**ORACLE:** restore the frozen rule/task contract.

**VERDICT:** each representation is judged relative to its task. Extra history can be irrelevant under a weaker rule system.

---

## F45 — G1 source fabrication

**TARGET:** any attempt to assign a board witness, memory representation or theorem to `GO-PSI G1` using only the currently recovered RED-1 source.

**ORACLE:** provenance check.

**CURRENT VERDICT:** blocked; the recovered source explicitly states G0/G2/G3/G4 but no separate G1 content.

**REOPEN:** only after recovery of the actual G1 source.

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