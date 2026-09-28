# PRINCIPIA V1/V2 FIRST FREEZE 01 — ERRATA 01

**Status:** `ACTIVE ERRATA / LOCAL THEOREM CORRECTION / NO CORE CHANGE`  
**Date:** 2026-09-29  
**Target:** C19-v2 / `CAT–FACT–NORM–MINI-01`  
**Corrected source:** `cat-fact-norm-mini-02.md`

## 1. Error

Freeze 01 retained the MINI statement that the restricted factorization fibre modulo declared gauge has cardinality one.

The source defined

\[
\mathfrak F^{0}_{FB,P}(Y)
=
\operatorname{RawFact}^{0}_{FB,P}(Y)/G_P
\]

but inferred from rewrite confluence that

\[
|\mathfrak F^{0}_{FB,P}(Y)|=1.
\]

This inference is invalid.

Confluence of a rewrite system establishes uniqueness of normal form modulo the rewrite/gauge setting. It does not imply that all pre-normal grammar terms are already equal under gauge alone.

## 2. Fixed witness

For any interior cut `a`, compare

\[
B_{[0,L]}
\]

with

\[
B_{[0,a]}\oplus B_{[a,L]}.
\]

They reconstruct the same regular curve and normalize to the same global Bishop class, but a constant `SO(2)` normal rotation does not remove the segmentation boundary.

Hence the two terms need not be equal in `RawFact/G`.

## 3. Correct theorem

Let

\[
\operatorname{NF}:
\mathfrak F^{0}_{FB,P}(Y)
\to
\mathcal N_{FB,P}(Y)
\]

be the normalization map induced by the terminating confluent rewrite.

Then the exact MINI theorem is

\[
\boxed{
|\operatorname{im}\operatorname{NF}|=1.
}
\]

Equivalently, for

\[
X\equiv_{NF}X'
\iff
\operatorname{NF}(X)=\operatorname{NF}(X'),
\]

\[
\boxed{
|\mathfrak F^{0}_{FB,P}(Y)/\!\equiv_{NF}|=1.
}
\]

This is normal-form/task identifiability, not literal factorization uniqueness modulo realization/presentation gauge.

## 4. What survives unchanged

The erratum does not affect:

- CORE5;
- C62/C63 canonical CAT/FACT definitions;
- the absolute-coordinate vs shape-contract gauge correction;
- termination of the `{F,B}` rewrite;
- local confluence and Newman confluence on legal gauge classes;
- uniqueness of the Bishop normal class;
- C20: Frenet failure at `kappa=0` while regular is recode/domain repair, not automatic catalog birth;
- F55/F56/F59;
- Agent v02.

## 5. Freeze impact

\[
\boxed{
\mathrm{FREEZE\ 01}
\text{ remains active subject to ERRATA 01.}
}
\]

This is a local theorem-scope correction, not a primitive/core reopening.
