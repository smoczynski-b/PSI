# PRINCIPIA SEMANTICA — VOLUME III.6

## Perturbacja operatorowa, stabilność widma i twierdzenie Hellmanna–Feynmana

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Upstream:** `principia-v3-04-compact-resolvent-spectrum.md`, `principia-v3-05-liouville-normal-form.md`  
**Historical source:** `PHISICA — NEW.pdf`, former “Deformacje struktury LOGOS i stabilność widma” section  
**Scope:** fixed-Hilbert-space self-adjoint perturbations after legal unitary trivialization

---

# 1. Purpose

Historical PHISICA correctly invokes first-order perturbation theory in the schematic form

\[
\widetilde H\mapsto \widetilde H+\varepsilon W,
\qquad
\delta E_n=\langle\phi_n,W\phi_n\rangle,
\]

but it does not state the operator hypotheses needed to license that formula and then promotes it to a broad claim that small structural deformations imply small spectral changes.

The repaired unit separates:

1. fixed-Hilbert-space bounded self-adjoint perturbations;
2. continuity/Lipschitz stability of ordered eigenvalues;
3. differentiability of a simple isolated eigenvalue branch;
4. the Hellmann–Feynman identity;
5. degenerate first-order splitting;
6. geometric deformations whose Hilbert spaces/domains vary and therefore require a prior unitary trivialization.

Permanent rule:

\[
\boxed{
\text{small coefficient deformation}
\neq
\text{licensed spectral perturbation theorem}.
}
\]

---

# 2. Canonical fixed-space contract

Let

\[
\mathcal H=L^2(J,dx),
\qquad
J=(0,L),
\]

and let

\[
H_0:D(H_0)\subset\mathcal H\to\mathcal H
\]

be one of the self-adjoint compact-resolvent Schrödinger realizations obtained from III.5:

\[
H_0=-\frac12\partial_x^2+Q_0(x),
\]

with fixed separated self-adjoint boundary conditions.

Let

\[
W(t)=W(t)^*\in\mathcal B(\mathcal H),
\qquad t\in(-t_0,t_0),
\]

be norm-\(C^1\) in \(t\), and define

\[
\boxed{
H(t)=H_0+W(t),
\qquad
D(H(t))=D(H_0).
}
\]

This is the clean canonical perturbation sector for the current PHISICA migration.

A particularly important case is multiplication by a real bounded potential perturbation

\[
W(t)=M_{q(t)},
\qquad
q(t)\in L^\infty(J;\mathbb R).
\]

---

# 3. Theorem III.6.A — self-adjointness and compact resolvent survive bounded perturbation

## Theorem

For every \(t\),

\[
\boxed{H(t)=H(t)^*}
\]

on the fixed domain \(D(H_0)\). If \(H_0\) has compact resolvent, then so does \(H(t)\).

## Proof

Because \(W(t)\) is bounded and self-adjoint, the bounded-perturbation theorem for self-adjoint operators gives

\[
H_0+W(t)=H(t)^*
\]

on the unchanged domain \(D(H_0)\).

Fix \(z\) in the common resolvent set locally, or equivalently choose a sufficiently negative real \(z\). The resolvent identity gives

\[
(H(t)-z)^{-1}
=
(H_0-z)^{-1}
-
(H(t)-z)^{-1}W(t)(H_0-z)^{-1}.
\]

The first term is compact by III.4. In the second term, \((H_0-z)^{-1}\) is compact and the remaining factors are bounded, hence the product is compact. Therefore \((H(t)-z)^{-1}\) is compact.

Compactness at one resolvent point implies compactness at all resolvent points.

Thus

\[
\boxed{
H(t)\text{ remains self-adjoint with compact resolvent.}
}
\]

---

# 4. Theorem III.6.B — quantitative eigenvalue stability for bounded perturbations

Let the eigenvalues of \(H(t)\), repeated according to multiplicity, be ordered as

\[
E_0(t)\le E_1(t)\le\cdots,
\qquad
E_n(t)\to+\infty.
\]

## Theorem

For all \(s,t\) in the perturbation interval,

\[
\boxed{
|E_n(t)-E_n(s)|
\le
\|W(t)-W(s)\|_{\mathcal B(\mathcal H)}
}
\]

for every \(n\).

In the multiplication-potential case,

\[
\boxed{
|E_n(t)-E_n(s)|
\le
\|q(t)-q(s)\|_{L^\infty(J)}.
}
\]

## Proof

Set

\[
K:=W(t)-W(s)=K^*.
\]

Then for every normalized \(u\in D(H_0)\),

\[
-\|K\|
\le
\langle u,Ku\rangle
\le
\|K\|.
\]

Hence, in the form order,

\[
H(s)-\|K\|I
\le
H(t)
\le
H(s)+\|K\|I.
\]

Applying the min–max principle to the compact-resolvent self-adjoint operators gives

\[
E_n(s)-\|K\|
\le
E_n(t)
\le
E_n(s)+\|K\|.
\]

This is the claimed bound.

Thus the historical statement “small perturbations produce small spectral changes” becomes valid only after a norm/topology and a perturbation class have been specified.

