# PRINCIPIA SEMANTICA — VOLUME III.12

## P9-H — modified-energy / hypocoercive bridge

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Source gate:** `p9u-hypocoercive-source-contract-01.md`  
**General P9 status:** `OPEN / CENTRAL`  
**Role:** closed Lyapunov-metric subclass; no universal P9 closure.

---

# 1. Contract

Let \(\mathcal H\) be a complex Hilbert space and let

\[
A:D(A)\subset\mathcal H\to\mathcal H
\]

generate a strongly continuous semigroup

\[
S(t)=e^{tA}.
\]

Let

\[
Q=Q^*\in\mathcal B(\mathcal H)
\]

be bounded and coercive:

\[
\boxed{
mI\le Q\le MI
}
\]

for some \(0<m\le M<\infty\).

Define

\[
\|x\|_Q^2:=\langle Qx,x\rangle.
\]

Assume that for some \(\lambda>0\),

\[
\boxed{
2\operatorname{Re}\langle QAx,x\rangle
\le
-2\lambda\langle Qx,x\rangle
\qquad(x\in D(A)).
}
\]

Equivalently, in quadratic-form notation,

\[
A^*Q+QA\le-2\lambda Q.
\]

Let

\[
c_Q:=\sqrt{M/m}=\sqrt{\kappa(Q)}.
\]

---

# 2. Theorem III.12.A — exponential contraction in the modified metric

For every \(t\ge0\),

\[
\boxed{
\|S(t)\|_Q\le e^{-\lambda t}.
}
\]

Hence, in the ambient Hilbert norm,

\[
\boxed{
\|S(t)\|
\le
c_Qe^{-\lambda t}.
}
\]

## Proof

For \(x\in D(A)\), set \(u(t)=S(t)x\). Then

\[
\frac d{dt}\|u(t)\|_Q^2
=
2\operatorname{Re}\langle QAu(t),u(t)\rangle
\le
-2\lambda\|u(t)\|_Q^2.
\]

Gronwall gives

\[
\|S(t)x\|_Q\le e^{-\lambda t}\|x\|_Q.
\]

Density of \(D(A)\) and strong continuity extend the estimate to all \(x\in\mathcal H\).

Since

\[
\sqrt m\|x\|\le\|x\|_Q\le\sqrt M\|x\|,
\]

we obtain

\[
\|S(t)x\|
\le
m^{-1/2}\|S(t)x\|_Q
\le
\sqrt{M/m}\,e^{-\lambda t}\|x\|.
\]

\(\square\)

---

# 3. Theorem III.12.B — resolvent bridge

For every

\[
\operatorname{Re}z> -\lambda,
\]

the point \(z\) belongs to the resolvent set of \(A\), and

\[
\boxed{
\|(zI-A)^{-1}\|_Q
\le
\frac{1}{\operatorname{Re}z+\lambda}.
}
\]

Consequently,

\[
\boxed{
\|(zI-A)^{-1}\|
\le
\frac{c_Q}{\operatorname{Re}z+\lambda}.
}
\]

## Proof

By III.12.A, the Laplace integral converges in the \(Q\)-norm whenever \(\operatorname{Re}z> -\lambda\):

\[
(zI-A)^{-1}x
=
\int_0^\infty e^{-zt}S(t)x\,dt.
\]

Therefore

\[
\|(zI-A)^{-1}x\|_Q
\le
\int_0^\infty
 e^{-(\operatorname{Re}z+\lambda)t}\,dt\,\|x\|_Q,
\]

which gives the first estimate. Norm equivalence yields the second. \(\square\)

---

# 4. Theorem III.12.C — Kreiss control

Define the continuous-time Kreiss constants

\[
\mathcal K_Q(A)
:=
\sup_{\operatorname{Re}z>0}
\operatorname{Re}z\,\|(zI-A)^{-1}\|_Q,
\]

and

\[
\mathcal K(A)
:=
\sup_{\operatorname{Re}z>0}
\operatorname{Re}z\,\|(zI-A)^{-1}\|.
\]

Then

\[
\boxed{
\mathcal K_Q(A)=1
}
\]

