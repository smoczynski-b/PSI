# PRINCIPIA — V2 THEOREM MAP 01

**Status:** CURRENT THEOREM / DEPENDENCY MAP — NOT A VOLUME FREEZE  
**Date:** 2026-09-28  
**Canonical target:** `PSI-R3-CONSOLIDATED-CANON-03`  
**Claim source:** `docs/claim-registry-10.md`  
**Regression source:** `docs/regression-bank-01.md`  
**Skeleton source:** `docs/principia-volume-skeleton-02.md`  
**Classical comparison source:** `docs/classical-compare-01.md`

## 0. Purpose

This file maps **Volume II — Theorems and structural bridges** before polished prose.

Every candidate theorem unit is classified by:

`ID | CLASS | STATEMENT | TYPE/DOMAIN | HYPOTHESES | STATUS | SOURCE | DEPENDS ON | USED BY | PROOF STATE | BOUNDARY/FALSIFIER | REGRESSION | DESTINATION`.

The map distinguishes three layers:

1. **self-contained quotient/factorization results** — may be proved directly in V2;
2. **classical bridges** — PSI contribution is the typed reduction/comparison, not ownership of the classical theorem;
3. **benchmarks / pressure witnesses** — may test a theorem but never substitute for one.

A theorem is not `READY FOR FREEZE` merely because its statement is plausible or appears in the Claim Registry.

---

# 1. Dependency spine

The current theorem spine is

\[
\boxed{
C04,C05
\to
C06,C07
\to
C08,C09
\to
\{C10,C13,C18,C32,C37,C42\}
\to
\{C44,C45,C30,C33\}.
}
\]

This is schematic, not a claim that all arrows are logical equivalences.

The critical central node is the factorization/adequacy layer:

\[
\boxed{
\ker_{eq}\rho\subseteq E_{\mathcal T}.
}
\]

HCube, Go, LAZARUS and HIGHER-FIBRE are primarily regressions/applications of this layer, not independent foundations.

---

# 2. II.1 — Elementary quotient and factorization layer

## T2.1 — C06 Exact task-level decidability

- **CLASS:** `THEOREM / elementary quotient fact`
- **STATEMENT:**
  \[
  |q_{\mathcal T}(F(Y))|=1
  \iff
  F(Y)\neq\varnothing
  \land
  F(Y)^2\subseteq E_{\mathcal T}.
  \]
- **TYPE/DOMAIN:** set `Omega`, equivalence relation `E_T`, quotient map `q_T`, compatible subset `F(Y)⊆Omega`.
- **HYPOTHESES:** only well-defined `E_T` and quotient; exact set-level semantics.
- **STATUS:** `CLASSICAL QUOTIENT FACT / ADAPTED CENTRAL CRITERION`.
- **SOURCE:** self-contained proof is sufficient; external attribution optional, not required for validity.
- **DEPENDS ON:** C02, C05.
- **USED BY:** exact local identification statements throughout V2/V3.
- **PROOF STATE:** `READY — elementary proof required in V2`.
- **BOUNDARY:** empty fibre must not count as exact identification.
- **REGRESSION:** `NONE` in Regression Bank 01; retain empty-fibre boundary as local theorem regression.
- **DESTINATION:** `V2 FOUNDATION THEOREM`.

## T2.2 — C07 Kernel factorization criterion

- **CLASS:** `LEMMA / classical elementary factorization`
- **STATEMENT:** for maps `rho:Omega→Z`, `R:Omega→W`,
  \[
  \ker_{eq}\rho\subseteq\ker_{eq}R
  \iff
  \exists!\,g:\operatorname{im}\rho\to W,
  \qquad R=g\circ\rho.
  \]
- **TYPE/DOMAIN:** ordinary sets/maps; uniqueness is on `im rho`.
- **HYPOTHESES:** none beyond the maps being defined on the same domain.
- **STATUS:** `CLASSICAL / ADAPTED`.
- **SOURCE:** direct proof should be included; no novelty claim.
- **DEPENDS ON:** C04.
- **USED BY:** C08, C09, C26, C30, C32, C37, C42, C44 and regression interpretations.
- **PROOF STATE:** `READY — self-contained proof`.
- **BOUNDARY:** do not claim a unique extension of `g` outside `im rho` without extra structure.
- **REGRESSION:** `R01`, `R02` are concrete failures of the kernel inclusion in applications.
- **DESTINATION:** `V2 FOUNDATION LEMMA`.

