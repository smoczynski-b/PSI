# PRINCIPIA SEMANTICA — CAT/FACT/NORM CROSS-CHECK 01

**Status:** `GLOBAL PASS AFTER REQUIRED ERRATA / FREEZE 01 ERRATA 01 ACTIVE`  
**Date:** 2026-09-29  
**Scope:** II.13–II.14, C62/C63/C66, C19-v3/C20/C67, F55/F56/F58/F59/F62.  
**Corrected source:** `cat-fact-norm-mini-02.md`.

---

## 1. Audit question

The block is accepted only if it preserves all of the following distinctions:

\[
\text{PSI-ID}
\neq
\text{PSI-CAT},
\]

\[
\text{realization gauge}
\neq
\text{recode/normalization},
\]

\[
\text{gauge-only factorization candidate space}
\neq
\text{normal-form task quotient},
\]

and

\[
\text{current canonical FACT}
\neq
\text{universal homotopy/groupoid FACT}.
\]

---

## 2. Defect found during cross-check

The previous MINI source defined

\[
\mathfrak F(Y)=\operatorname{RawFact}(Y)/G
\]

but inferred from rewrite confluence that

\[
|\mathfrak F(Y)|=1.
\]

This was false in general.

A fixed witness is

\[
B_{[0,L]}
\quad\text{versus}\quad
B_{[0,a]}\oplus B_{[a,L]}.
\]

A legal constant normal-frame gauge does not remove a segmentation boundary. The two terms may therefore be distinct in the gauge-only candidate fibre even though both normalize to the same global Bishop class.

This is now F62.

---

## 3. Corrected architecture

The block now has three levels.

### Level A — factorization candidates modulo legal gauge

\[
\boxed{
\mathfrak F^{0}_{FB,P}(Y)
=
\operatorname{RawFact}^{0}_{FB,P}(Y)/G_P.
}
\]

This space may contain many factorization classes.

### Level B — normalization

The terminating confluent rewrite induces

\[
\boxed{
\operatorname{NF}:
\mathfrak F^{0}_{FB,P}(Y)
\to
\mathcal N_{FB,P}(Y).
}
\]

For the exact interval MINI:

\[
\boxed{
|\operatorname{im}\operatorname{NF}|=1.
}
\]

### Level C — task quotient by normal form

\[
X\equiv_{NF}X'
\iff
\operatorname{NF}(X)=\operatorname{NF}(X').
\]

Then

\[
\boxed{
|\mathfrak F^{0}_{FB,P}(Y)/\!\equiv_{NF}|=1.
}
\]

This is the exact task-level identifiability result.

---

## 4. Relation to canonical PSI-FACT

C63 defines general PSI-FACT as the fibre of factorization candidates satisfying domain admissibility, external interface and data compatibility, modulo realization equivalence only when established by the contract.

The corrected MINI now respects this role exactly:

- gauge removes presentation/realization equivalence;
- recode/merge remain normalization operations;
- normal-form equality defines an additional task equivalence when the task asks only for the normalized class.

Therefore II.14 no longer silently inserts rewrite equivalence into the realization gauge.

---

## 5. Status of older structured FACT

C66 remains unchanged.

Factorization groupoids, stabilizers and homotopy/weak compatibility fibres remain derived structured extensions when task-relevant. MINI-02 neither requires them nor rules them out.

F59 remains satisfied.

---

## 6. Status of CAT result

C20 survives unchanged:

\[
\kappa=0
\text{ with regular }\gamma
\Rightarrow
\text{Frenet-domain failure can be repaired by Bishop recode}.
\]

No catalog birth follows automatically.

The correction concerns factorization uniqueness, not the recode/birth distinction.

---

## 7. Regressions

### F55
`PASS`: absolute-coordinate and shape gauges remain separated.

### F56
`PASS`: rewrite is defined on gauge classes before confluence is invoked.

### F58
`PASS`: old CAT/FACT apparatus remains derived.

### F59
`PASS`: MINI remains a restricted grammar benchmark, not general FACT.

### F62
`PASS`: singleton claim is now attached only to normalization image/task quotient.

---

## 8. Freeze impact

The defect changes a frozen theorem statement C19-v2, so pretending `NO FREEZE ERRATA` would be incorrect.

Therefore:

\[
\boxed{
\mathrm{FREEZE\ 01\ ERRATA\ 01}=\mathrm{ACTIVE}.
}
\]

The impact is local:

- C19-v2 withdrawn;
- C19-v3 active;
- C67 added;
- F62 added;
- CORE5 unchanged;
- C62/C63 unchanged;
- Agent v02 unchanged.

---

## 9. Global verdict

After the correction:

\[
\boxed{
\mathrm{II.13:II.14\ CAT/FACT/NORM}
=\mathrm{GLOBAL\ PASS\ AFTER\ ERRATA\ 01}.
}
\]

The next legal layer is FRAME C22–C24.
