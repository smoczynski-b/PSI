# PRINCIPIA — V1 UNIT MAP 01

**Status:** CURRENT EDITORIAL / DEPENDENCY MAP — NOT A VOLUME FREEZE  
**Date:** 2026-09-28  
**Canonical target:** `PSI-R3-CONSOLIDATED-CANON-03`  
**Claim source:** `docs/claim-registry-10.md`  
**Regression source:** `docs/regression-bank-01.md`  
**Skeleton source:** `docs/principia-volume-skeleton-02.md`  
**Migration source:** `docs/principia-migration-01.md`

## 0. Purpose

This file is the first structural map of **Volume I — Foundations**.

It is deliberately not chapter prose. It answers:

\[
\boxed{
\text{what belongs in V1}
\mid
\text{what class of statement it is}
\mid
\text{what it depends on}
\mid
\text{what depends on it}
\mid
\text{what tests/bounds it}.
}
\]

A unit may enter prose only after its unresolved `SOURCE / PROOF / MIGRATION` gates are cleared.

---

# 1. Statement classes

Volume I must not flatten every registered item into the word `claim`.

Use the classes:

- `DEFINITION` — introduces an object/type/role; no proof obligation beyond consistency and typing;
- `CLASSICAL-DEFINITION` — imported standard definition;
- `THEOREM/LEMMA` — proposition with proof obligation;
- `BRIDGE` — consequence/translation between PSI architecture and an imported or elementary theorem;
- `POLICY` — methodological or project-governance rule; not a mathematical theorem;
- `BOUNDARY` — counterexample/impossibility/scope restriction;
- `BENCHMARK` — reproducible laboratory witness;
- `OPEN` — unresolved statement or construction;
- `SOURCE-ONLY` — relevant older source material not yet migrated to the current claim registry.

Status and role remain separate.

---

# 2. V1 inclusion levels

Every item receives one of:

- `FOUNDATION` — belongs in the main mathematical exposition of V1;
- `PRINCIPLE` — belongs in V1 as discipline/interpretive rule;
- `BOUNDARY-BOX` — may appear as a short warning/example, with full derivation elsewhere;
- `CROSS-REFERENCE` — used by V1 but proved/developed in V2/V3;
- `DEFER` — should not enter V1 main text;
- `MIGRATION-GAP` — source exists but current registry migration is incomplete.

---

# 3. Unit I.1 — Contract and semantic roles

## Purpose

State what kind of mathematical problem PSI is before constructing fibres or quotients.

### I.1.A — C01

- **CLASS:** `DEFINITION`
- **ROLE:** contract-relative CORE architecture
- **STATEMENT:**
  \[
  \mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
  \]
- **TYPE:** typed tuple of candidate class, observation, compatibility, task observables and admissible dynamics/transport under contract `c`.
- **STATUS:** `PSI-NEW architecture / CORE`
- **SOURCE:** current CANON-03 / Claim Registry C01.
- **DEPENDS ON:** none inside current registry; typing conventions supplied by contract `c`.
- **USED BY:** C02, C03, C05, C08, C09, C10, C19–C33, C34–C37, C42 and all domain realizations.
- **FALSIFIER/BOUNDARY:** semantic-role confusion; candidate stuffing; silent contract change.
- **REGRESSION:** `NONE` in Regression Bank 01; governed by R4 pressure tests / candidate-stuffing no-go.
- **V1:** `FOUNDATION`.

### I.1.B — gauge declaration versus gauge legality

V1 must distinguish:

\[
\boxed{
\text{declared symmetry/gauge}
\neq
\text{licensed coarse quotient}.
}
\]

The contract may declare a candidate equivalence here, but the exact legality criterion is not available until task equivalence has been defined in I.3.

Therefore C32/C37 are **not proved in I.1**. They are forward references to I.3/Volume II.

### Unit verdict

\[
\boxed{I.1=\mathrm{READY}.}
\]

No missing mathematical object was found.

---

# 4. Unit I.2 — Observation, compatible fibre and catalog adequacy

## Purpose

Separate data from hidden candidates and require catalog adequacy before identification.

### I.2.A — C02

- **CLASS:** `DEFINITION + classical set operation`
- **STATEMENT:**
  \[
  F_c(Y)=\Psi_c^{-1}(\mathcal K_c^Y).
  \]
