# PSI-MEMORY-M7-EDGE-CERT-01

**Status:** EXPERIMENT PROTOCOL / FROZEN BEFORE FINAL REGRESSION  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## Question

Can a typed PSI memory relation be treated as a first-class certified object whose license is a fragment-addressable source witness rather than an entire source file?

## Object

For selected relation edges

\[
e=(v,r,u)
\]

attach a provenance record

\[
\operatorname{Prov}(e)=E_j
\]

where the evidence fragment carries

\[
E_j=(\text{path},\text{selector},\text{verified blob},\text{fragment SHA-256},\text{certification commit}).
\]

Multiple edges may legitimately share one evidence fragment.

## Frozen witnesses

Ten existing graph edges are mapped to six source fragments. The set includes hard dependency, explicit non-dependency, negative implication boundary, contract-relative falsification/support and exact PSI/Nerode identification.

## Status semantics

- `VALID`: selector resolves, fragment hash matches, and current file blob matches the certified file blob.
- `SOURCE_DRIFT`: selector resolves and fragment hash still matches, but the containing file blob changed. This is a context/version recheck signal, not an automatic refutation of the relation.
- `STALE`: selector no longer resolves or the selected fragment hash changed.

A relation cannot certify itself; the frozen fragment hash was emitted by an earlier CI run and only afterwards copied into the certificate table.

## Pass criteria

M7 passes iff:

1. all ten certified edge tuples exist in the current memory graph;
2. all six selectors resolve exactly and their current SHA-256 hashes match the frozen values;
3. the historical Git blob anchors match the source versions used at certification time;
4. a simulated mutation of one evidence fragment marks exactly the edges mapped to that evidence as `STALE`, and no unrelated edge;
5. shared evidence invalidates all and only its dependent edges;
6. fragment-level evidence is strictly smaller than loading the four complete source files;
7. M1–M6 remain passing.

## Scope boundary

A valid M7 certificate establishes source/provenance integrity of the relation record. It does **not** independently prove the mathematical truth of the relation. Epistemic truth remains governed by the PSI contract, mathematical proof/test status and dependencies.
