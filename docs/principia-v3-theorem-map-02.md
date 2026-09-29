# PRINCIPIA SEMANTICA — VOLUME III THEOREM MAP 02

**Status:** `CURRENT / PHISICA OPERATOR BLOCK GLOBAL PASS / SPECTRAL INFORMATION LAYER NEXT`  
**Date:** 2026-09-29  
**Supersedes for control:** `principia-v3-theorem-map-01.md`  
**Upstream:** `principia-volume-skeleton-03.md`, V2 global pass  
**Source audit:** `phisica-operator-migration-01.md` + `phisica-operator-migration-01-errata-01.md`  
**Global gate:** `principia-v3-phisica-whole-crosscheck-01.md`

---

# 1. PHISICA operator block — global status

The repaired operator chain is:

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
\mathrm{III.5\ UNITARY\ LIOUVILLE\ NORMAL\ FORM}
\to
\mathrm{III.6\ PERTURBATION/HF}.
}
\]

After whole-block crosscheck and correction of the III.3 boundary-form convention:

\[
\boxed{
\mathrm{PHISICA\ III.1:III.6}
=
\mathrm{MATHEMATICAL\ GLOBAL\ PASS}.
}
\]

No CORE5 or Agent-version change follows.

---

# 2. Contract nesting — mandatory reading of the arrows

The arrows above do not mean that every III.1 model automatically satisfies all later hypotheses.

The execution chain is a sequence of stricter sectors:

\[
\boxed{
\mathcal C_{III.6}
\subset
\mathcal C_{III.5}
\subset
\mathcal C_{III.3/4}
\subset
\mathcal C_{III.2}
\subset
\mathcal C_{III.1},
}
\]

schematically, with optional branches such as the geometric pushforward theorem of III.2.

Permanent interpretation:

\[
\boxed{
\text{later gate}
=
\text{earlier structure + stronger typed contract}.
}
\]

---

# 3. III.1 — operator projectability

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
**FALSIFIERS:** PF01, PF02, PF10.

---

# 4. III.2 — weight / Sturm–Liouville / geometric pushforward

For projectable coefficients with \(B>0\),

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

Under the additional proper-submersion/coarea contract,

\[
\boxed{
\rho d\lambda
=\Lambda_*(d\mathrm{vol}_g)
}
\]

after normalization.

The pushforward identification is an optional strengthening; the Hilbert/Sturm–Liouville weight theorem does not require it.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-02-weight-sturm-liouville.md`  
**FALSIFIERS:** PF03, PF04, PF06, PF11.

---

# 5. III.3 — domain and self-adjoint realization

The contract narrows to the regular finite interval.

With

\[
p=\rho B,
\qquad
\tau u=-\frac1{2\rho}(pu')'+Vu,
\]

and inner product convention

\[
\langle f,g\rangle_\rho
=\int\overline f g\rho,
\]

the corrected Green–Lagrange form is

\[
\boxed{
\mathfrak b(u,v)
=
\frac12
\left[
\overline u\,(pv')-
\overline{pu'}\,v
\right]_a^b.
}
\]

Then

\[
\boxed{H_{\min}^*=H_{\max}}
\]

and separated real Robin relations select maximal-isotropic complex boundary subspaces, producing self-adjoint realizations.

**STATUS:** `PASS AFTER WHOLE-BLOCK ERRATA 01`  
**SOURCE:** `principia-v3-03-domain-selfadjoint.md`  
**ERRATA:** `phisica-operator-migration-01-errata-01.md`  
**FALSIFIERS:** PF04, PF06, PF12.

---

# 6. III.4 — compact resolvent / spectrum

For the regular bounded-interval self-adjoint realization,

\[
\boxed{
\mathcal Q\hookrightarrow L^2(I,\rho d\lambda)
\text{ compactly}
}
\]

and hence

\[
\boxed{(H-z)^{-1}\text{ compact}.}
\]

Therefore the spectrum is discrete, real, of finite multiplicity, with

\[
E_n\to+\infty,
\]

and the eigenfunctions form a complete orthonormal basis.

Strict proof dependency: III.3 + regular finite-interval form compactness. III.2 is PHISICA provenance, not an extra independent spectral hypothesis.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-04-compact-resolvent-spectrum.md`  
**FALSIFIERS:** PF07, PF13.

