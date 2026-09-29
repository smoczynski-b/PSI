# PSI-MEMORY-M7-RESULT-01

**Status:** PASS  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36624193308` executed M1–M7 successfully.

M7 certified ten existing relation edges using six unique fragment-addressable evidence records.

Measured evidence size:

- certified edges: `10`;
- unique evidence fragments: `6`;
- unique fragment bytes: `2165`;
- naive duplicated per-edge evidence bytes: `3543`;
- four complete source files: `73277` bytes;
- fragment/full ratio: `0.0295`;
- reduction against complete source files: `97.05%`.

## 2. Certified relation classes

The witness set includes:

- `HARD_DEPENDS_ON`;
- `NOT_DEPENDS_ON`;
- `DOES_NOT_IMPLY`;
- `FALSIFIES`;
- `SUPPORTS`;
- `REQUIRES_CONTRACT`;
- `IDENTIFIES_WITH`.

The evidence set contains exact-line selectors and Markdown-heading section selectors.

## 3. Integrity semantics

M7 distinguishes three states:

\[
\boxed{\mathrm{VALID}}
\]

when both the fragment hash and containing-file version match the certified state;

\[
\boxed{\mathrm{SOURCE\_DRIFT}}
\]

when the selected fragment remains byte-identical but the containing file version changes;

\[
\boxed{\mathrm{STALE}}
\]

when the selected fragment changes or no longer resolves.

This prevents a change elsewhere in a large registry from being silently treated as a change to every certified relation, while still exposing source-version drift for recheck.

## 4. Selective invalidation

The regression mutates each evidence fragment in simulation and verifies that exactly the edges mapped to that fragment become stale.

Two explicit shared-evidence witnesses are retained:

- `EV-II9-LIMIT` supports three `DOES_NOT_IMPLY` edges;
- `EV-G4` supports three Go-G4 contract/falsification/support edges.

Thus one evidence object may license several relations without duplicating its source text.

## 5. Architectural conclusion

The memory object now has four separable layers:

\[
\boxed{V=\text{thin identity/content anchors}}
\]

\[
\boxed{E=\text{typed structural relations}}
\]

\[
\boxed{P=\text{fragment-addressable provenance/evidence}}
\]

\[
\boxed{S=\text{validity state derived from evidence and dependencies}}
\]

A relation is therefore no longer a bare line between two nodes. It is a first-class object with its own identity, evidence dependency and validity state.

## 6. Scope boundary

M7 certifies provenance integrity, not mathematical truth. A matching hash proves that the relation still points to the certified source fragment; it does not by itself establish that the source statement is mathematically correct. Mathematical status remains governed by PSI proof/test/contract dependencies.

## 7. Next target

The next architectural question is whether these certified relations can generate a compact task object automatically:

\[
\text{task anchor}\to\text{relation profile}\to\text{only licensed evidence fragments}\to\text{agent context}.
\]

This would combine M3 reachability, M5 automatic pack generation, M6 relational description and M7 certified fragment provenance into one end-to-end memory retrieval path.
