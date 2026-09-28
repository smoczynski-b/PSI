# PSI — claim registry 11

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-10.md` as current public registry  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`

This version records `PROOF-SOURCE-MIGRATION-AUDIT-01`, repairs C19, migrates the RED-1 history-equivalence definition, and sharpens the scope of exact task adequacy. CORE5 and Agent Architecture v02 remain unchanged.

## Retained claims

Retain C01–C18 and C20–C56 from `claim-registry-10.md` unless explicitly sharpened below.

C19 is replaced by C19-v2.

---

## C19-v2 — CAT–FACT–NORM–MINI corrected exact interval theorem

Let

\[
\gamma:[0,T]\to\mathbb R^3
\]

be `C^3` and regular, with fixed time parameter. Use the finite grammar `{F,B}` of Frenet/Bishop interval atoms and constant Bishop normal-plane gauge `SO(2)`.

Two exact observation contracts are legal.

### Absolute-coordinate contract

\[
P_0^{\rm abs}:\qquad Y_{\rm abs}=\gamma(t).
\]

Then external `SE(3)` is not quotiented inside the same fixed-coordinate observation fibre. Define

\[
\operatorname{Fact}^{0,\rm abs}_{FB,P_0}(Y_{\rm abs})
=
\operatorname{RawFact}^{0,\rm abs}_{FB,P_0}(Y_{\rm abs})/SO(2)_{\rm normal}.
\]

### Shape contract

\[
P_0^{\rm shape}:\qquad Y_{\rm shape}=[\gamma]_{SE(3)}
\]

or an explicitly `SE(3)`-invariant equivalent observation. Then

\[
\operatorname{Fact}^{0,\rm shape}_{FB,P_0}(Y_{\rm shape})
=
\operatorname{RawFact}^{0,\rm shape}_{FB,P_0}(Y_{\rm shape})/
(SE(3)\times SO(2)_{\rm normal}).
\]

For either correctly typed contract:

1. the rewrite on normal-frame gauge classes terminates;
2. it is locally confluent and therefore confluent by Newman's lemma;
3. every legal finite Frenet/Bishop segmentation reduces to one Bishop normal class;
4. the corresponding restricted MINI factorization set has cardinality one;
5. vanishing curvature that only destroys the Frenet frame is a recode/domain event, not automatic catalog birth.

The MINI `RawFact/Fact` objects are grammar-specific set-level shadows and do **not** redefine general PSI-FACT groupoid/homotopy fibres.

**STATUS:** `BRIDGE / EXACT MINI / PASS WITH CONTRACT ERRATA RESOLVED`  
**ROLE:** `CAT/FACT/NORM BENCHMARK`  
**SOURCE:** `cat-fact-norm-mini-01.md` after `PROOF-SOURCE-MIGRATION-AUDIT-01`.

---

## C57 — future task tree and history equivalence

For a history space `H_t`, define

\[
\operatorname{Beh}_{\mathcal T}(H)
\]

as the rooted tree of all legal future extensions of `H`, with node labels carrying the declared task information and edge labels carrying the literal experiment/outcome pair.

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

through a root-preserving isomorphism preserving node labels, edge labels and the parent-child relation.

**STATUS:** `DEFINITION / CURRENT MIGRATION OF RED-1`  
**ROLE:** `HISTORY / FUTURE-TASK SEMANTICS`.

---

## C58 — history equivalence is an equivalence relation

The relation `≡_{T,t}` from C57 is reflexive, symmetric and transitive because identity, inverse and composition preserve the required labelled rooted-tree structure.

No finite-horizon assumption is required.

\[
\boxed{\equiv_{\mathcal T,t}\text{ is an equivalence relation}.}
\]

**STATUS:** `THEOREM / RED-1 PASS`.

---

## C59 — congruence and recursive task-state update

Under the RED-1 literal-label future-tree contract, if

\[
H\equiv_{\mathcal T,t}H'
\]

and a labelled extension `(epsilon,y)` is legal from `H`, the matching root edge exists from `H'`; corresponding successor subtrees remain equivalent.

Therefore `≡_{T,t}` is a congruence for legal history extension and the partial map

\[
\boxed{
U_{\mathcal T,t}
([H],\varepsilon,y)
=
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}
}
\]

is well-defined on its legal domain.

This establishes mathematical recursive update only; it does not imply finite memory, effective computability or efficient implementation.

**STATUS:** `THEOREM / BRIDGE / RED-1 PASS`.

---

## C60 — exact task adequacy versus full contract legality

For a representation

\[
\rho:\Omega\to Z,
\]

\[
\boxed{
\ker_{eq}\rho\subseteq E_{\mathcal T}
}
\]

is the exact criterion that `rho` preserves every distinction required by the task quotient.

For a proposed reduction/gauge/truncation map `q`, this condition is therefore the exact **task-information adequacy** test.

However it is not, by itself, the complete contract-legality test. A contract can additionally require:

- correct domain/codomain;
- admissible gauge/action;
- observation compatibility or equivariance;
- hard domain constraints;
- other declared protocol conditions.

Thus

\[
\boxed{
\text{task-adequate reduction}
\neq
\text{fully contract-legal reduction}
}
\]

in general.

C09 remains valid. C32/C37 are exact task-adequacy gates and necessary components of contract legality, not an exhaustive replacement for all contract checks.

**STATUS:** `CORE CLARIFICATION / SCOPE CORRECTION`.

---

## C61 — observation-compatible gauge condition

A transformation group `G` may be quotiented inside a fixed compatible observation problem only when the observation/compatibility contract descends appropriately through that action.

In the simplest invariant case:

\[
\Psi(g\cdot x)=\Psi(x)
\qquad\forall g\in G.
\]

More generally an explicitly equivariant observation may require simultaneous action on the observation space and a correspondingly typed compatibility relation.

Therefore:

\[
\boxed{
\text{geometric symmetry}
\not\Rightarrow
\text{legal gauge of a fixed observation fibre}.
}
\]

C19-v2 is the fixed regression witness: fixed-coordinate trajectory observation does not automatically permit an `SE(3)` quotient over the same `Y`.

**STATUS:** `CONTRACT / GAUGE DISCIPLINE`.

---

## Migration state after audit

The following remain deliberately **unpromoted** pending explicit CANON-03 migration:

- general catalog-adequacy definition `D_ADEQ^cat`;
- full PSI-CAT typed calculus as current V1/V2 definitions;
- general PSI-FACT groupoid/homotopy-fibre construction;
- probabilistic bisimulation comparison as a dedicated current claim ID.

Strong older sources exist for these objects, but older typed source does not automatically become current canon.

---

## Current freeze state

\[
\boxed{
\mathrm{V1/V2\ FREEZE}=\mathrm{BLOCKED\ BY\ FINITE\ MIGRATION/SOURCE\ GATES},
}
\]

not by a newly discovered CORE defect.