- **STATUS:** `PSI-NEW role / CORE`.
- **DEPENDS ON:** C01.
- **USED BY:** C06, C08, all local/global identifiability statements, LAZARUS/FACT realizations.
- **BOUNDARY:** `Y` is not an identified hidden object; a selected representative requires an additional rule.
- **REGRESSION:** `NONE`.
- **V1:** `FOUNDATION`.

### I.2.B — C11

- **CLASS:** `POLICY`
- **STATEMENT:**
  \[
  \boxed{
  \text{catalog adequacy}
  \to
  \text{fibre}
  \to
  \text{local identifiability}
  \to
  \text{global identifiability}
  \to
  \text{protocol design}.
  }
  \]
- **STATUS:** `CORE discipline`.
- **DEPENDS ON:** semantic distinction between candidate catalog and observation problem.
- **USED BY:** redaction order and all laboratory protocols.
- **V1:** `PRINCIPLE`.

### I.2.C — V1-GAP-01: formal catalog adequacy definition

A recoverable older source contains the typed construction:

\[
D_{\rm ADEQ}^{beh}(\mathcal B;P,Y)
=
\inf_{b\in\mathcal B}d_{\mathcal Y}(\operatorname{Obs}_P(b),Y),
\]

\[
D_{\rm ADEQ}^{cat}(Q;P,Y)
=
D_{\rm ADEQ}^{beh}(\widetilde{\mathcal B}^{P}_{Q};P,Y),
\]

and the condition

\[
Q\text{ adequate under the declared contract}
\iff
D_{\rm ADEQ}^{cat}(Q;P,Y)\le\varepsilon.
\]

**Source:** `PRINCIPIA_SEMANTICA_KANON_SCALONY_2026-07-26A`, section `PSI-CAT: adekwatność katalogu`.

However this definition is **not currently represented by a dedicated C-ID in Claim Registry v10** and predates CANON-03.

Therefore:

\[
\boxed{
\mathrm{SOURCE\ FOUND}
\to
\mathrm{MIGRATION/AUDIT\ REQUIRED},
}
\]

not automatic promotion.

- **CLASS:** `SOURCE-ONLY`.
- **V1:** `MIGRATION-GAP`.
- **NEXT GATE:** check typing against CANON-03 and decide whether it becomes a current definition, a domain adapter, or remains genealogy.

### I.2.D — representation is not represented object

Migration Registry preserves this as a methodological restriction inherited from Integrata and compatible with current PSI.

- **CLASS:** `PRINCIPLE / migrated source discipline`.
- **V1:** `PRINCIPLE`.

### Unit verdict

\[
\boxed{I.2=\mathrm{READY\ WITH\ ONE\ MIGRATION\ GAP}.}
\]

`V1-GAP-01` is the only blocker before freeze, not before continuing the map.

---

# 5. Unit I.3 — Task-relative distinction and legal reduction

## Purpose

Construct task equivalence and state the exact criterion for whether a representation/quotient is allowed to forget a distinction.

### I.3.A — C03

- **CLASS:** `DEFINITION`
- **STATEMENT:**
  \[
  \mathscr R_{\mathcal T,c}
  =\operatorname{Cl}^{\mathcal T}_{\delta_c}(\mathscr O_{\mathcal T,c}).
  \]
- **STATUS:** `PSI-NEW architecture / CORE`.
- **DEPENDS ON:** C01.
- **USED BY:** C05, C06, C08, C09.
- **BOUNDARY:** closure operations/transports must be stated by the contract; the symbol is not an unspecified-dynamics license.
- **V1:** `FOUNDATION`.

### I.3.B — C04

- **CLASS:** `CLASSICAL-DEFINITION`
- **STATEMENT:**
  \[
  \ker_{eq}R=\{(x,y):R(x)=R(y)\}.
  \]
- **STATUS:** `CLASSICAL / ADAPTED`.
- **DEPENDS ON:** none.
- **USED BY:** C05–C10, C32, C37, C42 and Regression Bank.
- **V1:** `FOUNDATION`.

### I.3.C — C05

- **CLASS:** `DEFINITION using classical quotient machinery`
- **STATEMENT:**
  \[
  E_{\mathcal T,c}
  =\bigcap_{R\in\mathscr R_{\mathcal T,c}}\ker_{eq}R,
  \qquad
  M_{\mathcal T,c}=\Omega_c/E_{\mathcal T,c}.
  \]
- **STATUS:** `PSI-NEW architecture / CORE`.
- **DEPENDS ON:** C01, C03, C04.
- **USED BY:** C06, C08, C09, C32, C37, history analogues.
- **V1:** `FOUNDATION`.