and

\[
\boxed{
1\le\mathcal K(A)\le c_Q.
}
\]

## Proof

For \(x=\operatorname{Re}z>0\), III.12.B gives

\[
x\|(zI-A)^{-1}\|_Q
\le
\frac{x}{x+\lambda}<1.
\]

Thus \(\mathcal K_Q(A)\le1\). On the positive real axis,

\[
x(xI-A)^{-1}y\to y
\qquad(x\to\infty)
\]

for every \(y\in\mathcal H\), hence the operator norm has liminf at least \(1\). Therefore \(\mathcal K_Q(A)=1\).

The ambient estimate follows identically from III.12.B and norm equivalence, with the same large-\(x\) lower bound. \(\square\)

---

# 5. Theorem III.12.D — pseudospectral right-edge control

For the ambient norm define

\[
\sigma_\varepsilon(A)
:=
\sigma(A)
\cup
\{z\in\rho(A):\|(zI-A)^{-1}\|>\varepsilon^{-1}\}.
\]

Then

\[
\boxed{
\sup_{z\in\sigma_\varepsilon(A)}
\operatorname{Re}z
\le
-\lambda+c_Q\varepsilon.
}
\]

In the modified \(Q\)-norm,

\[
\boxed{
\sup_{z\in\sigma^{(Q)}_\varepsilon(A)}
\operatorname{Re}z
\le
-\lambda+\varepsilon.
}
\]

## Proof

The semigroup estimate implies

\[
s(A)\le-\lambda.
\]

If

\[
\operatorname{Re}z> -\lambda+c_Q\varepsilon,
\]

then

\[
\operatorname{Re}z+\lambda>c_Q\varepsilon
\]

and III.12.B yields

\[
\|(zI-A)^{-1}\|
<
\varepsilon^{-1}.
\]

Thus such a point is neither spectral nor \(\varepsilon\)-pseudospectral. The \(Q\)-norm statement is the same with \(c_Q=1\). \(\square\)

---

# 6. Hypocoercivity is not transient amplification

Suppose additionally that in the ambient Hilbert norm

\[
A=S+N,
\qquad
S=S^*\le0,
\qquad
N^*=-N.
\]

Then for classical trajectories

\[
\frac d{dt}\|S(t)x\|^2
=2\langle S S(t)x,S(t)x\rangle
\le0.
\]

Hence

\[
\boxed{
\|S(t)\|\le1
\qquad(t\ge0).
}
\]

The modified metric \(Q\) is therefore not introduced to remove unavoidable norm amplification. Its role is to recover a strict exponential rate when the direct symmetric part is degenerate.

Permanent distinction:

\[
\boxed{
\text{hypocoercive decay}
\neq
\text{transient growth}.
}
\]

---

# 7. Explicit finite-dimensional hypocoercive witness

Consider

\[
A=
\begin{pmatrix}
0&1\\
-1&-1
\end{pmatrix}.
\]

Its Hermitian part is

\[
\frac{A+A^*}{2}
=
\begin{pmatrix}
0&0\\
0&-1
\end{pmatrix},
\]

so direct dissipation is degenerate and the ambient norm is only non-increasing at the differential level.

Nevertheless

\[
\sigma(A)
=
\left\{
\frac{-1+i\sqrt3}{2},
\frac{-1-i\sqrt3}{2}
\right\},
\]

so the system is exponentially stable.

Define

\[
Q=
\begin{pmatrix}
3/2&1/2\\
1/2&1
\end{pmatrix}.
\]

Then

\[
\boxed{
A^*Q+QA=-I.
}
\]

The eigenvalues of \(Q\) are

\[
\frac{5\pm\sqrt5}{4}.
\]

Thus

\[
\kappa(Q)
=
\frac{5+\sqrt5}{5-\sqrt5}
=
\frac{3+\sqrt5}{2},
\]

and

\[
\boxed{
c_Q=\sqrt{\kappa(Q)}=\frac{1+\sqrt5}{2}.}
\]

Choosing

\[
\lambda
=
\frac{1}{2\lambda_{\max}(Q)}
=
\frac{2}{5+\sqrt5},
\]

