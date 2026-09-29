# PSI-MEMORY-M17-CROSS-PARTITION-01

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Does the M16 fibre law remain stable when the toy two-object witness is replaced by a larger relational domain with many objects, several relation families, unequal lexical fibre widths and non-hierarchical lexical partitions?

The governing law remains:

\[
F_0=\operatorname{Lex}_L(s),
\qquad
F_{k+1}=F_k\cap\operatorname{Supp}(r_k,o_k).
\]

M17 does not add a new PSI primitive.

## 1. Frozen world domain

The fixture contains `24` synthetic timekeeping objects generated from the product:

\[
4\;\text{position classes}
\times
2\;\text{mechanisms}
\times
3\;\text{functions}.
\]

Each object is described through six relation families:

- `POSITION`;
- `MECHANISM`;
- `FUNCTION`;
- `ENERGY`;
- `DISPLAY`;
- `MEASURES`.

The assignments are deliberately combinatorial and are not claims about the empirical ontology of real clocks or watches.

## 2. Crossing lexical partitions

Frozen PL/EN/DE adapters define several candidate fibres. They are not required to form one common taxonomy.

Examples include:

- form/position-oriented fibres such as `zegarek`, `watch`, `clock`, `Armbanduhr`;
- function-oriented fibres such as `chronograf`, `chronograph`, `Chronograph`;
- broad fibres such as `czasomierz`, `timepiece`, `Zeitmesser`, `Uhr`.

M17 requires the fixture to contain many pairs \(A,B\) such that:

\[
A\cap B\neq\varnothing,
\qquad
A\not\subseteq B,
\qquad
B\not\subseteq A.
\]

Thus no single lexical partition is treated as the canonical object structure.

## 3. Main tests

M17 checks:

1. all lexical candidates belong to the same frozen world domain;
2. at least 20 lexical-fibre pairs cross without inclusion;
3. PL/EN/DE fibres with different initial widths can converge to the same singleton under the same world constraints;
4. partial evidence narrows a broad fibre monotonically;
5. a globally shared relation can remain non-discriminating;
6. redundant relation families can preserve fibre width without being counted as new discrimination;
7. conjunctive constraint order does not change the final fibre;
8. a contradiction yields the empty fibre and no later conjunct resurrects a candidate;
9. `NO_LEXICAL_FIBRE` remains distinct from `INCONSISTENT`.

## 4. Key witness

For DE `Uhr` the broad initial fibre contains all 24 world objects.

The constraints

\[
MECHANISM=QUARTZ,
\quad
FUNCTION=ALARM,
\quad
POSITION=TABLE
\]

must produce the trace

\[
\boxed{24\to12\to4\to1}.
\]

All six permutations of the three conjuncts must produce the same final singleton.

## 5. Cross-language convergence witness

PL `zegarek`, EN `watch` and DE `Uhr` begin with different fibre widths.

Under the same relational evidence

\[
POSITION=WRIST,
\quad
MECHANISM=QUARTZ,
\quad
FUNCTION=ALARM,
\]

they must converge to the same world object.

The invariant is therefore not lexical extension equality but relational identification under a common task/world contract.

## 6. Boundary

The lexical partitions and world relation assignments are frozen test fixtures. M17 is not empirical lexicography, perception, learned ontology induction or a claim that the chosen word extensions are authoritative descriptions of Polish, English or German usage.

The experiment tests only the architecture:

\[
\boxed{
\text{crossing language-relative fibres}
+\text{common relational world}
\Rightarrow
\text{monotone PSI refinement}
}
\]

under explicitly supplied data.
