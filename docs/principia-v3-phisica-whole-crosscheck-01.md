# PRINCIPIA SEMANTICA — VOLUME III / PHISICA WHOLE-BLOCK CROSSCHECK 01

**Status:** `GLOBAL CROSSCHECK PASS AFTER LOCAL ERRATA 01`  
**Date:** 2026-09-29  
**Scope:** `III.1–III.6`  
**Source audit:** `phisica-operator-migration-01.md` + `phisica-operator-migration-01-errata-01.md`  
**Falsifier bank:** `phisica-falsifier-registry-01.md`, PF01–PF14

---

# 1. Question

Local PASS results do not imply that the six units compose into one legal operator-theoretic chain.

The whole-block gate asks whether

\[
\mathrm{III.1}
\to
\mathrm{III.2}
\to
\mathrm{III.3}
\to
\mathrm{III.4}
\to
\mathrm{III.5}
\to
\mathrm{III.6}
\]

is globally consistent with respect to:

1. object types and Hilbert spaces;
2. operator domains;
3. proof dependencies;
4. contract strengthening;
5. spectral terminology;
6. unitary/similarity transport;
7. perturbation topology;
8. PSI/CORE boundaries.

---

# 2. Typed chain

## III.1 — smooth projectability

The first layer lives on

\[
T_\Lambda:C^\infty(I)\to C^\infty(U),
\qquad
T_\Lambda\Phi=\Phi\circ\Lambda,
\]

and establishes

\[
\Delta_gT_\Lambda=T_\Lambda L_\Lambda
\]

iff

\[
|\nabla\Lambda|^2=B\circ\Lambda,
\qquad
\Delta\Lambda=C\circ\Lambda.
\]

No Hilbert-space or domain theorem is imported at this stage.

**CHECK:** `PASS`.

## III.2 — weighted Hilbert realization

For \(B>0\),

\[
(\rho B)'=\rho C
\]

defines the positive Hilbert/Sturm–Liouville weight up to scale and gives

\[
L_\Lambda
=\rho^{-1}\partial_\lambda(\rho B\partial_\lambda).
\]

Under the additional proper-submersion/coarea contract,

\[
\rho d\lambda
=\Lambda_*(d\mathrm{vol}_g)
\]

after normalization, and

\[
T_\Lambda:L^2(I,\rho d\lambda)	o L^2(U,d\mathrm{vol}_g)
\]

is an isometry onto the fibre-constant subspace.

The geometric pushforward theorem is an **optional strengthening**, not a prerequisite for every later regular Sturm–Liouville realization.

**CHECK:** `PASS`.

## III.3 — unbounded operator realization

The contract is narrowed to a regular finite interval with coefficients extending positively/regularly to the endpoints.

The reduced object becomes an actual unbounded operator

\[
H:D(H)\subset L^2(I,\rho d\lambda)	o L^2(I,\rho d\lambda).
\]

The whole-block audit found one convention mismatch between III.2 and the first version of III.3. III.2 fixes

\[
\langle f,g\rangle_\rho
=\int\overline f g\rho,
\]

whereas the original III.3 boundary form was displayed in the opposite conjugation convention.

Corrected III.3 now uses

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

Separated real Robin relations define one-dimensional complex maximal-isotropic endpoint subspaces and yield

\[
H_{\min}^*=H_{\max},
\qquad
H_{\alpha,\beta}=H_{\alpha,\beta}^*.
\]

**CHECK:** `PASS AFTER LOCAL ERRATA 01`.

## III.4 — compact-resolvent spectral sector

The regular finite-interval form domain embeds compactly:

\[
\mathcal Q\hookrightarrow L^2(I,\rho d\lambda).
\]

Hence the fixed self-adjoint realization from III.3 has compact resolvent and therefore discrete real spectrum with finite multiplicities and a complete orthonormal eigenbasis.

No claim of spectral completeness as a model identifier is made.

**CHECK:** `PASS`.

## III.5 — unitary Liouville normal form

The contract is strengthened to \(B,\rho\in C^2\), positive on the compact interval.

The historical multiplier

\[
\psi=e^\beta\phi
\]

is retained only as a bounded similarity after exact domain transport.

The canonical transform is

