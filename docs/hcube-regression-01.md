# PSI — HCUBE-REGRESSION-01

**Status:** COMPLETED REGRESSION / LAB-BENCHMARK / NO CORE CHANGE  
**Date:** 2026-09-28  
**Agent:** PSI Agent Architecture v02

## 0. Purpose

This run belongs to the post-R4 hardening phase. It does **not** ask whether HCube forces a new primitive. It asks whether a deliberately coarse operator representation can identify two systems that a declared resolvent/pseudospectral task must distinguish.

Primary level:

\[
\boxed{\mathrm{LAB/BENCHMARK}}
\]

with a bridge to representation adequacy.

---

## 1. Contract snapshot

Work on real `3 x 3` matrices with the Euclidean operator norm.

Task:

\[
\mathcal T_{1/2}: A\mapsto \left\|\left(\tfrac12 I-A\right)^{-1}\right\|_2.
\]

Coarse representation under test:

\[
\boxed{
\rho_0(A)=\left(\chi_A,\|A\|_2\right).
}
\]

Question: is `rho_0` sufficient for `T_{1/2}`?

No noise, estimation or statistical inference is involved.

---

## 2. Exact paired witness

Let

\[
A=
\begin{pmatrix}
2&0&0\\
0&1&0\\
0&0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
2&0&0\\
0&1&1\\
0&0&0
\end{pmatrix}.
\]

Both are upper triangular with diagonal `2,1,0`, hence

\[
\boxed{
\chi_A(\lambda)=\chi_B(\lambda)
=\lambda(\lambda-1)(\lambda-2).
}
\]

For `A`,

\[
\|A\|_2=2.
\]

For `B`, the lower block is

\[
C=\begin{pmatrix}1&1\\0&0\end{pmatrix},
\qquad
\|C\|_2=\sqrt2<2,
\]

so

\[
\boxed{\|B\|_2=2=\|A\|_2.}
\]

Therefore

\[
\boxed{\rho_0(A)=\rho_0(B).}
\]

---

## 3. Exact resolvent separation

At

\[
z=\tfrac12,
\]

we have

\[
(zI-A)^{-1}
=
\operatorname{diag}\left(-\tfrac23,-2,2\right),
\]

hence

\[
\boxed{\|(zI-A)^{-1}\|_2=2.}
\]

For `B`,

\[
(zI-B)^{-1}
=
\begin{pmatrix}
-\tfrac23&0&0\\
0&-2&-4\\
0&0&2
\end{pmatrix}.
\]

The lower `2 x 2` block

\[
M=\begin{pmatrix}-2&-4\\0&2\end{pmatrix}
\]

satisfies

\[
\lambda_{\max}(M^*M)=12+8\sqrt2,
\]

therefore

\[
\|M\|_2
=\sqrt{12+8\sqrt2}
=2(1+\sqrt2).
\]

Thus

\[
\boxed{
\left\|\left(\tfrac12I-B\right)^{-1}\right\|_2
=2(1+\sqrt2)
>2.
}
\]

The ratio is

\[
\boxed{1+\sqrt2\approx2.41421356.}
\]

So the same characteristic polynomial and the same spectral norm do not determine this resolvent task.

---

## 4. Representation-adequacy verdict

Let

\[
R_{1/2}(X)=\left\|\left(\tfrac12I-X\right)^{-1}\right\|_2.
\]

Then

\[
\rho_0(A)=\rho_0(B)
\]

but

\[
R_{1/2}(A)\neq R_{1/2}(B).
\]

Therefore

\[
(A,B)\in\ker_{eq}\rho_0
\]

while

\[
(A,B)\notin\ker_{eq}R_{1/2}.
\]

Hence

\[
\boxed{
\ker_{eq}\rho_0
\not\subseteq
\ker_{eq}R_{1/2}.
}
\]

By the ordinary PSI factorization criterion:

\[
\boxed{
\rho_0=(\chi_A,\|A\|_2)
\text{ is insufficient for the resolvent task }\mathcal T_{1/2}.
}
\]

This is the exact regression target.

---

## 5. Normality / nonnormality

`A` is normal. For `B`,

\[
BB^*-B^*B\neq0.
\]

In fact,

\[
\|BB^*-B^*B\|_F=2.
\]

Thus the paired witness keeps spectrum and operator norm fixed while changing nonnormal geometry.

This is not itself a universal metric of nonnormality; it only verifies that the pair is structurally different in the intended direction.

---

## 6. HCube separator

The project bridge retained from the classical finite-dimensional calculation is

\[
\boxed{
\|e^{t\operatorname{ad}_X}\|_{\mathrm{HS}}
=
\kappa_2(e^{tX}).
}
\]

At `t=1`:

\[
\kappa_2(e^A)=e^2\approx7.38905610,
\]

while direct calculation gives

\[
\kappa_2(e^B)\approx8.86992603.
\]

Thus the HCube bridge also distinguishes the pair.

But this does **not** prove that HCube is the unique, minimal or universally necessary representation. The resolvent already separates the declared task exactly.

The correct status is therefore:

\[
\boxed{
\text{HCube = diagnostic separator / benchmark, not CORE primitive.}
}
\]

---

## 7. P9 versus HCube discipline

Do not conflate:

\[
X\mapsto e^{tX}x
\]

with

\[
Y\mapsto e^{tX}Ye^{-tX}.
\]

P9 concerns state amplification, resolvents and pseudospectral/transient behaviour of `X`.

HCube concerns conditioning of the similarity action / inner derivation bridge.

The existence of the exact bridge

\[
\|e^{t\operatorname{ad}_X}\|_{\mathrm{HS}}
=
\kappa(e^{tX})
\]

does not license the claim that pseudospectra of `ad_X` predict state transient growth.

---

## 8. Permanent regression

Any representation `rho` proposed for a resolvent-sensitive task must pass

\[
\ker_{eq}\rho\subseteq E_{\mathcal T}.
\]

In particular, the regression pair requires that a future representation not identify `A` and `B` when the task includes `R_{1/2}` or another quantity separating their nonnormal geometry.

Permanent fixture:

```text
A = diag(2,1,0)
B = [[2,0,0],[0,1,1],[0,0,0]]
charpoly(A) = charpoly(B)
||A||_2 = ||B||_2 = 2
R_1/2(A) = 2
R_1/2(B) = 2(1+sqrt(2))
```

---

## 9. What this result does not test

This run does not establish:

- that the pair has maximally different pseudospectra;
- that HCube is necessary for every nonnormal problem;
- that HCube identifies physical mechanism or causality;
- that equal spectrum and norm are the only coarse summaries worth testing;
- that finite-dimensional results transfer automatically to unbounded operators;
- that numerical pseudospectral grids are unnecessary in larger examples.

It establishes one exact counterexample to sufficiency of a specific coarse representation.

---

## 10. Freeze verdict

Freeze:

\[
\boxed{
(\chi_A,\|A\|_2)
\text{ does not determine resolvent-sensitive task behaviour.}
}
\]

Classify as:

`CLASSICAL MATRIX FACT + PSI REPRESENTATION-ADEQUACY REGRESSION / LAB BENCHMARK`.

No CORE change and no Agent architecture change are justified.