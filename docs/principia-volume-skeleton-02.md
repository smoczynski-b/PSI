# PRINCIPIA — four-volume skeleton 02

**Status:** CURRENT EDITORIAL SKELETON / V1-V2 FIRST FREEZE BOUND  
**Canonical source:** physical `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Current claim source:** `docs/claim-registry-12.md`  
**Current falsifier source:** `docs/falsifier-registry-11.md`  
**Current regression source:** `docs/regression-bank-01.md`  
**Freeze source:** `docs/principia-v1-v2-freeze-01.md`  
**Migration source:** `docs/principia-migration-01.md`

This supersedes `principia-volume-skeleton-01.md` operationally. The earlier skeleton remains historical evidence.

The redaction rule is:

\[
\boxed{
\text{PHYSICAL CANON-03}
\to
\text{Claim Registry}
\to
\text{proof/source/regression freeze}
\to
\text{Volume unit}
\to
\text{prose}.
}
\]

The first V1/V2 mathematical-source freeze has passed. Polished prose is legal **only inside the frozen semantic boundaries**.

---

## Volume I — Foundations

Purpose: define the PSI problem, its types, inference discipline and epistemic boundaries before derived theorems.

### I.1 Contract and semantic roles

- candidate space `Ω_c`;
- observation map `Ψ_c`;
- typed compatibility `K_c`;
- task observables `O_{T,c}`;
- admissible dynamics / transports `δ_c`;
- contract-relative gauge.

Required current claims: `C01–C05`, `C35`, `C60`, `C61`.

Do **not** state `ker q⊆E_T` as the whole legality contract. It is the exact task-information adequacy gate; full legality can additionally require typing, admissible action/gauge, observation compatibility/equivariance and domain constraints.

### I.2 Observation, fibre and catalog adequacy

- observation is not the hidden object;
- compatible fibre `F(Y)`;
- catalog adequacy precedes identification;
- class before representative;
- no universal scalar `D_ADEQ^cat` is part of CORE5.

Required current claims: `C02`, `C11`, `C62`, `C64`.

Older metric/loss forms of `D_ADEQ` are typed adapters and may appear as examples, not as the universal foundation.

### I.3 Task-relative distinction

- task closure;
- exact kernels;
- task equivalence;
- task quotient;
- representation adequacy;
- task-adequate reduction versus fully contract-legal reduction.

Required claims: `C03–C05`, `C09`, `C32`, `C37`, `C60`.

### I.4 History and memory

- history space `H_t`;
- future task tree `Beh_T(H)`;
- future-task equivalence `≡_{T,t}` — `C57`;
- exact memory sufficiency `ker ρ_t⊆≡_{T,t}` — `C42`;
- distinction between current world fibre and full task state.

Boundary claims/examples: `C25–C27`.

Regression binding: `R02`.

### I.5 Exactness, stability and statistical licensing

Permanent discipline:

\[
\boxed{
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
}
\]

- exact uniqueness;
- perturbation stability;
- confidence only under a probability contract;
- `UNRESOLVED` as a legal output.

Foundation claims: `C51`, `C52`, `C56` as discipline/boundary.

Technical claims `C48–C50`, `C53–C55` belong to V2/V3 technical development, not the foundational spine.

Regression binding: `R03`.

### I.6 Methodological boundaries

Freeze:

- `REPRESENTATION != WORLD`;
- `UNOBSERVED != ZERO`;
- `PSI-ID != PSI-CAT`;
- realization equivalence != behavioural recoding;
- source/provenance requirements;
- status != role;
- primitive-growth freeze;
- candidate stuffing is not a legal sufficiency proof;
- geometric symmetry is not automatically a gauge of a fixed observed fibre.

Required claims: `C12`, `C34–C36`, `C61–C65` as provenance/scope controls.

---

## Volume II — Theorems and structural bridges

Purpose: collect typed propositions with hypotheses, proofs, provenance and applicable regressions.

Every theorem unit must contain:

`ID | statement | type/domain | hypotheses | status | source | proof/derivation | falsifier/boundary | regression IDs | dependencies | used-by`.

### II.1 Elementary quotient/factorization layer

- exact task-level decidability — `C06`;
- factorization criterion — `C07`;
- global task sufficiency — `C08`;
- representation adequacy — `C09`;
- task-information legality of quotient/gauge — `C32`, `C37`;
- scope correction to full contract legality — `C60`.

### II.2 Dynamic and history quotients

- deterministic quotient dynamics — `C10`;
- future-task equivalence definition/theorem — `C57`, `C58`;
- memory/history adequacy — `C42`;
- coarsest exact history quotient — `C44`;
- congruence/recursive update — `C59`, `C45`;
- explicit limits: no bit/compute minimality without separate proof.

Regression binding: `R02`.

### II.3 Classical comparison

Freeze only the comparisons needed by current theorem architecture:

- deterministic congruence;
- Markov strong/Kemeny–Snell lumpability bridge — `C13`, prose unit `II.10`, `PASS`;
- Nerode exact realization — `C18`, next prose unit `II.11`;
- Paige–Tarjan benchmark — `C14`.

Permanent stochastic boundary:

\[
\boxed{
\text{task quotient}
\not\Rightarrow
\text{Markov lumpability}
}
\]

without block-transition stability; regression `F61`.

Probabilistic bisimulation remains explanatory comparison-only; it has no current C-ID because no frozen theorem depends on it.

No originality claim for classical theorems.

### II.4 CAT / FACT / NORM

Current canonical definitions:

- PSI-CAT — `C62`;
- PSI-FACT — `C63`;
- realization-equivalence versus behavioural recoding — `C63`;
- corrected CAT–FACT–NORM–MINI — `C19-v2`, `C20`.

Derived, not universal:

- older `ISO/HOR/REF/CRS` CAT calculus;
- `GEN/TEST/SELECT` workflow;
- factorization groupoid / homotopy compatibility fibre — `C66`;
- scalar catalog-adequacy metrics — `C64` adapter status.

Never replace C19-v2 by the pre-audit mixed `Y=gamma(t)` + `SE(3)` quotient formulation.

### II.5 FRAME / transport

- frame change as typed contract/transport;
- closed-frame holonomy — `C22–C24`;
- return holonomy is primary; total torsion is a coordinate only under stronger Frenet-valid hypotheses;
- local trivialization does not imply global periodic representative.

### II.6 Structured / higher compatibility

- `B Z_2` witness — `C29`;
- truncation-order failure — `C30`;
- stabilizer sensitivity — `C31`;
- richer representation does not imply new semantic primitive — `C33`.

Do not state that all PSI-FACT fibres are homotopy fibres.

### II.7 Representation insufficiency theorem patterns

Use the hardening bank as examples attached to general criteria, not as theorem substitutes:

- operator representation inadequacy — `R01`;
- history/memory inadequacy — `R02`;
- exact/stable statistical boundary — `R03`.

---

## Volume III — Realizations / Models / Laboratories

Purpose: concrete contracts and reproducible demonstrations. Laboratory PASS does not promote a theorem into Volume II.

1. PHISICA / operator laboratories;
2. HCube — `R01`, separator/benchmark only;
3. LAZARUS — task state, execution and representation adequacy;
4. Go — `R02`, memory/history regression;
5. FS/Bishop and FS-STAT — `R03`;
6. Agents — Agent SPEC != LIVE state, handoff, regression preservation;
7. PSI-FORUM;
8. cultural laboratories;
9. SOP / genomic `Lambda`;
10. OPEN-PSI / public experiment.

For OPEN-PSI use the measured quantity names exactly:

\[
\boxed{\text{aggregate outbound research clicks}}
\]

not `confirmed transitions` or destination arrivals unless separately instrumented.

---

## Volume IV — Genealogy

Purpose: preserve intellectual and project history without contaminating current theorem status.

1. mathematical lineage;
2. Analiza semantyczna dialektyczna / Model psi;
3. multimodal psi;
4. TAO/SMOK and STPpsi/GTPpsi;
5. LOGOS / Integrata / Universalia;
6. superseded claims with reasons and counterexamples;
7. experimental genealogy;
8. agent/model genealogy and correction history.

Rule:

\[
\boxed{\text{superseded}\neq\text{erased}.}
\]

---

## Redaction gates after first freeze

Before prose for any V1/V2 unit require:

1. current `CLAIM ID` or explicit definition label;
2. `TYPE` — object/domain/codomain/contract;
3. `STATUS` — classical/bridge/new/policy/open;
4. `SOURCE` — physical canon, classical source or declared derivation;
5. `PROOF/DERIVATION` — appropriate to claim class;
6. `BOUNDARY/FALSIFIER` — explicit;
7. `REGRESSION` — applicable `Rxx/Fxx` or explicit `NONE`;
8. `DEPENDENCIES` and `USED BY`;
9. `NO-GO` — rejected nearby formulations when relevant;
10. no semantic deviation from `principia-v1-v2-freeze-01.md` without an erratum/impact audit.

---

## Current execution order

The structural freeze stage is complete. Current prose state is

\[
\boxed{
\mathrm{V1\ NORMALIZED\ PASS}
\to
\mathrm{V2.1:V2.9\ GLOBAL\ PASS}
\to
\mathrm{II.10\ LUMPABILITY\ PASS}
\to
\mathrm{II.11\ MYHILL\!\!-\!NERODE\ NEXT}.
}
\]

Continue through frozen units using

\[
\boxed{
\text{FROZEN UNIT}
\to
\text{CHAPTER PROSE}
\to
\text{REDUCTION / CROSS-CHECK}
}
\]

without reopening primitive discovery.

PHISICA/LOGOS migration resumes after the first V1/V2 prose pass unless a frozen theorem unit requires a precise source bridge sooner.