\[
x'=B^{-1/2},
\qquad
(Uu)(x)=\rho^{1/2}B^{1/4}u,
\]

with

\[
U:L^2(I,\rho d\lambda)\to L^2(J,dx)
\]

unitary and

\[
UHU^{-1}
=-\frac12\partial_x^2+Q(x).
\]

The operator domain and separated boundary conditions are transported by \(U\).

**CHECK:** `PASS`.

## III.6 — perturbation sector

The contract is narrowed once more to a fixed reference Hilbert space and fixed operator domain after legal trivialization:

\[
H(t)=H_0+W(t),
\qquad
D(H(t))=D(H_0),
\]

with bounded self-adjoint norm-\(C^1\) \(W(t)\).

Then

\[
|E_n(t)-E_n(s)|\le\|W(t)-W(s)\|
\]

and, for a simple isolated branch,

\[
E'(t)=\langle\phi(t),W'(t)\phi(t)\rangle.
\]

The eigenvector branch is controlled in the graph norm of the common domain. Degeneracy is treated by compression \(PWP\), not by a scalar shortcut.

Raw geometric deformation of \(\Lambda\) is explicitly outside this fixed-space theorem until a unitary or closed-form trivialization is supplied.

**CHECK:** `PASS`.

---

# 3. Contract nesting — mandatory interpretation

The execution arrows are **not universal logical implications with unchanged hypotheses**.

The actual architecture is a nested sequence of sectors:

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

schematically, with some optional branches such as the III.2 geometric pushforward theorem.

In particular:

- III.1 projectability does not imply endpoint regularity;
- III.2 weight existence does not imply the proper-submersion/coarea identification;
- III.2 does not imply that coefficients extend regularly to a compact closure;
- III.3 self-adjointness does not imply compact resolvent outside the regular finite-interval sector;
- III.4 compact spectrum does not imply the \(C^2\) regularity required for pointwise III.5 normal form;
- III.5 unitary normal form for each model does not by itself give a common perturbation trivialization for a family;
- III.6 proves perturbation results only after that extra family-level control.

Permanent rule:

\[
\boxed{
\text{later PHISICA gate}
=
\text{earlier structure + stronger contract},
}
\]

not an automatic consequence for every earlier model.

---

# 4. Proof-dependency normalization

The whole-block audit separates strict proof dependencies from PHISICA provenance.

## III.1

Strict: chain rule + factorization through \(\Lambda\).

## III.2.A

As an abstract integrating-factor theorem: \(B>0\) and regularity of \(B,C\).  
In the PHISICA chain, III.1 supplies the geometric origin of those coefficients.

## III.2.B

Strict: III.1 projectability + proper submersion/coarea + Green identity.

## III.3

Strict: regular finite-interval Sturm–Liouville contract + weighted Hilbert space.  
III.2 supplies the canonical PHISICA weight relation; its geometric pushforward subtheorem is not required.

## III.4

Strict: III.3 self-adjoint regular realization + semibounded closed form + compact embedding.  
III.2 is upstream provenance, not an additional independent spectral hypothesis.

## III.5

Strict for the unitary normal form: weighted realization + regular self-adjoint operator, i.e. III.2/III.3 under the strengthened \(C^2\) contract.  
III.4 is **not** required to construct \(UHU^{-1}\); it supplies the spectral consequences that are then transported unitarily.

## III.6

Strict for the current canonical sector: III.4 compact-resolvent spectral setup + III.5 fixed standard-Hilbert representation + bounded self-adjoint perturbation theorem.  
A general variable-domain/form perturbation theory is acknowledged but not claimed as proved here.

**DEPENDENCY CHECK:** `PASS AFTER NORMALIZATION`.

---

# 5. Permanent semantic separations survive composition

The whole chain preserves all required no-go distinctions:

\[
\boxed{
\text{scalar coordinate}
\not\Rightarrow
\text{operator projectability},
}
\]

\[
\boxed{
\text{Hilbert weight}
\neq
\text{spectral measure},
}
\]

\[
\boxed{
\text{formal differential expression}
\neq
\text{self-adjoint operator},
}
\]

\[
\boxed{
\text{self-adjointness}
\not\Rightarrow
\text{compact resolvent},
}
\]

