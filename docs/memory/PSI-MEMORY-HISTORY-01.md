# PSI-MEMORY-HISTORY-01 — II.7–II.12 dependency laboratory

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Scope:** II.7–II.12 plus claim-level dependencies needed to represent validity correctly.

## 1. Why this sector

II.7–II.12 is a natural memory laboratory because it separates:

- future-task equivalence;
- exact memory adequacy;
- coarsest exact quotient;
- recursive quotient update;
- stochastic quotient autonomy;
- exact future-test realization (Myhill–Nerode);
- finite partition-refinement algorithms (Paige–Tarjan).

The sector therefore contains both semantic memory questions and classical realization/algorithmic bridges.

## 2. First dependency tree: exact-history core

```text
C57  future task tree / history equivalence
 |
 +--> C58  equivalence-relation lemma
 |      |
 |      +----------------------+
 |                             |
 +-----------------------> II.7 exact memory adequacy
                              |
                 +------------+------------+
                 |                         |
                 v                         v
              II.8                      II.9
       coarsest exact quotient     recursive quotient update
                 |                         |
                 v                         +--> C45
                C44                        +--> C59

II.4 ---> II.7
II.2 ---> II.8
II.6 - - - ANALOGY - - -> II.9
II.8 - - NOT_DEPENDS_ON -> II.9
```

`II.9 NOT_DEPENDS_ON II.8` is first-class negative structural information. It prevents an agent from reconstructing a false proof chain merely because II.8 precedes II.9 editorially.

## 3. Second tree: bridge aspects must be split from classical content

A document cannot always be a validity atom.

### II.10

```text
II.10
├── II.10.CLASSICAL   Kemeny–Snell lumpability theorem
└── II.10.PSI-BRIDGE task equivalence vs stochastic quotient autonomy
```

### II.11

```text
II.11
├── II.11.CLASSICAL   Myhill–Nerode theorem
└── II.11.PSI-BRIDGE exact PSI/Nerode realization
       ├── BRIDGE_DEPENDS_ON II.7
       └── BRIDGE_DEPENDS_ON II.8
```

### II.12

```text
II.12
├── II.12.CLASSICAL   Paige–Tarjan algorithm
└── II.12.PSI-GATE    PT1–PT4 applicability gate
```

This is a structural requirement, not editorial refinement. Revoking a PSI bridge must not mark the underlying classical theorem/algorithm as false.

## 4. Architectural result H1 — granularity is semantic

The memory node cannot be identified mechanically with a file, paragraph, theorem number or chat turn.

The validity atom is the smallest unit that can change epistemic status independently.

Therefore a future node schema needs at least:

- stable semantic ID;
- source location;
- type;
- status;
- contract/scope;
- optionally a parent document/container.

`II.11.CLASSICAL` and `II.11.PSI-BRIDGE` are the first concrete witness that one source document may contain several independently validatable memory nodes.

## 5. Architectural result H2 — edges need propagation semantics

A relation label alone is insufficient. The same graph must distinguish whether invalidity propagates across an edge.

The experiment adds `effect`:

- `VALIDITY` — invalidity/staleness propagates from prerequisite to dependent;
- `BRIDGE_VALIDITY` — propagation affects the bridge layer but not the independent source theorem;
- `NONE` — structural/provenance/analogy/negative information only.

Thus:

```text
II.9 --HARD_DEPENDS_ON/VALIDITY--> II.7
II.9 --ANALOGY_TO/NONE-----------> II.6
II.9 --NOT_DEPENDS_ON/NONE-------> II.8
```

Automatic closure must use `(relation,effect)`, not adjacency alone.

## 6. M1 — ancestry separation

For `II.9`, the validity ancestry must include:

- `II.7`;
- `C57`;
- `C58`;
- `II.4` through II.7.

It must **not** include:

- `II.6` merely because of structural analogy;
- `II.8`, which is explicitly not a proof prerequisite.

For `II.11.PSI-BRIDGE`, bridge ancestry may include II.7/II.8, while `II.11.CLASSICAL` has no PSI validity ancestry.

## 7. M2 — invalidation simulation

Test mutation:

```text
C57 := REVOKED
```

Expected stale closure in the current sector includes at least:

```text
C58
II.7
C42
II.8
C44
II.9
C45
C59
II.11.PSI-BRIDGE
C18
```

Expected unaffected nodes include:

```text
II.6
II.10.CLASSICAL
II.10.PSI-BRIDGE
II.11.CLASSICAL
II.12.CLASSICAL
II.12.PSI-GATE
C13
C14
```

This demonstrates selective invalidation rather than global re-audit.

## 8. Certificate consequence

A future PSI certificate should bind not only a result and source hash, but also the exact prerequisite IDs and the propagation class used by that certificate.

Conceptually:

\[
Cert(v)=\bigl(v,scope,deps,evidence,status,hash\bigr).
\]

When a dependency changes, the system should locate only the affected descendants in the validity graph.

This is the mechanism by which one agent may safely reuse another agent's certified work without re-reading the whole project.

## 9. Blockchain note

Blockchain is relevant, but at a different layer.

The current repository already gives us a content-addressed, hash-linked version history through Git. That is sufficient for the first experiment in provenance, reproducibility and rollback.

A blockchain/distributed ledger could later provide an **external anchoring/witness layer** for selected certificate roots, for example:

\[
root_t = H(\text{certified memory state at }t).
\]

Its possible roles are:

- timestamped external witnessing;
- multi-party append-only anchoring;
- reducing dependence on one repository host;
- federation of mutually distrustful organizations/agents.

It should not initially store the graph itself. Consensus, transaction cost and replication do not solve semantic typing, dependency correctness or certificate scope.

Therefore the current architectural order is:

```text
MEMORY GRAPH
    -> PSI CERTIFICATE / dependency root
        -> optional external ledger anchor
```

not:

```text
blockchain -> memory semantics
```

## 10. Current verdict

The II.7–II.12 sector already forces five architectural properties:

1. graph storage, tree views;
2. semantic node granularity below document level;
3. typed positive and negative edges;
4. edge-specific invalidation semantics;
5. separation of mathematical validity from provenance and external witnessing.

The next test after M1/M2 is M3: one long-range evidenced bridge, followed by bounded retrieval from a local neighborhood.
