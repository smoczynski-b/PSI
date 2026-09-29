# PRINCIPIA SEMANTICA — VOLUME III.7

## MOST — zadaniowa hierarchia informacji spektralnej i rezolwentowej

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Upstream:** `principia-v3-phisica-whole-crosscheck-01.md`, `regression-bank-01.md`  
**Historical sources:** `KANON2.txt` (MOS/P9 operator-nonnormality layer), earlier project usage of the label `MOST`  
**Scope:** finite-dimensional bounded operators for the exact hierarchy theorem; operator-valued/resolvent/semigroup extensions stated only at the level licensed below.

---

# 1. Source status and naming discipline

The physical source `KANON2.txt` clearly preserves the MOS/P9 distinction:

- spectrum alone is insufficient for nonnormal stability tasks;
- resolvent and semigroup information become relevant;
- the PSI↔MOS bridge is legal only after a concrete operator is specified.

The exact acronym expansion of the earlier label `MOST` is not currently source-bound strongly enough to promote an expansion to canon. Therefore `MOST` is retained here only as the established project label for the **operator-information layer**.

No new PSI primitive is introduced.

Permanent rule:

\[
\boxed{
\text{information hierarchy}
=\text{factorization order of representations},
\quad
\text{not a universal ranking of methods}.
}
\]

---

# 2. Finite-dimensional contract

Fix

\[
\mathcal H=\mathbb C^n
\]

with a fixed Hilbert norm and induced operator norm. Let

\[
\mathfrak A=M_n(\mathbb C).
\]

For

\[
A\in\mathfrak A
\]

define the spectral representation

\[
\boxed{
\rho_\sigma(A):=\sigma(A).
}
\]

Define the extended resolvent-norm profile

\[
\boxed{
r_A(z):=
\begin{cases}
\|(zI-A)^{-1}\|,&z\notin\sigma(A),\\
+\infty,&z\in\sigma(A).
\end{cases}
}
\]

and the representation

\[
\boxed{
\rho_r(A):=r_A(\cdot).
}
\]

For \(\varepsilon>0\), fix the pseudospectrum convention

\[
\boxed{
\sigma_\varepsilon(A)
:=
\{z\in\mathbb C:r_A(z)>\varepsilon^{-1}\}.
}
\]

The full pseudospectral representation is

\[
\boxed{
\rho_{ps}(A)
:=
\bigl(\sigma_\varepsilon(A)\bigr)_{\varepsilon>0}.
}
\]

---

# 3. Theorem III.7.A — resolvent-norm profile and full pseudospectrum are equivalent representations

## Theorem

With the convention above,

\[
\boxed{
\rho_r
\text{ and }
\rho_{ps}
\text{ factor through each other exactly}.
}
\]

Equivalently,

\[
\boxed{
\ker_{eq}\rho_r
=
\ker_{eq}\rho_{ps}.
}
\]

## Proof

From the profile \(r_A\), every pseudospectrum is recovered by the threshold rule

\[
\sigma_\varepsilon(A)
=
\{z:r_A(z)>\varepsilon^{-1}\}.
\]

Thus

\[
\rho_{ps}=F\circ\rho_r.
\]

Conversely, for fixed \(z\), define

\[
\varepsilon_*(z)
:=
\inf\{\varepsilon>0:z\in\sigma_\varepsilon(A)\}.
\]

If \(z\notin\sigma(A)\), then

\[
z\in\sigma_\varepsilon(A)
\iff
\varepsilon>r_A(z)^{-1},
\]

so

\[
\varepsilon_*(z)=r_A(z)^{-1}.
\]

If \(z\in\sigma(A)\), then \(z\in\sigma_\varepsilon(A)\) for every \(\varepsilon>0\), hence

\[
\varepsilon_*(z)=0
\]

and therefore, with \(1/0:=+\infty\),

\[
\boxed{
r_A(z)=\varepsilon_*(z)^{-1}.
}
\]

Thus

\[
\rho_r=G\circ\rho_{ps}.
\]

Hence the two representations have exactly the same kernel relation. \(\square\)

---

# 4. Corollary III.7.B — spectrum is a quotient of resolvent/pseudospectral information

Because

\[
\boxed{
\sigma(A)=\{z:r_A(z)=+\infty\}
}
\]

and equivalently

\[
\boxed{
\sigma(A)
=\bigcap_{\varepsilon>0}\sigma_\varepsilon(A),
}
\]

there exist factor maps

\[
\rho_\sigma
=f_r\circ\rho_r
\]

and

\[
\rho_\sigma
=f_{ps}\circ\rho_{ps}.
\]

Therefore

\[
\boxed{
\ker_{eq}\rho_r
=
\ker_{eq}\rho_{ps}
\subseteq
\ker_{eq}\rho_\sigma.
}
\]

