# PSI

**PSI is a formal research program on justified inference under constrained observation.**

It asks:

> What are we entitled to conclude from what we can actually observe?

The central compatible set is

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

For a task \(\mathcal T\), exact resolution means

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)^2\subseteq E_{\mathcal T}.
\]

## Current control pointers

- [Physical CANON-03 source bind](docs/canon03-source-bind-01.md)
- [Core mathematical skeleton](docs/core.md)
- [Current claim registry v12](docs/claim-registry-12.md)
- [Current falsifier registry v11](docs/falsifier-registry-11.md)
- [Principia V1/V2 First Freeze 01](docs/principia-v1-v2-freeze-01.md)
- [V1 Normalization 01](docs/principia-v1-normalization-01.md)
- [V2.1 Exact task-level decidability](docs/principia-v2-01-exact-task-decidability.md)
- [V2.2 Kernel factorization](docs/principia-v2-02-kernel-factorization.md)
- [V2.3 Global observer sufficiency](docs/principia-v2-03-global-observer-sufficiency.md)
- [V2.4 Representation adequacy](docs/principia-v2-04-representation-adequacy.md)
- [V2.5 Task-information legality of reduction](docs/principia-v2-05-task-information-legality-of-reduction.md)
- [V2.6 Deterministic quotient dynamics](docs/principia-v2-06-deterministic-quotient-dynamics.md)
- [V2.7 Exact history-memory adequacy](docs/principia-v2-07-exact-history-memory-adequacy.md)
- [V2.8 Coarsest exact history quotient](docs/principia-v2-08-coarsest-exact-history-quotient.md)
- [V2.9 Recursive history quotient update](docs/principia-v2-09-recursive-history-quotient-update.md)
- [V2 own-layer handoff audit](docs/principia-v2-own-layer-crosscheck-02.md)
- [V2 handoff dependency errata](docs/principia-v2-own-layer-crosscheck-02-errata-01.md)
- [V2.10 Strong Markov lumpability](docs/principia-v2-10-strong-lumpability-bridge.md)
- [V2.11 Myhill–Nerode](docs/principia-v2-11-myhill-nerode-bridge.md)
- [V2.12 Paige–Tarjan](docs/principia-v2-12-paige-tarjan-benchmark.md)
- [V2 classical bridge layer cross-check](docs/principia-v2-classical-bridges-crosscheck-01.md)
- [Current V2 theorem map](docs/principia-v2-theorem-map-02.md)
- [Classical comparison map](docs/classical-compare-01.md)
- [Decision / Epistemic Ledger](docs/psi-ledger-01.md)
- [Agent PSI Architecture v02](docs/agent-psi-architecture-02.md)
- [Sector work map](docs/work-map-01.md)

## Core status

\[
\boxed{
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
}
\]

CORE5 remains frozen. Current pressure evidence does not force R4; this is not a universal completeness theorem.

Exact task-information adequacy:

\[
\boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}.}
\]

Inference discipline:

\[
\boxed{
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
}
\]

## Principia status

### Volume I

\[
\boxed{
\mathrm{V1\ FIRST\ PROSE\ PASS}=\mathrm{NORMALIZED\ PASS}.
}
\]

### Volume II — own layer

\[
\boxed{
\mathrm{II.1:II.9}=\mathrm{GLOBAL\ CROSSCHECK\ PASS}.
}
\]

The II.9 dependency correction is now explicit:

\[
\text{SOURCE/RESULT IDS}=C45+C59,
\]

\[
\text{STRICT PROOF DEPENDENCY}=II.7\;(C57/C58)
+\text{typed extension definitions}.
\]

II.6 is structural analogy; II.8 is not a proof prerequisite.

### Volume II — classical bridge layer

\[
\boxed{
\mathrm{II.10:II.12}=\mathrm{GLOBAL\ CROSSCHECK\ PASS}.
}
\]

The bridges are intentionally different:

- **II.10:** Kemeny–Snell / strong lumpability — preservation of transition masses on quotient blocks;
- **II.11:** Myhill–Nerode — exact equality of PSI future-test equivalence with Nerode under the full right-continuation contract;
- **II.12:** Paige–Tarjan — classical algorithm for an eligible finite relational coarsest-partition problem after an explicit reduction.

Permanent boundaries:

\[
\boxed{
\text{task quotient}\not\Rightarrow\text{Markov lumpability}
}
\]

(F61),

\[
\boxed{
\text{arbitrary task equivalence}\neq\text{Nerode equivalence}
}
\]

without full continuation tests, and

\[
\boxed{
\text{finite PSI instance}\not\Rightarrow\text{Paige–Tarjan applicability}
}
\]

without a reduction proof.

Paige–Tarjan complexity is scoped to the classical relational problem: literature reports \(O(m\log n)\) refinement time and \(O(n+m)\) space; Principia separately account for linear explicit-input initialization.

## Current phase

\[
\boxed{
\mathrm{V1\ NORMALIZED\ PASS}
\to
\mathrm{II.1:II.9\ GLOBAL\ PASS}
\to
\mathrm{II.10:II.12\ CLASSICAL\ GLOBAL\ PASS}
\to
\mathrm{CAT/FACT/NORM\ NEXT}
\to
\mathrm{FRAME}
\to
\mathrm{HIGHER}
\to
\mathrm{V2\ WHOLE\ CROSSCHECK}.
}
\]

No Agent v03 is justified by current evidence.

## Publications / Zenodo

- DOI: 10.5281/zenodo.18893354
- DOI: 10.5281/zenodo.18644750
- DOI: 10.5281/zenodo.18498472
- DOI: 10.5281/zenodo.18498440

## Language

Internal theoretical development is primarily in Polish. Public interoperability and repository-facing material are written in English.

## License

MIT. See [LICENSE](LICENSE).
