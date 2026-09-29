# PSI-MEMORY-M5-01 — automatic task-pack generation

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Motivation

M4a showed that a hand-prepared memory-guided pack can reduce raw input substantially. That is not yet a real memory system because a human/agent manually selected the guided manifest.

M5 tests the first automatic retrieval chain:

\[
\boxed{\text{task anchor}\to\text{bounded graph view}\to\text{node source pointers}\to\text{source pack}.}
\]

No embeddings, vector database or LLM source selection are used.

## 1. Frozen start condition

Start node:

```text
GO-G4
```

Directed radius:

```text
3
```

Admitted navigation relations are exactly the M3 relations:

- `MEMBER_OF`;
- `REGRESSION_FOR`;
- `HARD_DEPENDS_ON`;
- `USES_DEFINITION`;
- `USES_LEMMA`.

The expected node view is:

```text
C57
C58
GO-G4
GO-MEMORY-REGRESSION
II.4
II.7
II.9
```

## 2. Automatic source resolution

`scripts/build_memory_pack.py` reads the three node tables and two edge tables. It performs the bounded traversal and takes the `source` field from each reached node.

Duplicate file sources are collapsed. Non-file/external sources are reported separately rather than silently invented.

For this view the generated file pack is expected to be:

```text
docs/claim-registry.md
docs/go-memory-regression-01.md
docs/principia-v2-04-representation-adequacy.md
docs/principia-v2-07-exact-history-memory-adequacy.md
docs/principia-v2-09-recursive-history-quotient-update.md
```

The deterministic snapshot is stored in `experiments/m5-generated-manifest.txt` and CI rejects drift.

## 3. Success gate

The automatically generated pack must:

1. reproduce the seven-node M3 view;
2. retain the four task-critical mathematical sources frozen in M4;
3. resolve no unknown external source in this test;
4. reproduce its checked-in deterministic manifest;
5. including manifest overhead, remain at or below 50% of the M4 broad-baseline byte size.

This is an engineering compression gate, not a theorem about LLM performance.

## 4. Granularity hypothesis

M5 deliberately exposes the next likely architectural bottleneck.

Nodes `C57` and `C58` currently point to the whole stable file:

```text
docs/claim-registry.md
```

rather than to addressable claim fragments. Therefore a correct automatic traversal may pull tens of kilobytes to obtain two small semantic atoms.

If M5 passes while showing this overhead, the next target is not a more complex graph database. It is finer source addressing, for example:

\[
\boxed{\text{node}\to(\text{file},\text{stable fragment/range/hash})}
\]

with provenance preserved.

## 5. Scope

M5 does not claim that the generated pack is globally minimal. It tests whether the graph can itself produce a bounded, source-complete pack without hand-picking the files.