In the information order used throughout PSI, resolvent-norm/pseudospectral information is at least as fine as spectral information.

This is an exact factorization statement, not an evaluative ranking.

---

# 5. Strictness — HCube regression

Regression Bank R01 supplies

\[
A=\operatorname{diag}(2,1,0),
\]

\[
B=
\begin{pmatrix}
2&0&0\\
0&1&1\\
0&0&0
\end{pmatrix}.
\]

They satisfy

\[
\chi_A=\chi_B,
\qquad
\|A\|_2=\|B\|_2=2,
\]

hence in particular

\[
\rho_\sigma(A)=\rho_\sigma(B).
\]

But

\[
\left\|\left(\frac12I-A\right)^{-1}\right\|_2
=2,
\]

while

\[
\left\|\left(\frac12I-B\right)^{-1}\right\|_2
=2(1+\sqrt2).
\]

Therefore

\[
\boxed{
\ker_{eq}(\rho_\sigma,\|\cdot\|_2)
\not\subseteq
\ker_{eq}R_{1/2},
}
\]

where

\[
R_{1/2}(X)
=
\left\|\left(\frac12I-X\right)^{-1}\right\|_2.
\]

Hence even

\[
\boxed{
\text{spectrum + operator norm}
}
\]

is not sufficient for this resolvent-sensitive task.

This proves that the passage

\[
\rho_r\to\rho_\sigma
\]

can be genuinely information-losing for a legal task.

HCube remains a separator, not a universal representation prescription.

---

# 6. Operator-valued resolvent — a finer layer

For every legal resolvent point define

\[
\boxed{
\mathcal R_A(z):=(zI-A)^{-1}.
}
\]

Pointwise,

\[
\boxed{
r_A(z)=\|\mathcal R_A(z)\|.
}
\]

Thus the scalar resolvent-norm profile factors through the operator-valued resolvent:

\[
\boxed{
\mathcal R_A(\cdot)
\longrightarrow
r_A(\cdot)
\longleftrightarrow
\{\sigma_\varepsilon(A)\}_{\varepsilon>0}
\longrightarrow
\sigma(A).
}
\]

Whenever a fixed \(z_0\) lies in the resolvent of every operator in the declared candidate class,

\[
\boxed{
A=z_0I-\mathcal R_A(z_0)^{-1}.
}
\]

Hence the full operator-valued resolvent at one common legal point is faithful on that class.

This does **not** imply that its norm is faithful, nor that a basis-sensitive task may quotient by unitary similarity unless the contract declares that similarity as gauge.

## Directional witness III.7-X2

Fix the standard basis of \(\mathbb C^2\), do **not** quotient by unitary change of basis, and set

\[
A=\operatorname{diag}(0,1),
\qquad
B=\operatorname{diag}(1,0).
\]

The two matrices are unitarily similar, so for every legal \(z\),

\[
\boxed{
r_A(z)=r_B(z).}
\]

Thus

\[
\rho_r(A)=\rho_r(B)
\]

and likewise their full pseudospectral families agree.

However, at \(z=2\),

\[
(2I-A)^{-1}=\operatorname{diag}(1/2,1),
\]

\[
(2I-B)^{-1}=\operatorname{diag}(1,1/2).
\]

For the basis-sensitive task

\[
T(X):=\langle e_1,(2I-X)^{-1}e_1\rangle,
\]

we get

\[
\boxed{T(A)=1/2,\qquad T(B)=1.}
\]

Therefore

\[
\boxed{
\ker_{eq}\rho_r
\not\subseteq
\ker_{eq}T
}
\]

for this declared contract.

This witness is intentionally contract-relative. If unitary similarity is declared gauge and the task is required to be gauge-invariant, the task above is not legal on the quotient. Thus the example does not privilege basis-sensitive information universally; it proves only that scalar resolvent norms can lose directional information.

---

# 7. Semigroup / transient-growth branch

For a matrix \(A\), define

\[
S_A(t):=e^{tA},
\qquad
g_A(t):=\|e^{tA}\|,
\qquad t\ge0.
\]

The source layer MOS/P9 explicitly warns that for nonnormal stability one must investigate resolvent and semigroup behaviour rather than spectrum alone.

III.7 does **not** assert a universal factorization

\[
r_A(\cdot)
\leftrightarrow
g_A(\cdot).
\]

The canonical information diagram is therefore branched:

\[
\boxed{
A
\longrightarrow
\mathcal R_A(\cdot)
\longrightarrow
r_A(\cdot)
\longleftrightarrow
\rho_{ps}(A)
\longrightarrow
\rho_\sigma(A),
}
\]

and separately

