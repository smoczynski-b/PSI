# PRINCIPIA SEMANTICA — VOLUME III.8

## HCube — laboratorium nienormalności, rezolwenty i adekwatności reprezentacji

**Status:** `LAB PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Upstream:** `principia-v3-07-spectral-information-hierarchy-most.md`, `regression-bank-01.md`  
**Scope:** frozen two-point HCube catalog; finite-dimensional Euclidean operator norm.

---

# 1. Purpose

III.8 does not introduce a new witness. It upgrades Regression Bank R01 into a full MOST laboratory.

The frozen candidate catalog is

\[
\boxed{\Omega_H=\{A,B\}}
\]

with

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=
\begin{pmatrix}
2&0&0\\
0&1&1\\
0&0&0
\end{pmatrix}.
\]

The question is not merely whether `A` and `B` differ. It is:

\[
\boxed{
\text{for which declared tasks does a given representation preserve every required distinction?}
}
\]

The controlling criterion is unchanged:

\[
\boxed{
\ker_{eq}\rho|_{\Omega_H}\subseteq E_{\mathcal T}|_{\Omega_H}.
}
\]

---

# 2. Frozen facts

Regression R01 gives

\[
\chi_A=\chi_B,
\qquad
\sigma(A)=\sigma(B)=\{0,1,2\},
\]

\[
\|A\|_2=\|B\|_2=2,
\]

but at

\[
z_0=\frac12
\]

one has

\[
\boxed{
r_A(z_0)=2}
\]

and

\[
\boxed{
r_B(z_0)=2(1+\sqrt2)}.
\]

Thus the scalar resolvent-norm profile and the full pseudospectral family distinguish the two candidates, while spectrum and spectrum-plus-operator-norm do not.

For the pseudospectral membership task choose

\[
\varepsilon_0=\frac13.
\]

Then

\[
\varepsilon_0^{-1}=3,
\]

so

\[
\frac12\notin\sigma_{1/3}(A)
\]

because \(2<3\), while

\[
\frac12\in\sigma_{1/3}(B)
\]

because

\[
2(1+\sqrt2)>3.
\]

Hence the pseudospectral distinction is explicit at one legal threshold.

---

# 3. Semigroup-norm profile of the same HCube pair

The HCube pair also yields a nontrivial fact about the second III.7 branch.

For

\[
A=\operatorname{diag}(2,1,0),
\]

\[
\boxed{
\|e^{tA}\|_2=e^{2t}
\qquad(t\ge0).
}
\]

Write

\[
B=2\oplus C,
\qquad
C=
\begin{pmatrix}
1&1\\
0&0
\end{pmatrix}.
\]

For the Euclidean logarithmic norm,

\[
\mu_2(C)
=
\lambda_{\max}\!\left(\frac{C+C^*}{2}\right)
=
\frac{1+\sqrt2}{2}
<2.
\]

Indeed, for \(x(t)=e^{tC}x_0\),

\[
\frac d{dt}\|x(t)\|_2^2
=
2\operatorname{Re}\langle x(t),Cx(t)\rangle
\le
2\mu_2(C)\|x(t)\|_2^2.
\]

By Gronwall,

\[
\|e^{tC}\|_2
\le
 e^{\mu_2(C)t}.
\]

Therefore for \(t>0\),

\[
\|e^{tC}\|_2<e^{2t},
\]

and at \(t=0\) both terms equal \(1\). Since

\[
e^{tB}=e^{2t}\oplus e^{tC},
\]

we obtain

\[
\boxed{
\|e^{tB}\|_2=e^{2t}=\|e^{tA}\|_2
\qquad\forall t\ge0.
}
\]

Thus

\[
\boxed{
\rho_g(A)=\rho_g(B)
}
\]

for

\[
\rho_g(X):=\bigl(t\mapsto\|e^{tX}\|_2\bigr).
\]

Yet

\[
\rho_r(A)\neq\rho_r(B).
\]

Consequently there cannot exist a universal factor map on all matrices

\[
\boxed{
\rho_r=F\circ\rho_g.
}
\]

The scalar semigroup-norm profile does not determine the scalar resolvent-norm profile.

This proves one missing direction in the branched diagram of III.7. III.8 does not prove or assume the converse non-factorization.

---

# 4. Representation levels tested

On \(\Omega_H\), consider:

\[
\rho_\emptyset(X)=*,
\]

\[
\rho_\sigma(X)=\sigma(X),
\]

\[
\rho_{\sigma N}(X)=\bigl(\sigma(X),\|X\|_2\bigr),
\]

\[
\rho_g(X)=\bigl(t\mapsto\|e^{tX}\|_2\bigr),
\]

\[
\rho_r(X)=\bigl(z\mapsto r_X(z)\bigr),
\]

\[
\rho_{ps}(X)=\bigl(\sigma_\varepsilon(X)\bigr)_{\varepsilon>0},
\]

\[
\rho_{\mathcal R}(X)=\bigl(z\mapsto(zI-X)^{-1}\bigr),
\]

and

\[
\rho_S(X)=\bigl(t\mapsto e^{tX}\bigr).
\]

On the frozen pair:

\[
\rho_\emptyset(A)=\rho_\emptyset(B),
\]

\[
\rho_\sigma(A)=\rho_\sigma(B),
\]

\[
\rho_{\sigma N}(A)=\rho_{\sigma N}(B),
\]

\[
\rho_g(A)=\rho_g(B),
\]

while

\[
\rho_r(A)\neq\rho_r(B),
\qquad
\rho_{ps}(A)\neq\rho_{ps}(B),
\]

and, since the full operator-valued resolvent and full semigroup determine the generator in finite dimension,

\[
\rho_{\mathcal R}(A)\neq\rho_{\mathcal R}(B),
\qquad
\rho_S(A)\neq\rho_S(B).
\]

---

# 5. Declared HCube tasks

Define the following task observables on \(\Omega_H\).

### T1 — spectral task

\[
T_\sigma(X):=\sigma(X).
\]

Since

\[
T_\sigma(A)=T_\sigma(B),
\]

this task does not require separating the pair.

### T2 — operator-norm task

\[
T_N(X):=\|X\|_2.
\]

Again

\[
T_N(A)=T_N(B)=2.
\]

### T3 — resolvent task

\[
T_R(X):=
\left\|\left(\frac12I-X\right)^{-1}\right\|_2.
\]

Then

\[
T_R(A)\neq T_R(B).
\]

### T4 — pseudospectral-membership task

\[
T_{ps}(X):=
\mathbf 1_{\{1/2\in\sigma_{1/3}(X)\}}.
\]

Then

\[
T_{ps}(A)=0,
\qquad
T_{ps}(B)=1.
\]

### T5 — scalar transient-growth task

\[
T_g(X):=\bigl(t\mapsto\|e^{tX}\|_2\bigr).
\]

For the frozen pair,

\[
T_g(A)=T_g(B)=\bigl(t\mapsto e^{2t}\bigr).
\]

### T6 — exact candidate identity on the frozen catalog

\[
T_{id}(A)=A,
\qquad
T_{id}(B)=B.
\]

This is a deliberately maximal two-point task. It is included only to expose catalog-relative sufficiency: on a two-point catalog any representation that separates the pair is sufficient for `T_id`, even if it is not globally faithful on \(M_3(\mathbb C)\).

---

# 6. PASS/FAIL matrix

For a representation \(\rho\) and task \(T\), `PASS` means exactly

\[
\ker_{eq}\rho|_{\Omega_H}
\subseteq
\ker_{eq}T|_{\Omega_H}.
\]

`PASS*` is still a mathematical PASS, but the task is constant on the frozen pair, so the result is non-discriminating and gives no evidence of global sufficiency.

| representation | \(T_\sigma\) | \(T_N\) | \(T_R\) | \(T_{ps}\) | \(T_g\) | \(T_{id}\) |
|---|---|---|---|---|---|---|
| \(\rho_\emptyset\) | PASS* | PASS* | FAIL | FAIL | PASS* | FAIL |
| \(\rho_\sigma\) | PASS* | PASS* | FAIL | FAIL | PASS* | FAIL |
| \(\rho_{\sigma N}\) | PASS* | PASS* | FAIL | FAIL | PASS* | FAIL |
| \(\rho_g\) | PASS* | PASS* | FAIL | FAIL | PASS* | FAIL |
| \(\rho_r\) | PASS | PASS | PASS | PASS | PASS | PASS |
| \(\rho_{ps}\) | PASS | PASS | PASS | PASS | PASS | PASS |
| \(\rho_{\mathcal R}\) | PASS | PASS | PASS | PASS | PASS | PASS |
| \(\rho_S\) | PASS | PASS | PASS | PASS | PASS | PASS |

The last four rows must be read **only on the frozen two-point catalog**. For example, `rho_r` passes `T_id` here because it separates `A` and `B`; III.7-X2 already proves that the scalar resolvent-norm profile is not globally faithful for basis-sensitive operator tasks.

Likewise the `PASS*` entries for \(T_g\) do not imply that spectrum or a constant representation is generally adequate for transient-growth tasks. They mean only that the HCube pair happens to have the same scalar semigroup-norm profile.

---

# 7. What HCube now proves

The laboratory yields four distinct conclusions.

## H1 — spectral coarse data can fail a legal resolvent task

\[
\boxed{
(\sigma,\|\cdot\|_2)
\text{ merges }A,B,
\quad
T_R\text{ separates them}.
}
\]

This is Regression R01.

## H2 — full pseudospectrum and full resolvent-norm profile repair this witness

Because

\[
\rho_r(A)\neq\rho_r(B)
\]

and III.7 proves

\[
\ker\rho_r=\ker\rho_{ps},
\]

both representations preserve the HCube resolvent/pseudospectral distinction.

This is a witness-specific repair, not a universal minimality theorem.

## H3 — scalar transient-growth data can merge a resolvent-distinct pair

\[
\boxed{
\rho_g(A)=\rho_g(B),
\qquad
\rho_r(A)\neq\rho_r(B).
}
\]

Hence

\[
\boxed{
\rho_r\neq F\circ\rho_g
\text{ universally}.
}
\]

Thus the scalar semigroup-norm branch cannot replace the scalar resolvent branch for all tasks.

## H4 — adequacy is relative to both task and catalog

The same coarse representation that fails \(T_R\) can pass \(T_g\) on \(\Omega_H\), because \(T_g\) is constant on this pair.

Therefore

\[
\boxed{
\text{representation quality is not intrinsic to the representation alone}.
}
\]

The legal statement is always

\[
\boxed{
\mathrm{ADEQ}(\rho;\Omega,\mathcal T)
\iff
\ker\rho|_\Omega\subseteq E_\mathcal T|_\Omega.
}
\]

---

# 8. Nonnormality status

`A` is normal. `B` is nonnormal because its lower-right block

\[
C=
\begin{pmatrix}1&1\\0&0\end{pmatrix}
\]

satisfies

\[
CC^*\neq C^*C.
\]

The HCube witness therefore isolates a genuine nonnormal effect: equal spectrum and equal operator norm do not force equal resolvent response.

However, III.8 does **not** claim

\[
\boxed{
\text{nonnormality alone}
\Rightarrow
\text{large resolvent / transient growth}.
}
\]

Nonnormality is a structural condition; quantitative amplification remains task- and operator-dependent.

---

# 9. Local cross-check

### Frozen witness
`PASS`: no matrix has been changed from Regression R01.

### Arithmetic
`PASS`: the R01 resolvent values are preserved; the \(\varepsilon=1/3\) membership test separates the pair.

### Semigroup calculation
`PASS`: the logarithmic-norm estimate proves \(\|e^{tA}\|_2=\|e^{tB}\|_2=e^{2t}\) for all \(t\ge0\).

### Matrix semantics
`PASS`: every matrix entry is evaluated by the kernel-inclusion criterion on \(\Omega_H\).

### Catalog-relative warning
`PASS`: separation on a two-point catalog is not promoted to global faithfulness.

### MOST bind
`PASS`: III.8 realizes the partial information graph of III.7 rather than replacing it with one universal hierarchy.

### CORE discipline
`PASS`: HCube remains a regression/laboratory and adds no PSI primitive.

---

# 10. Verdict

\[
\boxed{
\mathrm{III.8\ HCUBE}
=
\mathrm{LAB\ PASS\ 01 / PROOF\ PASS / LOCAL\ CROSS\!\!-\!CHECK\ PASS}.
}
\]

The next mandatory gate is the MOST/HCube whole-layer crosscheck for III.7–III.8.
