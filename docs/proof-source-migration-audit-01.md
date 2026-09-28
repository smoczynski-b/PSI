# PRINCIPIA — PROOF / SOURCE / MIGRATION AUDIT 01

**Status:** CURRENT FREEZE-GATE AUDIT  
**Date:** 2026-09-28  
**Scope:** V1/V2 maps, C06–C09 spine, history quotient, classical bridges, CAT/FACT/MINI, FRAME, HIGHER-FIBRE  
**Rule:** `PASS | PASS WITH CORRECTION | BLOCKED`.

This audit does not add a new mathematical layer. It decides which mapped units are ready to enter the first V1/V2 freeze.

---

# 0. Global verdict

The elementary PSI quotient/factorization spine is sound.

The first freeze is **not yet legal** because several migration/source gates remain open and one real contract defect was found in `CAT–FACT–NORM–MINI-01`.

\[
\boxed{
\mathrm{V1/V2\ FREEZE}=\mathrm{BLOCKED\ BUT\ LOCALISED}.
}
\]

Current blockers:

1. `MINI-GAUGE-OBS-01` — fixed-coordinate exact observation was combined with an external `SE(3)` quotient that does not automatically preserve the same observation fibre;
2. `MIG-CAT-ADEQ-01` — catalog-adequacy definitions exist in older typed sources but still require explicit migration against CANON-03;
3. `MIG-CAT-FACT-01` — general PSI-CAT/PSI-FACT definitions and groupoid/homotopy-fibre layer have strong older sources but are not yet current registry units;
4. `SRC-BIND-01` — exact classical source binding must be frozen for lumpability, Myhill–Nerode, Newman, Bishop/RMF and higher pullback terminology;
5. `BISIM-CID-01` — probabilistic bisimulation comparison has a source and comparison text but no current C-ID.

The blockers are finite and typed. No CORE5 change is implicated.

---

# 1. Elementary theorem spine

## A01 — C06 exact task-level decidability

### Statement

For quotient map `q_T:Omega→Omega/E_T` and compatible fibre `F(Y)⊆Omega`:

\[
|q_{\mathcal T}(F(Y))|=1
\iff
F(Y)\neq\varnothing
\land
F(Y)\times F(Y)\subseteq E_{\mathcal T}.
\]

### Proof

- If the image is a singleton, `F(Y)` is nonempty and every two elements have the same quotient class, hence are `E_T`-equivalent.
- Conversely, if `F(Y)` is nonempty and all pairs are `E_T`-equivalent, all of `F(Y)` lies in one quotient class, so its image has cardinality one.

### Correction

Write explicitly

\[
F(Y)^2:=F(Y)\times F(Y)
\]

when the notation first appears.

### Verdict

\[
\boxed{\mathrm{C06=PASS}.}
\]

No external theorem source is required for validity; it is an elementary quotient fact.

---

## A02 — C07 kernel factorization criterion

### Statement

For maps

\[
\rho:\Omega\to Z,
\qquad
R:\Omega\to W,
\]

\[
\ker_{eq}\rho\subseteq\ker_{eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,
\quad
R=g\circ\rho.
\]

### Proof

If kernel inclusion holds, define

\[
g(\rho(x)):=R(x).
\]

If `rho(x)=rho(y)`, kernel inclusion gives `R(x)=R(y)`, so `g` is well-defined. Surjectivity of `rho:Omega→im rho` gives uniqueness on `im rho`.

Conversely, if `R=g∘rho`, equality of `rho` values implies equality of `R` values.

### Boundary

Do not claim uniqueness of an extension

\[
g:Z\to W
\]

outside `im rho` without extra assumptions.

### Verdict

\[
\boxed{\mathrm{C07=PASS}.}
\]

---

## A03 — C08 global task sufficiency

Since

\[
\ker_{eq}q_{\mathcal T}=E_{\mathcal T},
\]

C08 is exactly C07 with

\[
\rho=\Psi,
\qquad
R=q_{\mathcal T}.
\]

Therefore

\[
\ker_{eq}\Psi\subseteq E_{\mathcal T}
\iff
q_{\mathcal T}=f\circ\Psi
\]

for unique `f` on `im Psi`.

### Verdict

\[
\boxed{\mathrm{C08=PASS}.}
\]

---

## A04 — C09 representation adequacy

For arbitrary representation

\[
\rho:\Omega\to Z,
\]

exact preservation of task class is equivalent to

\[
\boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}},
\]

and to factorization of the task quotient through `rho` on its image.

### Scope correction

This criterion is exact **task-information adequacy**.

For a quotient/gauge map `q`, the inclusion

\[
\ker q\subseteq E_{\mathcal T}
\]

is equivalent to preservation of exact task distinctions. It is not, by itself, the complete statement that the reduction is legal under every aspect of the contract. Full contract legality can also require:

