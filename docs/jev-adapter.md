# PSI–Jev Adapter

**Status:** experimental adapter / not part of the PSI core.

This note records a proposed integration between PSI and **Jev** as a fast typed decision layer. The purpose is not to replace PSI, a general reasoning model, or deterministic control logic. The purpose is to test whether a small decision model can serve as a low-cost selector, router, or evaluator inside a PSI-governed inference process.

The central constraint is:

\[
\boxed{\text{model confidence} \neq \text{identifiability}.}
\]

A model may strongly prefer one answer while the observation still leaves several task-relevant possibilities alive. Conversely, a task-level conclusion may already be uniquely determined even when a model reports modest confidence.

---

## 1. Role of Jev inside PSI

PSI starts from the observation structure and the compatible fiber

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

Jev is treated only as an **auxiliary decision operator** acting on an already typed state and an explicitly finite answer space.

A minimal abstract interface is

\[
\mathcal J:(S,Q,A)\longmapsto(a,p,c),
\]

where:

- \(S\) is the current explicit state;
- \(Q\) is a typed question;
- \(A=\{a_1,\ldots,a_n\}\) is the admissible answer set;
- \(a\in A\) is the selected answer;
- \(p\) is a distribution or score vector over \(A\);
- \(c\) is the reported confidence or decision strength.

The output of \(\mathcal J\) is **evidence for policy selection**, not a proof of identification.

---

## 2. Control architecture

The intended architecture is

\[
S_t
\to
\text{hard constraints}
\to
F(Y_t)
\to
\mathcal J
\to
\Pi_{\mathrm{PSI}}
\to
\text{action}.
\]

The PSI policy layer may return

\[
\Pi_{\mathrm{PSI}}
\in
\{\mathrm{EXECUTE},\mathrm{TEST},\mathrm{ESCALATE},\mathrm{ABSTAIN}\}.
\]

Hard constraints are evaluated **before** the Jev decision. Jev is never allowed to override a frozen condition, a protocol invariant, a type constraint, or a known impossibility result.

This ordering is essential:

\[
\boxed{\text{hard constraints} \;>\; \text{probabilistic preference}.}
\]

---

## 3. Candidate use cases

### 3.1 Agent action routing

For an AI agent, the admissible next-step set may be

\[
A_t=\{\mathrm{READ},\mathrm{SEARCH},\mathrm{TEST},\mathrm{COMPARE},\mathrm{ASK},\mathrm{ESCALATE},\mathrm{HALT}\}.
\]

Jev may rank or choose among these actions from an explicit state. PSI then checks whether the selected action is legal and epistemically justified.

### 3.2 Separating-test selection

Let the live candidates be

\[
F(Y)=\{x_1,\ldots,x_n\}
\]

and let a finite test library be

\[
\mathcal T=\{T_1,\ldots,T_m\}.
\]

Jev may rank candidate tests according to expected usefulness. It does **not** establish that a test is actually separating. The observed result must still be incorporated into the PSI update

\[
Y_t\to F(Y_t)\to T^*\to Y_{t+1}\to F(Y_{t+1}).
\]

### 3.3 PSI-FORUM triage

For PSI-FORUM packets, Jev may provide first-pass typed classifications such as

\[
K\in\{\mathrm{CLAIM},\mathrm{PROOF},\mathrm{COUNTEREX},\mathrm{UNRESOLVED},\mathrm{RELATION},\mathrm{TEST}\}
\]

and auxiliary checks such as:

- schema validity;
- dependency presence;
- possible duplication;
- need for deep review;
- possible protocol fault;
- likely relation to an existing claim.

The ledger, formal relations, and final acceptance rules remain deterministic or independently verified.

### 3.4 PSI watchdog

A low-cost evaluator may inspect an agent trace for conditions such as:

- use of deprecated terminology;
- departure from the current canon pointer;
- hidden contract changes;
- unsupported conclusion;
- missing provenance;
- premature collapse of alternatives;
- violation of a frozen condition;
- failure to perform a required test.

