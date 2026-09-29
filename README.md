# PSI

**PSI is a formal research program on justified inference under constrained observation.**

It asks:

> What are we entitled to conclude from what we can actually observe?

For a task \(\mathcal T\), exact resolution is controlled by the compatible fibre

\[
F(Y)=\Psi^{-1}(\mathcal K^Y)
\]

and the task quotient:

\[
\boxed{
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)^2\subseteq E_{\mathcal T}.
}
\]

---

## Current control pointers

- [Physical CANON-03 source bind](docs/canon03-source-bind-01.md)
- [Core mathematical skeleton](docs/core.md)
- [Current Claim Registry v13](docs/claim-registry-13.md)
- [Current Falsifier Registry v12](docs/falsifier-registry-12.md)
- [Freeze 01](docs/principia-v1-v2-freeze-01.md)
- [Freeze 01 Errata 01](docs/principia-v1-v2-freeze-01-errata-01.md)
- [Current Volume Skeleton 03](docs/principia-volume-skeleton-03.md)
- [Current V2 Theorem Map 04](docs/principia-v2-theorem-map-04.md)
- [Current V3 Theorem Map 06](docs/principia-v3-theorem-map-06.md)
- [Current Sector Work Map 07](docs/work-map-07.md)
- [Agent PSI Architecture v02](docs/agent-psi-architecture-02.md)

Historical maps, older theorem maps and superseded source artefacts remain in the repository for provenance.

---

## Core status

\[
\boxed{
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
}
\]

CORE5 remains frozen.

Exact task-information adequacy:

\[
\boxed{
\ker_{eq}\rho\subseteq E_{\mathcal T}.
}
\]

Permanent inference discipline:

\[
\boxed{
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
}
\]

No current typed counterexample forces R4.

---

# Principia status

## Volume I

\[
\boxed{
\mathrm{V1}=\mathrm{NORMALIZED\ PASS}.
}
\]

## Volume II

\[
\boxed{
\mathrm{II.1:II.16}=\mathrm{MATHEMATICAL\ GLOBAL\ PASS}.
}
\]

The Volume II control layer is frozen through V2 Theorem Map 04.

## Freeze Errata 01

The former C19-v2 singleton claim for the gauge-only factorization fibre is withdrawn. Current MINI keeps uniqueness of the normal-form class rather than literal uniqueness of the gauge-only factorization fibre.

No CORE role changed.

---

# Volume III — PHISICA operator block

PHISICA was rebuilt by operator legality rather than copied from the historical text.

Certified chain:

\[
\boxed{
\mathrm{PROJECTABILITY}
\to
\mathrm{WEIGHTED\ REALIZATION}
\to
\mathrm{SELF\!-
ADJOINT\ REALIZATION}
\to
\mathrm{COMPACT\ SPECTRAL\ THEORY}
\to
\mathrm{UNITARY\ LIOUVILLE\ FORM}
\to
\mathrm{PERTURBATION/HF}.
}
\]

Current result:

\[
\boxed{
\mathrm{PHISICA\ III.1:III.6}
=
\mathrm{MATHEMATICAL\ GLOBAL\ PASS\ AFTER\ LOCAL\ ERRATA\ 01}.
}
\]

Main files:

- [III.1 — Lambda operator projectability](docs/principia-v3-01-lambda-operator-projectability.md)
- [III.2 — weighted Sturm–Liouville / pushforward measure](docs/principia-v3-02-weight-sturm-liouville.md)
- [III.3 — domain and self-adjoint realization](docs/principia-v3-03-domain-selfadjoint.md)
- [III.4 — compact resolvent and discrete spectrum](docs/principia-v3-04-compact-resolvent-spectrum.md)
- [III.5 — unitary Liouville normal form](docs/principia-v3-05-liouville-normal-form.md)
- [III.6 — perturbation and Hellmann–Feynman](docs/principia-v3-06-perturbation-hellmann-feynman.md)
- [PHISICA Whole-Block Crosscheck 01](docs/principia-v3-phisica-whole-crosscheck-01.md)

