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

Separated real Robin conditions select maximal isotropic boundary subspaces and define self-adjoint realizations.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-03-domain-selfadjoint.md`  
**FALSIFIERS:** PF04, PF06, PF12.

---

# 5. III.4 — Compact resolvent and discrete spectrum

For the regular bounded-interval self-adjoint realizations from III.3,

\[
\boxed{
\mathcal Q\hookrightarrow L^2(I,\rho d\lambda)
\text{ compactly}
}
\]

and therefore

\[
\boxed{(H-z)^{-1}\text{ is compact}.}
\]

Hence

\[
\boxed{
\sigma(H)=\{E_n\}_{n\ge0},
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
U H U^{-1}
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

On a fixed Hilbert space after legal unitary trivialization, let

\[
H(t)=H_0+W(t),
\qquad
D(H(t))=D(H_0),
\]

with bounded self-adjoint norm-\(C^1\) perturbation \(W(t)\).

Then self-adjointness and compact resolvent persist, and ordered eigenvalues satisfy

\[
\boxed{
|E_n(t)-E_n(s)|
\le
\|W(t)-W(s)\|.
}
\]

For a simple isolated eigenvalue branch, the eigenvector may be chosen \(C^1\) in the graph norm of the common domain and

\[
\boxed{
E'(t)=\langle\phi(t),W'(t)\phi(t)\rangle.
}
\]

For a bounded potential perturbation this becomes

\[
\boxed{
E'(t)=\int_J|\phi(t,x)|^2\,\partial_tQ(t,x)\,dx.
}
\]

At a degenerate eigenvalue the first-order splitting is governed by the compressed perturbation

\[
\boxed{PWP|_{\ker(H_0-E)},}
\]

not by a naive scalar expectation value.

A geometric deformation of \(\Lambda\) is not automatically a fixed-space perturbation: changing \(B,\rho\), the Liouville coordinate, interval or boundary realization requires a prior unitary/fixed-form trivialization before Hellmann–Feynman is licensed.

Permanent distinctions:

- small coefficient change != perturbation theorem without a topology;
- scalar HF requires a simple isolated branch or an appropriate branchwise treatment;
- stable eigenvalues != stable eigenvectors / spectral-DNA labels;
- variable-domain families require an additional perturbation framework.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-06-perturbation-hellmann-feynman.md`  
**FALSIFIERS:** PF08, PF09, PF14.

---

# 8. Historical claims held in genealogy

Do not promote without the repaired gates:

- `LOGOS=(B,C,rho)` as three independent or complete dynamical data;
- `rho dlambda` as spectral measure;
- eigenvalue sequence alone as complete model information;
- formal drift removal as automatic unitary equivalence;
- arbitrary small coefficient deformation as automatic spectral or DNA stability;
- historical `PSI-13` central theorem without III.1–III.3 gates.

---

# 9. Current execution order

\[
\boxed{
\mathrm{III.1:III.6\ LOCAL\ PASS}
\to
\mathrm{PHISICA\ WHOLE\!\!-\!BLOCK\ CROSSCHECK\ 01\ NEXT}.
}
\]

A sequence of local PASS results is not itself a global PHISICA PASS.

No CORE5 or Agent v03 change is licensed.
