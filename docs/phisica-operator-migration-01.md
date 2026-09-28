# PHISICA — OPERATOR MIGRATION 01

**Status:** `SOURCE AUDIT / DOMAIN REPAIR REQUIRED / VOLUME III GATE`  
**Date:** 2026-09-29  
**Primary source:** project file `PHISICA — NEW.pdf`  
**Target architecture:** current PSI/Principia after V2 global pass; no CORE growth.

---

# 0. Purpose

This document audits the operator-theoretic layer of PHISICA before migration into Volume III.

The audit separates:

\[
\boxed{
\text{valid differential identity}
\mid
\text{projectable one-dimensional reduction}
\mid
\text{closed/self-adjoint realization}
\mid
\text{spectral statement}
\mid
\text{perturbative statement}
}
\]

and forbids moving from one level to the next without its own hypotheses.

No result below adds a PSI primitive. PHISICA remains a realization/model layer.

---

# 1. Source claims under audit

The source uses a structural field

\[
\Lambda:M\to\mathbb R
\]

and defines pointwise

\[
B_0(x)=|\nabla\Lambda(x)|^2,
\qquad
C_0(x)=\Delta\Lambda(x).
\]

For a composite function

\[
\psi(x)=\Psi(\Lambda(x))
\]

the source correctly computes

\[
\boxed{
\Delta(\Psi\circ\Lambda)
=
B_0\,\Psi''(\Lambda)
+
C_0\,\Psi'(\Lambda).
}
\]

The source then writes these coefficients as `B(lambda)` and `C(lambda)`, constructs a Sturm–Liouville weight `rho`, introduces

\[
H_\Lambda
=-\frac1{2\rho}\frac d{d\lambda}
\left(\rho B\frac d{d\lambda}\right)+V,
\]

uses a multiplicative transform to remove the first derivative, states self-adjointness/discrete-spectrum results, and applies first-order perturbation theory.

The audit finds that these steps are not all licensed by the hypotheses stated in the source.

---

# 2. Gate P1 — projectability of the Laplacian

Let

\[
U\subset M,
\qquad
\Lambda:U\to I\subset\mathbb R
\]

be a smooth submersion, and define the pullback algebra

\[
\mathscr A_\Lambda
:=
\{\Phi\circ\Lambda:\Phi\in C^\infty(I)\}.
\]

## Theorem P1 — exact projectability criterion

The following are equivalent:

1. the Laplacian preserves the pullback algebra,
   \[
   \Delta\mathscr A_\Lambda\subseteq\mathscr A_\Lambda;
   \]
2. there exist functions
   \[
   B,C:I\to\mathbb R
   \]
   such that
   \[
   \boxed{
   |\nabla\Lambda|^2=B\circ\Lambda,
   \qquad
   \Delta\Lambda=C\circ\Lambda.
   }
   \]

Under these conditions

