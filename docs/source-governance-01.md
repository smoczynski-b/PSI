# PSI — source governance 01

**Status:** EDITORIAL / AGENT GOVERNANCE  
**Origin:** historical program `ŹRÓDŁA` / current PSI provenance discipline  
**Purpose:** prevent source loss, semantic drift and post-hoc promotion of claims during redaction and agent handoff.

This document is not a new mathematical primitive.

## 1. Minimal claim record

Every nontrivial migrated claim should be recoverable as

\[
C=(S,P,O,D,\sigma,\kappa),
\]

where:

- `S` — source or canonical parent;
- `P` — proposition / claim;
- `O` — operator path: transformations used to obtain the present formulation;
- `D` — dependencies;
- `σ` — epistemic status;
- `κ` — confidence / unresolved condition when relevant.

If the operator path cannot be recovered, the claim is not silently repaired from memory.

---

## 2. Processing order

Historical material passes through

\[
\boxed{
\text{SOURCE}
\to
\text{ANALYSIS}
\to
\text{AUDIT}
\to
\text{VERDICT}
\to
\text{PLACEMENT}.
}
\]

Allowed verdicts for Principia migration:

\[
\mathrm{KEEP}\mid
\mathrm{REFORMULATE}\mid
\mathrm{SUPERSEDE}\mid
\mathrm{GENEALOGY}.
\]

No narrative attractiveness can replace this path.

---

## 3. Source classes

Use at least:

- `CANONICAL` — current pinned PSI canon;
- `CLASSICAL` — external established mathematics;
- `HISTORICAL-PSI` — older project artifact;
- `EXPERIMENT` — recorded run / dataset / protocol output;
- `DERIVED` — proved or explicitly transformed from named sources;
- `OPEN` — unresolved hypothesis / bridge;
- `POLICY` — project or publication rule.

A historical source is evidence for what the project once claimed. It is not automatically evidence that the claim remains true.

---

## 4. Drift test

For source statement `S` and migrated statement `T`, record the transformation path

\[
S\xrightarrow{O_1}S_1\xrightarrow{O_2}\cdots\xrightarrow{O_n}T.
\]

Audit questions:

1. Did the object change?
2. Did its type/domain change?
3. Did hypotheses disappear?
4. Did claim strength increase?
5. Did an analogy become an identity?
6. Did a laboratory observable become a core primitive?
7. Did a correlation become a causal or ontological statement?
8. Did a model result become a theorem of PSI?

Any unrecorded YES blocks automatic migration.

---

## 5. Model / agent handoff

Model change does not reset provenance.

For agents `A_i`, `A_{i+1}`:

\[
A_i
\to
\text{explicit artifact/state}
\to
A_{i+1}.
\]

The successor must be able to classify inherited material as:

\[
\mathrm{FACT}\mid
\mathrm{CLAIM}\mid
\mathrm{INFERENCE}\mid
\mathrm{POLICY}\mid
\mathrm{OPEN}\mid
\mathrm{ACTION}.
\]

No model gets epistemic priority merely by being newer.

---

## 6. Bronsztejn gate

Before a mathematical statement is admitted, require:

\[
\boxed{
\text{object}
\to
\text{type/domain}
\to
\text{conditions}
\to
\text{measured/claimed quantity}
\to
\text{test/proof}.
}
\]

Missing elements do not prove a statement false; they block promotion to canon/theorem status.

For unbounded operators add:

\[
\boxed{\text{domain before formal algebra}.}
\]

---

## 7. Public provenance rule

Public PSI must distinguish:

**Claim status**
- `CLASSICAL`
- `BRIDGE`
- `PSI-NEW`
- `POLICY`
- `OPEN`

from **role in PSI**
- `ADAPTED`
- `GENEALOGICAL`
- `BENCHMARK`
- `CORE`
- laboratory / realization role where appropriate.

These are orthogonal metadata axes.

---

## 8. Empirical claims

An empirical claim requires:

- declared dataset / observation window;
- preprocessing path;
- measurement definition;
- baseline / comparator;
- uncertainty / censoring boundary;
- actual result artifact.

A protocol without a run is not a result.
A result of an adapter test is not a validation of PSI core.
A social reaction is not website traffic.
An aggregate outbound click is not comprehension.

---

## 9. Dual-use gate

Before public release classify:

\[
\boxed{
\mathrm{PUBLIC}\mid
\mathrm{REVIEW}\mid
\mathrm{WITHHOLD}.
}
\]

The gate is independent of scientific interest. A result can be epistemically valuable and still require restricted publication.

---

## 10. Invariant

The governing editorial invariant is:

\[
\boxed{
\text{claim without recoverable source or derivation is an unstable state}.
}
\]

The corrective action is not to invent provenance. It is to recover the source, downgrade the status, or leave the point open.