# PRINCIPIA SEMANTICA — VOLUME III / MOST–HCUBE WHOLE-LAYER CROSSCHECK 01

**Status:** `GLOBAL CROSSCHECK PASS`  
**Date:** 2026-09-29  
**Scope:** `III.7–III.8`  
**Inputs:** `principia-v3-07-spectral-information-hierarchy-most.md`, `principia-v3-08-hcube-nonnormal-resolvent-lab.md`, `regression-bank-01.md`

---

# 1. Question

Do III.7 and III.8 form one coherent operator-information layer without inflating a partial factorization order into a universal hierarchy?

Required checks:

1. representation types and kernels;
2. task/catalog relativity;
3. HCube arithmetic and pseudospectral thresholding;
4. semigroup/resolvent branch logic;
5. gauge discipline;
6. no CORE growth.

---

# 2. Result

\[
\boxed{
\mathrm{MOST/HCUBE\ III.7:III.8}
=
\mathrm{MATHEMATICAL\ GLOBAL\ PASS}.
}
\]

No theorem-level errata are required.

---

# 3. Factorization layer

III.7 proves, under the fixed finite-dimensional norm convention,

\[
\boxed{
\ker_{eq}\rho_r
=
\ker_{eq}\rho_{ps}
\subseteq
\ker_{eq}\rho_\sigma.
}
\]

This is an exact partial information order:

\[
\boxed{
\mathcal R_A(\cdot)
\to
r_A(\cdot)
\leftrightarrow
\rho_{ps}(A)
\to
\rho_\sigma(A).
}
\]

III.8 does not alter this theorem. It supplies explicit strictness witnesses and task-level tests.

---

# 4. HCube strictness survives composition

For the frozen pair

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=
\begin{pmatrix}
2&0&0\\
0&1&1\\
0&0&0
\end{pmatrix},
\]

one has

\[
\sigma(A)=\sigma(B),
\qquad
\|A\|_2=\|B\|_2=2,
\]

but

\[
r_A(1/2)=2,
\qquad
r_B(1/2)=2(1+\sqrt2).
\]

Therefore the R01 conclusion remains exact:

\[
\boxed{
\ker(\rho_\sigma,\|\cdot\|_2)
\not\subseteq
\ker T_R.
}
\]

The explicit threshold

\[
\varepsilon=1/3
\]

also yields

\[
1/2\notin\sigma_{1/3}(A),
\qquad
1/2\in\sigma_{1/3}(B),
\]

which is consistent with III.7's equivalence of full pseudospectral and full resolvent-norm information.

---

# 5. Semigroup branch — exact new conclusion

III.8 proves

\[
\boxed{
\|e^{tA}\|_2
=
\|e^{tB}\|_2
=e^{2t}
\quad\forall t\ge0,
}
\]

while

\[
\rho_r(A)\neq\rho_r(B).
\]

Hence there is no universal factorization

\[
\boxed{
\rho_r=F\circ\rho_g
}
\]

on the class of all finite matrices.

This is a strict theorem-level strengthening of III.7's decision not to posit a scalar resolvent/semigroup equivalence.

The converse statement

\[
\rho_g=G\circ\rho_r
\]

is **not** decided by HCube and is not claimed false here.

Therefore the correct status is:

\[
\boxed{
\text{one direction of universal scalar factorization is ruled out;}
\quad
\text{no total-order conclusion follows}.
}
\]

---

# 6. Task and catalog relativity

III.8 evaluates

\[
\ker\rho|_{\Omega_H}
\subseteq
\ker T|_{\Omega_H},
\qquad
\Omega_H=\{A,B\}.
\]

This is fully consistent with PSI.

The `PASS*` entries are important: if a task is constant on \(\Omega_H\), even the constant representation is adequate on that restricted catalog.

Thus:

\[
\boxed{
\mathrm{ADEQ}(\rho;\Omega,\mathcal T)
\text{ depends on both }\Omega\text{ and }\mathcal T.
}
\]

No `PASS` on the two-point catalog is promoted to global faithfulness.

In particular, although \(\rho_r\) separates the HCube pair and therefore passes the exact-identity task on \(\Omega_H\), III.7-X2 remains a valid counterexample to global faithfulness of the scalar resolvent-norm profile for directional tasks.

---

# 7. Nonnormality interpretation

`A` is normal and `B` is nonnormal. Their equal spectrum and operator norm but different resolvent response provide a clean nonnormal/resolvent witness.

However the same pair also has identical scalar semigroup-norm profiles. Therefore the combined layer explicitly rejects both inflations:

\[
\boxed{
\text{nonnormality}
\not\Rightarrow
\text{a particular quantitative transient-growth signature},
}
\]

and

\[
\boxed{
\text{resolvent separation}
\not\Rightarrow
\text{semigroup-norm separation for the same witness}.
}
\]

HCube is therefore a representation-separation laboratory, not a universal theorem equating nonnormality, pseudospectral growth and transient growth.

---

# 8. Gauge discipline

The original HCube pair is not related by unitary similarity because normality is unitarily invariant and only `A` is normal. Thus the main HCube separator survives unitary gauge.

The separate III.7-X2 directional witness is intentionally basis-sensitive and remains legal only in contracts where unitary similarity is not quotient gauge or where the distinguished direction is part of the physical/task data.

No gauge inconsistency is introduced by combining III.7 and III.8.

---

# 9. Regression status

The combined layer permanently protects against:

1. spectrum or spectrum+norm being treated as automatically sufficient for resolvent tasks;
2. full pseudospectral information being confused with only one chosen epsilon-level;
3. scalar resolvent norms being treated as full directional operator response;
4. scalar semigroup-norm data being treated as automatically sufficient for resolvent tasks;
5. two-point separation being inflated to global representation sufficiency;
6. nonnormality being equated with one universal transient-growth magnitude.

No new PSI primitive is required. All conclusions are instances of

\[
\boxed{
\ker_{eq}\rho\subseteq E_{\mathcal T}.
}
\]

---

# 10. Verdict

\[
\boxed{
\mathrm{III.7:III.8\ MOST/HCUBE}
=
\mathrm{GLOBAL\ PASS}.
}
\]

The MOST/HCube layer is now closed as a representation-information block. Further operator laboratories require their own contracts and cannot inherit HCube conclusions automatically.
