# PSI-MEMORY-M17-RESULT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36633967117` executed M1–M17 successfully.

M17 replaced the two-object M16 witness with a 24-object relational domain described by six relation families and 19 language-relative lexical entries.

The governing law remained unchanged:

\[
\boxed{
F_0=\operatorname{Lex}_L(s),
\qquad
F_{k+1}=F_k\cap\operatorname{Supp}(r_k,o_k).
}
\]

Every tested refinement remained monotone.

## 2. Crossing lexical partitions

The frozen PL/EN/DE lexical fibres contain `29` unordered pairs \(A,B\) satisfying:

\[
A\cap B\neq\varnothing,
\qquad
A\not\subseteq B,
\qquad
B\not\subseteq A.
\]

Thus the lexical layer is not a single hierarchy and cannot be represented faithfully as one language-independent word taxonomy.

A concrete witness is the crossing between a position-oriented fibre such as PL `zegarek` and a function-oriented fibre such as DE `Chronograph`.

## 3. Different language widths, same world object

For the same relational evidence

\[
POSITION=WRIST,
\quad
MECHANISM=QUARTZ,
\quad
FUNCTION=ALARM,
\]

the initial fibre widths were:

\[
|F_{PL}|=12,
\qquad
|F_{EN}|=6,
\qquad
|F_{DE}|=24.
\]

All three converged to the same singleton:

\[
\boxed{\{T\!-
WR\!-
QU\!-
AL\}}.
\]

Hence equality of initial lexical extensions is unnecessary for equality of final relational identification.

## 4. Partial evidence

For broad DE `Uhr` the sequence

\[
MECHANISM=QUARTZ,
\quad
FUNCTION=ALARM,
\quad
POSITION=TABLE
\]

produced:

\[
\boxed{24\to12\to4\to1}.
\]

Partial evidence therefore remains explicitly unresolved until the fibre is actually singleton.

All six permutations of the three conjuncts produced the same final singleton, although intermediate traces may differ.

## 5. Non-discrimination and redundancy

The world relation

\[
MEASURES=TIME
\]

is shared by all 24 objects and therefore produced:

\[
\boxed{24\to24}.
\]

It is true but non-discriminating for this task.

The fixture also intentionally correlates

\[
MECHANISM=QUARTZ
\]

with

\[
ENERGY=BATTERY.
\]

Applying both gave:

\[
\boxed{24\to12\to12}.
\]

Thus an additional true relation need not add identification power. M17 separates truth/compatibility from discrimination.

## 6. Contradiction and no resurrection

The incompatible conjunction

\[
MECHANISM=MECHANICAL,
\qquad
ENERGY=BATTERY
\]

produced:

\[
\boxed{24\to12\to0}.
\]

Adding further constraints left the fibre empty. No nearest-match or candidate resurrection occurred.

`NO_LEXICAL_FIBRE` also remained distinct from `INCONSISTENT`.

## 7. Architectural consequence

M17 supports a stronger working picture than a shared multilingual taxonomy:

\[
\boxed{
\{\operatorname{Lex}_{L_i}\}_{i\in I}
\text{ may cross arbitrarily over one relational world }W.
}
\]

The stable object is not the lexical partition. It is the candidate set under accumulated relation constraints:

\[
\boxed{
F_{L,s}(C)
=
\operatorname{Lex}_L(s)
\cap
\bigcap_{(r,o)\in C}\operatorname{Supp}(r,o).
}
\]

For finite conjunctive evidence, identification depends on this intersection, not on which language supplied the initial candidate fibre.

M17 also shows that relation truth and relation information value are distinct:

\[
\boxed{
\text{true relation}\not\Rightarrow\text{strict fibre reduction}.
}
\]

## 8. Boundary

The 24-object world and all PL/EN/DE lexical partitions are frozen combinatorial fixtures. They are not empirical lexicography, a theory of natural kinds, or a learned/perceptual ontology.

The demonstrated result is operational:

\[
\boxed{
\text{many crossing language-relative fibres}
+\text{one supplied relational domain}
\Rightarrow
\text{stable monotone PSI refinement}.
}
\]

The next unresolved issue is not scale alone. M17 still assumes all supplied relations are exact conjunctions. A harder successor should introduce partial/noisy/conflicting observations or relation uncertainty and test whether the fibre discipline can be generalized without collapsing back into heuristic nearest-match ranking.