The watchdog output should be treated as a **flag vector**, not as an authority.

---

## 4. The key PSI test: confidence versus identifiability

The most important experiment is to separate two quantities that are often conflated.

A decision model may report

\[
P(a\mid Y)=0.99,
\]

while PSI still gives

\[
|q_{\mathcal T}(F(Y))|>1.
\]

The model is confident, but the task-relevant ambiguity has not been removed.

The opposite configuration is also possible:

\[
P(a\mid Y)=0.65,
\qquad
|q_{\mathcal T}(F(Y))|=1.
\]

The model is uncertain, while the observation and task contract are already sufficient for a unique task-level conclusion.

This yields the experimental matrix:

| model confidence | PSI task identifiability | interpretation |
|---|---|---|
| high | high | decision and identifiability agree |
| high | low | dangerous overconfidence candidate |
| low | high | model underconfidence / representation problem candidate |
| low | low | unresolved case |

The PSI–Jev adapter is useful only if it preserves this distinction.

---

## 5. Exact task-level criterion

For a task \(\mathcal T\), exact decidability remains a PSI statement:

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)^2\subset E_{\mathcal T}.
\]

No Jev score, probability, or confidence value replaces this criterion.

Jev may help decide **what to inspect next**. PSI decides **what the current observation licenses us to conclude**.

---

## 6. Minimal experiment

A first controlled test should use a domain with:

1. an explicit state;
2. a finite action set;
3. a known compatible fiber;
4. an independently checkable legality relation;
5. a clear success criterion.

Good initial candidates are:

- PSI-FORUM packet routing;
- a frozen Lazarus recovery state;
- a synthetic identification problem with a known separating test.

For each case record:

\[
(S_t,F(Y_t),A_t,\mathcal J(S_t),a_t,Y_{t+1}).
\]

Compare:

- Jev choice;
- Jev confidence;
- PSI legality;
- PSI identifiability status;
- result after the chosen test or action;
- an independent deep-reasoning baseline.

The primary observation is not raw accuracy alone. It is the structure of disagreement between confidence, legality, and identifiability.

---

## 7. Failure modes to test explicitly

The adapter should be rejected or revised if it systematically exhibits any of the following:

1. **confidence substitution** — treating high confidence as evidence of identifiability;
2. **constraint override** — selecting actions forbidden by the protocol;
3. **fiber collapse** — silently selecting one representative from a non-singleton fiber;
4. **type drift** — answering a different question than the typed question supplied;
5. **state omission** — acting on an incomplete state without escalation;
6. **false separation** — claiming that a test distinguishes candidates without evidence;
7. **policy opacity** — producing a choice that cannot be related to the explicit admissible action set;
8. **calibration drift** — confidence ceases to track empirical reliability across domains.

---

## 8. Acceptance criterion

The PSI–Jev adapter is successful only if Jev can reduce cost or latency **without weakening the PSI contract**.

A useful outcome therefore has the form

\[
\text{lower decision cost}
\quad+\quad
\text{preserved constraints}
\quad+\quad
\text{preserved uncertainty structure}.
\]

If the integration gains speed by hiding ambiguity, collapsing the fiber, or replacing a task-relative criterion with a probability threshold, it fails the experiment.

---

## 9. Non-goals

This adapter does not claim that:

- Jev is a truth oracle;
- confidence is a substitute for proof;
- a small decision model can replace deep reasoning in open-ended problems;
- one fixed confidence threshold is valid across domains;
- vendor-reported calibration or benchmark results should be accepted without independent testing.

Any empirical claim about Jev itself must be verified separately.

---

## 10. Working principle

The intended division of labor is:

\[
\boxed{
\text{Jev proposes efficiently; PSI constrains and licenses; deeper reasoning resolves hard cases.}
}
\]

This document is deliberately provisional. The next step is not further theorizing but a controlled falsification run.