- correct domain/codomain;
- admissible action/gauge;
- observation compatibility/equivariance;
- preservation of hard domain constraints.

Thus distinguish:

\[
\boxed{
\text{task-adequate reduction}
\neq
\text{fully contract-legal reduction}.
}
\]

### Verdict

\[
\boxed{\mathrm{C09=PASS\ WITH\ SCOPE\ CORRECTION}.}
\]

C32/C37 remain valid as necessary task-adequacy gates; they must not be advertised as the only contract gate.

---

# 2. History quotient / RED-1

The recovered RED-1 source supplies the missing definitions.

For a history `H_t`, let

\[
\operatorname{Beh}_{\mathcal T}(H_t)
\]

be the rooted tree of all legal future extensions, with node labels carrying task information and edges carrying literal experiment/outcome labels.

Define

\[
\boxed{
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H')
}
\]

through a rooted label-preserving tree isomorphism.

The source also proves:

1. `≡_{T,t}` is an equivalence relation;
2. under literal legal-extension labels it is a congruence for the declared history update;
3. the partial update
   \[
   U_{\mathcal T,t}([H],\varepsilon,y)
   =[\delta_t(H,\varepsilon,y)]
   \]
   is well-defined on its legal domain;
4. every exact sufficient representation factors the canonical history quotient on `im rho`.

### Verdict

\[
\boxed{\mathrm{RED1\ MATHEMATICS=PASS}.}
\]

But the current claim registry lacks a dedicated definition ID for `Beh_T` / `≡_{T,t}`.

Therefore:

\[
\boxed{\mathrm{V2\!-\!GAP\!-\!01=RESOLVED\ MATHEMATICALLY,\ OPEN\ EDITORIALLY}.}
\]

The registry must migrate the definition before freeze.

---

# 3. Deterministic quotient dynamics

For `delta:Omega→Omega` and equivalence relation `E`, define

\[
\bar\delta([x]):=[\delta(x)].
\]

This is well-defined iff

\[
xEy\Rightarrow\delta(x)E\delta(y).
\]

Uniqueness follows from surjectivity of the quotient map.

### Verdict

\[
\boxed{\mathrm{C10=PASS}.}
\]

The stochastic analogue must remain separately typed; do not silently reuse the deterministic theorem.

---

# 4. Classical comparison/source layer

## A05 — Markov lumpability / C13

The present PSI statement matches the classical strong lumpability condition for a finite Markov chain: states in one block must assign the same total one-step transition probability to every target block.

**Primary classical source:** J. G. Kemeny, J. L. Snell, *Finite Markov Chains*, Chapter VI, Theorem 6.3.2 in the standard reprint tradition.

### Verdict

\[
\boxed{\mathrm{C13=PASS\ WITH\ SOURCE\ BIND}.}
\]

Boundary retained:

\[
E_{\mathcal T}\text{ alone}\not\Rightarrow\text{lumpability}.
\]

---

## A06 — probabilistic bisimulation comparison

**Source:** K. G. Larsen, A. Skou, “Bisimulation through probabilistic testing,” *Information and Computation* 94(1), 1991, 1–28, DOI `10.1016/0890-5401(91)90030-6`.

The existing comparison correctly treats equality with PSI task equivalence as conditional on choosing exactly the relevant action/future tests.

### Verdict

\[
\boxed{\mathrm{SOURCE=PASS},\qquad\mathrm{REGISTRY=BLOCKED}.}
\]

Reason: no dedicated current C-ID exists. The comparison may remain explanatory until migrated.

---

## A07 — Myhill–Nerode / C18

The equality

\[
E_{\mathcal T}=\equiv_L
\]

under candidate prefixes, right-concatenation transports and acceptance tests

\[
R_w(u)=1_L(uw)
\]

is a direct equality of definitions and can be proved self-contained in V2.

Classical provenance for the automata theorem:

- J. Myhill, *Finite Automata and the Representation of Events*, WADC Technical Report 57-624, 1957;
- A. Nerode, “Linear Automaton Transformations,” *Proceedings of the American Mathematical Society* 9 (1958), 541–544, DOI `10.1090/S0002-9939-1958-0135681-9` (also JSTOR DOI `10.2307/2033204`).

PSI does not own the finite-index/minimal-automaton theorem.

### Verdict

\[
\boxed{\mathrm{C18=PASS\ WITH\ SOURCE\ BIND}.}
\]

---

## A08 — Paige–Tarjan / C14

**Source:** R. Paige, R. E. Tarjan, “Three Partition Refinement Algorithms,” *SIAM Journal on Computing* 16(6), 1987, 973–989, DOI `10.1137/0216062`.

The current PSI status `CLASSICAL ALGORITHMIC BENCHMARK` is correct.

