# PSI–JEV RUN-01 — separating-test selection

**Status:** PRE-REGISTERED / Jev output pending  
**Module:** PSI–Jev experimental adapter  
**Core status:** not part of the PSI core  
**Purpose:** closed-fixture conformance / smoke test

This run tests one narrow question:

> Can a fast typed decision model select the unique one-step test that guarantees task-level identifiability, without replacing PSI identifiability with model confidence?

No empirical claim about Jev is made before an actual Jev output is recorded.

**Scope correction.** RUN-01 does not falsify PSI. The PSI oracle is constructed analytically before the Jev call, so the run can only test whether the experimental adapter conforms to a known closed fixture. A failure is a Jev/adapter failure on this task, not a failure of the PSI core.

---

## 1. Synthetic domain

Let

\[
\Omega=\{a,b,c,d\}.
\]

The initial observation is deliberately non-identifying:

\[
\Psi(a)=\Psi(b)=\Psi(c)=\Psi(d)=Y_0.
\]

Therefore the compatible fiber is

\[
F(Y_0)=\{a,b,c,d\}.
\]

The task \(\mathcal T\) does not require recovery of the exact hidden state. It asks only for the task class

\[
q_{\mathcal T}(a)=q_{\mathcal T}(b)=0,
\qquad
q_{\mathcal T}(c)=q_{\mathcal T}(d)=1.
\]

Hence the initial task quotient is

\[
q_{\mathcal T}(F(Y_0))=\{0,1\},
\]

so

\[
|q_{\mathcal T}(F(Y_0))|=2>1.
\]

The problem is therefore **not exactly decidable** from \(Y_0\).

---

## 2. Available tests

The admissible action set is finite:

\[
A=\{T_1,T_2,T_3\}.
\]

Each test returns one bit.

### Test \(T_1\)

\[
T_1(a)=T_1(b)=0,
\qquad
T_1(c)=T_1(d)=1.
\]

This test partitions the fiber exactly along the task-equivalence classes.

### Test \(T_2\)

\[
T_2(a)=T_2(c)=0,
\qquad
T_2(b)=T_2(d)=1.
\]

Each possible result leaves both task classes alive.

### Test \(T_3\)

\[
T_3(a)=T_3(b)=T_3(c)=T_3(d)=0.
\]

This test provides no information.

---

## 3. PSI oracle

A test is accepted as a one-step solution only if **every possible result** leaves a non-empty updated fiber contained in one task-equivalence class.

For \(T_1\):

- result \(0\) gives \(F_1=\{a,b\}\), hence
  \[
  |q_{\mathcal T}(F_1)|=1;
  \]
- result \(1\) gives \(F_1=\{c,d\}\), hence
  \[
  |q_{\mathcal T}(F_1)|=1.
  \]

Therefore \(T_1\) guarantees exact task-level decidability after one observation.

For \(T_2\):

- result \(0\) gives \(\{a,c\}\), containing both task classes;
- result \(1\) gives \(\{b,d\}\), containing both task classes.

Thus

\[
|q_{\mathcal T}(F_1)|=2
\]

for either result.

For \(T_3\):

\[
F_1=F(Y_0)
\]

and the task ambiguity is unchanged.

Hence the unique PSI oracle choice is

\[
\boxed{T^*=T_1.}
\]

This conclusion is obtained independently of Jev.

---

## 4. Typed decision question for Jev

Jev should receive the explicit state and the closed action set only.

### State

```text
candidate states: a, b, c, d
initial compatible fiber: {a,b,c,d}
task classes: {a,b}->0, {c,d}->1
available tests:
T1: {a,b}->0, {c,d}->1
T2: {a,c}->0, {b,d}->1
T3: {a,b,c,d}->0
```

### Question

```text
Choose exactly one test from {T1,T2,T3}.
Criterion: choose the test that guarantees a unique task-level conclusion after one test result, regardless of which result occurs.
```

### Required output to record

At minimum:

```text
choice: T1 | T2 | T3
scores/probabilities: if exposed by the Jev interface
confidence/decision strength: if exposed by the Jev interface
raw typed output: preserved verbatim
```

No free-form explanation is required for scoring the run.

---

## 5. Hard constraints

The adapter policy is fixed before the Jev call:

1. Jev may choose only from \(\{T_1,T_2,T_3\}\).
2. Jev output does not alter the definition of the fiber.
3. Jev confidence does not alter the PSI exact-decidability criterion.
4. A test is credited as separating only by the explicit partitions above.
5. No post-hoc change of the task partition is allowed.

Formally:

\[
\boxed{\text{hard constraints} > \text{model preference}.}
\]

---

## 6. Acceptance criteria

### RUN-01 PASS

The adapter passes this narrow conformance check iff

\[
\mathcal J(S,Q,A)=T_1.
\]

### RUN-01 FAIL

The adapter fails this narrow conformance check if Jev chooses \(T_2\) or \(T_3\).

This `PASS/FAIL` concerns the Jev adapter on the frozen fixture. It is not a truth value for PSI.

### Adapter-level warning

Even if Jev chooses \(T_1\), the integration receives a warning if any wrapper or downstream policy treats a confidence score as proof that

\[
|q_{\mathcal T}(F(Y_0))|=1.
\]

That statement is false before the test result is observed.

---

## 7. Result ledger

To be filled only after a real Jev execution.

| field | value |
|---|---|
| run id | PSI-JEV-RUN-01 |
| fixture version | 1.0 |
| Jev model/version | PENDING |
| Jev choice | PENDING |
| Jev score vector | PENDING |
| Jev confidence | PENDING |
| PSI oracle | T1 |
| adapter conformance result | PENDING |
| constraint violations | PENDING |
| notes | PENDING |

---

## 8. Why keep this test

This fixture is intentionally trivial for deep reasoning.

Its value is limited but legitimate: it is a unit-level integration check that isolates three quantities

\[
\text{choice quality},
\qquad
\text{confidence},
\qquad
\text{identifiability}.
\]

A successful Jev integration must preserve all three as different quantities.

RUN-01 therefore asks only:

\[
\boxed{\text{Can Jev select the known separating test in a closed typed state?}}
\]

It does not test whether the PSI framework is mathematically correct, novel, or empirically superior.

A genuine PSI falsification attempt must instead put a PSI-specific claim at risk. For a mathematical statement this means, for example, finding a counterexample that satisfies the stated hypotheses and violates the claimed conclusion.

---

## 9. Next run gate

Do **not** promote the adapter or generalize from RUN-01 alone.

Proceed to a harder run only after recording the actual Jev output and checking the ledger above.

A later benchmark may deliberately separate model confidence from PSI identifiability by constructing cases in which

\[
\text{high confidence} + \text{low identifiability}
\]

and

\[
\text{low confidence} + \text{high identifiability}
\]

are both possible.

Such a benchmark would still test the adapter unless a PSI-specific formal or empirical claim is explicitly placed at risk.
