# PSI — falsifier registry 07

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-06.md` as current public registry.

Retain F01–F33 from v06 without semantic change.

---

## F34 — spectrum-plus-norm sufficiency

**TARGET:** any claim that

\[
\rho_0(A)=(\chi_A,\|A\|_2)
\]

is sufficient for resolvent-sensitive tasks.

**FIXED WITNESS:**

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=\begin{pmatrix}2&0&0\\0&1&1\\0&0&0\end{pmatrix}.
\]

**ORACLE:** compare

\[
R_{1/2}(X)=\left\|\left(\tfrac12I-X\right)^{-1}\right\|_2.
\]

**VERDICT:**

\[
R_{1/2}(A)=2,
\qquad
R_{1/2}(B)=2(1+\sqrt2).
\]

Hence

\[
\ker\rho_0\not\subseteq\ker R_{1/2}.
\]

**REGRESSION:** YES.

---

## F35 — HCube inflation

**TARGET:** any inference

\[
\text{HCube separates one nonnormal pair}
\Rightarrow
\text{HCube is necessary/minimal/universal or a CORE primitive}.
\]

**ORACLE:** check whether the declared task is already separated by another legal observable/representation and whether any new semantic role is actually required.

**CURRENT VERDICT:** prohibited. In the fixed pair the ordinary resolvent already separates the task exactly.

---

## F36 — P9/HCube conflation

**TARGET:** any derivation identifying state amplification

\[
x\mapsto e^{tA}x
\]

with similarity-action conditioning

\[
X\mapsto e^{tA}Xe^{-tA}.
\]

**ORACLE:** type/domain audit and comparison of the actual observables used.

**VERDICT:** bridge does not imply identity of tasks.

**REGRESSION:** YES.

---

## F37 — norm/metric substitution

**TARGET:** comparison of pseudospectral, numerical-abscissa or HCube quantities computed in inconsistent geometries.

**FALSIFIER:** the declared norm/metric changes between compared diagnostics without lawful transport.

**ORACLE:** `METRIC-ID -> P10 -> P9/HCube` discipline.

**VERDICT:** comparison invalid until geometry is aligned.

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