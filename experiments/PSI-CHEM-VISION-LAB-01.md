# PSI-CHEM-VISION-LAB-01

**Scope correction — 2026-09-30:** auxiliary finite ambiguity witness.
This does not test the same data under different representations or memory
quality. Its proposed next image-collection stage is superseded by the
[current memory objective](../docs/memory/README.md).
Chemistry's intended motivation is formal, physically constrained process
knowledge and its possible geometry; the visual fixture below tests only an
auxiliary ambiguity question.

**Korekta zakresu — 2026-09-30:** pomocniczy skończony świadek niejednoznaczności.
Nie jest to test tych samych danych w różnych reprezentacjach ani jakości pamięci.
Propozycję dalszego zbierania obrazów zastępuje wskazany bieżący cel pamięci.
Motywacją chemiczną jest formalna wiedza o fizycznie ograniczonych procesach
i ich możliwej geometrii; poniższy przykład wizualny sprawdza jedynie pomocniczą
kwestię niejednoznaczności.

**Status:** EXPERIMENTAL / SYNTHETIC FIRST PASS  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30

## 1. Purpose

Reconnect the earlier PSI chemistry line with the current memory/geometry work by testing one narrow question:

\[
\boxed{\text{can identical coarse visual evidence support distinct reaction mechanisms?}}
\]

and, if so, whether the **reaction language** and its relational geometry can reduce the compatible fibre without confusing visual salience with identifiability.

This is not a wet-lab protocol and does not infer chemistry from pixels. The first pass uses a frozen synthetic image-feature trace as a surrogate for future real images.

## 2. Historical continuity

Earlier PSI chemistry already established the relevant boundary: concentration dynamics need not identify a unique reaction network, and the observational ladder runs from concentrations to full state, reaction fluxes, fluctuations and mechanism. Hidden chemical states may become memory kernels after elimination. `PSI-CHEM-VISION-LAB-01` takes the next observational step downward: a picture is a still coarser projection than a concentration trace.

## 3. Reaction language

A reaction statement is treated as a typed directed **hyperedge**:

\[
\rho:\quad \sum_i \alpha_i X_i \longrightarrow \sum_j \beta_j Y_j.
\]

A reaction mechanism is a finite hypergraph:

\[
\mathcal H=(S,\mathcal R),
\]

where `S` is the species set and `R` the reaction-hyperedge set.

Species names are not themselves structural identity. Two mechanisms are structurally equivalent for this test if a bijection of species names preserves every reactant/product multiset.

## 4. Frozen worlds

Three candidate worlds share the same coarse visual trace:

\[
V_0=\texttt{R1-C0-S0},\qquad
V_1=\texttt{R1-C1-S0},\qquad
V_2=\texttt{R2-C0-S1},
\]

where `R` = visible regions, `C` = cloud/turbidity flag, `S` = sediment flag.

The reaction languages are:

### SEQ_A

\[
A\to I,\qquad I\to P.
\]

### SEQ_X

\[
X\to J,\qquad J\to Y.
\]

### COUPLED

\[
A\to I,\qquad A\to J,\qquad I+J\to Q.
\]

The first two are isomorphic after relabelling species. The third is not: it contains a genuine two-reactant hyperedge.

## 5. PSI fibres

### Visual observation only

All three worlds generate the same frozen visual signature, hence:

\[
F_{\rm vis}(Y)=\{\mathrm{SEQ\_A},\mathrm{SEQ\_X},\mathrm{COUPLED}\}.
\]

Therefore visual clarity does not imply mechanism identifiability.

### Add a reaction-language constraint

Suppose the available symbolic observation establishes only that the compatible mechanism has two elementary reaction statements. Then:

\[
F_{\rm vis+lang}(Y)=\{\mathrm{SEQ\_A},\mathrm{SEQ\_X}\}.
\]

The concrete realization is still not identified:

\[
|F_{\rm vis+lang}(Y)|=2.
\]

But for the task

\[
\mathcal T_{\rm motif}=\text{identify reaction-network motif},
\]

both worlds belong to the same structural class:

\[
q_{\mathcal T_{\rm motif}}(\mathrm{SEQ\_A})
=
q_{\mathcal T_{\rm motif}}(\mathrm{SEQ\_X})
=\mathrm{SEQUENTIAL\_2STEP}.
\]

Thus:

\[
\boxed{|F|=2\quad\text{but}\quad |q_{\mathcal T_{\rm motif}}(F)|=1.}
\]

This is a direct finite witness of the distinction between **object identification** and **task decidability**.

### Add provenance/history

A sample/history tag may later split the remaining two realizations. For the frozen witness:

\[
\mathrm{SAMPLE\!-
ALPHA}\Rightarrow\mathrm{SEQ\_A}.
\]

Provenance identifies a realization; it does not change the structural equivalence of the two sequential reaction languages.

## 6. Image + information architecture

The intended future object is not `image -> label`, but:

\[
\boxed{
\text{image frame}
\to
\text{visual geometry}
\to
F_{\rm vis}
\to
\text{reaction-language constraints}
\to
q_{\mathcal T}(F)
}
\]

with the image itself stored as evidence/provenance rather than collapsed into a single semantic label.

The visual layer should eventually expose at least:

- number and geometry of visible regions;
- interfaces/boundaries;
- turbidity/cloud domains;
- sediment/crystal domains;
- bubbles/gas domains;
- temporal persistence and motion of those structures.

These are observational features, not chemical identities.

## 7. Geometry principle

Two chemically different systems may instantiate the same relational motif:

\[
\mathcal H_1\cong\mathcal H_2
\]

under a species relabelling. Conversely, similar visual geometry may arise from non-isomorphic reaction hypergraphs.

Therefore three notions must remain separate:

\[
\boxed{
\text{visual similarity}
\neq
\text{reaction-graph isomorphism}
\neq
\text{chemical identity}.
}
\]

This is the chemistry version of the current PSI memory rule: geometry can guide attention but cannot by itself grant the right to identify.

## 8. Regression

`scripts/test_chem_vision_lab.py` checks:

1. one visual trace leaves three distinct mechanisms compatible;
2. `SEQ_A` and `SEQ_X` are exact reaction-hypergraph isomorphs under relabelling;
3. `COUPLED` is not isomorphic to the sequential motif;
4. the two-step language constraint narrows the fibre from 3 to 2;
5. the object fibre remains non-singleton while the motif task quotient is singleton;
6. provenance may later resolve the concrete realization;
7. a true two-reactant hyperedge distinguishes the coupled branch from an ordinary chain.

## 9. Boundary / next physical stage

`visual_trace` is a synthetic surrogate. No claim is made about pixel segmentation, computer vision, laboratory chemistry or empirical frequencies.

The next physical stage, if selected, should replace the surrogate trace with a small set of real or generated safe laboratory images while preserving the same contract:

\[
\boxed{\text{image evidence first; mechanism claim only after compatible-fibre analysis}.}
\]

No new PSI primitive is introduced.
