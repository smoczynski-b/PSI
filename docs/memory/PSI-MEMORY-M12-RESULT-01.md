# PSI-MEMORY-M12-RESULT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36628431632` executed M1–M12 successfully. M12 tested task-relative retrieval inside a dense local neighbourhood rather than against remote noise.

Anchor:

\[
\boxed{\mathrm{II.9}}
\]

Task contract:

> retrieve proof prerequisites and explicit scope/boundary statements of II.9.

Measured local pool:

\[
|V_{local}|=25,
\qquad
|E_{local}|=37.
\]

Selected task view under edge budget \(B_E=12\):

\[
|V_{task}|=10,
\qquad
|E_{task}|=12.
\]

Hence

\[
\frac{|E_{task}|}{|E_{local}|}
=\frac{12}{37}
\approx 0.3243.
\]

The selector used 32.43% of the available nearby relations.

## 2. Selected relation profile

The selected view contains exactly:

- `II.9 HARD_DEPENDS_ON II.7`;
- `II.9 USES_DEFINITION C57`;
- `II.9 USES_LEMMA C58`;
- `II.9 NOT_DEPENDS_ON II.8`;
- `II.9 DOES_NOT_IMPLY BIT-MINIMALITY`;
- `II.9 DOES_NOT_IMPLY COMPUTABILITY`;
- `II.9 DOES_NOT_IMPLY EFFICIENCY`;
- `II.9 DOES_NOT_IMPLY FINITE-MEMORY`;
- `II.7 HARD_DEPENDS_ON II.4`;
- `II.7 USES_DEFINITION C57`;
- `II.7 USES_LEMMA C58`;
- `C58 HARD_DEPENDS_ON C57`.

The M9 `BIT-MINIMALITY` edge remains backed by its fragment-level certificate. The other eleven selected edges are `ROUTING_ATTESTED` in this experiment: present in the current audited memory map and linked to repository source paths, but not re-proved by M12.

## 3. Relation type as navigation semantics

M12 makes the following distinction executable:

\[
\boxed{
\text{edge meaning}
\longrightarrow
\text{edge traversal rule}.
}
\]

For this task:

- `HARD_DEPENDS_ON`, `USES_DEFINITION`, `USES_LEMMA` may expand their targets;
- `NOT_DEPENDS_ON`, `DOES_NOT_IMPLY` are included as semantic boundaries but their targets are terminal.

Thus `II.9 NOT_DEPENDS_ON II.8` records an important fact about II.9 without causing the retriever to expand all dependencies and results of II.8.

Likewise `DOES_NOT_IMPLY FINITE-MEMORY` describes the theorem's boundary without treating `FINITE-MEMORY` as a new search root.

## 4. Local competition witness

The local pool contains multiple legitimate relation families and alternative routes to the same objects. In particular both direct and mediated routes to `C57/C58` are present:

\[
II.9\to C57,
\qquad
II.9\to II.7\to C57,
\]

and analogously for `C58`.

M12 confirms that the deterministic selector recovers the same task view when the physical order of candidate edges is reversed.

Therefore:

\[
\boxed{
\text{selection result is contract-driven, not file-order-driven}.
}
\]

## 5. What was excluded

Nearby, legitimate relations such as `ANALOGY_TO`, `EVIDENCE_FOR`, `EXEMPLIFIES`, `CONTAINS`, `CONTRASTS_WITH` and `REGRESSION_FOR` remain in memory but do not enter this task view.

This is not rejection of those relations. It is a task projection:

\[
\boxed{
\mathcal M_{usable,\mathcal T}
\subsetneq
\mathcal M_{nearby}.
}
\]

## 6. Architectural conclusion

M11 established that remote disconnected growth need not enlarge task context. M12 establishes the stronger local statement for this witness:

\[
\boxed{
\text{nearby and validly mapped knowledge}
\not\Rightarrow
\text{automatic context inclusion}.
}
\]

Typed relations can serve simultaneously as:

1. structural description of an object;
2. validity/invalidation channels where applicable;
3. task-relative navigation instructions.

This strengthens the working architecture from a typed graph to a **task-interpreted typed graph**.

## 7. Boundary

M12 is not a theorem-level certification run for all 37 nearby relations. `ROUTING_ATTESTED` means current mapped/source provenance, not independent semantic proof. It also does not establish an optimal selector or solve arbitrary task interpretation.

The next unresolved problem is therefore no longer basic graph traversal. It is **task-to-contract compilation**: how a natural task should generate the relation policy and budget without manually writing `m12-task-contract.tsv`.
