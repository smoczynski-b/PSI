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
- [Principia V2.2 — Kernel factorization criterion](docs/principia-v2-02-kernel-factorization.md)
- [Principia V2.3 — Global observer sufficiency](docs/principia-v2-03-global-observer-sufficiency.md)
- [Principia V2.4 — Representation adequacy](docs/principia-v2-04-representation-adequacy.md)
- [Principia V2.5 — Task-information legality of reduction/quotient](docs/principia-v2-05-task-information-legality-of-reduction.md)
- [Principia V2.6 — Deterministic quotient dynamics](docs/principia-v2-06-deterministic-quotient-dynamics.md)
- [Principia V2.7 — Exact history-memory adequacy](docs/principia-v2-07-exact-history-memory-adequacy.md)
- [Principia V2.8 — Coarsest exact history quotient](docs/principia-v2-08-coarsest-exact-history-quotient.md)
- [Principia V2.9 — Recursive history quotient update](docs/principia-v2-09-recursive-history-quotient-update.md)
- [Principia V2 Spine Cross-Check 01](docs/principia-v2-spine-crosscheck-01.md)
- [Current Principia V2 Theorem Map 02](docs/principia-v2-theorem-map-02.md)
- [Historical Principia V2 Theorem Map 01](docs/principia-v2-theorem-map-01.md)
- [Proof / Source / Migration Audit 01](docs/proof-source-migration-audit-01.md)
- [CAT / ADEQ / FACT Migration 01](docs/cat-fact-migration-01.md)
- [Regression Bank 01](docs/regression-bank-01.md)
- [Decision / Epistemic Ledger 01](docs/psi-ledger-01.md)
- [Principia V1 Unit Map 01](docs/principia-v1-unit-map-01.md)
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

### V2.1–V2.6

The exact quotient/representation/dynamics spine is frozen in prose with PASS status, including exact task-level decidability, factorization, observer sufficiency, representation adequacy, task-information legality of reductions and deterministic quotient dynamics.

### V2.7 — exact history-memory adequacy

\[
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H'),
\]

and for \(\rho_t:\mathcal H_t\to Z_t\),

\[
\boxed{
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}
\iff
q_{\mathcal T,t}\text{ factors uniquely through }\rho_t\text{ on }\operatorname{im}\rho_t.
}
\]

**Status:** `PASS`.

### V2.8 — coarsest exact history quotient

\[
\boxed{
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}.
}
\]

For every exact memory \(\rho_t\),

\[
\boxed{
q_{\mathcal T,t}=f_t\circ\rho_t,
\qquad
f_t:\operatorname{im}\rho_t\twoheadrightarrow M_{\mathcal T,t}.
}
\]

Thus \(M_{\mathcal T,t}\) is the coarsest exact history quotient in quotient order, not automatically a minimum-bit or minimum-cost implementation.

**Status:** `PASS`.

### V2.9 — recursive history quotient update

Let

\[
D_t\subseteq\mathcal H_t\times\mathcal E_t\times\mathcal Y_{t+1},
\qquad
\delta_t:D_t\to\mathcal H_{t+1}
\]

be the legal partial history update. Under C59, both legality of the same literal label and the future-task class of the successor are invariant under \(\equiv_{\mathcal T,t}\). Therefore the quotient domain \(\overline D_t\) is well-defined and

\[
\boxed{
U_{\mathcal T,t}:\overline D_t\to M_{\mathcal T,t+1}
}
\]

exists uniquely with

\[
\boxed{
U_{\mathcal T,t}([H],\varepsilon,y)
=
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}.
}
\]

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`.

This is abstract representative-independent well-definedness. It does not imply an algorithm that computes the quotient update without a representative, nor finite memory, decidable equivalence, computability or efficiency.

### Current verdict

\[
\boxed{
\mathrm{V2.1:V2.9}=\mathrm{PASS}.
}
\]

The own quotient/history layer is now complete. The next phase is the classical bridge layer, beginning with strong lumpability. Deterministic congruence must not be transferred unchanged to stochastic kernels.

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

Agent v02 remains current and enforces type/domain discipline, scope fidelity, source/classical-status separation, theorem/benchmark separation and regression binding during theorem prose.

No Agent v03 is justified by current evidence.

## Current phase

\[
\boxed{
\mathrm{V1\ NORMALIZED\ PASS}
\to
\mathrm{V2.1:V2.9\ PASS}
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