## T2.3 — C08 Global task sufficiency

- **CLASS:** `THEOREM / PSI bridge`
- **STATEMENT:** with `E_Psi=ker_eq Psi`,
  \[
  E_\Psi\subseteq E_{\mathcal T}
  \iff
  \exists!\,f:\operatorname{im}\Psi\to M_{\mathcal T},
  \qquad q_{\mathcal T}=f\circ\Psi.
  \]
- **TYPE/DOMAIN:** exact deterministic observation map and task quotient.
- **HYPOTHESES:** C05 definitions; ordinary set-valued exact setting.
- **STATUS:** `BRIDGE / CORE`.
- **SOURCE:** direct specialization of T2.2.
- **DEPENDS ON:** C05, C07.
- **USED BY:** global observation sufficiency and protocol design.
- **PROOF STATE:** `READY — corollary proof`.
- **BOUNDARY:** approximate/stochastic sufficiency is not supplied by this theorem.
- **REGRESSION:** `R01/R02` illustrate analogous representation failures but are not direct observation-map counterexamples.
- **DESTINATION:** `V2 THEOREM`.

## T2.4 — C09 Representation adequacy

- **CLASS:** `COROLLARY / BRIDGE`
- **STATEMENT:** representation `rho` is exact-task adequate iff
  \[
  \boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}},
  \]
  equivalently the task quotient factors through `rho` on its image.
- **TYPE/DOMAIN:** exact set-level representation.
- **HYPOTHESES:** C05 + T2.2.
- **STATUS:** `BRIDGE / CORE-ADAPTED`.
- **SOURCE:** direct factorization corollary.
- **DEPENDS ON:** C05, C07.
- **USED BY:** C26, C30–C32, C37, C39, C42, C44 and the complete Regression Bank 01 interpretation.
- **PROOF STATE:** `READY`.
- **BOUNDARY:** exact adequacy is not stability, statistics or computability.
- **REGRESSION:** `R01`, `R02`; `R03` is the explicit boundary showing exact adequacy does not imply stable/statistical inference.
- **DESTINATION:** `V2 CENTRAL COROLLARY`.

## T2.5 — C32/C37 Legal quotient / gauge reduction

- **CLASS:** `COROLLARY / scope theorem`
- **STATEMENT:** a proposed reduction `q:Omega→Z` is exact-task legal only if
  \[
  \boxed{\ker_{eq}q\subseteq E_{\mathcal T}}.
  \]
- **HYPOTHESES:** exact setting; reduction is judged relative to the declared task.
- **STATUS:** `BRIDGE / CORE CLARIFICATION`.
- **SOURCE:** direct specialization of T2.4.
- **DEPENDS ON:** C09.
- **USED BY:** HIGHER-FIBRE, gauge legality, memory compression, future representation reductions.
- **PROOF STATE:** `READY — one-line specialization; discussion needs examples`.
- **BOUNDARY:** not every declared symmetry licenses passage to the coarse orbit set.
- **REGRESSION:** HIGHER-FIBRE fixed witness; R02 for memory compression.
- **DESTINATION:** `V2 COROLLARY`; principle stated earlier in V1.

### II.1 verdict

\[
\boxed{\mathrm{II.1=READY\ FOR\ PROOF\ AUDIT}.}
\]

No mathematical gap is presently visible in the elementary spine.

---

# 3. II.2 — Dynamic and history quotients

## T2.6 — C10 Deterministic quotient dynamics

- **CLASS:** `THEOREM / classical congruence criterion`
- **STATEMENT:** for `delta:Omega→Omega` and equivalence `E`, a unique quotient dynamics
  \[
  \bar\delta:\Omega/E\to\Omega/E,
  \qquad \bar\delta\circ q=q\circ\delta
  \]
  exists iff
  \[
  xEy\Rightarrow\delta(x)E\delta(y).
  \]
- **TYPE/DOMAIN:** deterministic map on a set.
- **HYPOTHESES:** `E` equivalence relation.
- **STATUS:** `CLASSICAL / ADAPTED`.
- **SOURCE:** self-contained proof; classical congruence provenance should be noted.
- **DEPENDS ON:** quotient definition only.
- **USED BY:** task-state update, deterministic abstractions, comparison with stochastic lumpability.
- **PROOF STATE:** `READY`.
- **BOUNDARY:** does not transfer unchanged to stochastic kernels.
- **REGRESSION:** `NONE` in RB01.
- **DESTINATION:** `V2 THEOREM`.

