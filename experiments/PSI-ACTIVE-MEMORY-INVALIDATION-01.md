# PSI-ACTIVE-MEMORY-INVALIDATION-01

Status: EXPERIMENTAL / NON-CANONICAL  
Branch: `psi-memory-map-01`

## Object

Selective invalidation of derived memory records after a source, edge, contract, object, or earlier derived record changes.

This is an execution-layer experiment. It does not add a PSI primitive, does not create M20, and does not change CORE5.

## Contract

Let `R` be the finite set of derived records and let each record `r` carry an explicit dependency set `Dep(r)`.

The runtime maintains the reverse index

`I(d) = { r in R : d in Dep(r) }`.

A changed dependency token `d` invalidates every directly dependent record. A newly stale derived record `r` emits the token `record:r`, so invalidation propagates transitively only through declared dependencies.

The admissible dependency tokens in this reference experiment include:

- `source:*`
- `edge:*`
- `contract:*`
- `record:*`

## Required properties

1. **Selectivity** — unrelated records must remain unchanged.
2. **Transitivity** — if `r2` depends on `record:r1`, invalidating `r1` must invalidate `r2`.
3. **Reference equivalence** — indexed invalidation must return the same stale set as repeated full scans to a fixed point.
4. **No silent FORUM admission** — a FORUM-derived source token can propagate invalidation only for records that already declare that admitted source as a dependency; this experiment does not admit FORUM objects itself.
5. **Work accounting** — after index construction, invalidating one local dependency should examine only the reverse dependency links reached from that dependency, not every unrelated record.

## Synthetic witness

The core dependency chain is:

`source:doc:changing -> workspace snapshot -> analysis:A -> decision:B`.

An admitted FORUM relation is represented independently by the dependency token `source:forum:OID-REL` and reaches the same snapshot because the snapshot actually depends on that source.

A large population of unrelated records is then added. The test varies that unrelated population while keeping the affected chain fixed.

## Success / STOP

PASS_WITH_BOUNDARY requires:

- exact equality with the full-scan oracle;
- exactly three affected derived records in the frozen witness;
- no invalidation of the independent record;
- the admitted FORUM source token to reach the same declared dependents;
- deterministic work accounting bounded by the reached reverse links for the frozen one-source change;
- all earlier memory regressions still passing.

Timing is reported only as measured evidence and is never a CI oracle.

## Boundary

Reference implementation is single-process and deterministic. It does not yet implement concurrent writers, transactions, rollback, distributed clocks, live FORUM mutation, GPU execution, or automatic truth reassessment. `STALE` means "must be rechecked because a declared dependency changed", not "false".