### Verdict

\[
\boxed{\mathrm{C14=PASS}.}
\]

---

# 5. CAT / FACT migration

Older typed sources contain a coherent general layer:

- catalog protocol and global `D_ADEQ`;
- `GEN ≠ TEST ≠ SELECT`;
- gauge as realization isomorphism, not catalog change;
- typed CAT morphism classes `ISO/HOR/REF/CRS`;
- `PSI-FACT = PSI-CAT|_{FactMorph}`;
- factorization groupoid `Fact_D^≃`;
- homotopy/weak ADEQ fibre retaining stabilizers and compatibility witnesses.

This is stronger than the current public Claim Registry representation of CAT/FACT.

However these sources predate the pinned CANON-03 target. Therefore the audit does **not** auto-promote them.

### Verdict

\[
\boxed{
\mathrm{CAT/FACT\ SOURCE=FOUND},
\qquad
\mathrm{CURRENT\ MIGRATION=BLOCKED}.
}
\]

Required next action:

1. compare the source roles with CANON-03 semantic roles;
2. migrate only compatible definitions;
3. retain higher/groupoid structure where task-relevant;
4. do not regress to a coarse set quotient by default.

This resolves `V2-GAP-03` as a **finite migration task**, not a mathematical mystery.

---

# 6. CAT–FACT–NORM–MINI proof audit

## A09 — termination

The measure

\[
\mu(X)=(n_F(X),n_{seg}(X))\in\mathbb N^2
\]

with lexicographic order decreases on every rewrite:

- `F→B` decreases `n_F`;
- `B⊕B→B` leaves `n_F` fixed and decreases `n_seg`.

The latter is true even if Frenet atoms remain elsewhere in the term.

### Verdict

\[
\boxed{\mathrm{TERMINATION=PASS\ WITH\ WORDING\ CORRECTION}.}
\]

---

## A10 — confluence modulo gauge

The intended rewrite should be defined **on gauge classes** or proved equivariant before quotienting.

After that correction, the only non-disjoint overlap type is the triple-Bishop configuration

\[
B_1\oplus B_2\oplus B_3,
\]

for which the two merge orders agree modulo the one constant normal-plane rotation. Disjoint `F→B` steps commute, and the unary `F→B` redex does not overlap a `B⊕B` redex at the same initial term.

With termination and local confluence on the quotient rewrite, Newman's lemma gives confluence.

**Classical source:** M. H. A. Newman, “On theories with a combinatorial definition of equivalence,” *Annals of Mathematics* 43 (1942), 223–243.

### Verdict

\[
\boxed{\mathrm{CONFLUENCE=PASS\ WITH\ FORMALIZATION\ CORRECTION}.}
\]

Do not say merely “the rules respect gauge” without defining or proving that statement.

---

## A11 — external `SE(3)` gauge versus exact observation

The current MINI snapshot says simultaneously:

\[
Y=\gamma(t)
\]

as an exact full coordinate trajectory and

\[
G_{ext}=SE(3)
\]

as a quotient on the compatible realization fibre.

This is not automatically legal.

For nontrivial `g∈SE(3)`, generally

\[
g\gamma(t)\neq\gamma(t),
\]

so the `SE(3)` action need not preserve the fibre over the same coordinate observation `Y`.

The older transport/gauge discipline already states the needed condition: an observation descends through gauge only when it is gauge-invariant/equivariantly interpreted at the observation level.

### Legal repair

Split the MINI contract into two variants.

#### Absolute-coordinate protocol

\[
P_0^{abs}:\qquad Y=\gamma(t).
\]

External `SE(3)` is **not** quotiented inside the same compatible fibre. The only presentation gauge relevant to the Frenet/Bishop factorization is the constant Bishop normal `SO(2)`.

#### Shape protocol

\[
P_0^{shape}:\qquad Y=[\gamma]_{SE(3)}
\]

or an explicitly `SE(3)`-invariant observation. Then external Euclidean gauge is legal and

\[
SE(3)\times SO(2)_{normal}
\]

may be used in the factorization quotient.

### Verdict

\[
\boxed{\mathrm{C19/MINI=PASS\ WITH\ REQUIRED\ CONTRACT\ ERRATA}.}
\]

Freeze must use one of the two typed variants; the mixed statement is prohibited.

---

## A12 — MINI factorization object versus general PSI-FACT

`RawFact_{FB,P0}` is a grammar-specific raw set of legal finite `{F,B}` segmentations/realizations.

Its quotient is a **set-level MINI shadow** of the general factorization groupoid/homotopy fibre. It must not be used to redefine general PSI-FACT or erase stabilizers/witnesses in other contracts.

### Verdict

\[
\boxed{\mathrm{MINI\ SET\ MODEL=PASS\ WITH\ SCOPE\ LABEL}.}
\]

