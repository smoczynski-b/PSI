# PRINCIPIA SEMANTICA — TOM III
## III.1. Projektowalność pola \(\Lambda\) i dokładna redukcja operatora

**Status:** `PHISICA REPAIR / THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Source audit:** `phisica-operator-migration-01.md`  
**Historical source:** `PHISICA — NEW.pdf`, operator-reduction chapters  
**Scope:** scalar Laplace–Beltrami / Schrödinger operator on a regular submersion region; exact deterministic reduction; no boundary/self-adjointness claim yet.

---

# 1. Type contract

Let

\[
(M,g)
\]

be a smooth Riemannian manifold and let

\[
U\subset M
\]

be a connected open set. Let

\[
\Lambda:U\to I:=\Lambda(U)\subset\mathbb R
\]

be a smooth submersion:

\[
\boxed{d\Lambda_x\neq0\qquad\forall x\in U.}
\]

Because `U` is connected and `Lambda` is a submersion to `R`, `I` is an interval.

Define the pullback operator

\[
T_\Lambda:C^\infty(I)\to C^\infty(U),
\qquad
T_\Lambda\Phi=\Phi\circ\Lambda,
\]

and its image algebra

\[
\mathscr A_\Lambda
:=
\operatorname{im}T_\Lambda
=
\{\Phi\circ\Lambda:\Phi\in C^\infty(I)\}.
\]

`A_Lambda` is the class of functions which are constant on every level set of `Lambda`.

---

# 2. Pointwise chain-rule identity

For every `Phi in C^infty(I)`,

\[
\boxed{
\Delta_g(\Phi\circ\Lambda)
=
|\nabla\Lambda|_g^2\,\Phi''(\Lambda)
+
(\Delta_g\Lambda)\,\Phi'(\Lambda).
}
\]

This identity is pointwise and does **not** by itself say that the right side is a function of `Lambda` alone.

That distinction is the central repair relative to historical PHISICA.

---

# 3. Theorem III.1.A — projectability of the Laplacian

The following statements are equivalent.

### (P1) Invariance of the pullback algebra

\[
\boxed{
\Delta_g\mathscr A_\Lambda
\subseteq
\mathscr A_\Lambda.
}
\]

### (P2) Level-set projectability of the geometric coefficients

There exist unique functions

\[
B,C:I\to\mathbb R
\]

such that

\[
\boxed{
|\nabla\Lambda|_g^2
=B\circ\Lambda,
\qquad
\Delta_g\Lambda
=C\circ\Lambda.
}
\]

### (P3) Exact intertwining with a one-dimensional operator

There exists a unique scalar second-order differential operator

\[
L_\Lambda
=
B(\lambda)\frac{d^2}{d\lambda^2}
+C(\lambda)\frac d{d\lambda}
\]

with

\[
\boxed{
\Delta_g\,T_\Lambda
=
T_\Lambda\,L_\Lambda.
}
\]

---

# 4. Proof

## (P2) => (P3)

For every `Phi`, the chain rule gives

\[
\Delta_g(T_\Lambda\Phi)
=
(B\circ\Lambda)\Phi''(\Lambda)
+(C\circ\Lambda)\Phi'(\Lambda),
\]

hence

\[
\Delta_gT_\Lambda\Phi
=
T_\Lambda(B\Phi''+C\Phi')
=
T_\Lambda L_\Lambda\Phi.
\]

Thus the intertwining identity holds.

## (P3) => (P1)

Immediate, since the right side belongs to `im T_Lambda`.

## (P1) => (P2)

Choose

\[
\Phi_1(\lambda)=\lambda.
\]

Then

\[
T_\Lambda\Phi_1=\Lambda.
\]

By (P1),

\[
\Delta_g\Lambda\in\mathscr A_\Lambda,
\]

so there exists `C:I->R` with

\[
\Delta_g\Lambda=C\circ\Lambda.
\]

Now choose

\[
\Phi_2(\lambda)=\frac12\lambda^2.
\]

Then

\[
\Delta_g\left(\frac12\Lambda^2\right)
=
|\nabla\Lambda|_g^2
+\Lambda\Delta_g\Lambda.
\]

By (P1) the left side belongs to `A_Lambda`, and the second term on the right already factors through `Lambda`. Therefore

\[
|\nabla\Lambda|_g^2\in\mathscr A_\Lambda,
\]

so

\[
|\nabla\Lambda|_g^2=B\circ\Lambda.
\]

Because `I=Lambda(U)`, the functions `B,C` are unique. This proves (P2). \(\square\)

---

# 5. Corollary III.1.B — Schrödinger projectability

Let

\[
H
=-\frac12\Delta_g+V
\]

act formally on smooth functions on `U`.

Then

\[
H\mathscr A_\Lambda\subseteq\mathscr A_\Lambda
\]

if and only if

1. `Lambda` satisfies III.1.A, and
2. the potential factors through `Lambda`:
   \[
   \boxed{V=V_\Lambda\circ\Lambda.}
   \]

When these conditions hold,

\[
\boxed{
H\,T_\Lambda
=
T_\Lambda H_\Lambda^{form},
}
\]

where

\[
\boxed{
H_\Lambda^{form}
=
-\frac12
\left(
B(\lambda)\frac{d^2}{d\lambda^2}
+C(\lambda)\frac d{d\lambda}
\right)
+V_\Lambda(\lambda).
}
\]

### Proof

The Laplace part is III.1.A. Multiplication by `V` preserves `A_Lambda` iff it sends the constant function `1` to an element of `A_Lambda`, i.e. iff `V=V_Lambda o Lambda`. \(\square\)

---

# 6. Why regularity is not enough

The historical regular region

\[
U=\{d\Lambda\neq0\}
\]

is necessary for using `Lambda` as a local transverse coordinate, but does not imply projectability.

## Counterexample III.1-X1

Take Euclidean

\[
U=\mathbb R^2,
\qquad
\Lambda(x,y)=x+y^2.
\]

Then

\[
d\Lambda=(1,2y)\neq0
\]

everywhere, so `Lambda` is a submersion.

But

\[
|\nabla\Lambda|^2
=1+4y^2.
\]

For a fixed level

\[
\Lambda(x,y)=\lambda,
\]

the value of `y` may vary, so `1+4y^2` is not constant on the level set. Hence there is no function `B(lambda)` satisfying

\[
|\nabla\Lambda|^2=B(\Lambda).
\]

Therefore

\[
\boxed{
\Delta\mathscr A_\Lambda
\not\subseteq
\mathscr A_\Lambda.
}
\]

The failure occurs despite `dLambda != 0` everywhere.

---

# 7. Positive benchmark

In Euclidean `R^n\setminus\{0\}` let

\[
\Lambda(x)=|x|^2.
\]

Then

\[
|\nabla\Lambda|^2=4|x|^2=4\Lambda,
\]

and

\[
\Delta\Lambda=2n.
\]

Thus

\[
B(\lambda)=4\lambda,
\qquad
C(\lambda)=2n,
\]

and the reduction is legal on every regular radial annulus.

This recovers the familiar radial-type one-dimensional reduction as an actual projectable case rather than as a generic consequence of having a scalar field.

---

# 8. Relation to PSI

`Lambda` is a candidate representation/reduction coordinate.

The condition

\[
\Delta_gT_\Lambda=T_\Lambda L_\Lambda
\]

is the operator analogue of the general PSI demand that downstream task-relevant structure factor through a proposed representation.

The important distinction is

\[
\boxed{
\text{scalar coordinate exists}
\not\Rightarrow
\text{operator descends through it}.
}
\]

No new PSI primitive is introduced.

---

# 9. Scope locks

III.1 does **not** yet establish:

- a Hilbert-space isometry between the full and reduced models;
- the correct one-dimensional weight `rho`;
- a domain for the unbounded reduced operator;
- self-adjointness;
- boundary conditions;
- discreteness of spectrum;
- completeness of spectral data;
- a Liouville/unitary normal form;
- perturbative stability.

These are later gates and must not be imported backward into III.1.

---

# 10. Local cross-check

### Types
`PASS`: `T_Lambda`, `Delta_g`, `L_Lambda` and their function spaces are explicit.

### Necessity
`PASS`: `Phi=lambda` and `Phi=lambda^2/2` recover `C` and `B`.

### Sufficiency
`PASS`: direct chain rule.

### Counterexample
`PASS`: regular submersion without level-set projectability exists.

### PSI scope
`PASS`: representation/factorization bridge only; no CORE change.

### Operator scope
`PASS`: no self-adjointness or spectral claim is made at this stage.

---

# 11. Verdict

\[
\boxed{
\mathrm{III.1\ LAMBDA\ OPERATOR\ PROJECTABILITY}
=
\mathrm{PASS}.
}
\]

Next legal unit:

\[
\boxed{
\mathrm{III.2\ —\ WEIGHT\ MEASURE\ AND\ STURM\!–\!LIOUVILLE\ FORM}.
}
\]
