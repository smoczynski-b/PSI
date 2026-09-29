# PRINCIPIA SEMANTICA — VOLUME III THEOREM MAP 01

**Status:** `CURRENT / PHISICA OPERATOR MIGRATION CONTROL MAP`  
**Date:** 2026-09-29  
**Upstream:** `principia-volume-skeleton-03.md`, V2 global pass  
**Source audit:** `phisica-operator-migration-01.md`  
**Primary historical source:** project file `PHISICA — NEW.pdf`

---

# 1. Current PHISICA gate

Historical PHISICA is not migrated theorem-by-theorem without repair.

Current discipline:

\[
\boxed{
\text{formal differential identity}
\to
\text{operator projectability}
\to
\text{weighted realization}
\to
\text{domain/self-adjointness}
\to
\text{spectrum}
\to
\text{normal form}
\to
\text{perturbation}.
}
\]

Skipping a gate is not licensed.

---

# 2. III.1 — Lambda operator projectability

\[
\boxed{
\Delta_g\operatorname{im}T_\Lambda
\subseteq
\operatorname{im}T_\Lambda
\iff
|\nabla\Lambda|^2=B\circ\Lambda
\land
\Delta_g\Lambda=C\circ\Lambda.
}
\]

For Schrödinger reduction additionally

\[
\boxed{V=V_\Lambda\circ\Lambda.}
\]

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-01-lambda-operator-projectability.md`  
**REGRESSION:** `Lambda(x,y)=x+y^2`.

---

# 3. III.2 — Weight measure and Sturm–Liouville form

For projectable coefficients with \(B>0\):

\[
\boxed{(\rho B)'=\rho C}
\]

and

\[
\boxed{
L_\Lambda
=\rho^{-1}\partial_\lambda(\rho B\partial_\lambda).
}
\]

Under the proper-submersion/coarea contract,

\[
\boxed{
\rho d\lambda=\Lambda_*(d\mathrm{vol}_g)
}
\]

after normalization, and \(T_\Lambda\) is an isometry onto the fibre-constant Hilbert subspace.

Permanent distinctions:

- Hilbert weight != spectral measure;
- integrating-factor weight != geometric pushforward without the geometric integration contract;
- formal symmetry != self-adjointness.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-02-weight-sturm-liouville.md`  
**FALSIFIERS:** PF03, PF04, PF06, PF11.

---

# 4. III.3 — Domain and self-adjoint realization

On a finite regular interval, with

\[
p=\rho B,
\qquad
\tau u=-\frac1{2\rho}(pu')'+Vu,
\]

one has

\[
\boxed{H_{\min}^*=H_{\max}.}
\]

Separated real Robin conditions select maximal isotropic boundary subspaces and define self-adjoint realizations

\[
\boxed{H_{\alpha,\beta}=H_{\alpha,\beta}^*.}
\]

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-03-domain-selfadjoint.md`  
**FALSIFIERS:** PF04, PF06, PF12.

---

# 5. III.4 — Compact resolvent and discrete spectrum

For the regular bounded-interval self-adjoint realizations from III.3,

\[
\boxed{
\mathcal Q_{\alpha,\beta}\hookrightarrow L^2(I,\rho d\lambda)
\text{ compactly}
}
\]

and therefore

\[
\boxed{(H_{\alpha,\beta}-z)^{-1}\text{ is compact}.}
\]

Hence

\[
\boxed{
\sigma(H_{\alpha,\beta})=\{E_n\}_{n\ge0},
\qquad E_n\to+\infty,
}
\]

with finite multiplicities and a complete orthonormal eigenbasis.

Permanent distinctions:

- self-adjointness != compact resolvent/discrete spectrum;
- eigenvalue sequence != complete model invariant.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-04-compact-resolvent-spectrum.md`  
**FALSIFIERS:** PF07, PF13.

---

# 6. III.5 — Liouville / normal-form transform

Historical PHISICA uses

\[
\psi=e^\beta\phi,
\qquad
\beta'=-\frac{C}{2B}.
\]

Under the regular compact contract this multiplier can be promoted to a bounded similarity only after the domain is transported exactly. It is not generally unitary in \(L^2(I,\rho d\lambda)\).

The canonical Liouville transform is

\[
\boxed{
x(\lambda)=\int_a^\lambda B(\mu)^{-1/2}d\mu
}
\]

and

\[
\boxed{
(Uu)(x)=s(\lambda(x))u(\lambda(x)),
\qquad
s=\rho^{1/2}B^{1/4}.
}
\]

Then

\[
\boxed{
U:L^2(I,\rho d\lambda)\to L^2(J,dx)
\text{ is unitary}
}
\]

and, with the transported domain,

\[
\boxed{
U H_{\theta_a,\theta_b}U^{-1}
=-\frac12\frac{d^2}{dx^2}
+Q(x),
}
\]

where

\[
\boxed{
Q(x)=V(\lambda(x))+\frac{s_{xx}}{2s}.
}
\]

The transformed boundary conditions remain separated real conditions, and self-adjointness, spectrum, multiplicities and compact-resolvent structure are preserved by unitary equivalence.

Permanent distinction:

\[
\boxed{
\text{bounded similarity}\neq\text{unitary equivalence}.
}
\]

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-05-liouville-normal-form.md`  
**FALSIFIER:** PF05.

---

# 7. III.6 — Perturbation / Hellmann–Feynman

Target clean contract:

- fixed Hilbert space after the unitary Liouville trivialization;
- differentiable self-adjoint operator or closed-form family;
- simple isolated eigenvalue for the scalar Hellmann–Feynman formula;
- explicit treatment of degeneracy and varying domains;
- no automatic spectral stability from coefficient-smallness without a topology/resolvent or form theorem.

**STATUS:** `NEXT / REPAIR REQUIRED`.

---

# 8. Historical claims held in genealogy

Until rebuilt, do not promote:

- `LOGOS=(B,C,rho)` as three independent data;
- `LOGOS` alone determines full self-adjoint dynamics;
- `rho dlambda` as spectral measure;
- eigenvalue sequence alone as complete model information;
- arbitrary small coefficient deformation implies small spectral change;
- historical `PSI-13` central theorem without III.1–III.3 gates.

The old drift-removal algebra survives only inside the repaired III.5 operator contract.

---

# 9. Current execution order

\[
\boxed{
\mathrm{III.1:III.5\ PASS}
\to
\mathrm{III.6\ NEXT}
\to
\mathrm{PHISICA\ WHOLE\ CROSSCHECK}.
}
\]

No CORE5 or Agent v03 change is licensed.