The arrows above mean progressively stronger typed contracts, not one blanket implication chain.

---

# Volume III — MOST / HCube

For finite-dimensional operators under a fixed norm:

\[
\boxed{
\ker_{eq}\rho_r
=
\ker_{eq}\rho_{ps}
\subseteq
\ker_{eq}\rho_\sigma.
}
\]

Operator-information graph:

\[
\boxed{
A\to\mathcal R_A(\cdot)
\to r_A(\cdot)
\leftrightarrow\rho_{ps}(A)
\to\rho_\sigma(A).
}
\]

Transient dynamics form a separate branch:

\[
\boxed{
A\to e^{tA}\to\|e^{tA}\|.
}
\]

HCube proves that equal spectrum and equal operator norm can still fail a resolvent-sensitive task. It also gives a pair with identical scalar semigroup-norm profiles but different resolvent-norm profiles, so

\[
\boxed{
\rho_r\neq F\circ\rho_g
\text{ universally}.
}
\]

The converse non-factorization is not claimed.

Current result:

\[
\boxed{
\mathrm{MOST/HCUBE\ III.7:III.8}
=
\mathrm{MATHEMATICAL\ GLOBAL\ PASS}.
}
\]

Main files:

- [III.7 — MOST spectral information hierarchy](docs/principia-v3-07-spectral-information-hierarchy-most.md)
- [III.8 — HCube MOST laboratory](docs/principia-v3-08-hcube-nonnormal-resolvent-lab.md)
- [MOST/HCube Whole-Layer Crosscheck 01](docs/principia-v3-most-hcube-whole-crosscheck-01.md)

---

# Volume III — DOM-LOGOS

The historical source gate recovered the semigroup formulation from `PRINCIPIA_SEMANTICA_KANON_SCALONY_2026-07-26A.tex`.

III.9 proves:

\[
\boxed{
\Lambda x=\Lambda y
\Rightarrow
\Lambda S(t)x=\Lambda S(t)y
\quad\forall t\ge0
}
\]

iff there exists a unique reduced semigroup on \(\operatorname{im}\Lambda\) satisfying

\[
\boxed{
\Lambda S(t)=\widetilde S(t)\Lambda.
}
\]

For bounded linear intertwiners between linear \(C_0\)-semigroups:

\[
\boxed{
TS(t)=\bar S(t)T
\iff
T(D(A))\subseteq D(\bar A)
\land
\bar AT=TA\text{ on }D(A).
}
\]

For nonlinear \(\Lambda\), the generator identity is retained only as a derivative consequence unless a separate well-posedness theorem closes the converse.

\[
\boxed{
\mathrm{III.9\ DOM\!-
LOGOS}=\mathrm{PASS/COMPOSITION\ PASS}.
}
\]

Main files:

- [DOM-LOGOS Source Bind 01](docs/dom-logos-source-bind-01.md)
- [III.9 — semigroup projectability / DOM-LOGOS](docs/principia-v3-09-semigroup-projectability-dom-logos.md)
- [DOM-LOGOS Crosscheck 01](docs/principia-v3-dom-logos-crosscheck-01.md)

---

# Volume III — SOP-11E well-posedness

The general historical equation

\[
D_t\psi=-\nabla_{G(\psi)}L(\psi)+Z
\]

remains too broad for a universal theorem.

Project-level status:

\[
\boxed{
P2_{\mathrm{general}}=PARTIAL.
}
\]

III.10 closes two typed sectors.

## Smooth forced Hilbert sector

For fixed bounded coercive \(G\), globally Lipschitz \(\nabla L\), and \(Z\in L^1_{loc}\), the evolution has a unique global absolutely continuous solution with quantitative continuous dependence.

Bare \(L\in C^2\) does not imply global existence.

## Convex subdifferential sector

For proper lsc convex \(L\) and constant forcing \(z\),

\[
\dot u\in-\partial L(u)+z
\]

