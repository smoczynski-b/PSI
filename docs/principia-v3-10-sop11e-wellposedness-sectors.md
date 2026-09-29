# PRINCIPIA SEMANTICA — VOLUME III.10

## SOP-11E — typed well-posedness sectors

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Migration source:** `sop11e-wellposedness-migration-01.md`  
**General P2 status:** `PARTIAL`  
**Current role:** typed realization theorems; no new PSI primitive.

---

# 1. Why a sector theorem is necessary

The historical SOP-11E equation is

\[
D_t\psi=-\nabla_G L(\psi)+Z.
\]

Without a declared state space, metric, functional regularity, forcing class and operator domain this is only a formal differential expression.

III.10 does not claim universal well-posedness. It isolates two standard sectors in which existence, uniqueness and continuous dependence are actually proved.

---

# 2. Sector S — smooth forced Hilbert flow

Let \(\mathcal H\) be a real Hilbert space. Let

\[
G\in\mathcal B(\mathcal H)
\]

be self-adjoint and uniformly positive:

\[
\boxed{0<mI\le G\le MI}
\]

for some \(0<m\le M<\infty\).

Let

\[
L\in C^1(\mathcal H;\mathbb R)
\]

and assume its gradient is globally Lipschitz:

\[
\boxed{
\|\nabla L(u)-\nabla L(v)\|
\le K\|u-v\|
\qquad\forall u,v\in\mathcal H.
}
\]

Let

\[
Z\in L^1_{\mathrm{loc}}([0,\infty);\mathcal H).
\]

Consider

\[
\boxed{
\dot\psi(t)
=-G^{-1}\nabla L(\psi(t))+Z(t),
\qquad
\psi(0)=\psi_0.
}
\]

---

# 3. Theorem III.10.A — global well-posedness in Sector S

For every \(\psi_0\in\mathcal H\) there exists a unique absolutely continuous solution

\[
\psi:[0,\infty)\to\mathcal H
\]

satisfying the equation almost everywhere.

If \(\psi,\varphi\) solve the equations with initial data \(\psi_0,\varphi_0\) and forcings \(Z,W\), then

\[
\boxed{
\|\psi(t)-\varphi(t)\|
\le
 e^{Lt}\|\psi_0-\varphi_0\|
+
\int_0^t e^{L(t-s)}\|Z(s)-W(s)\|\,ds,
}
\]

where

\[
\boxed{L:=K\|G^{-1}\|\le K/m.}
\]

Hence the evolution depends continuously — quantitatively — on initial data and forcing.

## Proof

Define

\[
F(t,u):=-G^{-1}\nabla L(u)+Z(t).
\]

For almost every \(t\),

\[
\|F(t,u)-F(t,v)\|
\le
\|G^{-1}\|K\|u-v\|
=L\|u-v\|.
\]

Thus the vector field is globally Lipschitz in the state variable, with an \(L^1_{\rm loc}\) inhomogeneity in time. Standard Picard–Carathéodory theory on Banach spaces yields a unique global absolutely continuous solution.

For two solutions,

\[
\psi(t)-\varphi(t)
=
\psi_0-\varphi_0
-
\int_0^tG^{-1}
\bigl(\nabla L(\psi(s))-\nabla L(\varphi(s))\bigr)\,ds
+
\int_0^t(Z(s)-W(s))\,ds.
\]

Taking norms gives

\[
\|\psi(t)-\varphi(t)\|
\le
\|\psi_0-\varphi_0\|
+
L\int_0^t\|\psi(s)-\varphi(s)\|\,ds
+
\int_0^t\|Z(s)-W(s)\|\,ds.
\]

The inhomogeneous Gronwall inequality yields the stated estimate. \(\square\)

---

# 4. Hessian criterion

If

\[
L\in C^2(\mathcal H;\mathbb R)
\]

and

\[
\boxed{
\sup_{u\in\mathcal H}\|D^2L(u)\|\le K,
}
\]

then the mean-value identity along line segments gives

\[
\|\nabla L(u)-\nabla L(v)\|
\le K\|u-v\|.
\]

Therefore the global Hessian bound is a sufficient Bronsztejn-legal realization of the historical requirement "controla Hessianu".

