# PRINCIPIA SEMANTICA — VOLUME III.11

## P9 — metric-gradient bridge: Hessian, resolvent and transient growth

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Migration source:** `p9-hessian-transient-migration-01.md`  
**General P9 status:** `OPEN / CENTRAL`  
**Current role:** closed metric-gradient sector; no universal P9 closure.

---

# 1. Contract

Let \(\mathcal H=\mathbb C^n\) with the Euclidean inner product. Let

\[
G=G^*>0,
\qquad
H=H^*>0.
\]

Consider the linearized gradient operator

\[
\boxed{
A=-G^{-1}H.
}
\]

Define

\[
\boxed{
B:=G^{-1/2}HG^{-1/2}=B^*>0.
}
\]

The associated energy inner product and norm are

\[
\langle x,y\rangle_G:=\langle Gx,y\rangle,
\qquad
\|x\|_G:=\langle Gx,x\rangle^{1/2}.
\]

Define the metric spectral gap

\[
\boxed{
\mu_G
:=
\lambda_{\min}(B)
=
\inf_{x\ne0}
\frac{\langle Hx,x\rangle}
{\langle Gx,x\rangle}
>0.
}
\]

This is the correct decay parameter of the gradient system.

---

# 2. Similarity to a self-adjoint negative operator

Since

\[
G^{-1/2}(-B)G^{1/2}
=
-G^{-1}H,
\]

we have

\[
\boxed{
A
=
G^{-1/2}(-B)G^{1/2}.
}
\]

Therefore

\[
\boxed{
e^{tA}
=
G^{-1/2}e^{-tB}G^{1/2}
}
\]

and for every \(z\in\rho(A)\),

\[
\boxed{
(zI-A)^{-1}
=
G^{-1/2}(zI+B)^{-1}G^{1/2}.
}
\]

Thus the gradient dynamics is unitarily equivalent to \(-B\) after passing to the \(G\)-metric.

---

# 3. Theorem III.11.A — exact energy-norm semigroup control

The induced operator norm in the energy metric satisfies

\[
\boxed{
\|e^{tA}\|_G
=
\|e^{-tB}\|_2
=
e^{-\mu_G t}
\qquad(t\ge0).
}
\]

Hence

\[
\boxed{
\sup_{t\ge0}\|e^{tA}\|_G=1
}
\]

and there is no transient amplification in the physical energy norm.

## Proof

The map

\[
U_Gx:=G^{1/2}x
\]

is unitary from \((\mathcal H,\langle\cdot,\cdot\rangle_G)\) to Euclidean \(\mathcal H\). Under this unitary map,

\[
U_GAU_G^{-1}=-B.
\]

Since \(B\) is self-adjoint positive,

\[
\|e^{-tB}\|_2
=
\max_{\beta\in\sigma(B)}e^{-t\beta}
=
e^{-t\mu_G}.
\]

The result follows. \(\square\)

---

# 4. Theorem III.11.B — exact energy-norm resolvent control

For every \(z\notin-\sigma(B)\),

\[
\boxed{
\|(zI-A)^{-1}\|_G
=
\frac{1}{\operatorname{dist}(z,-\sigma(B))}.
}
\]

In particular, for \(\operatorname{Re}z>0\),

\[
\boxed{
\|(zI-A)^{-1}\|_G
\le
\frac{1}{\operatorname{Re}z+\mu_G}.
}
\]

Therefore the continuous-time energy-norm Kreiss constant

\[
\mathcal K_G(A)
:=
\sup_{\operatorname{Re}z>0}
\operatorname{Re}z\,
\|(zI-A)^{-1}\|_G
\]

satisfies

\[
\boxed{
\mathcal K_G(A)=1.
}
\]

## Proof

Unitary transport by \(U_G\) gives

\[
\|(zI-A)^{-1}\|_G
=
\|(zI+B)^{-1}\|_2.
\]

The operator \(-B\) is normal, so its resolvent norm is the reciprocal distance to the spectrum. If \(\operatorname{Re}z=x>0\) and \(\beta\ge\mu_G\), then

