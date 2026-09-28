# PSI — falsifier registry 12

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-11.md` as current public registry.

Retain F01–F61 from v11 without semantic change.

---

## F62 — normal-form uniqueness / factorization-fibre singleton conflation

**TARGET:** any inference of the form

\[
\text{rewrite terminates and is confluent modulo gauge}
\Rightarrow
|\operatorname{RawFact}(Y)/G|=1.
\]

**FALSIFIER:** choose a regular interval curve admitting a Bishop representation and an interior cut `a`. Then

\[
B_{[0,L]}
\]

and

\[
B_{[0,a]}\oplus B_{[a,L]}
\]

are distinct grammar factorizations. A constant legal gauge rotation does not remove the segmentation boundary, so they need not be equal in the gauge-only quotient.

Nevertheless both reduce to the same Bishop normal class.

**ORACLE:** distinguish three objects:

1. raw grammar factorizations;
2. gauge-only factorization candidate classes;
3. task/normal-form quotient induced by equality of normal form.

Confluence licenses

\[
|\operatorname{im}\operatorname{NF}|=1
\]

or equivalently

\[
|\mathfrak F(Y)/\!\equiv_{NF}|=1,
\]

not literal singleton cardinality of `RawFact/G`.

**FIXED APPLICATION:** `cat-fact-norm-mini-02.md`, Freeze 01 Errata 01, C19-v3.

**REGRESSION:** YES.

---

## PASS inflation rule

Every run report must contain both:

`WHAT FAILED / PASSED`

and

`WHAT THIS RESULT DOES NOT TEST`.
