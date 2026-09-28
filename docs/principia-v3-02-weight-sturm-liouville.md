# PRINCIPIA SEMANTICA — TOM III
## III.2. Miara wagowa, forma Sturma–Liouville’a i pushforward geometryczny

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Upstream:** `principia-v3-01-lambda-operator-projectability.md`  
**Source audit:** `phisica-operator-migration-01.md`  
**Historical source:** project file `PHISICA — NEW.pdf`  
**Classical bridge:** coarea formula + weighted Sturm–Liouville formalism  
**Scope:** exact smooth operator reduction; no self-adjointness claim, no spectral-measure claim, no perturbation claim.

---

# 1. Upstream contract

Let \((U,g)\) be a smooth Riemannian manifold and let

\[
\Lambda:U\to I\subset\mathbb R
\]

be a smooth scalar field. Assume the III.1 projectability gate:

\[
|\nabla\Lambda|^2=B\circ\Lambda,
\qquad
\Delta_g\Lambda=C\circ\Lambda,
\]

with

\[
B\in C^1(I),\qquad C\in C(I),\qquad B(\lambda)>0.
\]

Then the algebra of fibre-constant functions is invariant under \(\Delta_g\), and the reduced differential expression is

\[
L_\Lambda
=
B(\lambda)\frac{d^2}{d\lambda^2}
+
C(\lambda)\frac{d}{d\lambda}.
\]

For a Schrödinger-type expression

\[
H=-\frac12\Delta_g+V
\]

we additionally require

\[
V=V_\Lambda\circ\Lambda.
\]

---

# 2. The integrating-factor theorem

## Theorem III.2.A — positive Sturm–Liouville weight

Let \(I\) be a connected interval, \(B\in C^1(I)\) with \(B>0\), and \(C\in C(I)\). Then there exists a positive \(C^1\) function

\[
\rho:I\to(0,\infty)
\]

satisfying

