# PSI-MEMORY-M16-RESULT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36633040607` executed M1–M16 successfully.

M16 promotes the M15 lexical candidate set from a demonstration fixture to an explicit working fibre updated by world-relation constraints.

The update law is:

\[
\boxed{
F_0=\operatorname{Lex}_L(s),
\qquad
F_{k+1}=F_k\cap\operatorname{Supp}(r_k,o_k)
}
\]

where

\[
\operatorname{Supp}(r,o)=\{x:(x,r,o)\in W\}.
\]

Therefore every legal refinement satisfies

\[
\boxed{F_{k+1}\subseteq F_k.}
\]

## 2. Identification states

The resolver uses three fibre states:

\[
|F|>1\Rightarrow\mathrm{UNRESOLVED},
\]

\[
|F|=1\Rightarrow\mathrm{IDENTIFIED},
\]

\[
F=\varnothing\Rightarrow\mathrm{INCONSISTENT}.
\]

An absent lexical entry is kept separate as `NO_LEXICAL_FIBRE`.

This prevents the system from conflating lack of a language adapter/lexical candidate set with contradiction between a known lexical fibre and world evidence.

## 3. German `Uhr` witness

Initial fibre:

\[
F_0=\{OBJ\!\!-
WRIST,OBJ\!\!-
WALL\}.
\]

The relation

\[
x\xrightarrow{MEASURES}TIME
\]

is satisfied by both candidates, hence

\[
\boxed{2\to2}
\]

and the status remains `UNRESOLVED`.

Adding

\[
x\xrightarrow{ATTACHED\_TO}WRIST
\]

gives

\[
\boxed{2\to2\to1}
\]

with final fibre

\[
\boxed{F=\{OBJ\!\!-
WRIST\}}.
\]

Identification therefore occurs only after a relation actually separates the candidates.

## 4. Conjunctive order invariance

For the frozen world relation fixture, reversing the order of

- `MEASURES -> TIME`;
- `ATTACHED_TO -> WRIST`

produces the same final fibre.

This follows operationally from conjunctive set intersection on the witness:

\[
F_0\cap S_1\cap S_2
=
F_0\cap S_2\cap S_1.
\]

The trace may differ, but the final admissible candidate set does not.

## 5. Cross-language convergence

PL `zegarek`, EN `watch`, and DE `Uhr` begin with different lexical fibre widths, but under the same discriminating relational evidence they converge to

\[
\boxed{OBJ\!\!-
WRIST}.
\]

Thus equality of lexical extensions is not required for equality of the finally identified world object.

The operational invariant is relational identification, not word identity.

## 6. Contradiction and no resurrection

PL `zegarek` begins with

\[
F_0=\{OBJ\!\!-
WRIST\}.
\]

Applying the incompatible constraint

\[
ATTACHED\_TO\to WALL
\]

yields

\[
\boxed{1\to0}
\]

and status `INCONSISTENT`.

The resolver performs no nearest-match, synonym substitution or lexical fallback.

Adding another conjunctive relation afterwards gives

\[
\boxed{1\to0\to0}.
\]

Hence an excluded candidate cannot be resurrected by later evidence under the same frozen conjunction contract.

## 7. Architectural consequence

M16 makes the language interface explicitly fibre-valued:

\[
\boxed{
\lambda_L:s\mapsto F_L(s)\subseteq W.
}
\]

The world relation layer then acts by monotone refinement:

\[
\boxed{
F\mapsto F\cap S_{r,o}.
}
\]

This is a direct realization of the existing PSI discipline:

- observation supplies a compatible candidate fibre;
- additional task-relevant relations refine that fibre;
- exact identification is legal only at singleton fibre;
- an empty fibre signals incompatibility rather than a forced answer.

M16 therefore adds no new PSI primitive.

## 8. Boundary

The candidate fibres and world relations are still frozen fixtures. M16 does not infer them from raw perception, unrestricted language, embeddings or a learned ontology.

The demonstrated result is narrower:

\[
\boxed{
\text{given a language-relative candidate fibre and relational world evidence, PSI refinement is monotone, fail-closed and language-scope tolerant.}
}
\]

A next useful test would replace the toy two-object world with a larger relational domain containing several overlapping lexical partitions and several independent discriminating/non-discriminating relation families, then measure whether the same fibre law remains stable under composition and partial evidence.
