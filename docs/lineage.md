# PSI — mathematical lineage

**Mathematics is a language made by people.**

This page is not a defensive bibliography and not a gallery of heroes. It is a guide to the problems, ideas and people whose work PSI inherits, adapts or uses as a benchmark.

The working rule is:

\[
\boxed{
\text{person}
\to
\text{problem}
\to
\text{idea}
\to
\text{later transformation}
\to
\text{role in PSI}
}
\]

A classical result remains classical when PSI uses it. A PSI-specific contribution must be stated separately as a new theorem, a new bridge, a new protocol role, or an explicit counterexample.

## Status labels

- `CLASSICAL` — established mathematics; attribution and citation are mandatory.
- `ADAPTED` — established mathematics used in a different role.
- `BRIDGE` — a claimed connection between established areas; must be proved or tested.
- `PSI-NEW` — a genuinely new result; requires a proof or a falsifiable formal statement.
- `POLICY` — an operational rule, not a theorem.
- `OPEN` — an unresolved mathematical point.

## People, problems, ideas

### Władysław Ślebodziński — change along a flow

**Problem.** How should a geometric object be differentiated when the underlying geometry is carried by a flow?

**Contribution.** In his 1931 paper *Sur les équations canoniques de Hamilton*, Ślebodziński introduced the differential operator later called the Lie derivative. The construction became a standard language for change and invariance of geometric objects along flows.

**Role in PSI.** `CLASSICAL → ADAPTED`. Whenever PSI asks what changes under a transformation and what remains invariant, the Lie-derivative lineage is part of the mathematical background. PSI does not claim this operator or the invariance idea as new.

Reference: W. Ślebodziński, *Sur les équations canoniques de Hamilton*, Bulletin de la Classe des Sciences, Académie Royale de Belgique, 17 (1931), 864–870. Historical note: https://mathshistory.st-andrews.ac.uk/Biographies/Slebodzinski/

### Wacław Sierpiński — sets, topology and the discipline of distinction

**Problem.** What structures become visible when one studies sets, point-set topology and the continuum in their own right?

**Contribution.** Sierpiński made major contributions to set theory, point-set topology and number theory, and helped establish the Polish school of set-theoretic topology and *Fundamenta Mathematicae*.

**Role in PSI.** `CLASSICAL → GENEALOGICAL`. PSI repeatedly depends on distinctions between points, classes, quotient spaces, fibers and topological structure. These are inherited mathematical languages, not proprietary vocabulary.

Reference: https://mathshistory.st-andrews.ac.uk/Biographies/Sierpinski/

### Jan C. Willems — system as behavior

**Problem.** Must a dynamical system be defined by one privileged input–state–output realization?

**Contribution.** The behavioral approach treats the behavior — the set of admissible trajectories — as the central object and makes open/interconnected systems primary.

**Role in PSI.** `CLASSICAL → ADAPTED`. Behavioral spaces and behavioral equivalence are direct antecedents of PSI's use of admissible behavior families. PSI-specific work must lie in the observation contract, task-relative equivalence, identifiability question or protocol design.

Reference: J. C. Willems, *The Behavioral Approach to Open and Interconnected Systems*, IEEE Control Systems Magazine 27(6), 2007. DOI: https://doi.org/10.1109/MCS.2007.906923

### Charles F. Manski — partial identification

**Problem.** What should inference return when data and assumptions do not identify a unique parameter value?

**Contribution.** Manski developed partial identification as a disciplined alternative to forcing point identification; the mathematically justified object may be an identified set.

**Role in PSI.** `CLASSICAL → ADAPTED`. The insistence on keeping a compatible set alive has a clear statistical lineage here. PSI adds task-relative quotients, typed observation contracts and explicit separating-test protocols.

Reference: C. F. Manski, *Partial Identification of Probability Distributions*, Springer, 2003. DOI: https://doi.org/10.1007/b97478

### Joseph L. Doob · Eugene Dynkin — factorization through information

**Problem.** When does one measurable quantity contain no information beyond another?

**Contribution.** The Doob–Dynkin factorization lemma gives conditions under which a measurable function factors through another measurable map.

**Role in PSI.** `CLASSICAL`. Any measurable PSI factorization statement must state the measurable-space hypotheses and acknowledge this lineage. The elementary set-theoretic factorization lemma should be kept distinct from the measurable version.

### Ronald A. Fisher — score and information

**Problem.** How can local sensitivity and inferential precision be quantified statistically?