we have

\[
A^*Q+QA
=-I
\le
-2\lambda Q.
\]

Hence III.12 gives

\[
\boxed{
\|e^{tA}\|_Q
\le
 e^{-\lambda t}
}
\]

and

\[
\boxed{
\|e^{tA}\|_2
\le
\frac{1+\sqrt5}{2}
 e^{-\lambda t}.
}
\]

At the same time, because the original Hermitian part is nonpositive,

\[
\boxed{
\|e^{tA}\|_2\le1.
}
\]

This witness cleanly separates:

- degenerate instantaneous dissipation;
- exponential stability recovered by a modified metric;
- absence of ambient-norm transient amplification.

---

# 8. Relation to DMS

In the DMS kinetic setting, under assumptions H1–H4, one constructs

\[
\mathscr H[f]
=
\frac12\|f\|^2
+
\varepsilon\operatorname{Re}\langle\mathcal Af,f\rangle
\]

with

\[
\frac12(1-\varepsilon)\|f\|^2
\le
\mathscr H[f]
\le
\frac12(1+\varepsilon)\|f\|^2
\]

for an admissible \(\varepsilon\), and with a strict differential decay inequality.

Thus the DMS modified entropy determines a bounded coercive quadratic metric \(Q\) of the III.12 type.

III.12 then adds a PSI/operator-theoretic consequence not to be confused with the original DMS statement: the same equivalent metric immediately yields explicit resolvent, Kreiss and pseudospectral half-plane bounds through \(c_Q\).

This is a derived bridge, not an authorship claim over the DMS construction.

---

# 9. Relation to Gearhart–Prüss

Gearhart–Prüss gives a Hilbert-space characterization of exponential stability in terms of right-half-plane / imaginary-axis resolvent control under the standard hypotheses.

III.12 is stronger in a different direction: once a coercive Lyapunov metric \(Q\) with rate \(\lambda\) is explicitly known, the resolvent bound is obtained directly and quantitatively by the Laplace transform.

Thus:

\[
\boxed{
\text{explicit Lyapunov metric}
\Rightarrow
\text{explicit resolvent half-plane control}.
}
\]

The converse construction of an explicit bounded coercive \(Q\) from resolvent data is not asserted here.

---

# 10. What III.12 does not prove

III.12 does not prove that every exponentially stable or every nonnormal generator admits a practically constructible \(Q\) with useful constants.

It does not close:

- unrestricted unbounded P9-U;
- optimal hypocoercive constants;
- continuous-spectrum pseudospectral geometry;
- minimal commutator families;
- a universal algorithm converting arbitrary resolvent information into a modified energy.

Hence

\[
\boxed{
P9_{\rm general}=OPEN/CENTRAL.
}
\]

---

# 11. Local cross-check

### Source discipline
`PASS`: DMS is used only under its typed H1–H4 mechanism; no universal bracket theorem is invented.

### Domain
`PASS`: the Lyapunov inequality is imposed on \(D(A)\), then extended through the generated semigroup.

### Semigroup
`PASS`: exact modified-norm decay follows by Gronwall.

### Resolvent
`PASS`: half-plane estimate follows by the Laplace representation.

### Kreiss
`PASS`: raw resolvent margin is not confused with the normalized Kreiss constant.

### Pseudospectrum
`PASS`: right-edge bound follows directly from the resolvent estimate.

### Hypocoercivity interpretation
`PASS`: no claim of unavoidable transient amplification in the ambient norm.

### III.11 relation
`PASS`: III.12 does not require self-adjointness after metric transport; it is a genuine extension from normalizable gradient dynamics to strictly dissipative equivalent metrics.

### CORE status
`PASS`: no new PSI primitive.

---

# 12. Verdict

\[
\boxed{
\mathrm{III.12\ P9\!-
H}
=
\mathrm{THEOREM\ PROSE\ PASS\ 01 / PROOF\ PASS / LOCAL\ CROSS\!-
CHECK\ PASS}.
}
\]

A composition cross-check with III.7–III.11 is required before opening a further P9-U subclass.