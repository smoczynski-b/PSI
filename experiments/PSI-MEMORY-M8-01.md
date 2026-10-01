# PSI-MEMORY-M8-01 — end-to-end licensed retrieval

**Status:** EXPERIMENTAL / FROZEN TASK / PASS  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Frozen task

Starting from `GO-G4`, prepare the smallest bounded agent context that can answer:

> What does G4 establish about sufficient memory, and how is that regression connected to II.7 and II.9?

The retrieval radius is `3`.

## 2. Admissible material

The context builder may emit only:

1. thin node identities reached from the task anchor;
2. typed relation edges with certified provenance;
3. evidence fragments whose current status is exactly `VALID`.

`STALE`, `SOURCE_DRIFT`, uncertified edges and whole-source fallback are excluded from strict retrieval.

The builder must not infer a missing bridge from textual similarity.

## 3. Distant bridge certification

M8 extends M7 with two independently certified fragments:

- `EV-GO-II7` — section `## 9. R02 — Go jako regres pamięci` in II.7;
- `EV-GO-II9` — section `## 10. Go jako regres kongruencji` in II.9.

`GO-G4 --MEMBER_OF--> GO-MEMORY-REGRESSION` reuses the already certified G4 fragment `EV-G4`.

Thus the M3 path is licensed as:

```text
GO-G4
  --MEMBER_OF--> GO-MEMORY-REGRESSION
  --REGRESSION_FOR--> II.7
  --REGRESSION_FOR--> II.9
```

The bridge has navigation/regression semantics, not theorem-premise semantics.

## 4. Success criteria

M8 passes only if:

- the generated radius-3 context contains the expected certified relation set;
- all emitted evidence is deduplicated and `VALID`;
- the complete serialized context is under 10% of the frozen M4 broad baseline;
- simulated `STALE` on `EV-GO-II9` removes II.9 and its descendants while preserving the independent Go→II.7 bridge;
- simulated `SOURCE_DRIFT` on the same evidence is also excluded by strict retrieval, without asserting that II.9 is false.

## 5. Scope

M8 tests memory retrieval architecture. It does not execute an LLM and therefore does not establish equal answer quality or lower model token consumption. Those remain the separate M4b question.
