# PSI-MEMORY-M11-GROWTH-01 — sequential growth, supersession and revocation

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can PSI-MEMORY preserve bounded task retrieval while the global memory grows, and can versioned verified records be superseded/revoked without deleting history or silently reactivating older records?

## 1. Important distinction

M11 versions a **memory/certificate record**, not the mathematical proposition itself.

The semantic relation remains:

\[
\mathrm{II.9}\xrightarrow{\mathrm{DOES\_NOT\_IMPLY}}\mathrm{BIT\!\!-
MINIMALITY}.
\]

The records `REC-BIT-v1`, `REC-BIT-v2`, `REC-BIT-v3` are successive certified representations of that same semantic edge.

Therefore:

\[
\boxed{\text{record supersession}\neq\text{claim falsification}.}
\]

## 2. Sequential events

The frozen event sequence is in `m11-record-sequence.tsv`:

1. `v1` active;
2. `v2` supersedes `v1`;
3. add a disconnected synthetic verified-load fixture of 256 nodes and 255 edges;
4. revoke `v2`;
5. reverify as `v3`, which supersedes `v2`.

The load fixture is structural test material only. It is not asserted to be mathematical knowledge.

## 3. Required semantics

- A superseded record remains in audit history but is not active.
- Revoking the active successor must **not** automatically reactivate its predecessor.
- A later explicitly reverified record may reactivate the semantic relation.
- `SUPERSEDES` belongs to version/audit structure and must not leak into the ordinary task graph.
- Irrelevant disconnected growth must not change the `GO-G4`, radius-3 task context.
- The active semantic edge must appear at most once even when several historical records encode it.

## 4. Success predicates

Let `C_t` be the usable radius-3 context from anchor `GO-G4`.

M11 passes iff:

\[
C_0=C_1=C_2,
\]

where step 2 includes the large irrelevant growth fixture,

\[
C_3=C_{pre-M9},
\]

with no fallback to `v1`, and

\[
C_4=C_0.
\]

Additionally the global record count must increase materially while the serialized task context at the growth step remains byte-for-byte unchanged.
