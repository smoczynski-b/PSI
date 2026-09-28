# PSI — falsifier registry 06

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-05.md` as current public registry.

Retain F01–F30 from v05 without semantic change.

---

## F31 — candidate-stuffing / anti-tautology regression

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

**TARGET:** any inference

\[
\text{four current pressure tests passed}
\Rightarrow
\text{CORE5 universally complete}.
\]

**FALSIFIER / CORRECTION:** the pressure court ranges only over the current counterexample set. A future new semantic-role witness may reopen R4.

**VERDICT:** universal completeness claim prohibited.

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