\[
|z+\beta|
\ge x+\beta
\ge x+\mu_G.
\]

Hence the stated bound. It gives \(\mathcal K_G(A)\le1\). Conversely,

\[
x(xI-A)^{-1}\to I
\qquad(x\to+\infty),
\]

so the supremum is at least \(1\). \(\square\)

---

# 5. Euclidean transport bounds

Let

\[
\kappa_2(G)
:=
\|G\|_2\|G^{-1}\|_2.
\]

Norm equivalence gives

\[
\|T\|_2
\le
\sqrt{\kappa_2(G)}\,\|T\|_G.
\]

Therefore

\[
\boxed{
\|e^{tA}\|_2
\le
\sqrt{\kappa_2(G)}\,e^{-\mu_Gt},
}
\]

and, for \(\operatorname{Re}z>0\),

\[
\boxed{
\|(zI-A)^{-1}\|_2
\le
\frac{\sqrt{\kappa_2(G)}}
{\operatorname{Re}z+\mu_G}.
}
\]

Hence

\[
\boxed{
1\le\mathcal K_2(A)
\le
\sqrt{\kappa_2(G)}.
}
\]

This is the legal quantitative bridge in the metric-gradient sector.

The gap \(\mu_G\) controls decay rate and raw resolvent margin; the metric condition number controls how much Euclidean coordinates can amplify the energy-normal dynamics.

---

# 6. Commuting metric and Hessian

If

\[
[G,H]=0,
\]

then \(G\) and \(H\) are simultaneously unitarily diagonalizable. Consequently

\[
A=-G^{-1}H
\]

is self-adjoint negative in the Euclidean inner product.

Thus

\[
\boxed{
\|e^{tA}\|_2=e^{-\mu_Gt},
\qquad
\mathcal K_2(A)=1.
}
\]

Metric-generated Euclidean nonnormality requires incompatibility between \(G\) and \(H\).

---

# 7. Explicit metric-mismatch witness

Take

\[
G=
\begin{pmatrix}
4&0\\0&1
\end{pmatrix},
\qquad
G^{1/2}=
\begin{pmatrix}
2&0\\0&1
\end{pmatrix}.
\]

Let

\[
B=
\begin{pmatrix}
11/2&-9/2\\
-9/2&11/2
\end{pmatrix},
\]

whose eigenvalues are \(1\) and \(10\). Define

\[
H=G^{1/2}BG^{1/2}
=
\begin{pmatrix}
22&-9\\
-9&11/2
\end{pmatrix}>0.
\]

Then

\[
A=-G^{-1}H
=
\begin{pmatrix}
-11/2&9/4\\
9&-11/2
\end{pmatrix}.
\]

In the energy norm,

\[
\boxed{
\|e^{tA}\|_G=e^{-t}.
}
\]

But in Euclidean norm,

\[
\frac{A+A^*}{2}
=
\begin{pmatrix}
-11/2&45/8\\
45/8&-11/2
\end{pmatrix}
\]

has eigenvalues

\[
\boxed{
\frac18,
\qquad
-\frac{89}{8}.
}
\]

The Euclidean numerical abscissa is therefore positive:

\[
\boxed{\omega_2(A)=1/8>0.}
\]

Hence there exists sufficiently small \(t>0\) such that

\[
\boxed{\|e^{tA}\|_2>1.}
\]

This is genuine Euclidean transient growth inside a true gradient system, but it disappears in the energy norm.

Therefore:

\[
\boxed{
\text{transient growth is norm/metric relative}.
}
\]

This witness does **not** say that all noncommuting \(G,H\) produce transient growth.

---

# 8. Jordan boundary — genuinely non-gradient Euclidean mechanism

Let

\[
J_{\mu,M}
=
\begin{pmatrix}
-\mu&M\\0&-\mu
\end{pmatrix}.
\]

Its numerical abscissa is

