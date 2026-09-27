# PSI — method

PSI is not only a set of formulas. It imposes a discipline on inference.

## 1. Separate observation from reconstruction

Start from what was actually observed.

Do not silently replace

\[
Y=\text{observation}
\]

with

\[
\widehat x=\text{preferred hidden explanation}.
\]

The first object to compute or describe is the compatible fiber

\[
F(Y).
\]

## 2. Preserve alternatives until they are separated

If the evidence identifies only a class, keep the class.

Do not choose a representative merely because it is familiar, simple or narratively attractive.

This is especially important for AI systems, where fluent language can conceal an unjustified collapse of uncertainty.

## 3. Ask for the next separating test

When several hypotheses remain compatible, the next useful action is not more description of the same data but an observation that distinguishes the live alternatives.

Operationally:

\[
Y_t
\to
F(Y_t)
\to
\text{separating test}
\to
Y_{t+1}
\to
\text{decision}.
\]

A good test reduces the task-relevant fiber. A bad test merely produces more data without changing distinguishability.

## 4. Preserve provenance and state

Claims, assumptions, observations and decisions should remain traceable.

For an AI agent, distinguish at least:

- the agent specification;
- the current live state;
- the observation history;
- the active contract/task;
- the decision ledger;
- frozen results and later corrections.

A later answer should not overwrite the conditions under which an earlier answer was justified.

## 5. Use counterexamples before adding concepts

PSI grows conservatively.

A new term is not a new primitive merely because it is useful. First ask whether the phenomenon can already be represented by the existing structure.

The preferred sequence is:

\[
\text{claim}
\to
\text{counterexample search}
\to
\text{minimal repair}
\to
\text{regression test}
\to
\text{freeze}.
\]

## 6. The Bronsztejn filter

Before accepting a mathematical statement into the stable layer, identify:

\[
\boxed{
\text{object}
\to
\text{type/domain}
\to
\text{conditions}
\to
\text{measured quantity}
\to
\text{test}
}
\]

If one of these is missing, the statement may still be useful as intuition, but it does not yet have the right to canonical status.

## 7. Boundary of knowledge

A mature model should not only answer questions. It should expose the boundary of its own distinguishability.

The goal is therefore not merely to reduce uncertainty, but to make the remaining uncertainty structured:

- missing data;
- non-observability;
- non-identifiability;
- competing hypotheses;
- inadequate representation;
- unresolved task definition.

PSI treats this boundary as part of the result, not as an embarrassment to be hidden.
