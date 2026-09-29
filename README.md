# PSI

**PSI is a formal research program on justified inference under constrained observation.**

For a task \(\mathcal T\), exact resolution is controlled by

\[
F(Y)=\Psi^{-1}(\mathcal K^Y)
\]

and

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
- [Current Claim Registry — C01–C67](docs/claim-registry.md)
- [Current Falsifier Registry — F01–F62](docs/falsifier-registry.md)
- [Current V2 Theorem Map](docs/theorem-map-v2.md)
- [Current V3 Theorem Map](docs/theorem-map-v3.md)
- [Current Work Map](docs/work-map.md)
- [Proportional working routine](docs/work-routine.md)
- [Agent PSI Architecture v02](docs/agent-psi-architecture-02.md)
- [Machine-readable control state](docs/control-state.json)

Stable current files are updated in place. Numbered maps and registries remain
historical provenance; their old CURRENT labels do not confer current authority.
Run `python scripts/check_control.py` to check organizational consistency.
This check does not verify mathematical proofs or live deployments.

---

# Core status

\[
\boxed{
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
}
\]

CORE5 remains frozen.

Exact task-information adequacy:

\[
\boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}.}
\]

No current typed counterexample forces R4.

---

# Principia status

## Volume I

\[
\boxed{\mathrm{V1}=\mathrm{NORMALIZED\ PASS}.}
\]

## Volume II

\[
\boxed{\mathrm{II.1:II.16}=\mathrm{MATHEMATICAL\ GLOBAL\ PASS}.}
\]

## Volume III — PHISICA

\[
\boxed{
\mathrm{III.1:III.6}
=\mathrm{MATHEMATICAL\ GLOBAL\ PASS\ AFTER\ LOCAL\ ERRATA\ 01}.
}
\]

## Volume III — MOST / HCube

\[
\boxed{
\mathrm{III.7:III.8}
=\mathrm{MATHEMATICAL\ GLOBAL\ PASS}.
}
\]

The resolvent-information and semigroup-norm branches are not universally interchangeable.

## Volume III — DOM-LOGOS

\[
\boxed{\mathrm{III.9}=\mathrm{PASS/COMPOSITION\ PASS}.}
\]

## Volume III — SOP-11E

\[
\boxed{P2_{\rm general}=PARTIAL}
\]

and

\[
\boxed{\mathrm{III.10}=\mathrm{SECTOR\ PASS}.}
\]

---

# Volume III — P9 operator-dynamic layer

The P9 migration separated:

\[
H_L=D^2L(x_*)
\]

from

\[
H_{\rm diss}=-\frac{A+A^*}{2},
\]

and raw resolvent sensitivity

\[
\mathcal R_0(A)
=
\sup_{\Re z\ge0}\|(zI-A)^{-1}\|
\]

from the continuous-time Kreiss constant

\[
\mathcal K(A)
=
\sup_{\Re z>0}
\Re z\,\|(zI-A)^{-1}\|.
\]

For \(A=-\mu I\):

\[
\boxed{
\mathcal R_0(A)=1/\mu,
\qquad
\mathcal K(A)=1.
}
\]

Thus resolvent-margin sensitivity and transient amplification are distinct observables.

---

## III.11 — P9-G metric-gradient bridge

For

\[
A=-G^{-1}H,
\qquad G,H>0,
\]

with

\[
B=G^{-1/2}HG^{-1/2},
\qquad
\mu_G=\lambda_{\min}(B),
\]

we have

\[
\boxed{\|e^{tA}\|_G=e^{-\mu_Gt}},
\]

\[
\boxed{\mathcal K_G(A)=1},
\]

and

\[
\boxed{
\|e^{tA}\|_2
\le
\sqrt{\kappa_2(G)}e^{-\mu_Gt}.
}
\]

Status:

\[
\boxed{\mathrm{III.11\ P9\!-
G}=PASS.}
\]

---

## III.12 — P9-H modified-energy / hypocoercive bridge

Let \(A\) generate a \(C_0\)-semigroup and suppose there exists a bounded coercive metric

\[
Q=Q^*,
\qquad
mI\le Q\le MI,
\]

such that

\[
\boxed{
A^*Q+QA\le-2\lambda Q.
}
\]

Then

\[
\boxed{\|e^{tA}\|_Q\le e^{-\lambda t}},
\]

\[
\boxed{
\|e^{tA}\|
\le
\sqrt{\kappa(Q)}e^{-\lambda t},
}
\]

