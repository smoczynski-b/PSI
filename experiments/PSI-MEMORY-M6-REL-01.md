# PSI-MEMORY-M6-REL-01 — relational object description

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can the memory graph describe a PSI object primarily by its typed relation profile rather than by a prose summary stored inside the node?

The experiment tests the stronger architectural reading:

\[
\boxed{\operatorname{Desc}(v)=\text{thin identity core}(v)+\operatorname{Star}(v)}
\]

where `Star(v)` contains typed incoming and outgoing relations.

This is not a claim that relations replace the internal mathematical proposition, formula or proof. The tested target is the object's **structural role**: prerequisites, outputs, contracts, negative limits, regressions and bridges.

## 1. Objects

Three heterogeneous objects are frozen for M6-REL:

1. `II.9` — theorem: recursive history-quotient update;
2. `GO-G4` — finite regression case: situational superko memory;
3. `II.11.PSI-BRIDGE` — bridge aspect: exact PSI/Myhill-Nerode realization.

This prevents the test from succeeding only for one node class.

## 2. New relation requirement discovered by audit

The existing II.9 graph reconstructed proof dependency, analogy, explicit non-dependency and registry outputs, but omitted the source boundary:

> well-defined mathematical recursion does not imply finite memory, computability or efficiency.

Therefore M6-REL adds explicit negative relations:

```text
II.9 --DOES_NOT_IMPLY--> FINITE-MEMORY
II.9 --DOES_NOT_IMPLY--> COMPUTABILITY
II.9 --DOES_NOT_IMPLY--> EFFICIENCY
```

This is a structural result: a useful relational description needs negative/modal edges, not only positive dependencies.

## 3. GO-G4 relational description

The G4 source says that positional-superko memory is insufficient under situational superko, while the situation-history representation is sufficient. The graph therefore records:

```text
GO-G4 --MEMBER_OF--> GO-MEMORY-REGRESSION
GO-G4 --REQUIRES_CONTRACT--> SSK-CONTRACT
GO-G4 --FALSIFIES--> PSK-MEMORY
GO-G4 --SUPPORTS--> SSK-MEMORY
```

The node can remain a thin identity anchor; these relations recover why it exists and what it says in the shared memory.

## 4. II.11 bridge relational description

The PSI bridge is kept distinct from the classical theorem. Its profile includes:

```text
II.11.PSI-BRIDGE --BRIDGE_DEPENDS_ON--> II.7
II.11.PSI-BRIDGE --BRIDGE_DEPENDS_ON--> II.8
II.11.PSI-BRIDGE --EXEMPLIFIES--> II.9
II.11.PSI-BRIDGE --EVIDENCE_FOR--> C18
II.11.PSI-BRIDGE --REQUIRES_CONTRACT--> NERODE-LANGUAGE-CONTRACT
II.11.PSI-BRIDGE --IDENTIFIES_WITH--> NERODE-EQUIVALENCE
```

The classical aspect must not inherit the PSI dependencies merely because both live in the same document.

## 5. Frozen success condition

`M6-REL` passes only if `scripts/test_relation_description.py` reconstructs all declared structural facets from relation direction/type/neighbor identity while ignoring prose labels and edge notes, and if classical/PSI separation remains intact.

Expected status:

\[
\boxed{\mathrm{PASS\_WITH\_BOUNDARY}}
\]

because structural description is not identical to internal mathematical content.

## 6. Architectural interpretation

If M6-REL passes, the working decomposition becomes:

\[
\boxed{\text{POINT}=\text{identity/content anchor}}
\]

\[
\boxed{\text{RELATIONS}=\text{structural description}}
\]

\[
\boxed{\text{PROVENANCE}=\text{why each relation is licensed}}
\]

This is stronger than a document graph but weaker than claiming that the entire theorem can be eliminated from the node.
