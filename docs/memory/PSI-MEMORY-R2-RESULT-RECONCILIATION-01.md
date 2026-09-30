# PSI-MEMORY-R2-RESULT-RECONCILIATION-01

**Status:** PASS_WITH_BOUNDARY  
**Date:** 2026-09-30  
**Branch:** `psi-memory-map-01`  
**Audit baseline:** `306e0706586c0e005450dda097b55c066f22ec45`  
**Servant correction:** `ea45008d2e476008ab7e70cff1950f3673e3c86e`  
**Access correction:** `3ff8b3522c3a1ea7d3cc0cb59de29cb7d8dfdb6b`  
**Final witness:** `1f79a752c9f4c87f2e870fcc1fecdbe0c1e35f2f`  
**Failing reproduction:** workflow run `36770611699`  
**Passing verification:** workflow run `36771111707`

## 1. Object and auditor invariant

R2 repairs the gap between locally durable projections of one logical operation:

```text
MEMORY COMMIT
    -> SERVANT_RESULT
    -> ACCESS_MOVEMENT
    -> ACCESS_RESULT
```

The governing audit rule inherited from **Semantica Rozmowy — 03** is:

```text
local projection success != global operation success
```

Equivalently, a valid component projection `P_i(S)` does not identify the whole
state `S`. Therefore R2 is accepted only when the projections reconcile to one
durable operation identity after crash/restart.

For a committed movement request `r` with transaction `tx(r)` the required
post-recovery invariant is:

```text
COMMIT(tx(r))
=> exactly one durable state transition
 + one canonical ACCESS_MOVEMENT
 + one canonical completed outcome for r
```

while a changed payload under the same request/command identifier remains a
collision rather than a replay.

## 2. Reproduced defect

The separating witness was executed before the correction. Workflow run
`36770611699`, job `result-reconciliation-r2`, failed at the Servant boundary:

```text
memory COMMIT exists
SERVANT_RESULT absent
restart
exact command replay
=> BLOCK_ILLEGAL_TRANSITION / DURABLE_PROTOCOL:ValueError
```

Thus R2 was reproduced as an execution defect, not inferred only from source
inspection.

## 3. Servant reconciliation

`ServantRuntime` now records the transaction identity in `SERVANT_OBSERVED` and,
on construction, reconciles an unfinished observed command against verified
memory-WAL `COMMIT` records.

If and only if the observed transaction is committed and the command kind is a
transactional kind, the runtime materializes a recovered `SERVANT_RESULT` with
the original command fingerprint and transaction identity. An exact replay then
uses ordinary idempotence; it does not submit the transaction again.

A different command under the same `command_id` still produces
`COMMAND_ID_COLLISION`.

## 4. ACCESS_STEWARD reconciliation

A new `ACCESS_PREPARED` record is written after policy/cost validation and before
calling Servant. It binds:

```text
request fingerprint
<-> servant command fingerprint
<-> txid
<-> historical location_before/location_after
<-> estimated/actual cost
```

On restart ACCESS_STEWARD reconciles only against a verified memory `COMMIT` and
a matching completed Servant command. It then restores a missing canonical
`ACCESS_MOVEMENT` and/or `ACCESS_RESULT` without:

- executing the durable transition again;
- calling the cost meter again;
- rebuilding the original proposal at a newer base revision;
- inferring the historical result from the session's current location.

This last condition is essential: a later independent committed movement may
move the session elsewhere while the recovered older request must still retain
its historical before/after pair.

## 5. Separating cases

`scripts/test_result_reconciliation_r2.py` verifies:

1. memory COMMIT exists, `SERVANT_RESULT` absent;
2. ACCESS COMMIT exists, both `ACCESS_MOVEMENT` and `ACCESS_RESULT` absent;
3. `ACCESS_MOVEMENT` exists, `ACCESS_RESULT` absent;
4. an older incomplete ENTER is followed by an independent committed TRANSIT;
5. restart and exact replay preserve the original historical result while the
   current location remains the result of the later movement;
6. the cost meter is not called again;
7. no second memory COMMIT is produced;
8. changed payload under the same command/request identifier is rejected as a
   collision.

## 6. Verification

Workflow run `36771111707`, job `110077446427`, completed with `success`.
All relevant steps passed:

```text
R2 separating witness
Servant regression
Access steward regression
Shared WAL regression
```

The existing ACCESS_STEWARD and R1 durability workflows also remained green on
the access-reconciliation implementation commit.

## 7. Boundary

The result remains a deterministic single-process recovery protocol over local
append-only journals. It does not establish distributed exactly-once execution,
multi-process serialization, or external transactional atomicity across storage
systems.

The reconciliation mechanism applies to operations carrying the new durable
binding records. Historical journal entries written before those bindings are
not retroactively assigned identities by inference.

## 8. Verdict

```text
R2 RESULT RECONCILIATION = PASS_WITH_BOUNDARY
```

After R0, R1 and R2, the work front is re-evaluated as required. No contrary
new evidence changes the ordering: the next unresolved blocking unit is
`R3 — visual digest verification`.

No change to CORE5, CANON-03, theorem status, constitutional role split or live
FORUM state.