\[
\boxed{
A
\longrightarrow
S_A(\cdot)
\longrightarrow
g_A(\cdot).
}
\]

Any arrow between scalar resolvent and scalar semigroup summaries requires an additional theorem and contract. It is not inserted by analogy.

Permanent boundary:

\[
\boxed{
\text{resolvent-sensitive adequacy}
\neq
\text{automatic transient-growth adequacy}.
}
\]

---

# 8. Task-relative MOST criterion

Let

\[
\rho:\mathfrak A\to Z
\]

be any operator representation. For a declared task \(\mathcal T\), exact legality remains the existing PSI condition

\[
\boxed{
\ker_{eq}\rho
\subseteq
E_{\mathcal T}.
}
\]

Thus:

### Spectral task

If every task observable factors through \(\rho_\sigma\), the spectrum may be sufficient.

### Resolvent-norm / pseudospectral task

If the task contains

\[
A\mapsto r_A(z_0)
\]

or an \(\varepsilon\)-pseudospectral query, \(\rho_\sigma\) must be tested and can fail; HCube gives an explicit failure.

### Operator-response task

If the task depends on directional/vector-valued information in

\[
(zI-A)^{-1},
\]

the scalar norm profile must itself be tested; III.7-X2 gives an explicit failure in a basis-sensitive contract.

### Transient-growth task

If the task contains

\[
A\mapsto \|e^{tA}\|,
\]

the semigroup representation must be tested directly; spectrum-only adequacy is not assumed.

Therefore MOST is not one representation. It is the task-controlled rule

\[
\boxed{
\text{choose the coarsest representation whose kernel still lies inside }E_{\mathcal T}.
}
\]

This is exactly II.4/II.5 applied to operator-information representations.

---

# 9. Relation to self-adjoint PHISICA

For the self-adjoint regular PHISICA sector III.1–III.6, spectral data can be much more informative than in the nonnormal sector. Nevertheless III.7 does not promote

\[
\{E_n\}
\]

to a complete model identifier.

The distinction remains:

\[
\boxed{
\text{spectrum as invariant}
\neq
\text{spectrum as task-sufficient representation}.
}
\]

III.7 therefore connects the repaired PHISICA operator block to the broader operator-information problem without reopening any withdrawn historical DNA claim.

---

# 10. Relation to MOS source material

The historical/project MOS layer retains concrete operator objects such as

\[
P_h,
\qquad
R_h(z)=(P_h-z)^{-1},
\qquad
\operatorname{Res}(P_h),
\]

and explicitly states that spectrum alone is insufficient for nonnormal stability, where resolvent and semigroup estimates matter.

III.7 imports only this typed operator-information lesson.

It does **not** import as theorem:

- the broad semantic analogies `resolvent = propagator sensu`;
- a global MOS composition theorem;
- a universal Hessian-to-Kreiss bridge;
- any claim that the microlocal MOS calculus is already globally closed.

Those statuses remain historical/open according to the source audit.

---

# 11. Local cross-check

### Types
`PASS`: spectrum, resolvent norm, pseudospectrum, operator-valued resolvent and semigroup profiles have explicit codomains/roles.

### Factorization
`PASS`: \(\rho_r\leftrightarrow\rho_{ps}\to\rho_\sigma\) is proved under a fixed norm and explicit pseudospectrum convention.

### Strictness I
`PASS`: Regression Bank R01 / HCube shows spectrum+norm can fail a resolvent task.

### Strictness II
`PASS`: III.7-X2 shows the full scalar resolvent-norm profile can fail a directional resolvent task when basis/unitary equivalence is not gauge.

### Gauge discipline
`PASS`: III.7-X2 is explicitly contract-relative and is not legal after quotienting by unitary similarity unless the task descends to that quotient.

### No total-order inflation
`PASS`: no unproved scalar resolvent-to-semigroup factorization is asserted.

### PSI bind
`PASS`: the controlling criterion is the existing

\[
\ker_{eq}\rho\subseteq E_{\mathcal T}.
\]

### Source discipline
`PASS`: MOS operator content is separated from old semantic analogy and from the unresolved microlocal/global composition program.

---

# 12. Verdict

\[
\boxed{
\mathrm{III.7\ MOST}
=
\mathrm{PROOF\ PASS / LOCAL\ CROSS\!\!-\!CHECK\ PASS}.
}
\]

The next legal unit is the fixed regression/laboratory:

\[
\boxed{
\mathrm{III.8\ —\ HCUBE\ NONNORMAL/RESOLVENT\ LAB}.
}
\]

III.8 must not merely repeat the two matrix calculations. Its job is to embed HCube into the III.7 factorization diagram and determine exactly which representation levels pass or fail which declared tasks.