### I.3.D — C09

- **CLASS:** `BRIDGE`
- **STATEMENT:**
  \[
  \boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}}
  \]
  is the exact task-adequacy criterion for a representation `rho`.
- **STATUS:** `BRIDGE / CORE-ADAPTED`.
- **DEPENDS ON:** C05 and the factorization criterion C07.
- **USED BY:** C26, C30, C32, C37, C39, C42 and all three hardening regressions conceptually.
- **PROOF:** deferred to V2 with C07.
- **REGRESSION:** `R01`, `R02`; `R03` concerns an additional stability/statistical layer rather than exact set-level adequacy.
- **V1:** `PRINCIPLE + CROSS-REFERENCE`; full theorem in V2.

### I.3.E — C32

- **CLASS:** `BRIDGE / specialization of C09`
- **STATEMENT:** for a proposed gauge/truncation/reduction map `q_G`,
  \[
  \boxed{\ker_{eq}q_G\subseteq E_{\mathcal T}}.
  \]
- **DEPENDS ON:** C09.
- **USED BY:** C33, higher-fibre interpretation, future gauge/truncation claims.
- **BOUNDARY:** coarse orbit/component reduction can be illegal when stabilizers or compatibility witnesses remain task-relevant.
- **V1:** `FOUNDATION PRINCIPLE`; derivation in V2.

### I.3.F — C37

- **CLASS:** `BRIDGE / scope clarification`
- **ROLE:** extends C32 explicitly across realization gauge, representation reduction, coarse truncation and memory compression.
- **DEPENDS ON:** C09, C32.
- **USED BY:** redaction discipline and future reductions.
- **V1:** `PRINCIPLE`, consolidated with C32 rather than repeated as a second theorem.

### Unit verdict

\[
\boxed{I.3=\mathrm{READY}.}
\]

Editorial correction: C32/C37 belong logically **after** task equivalence, not before it.

---

# 6. Unit I.4 — History, memory and future-task semantics

## Purpose

Show why the current observable/world fibre need not be a sufficient task state when future legality/action depends on history.

### I.4.A — C42

- **CLASS:** `BRIDGE / specialization of C09`
- **STATEMENT:** for
  \[
  \rho_t:\mathcal H_t\to R_t,
  \]
  exact memory sufficiency is
  \[
  \boxed{\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.}
  \]
- **DEPENDS ON:** C09 plus the definition of future-task equivalence on histories.
- **USED BY:** C44, C45, C46, Go regression R02 and LAZARUS memory analysis.
- **PROOF:** V2.
- **REGRESSION:** `R02`.
- **V1:** `FOUNDATION PRINCIPLE / CROSS-REFERENCE`.

### I.4.B — C25

- **CLASS:** `BOUNDARY / BRIDGE`
- **STATEMENT:** equal current world-state fibres do not imply equal future task agency/semantics.
- **DEPENDS ON:** history/task distinction; LAZARUS D2.
- **USED BY:** motivates C26/C42 and prevents `current fibre = full task information`.
- **REGRESSION:** conceptually aligned with R02, but the fixed witness is LAZARUS rather than Go.
- **V1:** `BOUNDARY-BOX` only.

### I.4.C — C26

- **CLASS:** `BRIDGE / factorization consequence`
- **STATEMENT:** `rho_F(H)=F_t(H)` can fail task adequacy when
  \[
  \ker\rho_F\not\subseteq\equiv_{\mathcal T,t}.
  \]
- **DEPENDS ON:** C09/C42 and C25 witness.
- **USED BY:** LAZARUS V3.
- **V1:** `BOUNDARY-BOX`; proof/example in V3.

### I.4.D — C27

- **CLASS:** `BOUNDARY / pressure result`
- **STATEMENT:** separate world/operational marginals can lose task-relevant correlation.
- **SOURCE:** LAZARUS D3.
- **USED BY:** joint-state representation discipline.
- **V1:** `BOUNDARY-BOX`, not a new state primitive.

### I.4.E — items deferred from V1

- C43 Go ladder → `V3 BENCHMARK`;
- C44 coarsest exact history quotient → `V2 THEOREM/BRIDGE`;
- C45 recursive quotient update → `V2 BRIDGE`;
- C46 task-relative Go representation change → `V3 BENCHMARK/POLICY`;
- C47 G1 source gap → `V3/V4 provenance note`.