\[
\boxed{(\rho B)'=\rho C.}
\]

It is unique up to multiplication by a positive constant. Explicitly,

\[
\boxed{
\rho(\lambda)
=K\,\frac1{B(\lambda)}
\exp\!\left(
\int_{\lambda_0}^{\lambda}
\frac{C(\mu)}{B(\mu)}\,d\mu
\right),
\qquad K>0.
}
\]

Consequently

\[
\boxed{
L_\Lambda f
=
\frac1\rho\frac d{d\lambda}
\left(\rho B f'\right).
}
\]

### Proof

The equation \((\rho B)'=\rho C\) gives

\[
\frac{\rho'}\rho
=
\frac{C-B'}{B}.
\]

Integration yields the displayed formula. Conversely, direct differentiation verifies \((\rho B)'=\rho C\). Since the logarithmic derivative is fixed, any two positive solutions differ by a positive multiplicative constant. Substitution gives the divergence form. \(\square\)

---

# 3. Formal symmetry — not self-adjointness

On \(C_c^\infty(I)\), with

\[
\langle f,g\rangle_\rho
=
\int_I \overline f g\,\rho\,d\lambda,
\]

we have

\[
\langle f,L_\Lambda g\rangle_\rho
=
-\int_I B\,\overline{f'}g'\,\rho\,d\lambda
=
\langle L_\Lambda f,g\rangle_\rho.
\]

Thus \(L_\Lambda\) is **formally symmetric** on compactly supported test functions.

For real \(V_\Lambda\),

\[
H_\Lambda^{\rm form}
=
-\frac1{2\rho}\frac d{d\lambda}
\left(\rho B\frac d{d\lambda}\right)
+V_\Lambda
\]

is likewise formally symmetric on \(C_c^\infty(I)\).

This does **not** yet define a self-adjoint operator. The domain, endpoint classification and boundary realization are III.3.

\[
\boxed{
\text{formal Sturm–Liouville form}
\not\Rightarrow
\text{self-adjoint realization}.
}
\]

---

# 4. Geometric pushforward theorem

The historical PHISICA text introduced \(\rho\) algebraically and then called \(\rho(\lambda)d\lambda\) a natural spectral measure. The geometric identification requires a separate theorem.

Assume now in addition:

1. \(U\) has no boundary;
2. \(\Lambda:U\to I\) is a smooth **proper submersion** onto a connected open interval \(I\);
3. the III.1 projectability conditions hold;
4. \(d\mathrm{vol}_g\) is the Riemannian volume measure.

Define

\[
\mu_\Lambda
:=
\Lambda_*(d\mathrm{vol}_g).
\]

Properness ensures local finiteness over compact subintervals.

## Theorem III.2.B — pushforward density equals the canonical weight up to scale

The measure \(\mu_\Lambda\) is absolutely continuous with respect to Lebesgue measure and, by the coarea formula,

\[
\boxed{
\mu_\Lambda(d\lambda)
=
m(\lambda)\,d\lambda,
\qquad
m(\lambda)
=
\int_{\Sigma_\lambda}
\frac{1}{|\nabla\Lambda|}\,dA_\lambda,
}
\]

where

\[
\Sigma_\lambda=\Lambda^{-1}(\lambda).
\]

Moreover \(m\) satisfies, in the distributional sense and hence classically under the stated smooth proper-submersion hypotheses,

\[
\boxed{(mB)'=mC.}
\]

Therefore, on connected \(I\),

\[
\boxed{m=K\rho\qquad(K>0).}
\]

After fixing the multiplicative normalization of \(\rho\), one may choose

\[
\boxed{
\rho(\lambda)d\lambda
=
\Lambda_*(d\mathrm{vol}_g).
}
\]

### Proof

The coarea formula for the scalar submersion gives

\[
\int_U F(x)\,d\mathrm{vol}_g(x)
=
\int_I
\left[
\int_{\Sigma_\lambda}
\frac{F}{|\nabla\Lambda|}\,dA_\lambda
\right]d\lambda.
\]

Taking \(F(x)=h(\Lambda(x))\) yields the density \(m\).

Now take \(\Phi,\Psi\in C_c^\infty(I)\). Properness makes their pullbacks compactly supported in \(U\). Green's identity gives

\[
\int_U
(\Psi\circ\Lambda)\,
\Delta_g(\Phi\circ\Lambda)
\,d\mathrm{vol}_g
=
-
\int_U
\langle
\nabla(\Psi\circ\Lambda),
\nabla(\Phi\circ\Lambda)
\rangle
\,d\mathrm{vol}_g.
\]

Using projectability,

\[
\Delta_g(\Phi\circ\Lambda)
=
(B\Phi''+C\Phi')\circ\Lambda
\]

and

\[
\langle
\nabla(\Psi\circ\Lambda),
\nabla(\Phi\circ\Lambda)
\rangle
=
(B\Psi'\Phi')\circ\Lambda.
\]

Push forward to \(I\):

\[
\int_I
\Psi(B\Phi''+C\Phi')m\,d\lambda
=
-
\int_I
B\Psi'\Phi'm\,d\lambda.
\]

Integrating the right-hand side by parts gives

\[
\int_I
\Psi\big((mB)'\Phi'+mB\Phi''\big)d\lambda.
\]

Since this holds for arbitrary compactly supported \(\Psi,\Phi\),

\[
(mB)'=mC.
\]

The uniqueness part of Theorem III.2.A then yields \(m=K\rho\). \(\square\)

---

# 5. Exact Hilbert-space reduction

With the geometric normalization

\[
\rho\,d\lambda
=
\Lambda_*(d\mathrm{vol}_g),
\]

define

\[
T_\Lambda:
L^2(I,\rho d\lambda)
\to
L^2(U,d\mathrm{vol}_g),
\qquad
T_\Lambda\Phi=\Phi\circ\Lambda.
\]

Then by definition of pushforward,

\[
\boxed{
\|T_\Lambda\Phi\|_{L^2(U)}^2
=
\|\Phi\|_{L^2(I,\rho d\lambda)}^2.
}
\]

Thus \(T_\Lambda\) is an isometry onto the closed fibre-constant subspace

\[
\mathscr H_\Lambda
:=
\overline{\{\Phi\circ\Lambda:\Phi\in C_c^\infty(I)\}}^{L^2(U)}.
\]

Under III.1 projectability, the formal reduced operator is the operator transported to this subspace.

This is the correct Hilbert-space meaning of the one-dimensional reduction. Full unbounded-operator equivalence still requires III.3 domains.

---

# 6. Three different measures — permanent distinction

The notation \(\rho\) in the historical text obscured three distinct objects.

### 6.1 Sturm–Liouville/Hilbert weight

\[
\rho(\lambda)d\lambda
\]

chosen so that

\[
(\rho B)'=\rho C.
\]

### 6.2 Geometric pushforward measure

\[
\Lambda_*(d\mathrm{vol}_g).
\]

Under Theorem III.2.B this equals the weight measure after normalization.

### 6.3 Spectral measure

A spectral measure belongs to the spectral theorem for a specified self-adjoint realization (projection-valued, or a scalar measure after choosing a cyclic/vector state). It is **not** supplied merely by the coefficient \(\rho\).

Therefore:

\[
\boxed{
\text{Hilbert weight}
\neq
\text{spectral measure}.
}
\]

The historical phrase "naturalna miara spektralna" is retained only as genealogy.

---

# 7. Status of LOGOS after III.2

The historical triple

\[
\mathrm{LOGOS}=(B,C,\rho)
\]

contains redundancy:

\[
\boxed{
B,C
\Longrightarrow
\rho\ \text{up to a positive scalar factor}.
}
\]

When the geometric normalization is available, that factor is fixed by

\[
\rho d\lambda=\Lambda_*(d\mathrm{vol}_g).
\]

Hence \((B,C,\rho)\) should be interpreted as a **derived weighted representation of the reduced differential expression**, not as three independent primitive data and not as the full self-adjoint dynamics.

The potential, operator domain and boundary realization remain additional information.

---

# 8. Boundaries / falsifiers

- **PF01/PF02:** regularity of \(\Lambda\) alone does not imply projectability of \(B,C\).
- **PF03:** \(\rho d\lambda\) is not automatically a spectral measure.
- **PF04:** divergence-form differential expression is not yet an unbounded operator.
- **PF06:** \((B,C,\rho)\) does not determine the full self-adjoint dynamics.

Additional boundary:

\[
\boxed{
\text{formal integrating factor}
\not\Rightarrow
\text{geometric pushforward identification}.
}
\]

Without properness/local finiteness or an equivalent integration contract, fibre volumes may diverge and the geometric measure need not furnish the Hilbert realization used above.

---

# 9. Source status

### Historical PHISICA source

The source correctly derives

\[
\rho
=
\frac1B\exp\!\int\frac CB\,d\lambda
\]

and the formal Sturm–Liouville expression. Its later naming of \(\rho d\lambda\) as a spectral measure is stronger than what those calculations establish.

### Classical content

- integrating-factor conversion to Sturm–Liouville form: classical;
- coarea formula: classical;
- Green identity: classical.

### PSI/PHISICA contribution here

The relevant migration result is the **typed composition of gates**:

\[
\boxed{
\text{III.1 projectability}
\to
\text{III.2 canonical weight}
\to
\text{geometric pushforward bind when licensed}
\to
\text{III.3 operator domain/self-adjointness}.
}
\]

No CORE5 growth follows.

---

# 10. Verdict

\[
\boxed{
\mathrm{III.2}
=
\mathrm{PROOF\ PASS / LOCAL\ CROSS\!\!\!-\!CHECK\ PASS}.
}
\]

The next legal unit is III.3: domain, boundary form and self-adjoint realizations.