---

# 7. III.5 — unitary Liouville normal form

Under the strengthened regularity contract,

\[
\boxed{
x(\lambda)=\int_a^\lambda B(\mu)^{-1/2}d\mu,
}
\]

\[
\boxed{
(Uu)(x)=\rho^{1/2}B^{1/4}u
}
\]

defines a unitary map

\[
U:L^2(I,\rho d\lambda)\to L^2(J,dx)
\]

with transported domain and

\[
\boxed{
UHU^{-1}
=-\frac12\partial_x^2
+V(\lambda(x))+rac{s_{xx}}{2s}.
}
\]

The historical multiplier survives only as bounded similarity after exact domain transport.

Strict construction dependency: III.2 + III.3 under the stronger regularity contract. III.4 supplies spectral consequences but is not required to construct the Liouville unitary.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-05-liouville-normal-form.md`  
**FALSIFIER:** PF05.

---

# 8. III.6 — perturbation / Hellmann–Feynman

After legal trivialization to a fixed Hilbert space/domain,

\[
H(t)=H_0+W(t),
\qquad
W(t)=W(t)^*\in\mathcal B(\mathcal H),
\]

with norm-\(C^1\) dependence.

Then

\[
\boxed{
|E_n(t)-E_n(s)|\le\|W(t)-W(s)\|.
}
\]

For a simple isolated branch with graph-norm differentiable eigenvector,

\[
\boxed{
E'(t)=\langle\phi(t),W'(t)\phi(t)\rangle.
}
\]

Degenerate first-order splitting is governed by \(PWP\) on the eigenspace. Raw geometric deformation of \(\Lambda\) requires a prior fixed-space or closed-form trivialization.

**STATUS:** `PASS`  
**SOURCE:** `principia-v3-06-perturbation-hellmann-feynman.md`  
**FALSIFIERS:** PF08, PF09, PF14.

---

# 9. Global PHISICA boundaries

The migrated block permanently rejects:

\[
\boxed{
\text{Hilbert weight}\neq\text{spectral measure},
}
\]

\[
\boxed{
(B,C,\rho)\not\Rightarrow\text{complete self-adjoint dynamics},
}
\]

\[
\boxed{
\text{formal drift removal}\neq\text{unitary equivalence},
}
\]

\[
\boxed{
\{E_n\}\not\Rightarrow\text{complete model identification},
}
\]

\[
\boxed{
\text{small coefficient deformation}\not\Rightarrow\text{spectral stability without a topology},
}
\]

\[
\boxed{
\text{stable eigenvalues}\not\Rightarrow\text{stable eigenvectors / DNA labels}.
}
\]

The historical PSI-13/LOGOS/DNA rhetoric remains genealogy unless separately rebuilt under these gates.

---

# 10. Whole-block result

`principia-v3-phisica-whole-crosscheck-01.md` found one convention/display defect in III.3 and no theorem-level failure after correction.

Thus:

\[
\boxed{
\mathrm{III.1:III.6}
=
\mathrm{GLOBAL\ PASS\ AFTER\ LOCAL\ ERRATA\ 01}.
}
\]

This closes the PHISICA operator migration block. It does not freeze all future Volume III material.

---

# 11. Next front — spectral information layer

The next legal question is no longer whether the reduced operator exists. It is:

> Which spectral/operator representations preserve enough information for the declared task?

This opens the MOST/HCube layer.

Planned order:

\[
\boxed{
\mathrm{III.7\ —\ SPECTRAL\ INFORMATION\ HIERARCHY\ (MOST)}
\to
\mathrm{III.8\ —\ HCUBE\ NONNORMAL\ RESOLVENT\ LAB}
\to
\mathrm{other\ realizations/laboratories}.
}
\]

The central boundary entering III.7 is

\[
\boxed{
\text{spectrum as invariant}
\neq
\text{spectrum as sufficient task representation}.
}
\]

No CORE5 or Agent v03 change is licensed.
