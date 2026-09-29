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

Let

\[
T_\Lambda\Phi=\Phi\circ\Lambda.
\]

Then

\[
\boxed{
\Delta_g\operatorname{im}T_\Lambda
\subseteq
\operatorname{im}T_\Lambda
}
\]

iff

\[
\boxed{
|\nabla\Lambda|^2=B\circ\Lambda,
\qquad
\Delta_g\Lambda=C\circ\Lambda.
}
\]

Equivalently

\[
\boxed{
\Delta_gT_\Lambda=T_\Lambda L_\Lambda,
\qquad
L_\Lambda=B\partial_\lambda^2+C\partial_\lambda.
}
\]

For

\[
H=-\frac12\Delta_g+V,
\]

exact projectability further requires

\[
V=V_\Lambda\circ\Lambda.
\]

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-01-lambda-operator-projectability.md`  
**BOUNDARY:** `dLambda != 0` alone is insufficient.  
**REGRESSION:** `Lambda(x,y)=x+y^2` on Euclidean `R^2`.

---

# 3. III.2 — Weight measure and Sturm–Liouville form

For projectable coefficients with \(B>0\):

\[
\boxed{(\rho B)'=\rho C}
\]

has a positive solution unique up to scale,

\[
\boxed{
\rho(\lambda)
=K\,B(\lambda)^{-1}
\exp\!\left(\int^\lambda\frac{C}{B}\,d\mu\right).
}
\]

Hence

\[
\boxed{
L_\Lambda
=\frac1\rho\partial_\lambda(\rho B\partial_\lambda).
}
\]

On compactly supported test functions this is formally symmetric in

\[
L^2(I,\rho d\lambda),
\]

but it is not yet a self-adjoint realization.

Under the additional proper-submersion/coarea contract,

\[
\mu_\Lambda:=\Lambda_*(d\mathrm{vol}_g)
=m(\lambda)d\lambda
\]

with

\[
m(\lambda)=\int_{\Lambda^{-1}(\lambda)}\frac1{|\nabla\Lambda|}\,dA_\lambda,
\]

and Green's identity plus projectability yields

\[
\boxed{(mB)'=mC.}
\]

Thus on connected \(I\),

\[
\boxed{m=K\rho.}
\]

After normalization,

\[
\boxed{
\rho d\lambda=\Lambda_*(d\mathrm{vol}_g),
}
\]

and \(T_\Lambda\) is an isometry onto the fibre-constant Hilbert subspace.

Permanent distinctions:

- `rho dlambda` = Hilbert/weight measure, not spectral measure;
- integrating-factor weight != geometric pushforward without an integration/coarea contract (PF11);
- formal symmetry != self-adjointness;
- `(B,C,rho)` do not determine full dynamics.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-02-weight-sturm-liouville.md`  
**FALSIFIERS:** PF03, PF04, PF06, PF11.

---

# 4. III.3 — Domain and self-adjoint realization

On a finite regular interval \(I=(a,b)\), let

\[
p=\rho B,
\qquad
\tau u=-\frac1{2\rho}(pu')'+Vu,
\]

with positive regular \(B,\rho\) and real regular \(V\).

The maximal domain is

\[
D(H_{\max})
=
\{u\in L^2(I,\rho d\lambda):u,pu'\in AC([a,b]),\ \tau u\in L^2(I,\rho d\lambda)\}.
\]

The Green–Lagrange boundary form is

\[
\boxed{
\mathfrak b(u,v)
=
\frac12
\left[
 u\overline{pv'}-(pu')\overline v
\right]_a^b.
}
\]

For the minimal realization,

\[
\boxed{H_{\min}^*=H_{\max}.}
\]

Separated Robin boundary conditions define maximal isotropic boundary subspaces and therefore self-adjoint realizations

\[
\boxed{H_{\alpha,\beta}=H_{\alpha,\beta}^*.}
\]

Dirichlet, Neumann/quasi-Neumann and mixed separated conditions are special cases.

Permanent distinction:

\[
\boxed{
\text{formal symmetry or vanishing boundary form}
\not\Rightarrow
\text{self-adjointness without maximality/adjoint-domain equality}.
}
\]

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-03-domain-selfadjoint.md`  
**FALSIFIERS:** PF04, PF06, PF12.

---

# 5. III.4 — Compact resolvent and discrete spectrum

For the regular bounded-interval self-adjoint realizations from III.3, the quadratic-form domain is a closed subspace of \(H^1(I)\), with form norm equivalent to an \(H^1\)-type norm. Rellich compactness therefore yields

\[
\boxed{
\mathcal Q_{\alpha,\beta}\hookrightarrow L^2(I,\rho d\lambda)
\text{ compactly}.
}
\]

Hence

\[
\boxed{(H_{\alpha,\beta}-z)^{-1}\text{ is compact}}
\]

for every resolvent point \(z\). Consequently

\[
\boxed{
\sigma(H_{\alpha,\beta})
=\{E_n\}_{n\ge0},
\qquad
E_n\to+\infty,
}
\]

with real eigenvalues of finite multiplicity, and the eigenfunctions form a complete orthonormal basis of \(L^2(I,\rho d\lambda)\).

Permanent distinctions:

- self-adjointness != compact resolvent/discrete spectrum (PF13);
- eigenvalue sequence != complete model invariant (PF07);
- no singular-endpoint/noncompact claim is made.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-04-compact-resolvent-spectrum.md`  
**FALSIFIERS:** PF07, PF13.

---

# 6. III.5 — Liouville / normal-form transform

Historical multiplicative `beta` transform is currently only

`FORMAL NORMAL-FORM / FUNCTION-SPACE BINDING REQUIRED`.

Canonical target: an explicitly unitary or bounded-invertible transport with domains and Hilbert spaces stated.

No automatic isospectrality from formal first-derivative elimination.

**STATUS:** `NEXT / REPAIR REQUIRED`.

---

# 7. III.6 — Perturbation / Hellmann–Feynman

Target clean contract:

- fixed Hilbert space after unitary trivialization;
- differentiable self-adjoint operator or closed-form family;
- simple isolated eigenvalue for scalar HF formula;
- explicit treatment of degeneracy and varying domains.

**STATUS:** `QUEUED / REPAIR REQUIRED`.

---

# 8. Historical claims held in genealogy

Until rebuilt, do not promote:

- `LOGOS=(B,C,rho)` as three independent data;
- `LOGOS` alone determines full self-adjoint dynamics;
- `rho dlambda` as spectral measure;
- eigenvalue sequence alone as complete model information;
- arbitrary small coefficient deformation implies small spectral change;
- historical `PSI-13` central theorem without III.1–III.3 gates.

These remain source material/genealogy, not current V3 theorem units.

---

# 9. Current execution order

\[
\boxed{
\mathrm{III.1\ PASS}
\to
\mathrm{III.2\ PASS}
\to
\mathrm{III.3\ PASS}
\to
\mathrm{III.4\ PASS}
\to
\mathrm{III.5\ NEXT}
\to
\mathrm{III.6}
\to
\mathrm{PHISICA\ WHOLE\ CROSSCHECK}.
}
\]

No CORE5 or Agent v03 change is licensed.