---

# 5. Theorem III.6.C — simple isolated eigenvalue branch

Fix \(t_*\). Suppose

\[
E_*(t_*)
\]

is a simple isolated eigenvalue of \(H(t_*)\).

Then there exists a neighbourhood of \(t_*\) and \(C^1\) functions

\[
E(t)\in\mathbb R,
\qquad
\phi(t)\in D(H_0),
\qquad
\|\phi(t)\|=1,
\]

such that

\[
H(t)\phi(t)=E(t)\phi(t),
\qquad
E(t_*)=E_*(t_*).
\]

## Proof sketch

Because \(t\mapsto W(t)\) is norm-\(C^1\), the resolvent depends \(C^1\) on \(t\) near a contour enclosing only \(E_*(t_*)\). The associated Riesz projection

\[
P(t)
=
\frac1{2\pi i}
\oint_\Gamma
(z-H(t))^{-1}\,dz
\]

is therefore \(C^1\) and has rank one for \(t\) sufficiently close to \(t_*\). A normalized \(C^1\) vector may be chosen in \(\operatorname{Ran}P(t)\), yielding the branch above.

This is the precise local content behind the scalar first-order perturbation formula.

---

# 6. Theorem III.6.D — Hellmann–Feynman

Under the hypotheses of III.6.C,

\[
\boxed{
E'(t)
=
\langle\phi(t),W'(t)\phi(t)\rangle.
}
\]

Equivalently, because \(H'(t)=W'(t)\) on the fixed domain,

\[
\boxed{
E'(t)
=
\langle\phi(t),H'(t)\phi(t)\rangle.
}
\]

## Proof

Differentiate

\[
H(t)\phi(t)=E(t)\phi(t).
\]

This gives

\[
H'(t)\phi(t)+H(t)\phi'(t)
=
E'(t)\phi(t)+E(t)\phi'(t).
\]

Take the inner product with \(\phi(t)\). Since \(H(t)\) is self-adjoint and

\[
H(t)\phi(t)=E(t)\phi(t),
\]

we have

\[
\langle\phi,H\phi'\rangle
=
E\langle\phi,\phi'\rangle.
\]

These terms cancel from both sides, while \(\|\phi(t)\|=1\). Therefore

\[
E'(t)
=
\langle\phi(t),H'(t)\phi(t)\rangle.
\]

For a pure potential perturbation

\[
H(t)=-\frac12\partial_x^2+Q(t,x)
\]

