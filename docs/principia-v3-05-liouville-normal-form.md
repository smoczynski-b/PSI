# PRINCIPIA SEMANTICA — VOLUME III.5

## Transformacja Liouville’a, unitarny transport i postać normalna

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Upstream:** `principia-v3-03-domain-selfadjoint.md`, `principia-v3-04-compact-resolvent-spectrum.md`  
**Historical source:** `PHISICA — NEW.pdf`, former “gauge transform / drift elimination” section  
**Scope:** regular finite-interval self-adjoint Sturm–Liouville realizations

---

# 1. Purpose

Historical PHISICA uses the substitution

\[
\psi=e^{\beta}\phi,
\qquad
\beta'=-\frac{C}{2B},
\]

to eliminate the first-derivative term in

\[
H
=-\frac12(B\partial_\lambda^2+C\partial_\lambda)+V.
\]

The algebraic cancellation is correct, but by itself it does not identify Hilbert spaces, transport the operator domain, or prove unitary equivalence.

The current unit separates:

1. the historical multiplicative similarity in the \(\lambda\)-coordinate;
2. the full Liouville transform, which is unitary and sends the self-adjoint realization to a standard Schrödinger operator in ordinary \(L^2\).

Permanent rule:

\[
\boxed{
\text{formal drift removal}
\neq
\text{unitary Liouville equivalence}.
}
\]

---

# 2. Contract

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
B,\rho\in C^2([a,b]),
\qquad
B>0,
\qquad
\rho>0,
\]

and

\[
V\in C([a,b];\mathbb R).
\]

Set

\[
p=\rho B.
\]

Let

\[
H_{\theta_a,\theta_b}
\]

be one of the separated self-adjoint realizations from III.3, with the former boundary parameters \(\alpha,\beta\) renamed here to \(\theta_a,\theta_b\) so that \(\beta(\lambda)\) is reserved exclusively for the historical multiplier:

