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
- [Volume III Addendum 02 — PHISICA closure / MOST handoff](docs/principia-volume-skeleton-03-v3-addendum-02.md)
- [Current V2 Theorem Map 04](docs/principia-v2-theorem-map-04.md)
- [Current V3 Theorem Map 02](docs/principia-v3-theorem-map-02.md)
- [PHISICA Operator Migration 01](docs/phisica-operator-migration-01.md)
- [PHISICA Operator Migration 01 — Errata 01](docs/phisica-operator-migration-01-errata-01.md)
- [PHISICA Whole-Block Crosscheck 01](docs/principia-v3-phisica-whole-crosscheck-01.md)
- [PHISICA Falsifier Registry 01](docs/phisica-falsifier-registry-01.md)
- [Volume III.1 — Lambda operator projectability](docs/principia-v3-01-lambda-operator-projectability.md)
- [Volume III.2 — weighted Sturm–Liouville / pushforward measure](docs/principia-v3-02-weight-sturm-liouville.md)
- [Volume III.3 — domain and self-adjoint realization](docs/principia-v3-03-domain-selfadjoint.md)
- [Volume III.4 — compact resolvent and discrete spectrum](docs/principia-v3-04-compact-resolvent-spectrum.md)
- [Volume III.5 — unitary Liouville normal form](docs/principia-v3-05-liouville-normal-form.md)
- [Volume III.6 — perturbation and Hellmann–Feynman](docs/principia-v3-06-perturbation-hellmann-feynman.md)
- [Decision / Epistemic Ledger base](docs/psi-ledger-01.md)
- [Ledger Addendum 02](docs/psi-ledger-01-addendum-02.md)
- [Ledger Addendum 03 — PHISICA migration](docs/psi-ledger-01-addendum-03.md)
- [Ledger Addendum 04 — PHISICA whole-block handoff](docs/psi-ledger-01-addendum-04.md)
- [Agent PSI Architecture v02](docs/agent-psi-architecture-02.md)
- [Current Sector Work Map 03](docs/work-map-03.md)

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

## Volume III — PHISICA operator block

Historical PHISICA was rebuilt by operator legality rather than copied chapter-by-chapter.

The certified chain is

\[
\boxed{
\mathrm{PROJECTABILITY}
\to
\mathrm{WEIGHTED\ REALIZATION}
\to
\mathrm{SELF\!\!-\!ADJOINT\ REALIZATION}
\to
\mathrm{COMPACT\ SPECTRAL\ THEORY}
\to
\mathrm{UNITARY\ LIOUVILLE\ NORMAL\ FORM}
\to
\mathrm{PERTURBATION/HELLMANN\!\!-\!FEYNMAN}.
}
\]

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

For Schrödinger reduction additionally

\[
\boxed{V=V_\Lambda\circ\Lambda.}
\]

### III.2 — weight / Sturm–Liouville / geometric pushforward

\[
\boxed{(\rho B)'=\rho C},
\qquad
\boxed{L_\Lambda=\rho^{-1}\partial_\lambda(\rho B\partial_\lambda).}
\]

Under the additional proper-submersion/coarea contract,

\[
\boxed{\rho d\lambda=\Lambda_*(d\mathrm{vol}_g)}
\]

after normalization. This geometric bind is an optional strengthening, not a prerequisite for every downstream regular Sturm–Liouville model.

### III.3 — domain and self-adjoint realization

The regular minimal/maximal realizations satisfy

\[
\boxed{H_{\min}^*=H_{\max}}.
\]

The whole-block audit corrected the inner-product/boundary-form convention. With

\[
\langle f,g\rangle_\rho=\int\overline f g\rho,
\]

the Green–Lagrange form is

\[
\boxed{
\mathfrak b(u,v)
=\frac12[\overline u\,pv'-\overline{pu'}v]_a^b.
}
\]

Separated real Robin relations select maximal-isotropic complex boundary subspaces and define self-adjoint realizations.

### III.4 — compact resolvent and discrete spectrum

For the regular finite-interval realizations,

\[
\boxed{(H-z)^{-1}\text{ compact}},
\]

hence

\[
\boxed{\sigma(H)=\{E_n\},\qquad E_n\to+\infty}
\]

with finite multiplicities and a complete orthonormal eigenbasis.

### III.5 — unitary Liouville normal form

\[
\boxed{x(\lambda)=\int_a^\lambda B(\mu)^{-1/2}d\mu},
\]

\[
\boxed{(Uu)(x)=\rho^{1/2}B^{1/4}u}
\]

defines a unitary map to ordinary \(L^2(J,dx)\), with

\[
\boxed{UHU^{-1}=-\frac12\partial_x^2+V(\lambda(x))+\frac{s_{xx}}{2s}.}
\]

The historical drift-killing multiplier survives only as a bounded similarity after exact domain transport; bounded similarity is not unitary equivalence.

### III.6 — perturbation and Hellmann–Feynman

After legal trivialization to one fixed Hilbert space/domain,

\[
H(t)=H_0+W(t),
\]

with bounded self-adjoint norm-\(C^1\) perturbation. Then

\[
\boxed{|E_n(t)-E_n(s)|\le\|W(t)-W(s)\|.}
\]

For a simple isolated branch, with graph-norm differentiable eigenvector,

\[
\boxed{E'(t)=\langle\phi(t),W'(t)\phi(t)\rangle.}
\]

Degenerate first-order splitting is governed by the compressed perturbation on the eigenspace. Raw geometric/LOGOS deformations require an additional fixed-space or closed-form trivialization when spaces, intervals or domains vary.

### PHISICA whole-block result

Local PASS results were not promoted automatically. `PHISICA Whole-Block Crosscheck 01` audited the six units together, found the III.3 boundary-form convention defect, applied the local errata and then granted:

\[
\boxed{
\mathrm{PHISICA\ III.1:III.6}
=\mathrm{MATHEMATICAL\ GLOBAL\ PASS\ AFTER\ LOCAL\ ERRATA\ 01}.
}
\]

The arrows above must be read as **progressively stronger typed contracts**, not as a blanket implication that every III.1 model satisfies III.2–III.6.

Permanent distinctions include

\[
\boxed{\text{Hilbert weight}\neq\text{spectral measure}},
\]

\[
\boxed{\text{formal expression}\neq\text{self-adjoint operator}},
\]

\[
\boxed{\text{self-adjointness}\not\Rightarrow\text{compact resolvent}},
\]

\[
\boxed{\text{bounded similarity}\neq\text{unitary equivalence}},
\]

\[
\boxed{\{E_n\}\not\Rightarrow\text{complete model identification}},
\]

\[
\boxed{\text{small coefficient change}\not\Rightarrow\text{spectral stability without a topology}},
\]

and

\[
\boxed{\text{stable eigenvalues}\not\Rightarrow\text{stable eigenvectors / DNA labels}.}
\]

## Current phase

The PHISICA operator migration block is closed. The next Volume III question is informational rather than existential:

> Which spectral/operator representation preserves enough distinctions for the declared task?

Current execution graph:

\[
\boxed{
\mathrm{V1\ PASS}
\to
\mathrm{V2\ GLOBAL\ PASS}
\to
\mathrm{PHISICA\ III.1:III.6\ GLOBAL\ PASS}
\to
\mathrm{III.7\ MOST\ NEXT}
\to
\mathrm{III.8\ HCUBE}.
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
