# PRINCIPIA V2 OWN-LAYER CROSS-CHECK 02 — ERRATA 01

**Status:** `CONTROL-GRAPH ERRATA / NO MATHEMATICAL VERDICT CHANGE`  
**Date:** 2026-09-29  
**Applies to:** `principia-v2-own-layer-crosscheck-02.md`, dependency classification for II.9.

## 1. What the Six audit got right

The audit correctly found that II.9 does **not** require II.8 as a proof prerequisite. II.7 already defines

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}
\]

and the quotient map. II.8 adds the coarsest-quotient theorem, not the existence needed by II.9.

It also correctly classified II.6 as structural analogy rather than an indispensable proof step.

## 2. Remaining overdependency

The audit wrote, in effect,

\[
\text{STRICT PROOF DEPENDENCY}=II.7+C59.
\]

This is still too broad and is potentially self-referential because II.9 is precisely the prose/proof migration of the registered results C45 and C59.

C59 is therefore a **source/result claim identifier**, not a theorem that should be listed as a prior proof dependency of the unit proving/migrating it.

## 3. Correct classification

The corrected graph is

\[
\boxed{
\text{SOURCE / RESULT IDS}=C45+C59,
}
\]

\[
\boxed{
\text{STRICT PROOF DEPENDENCY}=II.7\;(C57/C58)
+\text{typed legal-extension definitions},
}
\]

\[
\boxed{
II.6=\text{STRUCTURAL ANALOGY},
\qquad
II.8=\text{NOT A PROOF PREREQUISITE}.
}
\]

The two congruence properties are rederived inside II.9 from the literal-label-preserving future-tree isomorphism:

\[
(H,\varepsilon,y)\in D_t
\iff
(H',\varepsilon,y)\in D_t,
\]

and

\[
\delta_t(H,\varepsilon,y)
\equiv_{\mathcal T,t+1}
\delta_t(H',\varepsilon,y).
\]

## 4. Impact

- mathematical statement II.9: unchanged;
- C45/C59 status: unchanged;
- Freeze 01: no erratum;
- CORE5: unchanged;
- Agent v02: unchanged;
- only dependency/source classification changes.

## 5. Verdict

\[
\boxed{
\mathrm{SIX\ HANDOFF\ VERDICT}
=\mathrm{MATHEMATICALLY\ VALID}
\;\text{with this dependency-graph erratum}.
}
\]
