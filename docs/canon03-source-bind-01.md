# PSI — CANON03 SOURCE BIND 01

**Status:** `PASS / PHYSICAL CANON BOUND`  
**Date:** 2026-09-28

## 0. Physical source

The authoritative physical source used by this audit is:

- repository: `smoczynski-b/psi-model`;
- commit: `7e64ec8ad766623ffeede3daa4bb68dee15135c1`;
- path: `psi-agent/canon/PSI-R3-CONSOLIDATED-CANON-03.md`;
- document identifier: `PSI-R3-CONSOLIDATED-CANON-03`;
- document version: `1.0.0`;
- freeze date stated by the source: `2026-09-08`;
- source status stated by the source: `CURRENT / SUPERIOR PHYSICAL CANON SOURCE`.

The Git blob SHA returned for that file is:

`72d711a40c65376ee932809802622f3985ecb02a`.

This closes the provenance state `UNBOUND` for the current CANON-03 pointer.

---

## 1. Core verification

The physical source directly defines

\[
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c),
\]

with the same semantic roles used by the public `docs/core.md` derivative.

It directly states:

\[
F_c(Y)=\Psi_c^{-1}(\mathcal K_c^Y),
\]

\[
E_{\mathcal T,c}
=
\bigcap_{R\in\mathscr R_{\mathcal T,c}}\ker_{eq}R,
\qquad
M_{\mathcal T,c}=\Omega_c/E_{\mathcal T,c},
\]

and proves both:

\[
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)^2\subseteq E_{\mathcal T,c},
\]

and

\[
\ker_{eq}\rho\subseteq\ker_{eq}R
\iff
\exists!g:\operatorname{im}\rho\to W,
\quad R=g\circ\rho.
\]

It also states the deterministic quotient-dynamics criterion and separates it from stochastic lumpability.

### Verdict

\[
\boxed{\mathrm{CORE5\ /\ C06-C10\ SOURCE\ BIND=PASS}.}
\]

---

## 2. CAT verification

The physical source states:

- `PSI-ID` concerns identifiability inside a fixed catalog;
- `PSI-CAT` asks whether data/protocol justify a catalog change and which class of changes is justified;
- `PSI-CAT^D` adds domain admissibility conditions `ADM_D`;
- domain conditions can eliminate illegal candidates but are not themselves new empirical observations.

It freezes

\[
\boxed{\mathrm{PSI-ID}\neq\mathrm{PSI-CAT}.}
\]

### Consequence for older CAT material

The older detailed `ISO/HOR/REF/CRS`, `GEN/TEST/SELECT`, promotion thresholds and hysteresis machinery is **not** the physical CANON-03 definition of PSI-CAT.

It may survive only as:

- a compatible derived calculus;
- a domain policy;
- a laboratory realization;
- genealogy.

It must not be promoted merely because it occurs in an older typed source.

### Verdict

\[
\boxed{\mathrm{PSI-CAT\ CURRENT\ DEFINITION=BOUND}.}
\]

---

## 3. FACT verification

The physical source defines PSI-FACT for domain `D`, protocol `P`, tolerance `epsilon` and data `Y` through

\[
\operatorname{Fact}^{\varepsilon}_{D,P}(Y),
\]

the fibre of factorizations compatible with observation and protocol.

Objects must satisfy:

- `ADM_D`;
- fixed external interface;
- the data-compatibility criterion.

The source explicitly says that realization equivalence/gauge is quotiented **if the contract establishes it**.

It also freezes the distinction

\[
\boxed{
\text{realization equivalence}
\neq
\text{behavioural recoding}.
}
\]

One-way recoding need not be an equivalence.

### Consequence for older FACT material

The older factorization groupoid and homotopy-ADEQ fibre are mathematically compatible **extensions** when stabilizers/witnesses matter, but they are not the minimal current definition supplied by physical CANON-03.

The HIGHER-FIBRE result still governs when coarse set truncation is inadequate.

### Verdict

\[
\boxed{\mathrm{PSI-FACT\ CURRENT\ DEFINITION=BOUND}.}
\]

---

## 4. Catalog adequacy — correction of V1-GAP-01

Physical CANON-03 freezes the logical order

\[
\boxed{
\text{CATALOG ADEQUACY}
\to
\text{FIBRE}
\to
\text{LOCAL ID}
\to
\text{GLOBAL ID}
\to
\text{PROTOCOL DESIGN}.
}
\]

But it does **not** make the older scalar/pseudometric

\[
D_{ADEQ}^{cat}(Q;P,Y)
\]

a universal CORE5 primitive or universal canonical definition.

Therefore `V1-GAP-01` is resolved by **downgrading the old metric formula from required foundation to a derived protocol/domain adapter**.

V1 needs the principle that catalog adequacy is checked first and must be typed by the contract. It does not require one universal metric formula.

### Verdict

\[
\boxed{
\mathrm{V1\!-\!GAP\!-\!01=RESOLVED\ BY\ SCOPE\ CORRECTION}.
}
\]

Older `D_ADEQ` formulae remain usable where a pseudometric/loss is explicitly declared.

---

## 5. MINI correction against physical CANON-03

The physical source says gauge is applied in PSI-FACT **if the contract establishes it**.

Therefore the corrected MINI split is consistent:

- fixed coordinate observation `Y=gamma(t)` does not automatically establish external `SE(3)` gauge in the same fibre;
- shape observation `[gamma]_{SE(3)}` can establish that gauge;
- internal normal `SO(2)` remains a presentation gauge of the Bishop frame.

### Verdict

\[
\boxed{\mathrm{C19\!-\!v2\ CANON03\ COMPATIBILITY=PASS}.}
\]

---

## 6. FRAME / higher structure

Physical CANON-03 defines FRAME as a typed contract change and forbids automatic transfer between old and new fibres without explicit transport/commutation conditions.

This supports the existing CLOSED-FRAME discipline.

The physical source does not require a homotopy/groupoid object as a sixth CORE role. Structured/higher candidate or compatibility representations remain legal derived representations when task-relevant.

### Verdict

\[
\boxed{\mathrm{FRAME/HIGHER\ ROLE\ COMPATIBILITY=PASS}.}
\]

---

## 7. DOC-CANON-DRIFT

The physical source itself states that it closes the problem of lacking a current physical canon source.

Therefore for the present repository audit:

\[
\boxed{
\mathrm{CANON03\ SOURCE}=\mathrm{BOUND},
\qquad
\mathrm{DOC\!-\!CANON\!-\!DRIFT\ source\ absence}=\mathrm{CLOSED}.
}
\]

Historical missing originals remain genealogical gaps and must not be represented as recovered.

---

## 8. Freeze consequence

The highest provenance blocker identified by `PROOF-SOURCE-MIGRATION-AUDIT-01` is now closed.

Remaining freeze work is editorial/registry level:

1. update current CAT/FACT claims to the physical CANON-03 definitions;
2. keep the older detailed CAT calculus and FACT groupoid/homotopy layer explicitly derived;
3. decide whether probabilistic bisimulation needs a dedicated C-ID or remains comparison-only;
4. rerun V1/V2 freeze gate.

No CORE change is required.