## T2.7 — C42 Exact history-memory adequacy

- **CLASS:** `COROLLARY / history specialization of T2.4`
- **STATEMENT:** for `rho_t:H_t→R_t`,
  \[
  \ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}
  \]
  is exact memory sufficiency.
- **TYPE/DOMAIN:** history space with a declared future-task equivalence.
- **HYPOTHESES:** `≡_{T,t}` must be explicitly defined as an equivalence relation induced by future task semantics.
- **STATUS:** `BRIDGE / REPRESENTATION-ADEQUACY SPECIALIZATION`.
- **SOURCE:** T2.4 + recovered RED-1/Go history construction.
- **DEPENDS ON:** C09 and the history-equivalence definition.
- **USED BY:** C44, C45, Go and LAZARUS.
- **PROOF STATE:** `READY CONDITIONALLY`.
- **BOUNDARY:** current world fibre need not be the full history/task state.
- **REGRESSION:** `R02`.
- **DESTINATION:** `V2 COROLLARY`.

### V2-GAP-01 — history equivalence as a registered definition

The current registry contains C42 but does not give the future-task equivalence `≡_{T,t}` its own current definition ID.

The construction exists in recovered RED-1/Go material, but before freeze it must be either:

1. registered as a current definition; or
2. made an explicit local definition immediately before T2.7 and source-bound to the recovered result.

**Status:** `MIGRATION/REGISTRY GAP`, not a counterexample.

## T2.8 — C44 Coarsest exact history quotient

- **CLASS:** `THEOREM / factorization bridge`
- **STATEMENT:**
  \[
  M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}
  \]
  is the coarsest exact quotient in quotient order: every exact sufficient `rho_t` admits a unique
  \[
  f_t:\operatorname{im}\rho_t\to M_{\mathcal T,t}
  \]
  with
  \[
  q_{\mathcal T,t}=f_t\circ\rho_t.
  \]
- **HYPOTHESES:** explicit history equivalence; exact sufficiency.
- **STATUS:** `CLASSICAL FACTORIZATION + PSI TASK-HISTORY BRIDGE`.
- **SOURCE:** T2.2 specialized to history quotient; recovered RED-1.
- **DEPENDS ON:** C07, C42 / V2-GAP-01 definition.
- **USED BY:** claims of exact minimal history representation.
- **PROOF STATE:** `READY CONDITIONALLY`.
- **BOUNDARY:** no claim of minimum bits, dimension, storage or computational cost.
- **REGRESSION:** `R02` + F42/F43 from falsifier registry.
- **DESTINATION:** `V2 THEOREM`.

## T2.9 — C45 Recursive quotient update

- **CLASS:** `THEOREM / dynamic quotient bridge`
- **STATEMENT:** when history equivalence is a congruence for the declared update,
  \[
  U_{\mathcal T,t}([H_t],\varepsilon_t,y_{t+1})
  =
  [\delta_t(H_t,\varepsilon_t,y_{t+1})]_{\mathcal T,t+1}
  \]
  is well-defined.
- **HYPOTHESES:** precise update domain; congruence/representative-independence; admissible observation/event triple.
- **STATUS:** `BRIDGE / DYNAMIC QUOTIENT RESULT`.
- **SOURCE:** direct quotient well-definedness argument + RED-1.
- **DEPENDS ON:** C10 analogue, C42, explicit update typing.
- **USED BY:** recursive task-state representations.
- **PROOF STATE:** `READY CONDITIONALLY — domain typing must be written explicitly`.
- **BOUNDARY:** mathematical recurrency does not imply finite memory, computability or efficiency.
- **REGRESSION:** `R02`, F43.
- **DESTINATION:** `V2 THEOREM`.

### II.2 verdict

\[
\boxed{\mathrm{II.2=READY\ WITH\ ONE\ REGISTRY\ GAP}.}
\]

---

# 4. II.3 — Classical comparison layer

This chapter must not claim that PSI owns classical equivalence/congruence theory.

## T2.10 — C13 Markov lumpability bridge

