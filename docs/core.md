# PSI — core mathematical skeleton

This note gives the minimal public skeleton of PSI. It is a public derivative of the pinned `PSI-R3-CONSOLIDATED-CANON-03`; it is not the full historical development of the project and it does not supersede the canonical source.

## 1. Contract

Relative to a contract \(c\), the working core is

\[
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
\]

Interpretation:

- \(\Omega_c\) — candidate space after any **task-legal** realization/gauge reduction required by the contract;
- \(\Psi_c:\Omega_c\to\mathcal B_c\) — observation map;
- \(\mathcal K_c\subseteq\mathcal B_c\times\mathcal Y_c\) — typed compatibility relation;
- \(\mathscr O_{\mathcal T,c}\) — task-relevant local observables, each with an explicit codomain;
- \(\delta_c\) — admissible dynamics/update. In the deterministic case \(\delta_c:\Omega_c\to\Omega_c\); stochastic dynamics require an explicitly typed transition kernel rather than silently reusing the deterministic notation.

The contract matters: identifiability is always relative to what counts as a candidate, an observation, a task, an admissible distinction and an admissible evolution.

The phrase `after gauge reduction` does not mean that every symmetry object may automatically be replaced by its coarse orbit set. A proposed reduction must preserve all distinctions required by the task; the exact adequacy test is stated below.

## 2. Observation and fiber

The observation pipeline may be written as

\[
\Omega\xrightarrow{\mathrm{Sem}}\mathfrak B
\xrightarrow{\mathrm{Obs}}\mathfrak Z,
\qquad
\Psi=\mathrm{Obs}\circ\mathrm{Sem}.
\]

For observed data \(Y\), let

\[
\mathcal K^Y=\{b:(b,Y)\in\mathcal K\}.
\]

The compatible fiber is

\[
\boxed{F(Y)=\Psi^{-1}(\mathcal K^Y).}
\]

The first PSI discipline is therefore

\[
\boxed{\text{observation}\neq\text{identified hidden object}.}
\]

If several candidates remain in \(F(Y)\), selecting one representative is an additional inference and requires justification.

## 3. Task closure and task-relative equivalence

For a task \(\mathcal T\), let

\[
\mathscr R_{\mathcal T,c}
=
\operatorname{Cl}^{\mathcal T}_{\delta_c}(\mathscr O_{\mathcal T,c})
\]

be the smallest family of task quantities that contains \(\mathscr O_{\mathcal T,c}\) and is closed under the task operations admitted by the contract, in particular the transports through \(\delta_c\) that the task requires.

The notation is deliberately contract-relative: the contract must say which operations/transports are admissible. The symbol \(\operatorname{Cl}^{\mathcal T}_{\delta_c}\) is not a license to import an unspecified dynamics.

For a map \(R:\Omega_c\to W_R\), define its exact equivalence kernel by

\[
\boxed{
\ker_{\rm eq}R
=
\{(x,y)\in\Omega_c^2:R(x)=R(y)\}.
}
\]

Task-equivalence is

\[
\boxed{
E_{\mathcal T,c}
=
\bigcap_{R\in\mathscr R_{\mathcal T,c}}
\ker_{\rm eq}R.
}
\]

The task quotient is

\[
\boxed{M_{\mathcal T,c}=\Omega_c/E_{\mathcal T,c},}
\]

with quotient map

\[
q_{\mathcal T,c}:\Omega_c\to M_{\mathcal T,c}.
\]

This separates ontic multiplicity from task-relevant multiplicity: two candidates may be different while still being indistinguishable for the task at hand.

## 4. Exact decidability

Observation \(Y\) exactly resolves task \(\mathcal T\) iff

\[
|q_{\mathcal T,c}(F_c(Y))|=1.
\]

Equivalently,

\[
\boxed{
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)^2\subseteq E_{\mathcal T,c}.
}
\]

This is an elementary quotient statement. The PSI-specific content is the contract-, observation- and task-relative architecture in which the quotient is constructed.

## 5. Factorization criterion

For maps \(\rho:\Omega\to Z\) and \(R:\Omega\to W\),

\[
\boxed{
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,\quad R=g\circ\rho.
}
\]

Interpretation: a representation \(\rho\) is sufficient for recovering \(R\) exactly when \(\rho\) never identifies two states that \(R\) still needs to distinguish.

This is classical elementary factorization through equivalence classes; PSI does not claim novelty for the lemma itself.

## 6. Global sufficiency

Let

\[
E_\Psi=\ker_{\rm eq}\Psi.
\]

Then

\[
\boxed{
E_\Psi\subseteq E_{\mathcal T}
\iff
\exists!\,f:\operatorname{im}\Psi\to M_{\mathcal T},\quad
q_{\mathcal T}=f\circ\Psi.
}
\]

Thus a deterministic observation is globally sufficient for the task exactly when the task quotient factors through the observation.

For a general representation \(\rho\), task adequacy is

\[
\boxed{\ker_{\rm eq}\rho\subseteq E_{\mathcal T}.}
\]

### 6.1. Gauge / truncation legality

A proposed gauge, quotient or truncation map

\[
q_G:\Omega\to Z
\]

is legal for task \(\mathcal T\) only if it is itself a task-adequate representation:

\[
\boxed{
\ker_{\rm eq}q_G\subseteq E_{\mathcal T}.
}
\]

Therefore a groupoid, symmetry object or witness-bearing compatibility structure must not be replaced by a coarse orbit/component set when stabilizers, compatibility witnesses or other discarded data remain task-relevant.

Equivalently: quotienting is a conclusion licensed by the task contract, not a preprocessing right.

## 7. Dynamics on the quotient

For deterministic \(\delta:\Omega\to\Omega\) and an equivalence relation \(E\), a unique quotient dynamics

\[
\bar\delta:\Omega/E\to\Omega/E,
\qquad
\bar\delta\circ q=q\circ\delta,
\]

exists iff

\[
\boxed{xEy\Rightarrow\delta(x)E\delta(y).}
\]

This is the well-definedness condition for \(\bar\delta([x])=[\delta(x)]\).

For Markov dynamics, the corresponding classical reference is lumpability; the deterministic condition must not be transferred unchanged to the stochastic case.

## 8. Logical order

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

## 9. What is deliberately not in the minimal core

The public core does not automatically absorb every useful extension. Higher fibers, factorization spaces, frame changes, memory conditions, stochastic state abstraction, operator realizations and domain-specific laboratories belong to later layers unless a counterexample forces a genuinely new primitive role.

The rule is conservative:

\[
\boxed{\text{new primitive only when the semantic role truly changes}.}
\]
