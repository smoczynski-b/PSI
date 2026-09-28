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
- [Current claim registry v05](docs/claim-registry-05.md)
- [Current falsifier registry v04](docs/falsifier-registry-04.md)
- [CAT–FACT–NORM–MINI 01](docs/cat-fact-norm-mini-01.md)
- [CLOSED-FRAME 01](docs/closed-frame-01.md)
- [LAZARUS-AGENCY 01](docs/lazarus-agency-01.md)
- [Current PSI Agent Architecture v02](docs/agent-psi-architecture-02.md)
- [Historical dual-operator discipline v01](docs/agent-psi-dual-operator-01.md)
- [Sector work map](docs/work-map-01.md)
- [Principia migration registry](docs/principia-migration-01.md)
- [Principia four-volume skeleton](docs/principia-volume-skeleton-01.md)
- [Source governance discipline](docs/source-governance-01.md)
- [Classical comparison map](docs/classical-compare-01.md)
- [Mathematical lineage](docs/lineage.md)
- [Method and working discipline](docs/method.md)
- [Model-to-model handoff discipline](docs/llm-handoff.md)
- [Experimental PSI–Jev adapter](docs/jev-adapter.md)
- [Experimental and conformance runs](experiments/README.md)
- [Publications and archived research objects](docs/publications.md)
- Public project page: https://omni-artificial-intelligence-lab-sc4ilj.v2.appdeploy.ai/

Historical registries remain for provenance. Current control pointers are claim-registry v05, falsifier-registry v04 and Agent Architecture v02.

## Mathematical lineage

PSI is not presented as mathematics without ancestors. Classical results remain classical when placed inside PSI notation; claim status and role in PSI are separate metadata axes.

## Pressure results already completed

### CAT–FACT–NORM–MINI

For an exact time-parametrized regular `C^3` interval curve, legal Frenet/Bishop segmentations reduce to one Bishop normal class under the declared gauge. The result is a narrow bridge built from classical differential geometry, not a novelty claim for Bishop/Frenet theory.

### CLOSED-FRAME

For a closed curve, normal parallel transport produces a return holonomy

\[
H_\gamma\in SO(2).
\]

A periodic RMF exists iff `H_γ=I`. The PSI result is the typed reduction of this classical global datum into candidate/transport/task/compatibility roles. No sixth CORE primitive is required.

### LAZARUS-AGENCY

The historical slogan “same information, different agency” is corrected to the typed statement

\[
\boxed{
F_t(H)=F_t(H')
\not\Rightarrow
H\equiv_{\mathcal T,t}H'.
}
\]

Equal **current world-state fibres** can support different executable/future task semantics when history or operational composition differs. For

\[
\rho_F(H)=F_t(H),
\]

this is exactly the representation failure

\[
\ker_{eq}\rho_F
\not\subseteq
\equiv_{\mathcal T,t}.
\]

The repair is a task-sufficient history/joint-state representation; agency does not require a new CORE primitive. D3 adds the related warning that separate world-state and operational marginals can lose their task-relevant correlation.

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

State is separated into

\[
\mathrm{CANON}\mid\mathrm{SPEC}\mid\mathrm{WORKING}\mid\mathrm{LIVE}\mid\mathrm{FRONTIER}\mid\mathrm{HISTORY}.
\]

The architecture has now survived three substantive mathematical/pressure runs without requiring a new governance primitive: CAT–FACT–NORM–MINI, CLOSED-FRAME and LAZARUS-AGENCY.

## Status

**Research / work in progress.**

CORE5 remains frozen. After the three completed pressure runs, one independent branch remains before the explicit R4 court:

\[
\boxed{
\mathrm{HIGHER\ FIBRE}
\to
\mathrm{R4\ PRESSURE\ COURT}.
}
\]

Historical Principia material continues to be migrated claim-by-claim against the pinned CANON-03 rather than edited forward as one undifferentiated text.

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
