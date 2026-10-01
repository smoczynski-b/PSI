# PSI

**PSI is a formal research program on justified inference under constrained observation.**

For a task \(\mathcal T\), exact resolution is controlled by

\[
F(Y)=\Psi^{-1}(\mathcal K^Y)
\]

and

\[
\boxed{|q_{\mathcal T}(F(Y))|=1\iff F(Y)\neq\varnothing\land F(Y)^2\subseteq E_{\mathcal T}.}
\]

## Publication boundary

This repository is the public research and release surface. Internal agent instructions, conversation audits, private work selection and unpublished handoffs are maintained in a protected workspace and are not authoritative here.

See [Publication Policy](docs/publication-policy.md). A theorem/test/control PASS is not, by itself, publication authorization or a system-level PASS.

## Current control pointers

- [Physical CANON-03 source bind](docs/canon03-source-bind-01.md)
- [Core mathematical skeleton](docs/core.md)
- [Current Claim Registry — C01–C67](docs/claim-registry.md)
- [Current Falsifier Registry — F01–F64](docs/falsifier-registry.md)
- [Current V2 Theorem Map](docs/theorem-map-v2.md)
- [Current V3 Theorem Map](docs/theorem-map-v3.md)
- [Current Work Map](docs/work-map.md)
- [Public repository routine](docs/work-routine.md)
- [Agent PSI Architecture v02](docs/agent-psi-architecture-02.md)
- [Machine-readable control state](docs/control-state.json)
- [Public source/provenance policy](docs/source-governance-01.md)

Stable current files are updated in place. Numbered maps and registries remain historical provenance; old CURRENT labels do not confer current authority. `scripts/check_control.py` checks organizational consistency, not mathematical truth or live deployment state.

---

## Core status

\[
\boxed{\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).}
\]

CORE5 remains frozen. No accepted typed counterexample forces R4.

## Principia status

```text
Volume I              NORMALIZED PASS
Volume II             II.1–II.16 MATHEMATICAL GLOBAL PASS
Volume III PHISICA    III.1–III.6 PASS AFTER LOCAL ERRATA 01
MOST / HCube          III.7–III.8 MATHEMATICAL GLOBAL PASS
DOM-LOGOS             III.9 PASS / COMPOSITION PASS
SOP-11E               III.10 SECTOR PASS; P2 general PARTIAL
P9-G                  III.11 PASS
P9-H                  III.12 CONDITIONAL PASS / COMPOSITION PASS
P9-I                  III.13 PASS / COMPOSITION PASS
```

### III.13 — Hilbert resolvent/growth bridge

For a complex Hilbert space \(\mathcal H\) and a densely defined closed generator \(A\) of a linear \(C_0\)-semigroup \(T(t)\),

\[
\boxed{\omega_0(T)=s_0(A).}
\]

Classification: **CLASSICAL / ADAPTED — Gearhart–Prüss–Huang bridge — NOT PSI-NEW**.

The result does **not** imply the corresponding Banach-space equality, uniform boundedness from \(\omega_0=0\), a transient peak bound, a Kreiss theorem, or closure of general P9.

\[
\boxed{P9_{\rm general}=OPEN/CENTRAL.}
\]

## Public status of work selection

III.13 is closed. No automatic III.14 is defined. Public documents do not select the next private research unit; a new front requires explicit internal selection.

## Language

Public-facing documentation, release notes and public commit/PR descriptions use English. Mathematical symbols, quotations and protocol identifiers preserve source form. Internal reasoning and agent workshop material are not governed by this public-language rule.

## License

MIT. See [LICENSE](LICENSE).
