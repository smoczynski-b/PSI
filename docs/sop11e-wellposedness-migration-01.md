# SOP-11E WELL-POSEDNESS MIGRATION 01

**Status:** `MIGRATION GATE PASS / GENERAL P2 REMAINS PARTIAL / TYPED SECTORS IDENTIFIED`  
**Date:** 2026-09-29

---

# 1. Source hierarchy

The active project source `KANON2.txt` classifies

\[
D_t\psi=-\nabla_G L+Z
\]

as `P2 — DOBRZE POSTAWIONA DYNAMIKA SOP-11E`, requiring existence, uniqueness and continuous dependence, with explicit demands for regularity/Hessian control, semigroup estimates and operator domains. Its status is `PARTIAL`.

The earlier consolidated source `PRINCIPIA_SEMANTICA_KANON_SCALONY_2026-07-26A.tex` canonizes only a narrower local operator-energy sector: a Hilbert space, a positive metric, a C2 functional, linearization by the Hessian, and semigroup decay estimates under a positive Hessian gap.

A genealogical Library note contains classical imports from maximal-monotone and nonlinear-semigroup theory. These imports are useful, but they do not by themselves close the project-level general P2 problem.

Therefore:

\[
\boxed{
\text{general SOP-11E well-posedness remains PARTIAL.}
}
\]

---

# 2. What can be promoted

Two typed sectors are mature enough for theorem prose.

## Sector S — smooth Hilbert evolution with controlled Hessian

Take a real Hilbert space \(\mathcal H\), a fixed bounded self-adjoint coercive operator

\[
0<mI\le G\le MI,
\]

and a functional \(L\in C^1(\mathcal H;\mathbb R)\) whose gradient is globally Lipschitz:

\[
\|\nabla L(u)-\nabla L(v)\|\le K\|u-v\|.
\]

A sufficient C2 condition is a global Hessian bound

\[
\sup_{u\in\mathcal H}\|D^2L(u)\|\le K.
\]

With forcing \(Z\in L^1_{\mathrm{loc}}([0,\infty);\mathcal H)\), the equation

\[
\dot\psi=-G^{-1}\nabla L(\psi)+Z(t)
\]

is a globally well-posed Carathéodory evolution.

If \(Z\) is time dependent, this defines an evolution family/process, not an autonomous semigroup.

If \(Z=z\) is constant, the equation is autonomous and its flow is a semigroup.

## Sector C — convex subdifferential flow

Let \(L:\mathcal H\to(-\infty,+\infty]\) be proper, lower semicontinuous and convex. Then

\[
\partial L
\]

is maximal monotone and

\[
A=-\partial L
\]

is m-dissipative in the standard Hilbert convention. Crandall–Liggett therefore generates a nonlinear contraction semigroup on the closure of its domain.

For constant forcing \(z\in\mathcal H\), define

\[
L_z(u)=L(u)-\langle z,u\rangle.
\]

Then

\[
\partial L_z=\partial L-z,
\]

so the autonomous inclusion

\[
\dot\psi\in-\partial L(\psi)+z
\]

belongs to the same maximal-monotone sector.

---

# 3. What is not promoted

The following statements remain illegal without extra hypotheses.

### 3.1 C2 does not imply global existence

Even in one dimension,

\[
L(x)=-\frac{x^3}{3}
\]

is C∞, but

\[
\dot x=-L'(x)=x^2
\]

has

\[
x(t)=\frac{x_0}{1-x_0t}
\]

for \(x_0>0\), hence finite-time blow-up.

Therefore:

\[
\boxed{L\in C^2\not\Rightarrow\text{global SOP-11E well-posedness}.}
\]

A global growth/Lipschitz/monotonicity mechanism is required.

### 3.2 Time-dependent forcing does not define a semigroup

For general \(Z(t)\), the solution operator has two time arguments

\[
U(t,s),
\]

and satisfies the cocycle/evolution law

\[
U(t,r)U(r,s)=U(t,s),
\]

not in general

\[
S(t+s)=S(t)S(s).
\]

Hence:

\[
\boxed{
\text{well-posed nonautonomous flow}
\neq
\text{autonomous semigroup}.
}
\]

### 3.3 Coercivity alone does not imply a compact global attractor

The older working synthesis overstated this point. In an infinite-dimensional Hilbert space, let \(C\) be the closed unit ball and

\[
L(x)=\operatorname{dist}(x,C)^2.
\]

Then \(L\) is coercive and every point of \(C\) is a minimizer/equilibrium. Since \(C\) is not compact in norm, no compact global attractor can contain all equilibria.

Therefore compactness requires additional compact-sublevel/asymptotic-compactness hypotheses.

### 3.4 Convexity does not imply strong convergence of every orbit without further structure

The contraction semigroup theorem gives well-posedness. Strong convergence to one minimizer is a separate asymptotic theorem and requires additional hypotheses unless strong convexity supplies a spectral/monotonicity gap.

---

# 4. Relation to III.9 DOM-LOGOS

III.9 requires a well-defined original and reduced evolution before semigroup projectability can be used globally.

This migration clarifies the legal order:

\[
\boxed{
\text{well-posed evolution}
\to
\text{semigroup/evolution family type}
\to
\text{DOM-LOGOS projectability}.
}
\]

One must not use the infinitesimal identity

\[
D\Lambda(x)Ax=\bar A\Lambda(x)
\]

as a substitute for existence and uniqueness of the underlying evolution.

---

# 5. Relation to old SOP-11 local stability

The 2026-07-26A source contains a local linearized gradient sector:

\[
A_0=-G^{-1}H,
\qquad
B_0=G^{-1/2}HG^{-1/2}=B_0^*,
\]

and, when \(B_0\ge\mu I\),

\[
\|e^{tA_0}\|_G\le e^{-\mu t}.
\]

This is a stability theorem **after** a well-defined local linearization exists. It is not a substitute for nonlinear existence/uniqueness.

Permanent distinction:

\[
\boxed{
\text{linearized stability}
\neq
\text{nonlinear well-posedness}.
}
\]

---

# 6. Classical provenance

The nonlinear contraction-semigroup import is classical. The project does not claim authorship of:

- maximal monotonicity of subdifferentials of proper lsc convex functionals;
- Crandall–Liggett generation for m-accretive/m-dissipative operators;
- standard Banach/Hilbert ODE well-posedness for globally Lipschitz vector fields.

The project contribution is the typed migration into SOP-11E and the separation of autonomous semigroup, nonautonomous evolution family, local stability and full project-level P2.

---

# 7. Gate verdict

\[
\boxed{
\mathrm{SOP\!-\!11E\ WELL\!-
POSEDNESS\ MIGRATION\ GATE}=PASS.
}
\]

But:

\[
\boxed{
P2_{\mathrm{general}}=PARTIAL.
}
\]

The gate authorizes one theorem unit containing the two typed closed sectors, with explicit prohibition against promoting them to a universal SOP-11E theorem.