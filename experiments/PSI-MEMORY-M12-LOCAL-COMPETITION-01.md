# PSI-MEMORY-M12-LOCAL-COMPETITION-01

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can task retrieval remain bounded when the competing information is not remote noise but nearby, source-attested structure around the same mathematical object?

Anchor:

\[
\boxed{\mathrm{II.9}}
\]

Task:

> retrieve the proof prerequisites and explicit scope/boundary statements of II.9.

## 1. Local competition pool

M12 constructs an undirected discovery neighbourhood of radius 2 from `II.9` using the existing history, relational and bridge memory tables plus the verified M9 delta.

The semantic direction of every edge is preserved; undirected traversal is used only to discover the local competing pool.

Rows from existing memory maps are admitted to the routing stress pool only when they point to an existing repository source. They receive status `ROUTING_ATTESTED` for this experiment. This means **mapped and source-addressed**, not independently re-proved by M12.

The M9 edge remains backed by its stricter fragment certificate and is labelled `VALID_FRAGMENT_CERT`.

## 2. Task-relative navigation contract

The frozen contract is `m12-task-contract.tsv`.

For this task:

- `HARD_DEPENDS_ON`, `USES_DEFINITION`, `USES_LEMMA` are proof-prerequisite relations and may expand their target;
- `NOT_DEPENDS_ON`, `DOES_NOT_IMPLY` are boundary relations: include them, but do **not** expand their targets;
- all other nearby relation types remain valid memory but are irrelevant to this particular retrieval contract.

Thus relation type controls both descriptive meaning and traversal legality.

## 3. Budget

\[
\boxed{B_E=12\text{ edges}}
\]

The selector must operate inside this fixed budget regardless of the size of the radius-2 local pool.

## 4. Required witness

The selected task view must include exactly:

- `II.9 HARD_DEPENDS_ON II.7`;
- `II.9 USES_DEFINITION C57`;
- `II.9 USES_LEMMA C58`;
- `II.9 NOT_DEPENDS_ON II.8`;
- `II.9 DOES_NOT_IMPLY {FINITE-MEMORY, COMPUTABILITY, EFFICIENCY, BIT-MINIMALITY}`;
- the proof closure of II.7 through `II.4`, `C57`, `C58`;
- `C58 HARD_DEPENDS_ON C57`.

The wider nearby pool contains alternative routes to `C57/C58` and multiple other legitimate relation families. Those must not enter the task view merely because they are close.

## 5. Success predicates

M12 passes iff:

1. the local competing pool contains at least 25 edges and 15 nodes;
2. the task view contains at most 12 edges;
3. the frozen required set is recovered exactly;
4. reversing the physical input order of candidate edges does not alter selection;
5. boundary targets are terminal and do not expand into unrelated local subgraphs;
6. selected edges are less than 60% of the local candidate pool.

## 6. Boundary

M12 is a **routing/selectivity** experiment. `ROUTING_ATTESTED` is deliberately weaker than the fragment-level epistemic certificate of M7/M8/M9. A PASS therefore supports the claim that typed relations can govern bounded task navigation in a dense local graph; it does not promote every mapped relation to theorem-level `VALID` and does not establish optimal retrieval for arbitrary tasks.
