# PSI — claim registry 12

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-11.md` as current public registry  
**Canonical source:** physical `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0, commit `7e64ec8ad766623ffeede3daa4bb68dee15135c1`

This version closes the CANON-03 provenance bind, records the current canonical CAT/FACT definitions, and resolves the former catalog-adequacy migration gap by scope correction.

## Retained claims

Retain C01–C61 from `claim-registry-11.md`, including corrected C19-v2 and RED-1 C57–C59.

---

## C62 — current canonical PSI-CAT definition

`PSI-CAT` asks whether the data and protocol justify a change of the candidate catalog and, if so, which class of changes is justified.

`PSI-CAT^D` adds domain-admissibility conditions `ADM_D`.

Domain restrictions can eliminate inadmissible hypotheses but are not themselves new empirical observations.

The current physical canon freezes

\[
\boxed{\mathrm{PSI-ID}\neq\mathrm{PSI-CAT}.}
\]

`PSI-ID` concerns identifiability inside a fixed catalog; `PSI-CAT` concerns justification for changing that catalog.

**STATUS:** `CANONICAL DEFINITION / PHYSICAL CANON-03`  
**ROLE:** `DERIVED META-IDENTIFICATION MODULE, NOT CORE6`.

The older `ISO/HOR/REF/CRS` and `GEN/TEST/SELECT` calculi remain compatible derived machinery, not the minimal current definition.

---

## C63 — current canonical PSI-FACT definition

For realization domain `D`, protocol `P`, tolerance `epsilon` and data `Y`, `PSI-FACT` studies

\[
\boxed{\operatorname{Fact}^{\varepsilon}_{D,P}(Y),}
\]

the fibre of factorizations compatible with observation and protocol.

Objects must satisfy:

- `ADM_D`;
- the declared external interface;
- the declared data-compatibility criterion.

Realization gauge is quotiented **if the contract establishes it**.

The physical canon distinguishes:

\[
\boxed{
\text{realization equivalence}
\neq
\text{behavioural recoding}.
}
\]

A one-way behavioural recoding need not be an equivalence.

**STATUS:** `CANONICAL DEFINITION / PHYSICAL CANON-03`  
**ROLE:** `DERIVED FACTORIZATION IDENTIFIABILITY MODULE`.

The older factorization groupoid / homotopy-ADEQ fibre remains a derived structured extension when stabilizers or compatibility witnesses are task-relevant; it is not the universal minimal definition of current PSI-FACT.

---

## C64 — catalog adequacy is a prior gate, not one universal metric

The physical canon freezes the logical order

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

It does **not** make one scalar expression `D_ADEQ^cat` a universal CORE primitive.

Older constructions such as

\[
D_{ADEQ}^{cat}(Q;P,Y)
\]

remain valid contract-specific adapters when their observation map, data metric/loss, topology, tolerance and nuisance treatment are declared.

Therefore:

\[
\boxed{
\text{catalog adequacy is canonical as a required prior question,}
\quad
D_{ADEQ}^{cat}\text{ is adapter-dependent}.
}
\]

**STATUS:** `CANONICAL SCOPE CLARIFICATION`.

This resolves former `V1-GAP-01` without adding a new core definition.

---

## C65 — physical CANON-03 source bind

The current authoritative physical source is:

- repository `smoczynski-b/psi-model`;
- commit `7e64ec8ad766623ffeede3daa4bb68dee15135c1`;
- path `psi-agent/canon/PSI-R3-CONSOLIDATED-CANON-03.md`;
- version `1.0.0`;
- Git blob SHA `72d711a40c65376ee932809802622f3985ecb02a`.

It identifies itself as `CURRENT / SUPERIOR PHYSICAL CANON SOURCE` and explicitly establishes its precedence over earlier compatible typed sources.

**STATUS:** `PROVENANCE / CURRENT CANON POINTER`.

Historical missing originals remain genealogy gaps only and are not represented as recovered.

---

## C66 — older structured CAT/FACT apparatus status

The following older structures are retained only at their audited scopes:

- `ISO/HOR/REF/CRS` — derived typed CAT calculus;
- `GEN/TEST/SELECT` — derived workflow discipline;
- fixed birth/death thresholds or hysteresis — domain/update policy unless separately justified;
- factorization groupoid and homotopy/weak ADEQ fibre — derived structured extension when required by the task/contract;
- scalar `D_ADEQ^cat` — protocol-specific adapter.

None of these overrides the smaller physical CANON-03 definitions C62–C64.

**STATUS:** `DERIVED / GENEALOGY-COMPATIBLE / NOT CORE`.

---

## Probabilistic bisimulation editorial decision

The Larsen–Skou comparison remains in `classical-compare-01.md` as an explanatory classical comparison.

It receives **no current C-ID** because no V1/V2 theorem depends on it. Lack of a C-ID is therefore no longer a freeze blocker.

If a later theorem uses probabilistic bisimulation essentially, it must be promoted through the ordinary claim/source gate at that time.

---

## Freeze readiness

After C62–C66:

- physical CANON-03 provenance is bound;
- current CAT and FACT definitions are registered;
- the old universal-`D_ADEQ` expectation is removed;
- RED-1 definitions are registered;
- MINI gauge/observation mismatch is repaired;
- major classical comparison sources are bound.

The next legal operation is `V1-V2-FREEZE-RECHECK-01`.
