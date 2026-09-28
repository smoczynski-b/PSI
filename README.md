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
- [Current claim registry v03](docs/claim-registry-03.md)
- [Current falsifier registry v02](docs/falsifier-registry-02.md)
- [CAT–FACT–NORM–MINI 01](docs/cat-fact-norm-mini-01.md)
- [PSI agent dual-operator discipline](docs/agent-psi-dual-operator-01.md)
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

Historical registries remain in the repository for provenance; v03/v02 are the current public claim/falsifier layers.

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

A classical result remains classical when PSI uses it. Public provenance keeps two independent metadata axes.

**Claim status:**

- `CLASSICAL` — established mathematics;
- `BRIDGE` — a claimed connection requiring proof or testing;
- `PSI-NEW` — a genuinely new result requiring proof or a precise formal falsifier;
- `POLICY` — an operational rule rather than a theorem;
- `OPEN` — an unresolved mathematical point.

**Role in PSI:**

- `ADAPTED` — inherited mathematics used in a different task or architectural role;
- `GENEALOGICAL` — conceptual or mathematical ancestry;
- `BENCHMARK` — a classical reference against which a PSI construction must be compared.

The two axes must not be collapsed.

## First dual-operator mathematical run

`CAT–FACT–NORM–MINI-01` is the first result carried through

\[
\mathsf E\to\mathsf A\to\mathsf E_{\rm fals}\to\mathsf A_{\rm freeze}.
\]

Under an exact, time-parametrized `C^3` regular curve on an interval, finite legal Frenet/Bishop segmentations reduce to one Bishop factorization class modulo `SE(3)×SO(2)`. In that specific contract, loss of the Frenet frame at zero curvature is a representation/domain event rather than evidence for catalog `birth`.

The result is deliberately narrow: closed-loop holonomy, reparameterization gauge and sampled/noisy stability remain open gates.

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

The next core-pressure packet is parallel rather than linear:

\[
\mathrm{CLOSED\!-\!FRAME/FRAME}
\parallel
\mathrm{HIGHER\ FIBRE}
\parallel
\mathrm{LAZARUS\ AGENCY},
\]

followed by an explicit R4 pressure test.

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
