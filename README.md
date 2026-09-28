# PSI

**PSI is a formal research program on justified inference under constrained observation.**

It asks:

> What are we entitled to conclude from what we can actually observe?

The central object is not a guessed hidden state but the full compatible fibre

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

For task \(\mathcal T\), exact resolution is

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)\times F(Y)\subset E_{\mathcal T}.
\]

## Current control pointers

- [Physical CANON-03 source bind](docs/canon03-source-bind-01.md)
- [Core mathematical skeleton](docs/core.md)
- [Current claim registry v12](docs/claim-registry-12.md)
- [Current falsifier registry v10](docs/falsifier-registry-10.md)
- [Principia V1/V2 First Freeze 01](docs/principia-v1-v2-freeze-01.md)
- [Whole-V1 Cross-Check 01](docs/principia-v1-whole-crosscheck-01.md)
- [Principia V1 I.1 — Contract and semantic roles](docs/principia-v1-01-contract-semantic-roles.md)
- [Principia V1 I.2 — Observation, compatible fibre and catalog adequacy](docs/principia-v1-02-observation-fibre-catalog-adequacy.md)
- [Principia V1 I.3 — Task-relative distinction and legal reduction](docs/principia-v1-03-task-distinction-legal-reduction.md)
- [Principia V1 I.4 — History, memory and future-task semantics](docs/principia-v1-04-history-memory-future-semantics.md)
- [Principia V1 I.5 — Exact identification, stability and statistical licensing](docs/principia-v1-05-exact-stable-statistical-licensing.md)
- [Principia V1 I.6 — Methodological boundaries and primitive discipline](docs/principia-v1-06-methodological-boundaries.md)
- [Proof / Source / Migration Audit 01](docs/proof-source-migration-audit-01.md)
- [CAT / ADEQ / FACT Migration 01](docs/cat-fact-migration-01.md)
- [Regression Bank 01](docs/regression-bank-01.md)
- [Decision / Epistemic Ledger 01](docs/psi-ledger-01.md)
- [Principia V1 Unit Map 01](docs/principia-v1-unit-map-01.md)
- [Principia V2 Theorem Map 01](docs/principia-v2-theorem-map-01.md)
- [Current Principia four-volume skeleton v02](docs/principia-volume-skeleton-02.md)
- [Corrected CAT–FACT–NORM–MINI 01](docs/cat-fact-norm-mini-01.md)
- [Classical comparison map](docs/classical-compare-01.md)
- [Current PSI Agent Architecture v02](docs/agent-psi-architecture-02.md)
- [Sector work map](docs/work-map-01.md)

Historical registries/specs remain for provenance.

## Physical canon

The authoritative physical canon is bound to:

- repository `smoczynski-b/psi-model`;
- commit `7e64ec8ad766623ffeede3daa4bb68dee15135c1`;
- path `psi-agent/canon/PSI-R3-CONSOLIDATED-CANON-03.md`;
- version `1.0.0`;
- blob `72d711a40c65376ee932809802622f3985ecb02a`.

Historical missing originals remain genealogy gaps only.

## Core status

\[
\boxed{\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).}
\]

The current counterexample set does not force R4; this is not a universal completeness theorem.

Exact task-information adequacy:

\[
\boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}.}
\]

History/memory specialization:

\[
\boxed{\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.}
\]

Task-information adequacy is not, in general, the whole contract-legality test.

## Current CAT / FACT status

Physical CANON-03 defines:

- `PSI-CAT`: whether data/protocol justify catalog change and which class of changes is justified;
- `PSI-CAT^D`: the same question under `ADM_D`;
- `PSI-FACT`: the contract-relative fibre
  \[
  \operatorname{Fact}^{\varepsilon}_{D,P}(Y)
  \]
  of legal factorizations compatible with observation, interface and domain constraints.

Gauge is quotiented only when the contract establishes it. Older rich CAT taxonomies and FACT groupoid/homotopy constructions remain derived extensions. `D_ADEQ^cat` is a typed protocol adapter, not a universal CORE primitive.

## Principia freeze and prose status

The first mathematical/source freeze for Volumes I and II has passed:

\[
\boxed{\mathrm{PRINCIPIA\ V1/V2\ FIRST\ FREEZE}=\mathrm{PASS}.}
\]

The first V1 prose pass contains six locally checked units I.1–I.6.

The whole-volume audit then found no semantic contradiction and no Freeze 01 erratum, but did find seven cross-chapter normalization requirements: protocol-refinement wording, suppressed contract indices in history notation, symbol collisions in I.4/I.5, local typing of laboratory witnesses, formal replacement of chained `!=` shorthand, and reduction of R4 project-history material in I.6.

Therefore:

\[
\boxed{
\mathrm{WHOLE\!-
V1\ CROSS\!-
CHECK\ 01}
=
\mathrm{PASS\ WITH\ REQUIRED\ NORMALIZATION}.
}
\]

The next gate is

\[
\boxed{\mathrm{V1\!-
NORMALIZATION\!-
01}.}
\]

V2 prose does not begin until those nonsemantic corrections are applied and mechanically rechecked.

## Hardening bank

\[
\boxed{R01=\mathrm{HCube},\qquad R02=\mathrm{Go},\qquad R03=\mathrm{FS\!-\!STAT}.}
\]

Permanent inference discipline:

\[
\boxed{
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
}
\]

## PSI Agent Architecture v02

Agent v02 remains current. During redaction it acts as a semantic/type cross-check. The whole-V1 audit found cross-chapter notation and architecture defects without exposing a missing governance primitive; no Agent v03 is justified.

## Current phase

\[
\boxed{
\mathrm{V1\ LOCAL\ PASS}
\to
\mathrm{WHOLE\!-
V1\ CROSS\!-
CHECK}
\to
\mathrm{V1\ NORMALIZATION}
\to
\mathrm{V2\ PROSE}
\to
\mathrm{V2\ CROSS\!-
CHECK}.
}
\]

Primitive growth remains stopped until a new typed counterexample forces a genuinely new semantic role.

## Publications / Zenodo

Archived project materials:

- DOI: 10.5281/zenodo.18893354
- DOI: 10.5281/zenodo.18644750
- DOI: 10.5281/zenodo.18498472
- DOI: 10.5281/zenodo.18498440

## Language

The internal theoretical development is primarily in Polish. Public interoperability and repository-facing material are written in English.

## License

MIT. See [LICENSE](LICENSE).