---

# 7. FRAME / closed-loop source audit

Classical source binding:

- R. L. Bishop, “There Is More than One Way to Frame a Curve,” *American Mathematical Monthly* 82(3), 1975, 246–251, DOI `10.1080/00029890.1975.11993807`;
- D. Brander, J. Gravesen, “Monge surfaces and planar geodesic foliations,” *Journal of Geometry* 109 (2018), source explicitly identifies total torsion as the total rotation angle of an RMF around a closed curve;
- R. T. Farouki, S. H. Kim, H. P. Moon, “Construction of periodic adapted orthonormal frames on closed space curves,” *Computer Aided Geometric Design* 76 (2020), 101802, DOI `10.1016/j.cagd.2019.101802`.

The correct hierarchy remains:

\[
\boxed{\text{holonomy/return map first; total torsion as a coordinate under stronger Frenet hypotheses}.}
\]

### Verdict

\[
\boxed{\mathrm{C22/C24=PASS\ WITH\ SOURCE\ BIND}.}
\]

C23 remains a scoped PSI architectural verdict, not a classical geometry theorem.

---

# 8. HIGHER-FIBRE source audit

The explicit `B Z_2` witness is self-contained at the level of 1-groupoids.

For functors to a groupoid, the weak/2-pullback is represented by the iso-comma construction: objects carry a compatibility isomorphism. For

\[
*\to B\mathbb Z_2\leftarrow *,
\]

those compatibility isomorphisms are exactly `e,s∈Z_2`, yielding two components in the witness while the coarse component pullback is a singleton.

The terminology `2-pullback / iso-comma / homotopy pullback of groupoids` should be source-bound explicitly in V2.

### Verdict

\[
\boxed{\mathrm{C29/C30=PASS\ WITH\ TERMINOLOGY\ SOURCE\ BIND}.}
\]

C33 remains a scoped pressure verdict, not a universal higher-categorical theorem.

---

# 9. Catalog adequacy migration gap

Older sources provide two closely related exact constructions:

1. behavior-set pseudometric
   \[
   D_{ADEQ}^{cat}(Q;P,Y)
   =D_{ADEQ}^{beh}(\widetilde{\mathcal B}_Q^P;P,Y);
   \]
2. distance-to-manifested-behavior-set form
   \[
   D_{ADEQ}(Q;P,Y)
   =\operatorname{dist}(Y,\overline{\widetilde{\mathcal B}_Q^P}).
   \]

They are compatible when the same data pseudometric/topology is used, but the later CANON-03 migration has not yet been physically bound in the current registry.

### Verdict

\[
\boxed{\mathrm{V1\!-\!GAP\!-\!01=BLOCKED\ FOR\ FREEZE}.}
\]

Do not silently choose one notation during prose writing.

---

# 10. Freeze table

| Unit | Verdict | Freeze status |
|---|---|---|
| C06 exact decidability | PASS | READY |
| C07 factorization | PASS | READY |
| C08 global sufficiency | PASS | READY |
| C09 representation adequacy | PASS WITH SCOPE CORRECTION | READY AFTER WORDING PATCH |
| C10 quotient dynamics | PASS | READY |
| RED-1 history equivalence | PASS mathematics / migration missing | BLOCKED EDITORIALLY |
| C13 lumpability | PASS WITH SOURCE BIND | READY AFTER CITATION BIND |
| probabilistic bisimulation | source PASS / no C-ID | DEFER or MIGRATE |
| C18 Myhill–Nerode bridge | PASS WITH SOURCE BIND | READY AFTER CITATION BIND |
| C14 Paige–Tarjan | PASS | READY |
| general CAT/FACT | SOURCE FOUND / current migration missing | BLOCKED |
| C19 MINI | PASS WITH REQUIRED CONTRACT ERRATA | BLOCKED UNTIL PATCHED |
| C22/C24 FRAME | PASS WITH SOURCE BIND | READY AFTER CITATION BIND |
| C29/C30 HIGHER-FIBRE | PASS WITH SOURCE BIND | READY AFTER TERMINOLOGY BIND |
| catalog ADEQ definition | older source found / current migration unresolved | BLOCKED |

---

# 11. Immediate actions licensed by this audit

1. patch `CAT–FACT–NORM–MINI-01` into `P_abs` and `P_shape` variants;
2. create current registry IDs for RED-1 future-task equivalence;
3. create Claim/Falsifier registry versions recording the MINI gauge-observation correction;
4. source-bind the classical bridge bibliography;
5. perform explicit CANON-03 migration of CAT/ADEQ/FACT before first freeze;
6. only after these gates rerun `V1/V2 FREEZE 01`.

No new primitive and no Agent v03 is licensed by this audit.