\[
\boxed{
\Delta(\Phi\circ\Lambda)
=
\bigl(B\Phi''+C\Phi'\bigr)\circ\Lambda.
}
\]

### Proof

If `B,C` factor through `Lambda`, the chain-rule identity gives the result immediately.

Conversely, assume `Delta A_Lambda subset A_Lambda`. Applying this to `Phi(lambda)=lambda` gives

\[
\Delta\Lambda=C\circ\Lambda.
\]

Applying it to `Phi(lambda)=lambda^2/2` gives

\[
\Delta\left(\frac12\Lambda^2\right)
=|\nabla\Lambda|^2+\Lambda\Delta\Lambda.
\]

The left side and the second term on the right factor through `Lambda`, hence so does `|grad Lambda|^2`. \(\square\)

## Migration verdict

The source's pointwise identity is `PASS`.

The source's transition from `B(x),C(x)` to a one-dimensional operator with `B(lambda),C(lambda)` is `BLOCKED WITHOUT P1`.

The conditions

\[
D=D(\Lambda),
\qquad
\nu=U(\Lambda)d\Lambda
\]

used later in the historical class `PSI-13` do not by themselves establish P1 for the Laplacian.

Therefore P1 becomes the first mandatory PHISICA operator gate.

---

# 3. Gate P2 — projectability of the potential

For a Schrödinger-type operator

\[
H=-\frac12\Delta+V,
\]

preservation of `A_Lambda` also requires multiplication by `V` to preserve that algebra.

Since `1 in A_Lambda`, this is equivalent to

\[
\boxed{
V=V_\Lambda\circ\Lambda
}
\]

on the reduction domain.

Hence the exact invariant-subspace condition is

\[
\boxed{
|\nabla\Lambda|^2=B\circ\Lambda,
\quad
\Delta\Lambda=C\circ\Lambda,
\quad
V=V_\Lambda\circ\Lambda.
}
\]

Only after these conditions are established does the scalar differential expression

\[
L_\Lambda
=B(\lambda)\frac{d^2}{d\lambda^2}
+C(\lambda)\frac d{d\lambda}
\]

represent the restriction/projected action on functions of `Lambda`.

---

# 4. Gate P3 — Sturm–Liouville weight

Assume on an interval `I` that

\[
B>0,
\qquad
B,C\ \text{have the regularity required below}.
\]

A positive integrating factor `rho` satisfies

\[
\boxed{
(\rho B)'=\rho C.
}
\]

Equivalently

\[
\frac{\rho'}{\rho}
=\frac{C-B'}{B}.
\]

Thus locally

\[
\boxed{
\rho(\lambda)
=K\,B(\lambda)^{-1}
\exp\!\left(\int^\lambda\frac{C(\mu)}{B(\mu)}d\mu\right),
\qquad K>0.
}
\]

Hence

\[
B\partial_\lambda^2+C\partial_\lambda
=
\frac1\rho\partial_\lambda(\rho B\partial_\lambda).
\]

## Status correction

`rho` is not a third independent geometric primitive once `B,C` are fixed: it is determined up to a positive multiplicative constant on each connected interval.

The measure

\[
\rho(\lambda)d\lambda
\]

is the **Hilbert-space weight measure** for the reduced Sturm–Liouville representation. It must not be called a spectral measure without separately constructing the spectral measure/projection-valued measure of a self-adjoint operator.

## Geometric strengthening

If the pushforward of Riemannian volume by `Lambda` has a smooth density

\[
\Lambda_*(d\mathrm{vol}_g)=\rho_{geo}(\lambda)d\lambda
\]

and the reduction is projectable, then symmetry of the original Laplacian implies the same divergence relation

\[
(\rho_{geo}B)'=\rho_{geo}C
\]

under the corresponding no-boundary/no-flux hypotheses. This identifies the formal weight with the geometric pushforward weight up to normalization.

This stronger statement is retained as a target theorem for Volume III, not silently assumed here.

---

# 5. Gate P4 — what LOGOS can determine

The historical source defines

\[
\mathrm{LOGOS}=(B,C,\rho)
\]

and at places says that this triple uniquely determines the reduced dynamics.

The audit separates three levels.

### Kinetic differential expression

`B,C` determine

\[
L_\Lambda=B\partial_\lambda^2+C\partial_\lambda.
\]

Equivalently `B,rho` determine its divergence form when `(rho B)'=rho C`.

### Full formal Hamiltonian expression

To determine

\[
H_\Lambda
=-\frac1{2\rho}\partial_\lambda(\rho B\partial_\lambda)+V_\Lambda
\]

one must also specify `V_Lambda`.

### Self-adjoint operator

To determine an actual unbounded operator, one must additionally specify its Hilbert space and domain/boundary realization.

Therefore

\[
\boxed{
(B,C,\rho)
\not\Rightarrow
\text{unique full self-adjoint dynamics}.
}
\]

The historical claim survives only in the narrower form:

\[
\boxed{
(B,C)\ \text{determine the reduced kinetic differential expression},
}
\]

with `rho` an associated weight up to normalization.

---

# 6. Gate P5 — reparameterization

Let

\[
\mu=f(\lambda)
\]

be a smooth monotone coordinate change. For increasing `f`, the coefficients transform as

\[
\boxed{
\widetilde B(\mu)
=B(\lambda)[f'(\lambda)]^2,
}
\]

\[
\boxed{
\widetilde C(\mu)
=B(\lambda)f''(\lambda)+C(\lambda)f'(\lambda),
}
\]

and the weight density transforms by

\[
\boxed{
\widetilde\rho(\mu)
=\frac{\rho(\lambda)}{f'(\lambda)}.
}
\]

Thus the tuple of coefficient functions is not literally invariant. What is invariant is the underlying operator/weighted differential problem up to the declared coordinate transport.

Migration language:

\[
\boxed{
\text{reparameterization covariance / equivalence class},
\quad
\text{not coefficient-wise invariance}.
}
\]

---

# 7. Gate P6 — multiplicative drift removal

The historical transformation

\[
\psi=e^{\beta}\phi,
\qquad
\beta'=-\frac{C}{2B},
\]

is a correct **formal algebraic** elimination of the first-derivative term in

\[
-\frac12(B\psi''+C\psi')+V\psi.
\]

It yields formally

\[
-\frac12B\phi''+V_{eff}\phi
\]

with the stated correction

\[
V_{geom}
=
\frac{C'}4-rac{CB'}{4B}+\frac{C^2}{8B}.
\]

However:

1. multiplication by `e^beta` is not automatically unitary on `L^2(I,rho dlambda)`;
2. similarity preserves spectrum only after the function spaces and domains are transported by a bounded invertible map (or after another explicitly justified similarity framework);
3. the transformed non-divergence expression is not automatically self-adjoint in the original weighted Hilbert space;
4. a true Liouville normal form generally also transports the independent variable and the Hilbert-space weight.

Therefore the canonical PHISICA operator remains the **divergence-form Sturm–Liouville realization**. The historical `beta` transform is downgraded to

`FORMAL NORMAL-FORM / REQUIRES FUNCTION-SPACE BINDING`.

No spectral claim may use it before that binding is supplied.

---

# 8. Gate P7 — self-adjoint realization

The canonical reduced differential expression is

\[
\tau u
=
-\frac1{2\rho}(p u')'+Vu,
\qquad
p=\rho B.
\]

The Hilbert space is

\[
\mathcal H_\Lambda=L^2(I,\rho d\lambda).
\]

An operator is not determined until a domain is fixed.

For the regular finite-interval case, a convenient maximal domain is

\[
D(H_{max})
=
\left\{
 u\in L^2_\rho:
 u,pu'\in AC_{loc}(I),
 \tau u\in L^2_\rho
\right\}.
\]

The Lagrange boundary form is

\[
\boxed{
\mathcal B[u,v]
=
\frac12
\left[p(u'\bar v-u\bar v')\right]_a^b.
}
\]

Self-adjoint realizations are selected by boundary conditions that make this boundary form vanish maximally.

On a regular bounded interval, separated Robin conditions may be written as

\[
\cos\alpha\,u(a)+\sin\alpha\,p(a)u'(a)=0,
\]

\[
\cos\beta\,u(b)+\sin\beta\,p(b)u'(b)=0.
\]

Dirichlet and Neumann are special cases.

Hence the source statement

`regularity => possesses a self-adjoint extension`

is too imprecise for the current canon. The repaired statement is:

\[
\boxed{
\text{regular coefficients + explicit self-adjoint boundary realization}
\Rightarrow
\text{self-adjoint }H_\Lambda.
}
\]

On singular/unbounded intervals, endpoint classification must be handled separately.

---

# 9. Gate P8 — discrete spectrum

For a regular bounded interval, positive regular `p,rho`, real lower-bounded potential, and a self-adjoint regular Sturm–Liouville boundary realization, the resolvent is compact and the spectrum is purely discrete with finite multiplicities accumulating only at infinity.

Thus the source's discrete-spectrum statement is retained only with these hypotheses made explicit.

It is not valid as a blanket statement for arbitrary `I`.

---

# 10. Gate P9 — spectrum versus complete model information

The source repeatedly states that the eigenvalue sequence contains full dynamical information.

This is withdrawn as a general statement.

In general

\[
\boxed{
\{E_n\}\ \text{alone is not a complete invariant of an operator/model}.
}
\]

Isospectral but inequivalent operators/geometries exist, and even in one-dimensional inverse Sturm–Liouville theory additional spectral/norming/boundary data are generally required depending on the inverse problem.

The safe hierarchy is:

\[
\boxed{
\text{spectrum}=\text{invariant / observable signature},
\quad
\text{not automatically a complete identifier}.
}
\]

A self-adjoint operator is represented completely by its spectral theorem data only after the Hilbert-space representation and full projection-valued spectral measure are fixed. This is different from the coefficient weight `rho dlambda`.

HCube remains the permanent PSI warning against promoting a coarse spectral signature to a complete representation.

---

# 11. Gate P10 — perturbation and Hellmann–Feynman

The historical statement

\[
\delta E_n=\langle\phi_n,W\phi_n\rangle
\]

is not legal under only the phrase `H -> H + epsilon W`.

A sufficient clean contract is:

1. a fixed Hilbert space `H`;
2. a `C^1` family of self-adjoint operators `H(epsilon)` with a common domain, or a controlled differentiable family of closed forms;
3. an isolated simple eigenvalue `E_n(epsilon)`;
4. a normalized differentiable eigenvector branch `phi_n(epsilon)`.

Then

\[
\boxed{
E_n'(0)
=
\langle\phi_n(0),H'(0)\phi_n(0)\rangle.
}
\]

For a degenerate eigenvalue, first-order splitting is governed by the perturbation compressed to the eigenspace; one scalar expectation value is not generally sufficient.

In PHISICA, deformation of `Lambda` changes `B`, `C`, `rho` and potentially the interval/domain. Therefore the family must first be transported to a **fixed Hilbert space/domain framework** before Hellmann–Feynman is invoked.

Likewise

\[
\boxed{
\text{small coefficient deformation}
\not\Rightarrow
\text{small spectral deformation}
}
\]

without a topology such as norm-resolvent/form convergence or another perturbation theorem whose hypotheses are checked.

---

# 12. Migration status table

| Source component | Status after audit |
|---|---|
| Chain rule for `Delta(Phi o Lambda)` | `PASS` |
| `B(x),C(x) -> B(lambda),C(lambda)` | `REPAIR: P1 PROJECTABILITY REQUIRED` |
| Sturm–Liouville integrating factor | `PASS LOCALLY WITH B>0/REGULARITY` |
| `rho dlambda` called spectral measure | `RENAME: HILBERT/WEIGHT MEASURE` |
| `LOGOS=(B,C,rho)` as three independent data | `DOWNGRADE: rho DERIVED UP TO SCALE` |
| LOGOS determines full dynamics | `FAIL AS STATED: V + DOMAIN/BC ALSO REQUIRED` |
| monotone reparameterization | `PASS AS COVARIANCE/EQUIVALENCE, NOT LITERAL INVARIANCE` |
| multiplicative `beta` drift removal | `FORMAL PASS / FUNCTION-SPACE BINDING REQUIRED` |
| spectral invariance under `beta` | `BLOCKED UNTIL BOUNDED/UNITARY OR SIMILARITY BINDING` |
| self-adjointness | `REPAIR: DOMAIN + SA BOUNDARY CONDITIONS` |
| discrete spectrum on bounded regular interval | `PASS WITH REGULAR SA REALIZATION` |
| eigenfunctions ONB | `PASS AFTER SELF-ADJOINT + COMPACT RESOLVENT` |
| eigenvalues alone = full model information | `WITHDRAW` |
| first-order Hellmann–Feynman | `REPAIR: FIXED SPACE/DOMAIN + SIMPLE ISOLATED EIGENVALUE` |
| small deformation => spectral stability | `BLOCKED WITHOUT PERTURBATION TOPOLOGY` |
| historical PSI-13 central theorem | `GENEALOGY / REQUIRES P1+P2+P7 BEFORE REUSE` |

---

# 13. PSI relation

PHISICA supplies a realization of the already established PSI discipline:

- `Lambda` is a proposed representation/reduction coordinate;
- P1 tests whether the operator actually factors through that representation;
- domain/boundary data test whether the formal differential expression defines the claimed operator;
- spectral data are task representations whose adequacy must be tested, not assumed;
- perturbative conclusions require their own stability contract.

Thus the operator migration reinforces, rather than extends, the PSI core:

\[
\boxed{
\text{formal reduction}
\neq
\text{operator reduction}
\neq
\text{self-adjoint realization}
\neq
\text{spectral identifiability}.
}
\]

---

# 14. Volume III execution order

The repaired PHISICA sequence is:

\[
\boxed{
\mathrm{III.1\ PROJECTABILITY}
\to
\mathrm{III.2\ WEIGHT/STURM\!-\!LIOUVILLE}
\to
\mathrm{III.3\ DOMAIN/SELF\!-\!ADJOINTNESS}
\to
\mathrm{III.4\ SPECTRUM}
\to
\mathrm{III.5\ LIOUVILLE/NORMAL\ FORM}
\to
\mathrm{III.6\ PERTURBATION/HF}
\to
\mathrm{III.7\ PHISICA\ CROSSCHECK}.
}
\]

Historical `PSI-13`, `DNA`, and broad claims of spectral completeness remain genealogy until separately rebuilt under these gates.

---

# 15. Audit verdict

\[
\boxed{
\mathrm{PHISICA\ OPERATOR\ MIGRATION\ 01}
=
\mathrm{SOURCE\ RECOVERED\ /
REPAIR\ MAP\ ESTABLISHED\ /
NOT\ YET\ FROZEN}.
}
\]

No CORE5 change and no Agent v03 are justified.
