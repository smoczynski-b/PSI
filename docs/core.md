# PSI — core mathematical skeleton

This note gives the minimal public skeleton of PSI. It is not the full historical development of the project.

## 1. Contract

Relative to a contract \(c\), the working core is

\[
\mathfrak P_c=
(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
\]

Interpretation:

- \(\Omega_c\) — candidate space after the relevant gauge quotient;
- \(\Psi_c\) — observation map;
- \(\mathcal K_c\) — typed compatibility relation between observations and admissible data/claims;
- \(\mathscr O_{\mathcal T,c}\) — task-relevant local observables;
- \(\delta_c\) — dynamics used to close those observables under the task horizon.

The contract matters: identifiability is always relative to what counts as a candidate, an observation, a task and an admissible distinction.

## 2. Observation and fiber

The observation pipeline may be written as

\[
\Omega\xrightarrow{\mathrm{Sem}}\mathfrak B
\xrightarrow{\mathrm{Obs}}\mathfrak Z,
\qquad
\Psi=\mathrm{Obs}\circ\mathrm{Sem}.
\]

For observed data \(Y\), the compatible fiber is

\[
F(Y)=\Psi^{-1}(\mathcal K^Y).
\]

The first PSI discipline is therefore:

\[
\boxed{\text{observation} \neq \text{identified hidden object}.}
\]

If several candidates remain in \(F(Y)\), selecting one representative is an extra inference and requires justification.

## 3. Task-relative equivalence

For a task \(\mathcal T\), let the dynamically closed family of relevant observables be

\[
\mathcal R_{\mathcal T}
=
\operatorname{Cl}^{\mathcal T}_{\delta}(\mathscr O_{\mathcal T}).
\]

Define task-equivalence by

\[
E_{\mathcal T}
=
\bigcap_{R\in\mathcal R_{\mathcal T}}
\ker_{\mathrm{meq}} R.
\]

The task quotient is

\[
M_{\mathcal T}=\Omega/E_{\mathcal T},
\]

with quotient map

\[
q_{\mathcal T}:\Omega\to M_{\mathcal T}.
\]

This separates ontic multiplicity from task-relevant multiplicity: two candidates may be different while still being indistinguishable for the task at hand.

## 4. Exact decidability

Observation \(Y\) exactly resolves task \(\mathcal T\) iff

\[
|q_{\mathcal T}(F(Y))|=1.
\]

Equivalently,

\[
\boxed{
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)^2\subset E_{\mathcal T}.
}
\]

This is the core form of the right-to-conclude criterion: the full compatible fiber must lie inside one task-equivalence class.

## 5. Factorization criterion

For maps \(\rho\) and \(R\), a basic PSI factorization criterion is

\[
\ker_{\mathrm{meq}}\rho
\subset
\ker_{\mathrm{meq}}R
\iff
\exists g:\;R=g\circ\rho.
\]

Interpretation: a representation \(\rho\) is sufficient for recovering \(R\) exactly when \(\rho\) never identifies two states that \(R\) still needs to distinguish.

## 6. Global sufficiency

Let \(E_\Psi\) be the equivalence induced by the observation map. A global sufficiency statement takes the form

\[
E_\Psi\subset E_{\mathcal T}
\iff
\exists f:\;q_{\mathcal T}=f\circ\Psi.
\]

Thus the observation is globally sufficient for the task exactly when the task quotient factors through the observation.

## 7. Logical order

PSI uses the following order of work:

\[
\boxed{
\text{catalog adequacy}
\to
\text{fiber}
\to
\text{local identifiability}
\to
\text{global identifiability}
\to
\text{protocol design}
}
\]

Changing the order usually introduces hidden assumptions.

## 8. What is deliberately not in the minimal core

The public core does not automatically absorb every useful extension. Higher fibers, factorization spaces, frame changes, memory conditions, lumpability, operator realizations and domain-specific laboratories belong to later layers unless a counterexample forces a new primitive role.

The rule is conservative:

\[
\boxed{\text{new primitive only when the semantic role truly changes}.}
\]