By contrast, merely

\[
L\in C^2
\]

without global growth control is insufficient for global existence.

### Counterexample

On \(\mathbb R\), let

\[
L(x)=-\frac{x^3}{3},
\qquad G=1,
\qquad Z=0.
\]

Then

\[
\dot x=x^2
\]

and for \(x_0>0\)

\[
\boxed{
x(t)=\frac{x_0}{1-x_0t}
}
\]

blows up at \(t=x_0^{-1}\).

Thus

\[
\boxed{
L\in C^2
\not\Rightarrow
\text{global SOP-11E well-posedness}.
}
\]

---

# 5. Energy law in the unforced smooth sector

If \(Z=0\), then for a sufficiently regular solution,

\[
\frac{d}{dt}L(\psi(t))
=
\langle\nabla L(\psi),\dot\psi\rangle
=-
\langle\nabla L(\psi),G^{-1}\nabla L(\psi)\rangle.
\]

Because

\[
G^{-1}\ge M^{-1}I,
\]

we have

\[
\boxed{
\frac{d}{dt}L(\psi(t))
\le
-\frac1M\|\nabla L(\psi(t))\|^2
\le0.
}
\]

Thus \(L\) is a Lyapunov functional in the unforced sector.

For nonzero forcing,

\[
\frac{d}{dt}L(\psi(t))
=
-
\langle\nabla L,G^{-1}\nabla L\rangle
+
\langle\nabla L,Z(t)\rangle,
\]

so monotonicity of \(L\) is not automatic.

Permanent distinction:

\[
\boxed{
\text{well-posed forced evolution}
\not\Rightarrow
\text{energy dissipation}.
}
\]

---

# 6. Semigroup versus evolution family

If \(Z=Z(t)\) genuinely depends on time, the solution map is naturally

\[
U(t,s):\mathcal H\to\mathcal H,
\qquad t\ge s,
\]

with

\[
\boxed{
U(t,r)U(r,s)=U(t,s).
}
\]

There is no reason for

\[
U(t,0)=S(t)
\]

to satisfy the autonomous semigroup identity.

If \(Z=z\in\mathcal H\) is constant, the vector field is autonomous and uniqueness yields a semigroup

\[
S_z(t):\mathcal H\to\mathcal H.
\]

Therefore:

\[
\boxed{
\text{time-dependent forcing}
\Rightarrow
\text{evolution family, not automatically a semigroup}.
}
\]

This distinction is mandatory before applying III.9 DOM-LOGOS.

---

# 7. Sector C — convex subdifferential dynamics

Let \(\mathcal H\) be a real Hilbert space and let

\[
L:\mathcal H\to(-\infty,+\infty]
\]

be proper, lower semicontinuous and convex.

Let \(z\in\mathcal H\) be constant and define

\[
\Phi_z(u):=L(u)-\langle z,u\rangle.
\]

Then \(\Phi_z\) is proper, lsc and convex, and

\[
\partial\Phi_z=\partial L-z.
\]

---

# 8. Theorem III.10.B — maximal-monotone SOP-11E sector

The operator

\[
\partial\Phi_z
\]

is maximal monotone. Consequently

\[
A_z:=-\partial\Phi_z
\]

is m-dissipative in the nonlinear-semigroup convention and generates a unique nonlinear contraction semigroup

\[
S_z(t):\overline{D(A_z)}\to\overline{D(A_z)}.
\]

For every \(u_0,v_0\in\overline{D(A_z)}\),

\[
\boxed{
\|S_z(t)u_0-S_z(t)v_0\|
\le
\|u_0-v_0\|.
}
\]

Its trajectories are mild solutions of

\[
\boxed{
\dot u(t)
\in
-\partial L(u(t))+z.
}
\]

For initial data in the operator domain one obtains the corresponding strong solution in the standard maximal-monotone sense.

## Proof

For a proper lsc convex functional on a Hilbert space, the subdifferential is maximal monotone. Hence \(-\partial\Phi_z\) is m-dissipative. The Crandall–Liggett generation theorem produces the contraction semigroup by the exponential/resolvent formula

\[
\boxed{
S_z(t)u_0
=
\lim_{n\to\infty}
\left(
I+\frac tn\partial\Phi_z
\right)^{-n}u_0.
}
\]

