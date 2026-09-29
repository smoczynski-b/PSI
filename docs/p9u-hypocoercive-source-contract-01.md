# P9-U HYPOCOERCIVE SOURCE / CONTRACT GATE 01

**Status:** `SOURCE GATE PASS / P9-H SUBCLASS IDENTIFIED / GENERAL P9-U REMAINS OPEN`  
**Date:** 2026-09-29

---

# 1. Source result

The project sources classify the unrestricted P9 bridge as `OPEN / CENTRAL`, while older working notes isolate a hypocoercive class based on modified energies.

External classical verification confirms the relevant restricted source:

- Dolbeault–Mouhot–Schmeiser (DMS), *Hypocoercivity for linear kinetic equations conserving mass*;
- Villani, *Hypocoercivity*.

The DMS abstract setting is not the loose statement "bracket condition implies decay". It uses a typed Hilbert-space generator \(L-T\), an orthogonal projection \(\Pi\) onto \(N(L)\), and assumptions H1–H4:

1. microscopic coercivity of \(L\) on \((I-\Pi)\mathcal H\);
2. macroscopic coercivity of \(T\Pi\);
3. \(\Pi T\Pi=0\);
4. boundedness of the auxiliary operators used in the modified entropy estimate.

It then constructs a modified entropy

\[
\mathscr H[f]
=
\frac12\|f\|^2
+
\varepsilon\,\operatorname{Re}\langle \mathcal A f,f\rangle
\]

which is equivalent to the ambient Hilbert norm and satisfies a Gronwall-type decay inequality.

---

# 2. Main correction to older P9 prose

Suppose

\[
A=S+N,
\qquad
S=S^*\le0,
\qquad
N^*=-N.
\]

Then for classical trajectories

\[
\frac d{dt}\|u(t)\|^2
=
2\langle Su(t),u(t)\rangle
\le0.
\]

Thus this standard hypocoercive setup is already non-expansive in the ambient norm.

The issue is not unavoidable transient amplification. The issue is that when \(\ker S\neq0\), the ambient energy may fail to provide a **strict exponential rate** directly.

The purpose of the modified hypocoercive metric is to recover strict coercivity by using the coupling between the dissipative and conservative directions.

Therefore the older working statement

\[
\text{"hypocoercivity implies unavoidable transient growth in the standard norm"}
\]

is withdrawn.

---

# 3. Abstract contract extracted from hypocoercivity

The stable theorem-level object is not a particular commutator formula but an equivalent quadratic metric.

Let \(A:D(A)\subset\mathcal H\to\mathcal H\) generate a \(C_0\)-semigroup \(S(t)\). Let

\[
Q=Q^*\in\mathcal B(\mathcal H)
\]

satisfy

\[
\boxed{
mI\le Q\le MI
}
\]

for some \(0<m\le M<\infty\).

Assume that for some \(\lambda>0\),

\[
\boxed{
2\operatorname{Re}\langle QAx,x\rangle
\le
-2\lambda\langle Qx,x\rangle
\qquad(x\in D(A)).
}
\]

Equivalently, in form notation,

\[
A^*Q+QA\le-2\lambda Q.
\]

This is the exact contract promoted to III.12.

DMS/Villani supply mechanisms for constructing such a modified energy in important kinetic/hypocoercive subclasses. The project does not claim that every P9-U generator admits such a \(Q\).

---

# 4. Why this is a genuine extension of III.11

III.11 treated the metric-gradient class

\[
A=-G^{-1}H,
\qquad G,H>0,
\]

which becomes self-adjoint after transport to the energy metric.

The present contract only requires strict dissipativity in an equivalent metric:

\[
A^*Q+QA\le-2\lambda Q.
\]

The transformed generator

\[
Q^{1/2}AQ^{-1/2}
\]

need not be self-adjoint or normal.

Hence P9-H is strictly broader than the gradient-normal sector P9-G.

---

# 5. DMS source discipline

The DMS method provides a constructive modified entropy under its H1–H4 assumptions. It is not licensed to be rewritten as a universal theorem for arbitrary

\[
A=S+N,\quad S\le0,\quad N^*=-N.
\]

In particular:

- the microscopic/macroscopic decomposition matters;
- domain and boundedness hypotheses matter;
- the constants are class-dependent;
- optimality is not claimed.

The project therefore uses DMS as a **source mechanism for the existence of an equivalent Lyapunov metric in a typed kinetic subclass**, not as proof of a universal P9 bridge.

---

# 6. Gate verdict

\[
\boxed{
\mathrm{P9\!-
U\ SOURCE/CONTRACT\ GATE}=PASS
}
\]

with identified subclass

\[
\boxed{
\mathrm{P9\!-
H}:=\text{generators admitting a bounded coercive Lyapunov metric }Q.
}
\]

The gate authorizes III.12.

The unrestricted sector remains

\[
\boxed{P9_{\rm general}=OPEN/CENTRAL.}
\]
