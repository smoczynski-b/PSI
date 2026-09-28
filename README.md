# PSI

**PSI is a formal research program on justified inference under constrained observation.**

It asks a strict question:

> What are we entitled to conclude from what we can actually observe?

The central object is not a guessed hidden state, but the full set of states still compatible with the observation.

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

For a task \(\mathcal T\), the current exact task-level criterion is

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)\times F(Y)\subset E_{\mathcal T}.
\]

This repository is a **public entry point** to the PSI project. It is intentionally smaller and more stable than the internal working corpus.

## Start here

- [Core mathematical skeleton](docs/core.md)
- [Current claim registry v11](docs/claim-registry-11.md)
- [Current falsifier registry v10](docs/falsifier-registry-10.md)
- [Proof / Source / Migration Audit 01](docs/proof-source-migration-audit-01.md)
- [CAT / ADEQ / FACT Migration 01](docs/cat-fact-migration-01.md)
- [Regression Bank 01](docs/regression-bank-01.md)
- [Decision / Epistemic Ledger 01](docs/psi-ledger-01.md)
- [Principia V1 Unit Map 01](docs/principia-v1-unit-map-01.md)
- [Principia V2 Theorem Map 01](docs/principia-v2-theorem-map-01.md)
- [CAT–FACT–NORM–MINI 01 — corrected contract](docs/cat-fact-norm-mini-01.md)
- [CLOSED-FRAME 01](docs/closed-frame-01.md)
- [LAZARUS-AGENCY 01](docs/lazarus-agency-01.md)
- [HIGHER-FIBRE 01](docs/higher-fibre-01.md)
- [R4 PRESSURE COURT 01](docs/r4-pressure-court-01.md)
- [HCUBE REGRESSION 01](docs/hcube-regression-01.md)
- [GO MEMORY REGRESSION 01](docs/go-memory-regression-01.md)
- [FS-STAT 01](docs/fs-stat-01.md)
- [Current PSI Agent Architecture v02](docs/agent-psi-architecture-02.md)
- [Sector work map](docs/work-map-01.md)
- [Principia migration registry](docs/principia-migration-01.md)
- [Current Principia four-volume skeleton v02](docs/principia-volume-skeleton-02.md)
- [Source governance discipline](docs/source-governance-01.md)
- [Classical comparison map](docs/classical-compare-01.md)
- [Mathematical lineage](docs/lineage.md)

Historical registries/specs remain for provenance. Current control pointers are **claim-registry v11**, **falsifier-registry v10**, **Regression Bank 01**, **Agent Architecture v02**, and **Proof/Source/Migration Audit 01**.

## Core status

The primitive-pressure sequence is closed. CAT/FACT, CLOSED-FRAME, LAZARUS-AGENCY and HIGHER-FIBRE did not force a sixth semantic role. `R4-PRESSURE-COURT-01` keeps CORE5 frozen until a genuinely new typed counterexample survives the role-preservation and minimality gates.

This is not a universal completeness theorem.

Exact representation adequacy is

\[
\boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}.}
\]

The proof audit sharpened its scope:

\[
\boxed{
\text{task-adequate reduction}
\neq
\text{fully contract-legal reduction}
}
\]

in general. Full legality can additionally require correct typing, admissible gauge/action, observation compatibility/equivariance and domain constraints.

## Proof/source/migration audit

`PROOF-SOURCE-MIGRATION-AUDIT-01` gives the first formal freeze-gate result.

### Passed elementary spine

- C06 exact task-level decidability — `PASS`;
- C07 kernel factorization — `PASS`;
- C08 global task sufficiency — `PASS`;
- C09 exact representation adequacy — `PASS WITH SCOPE CORRECTION`;
- C10 deterministic quotient dynamics — `PASS`.

### History quotient

The RED-1 future-task construction has been migrated to C57–C59:

\[
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H')
\]

through a rooted label-preserving future-tree isomorphism. Its equivalence, congruence and partial recursive-update results are now registered.

### MINI contract errata

The audit found a real defect in the earlier MINI statement. Exact fixed-coordinate observation

\[
Y=\gamma(t)
\]

was combined with an external `SE(3)` quotient, although a nontrivial Euclidean motion generally changes that observation.

The corrected result now distinguishes:

\[
P_0^{abs}:\quad Y=\gamma(t),
\]

with only constant Bishop-normal `SO(2)` quotient in the same observation fibre, from

\[
P_0^{shape}:\quad Y=[\gamma]_{SE(3)},
\]

where external `SE(3)` gauge is legal.

C19 has therefore been replaced by **C19-v2** without changing CORE5.

## CAT / ADEQ / FACT migration

Strong older typed sources have been aligned with the current public CANON-03 derivative. They contain:

- protocol-relative catalog adequacy;
- `GEN ≠ TEST ≠ SELECT`;
- gauge as realization isomorphism rather than catalog change;
- typed CAT layers `ISO/HOR/REF/CRS`;
- `PSI-FACT = PSI-CAT|_{FactMorph}`;
- a factorization groupoid and weak/homotopy ADEQ fibre preserving stabilizers and compatibility witnesses.

The semantic roles align with the current public core. However the physical authoritative `PSI-R3-CONSOLIDATED-CANON-03` source has not yet been bound in this audit, so the migration remains **ALIGNMENT / REVIEW**, not canonical freeze.

## Classical comparison

The comparison map now binds the main imported sources and keeps their role separate from PSI claims:

- Kemeny–Snell — Markov lumpability;
- Larsen–Skou — probabilistic bisimulation;
- Myhill / Nerode — future-continuation equivalence and automata theorem provenance;
- Paige–Tarjan — partition refinement benchmark;
- Newman — termination + local confluence ⇒ confluence;
- Bishop / later RMF literature — framing and closed-loop geometry.

## Hardening bank

The first post-R4 hardening cycle remains

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

## Principia freeze status

The V1/V2 maps and Audit 01 are complete, but the first volume freeze is still deliberately blocked.

Current remaining gate:

\[
\boxed{\mathrm{CANON03\!-\!SOURCE\!-\!BIND\!-\!01}.}
\]

After that bind, the next legal step is

\[
\boxed{\mathrm{V1\!-\!V2\!-\!FREEZE\!-\!RECHECK\!-\!01}.}
\]

Only after a PASS should polished chapter prose begin.

## PSI Agent Architecture v02

The audit is a substantive Agent-v02 regression: the procedure found and corrected a genuine contract error in an already accepted bridge result instead of defending it narratively.

No Agent v03 is justified by the current evidence.

## Status

**Research / work in progress.**

Primitive growth remains stopped until a new counterexample forces a genuinely new semantic role.

## Publications / Zenodo

Archived project materials are available on Zenodo:

- DOI: 10.5281/zenodo.18893354
- DOI: 10.5281/zenodo.18644750
- DOI: 10.5281/zenodo.18498472
- DOI: 10.5281/zenodo.18498440

## Language

The internal theoretical development is primarily in Polish. Public interoperability and repository-facing material are written in English.

## License

MIT. See [LICENSE](LICENSE).