The contraction estimate is part of the generated nonlinear semigroup structure. \(\square\)

---

# 9. Strong convexity refinement

If \(\Phi_z\) is \(\lambda\)-strongly convex with \(\lambda>0\), then its subdifferential is \(\lambda\)-strongly monotone. The generated flow satisfies

\[
\boxed{
\|S_z(t)u-S_z(t)v\|
\le
 e^{-\lambda t}\|u-v\|.
}
\]

If a stationary point \(u_*\) exists, it is unique and

\[
\boxed{
\|S_z(t)u-u_*\|
\le
 e^{-\lambda t}\|u-u_*\|.
}
\]

No analogous strong-convergence claim is made in the merely convex case without additional hypotheses.

---

# 10. What III.10 does not prove

III.10 does **not** prove universal well-posedness for

\[
D_t\psi=-\nabla_{G(\psi)}L(\psi)+Z.
\]

In particular it does not close, without new hypotheses:

1. arbitrary state-dependent metrics \(G(\psi)\);
2. arbitrary nonconvex functionals;
3. arbitrary unbounded non-monotone PDE generators;
4. general time-dependent forcing in the autonomous-semigroup sector;
5. compactness of attractors from coercivity alone;
6. strong convergence of every convex gradient-flow trajectory;
7. Hessian-to-transient-growth bridge P9.

Thus

\[
\boxed{
P2_{\rm general}=PARTIAL
}
\]

remains the correct project-level status.

---

# 11. Relation to III.9 DOM-LOGOS

The logical order is now explicit:

\[
\boxed{
\text{well-posed evolution}
\to
\text{identify semigroup/evolution-family structure}
\to
\text{test DOM-LOGOS projectability}.
}
\]

For autonomous sectors S or C, III.9 may be applied to the generated semigroup.

For genuinely nonautonomous Sector S with \(Z(t)\), the correct reduction object is an evolution family/cocycle; III.9 in its current semigroup form cannot be imported word-for-word.

Permanent distinction:

\[
\boxed{
\text{well-posedness}
\neq
\text{projectability}.
}
\]

---

# 12. Relation to historical SOP-11 local stability

The 2026-07-26A source gives, near a stationary state,

\[
A_0=-G^{-1}H,
\qquad
B_0=G^{-1/2}HG^{-1/2},
\]

and under \(B_0\ge\mu I\),

\[
\|e^{tA_0}\|_G\le e^{-\mu t}.
\]

III.10 clarifies that this is a linearized stability result after an evolution has been legally defined. It does not establish nonlinear global existence.

Thus:

\[
\boxed{
\text{linearized semigroup decay}
\not\Rightarrow
\text{global nonlinear well-posedness}.
}
\]

---

# 13. Local cross-check

### Source status
`PASS`: KANON2 general P2 remains PARTIAL; 2026-07-26A supplies only a narrower local stability sector.

### Smooth sector
`PASS`: global Lipschitz control gives global existence, uniqueness and quantitative continuous dependence.

### C2 boundary
`PASS`: explicit finite-time blow-up witness prevents promotion of bare C2 regularity to global well-posedness.

### Forcing type
`PASS`: nonautonomous forcing is classified as an evolution family rather than silently called a semigroup.

### Convex sector
`PASS`: maximal monotonicity + Crandall–Liggett closes the autonomous convex/subdifferential class.

### Attractor boundary
`PASS`: coercivity is not used as a substitute for compactness.

### DOM-LOGOS relation
`PASS`: well-posedness and projectability remain distinct gates.

### CORE status
`PASS`: no new PSI primitive is introduced.

---

# 14. Verdict

\[
\boxed{
\mathrm{III.10\ SOP\!-\!11E}
=
\mathrm{THEOREM\ PROSE\ PASS\ 01 / PROOF\ PASS / LOCAL\ CROSS\!-
CHECK\ PASS}.
}
\]

with

\[
\boxed{
P2_{\mathrm{general}}=PARTIAL.
}
\]

The next required process step is a composition cross-check of III.9–III.10 and the historical SOP-11 local stability block before opening any further SOP/P9 theorem prose.