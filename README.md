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

The current primitive-pressure sequence is closed. CAT/FACT, CLOSED-FRAME, LAZARUS-AGENCY and HIGHER-FIBRE did not force a sixth semantic role. `R4-PRESSURE-COURT-01` therefore keeps CORE5 frozen until a genuinely new typed counterexample survives the role-preservation and minimality gates.

This is not a universal completeness theorem.

## First hardening cycle

The first post-R4 hardening cycle contains three independent regressions.

### HCube — operator representation

Equal characteristic polynomial and equal operator norm need not preserve resolvent behaviour. The fixed pair in `HCUBE-REGRESSION-01` therefore falsifies spectrum-plus-norm sufficiency for the declared resolvent-sensitive task.

HCube remains a derived separator/benchmark, not a CORE primitive.

### Go — memory/history representation

For a history representation

\[
\rho_t:\mathcal H_t\to R_t,
\]

exact task adequacy is

\[
\boxed{
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
}
\]

The recovered no-ko/simple-ko/PSK/SSK ladder gives successive exact counterexamples to memories that are too coarse for the rule/task contract.

The canonical quotient

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}
\]

is the coarsest exact quotient in quotient order, not necessarily the smallest implementation in bits, dimension or computation.

### FS-STAT — exact versus stable/statistical identification

The exact Frenet/Bishop MINI result does not automatically survive sampled noisy observations.

For bounded sample error, explicit centered stencils give derivative-error terms of the form

\[
O(h^2)+O(\delta h^{-r}),
\]

with increasing noise amplification at derivative order `r=1,2,3`.

The fixed low-curvature family

\[
\gamma_{\varepsilon,\omega}(s)
=
(s,\varepsilon\cos\omega s,\varepsilon\sin\omega s)
\]

satisfies

\[
\kappa_{\varepsilon,\omega}
=
\frac{\varepsilon\omega^2}{1+\varepsilon^2\omega^2},
\qquad
\tau_{\varepsilon,\omega}
=
\frac{\omega}{1+\varepsilon^2\omega^2}.
\]

As `ε→0`, the curves converge in `C^3` to a line and `κ→0`, while `τ→ω`. Thus Frenet torsion has no continuous extension through the zero-curvature straight-line stratum and cannot be uniformly stably recovered across that boundary.

The permanent inference distinction is

\[
\boxed{
\mathrm{ID}_{exact}
\mid
\mathrm{ID}_{stable}
\mid
\mathrm{CONF}_{1-\alpha}.
}
\]

Confidence claims require an explicit probability model. The Frenet/Bishop switch must be uncertainty- and task-driven rather than based on a universal curvature threshold.

## Regression Bank 01

The three hardening runs are frozen as

\[
\boxed{
R01=\mathrm{HCube},
\qquad
R02=\mathrm{Go},
\qquad
R03=\mathrm{FS\!-\!STAT}.
}
\]

Their common invariant is:

\[
\boxed{
\text{a representation is legal only if it preserves every distinction required by the task}.}
\]

The bank is mandatory regression material for later theorem promotion, redaction and model handoff.

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

The pressure phase, R4 court and first hardening cycle did not reveal a missing control primitive.

Decision and epistemic phase changes are now recorded in `docs/psi-ledger-01.md`; ordinary derivations are intentionally not logged.

No Agent v03 is justified by the current evidence.

## Status

**Research / work in progress.**

The primitive-pressure phase and first hardening cycle are closed.

Current primary work is now:

\[
\boxed{
\mathrm{Claim\ Registry\ v10}
+
\mathrm{Regression\ Bank\ 01}
\to
\mathrm{Principia\ V1/V2\ unit\ maps}
\to
\mathrm{source/proof/regression\ audit}
\to
\mathrm{first\ V1/V2\ freeze}.
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
