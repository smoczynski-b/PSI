# PRINCIPIA SEMANTICA — VOLUME III.4

## Zwarta rezolwenta, widmo dyskretne i zupełność

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Upstream:** `principia-v3-03-domain-selfadjoint.md`  
**Historical source:** `PHISICA — NEW.pdf`, former claims on discrete spectrum/eigenfunction basis  
**Scope:** regular finite-interval Sturm–Liouville realizations from III.3

---

# 1. Contract

Let

\[
I=(a,b),\qquad -\infty<a<b<\infty,
\]

and let

\[
\mathcal H_\rho=L^2(I,\rho(\lambda)d\lambda).
\]

Assume

\[
\rho\in C^1([a,b]),\qquad B\in C^1([a,b]),\qquad V\in C([a,b];\mathbb R),
\]

with

\[
\rho(\lambda)>0,\qquad B(\lambda)>0
\quad\text{on }[a,b].
\]

Set

\[
p=\rho B.
\]

Let

\[
H_{\alpha,\beta}
\]

be one of the separated self-adjoint realizations constructed in III.3:

\[
\tau u
=-\frac1{2\rho}(pu')'+Vu,
\]

with boundary conditions

\[
\cos\alpha\,u(a)+\sin\alpha\,(pu')(a)=0,
\]

\[
\cos\beta\,u(b)+\sin\beta\,(pu')(b)=0.
\]

No spectral statement below is attached merely to the differential expression \(\tau\); it concerns this fixed self-adjoint realization.

---

# 2. Uniform equivalence of weighted and unweighted norms

Since \(\rho\) is continuous and positive on the compact interval,

\[
0<\rho_-\le \rho(\lambda)\le \rho_+<\infty.
\]

Hence

\[
\rho_-\|u\|_{L^2}^2
\le
\|u\|_{\mathcal H_\rho}^2
\le
\rho_+\|u\|_{L^2}^2.
\]

Likewise, because \(p=\rho B\) is continuous and positive,

\[
0<p_-\le p(\lambda)\le p_+<\infty.
\]

Thus the energy term

\[
\frac12\int_a^b p|u'|^2d\lambda
\]

controls the ordinary \(H^1\)-seminorm.

---

# 3. Semibounded closed form

Each separated self-adjoint realization admits the standard semibounded closed quadratic form

\[
\mathfrak q_{\alpha,\beta}[u]
=
\frac12\int_a^b p|u'|^2d\lambda
+
\int_a^b V|u|^2\rho\,d\lambda
+
\text{finite real endpoint terms},
\]

on a closed subspace

\[
\mathcal Q_{\alpha,\beta}\subseteq H^1(I),
\]

where Dirichlet endpoints are imposed as trace constraints and Robin endpoints contribute finite trace terms.

Because point evaluation is continuous on \(H^1(I)\), the endpoint terms are form-bounded with respect to the \(H^1\)-norm. Since \(V\) is continuous on \([a,b]\), it is bounded below. Therefore there exists \(c\in\mathbb R\) such that

\[
\mathfrak q_{\alpha,\beta}[u]+c\|u\|_{\mathcal H_\rho}^2
\]

is equivalent to an \(H^1\)-type norm on \(\mathcal Q_{\alpha,\beta}\).

Consequently the form is closed and semibounded.

---

# 4. Theorem III.4.A — compact embedding of the form domain

## Theorem

The embedding

\[
\mathcal Q_{\alpha,\beta}
\hookrightarrow
\mathcal H_\rho
\]

is compact.

## Proof

The form norm is equivalent to an \(H^1\)-type norm on the closed subspace \(\mathcal Q_{\alpha,\beta}\subseteq H^1(I)\).

On a bounded interval, the Rellich compactness theorem gives

\[
H^1(I)\hookrightarrow L^2(I)
\]

compactly.

The weighted and unweighted \(L^2\)-norms are equivalent because \(\rho\) is positive and bounded above and below. Therefore

\[
H^1(I)\hookrightarrow \mathcal H_\rho
\]

is compact, and hence so is its restriction to \(\mathcal Q_{\alpha,\beta}\).

\[
\boxed{\mathcal Q_{\alpha,\beta}\hookrightarrow\mathcal H_\rho\text{ compactly}.}
\]

---

# 5. Theorem III.4.B — compact resolvent

## Theorem

For every separated self-adjoint realization \(H_{\alpha,\beta}\) from III.3,

\[
\boxed{(H_{\alpha,\beta}-z)^{-1}\text{ is compact}}
\]

for every \(z\in\rho(H_{\alpha,\beta})\).

## Proof

Choose \(c\) so that

\[
A:=H_{\alpha,\beta}+cI
\]

is strictly positive.

The form domain of \(A\) is \(\mathcal Q_{\alpha,\beta}\). By functional calculus,

\[
A^{-1/2}:\mathcal H_\rho\to\mathcal Q_{\alpha,\beta}
\]

is bounded when the target is equipped with the form norm.

Since the embedding

\[
\mathcal Q_{\alpha,\beta}\hookrightarrow\mathcal H_\rho
\]

is compact by III.4.A, the operator \(A^{-1/2}\), viewed as an operator from \(\mathcal H_\rho\) back into \(\mathcal H_\rho\), is compact. Therefore

\[
A^{-1}=A^{-1/2}A^{-1/2}
\]

is compact.

Compactness of one resolvent value implies compactness of every resolvent value by the resolvent identity. Therefore

\[
\boxed{H_{\alpha,\beta}\text{ has compact resolvent}.}
\]

---

# 6. Corollary III.4.C — discrete spectrum

Since \(H_{\alpha,\beta}\) is self-adjoint and has compact resolvent,

\[
\boxed{
\sigma(H_{\alpha,\beta})
=\sigma_{\mathrm{disc}}(H_{\alpha,\beta}).
}
\]

Thus the spectrum consists of real eigenvalues of finite multiplicity, which may be listed with multiplicity as

\[
E_0\le E_1\le E_2\le\cdots,
\]

and

\[
\boxed{E_n\to+\infty.}
\]

There is no finite accumulation point of the spectrum.

For the present separated scalar regular Sturm–Liouville problem one can further prove simplicity of the eigenvalues, but that stronger statement is not required for the PHISICA migration and is not used downstream here.

---

# 7. Corollary III.4.D — complete eigenfunction expansion

By the spectral theorem for self-adjoint operators with compact resolvent, there exists an orthonormal basis

\[
\{\phi_n\}_{n\ge0}
\subset\mathcal H_\rho
\]

consisting of eigenfunctions:

\[
H_{\alpha,\beta}\phi_n=E_n\phi_n.
\]

Hence every

\[
f\in\mathcal H_\rho
\]

has the Hilbert-space expansion

\[
f
=
\sum_{n=0}^{\infty}
\langle \phi_n,f\rangle_{\mathcal H_\rho}\phi_n,
\]

with convergence in \(\mathcal H_\rho\).

This recovers the legitimate content of the historical PHISICA statement that the eigenfunctions form an orthonormal basis — but only after III.1–III.3 have fixed projectability, the weighted Hilbert space, the domain and the self-adjoint boundary realization.

---

# 8. What is and is not recovered from historical PHISICA

Historical PHISICA stated, in effect,

\[
I\text{ bounded}+V_{\mathrm{eff}}\text{ bounded below}
\Rightarrow
\text{discrete spectrum}.
\]

For the regular finite-interval sector this conclusion is correct only after the missing operator hypotheses are made explicit:

1. positive regular coefficients;
2. a fixed weighted Hilbert space;
3. a self-adjoint realization with legal boundary conditions.

Thus the repaired statement is

\[
\boxed{
\text{regular finite interval}
+\text{self-adjoint realization}
\Rightarrow
\text{compact resolvent}
\Rightarrow
\text{discrete spectrum and complete eigenbasis}.
}
\]

---

# 9. Boundary / falsification

## 9.1 Self-adjointness alone is insufficient

A self-adjoint operator need not have compact resolvent. For example, multiplication by \(x\) on \(L^2(\mathbb R)\), or the free Laplacian on \(L^2(\mathbb R)\), has continuous spectrum and noncompact resolvent.

Therefore

\[
\boxed{
\text{self-adjointness}
\not\Rightarrow
\text{discrete spectrum}.
}
\]

The compactness mechanism in III.4 is the finite regular geometry/form-domain embedding, not self-adjointness by itself.

## 9.2 Eigenvalues are not a complete model invariant

Even though

\[
\sigma(H_{\alpha,\beta})=\{E_n\},
\]

nothing here implies

\[
\{E_n\}
\Rightarrow
\text{unique potential/geometry/operator realization/model}.
\]

PF07 remains active.

## 9.3 No singular-endpoint claim

The theorem does not cover infinite intervals, singular endpoints, vanishing \(p\) or \(\rho\), or general noncompact geometries. Those require separate limit-point/limit-circle and compactness analysis.

---

# 10. Source / status

The historical source contains the intended finite-interval conclusion: discrete spectrum and orthonormal eigenfunction basis. Its proof, however, suppresses the operator realization and compactness mechanism. III.4 repairs those missing hypotheses and derives the conclusion from III.3.

**STATUS:** `CLASSICAL REGULAR STURM–LIOUVILLE RESULT / PHISICA OPERATOR REPAIR`.

**PROOF DEPENDENCY:** III.2 + III.3 + compact embedding \(H^1(I)\hookrightarrow L^2(I)\) + spectral theorem for compact-resolvent self-adjoint operators.

**STRUCTURAL ANALOGY:** none needed.

**DOWNSTREAM USE:** III.5 Liouville transform; III.6 perturbation/Hellmann–Feynman; later MOST/HCube comparison.

---

# 11. Verdict

\[
\boxed{
\mathrm{III.4}
=\mathrm{PROOF\ PASS / LOCAL\ CROSS\!\!-\!CHECK\ PASS}.
}
\]

The migrated PHISICA chain is now

\[
\boxed{
\mathrm{III.1\ PROJECTABILITY}
\to
\mathrm{III.2\ WEIGHTED\ REALIZATION}
\to
\mathrm{III.3\ SELF\!\!-\!ADJOINT\ REALIZATION}
\to
\mathrm{III.4\ COMPACT\ RESOLVENT/SPECTRUM}.
}
\]