- **CLASS:** `CLASSICAL THEOREM + PSI CONDITIONAL BRIDGE`
- **STATEMENT:** a PSI task partition becomes a valid strong-lumpability quotient only when transition mass to every quotient block is constant across representatives:
  \[
  xE_{\mathcal T}y
  \Rightarrow
  P(x,C)=P(y,C)
  \quad\forall C\in\Omega/E_{\mathcal T}.
  \]
- **TYPE/DOMAIN:** finite/discrete Markov chain in the present comparison.
- **HYPOTHESES:** stochastic kernel + block stability.
- **STATUS:** `CLASSICAL CONDITION + PSI BRIDGE`.
- **SOURCE:** Kemeny–Snell / standard lumpability literature; exact edition/page/theorem binding still required.
- **DEPENDS ON:** task equivalence C05; stochastic transition structure.
- **USED BY:** stochastic quotient implementations.
- **PROOF STATE:** `SOURCE-BIND REQUIRED`; no need to re-prove full classical theory if accurately cited.
- **BOUNDARY:** task equivalence alone does not imply lumpability.
- **REGRESSION:** none in RB01.
- **DESTINATION:** `V2 CLASSICAL BRIDGE`.

## T2.11 — C18 Myhill–Nerode exact realization

- **CLASS:** `CLASSICAL REALIZATION / BRIDGE`
- **STATEMENT:** for candidates `u∈Sigma*`, transports by right concatenation and acceptance tests
  \[
  R_w(u)=1_L(uw),
  \]
  PSI task equivalence equals Nerode equivalence:
  \[
  E_{\mathcal T}=\equiv_L.
  \]
- **TYPE/DOMAIN:** formal language `L⊆Sigma*`.
- **HYPOTHESES:** task closure contains all continuation tests `w∈Sigma*`.
- **STATUS:** `CLASSICAL THEOREM + EXACT PSI REALIZATION`.
- **SOURCE:** classical Myhill–Nerode theorem + self-contained equality of the two definitions; precise classical source binding required before freeze.
- **DEPENDS ON:** C03–C05.
- **USED BY:** canonical example of future-test equivalence and coarsest sufficient quotient.
- **PROOF STATE:** `BRIDGE PROOF READY / CLASSICAL SOURCE-BIND REQUIRED`.
- **BOUNDARY:** PSI does not claim the regular-language finite-index theorem.
- **REGRESSION:** conceptual support for R02; not itself a bank regression.
- **DESTINATION:** `V2 CLASSICAL REALIZATION`.

## T2.12 — C14 Paige–Tarjan partition refinement

- **CLASS:** `CLASSICAL ALGORITHMIC BENCHMARK`, not PSI theorem.
- **STATEMENT ROLE:** when a finite PSI problem reduces to a coarsest stable partition problem, established partition-refinement algorithms should be used/compared rather than redescribed as new PSI mathematics.
- **SOURCE:** Paige & Tarjan, SIAM J. Comput. 16(6), 1987, DOI `10.1137/0216062`.
- **DEPENDS ON:** finite-state/stability reduction.
- **PROOF STATE:** `NO PSI PROOF OBLIGATION`; source/bounds must match any complexity claim actually quoted.
- **DESTINATION:** `V2 COMPARISON BOX / V3 IMPLEMENTATION BENCHMARK`.

### V2-GAP-02 — probabilistic bisimulation has no C-ID

`classical-compare-01` contains a typed probabilistic-bisimulation comparison and cites Larsen–Skou (1991), but Claim Registry v10 has no dedicated current claim ID for it.

Therefore it may not enter the first V2 freeze as a registered theorem/bridge until it is either:

- migrated into the Claim Registry after source/hypothesis audit; or
- explicitly left as a non-frozen comparison note.

### II.3 verdict

\[
\boxed{\mathrm{II.3=SOURCE\ AUDIT\ REQUIRED}.}
\]

The mathematics is classical; the blocker is provenance precision and registry synchronization.

---

# 5. II.4 — CAT / FACT / NORM

## V2-GAP-03 — general CAT/FACT definitions are not fully registered

The V2 skeleton requests:

- catalog-change identifiability;
- factorization fibre;
- raw realization versus realization-gauge quotient;
- meta-identifiability of factorization.

The current Claim Registry contains the tested MINI results C19–C20, but not a complete set of dedicated current C-IDs for the general CAT/FACT definitions now expected in V2.

Older sources contain substantial CAT/FACT material, but later typed canon has priority.

