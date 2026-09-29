# PSI-MEMORY-M16-LANGUAGE-FIBRE-01

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can a language adapter return a candidate fibre rather than a single concept, while task/world relations monotonically refine that fibre until identification is licensed?

M16 reuses the frozen M15 lexical and world fixtures. It adds no PSI primitive.

## 1. Fibre update law

For language \(L\), lexical surface \(s\), and world relation constraint \((r_k,o_k)\), define

\[
F_0=\operatorname{Lex}_L(s)
\]

and

\[
\boxed{
F_{k+1}=F_k\cap\{x:(x,r_k,o_k)\in W\}.
}
\]

Therefore

\[
\boxed{F_{k+1}\subseteq F_k.}
\]

A relational refinement may preserve or reduce a candidate fibre, but may never enlarge it.

## 2. Status semantics

\[
|F|>1\Rightarrow\mathrm{UNRESOLVED},
\]

\[
|F|=1\Rightarrow\mathrm{IDENTIFIED},
\]

\[
F=\varnothing\Rightarrow\mathrm{INCONSISTENT}.
\]

An unknown lexical surface has the separate status `NO_LEXICAL_FIBRE`; it is not treated as an inconsistent known fibre.

## 3. Frozen witnesses

### M16-A — non-discriminating relation

For German `Uhr`:

\[
F_0=\{OBJ\!\!-
WRIST,OBJ\!\!-
WALL\}.
\]

Both satisfy `MEASURES -> TIME`, hence

\[
|F_0|=2\to|F_1|=2.
\]

The ambiguity must remain unresolved.

### M16-B — discriminating relation

Add `ATTACHED_TO -> WRIST`:

\[
2\to2\to1,
\]

with final fibre

\[
\{OBJ\!\!-
WRIST\}.
\]

### M16-C — order invariance

Applying the two conjunctive relational constraints in reverse order must produce the same final fibre.

### M16-D — cross-language convergence

PL `zegarek`, EN `watch`, and DE `Uhr` may begin with different fibre widths, but under the same discriminating relational constraints they must converge to the same world object when the evidence supports it.

### M16-E — inconsistency

PL `zegarek` constrained by `ATTACHED_TO -> WALL` yields the empty fibre. The resolver must not substitute the closest candidate or another lexical label.

Once empty, later conjunctive constraints cannot resurrect a candidate.

## 4. Success predicate

M16 passes iff all tested refinements satisfy monotone narrowing, non-discriminating relations preserve ambiguity, discriminating relations can identify, final conjunction is order-invariant, cross-language fibres can converge relationally, contradictions remain empty, and unknown lexical surfaces remain distinct from inconsistent known fibres.

## 5. Boundary

M16 operates on frozen candidate fibres and frozen world relations. It does not infer either from raw perception or unrestricted natural language. It demonstrates the PSI mechanism for language-relative candidate fibres once the observation/adapter layer has supplied them.
