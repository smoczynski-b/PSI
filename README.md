# PSI

**PSI is a formal research program on justified inference under constrained observation.**

It asks:

> What are we entitled to conclude from what we can actually observe?

The central object is not a guessed hidden state, but the full set of candidates still compatible with the observation:

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

For a task \(\mathcal T\), exact resolution means

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)\times F(Y)\subseteq E_{\mathcal T}.
\]

## Current control pointers

- [Physical CANON-03 source bind](docs/canon03-source-bind-01.md)
- [Core mathematical skeleton](docs/core.md)
- [Current claim registry v12](docs/claim-registry-12.md)
- [Current falsifier registry v10](docs/falsifier-registry-10.md)
- [Principia V1/V2 First Freeze 01](docs/principia-v1-v2-freeze-01.md)
- [Principia V1 I.1 — Contract and semantic roles](docs/principia-v1-01-contract-semantic-roles.md)
- [Principia V1 I.2 — Observation, compatible fibre and catalog adequacy](docs/principia-v1-02-observation-fibre-catalog-adequacy.md)
- [Principia V1 I.3 — Task-relative distinction and legal reduction](docs/principia-v1-03-task-distinction-legal-reduction.md)
- [Principia V1 I.4 — History, memory and future-task semantics](docs/principia-v1-04-history-memory-future-semantics.md)
- [Principia V1 I.5 — Exact identification, stability and statistical licensing](docs/principia-v1-05-exact-stable-statistical-licensing.md)
- [Principia V1 I.6 — Methodological boundaries](docs/principia-v1-06-methodological-boundaries.md)
- [Whole-V1 Cross-Check 01](docs/principia-v1-whole-crosscheck-01.md)
- [V1 Normalization 01](docs/principia-v1-normalization-01.md)
- [Principia V2.1 — Exact task-level decidability](docs/principia-v2-01-exact-task-decidability.md)
- [Principia V2.2 — Kernel factorization criterion](docs/principia-v2-02-kernel-factorization.md)
- [Principia V2.3 — Global observer sufficiency](docs/principia-v2-03-global-observer-sufficiency.md)
- [Principia V2.4 — Representation adequacy](docs/principia-v2-04-representation-adequacy.md)
- [Principia V2.5 — Task-information legality of reduction/quotient](docs/principia-v2-05-task-information-legality-of-reduction.md)
- [Principia V2.6 — Deterministic quotient dynamics](docs/principia-v2-06-deterministic-quotient-dynamics.md)
- [Principia V2.7 — Exact history-memory adequacy](docs/principia-v2-07-exact-history-memory-adequacy.md)
- [Principia V2.8 — Coarsest exact history quotient](docs/principia-v2-08-coarsest-exact-history-quotient.md)
- [Principia V2.9 — Recursive history quotient update](docs/principia-v2-09-recursive-history-quotient-update.md)
- [Principia V2 Spine Cross-Check 01 — early II.1–II.4 audit](docs/principia-v2-spine-crosscheck-01.md)
- [Principia V2 Own-Layer Cross-Check 02 — independent II.1–II.9 handoff audit](docs/principia-v2-own-layer-crosscheck-02.md)
- [Current Principia V2 Theorem Map 02](docs/principia-v2-theorem-map-02.md)
- [Historical Principia V2 Theorem Map 01](docs/principia-v2-theorem-map-01.md)
- [Proof / Source / Migration Audit 01](docs/proof-source-migration-audit-01.md)
- [CAT / ADEQ / FACT Migration 01](docs/cat-fact-migration-01.md)
- [Classical comparison map](docs/classical-compare-01.md)
- [Regression Bank 01](docs/regression-bank-01.md)
- [Decision / Epistemic Ledger 01](docs/psi-ledger-01.md)
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

## Core status

CORE5 remains

\[
\boxed{
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
}
\]

The current counterexample set does not force R4. This is not a universal completeness theorem.

Exact task-information adequacy:

\[
\boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}.}
\]

History/memory specialization:

\[
\boxed{\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.}
\]

Scope discipline:

\[
\boxed{
\text{task-adequate reduction}
\neq
\text{fully contract-legal reduction}
}
\]

in general.

Inference discipline:

\[
\boxed{
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
}
\]

## Principia V1/V2 freeze

\[
\boxed{
\mathrm{PRINCIPIA\ V1/V2\ FIRST\ FREEZE}=\mathrm{PASS}.
}
\]

It freezes definitions, theorem statements/hypotheses, source status, dependencies, principal boundaries and regression obligations. It does not freeze final wording or typography.

## Volume I status

\[
\boxed{
\mathrm{PRINCIPIA\ V1\ FIRST\ PROSE\ PASS}
=
\mathrm{NORMALIZED\ PASS}.
}
\]

No Freeze 01 erratum was required.

## Volume II own theorem layer

The exact quotient/history layer contains:

\[
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)^2\subseteq E_{\mathcal T,c},
\]

\[
\ker_{eq}\rho\subseteq\ker_{eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,
\quad R=g\circ\rho,
\]

\[
\ker_{eq}\rho\subseteq E_{\mathcal T,c},
\qquad
\ker_{eq}q\subseteq E_{\mathcal T,c},
\]

and deterministic quotient dynamics under

\[
xEy\Longrightarrow\delta(x)E\delta(y).
\]

For histories:

\[
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H'),
\]

\[
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t},
\qquad
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t},
\]

and on the typed legal quotient domain

\[
U_{\mathcal T,t}([H],\varepsilon,y)
=
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}.
\]

### Independent handoff verdict

After the post-history independent Agent audit:

\[
\boxed{
\mathrm{V2.1:V2.9\ OWN\ LAYER}
=
\mathrm{GLOBAL\ CROSSCHECK\ PASS}.
}
\]

The audit found no mathematical contradiction and no Freeze 01 erratum. It did require control corrections:

- the II.9 dependency graph was narrowed: strict proof dependency is `II.7 + C59`; II.6 is structural analogy and II.8 is not a proof prerequisite;
- the classical comparison map was updated from Claim Registry v11 to v12;
- probabilistic bisimulation is now explicitly comparison-only with no current C-ID required;
- the Decision/Epistemic Ledger now records V1 normalization, V2 own-layer completion and the independent handoff gate.

Permanent Agent-process lesson:

\[
\boxed{
\text{sequence of local PASSes}
\not\Rightarrow
\text{whole-layer PASS}.
}
\]

This uses existing Agent v02 `IMPACT/HANDOFF` controls; it does not justify Agent v03.

## Classical bridges — released

The next bridge layer starts with strong Markov lumpability. The critical scope lock is:

\[
\boxed{
E_{\mathcal T}
\not\Rightarrow
\text{stochastic lumpability}
}
\]

without the classical block-transition stability condition.

Next: Myhill–Nerode, then Paige–Tarjan strictly as an algorithmic benchmark.

## Hardening bank

\[
\boxed{
R01=\mathrm{HCube},\qquad
R02=\mathrm{Go},\qquad
R03=\mathrm{FS\!-STAT}.
}
\]

These remain regression/boundary witnesses, not theorem substitutes.

## PSI Agent Architecture v02

Agent v02 remains current. The handoff audit found execution drift, not a missing control primitive.

No Agent v03 is justified by current evidence.

## Current phase

\[
\boxed{
\mathrm{V1\ NORMALIZED\ PASS}
\to
\mathrm{V2.1:V2.9\ GLOBAL\ PASS}
\to
\mathrm{CLASSICAL\ BRIDGES}
\to
\mathrm{CAT/FACT/FRAME/HIGHER}
\to
\mathrm{V2\ WHOLE\ CROSSCHECK}.
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
