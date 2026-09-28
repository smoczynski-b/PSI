# PRINCIPIA SEMANTICA — WHOLE-V1 CROSS-CHECK 01

**Status:** `PASS WITH REQUIRED NONSEMANTIC NORMALIZATION / NO FREEZE ERRATA`  
**Date:** 2026-09-28  
**Scope:** first prose pass of Volume I, units I.1–I.6  
**Canonical basis:** `principia-v1-v2-freeze-01.md`, `claim-registry-12.md`, physical `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0

---

## 0. Purpose

Local cross-checks of I.1–I.6 tested every unit against its immediate frozen claims. This run tests **Volume I as one typed system**.

The audit asks whether, across chapter boundaries, the first prose pass preserves:

1. one coherent notation and type system;
2. the dependency order frozen for V1;
3. the distinction between `DEFINITION`, `THEOREM/BRIDGE`, `POLICY`, `BOUNDARY` and `BENCHMARK`;
4. the boundary between V1 foundations and V2 proofs / V3 laboratories / V4 genealogy;
5. all regression obligations relevant to the foundation layer;
6. the prohibition on silent semantic change after Freeze 01.

The whole-volume audit found **no contradiction in CORE5, no false theorem requiring retraction, and no need for an erratum to Freeze 01**. It did find a finite set of editorial/type-normalization corrections that must be applied before V2 prose begins.

---

# 1. Global dependency order

The six units form a valid forward dependency chain:

\[
\boxed{
I.1\to I.2\to I.3\to I.4,
\qquad
I.3\to I.5,
\qquad
(I.1\!:\!I.5)\to I.6.
}
\]

More explicitly:

- I.1 types the contract-relative roles;
- I.2 constructs the compatible fibre at fixed catalog/observation contract;
- I.3 constructs task equivalence and the task quotient;
- I.4 specializes representation adequacy to histories/future-task semantics;
- I.5 adds an orthogonal inference-quality layer: exactness, stability and probabilistic licensing;
- I.6 records methodological no-go transitions and primitive-growth discipline.

No chapter requires a mathematical object that is introduced only later, except for explicit forward references to V2 proofs.

**RESULT:** `PASS`.

---

# 2. Frozen semantic roles

Across I.1–I.6, the five CORE roles remain distinguishable:

\[
\boxed{
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
}
\]

No chapter introduces a sixth semantic role. History, memory, operational state, probability models and structured factorization data are treated as contract-relative candidates/representations/protocol structure or derived modules, not as automatic CORE additions.

The following frozen distinctions survive the prose pass:

\[
\text{representation}\neq\text{represented object},
\]

\[
\text{task-information adequacy}\neq\text{full contract legality},
\]

\[
\mathrm{PSI\!-
ID}\neq\mathrm{PSI\!-CAT},
\]

\[
\text{realization equivalence}\neq\text{behavioural recoding},
\]

\[
\text{symmetry}\not\Rightarrow\text{legal gauge}.
\]

**RESULT:** `PASS`.

---

# 3. Exact foundation chain

The exact set-level chain is coherent:

\[
Y
\to
\mathcal K_c^Y
\to
F_c(Y)
\to
E_{\mathcal T,c}
\to
M_{\mathcal T,c}.
\]

The representation-adequacy gate remains

\[
\boxed{
\ker_{\rm eq}\rho\subseteq E_{\mathcal T,c}.
}
\]

The history specialization remains

\[
\boxed{
\ker_{\rm eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
}
\]

and is presented as the same representation-adequacy logic on a history reference space, not as a new primitive law.

V1 does not silently import the factorization proof, exact decidability theorem, quotient dynamics theorem or history-quotient minimality proof from V2.

**RESULT:** `PASS`.

---

# 4. Two independent orders are preserved

The volume contains two distinct logical structures.

## 4.1 Identification workflow

\[
\boxed{
\text{catalog adequacy}
\to
\text{fibre}
\to
\text{local ID}
\to
\text{global ID}
\to
\text{protocol design/refinement}.
}
\]

## 4.2 Inference-quality gates

\[
\boxed{
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
}
\]

These are not one long sequence. The second is an orthogonal quality/licensing audit applied when stability or probabilistic inference is part of the declared problem.

**RESULT:** `PASS AFTER WORDING CORRECTION IN I.6`.

---

# 5. Required normalization N1 — protocol design is redesign/refinement

### Problem

I.1 already requires an observation/protocol contract before a fibre can be formed. I.2 reproduces the canonical sequence ending in `PROJEKTOWANIE PROTOKOŁU`. Read literally across the volume, this can look circular: protocol both precedes the fibre and is designed after global identifiability.

### Correction

V1 must state explicitly that the final arrow means **design, redesign or refinement of the next/instrumented identification protocol in response to the adequacy/identifiability diagnosis**, not that no initial protocol existed before the fibre was constructed.

Thus the intended logic is:

\[
\boxed{
P_0
\to
\text{adequacy/fibre/ID diagnosis}
\to
P_1\text{ (redesigned/refined protocol)}.
}
\]

No change to C11/C64 is required.

**CLASS:** `EDITORIAL TYPE CLARIFICATION`  
**FREEZE IMPACT:** `NONE`.

---

# 6. Required normalization N2 — contract index in history semantics

### Problem

I.1–I.3 make contract dependence explicit through the index `c`, while I.4 uses the historically frozen notation

\[
\operatorname{Beh}_{\mathcal T}(H),
\qquad
\equiv_{\mathcal T,t}.
\]

Across chapter boundaries this can be read as contract-independent future semantics.

### Correction

At the start of I.4 state once:

> Throughout I.4 a contract `c` and time `t` are fixed. The RED-1 notation suppresses the `c` index for readability. Full notation may be written `Beh_{\mathcal T,c,t}` and `\equiv_{\mathcal T,c,t}` when several contracts are compared.

This is notation only; the registered RED-1 symbols remain valid.

**CLASS:** `NOTATION NORMALIZATION`  
**FREEZE IMPACT:** `NONE`.

---

# 7. Required normalization N3 — remove `R` collisions in I.4

### Problem A — memory codomain

I.3 uses

\[
R\in\mathscr R_{\mathcal T,c}
\]

for task quantities. I.4 then writes

\[
\rho_t:\mathcal H_t\to R_t
\]

for the codomain of a memory representation. The meanings are unrelated.

### Correction

In V1 prose use

\[
\boxed{\rho_t:\mathcal H_t\to Z_t}
\]

for the memory representation space. The old C42 notation `R_t` remains source provenance only.

### Problem B — LAZARUS operational regime notation

The historical expression `Comp(\mathcal R_t)` is visually too close to the central task closure `\mathscr R_{\mathcal T,c}`.

### Correction

In V1 do not expose the historical regime-set symbol unless required. Use a locally typed operational state

\[
\Gamma_t\in\mathcal G_t^{op}
\]

or define the historical symbol explicitly in a boundary box. Full LAZARUS notation belongs to V3.

**CLASS:** `NOTATION / LOCAL TYPING`  
**FREEZE IMPACT:** `NONE`.

---

# 8. Required normalization N4 — type all Go/LAZARUS witness symbols locally

### Problem

The I.4 boundary examples use `X_t`, `F_t(H)`, `B_t`, `\sigma_t`, `V_t`, `U_t` and `\Gamma_t`. They are well-defined in their laboratory sources, but several appear in V1 without local typing.

That is inconsistent with the Bronsztejn discipline established in I.1.

### Correction

Either reduce the examples to prose cross-references or define them locally before use. Minimum legal local typing:

- `X_t` — current physical candidate/state space of the LAZARUS witness;
- `F_t(H)\subseteq X_t` — current world-state fibre induced by history `H`;
- `B_t` — Go board position;
- `\sigma_t` — player to move;
- `V_t=\{B_0,\ldots,B_t\}` — visited-board set for the PSK witness;
- `U_t=\{(B_i,\sigma_i):i\le t\}` — visited-situation set for the SSK witness;
- `\Gamma_t` — active operational state/composition in the LAZARUS witness.

These remain boundary examples, not V1 foundations.

**CLASS:** `TYPE COMPLETION`  
**FREEZE IMPACT:** `NONE`.

---

# 9. Required normalization N5 — inference-gate symbols in I.5

### Problem

I.5 names its three gates `E`, `S`, `P` and writes

\[
E\not\Rightarrow S,
\qquad
S\not\Rightarrow P.
\]

But V1 already reserves `E_{\mathcal T,c}` for task equivalence. The naked `E` is therefore an avoidable collision.

### Correction

Use non-conflicting labels, for example

\[
\boxed{
\mathsf G_{EX},
\quad
\mathsf G_{ST},
\quad
\mathsf G_{PR},
}
\]

with

\[
\boxed{
\mathsf G_{EX}\not\Rightarrow\mathsf G_{ST},
\qquad
\mathsf G_{ST}\not\Rightarrow\mathsf G_{PR}.
}
\]

No mathematical content changes.

**CLASS:** `NOTATION NORMALIZATION`  
**FREEZE IMPACT:** `NONE`.

---

# 10. Required normalization N6 — do not use chained `!=` as inference logic

### Problem

I.5 correctly replaced the old shorthand

`exact != stable != confidence`

by non-implications. I.6 nevertheless reintroduces the chained shorthand

\[
\text{adequacy}\neq\text{identifiability}\neq\text{stability}\neq\text{confidence}.
\]

This is readable rhetoric but poor formal notation because the terms are differently typed questions, not four elements of one comparison set.

### Correction

Replace the chain by prose:

> catalog adequacy, identifiability, perturbation stability and probabilistic confidence are distinct questions with distinct licensing conditions.

Where an actual logical direction is intended, use `\not\Rightarrow`.

**CLASS:** `FORMAL-NOTATION CORRECTION`  
**FREEZE IMPACT:** `NONE`.

---

# 11. Required normalization N7 — keep R4 project governance out of the mathematical backbone

### Problem

The V1 Unit Map correctly classified C36 as `PROJECT POLICY / CROSS-REFERENCE` and C34 as a pressure result to be deferred from the mathematical foundations. The current I.6 prose gives the R4 pressure history a larger footprint than that classification licenses.

### Correction

The V1 mathematical text should retain only the general methodological rule:

\[
\boxed{
\text{a new primitive requires a typed witness forcing a genuinely new semantic role}.
}
\]

Then add at most a short editorial note:

> In the current project state no tested pressure witness has forced R4; this is a project freeze, not a completeness theorem.

The detailed list `CAT/FACT, CLOSED-FRAME, LAZARUS, HIGHER-FIBRE`, the R4 court history and admission ledger belong to V4/genealogy or project documentation.

**CLASS:** `EDITORIAL BOUNDARY RESTORATION`  
**FREEZE IMPACT:** `NONE`.

---

# 12. Cross-volume bridge: generic task equivalence versus history equivalence

I.4 must not create the impression of a second independent ontology of task equivalence.

The intended relation is:

- I.3 supplies the generic representation-adequacy architecture on a candidate space;
- I.4 takes the reference space to be histories and supplies a concrete future-task equivalence `\equiv_{\mathcal T,t}`;
- the memory test
  \[
  \ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}
  \]
  is the history analogue/specialization of the generic I.3 criterion.

V1 does **not** assert an unconditional identity

\[
E_{\mathcal T,c}=\equiv_{\mathcal T,t}
\]

between objects living on different underlying spaces. Such an identification requires an explicitly chosen history-space contract / map.

**RESULT:** `PASS WITH CLARIFYING SENTENCE REQUIRED IN I.4`.

---

# 13. Theorem / policy / boundary audit

No V1 unit falsely upgrades a project policy or benchmark into a mathematical theorem after the required normalization above.

| Item | Correct V1 role |
|---|---|
| CORE5 tuple | definition / architecture |
| compatible fibre | definition |
| catalog-first order | methodological principle |
| task closure / equivalence / quotient | definitions |
| `ker rho ⊆ E_T` | frozen bridge/principle; proof in V2 |
| history future-tree equivalence | definition; properties in V2 |
| Go / LAZARUS | boundary / regression witnesses |
| exact→stable→confidence separation | inference discipline |
| candidate stuffing prohibition | methodological no-go |
| current R4 stop | project policy / editorial note |

**RESULT:** `PASS`.

---

# 14. Regression coverage

The first prose volume does not need to reproduce laboratory calculations, but its central claims are guarded by the existing bank:

- `R01 HCube` guards I.3 against coarse-representation sufficiency inflation;
- `R02 Go` guards I.4 against task-independent memory sufficiency;
- `R03 FS-STAT` guards I.5 against exact→stable→confidence inflation;
- F55/F57 guard I.1/I.3/I.6 against gauge/observation and contract-legality conflation;
- F58/F59 guard I.2/I.6 against automatic promotion of older ADEQ/CAT/FACT machinery;
- F60 remains a V2 proof-boundary guard for factorization uniqueness on `im rho`.

**RESULT:** `PASS`.

---

# 15. Repetition audit

Some repetition is deliberate and useful:

- I.1 introduces `representation != represented object`; I.6 recalls it as a no-go rule;
- I.1 introduces symmetry/gauge caution; I.3 gives the exact task-information criterion; I.6 summarizes the boundary;
- I.2 introduces `UNRESOLVED`-compatible fibre logic; I.5 generalizes non-certification discipline.

However I.6 should function as a **compact consolidation**, not a second derivation of I.1–I.5. During normalization, repeated explanations should be shortened to references where they do not add a new boundary.

**RESULT:** `PASS WITH COMPRESSION RECOMMENDED`.

---

# 16. Whole-volume verdict

The first prose pass is mathematically coherent with Freeze 01. The audit found no semantic contradiction and no new primitive pressure.

It did find seven nonsemantic corrections N1–N7 plus one clarifying bridge between generic and history task equivalence.

Therefore:

\[
\boxed{
\mathrm{WHOLE\!-
V1\ CROSS\!-
CHECK\ 01}
=
\mathrm{PASS\ WITH\ REQUIRED\ NORMALIZATION}.
}
\]

and

\[
\boxed{
\mathrm{FREEZE\ 01\ ERRATA}=\mathrm{NONE}.
}
\]

The next legal operation is not yet V2 prose. It is a short **`V1-NORMALIZATION-01`** applying N1–N7 and the I.3/I.4 bridge, followed by a mechanical recheck of symbols and chapter pointers. After that:

\[
\boxed{
\mathrm{V1\ PROSE\ PASS\ 01}
\to
\mathrm{V1\ NORMALIZED\ PASS}
\to
\mathrm{V2\ PROSE}.
}
\]