is generated by a nonlinear contraction semigroup through maximal-monotone / Crandall–Liggett theory.

Time-dependent forcing yields an evolution family \(U(t,s)\), not automatically an autonomous semigroup.

Current result:

\[
\boxed{
\mathrm{III.10\ SOP\!-
11E}=\mathrm{SECTOR\ PASS}.
}
\]

and

\[
\boxed{
\mathrm{III.9:III.10}=\mathrm{COMPOSITION\ PASS}.
}
\]

Main files:

- [SOP-11E Well-Posedness Migration 01](docs/sop11e-wellposedness-migration-01.md)
- [III.10 — typed well-posedness sectors](docs/principia-v3-10-sop11e-wellposedness-sectors.md)
- [III.9–III.10 Composition Crosscheck 01](docs/principia-v3-sop11e-dom-logos-crosscheck-01.md)

---

# Permanent distinctions

\[
\boxed{\text{Hilbert weight}\neq\text{spectral measure}},
\]

\[
\boxed{\text{formal expression}\neq\text{self-adjoint operator}},
\]

\[
\boxed{\text{self-adjointness}\not\Rightarrow\text{compact resolvent}},
\]

\[
\boxed{\text{bounded similarity}\neq\text{unitary equivalence}},
\]

\[
\boxed{\{E_n\}\not\Rightarrow\text{complete model identification}},
\]

\[
\boxed{\text{static task adequacy}\not\Rightarrow\text{dynamic projectability}},
\]

\[
\boxed{\text{well-posedness}\neq\text{projectability}},
\]

\[
\boxed{\text{time-dependent forcing}\not\Rightarrow\text{autonomous semigroup}},
\]

\[
\boxed{L\in C^2\not\Rightarrow\text{global well-posedness}},
\]

\[
\boxed{\text{coercivity}\not\Rightarrow\text{compact global attractor}},
\]

\[
\boxed{\text{linearized stability}\not\Rightarrow\text{global nonlinear dynamics}}.
\]

---

# Current phase

The next unresolved operator-dynamic front is the historical P9 bridge:

\[
\boxed{
H
\longleftrightarrow
(zI-A)^{-1}
\longleftrightarrow
e^{tA}.
}
\]

`KANON2.txt` classifies this as `OPEN / CENTRAL`.

MOST/HCube has clarified the information structure but has not proved a universal Hessian-to-transient theorem.

Therefore:

\[
\boxed{
\mathrm{P9\ HESSIAN\!-
TRANSIENT\ MIGRATION\ GATE\ NEXT}.
}
\]

Current execution graph:

\[
\boxed{
\mathrm{V1\ PASS}
\to
\mathrm{V2\ GLOBAL\ PASS}
\to
\mathrm{PHISICA\ GLOBAL\ PASS}
\to
\mathrm{MOST/HCUBE\ GLOBAL\ PASS}
\to
\mathrm{III.9\ DOM\!-
LOGOS\ PASS}
\to
\mathrm{III.10\ SOP\!-
11E\ SECTOR\ PASS}
\to
\mathrm{P9\ MIGRATION\ GATE\ NEXT}.
}
\]

Primitive growth remains frozen until a new typed counterexample forces a genuinely new semantic role.

---

## Decision / epistemic ledger

- [Ledger base](docs/psi-ledger-01.md)
- [Ledger Addendum 07 — DOM-LOGOS closure / SOP-11E handoff](docs/psi-ledger-01-addendum-07.md)
- [Ledger Addendum 08 — SOP-11E sector closure / P9 handoff](docs/psi-ledger-01-addendum-08.md)

---

## Publications / Zenodo

- DOI: 10.5281/zenodo.18893354
- DOI: 10.5281/zenodo.18644750
- DOI: 10.5281/zenodo.18498472
- DOI: 10.5281/zenodo.18498440

## Language

Internal theoretical development is primarily in Polish. Public repository-facing material is written primarily in English.

## License

MIT. See [LICENSE](LICENSE).