Therefore:

\[
\boxed{\text{GENERAL CAT/FACT CHAPTER}=\mathrm{MIGRATION\ REQUIRED}.}
\]

Do not reconstruct it from memory while writing prose.

## T2.13 — C19 CAT–FACT–NORM–MINI interval normal-class result

- **CLASS:** `THEOREM/BRIDGE — MINI`
- **DOMAIN:** exactly observed time-parametrized `C^3` regular curve on compact interval; time reparameterization excluded from gauge.
- **GAUGE:** external `SE(3)` on realization; constant internal `SO(2)` normal-frame presentation.
- **STATEMENT:** every legal finite Frenet/Bishop segmentation reduces to one Bishop normal class; the raw realization family has one factorization class after the declared realization gauge.
- **STATUS:** `BRIDGE / EXACT-NOISELESS MINI`.
- **SOURCE:** `cat-fact-norm-mini-01.md`; Frenet/Bishop ingredients classical.
- **DEPENDS ON:** explicit grammar `{F,B}`, rewrite rules, gauge typing, termination, local confluence, Newman's lemma.
- **USED BY:** C20, CLOSED-FRAME boundary, FS-STAT exact/noisy separation.
- **PROOF STATE:** `PROOF AUDIT REQUIRED`.
- **REASON:** the argument is present, but the freeze should verify each critical-pair claim and bind the exact version/hypotheses of Newman's lemma; this is stronger than merely citing the MINI artifact.
- **BOUNDARY:** loss of regularity, time-reparameterization gauge, closed loops, noisy sampling, reflections.
- **REGRESSION:** CLOSED-FRAME and R03 are external boundary regressions; MINI has its own X1–X5 set.
- **DESTINATION:** `V2 MINI THEOREM`, not general CAT theorem.

## T2.14 — C20 Frenet failure at zero curvature is recode/domain repair under MINI

- **CLASS:** `COROLLARY / CONTRACT-RELATIVE CLASSIFICATION`
- **STATEMENT:** if the curve stays regular while Frenet fails at `kappa=0` and Bishop remains legal, the event is a representation/domain repair rather than catalog birth under MINI-01.
- **DEPENDS ON:** C19 + declared CAT semantics.
- **STATUS:** `BRIDGE / CAT-FRAME BENCHMARK`.
- **PROOF STATE:** `READY ONCE T2.13 PASSES`.
- **BOUNDARY:** not a universal theorem that every representation singularity is non-birth.
- **REGRESSION:** R03 strengthens the statistical boundary: unresolved Frenet condition is not evidence of true zero curvature.
- **DESTINATION:** `V2 COROLLARY / V3 EXAMPLE`.

### II.4 verdict

\[
\boxed{\mathrm{II.4=MINI\ READY\ FOR\ AUDIT;\ GENERAL\ CAT/FACT\ BLOCKED\ BY\ MIGRATION}.}
\]

---

# 6. II.5 — FRAME and transport

## T2.15 — C22 Closed-frame holonomy / periodicity

- **CLASS:** `CLASSICAL GEOMETRY + PSI BRIDGE`
- **DOMAIN:** regular closed oriented curve with normal parallel transport; total-torsion coordinate requires the stronger Frenet-valid subdomain with positive curvature and appropriate periodic Frenet/binormal data.
- **STATEMENT:** normal transport defines return holonomy
  \[
  H_\gamma\in SO(2),
  \]
  and a periodic Bishop/RMF frame exists iff
  \[
  H_\gamma=I.
  \]
  On the stated Frenet-valid subdomain,
  \[
  H_\gamma=R_{-\int\tau ds}
  \]
  up to sign convention, hence periodicity iff total torsion lies in `2pi Z`.
- **STATUS:** `CLASSICAL GEOMETRY + PSI BRIDGE`.
- **SOURCE:** Bishop (1975); Brander–Gravesen (2018); Farouki–Kim–Moon (2020), already listed in CLOSED-FRAME-01.
- **DEPENDS ON:** declared normal transport; MINI only as motivation/boundary.
- **USED BY:** C23, C24; FRAME global/local boundary.
- **PROOF STATE:** `SOURCE/HYPOTHESIS AUDIT REQUIRED` — exact source statement must be matched to the exact periodicity hypotheses used in V2.
- **BOUNDARY:** vanishing curvature invalidates the Frenet coordinate, not necessarily Bishop holonomy.
- **REGRESSION:** CLOSED-FRAME CF-R1–CF-R4.
- **DESTINATION:** `V2 CLASSICAL BRIDGE`.

