# PSI

**PSI is a formal research program on justified inference under constrained observation.**

It asks a strict question:

> What are we entitled to conclude from what we can actually observe?

The central object is not a guessed hidden state, but the full set of states still compatible with the observation.

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

Inference is organized in the intended order

\[
\text{catalog adequacy}
\to
\text{fiber}
\to
\text{local identifiability}
\to
\text{global identifiability}
\to
\text{protocol design}.
\]

For a task \(\mathcal T\), the current exact task-level criterion is

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)^2\subset E_{\mathcal T}.
\]

This repository is a **public entry point** to the PSI project. It is intentionally smaller and more stable than the internal working corpus.

## Start here

- [Core mathematical skeleton](docs/core.md)
- [Current claim registry v10](docs/claim-registry-10.md)
- [Current falsifier registry v09](docs/falsifier-registry-09.md)
- [Regression Bank 01](docs/regression-bank-01.md)
- [Decision / Epistemic Ledger 01](docs/psi-ledger-01.md)
- [Principia V1 Unit Map 01](docs/principia-v1-unit-map-01.md)
- [Principia V2 Theorem Map 01](docs/principia-v2-theorem-map-01.md)
- [CAT–FACT–NORM–MINI 01](docs/cat-fact-norm-mini-01.md)
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
- [Method and working discipline](docs/method.md)
- [Model-to-model handoff discipline](docs/llm-handoff.md)
- [Experimental PSI–Jev adapter](docs/jev-adapter.md)
- [Experimental and conformance runs](experiments/README.md)
- [Publications and archived research objects](docs/publications.md)
- Public project page: https://omni-artificial-intelligence-lab-sc4ilj.v2.appdeploy.ai/

Historical registries/specs remain for provenance. Current control pointers are claim-registry v10, falsifier-registry v09, Regression Bank 01, Agent Architecture v02 and Principia skeleton v02.

## Pressure phase

The primitive-pressure sequence is closed. CAT/FACT, CLOSED-FRAME, LAZARUS-AGENCY and HIGHER-FIBRE did not force a sixth semantic role. `R4-PRESSURE-COURT-01` keeps CORE5 frozen until a genuinely new typed counterexample survives the role-preservation and minimality gates.

This is not a universal completeness theorem.

## First hardening cycle

The first post-R4 hardening cycle contains three independent regressions:

\[
\boxed{R01=\mathrm{HCube},\qquad R02=\mathrm{Go},\qquad R03=\mathrm{FS\!-\!STAT}.}
\]

Their common invariant is:

\[
\boxed{\text{a representation is legal only if it preserves every distinction required by the task}.}
\]

HCube tests operator representation adequacy; Go tests history/memory adequacy; FS-STAT separates exact identifiability from perturbation stability and confidence licensing.

Permanent statistical discipline:

\[
\boxed{
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
}
\]

## Principia redaction

`V1-UNIT-MAP-01` and `V2-THEOREM-MAP-01` are complete. Neither is a volume freeze.

### V1

Volume I is mapped as six structural units with explicit statement class, dependencies, downstream use, regression binding and source status. One major migration gap remains: the older formal catalog-adequacy definition has a recoverable source but no dedicated current claim ID.

### V2

Volume II is now separated into:

1. self-contained quotient/factorization results;
2. classical bridges requiring exact source/hypothesis binding;
3. benchmarks/pressure witnesses that test scope but do not create theorem status.

The elementary spine

\[
C06,C07\to C08,C09\to C32/C37
\]

is structurally ready for proof audit.

Current V2 blockers are explicit:

- history future-task equivalence lacks a dedicated current definition ID;
- probabilistic bisimulation comparison lacks a current C-ID;
- general CAT/FACT definitions are not yet fully migrated into current registered form;
- exact source/hypothesis binding is still needed for imported classical results;
- MINI requires a dedicated proof audit of quotient rewrite, critical pairs and Newman hypotheses.

Therefore:

\[
\boxed{\mathrm{V1\ FREEZE}=\mathrm{NOT\ YET},\qquad
\mathrm{V2\ FREEZE}=\mathrm{NOT\ YET}.}
\]

Current execution order:

\[
\boxed{
\mathrm{V1\ MAP\ DONE}
+
\mathrm{V2\ MAP\ DONE}
\to
\mathrm{PROOF/SOURCE/MIGRATION\ AUDIT}
\to
\mathrm{FIRST\ V1/V2\ FREEZE}
\to
\mathrm{PROSE}.
}
\]

## PSI Agent Architecture v02

The current agent operates through

\[
\boxed{
\mathrm{RESCAN}
\to
\mathrm{ROUTER}
\to
\mathrm{CONTRACT\ SNAPSHOT}
\to
\mathsf E
\to
\mathsf A_0
\to
\mathsf A_1
\to
\mathsf E_{fals}
\to
\mathrm{IMPACT}
\to
\mathrm{DECIDE}
\to
\mathrm{REGRESSION}
\to
\mathrm{HANDOFF}.
}
\]

The V1/V2 mapping phase did not reveal a missing control primitive. Missing sources and missing current claim IDs remain explicit gaps instead of being filled from memory.

Decision and epistemic phase changes are recorded in `docs/psi-ledger-01.md`; ordinary derivations are intentionally not logged.

No Agent v03 is justified by the current evidence.

## Status

**Research / work in progress.**

Primitive growth remains stopped until a new counterexample forces a genuinely new semantic role.

## Publications / Zenodo

Archived project materials are available on Zenodo:

- DOI: [10.5281/zenodo.18893354](https://doi.org/10.5281/zenodo.18893354)
- DOI: [10.5281/zenodo.18644750](https://doi.org/10.5281/zenodo.18644750)
- DOI: [10.5281/zenodo.18498472](https://doi.org/10.5281/zenodo.18498472)
- DOI: [10.5281/zenodo.18498440](https://doi.org/10.5281/zenodo.18498440)

## Language

The internal theoretical development is primarily in Polish. Public interoperability and repository-facing material are written in English. Important material transferred between models follows the model-to-model handoff discipline: facts, claims, inferences, uncertainty and next actions retain their status.

## License

MIT. See [LICENSE](LICENSE).
