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
- [Current claim registry v08](docs/claim-registry-08.md)
- [Current falsifier registry v07](docs/falsifier-registry-07.md)
- [CAT–FACT–NORM–MINI 01](docs/cat-fact-norm-mini-01.md)
- [CLOSED-FRAME 01](docs/closed-frame-01.md)
- [LAZARUS-AGENCY 01](docs/lazarus-agency-01.md)
- [HIGHER-FIBRE 01](docs/higher-fibre-01.md)
- [R4 PRESSURE COURT 01](docs/r4-pressure-court-01.md)
- [HCUBE REGRESSION 01](docs/hcube-regression-01.md)
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

Historical registries/specs remain for provenance. Current control pointers are claim-registry v08, falsifier-registry v07 and Agent Architecture v02.

## Pressure phase

### CAT–FACT–NORM–MINI

For an exact time-parametrized regular `C^3` interval curve, legal Frenet/Bishop segmentations reduce to one Bishop normal class under the declared gauge. Frenet failure at zero curvature is a representation/domain event, not automatic catalog `birth`.

### CLOSED-FRAME

For a closed curve, normal parallel transport produces a return holonomy

\[
H_\gamma\in SO(2).
\]

A periodic RMF exists iff `H_γ=I`. The global datum is representable through transport/task roles; no sixth primitive is required.

### LAZARUS-AGENCY

The exact statement is

\[
F_t(H)=F_t(H')
\not\Rightarrow
H\equiv_{\mathcal T,t}H'.
\]

Equal current world-state fibres can support different executable/future task semantics. This is a representation inadequacy of `rho_F(H)=F_t(H)`, not “same full information, different agency”.

### HIGHER-FIBRE

For

\[
*\to B\mathbb Z_2\leftarrow *,
\]

the coarse strict object-set pullback is one point, while the weak/2-pullback retains two compatibility witnesses. Therefore truncating before fibre construction can lose task-relevant data.

The PSI consequence is a legality condition on representation/gauge reduction:

\[
\boxed{\ker_{eq}q\subseteq E_{\mathcal T}.}
\]

If stabilizers or compatibility witnesses matter for the task, the contract must retain them before coarse truncation.

## R4 PRESSURE COURT

The accepted pressure branches were compared under a non-vacuity rule: CORE5 may not be “saved” by stuffing observed answers, task verdicts or oracle information into the candidate object.

No current witness exhibits an unavoidable task-relevant distinction outside the current semantic roles. Therefore

\[
\boxed{
\mathrm{R4\ PRESSURE\ COURT\ 01}
=
\mathrm{NO\ R4\ WITNESS}.
}
\]

and

\[
\boxed{\mathrm{CORE5\ remains\ frozen}.}
\]

This is **not** a universal completeness theorem. R4 may reopen only after a genuinely new typed counterexample survives the role-preservation and minimality gates.

## Hardening phase — HCube regression

The first post-R4 hardening benchmark uses

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=\begin{pmatrix}2&0&0\\0&1&1\\0&0&0\end{pmatrix}.
\]

They have the same characteristic polynomial and the same Euclidean operator norm:

\[
\chi_A=\chi_B,
\qquad
\|A\|_2=\|B\|_2=2.
\]

But at `z=1/2`:

\[
\left\|\left(\tfrac12I-A\right)^{-1}\right\|_2=2,
\]

while

\[
\left\|\left(\tfrac12I-B\right)^{-1}\right\|_2=2(1+\sqrt2).
\]

Therefore the coarse representation

\[
\rho_0(X)=(\chi_X,\|X\|_2)
\]

fails the PSI adequacy condition for this resolvent-sensitive task:

\[
\boxed{
\ker\rho_0\not\subseteq\ker R_{1/2}.
}
\]

The HCube bridge also separates the pair through

\[
\|e^{t\operatorname{ad}_X}\|_{HS}=\kappa_2(e^{tX}),
\]

but this does not promote HCube to a necessary/minimal/universal representation. HCube remains a derived diagnostic and benchmark.

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

The architecture survived the pressure sequence, the R4 court and the first hardening regression without requiring a new governance primitive.

No Agent v03 is justified by the current evidence.

## Status

**Research / work in progress.**

The primitive-pressure phase is closed. Current work is regression strengthening and Principia redaction:

\[
\boxed{
\mathrm{HCube\ DONE}
\to
\mathrm{Go}
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
