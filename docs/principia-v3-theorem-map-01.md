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

Target:

\[
(\rho B)'=\rho C
\]

and

\[
H_\Lambda
=-\frac1{2\rho}\partial_\lambda(\rho B\partial_\lambda)+V_\Lambda.
\]

Required distinctions:

- `rho dlambda` = Hilbert/weight measure, not automatically spectral measure;
- `rho` is derived from `B,C` up to positive scale in the formal ODE;
- geometric identification of `rho` with `Lambda_*(dvol_g)` requires a separate pushforward/coarea theorem.

**STATUS:** `NEXT`.

---

# 4. III.3 — Domain and self-adjoint realization

Target objects:

\[
\tau u=-\frac1{2\rho}(\rho Bu')'+Vu,
\]

maximal/minimal domains, boundary form, regular self-adjoint boundary conditions.

No self-adjoint theorem before the domain is explicit.

**STATUS:** `QUEUED`.

---

# 5. III.4 — Compact resolvent and discrete spectrum

Only after III.3.

Regular bounded interval + positive regular coefficients + real lower-bounded potential + self-adjoint boundary realization.

**STATUS:** `QUEUED`.

---

# 6. III.5 — Liouville / normal-form transform

Historical multiplicative `beta` transform is currently only

`FORMAL NORMAL-FORM / FUNCTION-SPACE BINDING REQUIRED`.

Canonical target: an explicitly unitary or bounded-invertible transport with domains and Hilbert spaces stated.

No automatic isospectrality from formal first-derivative elimination.

**STATUS:** `QUEUED / REPAIR REQUIRED`.

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
\mathrm{III.2\ NEXT}
\to
\mathrm{III.3}
\to
\mathrm{III.4}
\to
\mathrm{III.5}
\to
\mathrm{III.6}
\to
\mathrm{PHISICA\ WHOLE\ CROSSCHECK}.
}
\]

No CORE5 or Agent v03 change is licensed.
