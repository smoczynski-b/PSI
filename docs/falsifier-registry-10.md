# PSI — falsifier registry 10

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-09.md` as current public registry.

Retain F01–F54 from v09 without semantic change.

This version adds permanent regressions discovered by `PROOF-SOURCE-MIGRATION-AUDIT-01`.

---

## F55 — gauge / observation mismatch

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

**TARGET:** invocation of confluence modulo gauge without defining the induced rewrite on gauge classes or proving raw-rewrite equivariance.

**FALSIFIER:** two gauge-equivalent raw representatives for which a claimed rewrite step fails to descend to one quotient step/class.

**ORACLE:** either:

1. define the rewrite relation directly on quotient/gauge classes; or
2. prove equivariance/representative independence before invoking quotient confluence.

**FIXED APPLICATION:** `CAT–FACT–NORM–MINI-01` now states the rewrite theorem on constant-normal-`SO(2)` gauge classes.

**REGRESSION:** YES.

---

## F57 — task adequacy / full contract legality conflation

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