\[
\boxed{
\text{bounded similarity}
\neq
\text{unitary equivalence},
}
\]

\[
\boxed{
\text{eigenvalue sequence}
\not\Rightarrow
\text{complete model identification},
}
\]

\[
\boxed{
\text{small coefficient variation}
\not\Rightarrow
\text{spectral stability without a topology},
}
\]

\[
\boxed{
\text{stable eigenvalues}
\not\Rightarrow
\text{stable eigenvectors / DNA labels}.
}
\]

**SEMANTIC-BOUNDARY CHECK:** `PASS`.

---

# 6. Historical PHISICA claims after migration

## Recovered under explicit hypotheses

- exact one-dimensional operator reduction when III.1 projectability holds;
- canonical Sturm–Liouville weight;
- self-adjoint regular realizations with explicit boundary domains;
- compact resolvent and discrete spectrum on the regular finite interval;
- complete Hilbert eigenbasis for the fixed self-adjoint realization;
- historical drift-elimination algebra as a bounded similarity after domain transport;
- stronger unitary Liouville normal form;
- Hellmann–Feynman for a licensed simple isolated branch;
- quantitative eigenvalue stability in the bounded fixed-space perturbation sector.

## Withdrawn or retained only as genealogy

- `dLambda != 0` as sufficient for one-dimensional reduction;
- `LOGOS=(B,C,rho)` as three independent primitive data;
- LOGOS alone as complete self-adjoint dynamics;
- `rho dlambda` as spectral measure;
- formal multiplier as automatic unitary equivalence;
- eigenvalue sequence as complete model invariant;
- arbitrary small LOGOS/coefficient deformation as automatic spectral stability;
- stability of the full historical spectral `DNA` from stability of eigenvalues alone;
- blanket historical PSI-13 spectral theorem without the III.1–III.6 gates.

**SOURCE-MIGRATION CHECK:** `PASS`.

---

# 7. PSI status

Nothing in III.1–III.6 introduces a new PSI semantic role.

PHISICA remains a realization/model layer in which the PSI discipline appears as:

\[
\boxed{
\text{candidate reduction}
\to
\text{factorization/projectability test}
\to
\text{legal representation}
\to
\text{task-specific spectral/perturbative conclusions}.
}
\]

No typed counterexample forces R4.

No missing control primitive forces Agent v03.

**CORE/AGENT CHECK:** `PASS`.

---

# 8. Whole-block errata

Exactly one mathematical-display/convention defect was found during the global composition audit:

1. III.2 fixed the inner-product convention \(\int\bar f g\rho\), while the first III.3 boundary-form display used the opposite conjugation convention;
2. the first III.3 prose called a Robin boundary subspace a “one-dimensional real line” although it is a one-dimensional complex subspace generated by a real vector.

Both have been corrected in physical III.3. The source-audit P7 is superseded on this point by `phisica-operator-migration-01-errata-01.md`.

Blast radius:

\[
\boxed{
\text{display/convention repair only};
\quad
\mathrm{III.3:III.6\ theorem\ conclusions\ unchanged}.
}
\]

No Freeze 01 errata follows because Volume III PHISICA was still in active migration and had not been globally frozen.

---

# 9. Verdict

After application of the local boundary-form errata:

\[
\boxed{
\mathrm{PHISICA\ III.1:III.6}
=
\mathrm{MATHEMATICAL\ GLOBAL\ PASS}.
}
\]

More explicitly:

\[
\boxed{
\mathrm{LOCAL\ PASS}^{\times 6}
+\mathrm{WHOLE\!\!-\!BLOCK\ CROSSCHECK}
+\mathrm{ERRATA\ 01}
\Rightarrow
\mathrm{GLOBAL\ PASS}.
}
\]

This does not freeze all future Volume III material. It closes the **PHISICA operator migration block** only.

---

# 10. Next legal front

The next Volume III front may now use the repaired operator block as a certified dependency.

Recommended order from the current project architecture:

\[
\boxed{
\mathrm{PHISICA\ GLOBAL\ PASS}
\to
\mathrm{MOST/HCUBE\ SPECTRAL\ INFORMATION\ LAYER}
\to
\mathrm{other\ realizations/laboratories}.
}
\]

The operator block must not be reopened merely to restore withdrawn historical rhetoric.
