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
- [Current claim registry v09](docs/claim-registry-09.md)
- [Current falsifier registry v08](docs/falsifier-registry-08.md)
- [CAT–FACT–NORM–MINI 01](docs/cat-fact-norm-mini-01.md)
- [CLOSED-FRAME 01](docs/closed-frame-01.md)
- [LAZARUS-AGENCY 01](docs/lazarus-agency-01.md)
- [HIGHER-FIBRE 01](docs/higher-fibre-01.md)
- [R4 PRESSURE COURT 01](docs/r4-pressure-court-01.md)
- [HCUBE REGRESSION 01](docs/hcube-regression-01.md)
- [GO MEMORY REGRESSION 01](docs/go-memory-regression-01.md)
- [Current PSI Agent Architecture v02](docs/agent-psi-architecture-02.md)
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

Historical registries/specs remain for provenance. Current control pointers are claim-registry v09, falsifier-registry v08 and Agent Architecture v02.

## Pressure phase

The current primitive-pressure sequence is closed. CAT/FACT, CLOSED-FRAME, LAZARUS-AGENCY and HIGHER-FIBRE did not force a sixth semantic role. `R4-PRESSURE-COURT-01` therefore keeps CORE5 frozen until a genuinely new typed counterexample survives the role-preservation and minimality gates.

This is not a universal completeness theorem.

## Hardening phase — HCube regression

The first hardening benchmark uses

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=\begin{pmatrix}2&0&0\\0&1&1\\0&0&0\end{pmatrix}.
\]

They have the same characteristic polynomial and Euclidean operator norm, but at `z=1/2`:

\[
\left\|\left(\tfrac12I-A\right)^{-1}\right\|_2=2,
\qquad
\left\|\left(\tfrac12I-B\right)^{-1}\right\|_2=2(1+\sqrt2).
\]

Hence the coarse representation

\[
\rho_0(X)=(\chi_X,\|X\|_2)
\]

is insufficient for this resolvent-sensitive task.

HCube remains a derived diagnostic/benchmark, not a CORE primitive.

## Hardening phase — Go memory regression

The Go benchmark tests exact history/memory sufficiency.

For a representation

\[
\rho_t:\mathcal H_t\to R_t,
\]

exact task adequacy is

\[
\boxed{
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
}
\]

The recovered frozen sequence gives:

\[
(B_t,\sigma_t)
\to
(B_t,\sigma_t,B_{t-1})
\to
(B_t,\sigma_t,V_t)
\to
(B_t,\sigma_t,U_t),
\]

where the successive contracts are no-ko, simple ko, positional superko and situational superko.

The progression is not primitive growth. It is a sequence of increasingly adequate representations for different rule/task contracts.

The canonical history quotient

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}
\]

is the **coarsest exact quotient of histories** for the task. This is minimality in quotient order, not minimality of dimension, bits, storage or computation.

When the equivalence is a congruence for update, task classes admit a well-defined mathematical recursive update `U_T,t`; this does not by itself prove finite memory or an efficient algorithm.

### Source boundary

The currently recovered RED-1 artifact explicitly freezes `G0`, `G2`, `G3`, `G4` but does not contain a separate `G1` statement. No `G1` witness or theorem is reconstructed without its actual source.

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

HCube and Go hardening both passed without requiring a new governance primitive. The Go run additionally validated source-gap discipline by refusing to fabricate missing `G1` content.

No Agent v03 is justified by the current evidence.

## Status

**Research / work in progress.**

Current hardening sequence:

\[
\boxed{
\mathrm{HCube\ DONE}
\to
\mathrm{Go\ DONE}
\to
\mathrm{FS\!-\!STAT}
\to
\text{regression bank}
\to
\text{Principia V1/V2 migration/freeze}.
}
\]

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
