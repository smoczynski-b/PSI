# P9 HESSIAN–TRANSIENT MIGRATION 01

**Status:** `MIGRATION GATE PASS / GENERAL P9 REMAINS OPEN-CENTRAL / WORKING CLAIMS REPAIRED`  
**Date:** 2026-09-29

---

# 1. Source hierarchy

The active project source `KANON2.txt` marks the bridge

\[
H\longrightarrow(zI-A)^{-1}\longrightarrow e^{tA}
\]

as `OPEN / CENTRAL`, and explicitly separates the gradient-stability sector from the nonnormal sector.

The earlier strict mathematical canon of 2026-07-16 contains two distinct valid ingredients:

1. the exact Jordan-block transient-growth laboratory;
2. the metric-gradient bridge
   \(A=-G^{-1}H\), \(B=G^{-1/2}HG^{-1/2}\).

Later working P9 syntheses contain useful calculations but also several incompatible identifications. They are therefore treated as genealogy / working material, not as current theorem authority.

---

# 2. First structural repair — two different "Hessians"

For a general linear operator \(A\) in a fixed Hilbert norm, define its Hermitian part

\[
S_A:=\frac{A+A^*}{2}.
\]

If one writes

\[
A=-H_{\rm diss}+N,
\qquad
H_{\rm diss}:=-S_A,
\qquad
N^*=-N,
\]

then \(H_{\rm diss}\) is the dissipative Hermitian part of the operator in that chosen norm.

This object must not be silently identified with an energy Hessian

\[
H_L=D^2L(x_*),
\]

when the gradient dynamics uses a nontrivial metric \(G\):

\[
A=-G^{-1}H_L.
\]

In general,

\[
\boxed{
H_L\neq -\frac{A+A^*}{2}
\quad\text{when }G\neq I.
}
\]

This confusion generated several false P9 statements.

---

# 3. Dissipative decomposition gives contraction, not transient growth

Suppose, in a fixed Hilbert norm,

\[
A=-H+N,
\qquad
H=H^*\ge\mu I,
\qquad
N^*=-N,
\qquad
\mu>0.
\]

Then

\[
\operatorname{Re}\langle Ax,x\rangle
=-\langle Hx,x\rangle
\le-\mu\|x\|^2.
\]

For bounded matrices, or more generally after the standard maximal-dissipativity generation hypotheses, this implies

\[
\boxed{
\|e^{tA}\|\le e^{-\mu t}.
}
\]

Hence there is no transient amplification in this norm.

For \(\operatorname{Re}z>0\), the shifted dissipativity estimate gives

\[
\boxed{
\|(zI-A)^{-1}\|
\le
\frac{1}{\operatorname{Re}z+\mu}.
}
\]

Therefore the continuous-time Kreiss constant

\[
\mathcal K(A)
:=
\sup_{\operatorname{Re}z>0}
\operatorname{Re}z\,\|(zI-A)^{-1}\|
\]

satisfies

\[
\boxed{\mathcal K(A)=1.}
\]

The upper bound is \(\le1\), while the large-\(z\) resolvent asymptotic gives the reverse limiting bound.

Thus all historical claims assigning large transient growth or \(\mathcal K(A)\sim M/\mu\) to the whole class

\[
A=-H+N,\quad H\ge\mu I,\quad N^*=-N
\]

are withdrawn.

---

# 4. Second structural repair — raw resolvent sensitivity is not the Kreiss constant

For

\[
A=-\mu I,
\qquad\mu>0,
\]

we have

\[
\sup_{\operatorname{Re}z\ge0}
\|(zI-A)^{-1}\|
=
\frac1\mu.
\]

This quantity diverges as \(\mu\downarrow0\).

But

\[
\mathcal K(-\mu I)
=
\sup_{x>0}
\frac{x}{x+\mu}
=1.
\]

Therefore:

\[
\boxed{
\text{resolvent-margin blow-up}
\not\Rightarrow
\text{Kreiss/transient blow-up}.
}
\]

The former working counterexample `KP-P9.5` is invalid and withdrawn.

---

# 5. Jordan laboratory survives — but outside the positive-dissipative class

For

\[
J_{\mu,M}
=
\begin{pmatrix}
-\mu&M\\
0&-\mu
\end{pmatrix},
\qquad\mu>0,
\]

