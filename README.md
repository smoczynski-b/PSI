# PSI

**PSI is a theory of justified inference under constrained observation.**

It asks a strict question:

> What are we entitled to conclude from what we can actually observe?

The central object is not a guessed hidden state, but the full set of states still compatible with the observation.

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

Inference proceeds in a fixed order:

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

A conclusion is justified only when the available observation collapses the task-relevant ambiguity far enough.

For a task \(\mathcal T\), exact decidability is expressed by

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
- [Method and working discipline](docs/method.md)
- [Model-to-model handoff discipline](docs/llm-handoff.md)
- [Minimal separating-test example](examples/separating-test.md)
- [Experimental PSI–Jev adapter](docs/jev-adapter.md)
- [Controlled experiments and falsification runs](experiments/README.md)
- [Publications and archived research objects](docs/publications.md)
- Public project page: https://omni-artificial-intelligence-lab-sc4ilj.v2.appdeploy.ai/

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

The mathematical core is under active consolidation. Later public releases will separate stable canonical statements from genealogy, examples and experimental modules.

## Publications / Zenodo

Archived project materials are available on Zenodo:

- DOI: [10.5281/zenodo.18893354](https://doi.org/10.5281/zenodo.18893354)
- DOI: [10.5281/zenodo.18644750](https://doi.org/10.5281/zenodo.18644750)
- DOI: [10.5281/zenodo.18498472](https://doi.org/10.5281/zenodo.18498472)
- DOI: [10.5281/zenodo.18498440](https://doi.org/10.5281/zenodo.18498440)

See [docs/publications.md](docs/publications.md) for the release index.

When a Zenodo record and a repository version refer to the same work, cite the Zenodo record as the archival publication and this repository as the evolving public source.

## Language

The internal theoretical development is primarily in Polish. Public interoperability, software-facing material and international documentation are written in English. The two language layers carry the same formal content but are not required to be literal translations.

Important material intended for reuse between models follows the [model-to-model handoff discipline](docs/llm-handoff.md): facts, claims, inferences, uncertainty and next actions should retain their status when transferred to another model.

## License

MIT. See [LICENSE](LICENSE).