\[
\omega_2(J_{\mu,M})
=-\mu+|M|/2.
\]

Hence

\[
\boxed{
\sup_{t>0}\|e^{tJ_{\mu,M}}\|_2>1
\iff
|M|>2\mu.
}
\]

In that regime the dissipative Hermitian part

\[
H_{\rm diss}:=-\frac{J_{\mu,M}+J_{\mu,M}^*}{2}
\]

is not positive semidefinite.

Moreover a nontrivial Jordan block is not similar to a self-adjoint operator, because self-adjoint operators are diagonalizable. Thus this transient-growth mechanism lies outside the positive-definite metric-gradient sector of III.11.

This separates two mechanisms that older P9 prose had conflated:

1. metric-coordinate transient growth of a gradient system;
2. genuinely defective/nongradient transient growth.

---

# 9. Raw resolvent versus transient measure

For the normal scalar family

\[
A_\mu=-\mu I,
\]

we have

\[
\boxed{
\sup_{\operatorname{Re}z\ge0}
\|(zI-A_\mu)^{-1}\|
=
1/\mu,
}
\]

while

\[
\boxed{
\mathcal K(A_\mu)=1,
\qquad
\sup_{t\ge0}\|e^{tA_\mu}\|=1.
}
\]

Therefore closing the spectral gap can make the system increasingly sensitive in a raw resolvent sense without producing transient amplification.

Permanent boundary:

\[
\boxed{
\text{resolvent sensitivity}
\neq
\text{transient amplification measure}.
}
\]

---

# 10. What III.11 does not prove

III.11 does not solve the general historical P9 problem.

It does not provide a universal function

\[
\Phi(\mu,\nu)
\]

for arbitrary nonnormal generators.

It does not classify:

- unbounded non-gradient generators;
- continuous-spectrum transient mechanisms;
- hypocoercive systems with degenerate symmetric part;
- minimal sufficient commutator families;
- general resolvent-to-semigroup equivalence in infinite dimension.

Thus

\[
\boxed{
P9_{\rm general}=OPEN/CENTRAL.
}
\]

---

# 11. Relation to MOST / HCube

MOST/HCube established that resolvent and semigroup-norm information are not universally the same representation.

III.11 does not contradict this. It identifies a restricted class in which the common metric-gradient structure simultaneously controls both branches.

Thus:

\[
\boxed{
\text{general partial information order}
+
\text{restricted structural bridge}
}
\]

is the correct combined picture.

---

# 12. Local cross-check

### Source hierarchy
`PASS`: KANON2 general P9 remains OPEN/CENTRAL; July strict source supplies the valid P10 metric bridge and Jordan laboratory.

### Hessian typing
`PASS`: energy Hessian and dissipative Hermitian part are separated.

### Semigroup
`PASS`: energy norm gives exact monotone decay.

### Resolvent
`PASS`: energy resolvent is exactly the normal resolvent of \(-B\).

### Kreiss normalization
`PASS`: \(\mathcal K_G(A)=1\); scalar \(-\mu I\) no longer yields a false Kreiss blow-up.

### Euclidean norm
`PASS`: the only universal estimate imported from the metric bridge is the \(\sqrt{\kappa(G)}\) similarity bound.

### Transient witness
`PASS`: explicit positive \(G,H\) example has energy contraction and Euclidean initial growth.

### Jordan boundary
`PASS`: Jordan transient is not mislabeled as positive-dissipative Hessian dynamics.

### CORE status
`PASS`: no new PSI primitive.

---

# 13. Verdict

\[
\boxed{
\mathrm{III.11\ P9\ METRIC\!-
GRADIENT\ BRIDGE}
=
\mathrm{THEOREM\ PROSE\ PASS\ 01 / PROOF\ PASS / LOCAL\ CROSS\!-
CHECK\ PASS}.
}
\]

with

\[
\boxed{
P9_{\rm general}=OPEN/CENTRAL.
}
\]

A composition cross-check with III.7–III.10 is required before any next P9 theorem unit.