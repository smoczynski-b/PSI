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
F(Y)\times F(Y)\subset E_{\mathcal T}.
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
- [Proof / Source / Migration Audit 01](docs/proof-source-migration-audit-01.md)
- [CAT / ADEQ / FACT Migration 01](docs/cat-fact-migration-01.md)
- [Regression Bank 01](docs/regression-bank-01.md)
- [Decision / Epistemic Ledger 01](docs/psi-ledger-01.md)
- [Principia V1 Unit Map 01](docs/principia-v1-unit-map-01.md)
- [Principia V2 Theorem Map 01](docs/principia-v2-theorem-map-01.md)
- [Principia four-volume skeleton v02](docs/principia-volume-skeleton-02.md)
- [Corrected CAT–FACT–NORM–MINI 01](docs/cat-fact-norm-mini-01.md)
- [Classical comparison map](docs/classical-compare-01.md)
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

## Corrected MINI contract

The proof/source audit repaired a genuine observation/gauge mismatch in the earlier Frenet/Bishop MINI theorem.

The corrected result distinguishes

\[
P_0^{abs}:Y=\gamma(t),
\]

with only constant Bishop-normal `SO(2)` presentation quotient in the same observed fibre, from

\[
P_0^{shape}:Y=[\gamma]_{SE(3)},
\]

where external `SE(3)` gauge is legal.

C19-v2 records the repaired result.

## Current CAT / FACT status

Physical CANON-03 defines:

- `PSI-CAT`: whether data/protocol justify a catalog change and which class of change is justified;
- `PSI-CAT^D`: the same problem with domain admissibility `ADM_D`;
- `PSI-FACT`: the contract-relative fibre
  \[
  \operatorname{Fact}^{\varepsilon}_{D,P}(Y)
  \]
  of legal factorizations compatible with observation, external interface and domain constraints.

Gauge is quotiented only when the contract establishes it.

Older richer CAT taxonomies and FACT groupoid/homotopy constructions are derived extensions, not replacements for the current physical definitions. A universal scalar `D_ADEQ^cat` is not a CORE primitive; metric/loss catalog adequacy is a protocol-specific adapter.

## Principia V1/V2 freeze

\[
\boxed{
\mathrm{PRINCIPIA\ V1/V2\ FIRST\ FREEZE}=\mathrm{PASS}.
}
\]

It freezes definitions, theorem statements/hypotheses, source status, dependencies, principal boundaries and regression obligations. It does not freeze final wording or typography.

## Volume I status

The six first-pass foundation units have been written and locally cross-checked. The whole-volume audit then detected seven nonsemantic notation/editorial normalization issues. `V1 NORMALIZATION 01` applied all N1–N7 without changing Freeze 01 semantics.

Therefore:

\[
\boxed{
\mathrm{PRINCIPIA\ V1\ FIRST\ PROSE\ PASS}
=
\mathrm{NORMALIZED\ PASS}.
}
\]

Key normalizations include:

- protocol workflow read as `P0 -> diagnosis -> P1` redesign/refinement;
- explicit suppression of contract index in RED-1 history notation;
- memory codomain `Z_t`, avoiding collision with task quantity `R`;
- local typing of all Go/LAZARUS witness symbols used in V1;
- inference gates `G_EX`, `G_ST`, `G_PR`, avoiding collision with `E_T`;
- removal of untyped chained `!=` shorthand;
- detailed R4 pressure-court genealogy moved out of V1 foundation prose.

No Freeze 01 erratum was required.

## Volume II theorem-spine status

V2.1 has been written, proved and cross-checked:

\[
\boxed{
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)\times F_c(Y)\subseteq E_{\mathcal T,c}.
}
\]

Status:

\[
\boxed{
\mathrm{V2.1}=\mathrm{THEOREM\ PROSE\ PASS\ 01 / PROOF\ PASS / CROSS\!-\!CHECK\ PASS}.
}
\]

The result is explicitly classified as a **classical elementary quotient fact / PSI-adapted central criterion**. The proof uses no finiteness, topology, probability, stability or computability assumptions. The empty-fibre condition is retained as a mandatory theorem boundary.

Next theorem:

\[
\boxed{
\mathrm{V2.2\ —\ kernel\ factorization\ criterion}.
}
\]

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

Agent v02 remains current. It is now used during theorem prose to enforce:

- type/domain discipline;
- scope fidelity to freeze;
- source/classical-status separation;
- theorem versus policy/benchmark separation;
- regression binding.

No Agent v03 is justified by current evidence.

## Current phase

\[
\boxed{
\mathrm{V1\ NORMALIZED\ PASS}
\to
\mathrm{V2.1\ PASS}
\to
\mathrm{V2.2\ KERNEL\ FACTORIZATION}
\to
\mathrm{V2.3\ GLOBAL\ SUFFICIENCY}
\to
\mathrm{V2.4\ REPRESENTATION\ ADEQUACY}
\to
\mathrm{V2\ SPINE\ CROSSCHECK}.
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