\[
\boxed{
\|(zI-A)^{-1}\|_Q
\le
\frac1{\Re z+\lambda}
\quad(\Re z>-\lambda),
}
\]

\[
\boxed{
1\le\mathcal K(A)\le\sqrt{\kappa(Q)},
\qquad
\mathcal K_Q(A)=1,
}
\]

and

\[
\boxed{
\sup\Re\sigma_\varepsilon(A)
\le
-\lambda+\sqrt{\kappa(Q)}\,\varepsilon.
}
\]

For the standard hypocoercive decomposition

\[
A=S+N,
\quad S=S^*\le0,
\quad N^*=-N,
\]

the ambient norm is non-increasing. Hence

\[
\boxed{
\text{hypocoercive decay}
\neq
\text{transient growth}.
}
\]

DMS is retained only under its typed H1–H4 mechanism; the project does not replace those hypotheses with a generic commutator slogan.

Status:

\[
\boxed{
\mathrm{III.12\ P9\!-
H}=PASS,
\qquad
\mathrm{III.7:III.12}=\mathrm{COMPOSITION\ PASS}.
}
\]

Main files:

- [P9-U Hypocoercive Source / Contract Gate 01](docs/p9u-hypocoercive-source-contract-01.md)
- [III.12 — hypocoercive modified-energy bridge](docs/principia-v3-12-hypocoercive-modified-energy-bridge.md)
- [P9-H Composition Crosscheck 01](docs/principia-v3-p9h-composition-crosscheck-01.md)

---

# Current P9 taxonomy

- `P9-G` — metric-gradient: **CLOSED as III.11**;
- `P9-H` — bounded coercive Lyapunov metric / hypocoercive modified energy: **CLOSED CONDITIONALLY as III.12**;
- `P9-J` — Jordan / defective local laboratory: **CLOSED LOCALLY**;
- `P9-I / P9-U` — infinite-dimensional and unrestricted nonnormal generators: **OPEN / CENTRAL**.

Therefore

\[
\boxed{P9_{\rm general}=OPEN/CENTRAL.}
\]

---

# Permanent distinctions

\[
\boxed{\text{static task adequacy}\not\Rightarrow\text{dynamic projectability}},
\]

\[
\boxed{\text{well-posedness}\neq\text{projectability}},
\]

\[
\boxed{\text{raw resolvent sensitivity}\neq\text{Kreiss/transient amplification}},
\]

\[
\boxed{H_L\neq H_{\rm diss}\text{ in general}},
\]

\[
\boxed{\text{hypocoercive decay}\neq\text{transient growth}},
\]

\[
\boxed{\text{Kreiss amplification index}\neq\text{decay/growth margin}},
\]

\[
\boxed{\text{modified metric}\Rightarrow\text{new norm-sensitive representation contract}}.
\]

---

# Current phase

Subject to [global work selection](docs/work-map.md), the next mathematical source gate concerns the genuinely infinite-dimensional relation between resolvent and semigroup growth:

- unbounded generators;
- continuous spectrum;
- Gearhart–Prüss scope;
- failure of finite-dimensional Kreiss equivalence;
- the exact role of uniform half-plane versus imaginary-axis resolvent bounds.

No III.13 theorem is authorized yet.

Current admissible mathematical state (not an unconditional global priority):

\[
\boxed{
\mathrm{P9\!-
I\ INFINITE\!-
DIMENSIONAL\ RESOLVENT/GROWTH\ SOURCE\ GATE\ NEXT}.
}
\]

Mathematical dependency history:

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
11E\ PASS}
\to
\mathrm{III.11\ P9\!-
G\ PASS}
\to
\mathrm{III.12\ P9\!-
H\ PASS}
\to
\mathrm{P9\!-
I\ SOURCE\ GATE\ NEXT}.
}
\]

Traffic instrumentation is intentionally WAIT under [the frozen protocol](experiments/PSI-TRAFFIC-EST-01.md); prospective observation continues. Read the [work map](docs/work-map.md) for release conditions and regular checks.

Primitive growth remains frozen until a new typed counterexample forces a new semantic role.

---

## Decision / epistemic ledger

- [Ledger base](docs/psi-ledger-01.md)
- [Ledger Addendum 09 — P9 repair / P9-U handoff](docs/psi-ledger-01-addendum-09.md)
- [Ledger Addendum 10 — P9-H closure / P9-I handoff](docs/psi-ledger-01-addendum-10.md)

## Language

Internal theoretical development is primarily in Polish. Public repository-facing material is written primarily in English.

## License

MIT. See [LICENSE](LICENSE).
