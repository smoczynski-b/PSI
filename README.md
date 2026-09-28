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

## Volume II theorem-spine status

### V2.1 — exact task-level decidability

\[
\boxed{
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)\times F_c(Y)\subseteq E_{\mathcal T,c}.
}
\]

**Status:** `PASS`.

### V2.2 — kernel factorization criterion

\[
\boxed{
\ker_{eq}\rho\subseteq\ker_{eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,
\quad
R=g\circ\rho.
}
\]

**Status:** `PASS`. Uniqueness holds only on `im rho`.

### V2.3 — global observer sufficiency

\[
\boxed{
E_{\Psi,c}\subseteq E_{\mathcal T,c}
\iff
\exists!\,f:\operatorname{im}\Psi_c\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=f\circ\Psi_c.
}
\]

**Status:** `PASS`. `Global` means a property of the observer on the whole candidate space, not per-record decidability or statistical sufficiency.

### V2.4 — representation adequacy

\[
\boxed{
\ker_{eq}\rho\subseteq E_{\mathcal T,c}
\iff
\exists!\,g:\operatorname{im}\rho\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=g\circ\rho.
}
\]

**Status:** `PASS`. Task-information adequacy remains distinct from full contract legality.

### V2.5 — task-information legality of reduction / quotient

For a proposed reduction `q:Omega_c->Z`:

\[
\boxed{
\ker_{eq}q\subseteq E_{\mathcal T,c}
\iff
\exists!\,h:\operatorname{im}q\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=h\circ q.
}
\]

**Status:** `PASS`. F57 and F55 remain mandatory boundaries.

### V2.6 — deterministic quotient dynamics

For deterministic \(\delta:\Omega\to\Omega\) and equivalence `E`, a unique quotient dynamics

\[
\bar\delta:\Omega/E\to\Omega/E,
\qquad
\bar\delta\circ q_E=q_E\circ\delta
\]

exists iff

\[
\boxed{xEy\Longrightarrow\delta(x)E\delta(y).}
\]

**Status:** `PASS`.

Static task adequacy does not imply dynamic descent. If the task closure is stable under \(R\mapsto R\circ\delta_c\), then the canonical task equivalence is automatically a congruence for `delta_c`. The theorem is deterministic and must not be conflated with stochastic lumpability.

### V2.7 — exact history-memory adequacy

Future-task equivalence is

\[
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H'),
\]

with root, node labels, edge labels and parent-child structure preserved. It is an equivalence relation by C58.

For

\[
\rho_t:\mathcal H_t\to Z_t,
\]

\[
\boxed{
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}
\iff
\exists!\,f_t:\operatorname{im}\rho_t\to M_{\mathcal T,t},
\quad
q_{\mathcal T,t}=f_t\circ\rho_t.
}
\]

**Status:** `PASS`.

This does not require storing the full history and does not imply bit-, state-, dimension-, storage- or computation-minimality. Go and LAZARUS remain scoped regression witnesses.

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

For quotient representations `q_Q`, exactness is equivalent to

\[
Q\subseteq\equiv_{\mathcal T,t}.
\]

Hence \(\equiv_{\mathcal T,t}\) is the largest admissible exact equivalence relation and \(M_{\mathcal T,t}\) the coarsest exact history quotient in quotient order.

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`.

The claim is about quotient/information order. It does not imply minimum bits, dimension, storage, update cost or computation. F60 continues to restrict factorization/minimality claims to `im rho_t`, not unused codomain points.

### Current verdict

\[
\boxed{
\mathrm{V2.1:V2.8}=\mathrm{PASS}.
}
\]

Next theorem:

\[
\boxed{
\mathrm{V2.9\ —\ recursive\ quotient\ update}.
}
\]

The next boundary is dynamic/algorithmic:

\[
\boxed{
\text{well-defined mathematical recurrence}
\not\Rightarrow
\text{finite memory / computability / efficiency}.
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

Agent v02 remains current and enforces type/domain discipline, scope fidelity, source/classical-status separation, theorem/benchmark separation and regression binding during theorem prose.

No Agent v03 is justified by current evidence.

## Current phase

\[
\boxed{
\mathrm{V1\ NORMALIZED\ PASS}
\to
\mathrm{V2.1:V2.8\ PASS}
\to
\mathrm{V2.9\ HISTORY\ UPDATE}
\to
\mathrm{CLASSICAL\ BRIDGES}.
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