\[
H_{\theta_a,\theta_b}u
=-\frac1{2\rho}(pu')'+Vu.
\]

The strengthened \(C^2\) regularity is used only to write the transformed effective potential pointwise.

---

# 3. Historical multiplicative transform as a similarity

From III.2,

\[
(\rho B)'=\rho C,
\]

hence

\[
\frac{C}{B}
=
\frac{(\rho B)'}{\rho B}
=
(\log(\rho B))'.
\]

Therefore the historical equation

\[
\beta'=-\frac{C}{2B}
\]

gives

\[
\boxed{
\beta
=-\frac12\log(\rho B)+\mathrm{const}.
}
\]

Thus

\[
e^\beta\propto(\rho B)^{-1/2}.
\]

Because \(\rho B\) is positive and continuous on the compact interval, multiplication by \(e^\beta\) is bounded and boundedly invertible on \(\mathcal H_\rho\).

Define

\[
M_\beta\phi=e^\beta\phi.
\]

If one transports the domain exactly,

\[
D(\widehat H_\beta)
=M_\beta^{-1}D(H_{\theta_a,\theta_b}),
\]

and defines

\[
\widehat H_\beta
=M_\beta^{-1}H_{\theta_a,\theta_b}M_\beta,
\]

then \(\widehat H_\beta\) is boundedly similar to \(H_{\theta_a,\theta_b}\) and therefore has the same spectrum.

At the level of differential expressions,

\[
\widehat H_\beta
=-\frac12 B(\lambda)\partial_\lambda^2
+V_{\mathrm{hist}}(\lambda),
\]

where

\[
V_{\mathrm{hist}}
=V+V_{\mathrm{geom}}^{\mathrm{hist}},
\]

\[
V_{\mathrm{geom}}^{\mathrm{hist}}
=
\frac{C'}4
-\frac{CB'}{4B}
+\frac{C^2}{8B}.
\]

This recovers the historical algebraic formula.

However,

\[
\boxed{
M_\beta\text{ is not generally unitary in }\mathcal H_\rho.
}
\]

Consequently this similarity does not by itself make the transformed differential expression a self-adjoint Schrödinger operator in the unchanged weighted Hilbert space.

---

# 4. Liouville coordinate

Define

\[
\boxed{
x=\chi(\lambda)
:=
\int_a^\lambda B(\mu)^{-1/2}\,d\mu.
}
\]

Since \(B>0\) on \([a,b]\), \(\chi\) is strictly increasing and maps \([a,b]\) diffeomorphically onto

\[
J=[0,L],
\qquad
L=\int_a^b B(\mu)^{-1/2}d\mu<\infty.
\]

Thus

\[
\frac{dx}{d\lambda}=B^{-1/2},
\qquad
\frac{d}{d\lambda}=B^{-1/2}\frac{d}{dx}.
\]

---

# 5. Liouville amplitude and the unitary map

Define

\[
\boxed{
s(\lambda)
:=
\rho(\lambda)^{1/2}B(\lambda)^{1/4}.
}
\]

Equivalently,

\[
s=(p\rho)^{1/4}.
\]

Define

\[
U:\mathcal H_\rho\to L^2(J,dx)
\]

by

\[
\boxed{
(Uu)(x)
=s(\lambda(x))u(\lambda(x)).
}
\]

## Theorem III.5.A — unitarity

\[
\boxed{U\text{ is unitary}.}
\]

## Proof

Because

\[
dx=B^{-1/2}d\lambda
\]

and

\[
s^2=\rho\sqrt B,
\]

we have

\[
\begin{aligned}
\|Uu\|_{L^2(J)}^2
&=
\int_J |s(\lambda(x))u(\lambda(x))|^2dx\\
&=
\int_I s(\lambda)^2|u(\lambda)|^2B(\lambda)^{-1/2}d\lambda\\
&=
\int_I \rho(\lambda)|u(\lambda)|^2d\lambda\\
&=
\|u\|_{\mathcal H_\rho}^2.
\end{aligned}
\]

Surjectivity follows from the inverse formula

\[
(U^{-1}\phi)(\lambda)
=s(\lambda)^{-1}\phi(\chi(\lambda)).
\]

---

# 6. Theorem III.5.B — unitary Liouville normal form

Let

\[
\widetilde H_{\theta_a,\theta_b}
:=
U H_{\theta_a,\theta_b}U^{-1}
\]

with domain

\[
D(\widetilde H_{\theta_a,\theta_b})
=U D(H_{\theta_a,\theta_b}).
\]

Then

\[
\boxed{
\widetilde H_{\theta_a,\theta_b}
=-\frac12\frac{d^2}{dx^2}
+Q(x)
}
\]

where

\[
\boxed{
Q(x)
=
V(\lambda(x))
+
\frac{1}{2}\frac{s_{xx}(x)}{s(x)}.
}
\]

Here \(s(x)\) denotes \(s(\lambda(x))\).

## Proof

Write

\[
\phi=Uu=su,
\qquad
u=\frac{\phi}{s}.
\]

Using

\[
\frac{d}{d\lambda}=B^{-1/2}\frac{d}{dx}
\]

and

\[
p=\rho B,
\qquad
s^2=\rho\sqrt B,
\]

we obtain

\[
pu_\lambda
=s^2u_x.
\]

Since

\[
u_x
=\frac{\phi_x}{s}-\frac{s_x}{s^2}\phi,
\]

it follows that

\[
s^2u_x
=s\phi_x-s_x\phi.
\]

Differentiating with respect to \(x\),

\[
\frac{d}{dx}(s^2u_x)
=s\phi_{xx}-s_{xx}\phi.
\]

Also

\[
\frac1\rho\frac{d}{d\lambda}
=
\frac1{\rho\sqrt B}\frac{d}{dx}
=
\frac1{s^2}\frac{d}{dx}.
\]

Therefore

\[
-\frac1{2\rho}(pu_\lambda)_\lambda
=
-\frac1{2s^2}
\left(s\phi_{xx}-s_{xx}\phi\right).
\]

Multiplying by \(s\), as required by \(U\), gives

\[
U\left[-\frac1{2\rho}(pu')'\right]U^{-1}\phi
=
-\frac12\phi_{xx}
+
\frac{s_{xx}}{2s}\phi.
\]

The potential term transforms by composition:

\[
U(Vu)=V(\lambda(x))\phi.
\]

Hence the asserted formula follows.

---

# 7. Boundary conditions under the unitary transform

The original separated condition at \(a\) is

\[
\cos\theta_a\,u(a)
+
\sin\theta_a\,(pu')(a)=0.
\]

Since

\[
u=\phi/s,
\qquad
pu'=s\phi_x-s_x\phi,
\]

this becomes, at \(x=0\),

\[
\boxed{
\bigl(\cos\theta_a-\sin\theta_a\,s s_x\bigr)\phi
+
\sin\theta_a\,s^2\phi_x
=0.
}
\]

At \(x=L\), the corresponding condition is

\[
\boxed{
\bigl(\cos\theta_b-\sin\theta_b\,s s_x\bigr)\phi
+
\sin\theta_b\,s^2\phi_x
=0.
}
\]

Thus separated real boundary conditions remain separated real boundary conditions after the Liouville transport.

More importantly, self-adjointness does not need to be re-proved from the differential expression:

\[
\boxed{
\widetilde H_{\theta_a,\theta_b}
=U H_{\theta_a,\theta_b}U^{-1}
}
\]

is self-adjoint because \(U\) is unitary and \(H_{\theta_a,\theta_b}\) is self-adjoint.

---

# 8. Spectral consequences

Unitary equivalence gives

\[
\boxed{
\sigma(\widetilde H_{\theta_a,\theta_b})
=
\sigma(H_{\theta_a,\theta_b}).
}
\]

The spectral type, multiplicities, compact-resolvent property and orthonormal eigenbasis are preserved.

If

\[
H_{\theta_a,\theta_b}u_n=E_nu_n,
\]

then

\[
\phi_n=Uu_n
\]

satisfies

\[
\widetilde H_{\theta_a,\theta_b}\phi_n=E_n\phi_n.
\]

Thus III.4 passes unchanged to the Liouville normal form.

---

# 9. Relation between the historical and canonical transforms

The historical transform uses

\[
e^\beta\propto(\rho B)^{-1/2}.
\]

The unitary Liouville amplitude is

\[
s^{-1}
=
\rho^{-1/2}B^{-1/4}.
\]

Therefore the historical multiplication is not the full Liouville transform. It removes the first derivative in the original coordinate \(\lambda\), whereas the canonical unitary transform additionally changes coordinate by

\[
dx=B^{-1/2}d\lambda
\]

and uses the amplitude required by the Hilbert-space Jacobian.

Hence:

\[
\boxed{
\text{historical }e^\beta
=\text{valid drift-killing similarity factor},
}
\]

but

\[
\boxed{
\text{full Liouville equivalence}
=\text{coordinate change + unitary amplitude + transported domain}.
}
\]

---

# 10. Boundary / falsification

## 10.1 Formal cancellation is insufficient

The identity

\[
2B\beta'+C=0
\]

only removes a coefficient in a formal differential expression.

Without transporting the domain,

\[
\boxed{
\text{formal drift removal}
\not\Rightarrow
\text{operator similarity or spectral equivalence}.
}
\]

PF05 remains active.

## 10.2 Similarity is not unitarity

Even after the historical multiplication is promoted to a bounded similarity on the regular compact interval,

\[
M_\beta^{-1}HM_\beta
\]

need not be self-adjoint in the original weighted inner product.

Thus:

\[
\boxed{
\text{isospectral bounded similarity}
\not\Rightarrow
\text{unitary equivalence / preserved self-adjointness in the same metric}.
}
\]

## 10.3 No singular transform claim

The present theorem assumes positive regular \(B,\rho\) on a finite interval. If \(B\) or \(\rho\) vanish, or if the transformed interval is infinite, the unitary map may still exist in another contract but the present proof and downstream compactness statements must be re-audited.

---

# 11. Source / classical bridge

The historical PHISICA source correctly computes the multiplier condition

\[
\beta'=-\frac{C}{2B}
\]

and the resulting formal potential

\[
V_{\mathrm{geom}}^{\mathrm{hist}}
=
\frac{C'}4
-\frac{CB'}{4B}
+\frac{C^2}{8B}.
\]

Its claim of spectral invariance becomes correct only after one specifies an operator similarity with the transported domain.

The stronger canonical construction used here is the classical Liouville transformation for Sturm–Liouville systems:

\[
x=\int\sqrt{w/p}\,d\lambda,
\qquad
\phi=(pw)^{1/4}u,
\]

specialized to

\[
p=\rho B,
\qquad
w=\rho.
\]

**STATUS:** `CLASSICAL LIOUVILLE NORMAL FORM / PHISICA OPERATOR REPAIR`.

**PROOF DEPENDENCY:** III.2 + III.3; III.4 supplies spectral consequences after unitary equivalence.

**DOWNSTREAM USE:** III.6 perturbation/Hellmann–Feynman on a fixed standard Hilbert space.

---

# 12. Verdict

\[
\boxed{
\mathrm{III.5}
=\mathrm{PROOF\ PASS / LOCAL\ CROSS\!\!-\!CHECK\ PASS}.
}
\]

The repaired PHISICA operator chain is now

\[
\boxed{
\mathrm{III.1\ PROJECTABILITY}
\to
\mathrm{III.2\ WEIGHTED\ REALIZATION}
\to
\mathrm{III.3\ SELF\!\!-\!ADJOINT\ REALIZATION}
\to
\mathrm{III.4\ COMPACT\ SPECTRAL\ THEORY}
\to
\mathrm{III.5\ UNITARY\ LIOUVILLE\ NORMAL\ FORM}.
}
\]