we have

\[
e^{tJ_{\mu,M}}
=
e^{-\mu t}
\begin{pmatrix}
1&Mt\\0&1
\end{pmatrix},
\]

and

\[
\boxed{
\|e^{tJ_{\mu,M}}\|_2
=
 e^{-\mu t}
\frac{\sqrt{M^2t^2+4}+|M|t}{2}.
}
\]

Its numerical abscissa is

\[
\boxed{
\omega(J_{\mu,M})
=
-\mu+\frac{|M|}{2}.
}
\]

Hence

\[
\boxed{
\sup_{t>0}\|e^{tJ_{\mu,M}}\|_2>1
\iff
|M|>2\mu.
}
\]

But then

\[
-\frac{J_{\mu,M}+J_{\mu,M}^*}{2}
\]

has a negative eigenvalue. Therefore the transient-growth regime is **not** in the class

\[
A=-H+N,\quad H\ge0,\quad N^*=-N
\]

with \(H\) equal to the dissipative Hermitian part.

The older claim that this Jordan matrix has \(H=\mu I\) and a skew-adjoint remainder is false.

---

# 6. Invalid working claims withdrawn

The migration gate withdraws or demotes the following working statements.

### 6.1 `[H,N]=0` with nonnormality

If

\[
A=-H+N,
\quad H^*=H,
\quad N^*=-N,
\quad [H,N]=0,
\]

then

\[
AA^*=A^*A.
\]

Thus \(A\) is normal. Any working counterexample claiming nonnormality with \([H,N]=0\) in this decomposition is invalid.

### 6.2 Scalar Kreiss blow-up

The claim

\[
A=-\mu I,\ \mu\to0
\quad\Rightarrow\quad
\mathcal K(A)\to\infty
\]

is false. The correct value is \(\mathcal K(A)=1\).

### 6.3 Jordan inside the positive-Hessian dissipative class

The Jordan transient-growth model cannot simultaneously satisfy

\[
A=-H+N,\quad H\ge0,\quad N^*=-N
\]

in the same Euclidean/Hilbert norm once \(|M|>2\mu\).

### 6.4 Universal no-bridge claims

Any claimed theorem of nonexistence of a universal scalar bridge that depends on the invalid counterexamples above is demoted back to `OPEN` unless separately reproved.

### 6.5 Hypocoercive transient growth as "unavoidable"

Existence of a modified coercive norm does not imply that the original norm must exhibit transient growth. Such statements require a separate example or theorem and are not promoted.

---

# 7. The correct metric-gradient bridge

The valid P10 structure is

\[
G=G^*>0,
\qquad
H_L=H_L^*>0,
\qquad
A=-G^{-1}H_L.
\]

Define

\[
B=G^{-1/2}H_LG^{-1/2}=B^*>0.
\]

Then

\[
\boxed{
A=G^{-1/2}(-B)G^{1/2}.
}
\]

Thus \(A\) is self-adjoint negative in the energy inner product

\[
\langle x,y\rangle_G:=\langle Gx,y\rangle.
\]

The correct spectral gap is the generalized/metric gap

\[
\boxed{
\mu_G
:=
\lambda_{\min}(B)
=
\inf_{x\ne0}
\frac{\langle H_Lx,x\rangle}
{\langle Gx,x\rangle}.
}
\]

It is not generally the Euclidean \(\lambda_{\min}(H_L)\).

This sector is theorem-ready and becomes III.11.

---

# 8. External classical verification

The migration was checked against classical semigroup facts:

- maximal dissipativity generates contraction semigroups (Lumer–Phillips);
- continuous-time Kreiss theory relates right-half-plane resolvent growth to finite-dimensional transient amplification;
- numerical-abscissa / Hermitian-part criteria control initial Euclidean growth.

The project claims no authorship of these classical results.

---

# 9. Gate verdict

\[
\boxed{
\mathrm{P9\ HESSIAN\!-
TRANSIENT\ MIGRATION\ GATE}=PASS.
}
\]

with

\[
\boxed{
P9_{\mathrm{general}}=OPEN/CENTRAL.
}
\]

The gate authorizes a restricted theorem unit for the metric-gradient sector only.