### Unit verdict

\[
\boxed{I.4=\mathrm{READY}.}
\]

V1 contains the **principle and boundary**, not the full Go/Lazarus laboratories.

---

# 7. Unit I.5 — Exact identification, stability and statistical licensing

## Purpose

Prevent exact uniqueness from being silently upgraded into perturbation stability or statistical confidence.

### I.5.A — C51

- **CLASS:** `POLICY / inference discipline`
- **CORRECT FORM:**
  \[
  \boxed{
  \mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
  \qquad
  \mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
  }
  \]
- **NOTE:** use non-implication, not literal inequality between three differently typed notions.
- **EVIDENCE:** FS-STAT / R03.
- **USED BY:** all future statistical/noisy extensions.
- **REGRESSION:** `R03`.
- **V1:** `PRINCIPLE`.

### I.5.B — C52

- **CLASS:** `POLICY / classical statistical discipline`
- **STATEMENT:** deterministic bounded noise does not license frequentist confidence coverage; a confidence statement requires an explicit probability model and its assumptions.
- **DEPENDS ON:** probability semantics, not on a new PSI theorem.
- **USED BY:** C53–C55 and all PSI-STAT modules.
- **REGRESSION:** `R03`.
- **V1:** `PRINCIPLE`.

### I.5.C — `UNRESOLVED` as legal output

When the protocol cannot certify the condition required for an inference, the output is allowed to remain `UNRESOLVED`. Failure to identify is not identification of a null value.

This principle is supported in FS-STAT by the Frenet/Bishop gate and more generally by PSI fibre semantics.

- **CLASS:** `PRINCIPLE`.
- **V1:** `FOUNDATION DISCIPLINE`.

### I.5.D — items explicitly deferred

The following do **not** become V1 foundations:

- C48 finite-difference error bounds → V3/technical appendix;
- C49 low-curvature torsion witness → V3 / R03;
- C50 uncertainty-driven Frenet/Bishop gate → V3;
- C53 local polynomial estimator layer → V3/classical source binding;
- C54 global flatness test boundary → V3/OPEN;
- C55 quotient confidence → V2/V3 OPEN bridge;
- C56 FS-STAT hardening verdict → project/lab status.

### Unit verdict

\[
\boxed{I.5=\mathrm{READY}.}
\]

This is an epistemic-level unit, not a statistics chapter.

---

# 8. Unit I.6 — Methodological boundaries and primitive discipline

## Purpose

State what PSI is not allowed to infer merely from successful representation, attractive analogy or current absence of counterexamples.

### I.6.A — C12

- **CLASS:** `POLICY`
- **STATEMENT:** a new primitive is admitted only when a counterexample forces a genuinely new semantic role.
- **DEPENDS ON:** C01 semantic-role architecture.
- **USED BY:** R4 gate / C36.
- **V1:** `PRINCIPLE`.

### I.6.B — C35

- **CLASS:** `POLICY / anti-tautology`
- **STATEMENT:** arbitrary candidate stuffing is not a legal proof of CORE sufficiency; reductions must preserve semantic roles.
- **DEPENDS ON:** C01 and R4 pressure analysis.
- **USED BY:** future R4 tests and candidate-enrichment arguments.
- **V1:** `PRINCIPLE`.

### I.6.C — C36

- **CLASS:** `PROJECT POLICY / FREEZE`, not a timeless mathematical theorem.
- **STATEMENT:** current primitive growth is stopped until a new typed witness passes the R4 admission test.
- **DEPENDS ON:** C34, C35, C12.
- **USED BY:** current project frontier.
- **V1:** `CROSS-REFERENCE / editorial note`, not an axiom of PSI.

### I.6.D — C34

- **CLASS:** `PRESSURE RESULT / BENCHMARK`
- **STATEMENT:** no current pressure witness forced R4.
- **SCOPE:** current counterexample set only.
- **V1:** `DEFER` from mathematical foundations; provenance may be cited in an editorial note or V4.

### I.6.E — source/provenance discipline

Migration Registry and Source Governance supply:

\[
\boxed{
\text{representation}\neq\text{represented object},
\qquad
\text{claim status}\neq\text{role},
\qquad
\text{unrecoverable provenance}=\text{unstable editorial state}.
}
\]

These are governance/methodological restrictions, not new mathematical primitives.

### Unit verdict

\[
\boxed{I.6=\mathrm{READY}.}
\]

---

# 9. Dependency graph — V1 backbone