## T2.16 — C24 Periodic gauge cannot erase nontrivial holonomy

- **CLASS:** `LEMMA / classical gauge fact`
- **STATEMENT:** changing initial normal basis conjugates holonomy; in `SO(2)` conjugation is trivial. A nonperiodic gauge on a cut interval is not a legal periodic gauge on `S^1`.
- **HYPOTHESES:** periodic/single-valued gauge on the closed base.
- **STATUS:** `CLASSICAL / ADAPTED`.
- **SOURCE:** elementary holonomy/gauge argument; can be proved self-contained.
- **DEPENDS ON:** T2.15 definition of return map.
- **USED BY:** C23 and closed-loop normalization discipline.
- **PROOF STATE:** `READY`.
- **REGRESSION:** CF-R3, CF-R4.
- **DESTINATION:** `V2 LEMMA`.

## C23 placement

`C23 — CLOSED-FRAME pressure result: no sixth primitive` is not a mathematical theorem about curves. It is a **pressure/architecture verdict** based on a CORE5 reduction table.

Place as a concluding bridge/policy note after T2.15–T2.16 or in V4/agent genealogy; do not present it as classical geometry.

### II.5 verdict

\[
\boxed{\mathrm{II.5=READY\ WITH\ CLASSICAL\ SOURCE/HYPOTHESIS\ AUDIT}.}
\]

---

# 7. II.6 — Structured / higher compatibility

## T2.17 — C29 `B Z_2` weak-fibre witness

- **CLASS:** `EXACT EXAMPLE / classical groupoid fact`
- **STATEMENT:** for
  \[
  *\to B\mathbb Z_2\leftarrow *,
  \]
  the coarse object-set pullback has one point, while the weak/2-pullback has two witness objects and
  \[
  \left|\pi_0(*\times^h_{B\mathbb Z_2}*)\right|=2.
  \]
- **TYPE/DOMAIN:** small 1-groupoids.
- **STATUS:** `CLASSICAL FACT + PSI BENCHMARK`.
- **SOURCE:** self-contained groupoid calculation is present; classical terminology/provenance should be source-bound before publication.
- **DEPENDS ON:** definition of weak/2-pullback.
- **USED BY:** C30, C33 and quotient-legality examples.
- **PROOF STATE:** `MATHEMATICAL CALCULATION READY / TERMINOLOGY SOURCE-BIND REQUIRED`.
- **REGRESSION:** higher-fibre fixed witness.
- **DESTINATION:** `V2 EXAMPLE/LEMMA`.

## T2.18 — C30 Truncation before fibre may lose task-relevant witness data

- **CLASS:** `COROLLARY / representation-adequacy bridge`
- **STATEMENT:** for witness-sensitive task observable `R_alpha`, the coarse representation of the C29 witness satisfies
  \[
  \ker\rho_{coarse}\not\subseteq\ker R_\alpha.
  \]
- **DEPENDS ON:** C29, C09.
- **STATUS:** `BRIDGE / PRESSURE RESULT`.
- **USED BY:** C32/C37 explanatory examples.
- **PROOF STATE:** `READY`.
- **BOUNDARY:** if the task is witness-invariant, the coarse representation may be adequate.
- **REGRESSION:** fixed BZ2 witness.
- **DESTINATION:** `V2 COROLLARY`.

## T2.19 — C31 Stabilizer-sensitive tasks defeat `pi_0`-only representation

- **CLASS:** `EXACT EXAMPLE / COROLLARY`
- **STATEMENT:** `B1` and `B Z_2` have the same component set but different automorphism groups; therefore `pi_0` alone is insufficient for tasks that distinguish isotropy/stabilizer structure.
- **DEPENDS ON:** C09 and elementary groupoid data.
- **STATUS:** `CLASSICAL STRUCTURE + PSI BRIDGE`.
- **PROOF STATE:** `READY`, subject to terminology/source audit.
- **BOUNDARY:** stabilizers are not automatically task-relevant.
- **DESTINATION:** `V2 EXAMPLE/COROLLARY`.

## C33 placement

