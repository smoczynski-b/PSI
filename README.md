# PSI

**PSI is a formal research program on justified inference under constrained observation.**

It asks:

> What are we entitled to conclude from what we can actually observe?

The central compatible set is

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

For a task \(\mathcal T\), exact resolution means

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)^2\subseteq E_{\mathcal T}.
\]

## Current control pointers

- [Physical CANON-03 source bind](docs/canon03-source-bind-01.md)
- [Core mathematical skeleton](docs/core.md)
- [Current claim registry v13](docs/claim-registry-13.md)
- [Current falsifier registry v12](docs/falsifier-registry-12.md)
- [Freeze 01](docs/principia-v1-v2-freeze-01.md)
- [Freeze 01 Errata 01](docs/principia-v1-v2-freeze-01-errata-01.md)
- [Current Volume Skeleton 03](docs/principia-volume-skeleton-03.md)
- [Volume III Addendum 01](docs/principia-volume-skeleton-03-v3-addendum-01.md)
- [Current V2 Theorem Map 04](docs/principia-v2-theorem-map-04.md)
- [Current V3 Theorem Map 01](docs/principia-v3-theorem-map-01.md)
- [PHISICA Operator Migration 01](docs/phisica-operator-migration-01.md)
- [PHISICA Falsifier Registry 01](docs/phisica-falsifier-registry-01.md)
- [Volume III.1 — Lambda operator projectability](docs/principia-v3-01-lambda-operator-projectability.md)
- [Volume III.2 — weighted Sturm–Liouville / pushforward measure](docs/principia-v3-02-weight-sturm-liouville.md)
- [Volume III.3 — domain and self-adjoint realization](docs/principia-v3-03-domain-selfadjoint.md)
- [Volume III.4 — compact resolvent and discrete spectrum](docs/principia-v3-04-compact-resolvent-spectrum.md)
- [Volume III.5 — unitary Liouville normal form](docs/principia-v3-05-liouville-normal-form.md)
- [Decision / Epistemic Ledger base](docs/psi-ledger-01.md)
- [Ledger Addendum 02](docs/psi-ledger-01-addendum-02.md)
- [Ledger Addendum 03 — PHISICA migration](docs/psi-ledger-01-addendum-03.md)
- [Agent PSI Architecture v02](docs/agent-psi-architecture-02.md)
- [Current Sector Work Map 02](docs/work-map-02.md)

Historical maps, skeletons and pre-repair PHISICA material remain for provenance.

## Core status

\[
\boxed{
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
}
\]

CORE5 remains frozen. Current pressure evidence does not force R4; this is not a universal completeness theorem.

Exact task-information adequacy:

\[
\boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}.}
\]

Inference discipline:

\[
\boxed{
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
}
\]

## Principia status

### Volume I

\[
\boxed{\mathrm{V1\ FIRST\ PROSE\ PASS}=\mathrm{NORMALIZED\ PASS}.}
\]

### Volume II

\[
\boxed{
\mathrm{PRINCIPIA\ V2\ II.1:II.16}
=\mathrm{MATHEMATICAL\ GLOBAL\ PASS}.
}
\]

The V2 control layer is normalized through Volume Skeleton 03 and V2 Theorem Map 04.

### Freeze Errata 01

The former C19-v2 singleton statement for the gauge-only factorization fibre is withdrawn. Current MINI keeps unique normal-form class rather than literal gauge-only factorization uniqueness. No CORE role changed and no Agent v03 is justified.

## Volume III — PHISICA operator migration

Historical PHISICA is being rebuilt by operator legality rather than copied chapter-by-chapter.

### III.1 — operator projectability

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

For a Schrödinger-type reduction one additionally requires

\[
\boxed{V=V_\Lambda\circ\Lambda.}
\]

### III.2 — weight, Sturm–Liouville form and geometric pushforward

\[
\boxed{(\rho B)'=\rho C},
\qquad
\boxed{
L_\Lambda=\rho^{-1}\partial_\lambda(\rho B\partial_\lambda).
}
\]

Under the additional proper-submersion/coarea contract, after normalization,

\[
\boxed{
\rho(\lambda)d\lambda
=\Lambda_*(d\mathrm{vol}_g).
}
\]

### III.3 — operator domain and self-adjoint realization

For

\[
p=\rho B,
\qquad
\tau u=-\frac1{2\rho}(pu')'+Vu,
\]

one has

\[
\boxed{H_{\min}^*=H_{\max}}
\]

and separated Robin conditions define self-adjoint realizations.

### III.4 — compact resolvent and discrete spectrum

For the regular finite-interval realizations from III.3,

\[
\boxed{(H-z)^{-1}\text{ compact}}
\]

for every resolvent point, hence

\[
\boxed{
\sigma(H)=\{E_n\},
\qquad
E_n\to+\infty,
}
\]

with finite multiplicities and a complete orthonormal eigenbasis.

### III.5 — unitary Liouville normal form

Historical PHISICA used the multiplier

\[
\psi=e^\beta\phi,
\qquad
\beta'=-\frac{C}{2B},
\]

which correctly removes the first derivative algebraically. Under the regular compact contract it becomes a bounded similarity only after exact domain transport; it is not generally unitary.

The canonical Liouville transform is

\[
\boxed{
x(\lambda)=\int_a^\lambda B(\mu)^{-1/2}d\mu,
}
\]

\[
\boxed{
(Uu)(x)=\rho(\lambda(x))^{1/2}B(\lambda(x))^{1/4}u(\lambda(x)).
}
\]

Then

\[
\boxed{
U:L^2(I,\rho d\lambda)\to L^2(J,dx)
\text{ is unitary}
}
\]

and

\[
\boxed{
UHU^{-1}
=-\frac12\frac{d^2}{dx^2}
+V(\lambda(x))+rac{s_{xx}}{2s}.
}
\]

Thus self-adjointness, spectrum, multiplicities, compact resolvent and the eigenbasis are preserved by a genuine unitary equivalence.

Permanent distinctions now include

\[
\boxed{
\text{Hilbert weight}\neq\text{spectral measure},
}

\[
\boxed{
\text{formal symmetry}\not\Rightarrow\text{self-adjointness},
}

\[
\boxed{
\text{self-adjointness}\not\Rightarrow\text{compact resolvent/discrete spectrum},
}
\]

\[
\boxed{
\text{bounded similarity}\neq\text{unitary equivalence},
}
\]

and

\[
\boxed{
\{E_n\}\not\Rightarrow\text{complete model identification}.
}
\]

`III.1–III.5` are PASS. The next unit is `III.6 — perturbation / Hellmann–Feynman`.

## Current phase

\[
\boxed{
\mathrm{V1\ PASS}
\to
\mathrm{V2\ GLOBAL\ PASS}
\to
\mathrm{PHISICA\ SOURCE\ AUDIT}
\to
\mathrm{III.1:III.5\ PASS}
\to
\mathrm{III.6\ NEXT}.
}
\]

Primitive growth remains stopped until a new typed counterexample forces a genuinely new semantic role.

## Publications / Zenodo

- DOI: 10.5281/zenodo.18893354
- DOI: 10.5281/zenodo.18644750
- DOI: 10.5281/zenodo.18498472
- DOI: 10.5281/zenodo.18498440

## Language

Internal theoretical development is primarily in Polish. Public interoperability and repository-facing material are written in English.

## License

MIT. See [LICENSE](LICENSE).
