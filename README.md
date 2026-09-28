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

A conclusion is justified only when the available observation collapses task-relevant ambiguity far enough.

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
- [Current claim registry v04](docs/claim-registry-04.md)
- [Current falsifier registry v03](docs/falsifier-registry-03.md)
- [CAT–FACT–NORM–MINI 01](docs/cat-fact-norm-mini-01.md)
- [CLOSED-FRAME 01](docs/closed-frame-01.md)
- [Current PSI Agent Architecture v02](docs/agent-psi-architecture-02.md)
- [Historical dual-operator discipline v01](docs/agent-psi-dual-operator-01.md)
- [Sector work map](docs/work-map-01.md)
- [Principia migration registry](docs/principia-migration-01.md)
- [Principia four-volume skeleton](docs/principia-volume-skeleton-01.md)
- [Source governance discipline](docs/source-governance-01.md)
- [Classical comparison map](docs/classical-compare-01.md)
- [Mathematical lineage — people, problems, ideas](docs/lineage.md)
- [Method and working discipline](docs/method.md)
- [Model-to-model handoff discipline](docs/llm-handoff.md)
- [Minimal separating-test example](examples/separating-test.md)
- [Experimental PSI–Jev adapter](docs/jev-adapter.md)
- [Experimental and conformance runs](experiments/README.md)
- [Publications and archived research objects](docs/publications.md)
- Public project page: https://omni-artificial-intelligence-lab-sc4ilj.v2.appdeploy.ai/
- Public lineage page: https://omni-artificial-intelligence-lab-sc4ilj.v2.appdeploy.ai/?view=lineage

Historical registries and agent specs remain in the repository for provenance. Current control pointers are claim-registry v04, falsifier-registry v03 and Agent Architecture v02.

## Mathematical lineage

PSI is not presented as mathematics without ancestors.

For each substantial imported construction, the public project should state:

\[
\boxed{
\text{person}
\to
\text{problem}
\to
\text{contribution}
\to
\text{role in PSI}
}
\]

A classical result remains classical when PSI uses it. Public provenance keeps claim status and role in PSI as separate metadata axes.

## First full agent-cycle mathematical run

`CAT–FACT–NORM–MINI-01` is the first result carried through exploration, semantic/source audit, mathematical audit, falsification and freeze.

For an exact, time-parametrized `C^3` regular curve on `[0,T]`, finite legal Frenet/Bishop segmentations reduce to one Bishop normal class modulo constant normal-plane rotation. The raw compatible realization family has one factorization class after the declared Euclidean and normal-frame gauge.

The current notation explicitly distinguishes

\[
\operatorname{RawFact}
\quad\text{from}\quad
\operatorname{Fact}=\operatorname{RawFact}/G,
\]

so the realization gauge is not applied twice.

Within that contract, loss of the Frenet frame at zero curvature is a representation/domain event rather than evidence for catalog `birth`.

## First Agent-v02 pressure run: CLOSED-FRAME

`CLOSED-FRAME-01` tests the interval result against a genuinely global obstruction.

For a closed curve, normal parallel transport produces a return map

\[
H_\gamma\in SO(2).
\]

A periodic Bishop / rotation-minimizing frame exists iff

\[
H_\gamma=I.
\]

On the positive-curvature periodic-Frenet domain this return rotation is the classical total-torsion angle modulo `2π` (up to sign convention).

The PSI pressure result is negative for R4: the holonomy is representable as a transport-derived task observable, and periodicity is a typed compatibility/task condition. Thus

\[
\boxed{\mathrm{CLOSED\!-\!FRAME\!-01}\text{ does not trigger a new CORE primitive}.}
\]

The important distinction is

\[
\boxed{\text{local frame trivialization}\neq\text{global periodic trivialization}.}
\]

This result does not prejudge higher-fibre or Lazarus-agency pressure tests.

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

The architecture has now survived two mathematical runs without requiring a new governance primitive: CAT–FACT–NORM–MINI and CLOSED-FRAME.

## What PSI is for

PSI is meant for situations where several underlying realities can produce the same visible data. Typical questions are:

- when an observation identifies one object and when it identifies only a class;
- which additional test actually separates competing hypotheses;
- when a representation is sufficient for a task;
- how to keep an AI agent from silently replacing missing evidence with reconstruction;
- how provenance, state, assumptions and counterexamples should constrain later conclusions.

The framework is developed through mathematics, counterexamples and stress tests across technical diagnosis, open systems, games, information hierarchies, historical analysis and cultural research.

## Status

**Research / work in progress.**

The mathematical core is under active consolidation. Classical imports, adaptations, open problems and PSI-specific claims are separated explicitly; substantial claims are paired with proof/falsification scope before freeze.

Historical Principia material is migrated claim-by-claim against the pinned CANON-03 rather than edited forward as one undifferentiated text.

The remaining independent core-pressure branches before the explicit R4 court are

\[
\boxed{
\mathrm{HIGHER\ FIBRE}
\parallel
\mathrm{LAZARUS\ AGENCY}.
}
\]

`CLOSED-FRAME` is now a frozen bridge/benchmark regression, not an open branch.

## Publications / Zenodo

Archived project materials are available on Zenodo:

- DOI: [10.5281/zenodo.18893354](https://doi.org/10.5281/zenodo.18893354)
- DOI: [10.5281/zenodo.18644750](https://doi.org/10.5281/zenodo.18644750)
- DOI: [10.5281/zenodo.18498472](https://doi.org/10.5281/zenodo.18498472)
- DOI: [10.5281/zenodo.18498440](https://doi.org/10.5281/zenodo.18498440)

See [docs/publications.md](docs/publications.md) for the release index.

## Language

The internal theoretical development is primarily in Polish. Public interoperability, software-facing material and international documentation are written in English. The two language layers carry the same formal content but are not required to be literal translations.

Important material intended for reuse between models follows the [model-to-model handoff discipline](docs/llm-handoff.md): facts, claims, inferences, uncertainty and next actions should retain their status when transferred to another model.

## License

MIT. See [LICENSE](LICENSE).