with fixed domain and \(Q'(t,\cdot)\in L^\infty\), this becomes

\[
\boxed{
E'(t)
=
\int_J
|\phi(t,x)|^2\,\partial_tQ(t,x)\,dx.
}
\]

This is the clean PHISICA Hellmann–Feynman formula.

---

# 7. Degenerate eigenvalues — no scalar shortcut

Suppose \(E\) is an isolated eigenvalue of \(H_0\) of multiplicity \(m>1\), and consider the affine perturbation

\[
H(t)=H_0+tW,
\qquad
W=W^*\in\mathcal B(\mathcal H).
\]

Let

\[
P
\]

be the orthogonal projection onto the eigenspace

\[
\mathcal E=\ker(H_0-E).
\]

Then the first-order splitting is governed not by one expectation value but by the finite-dimensional self-adjoint operator

\[
\boxed{
W_E:=PWP|_{\mathcal E}.
}
\]

If

\[
\mu_1,\ldots,\mu_m
\]

are its eigenvalues, then the eigenvalue branches emerging from \(E\) satisfy

\[
\boxed{
E_j(t)
=E+t\mu_j+o(t).
}
\]

Thus an arbitrary normalized vector \(\phi\in\mathcal E\) does **not** define a unique scalar first-order correction unless it is chosen in the appropriate eigenbasis of the compressed perturbation.

Permanent rule:

\[
\boxed{
\text{degeneracy}
\Rightarrow
\text{matrix perturbation on the eigenspace, not naive scalar HF}.
}
\]

---

# 8. Geometric / LOGOS deformations require trivialization first

Historical PHISICA begins from

\[
\Lambda\mapsto\Lambda+\varepsilon\eta
\]

and computes variations of \(B,C,\rho\). Those calculations may be useful local coefficient derivatives, but they do not yet define a perturbation family on one fixed Hilbert space and one fixed operator domain.

Indeed a deformation of \(\Lambda\) can change:

- \(B_\varepsilon\) and \(\rho_\varepsilon\);
- the weighted Hilbert space \(L^2(I_\varepsilon,\rho_\varepsilon d\lambda)\);
- the Liouville coordinate \(x_\varepsilon\);
- the Liouville interval length \(L_\varepsilon\);
- transformed boundary coefficients;
- the unitary map \(U_\varepsilon\) itself.

Therefore the raw symbolic expression

\[
W
=-\frac12\delta B\,\partial_\lambda^2
+\delta V_{\rm eff}
\]

is not, by itself, a licensed derivative \(H'(0)\) of self-adjoint operators on a fixed Hilbert space.

The legal procedure is:

\[
\boxed{
H_\varepsilon
\xrightarrow{\ U_\varepsilon\ }
\widehat H_\varepsilon
:=
U_\varepsilon H_\varepsilon U_\varepsilon^{-1}
}
\]

on one chosen reference Hilbert space, followed by a proof that

\[
\varepsilon\mapsto\widehat H_\varepsilon
\]

is differentiable in a fixed-domain operator sense or in a controlled closed-form sense.

Only then does Hellmann–Feynman apply, and the derivative is

\[
\widehat H_\varepsilon',
\]

which includes the contribution of the parameter-dependent trivialization. One must not identify it mechanically with the coefficient-wise variation written before the trivialization.

---

# 9. Relation to III.5 and the Liouville interval

III.5 gives, for each legal regular model, a unitary normal form

\[
UHU^{-1}
=-\frac12\partial_x^2+Q(x).
\]

If a perturbation family is such that after a common trivialization:

- the reference interval \(J\) is fixed;
- the self-adjoint boundary domain is fixed;
- only the bounded real potential \(Q(t,\cdot)\) varies norm-\(C^1\),

then III.6 applies directly with

\[
W(t)=M_{Q(t)-Q(0)}.
\]

This is the preferred canonical PHISICA perturbation sector.

If the Liouville interval or boundary realization varies, an additional unitary identification with a fixed reference interval/domain is required before any scalar HF formula is asserted.

---

# 10. What is recovered from historical PHISICA

The source-level statement

\[
\delta E_n
=
\langle\phi_n,W\phi_n\rangle
\]

is recovered as the local Hellmann–Feynman derivative for a simple isolated eigenvalue branch under the fixed-space/fixed-domain differentiability contract.

The historical global statement

\[
\text{small deformation of LOGOS}
\Rightarrow
\text{small spectral deformation}
\]

is **not** retained without qualification.

A correct quantitative version in the canonical bounded-perturbation sector is

\[
\boxed{
|E_n(t)-E_n(s)|
\le
\|W(t)-W(s)\|.
}
\]

For bounded potential perturbations this becomes

\[
\boxed{
|E_n(t)-E_n(s)|
\le
\|Q(t)-Q(s)\|_\infty.
}
\]

Thus spectral stability is a theorem relative to an explicit perturbation topology, not a consequence of the adjective “small”.

---

# 11. Boundary / falsification

## 11.1 PF08 remains active

The scalar formula

\[
E'(t)=\langle\phi,H'\phi\rangle
\]

is not licensed without a differentiable self-adjoint family and an appropriate eigenvalue branch.

## 11.2 PF09 remains active

Pointwise-small changes of \(B,C,V\) do not by themselves imply norm-resolvent, form, or eigenvalue stability.

## 11.3 Eigenvectors may be unstable near crossings

Even when ordered eigenvalues are Lipschitz under bounded perturbations, individual eigenvectors or labels of branches need not vary smoothly through degeneracies. Therefore

\[
\boxed{
\text{stable eigenvalues}
\not\Rightarrow
\text{stable eigenvectors / stable spectral DNA labels}.
}
\]

## 11.4 No variable-domain shortcut

A family with parameter-dependent boundary conditions or Hilbert spaces is outside Theorem III.6.D until it has been placed in a fixed-space/domain or controlled closed-form framework.

---

# 12. Classical status

The unit is a classical perturbation-theoretic bridge:

- bounded self-adjoint perturbation preserves self-adjointness on a fixed domain;
- compact resolvent is preserved under bounded perturbations;
- min–max gives the eigenvalue norm bound;
- a simple isolated eigenvalue admits a local differentiable branch under norm-\(C^1\) perturbation;
- Hellmann–Feynman follows by differentiating the eigenvalue equation;
- degenerate first-order splitting is governed by the compressed perturbation on the eigenspace.

Parameter-dependent domains require a more general perturbation framework and are not silently covered by the fixed-domain theorem.

**STATUS:** `CLASSICAL SELF-ADJOINT PERTURBATION THEORY / PHISICA OPERATOR REPAIR`.

**PROOF DEPENDENCY:** III.4 + III.5 + fixed-space perturbation contract.

**DOWNSTREAM USE:** PHISICA whole-block cross-check; later MOST/HCube stability comparisons.

---

# 13. Verdict

\[
\boxed{
\mathrm{III.6}
=\mathrm{PROOF\ PASS / LOCAL\ CROSS\!\!-\!CHECK\ PASS}.
}
\]

The repaired PHISICA chain is now locally complete:

\[
\boxed{
\mathrm{III.1\ PROJECTABILITY}
\to
\mathrm{III.2\ WEIGHT}
\to
\mathrm{III.3\ SELF\!\!-\!ADJOINTNESS}
\to
\mathrm{III.4\ COMPACT\ RESOLVENT/SPECTRUM}
\to
\mathrm{III.5\ UNITARY\ LIOUVILLE}
\to
\mathrm{III.6\ PERTURBATION/HF}.
}
\]

Next mandatory gate:

\[
\boxed{
\mathrm{PHISICA\ WHOLE\!\!-\!BLOCK\ CROSSCHECK\ 01}.
}
\]