**Contribution.** Fisher placed likelihood, score and information at the center of statistical estimation.

**Role in PSI.** `CLASSICAL → ADAPTED`. Score-like quantities and Fisher information are imported objects. Any PSI-specific content must be in the surrounding identification problem or in a proved bridge.

Reference: R. A. Fisher, *Theory of Statistical Estimation*, Proceedings of the Cambridge Philosophical Society 22 (1925). DOI: https://doi.org/10.1017/S0305004100009580

### Douglas M. Bates · Donald G. Watts — geometry of nonlinear least squares

**Problem.** How does curvature of a nonlinear model affect estimation, residuals and local approximations?

**Contribution.** Bates and Watts developed a geometric treatment of nonlinear regression using expectation surfaces, tangent approximations, residual structure and curvature.

**Role in PSI.** `CLASSICAL → ADAPTED`. Residual geometry used in PSI must be cited as inherited; a PSI contribution begins only with an additional identifiability statement or bridge.

Reference: D. M. Bates and D. G. Watts, *Nonlinear Regression Analysis and Its Applications*, Wiley, 1988. DOI: https://doi.org/10.1002/9780470316757

### Élie Cartan · Hans F. Münzner · Quo-Shin Chi — isoparametric geometry

**Problem.** How are hypersurfaces constrained when their principal curvatures and level-set geometry satisfy strong invariance conditions?

**Contribution.** Cartan founded the modern theory of isoparametric hypersurfaces; Münzner proved decisive structural restrictions in spheres; later work, including Chi's series, completed the remaining four-principal-curvature classification cases.

**Role in PSI / PHISICA.** `CLASSICAL → ADAPTED`. Conditions of the form

\[
|\nabla \Lambda|^2=B(\Lambda),
\qquad
\Delta\Lambda=C(\Lambda)
\]

belong to the isoparametric tradition. If PSI or PHISICA uses them, they must be named as such. New content, if any, lies in the role imposed on them, not in the equations themselves.

Reference: T. E. Cecil and P. J. Ryan, *On the Work of Cartan and Münzner on Isoparametric Hypersurfaces*, Axioms 14(1), 56 (2025). DOI: https://doi.org/10.3390/axioms14010056

### John G. Kemeny · J. Laurie Snell — lumpability

**Problem.** When can a Markov chain be aggregated to a quotient without losing the Markov property?

**Contribution.** The classical finite-state theory of lumpability formalizes when a partition supports a well-defined reduced Markov chain.

**Role in PSI.** `CLASSICAL → BENCHMARK`. Dynamic task quotients should be compared with lumpability, not merely renamed. A PSI result must specify hypotheses under which the two coincide or differ.

Reference: J. G. Kemeny and J. L. Snell, *Finite Markov Chains*, 1960.

### Robert Paige · Robert E. Tarjan — partition refinement

**Problem.** How can the coarsest stable partition of a finite relational system be computed efficiently?

**Contribution.** Paige and Tarjan developed efficient partition-refinement algorithms that became a central pattern for finite-state equivalence computation.

**Role in PSI.** `CLASSICAL → BENCHMARK`. Any finite PSI algorithm for a coarsest dynamically stable partition should be compared against this lineage.

Reference: R. Paige and R. E. Tarjan, *Three Partition Refinement Algorithms*, SIAM Journal on Computing 16(6), 1987. DOI: https://doi.org/10.1137/0216062

### Lloyd N. Trefethen · Mark Embree — pseudospectra and nonnormality

**Problem.** What does ordinary spectral analysis miss for nonnormal matrices and operators?

**Contribution.** Trefethen and Embree systematized the modern use of pseudospectra to expose sensitivity and transient amplification that eigenvalues alone can hide.

**Role in PSI.** `CLASSICAL → ADAPTED`. Operator laboratories and HCube inherit this language directly. PSI-specific content begins only where pseudospectral tools enter a distinct identifiability problem or produce a genuinely new separating invariant.

Reference: L. N. Trefethen and M. Embree, *Spectra and Pseudospectra: The Behavior of Nonnormal Matrices and Operators*, Princeton University Press, 2005. DOI: https://doi.org/10.2307/j.ctvzxx9kj

## Working rule

For every substantial mathematical object introduced in the repository, ask:

\[
\boxed{
\text{Who?}
\quad
\text{Which problem?}
\quad
\text{What exactly was contributed?}
\quad
\text{What changes in PSI?}
}
\]

Citation is not merely defensive apparatus. It is part of mathematical memory.
