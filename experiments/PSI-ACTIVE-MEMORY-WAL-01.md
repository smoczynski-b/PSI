# PSI-ACTIVE-MEMORY-WAL-01

Status: EXPERIMENTAL / NON-CANONICAL / CPU REFERENCE

## Goal

Close the crash-consistency gap between an authoritative MVCC commit and selective propagation into active workspaces.

The target protocol is:

```text
PREPARE -> durable WAL -> COMMIT -> PROPAGATE -> ACK
```

with deterministic recovery from a caller-supplied baseline plus the append-only WAL.

## Contract

A transaction is authoritative after and only after a durable `COMMIT` record exists.

- `PREPARE` without `COMMIT` is ignored during recovery.
- `COMMIT` without `ACK` must be replayed and propagated.
- partial propagation before a crash must converge after restart to the same semantic state as an uninterrupted commit.
- replay must not promote rejected FORUM observations.
- a torn final WAL record may be discarded as crash tail.
- corruption inside the completed hash-chained prefix must fail closed.

The WAL is newline-delimited JSON, each record carrying `seq`, `prev_hash` and `record_hash`. Appends use flush plus `fsync`.

## Recovery model

Recovery rebuilds:

```text
baseline authoritative memory
+ committed WAL transactions
-> authoritative memory at r_t
-> selective workspace routing
-> dependency invalidation
```

Local active workspaces are therefore derived state, not independent authorities.

## Witnesses

1. clean commit and restart equivalence;
2. crash after PREPARE;
3. crash after COMMIT before propagation;
4. crash after exactly one event of a multi-event transaction has propagated, before remaining routing/invalidation;
5. torn final record repair;
6. internal WAL corruption rejection;
7. rejected FORUM observation remains non-authoritative after restart.

## Performance guard

The runtime caches known transaction identifiers in memory. Normal duplicate-`txid` checking is therefore set membership rather than a full WAL scan. Full WAL traversal is restricted to startup/recovery.

## Boundary

This is not yet a production durability claim. It does not provide:

- a durable checkpoint/snapshot store;
- a guarantee across arbitrary filesystem/controller power-loss behavior beyond the process-level `fsync` contract exercised here;
- concurrent multi-process writers;
- distributed clocks or consensus;
- live FORUM mutation;
- GPU execution.

No PSI core primitive is added or changed.