`C33 — richer groupoid/homotopy data do not force a sixth CORE role in the tested witness` is a **pressure verdict**, not a universal higher-categorical theorem.

It may close the section as a scoped PSI architectural conclusion, with explicit warning that arbitrary higher dynamics have not been formalized.

### II.6 verdict

\[
\boxed{\mathrm{II.6=MATHEMATICALLY\ READY;\ CLASSICAL\ TERMINOLOGY/SOURCE\ BINDING\ PENDING}.}
\]

---

# 8. II.7 — Representation-insufficiency theorem pattern and regression binding

The hardening bank must not be promoted into three unrelated PSI theorems. Its role is to test T2.4/T2.5 and the exact/stable boundary.

## R01 — HCube

- **Binds to:** T2.4 representation adequacy.
- **Witness:** equal `(characteristic polynomial, operator norm)` but unequal resolvent norm.
- **Function in V2:** exact counterexample box showing `ker rho not subset ker R`.
- **Primary derivation:** V3 / HCube artifact.

## R02 — Go

- **Binds to:** T2.7–T2.9.
- **Function in V2:** finite history-memory counterexamples and boundary on quotient minimality/recursive update.
- **Primary derivation:** V3 / Go artifact.

## R03 — FS-STAT

- **Binds to:** boundary after T2.4, not to exact set-level proof itself.
- **Function:** demonstrates
  \[
  \mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable}.
  \]
- **Primary derivation:** V3 / FS-STAT.

Thus:

\[
\boxed{\text{theorem}\to\text{regression witness},\qquad
\text{not }\text{regression witness}\to\text{theorem status}.}
\]

---

# 9. Current V2 gaps

## V2-GAP-01 — registered history-equivalence definition

Needed for C42/C44/C45 freeze.

## V2-GAP-02 — probabilistic bisimulation registry migration

Comparison exists; current C-ID does not.

## V2-GAP-03 — general CAT/FACT definitions

MINI exists; general current typed definitions are not yet fully represented in Claim Registry v10.

## V2-GAP-04 — classical source binding

Before freeze, bind exact source statements/hypotheses for at least:

- Markov lumpability;
- Myhill–Nerode theorem/context;
- probabilistic bisimulation if migrated;
- Newman lemma as used in MINI;
- Bishop/RMF closed-loop statements;
- weak/2-pullback terminology if kept as a formal theorem unit.

This is a provenance blocker, not evidence that the mathematical statements are false.

## V2-GAP-05 — proof audit for MINI

Check:

- induced rewrite relation is genuinely well-defined modulo the declared gauge;
- listed critical configurations are exhaustive for the finite grammar;
- local confluence statement is sufficient under the exact version of Newman used;
- reconstruction/uniqueness statement does not silently enlarge the contract.

---

# 10. Topological execution order for V2

Do not write V2 in thematic order before dependency order has been checked.

Recommended proof audit order:

\[
\boxed{
T2.1
\to
T2.2
\to
T2.3/T2.4/T2.5
\to
T2.6
\to
T2.7/T2.8/T2.9
\to
T2.10/T2.11
\to
T2.13/T2.14
\to
T2.15/T2.16
\to
T2.17/T2.18/T2.19.
}
\]

Classical comparison boxes and benchmarks are inserted only after the theorem they compare/test is stable.

---

# 11. Freeze assessment

Current status by section:

| Section | Status |
|---|---|
| II.1 elementary quotient/factorization | `READY FOR PROOF AUDIT` |
| II.2 dynamics/history | `READY WITH REGISTRY GAP` |
| II.3 classical comparisons | `SOURCE AUDIT REQUIRED` |
| II.4 CAT/FACT/NORM | `MINI READY; GENERAL CAT/FACT MIGRATION REQUIRED` |
| II.5 FRAME | `SOURCE/HYPOTHESIS AUDIT REQUIRED` |
| II.6 higher compatibility | `MATH READY; TERMINOLOGY/SOURCE AUDIT REQUIRED` |
| II.7 regression binding | `READY` |

Therefore

\[
\boxed{\mathrm{V2\ FREEZE}=\mathrm{NOT\ YET}.}
\]

The next legal phase is not prose. It is a combined

\[
\boxed{\mathrm{PROOF/SOURCE/MIGRATION\ AUDIT\ 01}.}
\]

This audit should resolve V1-GAP-01 together with V2-GAP-01…05 before the first V1/V2 freeze.