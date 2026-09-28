# PSI

**PSI is a formal research program on justified inference under constrained observation.**

It asks a strict question:

> What are we entitled to conclude from what we can actually observe?

The central object is not a guessed hidden state, but the full set of states still compatible with the observation.

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

For a task \(\mathcal T\), exact resolution means

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

The current authoritative physical canon is bound to:

- repository `smoczynski-b/psi-model`;
- commit `7e64ec8ad766623ffeede3daa4bb68dee15135c1`;
- path `psi-agent/canon/PSI-R3-CONSOLIDATED-CANON-03.md`;
- version `1.0.0`;
- blob `72d711a40c65376ee932809802622f3985ecb02a`.

This closes the current-canon provenance gap. Historical missing originals remain genealogy gaps only.

## Core status

CORE5 remains

\[
\boxed{\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).}
\]

The current counterexample set does not force R4. This is not a universal completeness theorem.

Exact task-information adequacy is

\[
\boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}.}
\]

The proof audit sharpened the scope:

\[
\boxed{
\text{task-adequate reduction}
\neq
\text{fully contract-legal reduction}
}
\]

in general. Full legality can additionally require correct typing, admissible gauge/action, observation compatibility/equivariance and domain constraints.

## Corrected MINI contract

The first proof/source audit found a genuine error in the earlier Frenet/Bishop MINI statement: fixed-coordinate exact observation had been mixed with an external `SE(3)` quotient.

The corrected theorem distinguishes:

\[
P_0^{abs}:Y=\gamma(t),
\]

with only constant Bishop-normal `SO(2)` presentation quotient in the same observation fibre, from

\[
P_0^{shape}:Y=[\gamma]_{SE(3)},
\]

where external `SE(3)` gauge is legal.

C19-v2 records the repaired result.

## Current CAT / FACT status

Physical CANON-03 defines:

- `PSI-CAT`: whether data/protocol justify a catalog change and which class of changes is justified;
- `PSI-CAT^D`: the same problem under domain-admissibility conditions `ADM_D`;
- `PSI-FACT`: the contract-relative fibre
  \[
  \operatorname{Fact}^{\varepsilon}_{D,P}(Y)
  \]
  of legal factorizations compatible with observation, external interface and domain constraints.

Gauge is quotiented when the contract establishes it.

The richer older CAT taxonomy and FACT groupoid/homotopy fibre are retained as **derived extensions**, not as replacements for the current physical definitions.

A universal scalar `D_ADEQ^cat` is likewise not a CORE primitive; metric/loss-based catalog adequacy is a protocol-specific adapter.

## First Principia freeze

The first mathematical/source freeze for Volumes I and II has passed:

\[
\boxed{
\mathrm{PRINCIPIA\ V1/V2\ FIRST\ FREEZE}=\mathrm{PASS}.
}
\]

It freezes:

- definitions and semantic roles;
- theorem statements and hypotheses;
- source/classical status;
- dependencies and principal boundaries;
- regression obligations.

It does **not** freeze final prose or typography and does not assert universal completeness of CORE5.

The next legal phase is chapter prose **from frozen units**, with semantic changes requiring an explicit erratum and impact audit.

## Hardening bank

The first regression bank remains

\[
\boxed{R01=\mathrm{HCube},\qquad R02=\mathrm{Go},\qquad R03=\mathrm{FS\!-\!STAT}.}
\]

Permanent statistical discipline:

\[
\boxed{
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
}
\]

## PSI Agent Architecture v02

The Agent-v02 procedure found and corrected the MINI contract error, recovered the physical canon instead of filling the gap from memory, and downgraded older rich machinery where the physical canon was narrower.

No Agent v03 is justified by current evidence.

## Current phase

\[
\boxed{
\mathrm{V1\ PROSE}
\to
\mathrm{V1\ CROSS\!-\!CHECK}
\to
\mathrm{V2\ PROSE}
\to
\mathrm{V2\ CROSS\!-\!CHECK}.
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