The minimal forward graph is:

\[
\boxed{
C01
\to
\{C02,C03\},
}
\]

\[
\boxed{
(C03,C04)\to C05,
}
\]

\[
\boxed{
(C05,C07)\to C09\to C32\to C37,
}
\]

\[
\boxed{
C09\to C42\to\{C44,C45\},
}
\]

and the primitive-governance branch is

\[
\boxed{
C01+C12+C35+C34\to C36
}
\]

with C34 used only as current evidence, not as a universal theorem.

The inference-quality branch is logically separate:

\[
\boxed{
R03/C49\to C51,
\qquad
\text{probability contract discipline}\to C52.
}
\]

No edge is intended from `exact task adequacy` directly to statistical confidence.

---

# 10. Blast-radius / USED-BY index

| Upstream item | Principal downstream use |
|---|---|
| C01 | almost all current PSI modules; changing a semantic role has maximal blast radius |
| C02 | exact decidability, global sufficiency, FACT/Lazarus observation fibres |
| C03 | task equivalence and all dynamics/transport-sensitive tasks |
| C04 | quotient/equivalence/factorization machinery |
| C05 | C06, C08, C09, legal reduction/gauge tests |
| C09 | C26, C30, C32, C37, C39, C42, R01/R02 interpretation |
| C32 | higher-fibre, gauge/truncation legality, future structured quotients |
| C42 | C44, C45, Go and history-dependent agent/state work |
| C51 | every noisy/stability claim; FS-STAT and future PSI-STAT |
| C52 | every frequentist confidence claim in PSI-STAT |
| C12/C35 | every future R4/primitive-growth proposal |

This table is the initial blast-radius graph. It must be expanded rather than replaced by prose.

---

# 11. Regression binding for V1

| V1 unit | Regression binding | Meaning |
|---|---|---|
| I.1 Contract/roles | `NONE` in Bank 01 | pressure/R4 falsifiers remain external |
| I.2 Observation/fibre/catalog | `NONE` | catalog adequacy migration gap remains |
| I.3 Task distinction/reduction | `R01`, `R02` | representation adequacy tested in operator and history domains |
| I.4 History/memory | `R02` | fixed Go memory ladder; LAZARUS as additional non-bank witness |
| I.5 Exact/stable/confidence | `R03` | fixed geometric/statistical conditioning witness |
| I.6 Methodological boundaries | `NONE` | governed by R4 court / no-go history |

Do not attach a regression merely for symmetry. `NONE` is a legal explicit value.

---

# 12. V1 gaps before freeze

## V1-GAP-01 — catalog adequacy migration

**State:** SOURCE FOUND / NOT YET CURRENT CLAIM.

Required action:

1. compare the 2026-07-26A `D_ADEQ^cat` definition against CANON-03 typing;
2. decide whether it is universal V1 definition or a protocol/domain adapter;
3. if accepted, assign current claim ID and source status;
4. if not, state the replacement current definition explicitly.

## V1-GAP-02 — exact source binding for imported fundamentals

Before freeze, V1 needs explicit source/provenance binding for the classical pieces it actually invokes:

- equivalence kernels / quotient factorization;
- probability/confidence semantics where discussed;
- any imported definition used in catalog adequacy.

This is editorial/source work, not a new mathematics problem.

## V1-GAP-03 — proof placement boundary

C09 and C42 should be **stated** in V1 but proved/derived in V2. The final redaction must prevent duplicated proofs and prevent a V1 principle from acquiring theorem status merely by repetition.

---

# 13. Redaction verdict

The first Volume-I dependency scan gives:

\[
\boxed{
I.1=READY,
\ I.2=READY\ WITH\ GAP,
\ I.3=READY,
\ I.4=READY,
\ I.5=READY,
\ I.6=READY.
}
\]

but

\[
\boxed{\mathrm{V1\ FREEZE}=\mathrm{NOT\ YET}.}
\]

The blockers are source/migration/proof-placement tasks, not new primitive mathematics.

---

# 14. Next legal step

The next map is:

\[
\boxed{\mathrm{V2\!-\!THEOREM\!-\!MAP\!-01}.}
\]

It must classify every V2 unit as

`CLASSICAL | BRIDGE | PSI-NEW | BENCHMARK | OPEN`,

bind exact hypotheses/proofs/sources, and expose the dependency direction back to this V1 map.

Only after V1 + V2 maps exist should `PROOF-AUDIT-01` begin.