# PSI — falsifier registry 11

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-10.md` as current public registry.  
**Reason:** add the permanent regression exposed by the first classical Markov-lumpability bridge.

Retain F01–F60 from v10 without semantic change.

---

## F61 — task quotient / Markov lumpability conflation

**TARGET:** any inference of the form

\[
\text{a partition/quotient is exact for the declared task}
\Longrightarrow
\text{the quotient carries an autonomous Markov dynamics}
\]

without checking block-transition stability.

For a finite Markov chain with transition matrix `P`, equivalence relation `E`, quotient `S/E` and a block `C`, define

\[
P(x,C)=\sum_{z\in C}P(x,z).
\]

**ORACLE:** strong/Kemeny–Snell lumpability requires

\[
\boxed{
 xEy
 \Longrightarrow
 P(x,C)=P(y,C)
 \quad\forall C\in S/E.
}
\]

Task adequacy and stochastic projectability are distinct gates.

### Fixed witness

Let

\[
S=\{a,b,c\},
\qquad
E=\{\{a,b\},\{c\}\},
\]

and

\[
P(a,a)=1,
\qquad
P(b,c)=1,
\qquad
P(c,c)=1.
\]

For the block `A={a,b}`:

\[
P(a,A)=1,
\qquad
P(b,A)=0.
\]

Thus `aEb` may be legal for a static task that does not distinguish `a` from `b`, while the partition is not lumpable.

**VERDICT:**

\[
\boxed{
\text{task quotient}
\not\Rightarrow
\text{Markov lumpability}.
}
\]

**REPAIR:** either add the block-transition stability condition, or refine/change the task/contract so that the dynamically relevant distinction is retained.

**REGRESSION:** `principia-v2-10-strong-lumpability-bridge.md`, §7.

---

## PASS inflation rule

Every run report must contain both:

`WHAT FAILED / PASSED`

and

`WHAT THIS RESULT DOES NOT TEST`.

## Promotion gate

A non-classical claim may move toward stable theorem status only after

\[
\boxed{\text{typed hypotheses}+\text{proof/test}+\text{real falsifier}+\text{oracle}+\text{scope}.}
\]

For classical theorems, proof and provenance take precedence over manufactured pseudo-falsification.
