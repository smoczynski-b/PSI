# PRINCIPIA SEMANTICA — VOLUME III.3

## Dziedzina, forma brzegowa i realizacja samosprzężona

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / LOCAL CROSS-CHECK PASS`  
**Date:** 2026-09-29  
**Upstream:** `principia-v3-01-lambda-operator-projectability.md`, `principia-v3-02-weight-sturm-liouville.md`  
**Historical source:** project file `PHISICA — NEW.pdf`  
**Classical bridge:** regular Sturm–Liouville theory on a finite interval.

---

# 1. Why III.3 is necessary

The differential expression

\[
\tau u
=
-\frac{1}{2\rho}(\rho B u')'+V u
\]

is not yet an unbounded operator.

A Hilbert space, operator domain and boundary realization must be fixed before self-adjointness is meaningful.

Thus:

\[
\boxed{
\text{formal Sturm–Liouville expression}
\neq
\text{self-adjoint operator}.
}
\]

This is the PHISICA lock PF04.

---

# 2. Regular contract

Let

\[
I=(a,b),
\qquad
-\infty<a<b<\infty.
\]

Assume

\[
B,\rho\in C^1([a,b]),
\qquad
B(\lambda)>0,
\qquad
\rho(\lambda)>0,
\]

and

\[
V\in C([a,b],\mathbb R).
\]

Set

\[
p(\lambda):=\rho(\lambda)B(\lambda)>0
\]

and

\[
\mathcal H_\rho:=L^2(I,\rho(\lambda)d\lambda).
\]

Define the real formally symmetric differential expression

\[
\tau u
=
-\frac{1}{2\rho}(p u')'+Vu.
\]

The present chapter treats only the regular finite-interval sector. Singular endpoints and Weyl limit-point/limit-circle theory are outside III.3.

---

# 3. Maximal realization

Define

\[
D(H_{\max})
:=
\left\{
 u\in\mathcal H_\rho:
 u,\,pu'\in AC([a,b]),
 \ \tau u\in\mathcal H_\rho
\right\}.
\]

Then

\[
H_{\max}u:=\tau u.
\]

Because the interval and coefficients are regular, the endpoint traces

\[
u(a),\quad (pu')(a),\quad u(b),\quad (pu')(b)
\]

are well-defined for every \(u\in D(H_{\max})\).

Introduce the boundary trace map

\[
\Gamma:D(H_{\max})\to\mathbb C^4,
\]

\[
\Gamma u
=
\big(u(a),(pu')(a),u(b),(pu')(b)\big).
\]

In the regular sector this map is surjective: arbitrary endpoint values and quasi-derivative values can be realized by a smooth function with prescribed endpoint jets.

---

# 4. Green–Lagrange identity

For \(u,v\in D(H_{\max})\), integration by parts gives

\[
\langle H_{\max}u,v\rangle_{\rho}
-
\langle u,H_{\max}v\rangle_{\rho}
=
\mathfrak b(u,v),
\]

where

\[
\boxed{
\mathfrak b(u,v)
=
\frac12
\left[
 u\,\overline{pv'}
-(pu')\,\overline v
\right]_{a}^{b}.
}
\]

Hence the obstruction to operator symmetry is purely boundary data.

Equivalently, if

\[
\omega\big((x_1,x_2),(y_1,y_2)\big)
:=x_1\overline{y_2}-x_2\overline{y_1},
\]

then

\[
2\mathfrak b(u,v)
=
\omega\big((u(b),(pu')(b)),(v(b),(pv')(b))\big)
-
\omega\big((u(a),(pu')(a)),(v(a),(pv')(a))\big).
\]

Thus self-adjoint boundary realizations correspond to maximal isotropic subspaces of the boundary trace space for this symplectic boundary form.

---

# 5. Minimal realization

Let

\[
H_0:=\tau|_{C_c^\infty(a,b)}
\]

and define

\[
H_{\min}:=\overline{H_0}.
\]

For the regular contract above,

\[
\boxed{
D(H_{\min})
=
\left\{
 u\in D(H_{\max}):
 u(a)=(pu')(a)=u(b)=(pu')(b)=0
\right\}.
}
\]

Moreover,

\[
\boxed{
H_{\min}^*=H_{\max}.
}
\]

## Proof sketch

1. Every compactly supported smooth function has zero boundary trace, so the closure of \(H_0\) is contained in the displayed four-trace kernel.
2. In the regular finite-interval case the graph closure of \(C_c^\infty(a,b)\) gives exactly that kernel.
3. The Green identity shows that every \(v\in D(H_{\max})\) defines a bounded graph functional against \(H_{\min}\), hence \(H_{\max}\subseteq H_{\min}^*\).
4. Conversely, testing against compactly supported smooth functions forces any vector in \(D(H_{\min}^*)\) to possess the local regularity of the maximal domain and satisfy \(H_{\min}^*v=\tau v\).

Therefore the adjoint of the minimal realization is precisely the maximal realization.

---

# 6. Separated Robin self-adjoint realizations

Let

\[
\alpha,\beta\in[0,\pi).
\]

Define

\[
D(H_{\alpha,\beta})
:=
\left\{
 u\in D(H_{\max}):
 \cos\alpha\,u(a)
 +\sin\alpha\,(pu')(a)=0,
\right.
\]

\[
\left.
 \cos\beta\,u(b)
 +\sin\beta\,(pu')(b)=0
\right\}.
\]

Set

\[
H_{\alpha,\beta}u:=\tau u.
\]

## Theorem III.3.A — regular separated self-adjoint realization

Under the regular contract of Section 2,

\[
\boxed{
H_{\alpha,\beta}=H_{\alpha,\beta}^*.
}
\]

### Proof

At each endpoint the Robin condition selects a one-dimensional real line in the two-dimensional boundary space

\[
(u,pu').
\]

Any such line is isotropic for the endpoint symplectic form \(\omega\). Therefore for any

\[
u,v\in D(H_{\alpha,\beta})
\]

both endpoint contributions in the Green form vanish and

\[
\mathfrak b(u,v)=0.
\]

Hence

\[
H_{\alpha,\beta}\subseteq H_{\alpha,\beta}^*.
\]

To compute the adjoint, let

\[
v\in D(H_{\alpha,\beta}^*).
\]

Since

\[
H_{\min}\subseteq H_{\alpha,\beta},
\]

we have

\[
v\in D(H_{\min}^*)=D(H_{\max}).
\]

The condition that

\[
\mathfrak b(u,v)=0
\quad
\forall u\in D(H_{\alpha,\beta})
\]

forces the boundary trace of \(v\) to lie in the symplectic annihilator of the Robin boundary subspace. Because this subspace is maximal isotropic, its symplectic annihilator is itself. Hence \(v\) satisfies the same two Robin conditions.

Thus

\[
D(H_{\alpha,\beta}^*)
=
D(H_{\alpha,\beta}),
\]

which proves self-adjointness.

---

# 7. Classical boundary cases recovered

The historical PHISICA list becomes a precise subfamily:

- \(\alpha=0\): Dirichlet at \(a\), \(u(a)=0\);
- \(\alpha=\pi/2\): Neumann/quasi-Neumann at \(a\), \((pu')(a)=0\);
- analogously at \(b\);
- different endpoint choices give mixed separated conditions.

Thus the old statement that the boundary conditions determine the self-adjoint realization survives, but only after the operator domain is explicit.

The source itself noted that the exact self-adjoint operator depends on the boundary conditions; III.3 turns this remark into the formal operator theorem.

---

# 8. What III.3 does not claim

III.3 does not establish:

- classification of all coupled self-adjoint boundary conditions;
- singular-endpoint self-adjointness;
- essential self-adjointness on \(C_c^\infty\);
- compact resolvent or discreteness of spectrum;
- semiboundedness for arbitrary nonregular coefficients;
- equivalence of distinct boundary realizations.

Those are separate questions.

In particular:

\[
\boxed{
\text{formal symmetry}
\not\Rightarrow
\text{self-adjointness}
}
\]

and

\[
\boxed{
\text{one self-adjoint boundary realization}
\not\Rightarrow
\text{uniqueness of self-adjoint realization}.
}
\]

---

# 9. Relation to historical PHISICA

Historical PHISICA supplied:

1. a candidate domain with absolute-continuity conditions;
2. a theorem asserting existence of a self-adjoint extension;
3. a list of Dirichlet, Neumann and mixed boundary conditions;
4. the observation that the boundary choice determines the exact self-adjoint operator.

The source did not yet provide the minimal/maximal operator pair, the Green boundary form, or the proof that a stated boundary domain is self-adjoint.

III.3 repairs exactly that missing operator layer.

---

# 10. Classical status

The minimal/maximal Sturm–Liouville operators, Green–Lagrange boundary form and regular self-adjoint boundary realizations are classical operator theory.

PSI/PHISICA contribution here is not a claim of novelty. It is the explicit insertion of the correct operator gate into the migration chain

\[
\boxed{
\mathrm{PROJECTABILITY}
\to
\mathrm{WEIGHT}
\to
\mathrm{DOMAIN/SELF\!-\!ADJOINTNESS}.
}
\]

Classical references checked during migration include DLMF sections on regular Sturm–Liouville systems and self-adjoint second-order operators, together with the standard maximal/minimal operator framework.

---

# 11. Regression / falsification locks

III.3 is protected by:

- PF04 — formal differential expression != unbounded operator;
- PF06 — coefficient/LOGOS data != full self-adjoint dynamics;
- PF12 — formal symmetry or arbitrary boundary restrictions do not by themselves establish self-adjointness; the boundary subspace must be maximal isotropic / the adjoint domain must coincide.

---

# 12. Verdict

\[
\boxed{
\mathrm{III.3}=\mathrm{PASS}.
}
\]

The next legal unit is III.4 — compact resolvent and discrete spectrum for the regular bounded-interval self-adjoint realizations established here.
