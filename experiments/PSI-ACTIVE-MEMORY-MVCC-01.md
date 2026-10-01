# PSI-ACTIVE-MEMORY-MVCC-01

Status: EXPERIMENTAL / NON-CANONICAL  
Branch: `psi-memory-map-01`

## Object

Replace the correctness-reference `deepcopy` transaction publish path with a local optimistic MVCC path over the active-memory runtime.

This is an execution-layer experiment. It does not add a PSI primitive, does not create M20, and does not change CORE5.

## Contract

Each semantic write slot has a version stamp:

`V(s) = revision of the last committed mutation of slot s`.

A proposal is:

`P = (proposal_id, actor_id, base_revision, event, read_set)`.

Its write slot is determined by the event. For example:

- edge mutation: `EDGE|source|relation|target`
- node-status mutation: `NODE_STATUS|node`

A proposal authored at revision `b` may commit at a later global revision `r >= b` iff every declared read slot and its write slot satisfy:

`V(s) <= b`.

Therefore an unrelated commit elsewhere does not itself force rebase.

## Batch rules

1. Contradictory writes to one semantic slot -> `CONFLICT`.
2. Identical writes may coalesce, but every proposal is still version-validated.
3. If one proposal reads a slot written by another proposal in the same batch -> `CONFLICT`.
4. If any declared read/write slot changed after a proposal snapshot -> `REBASE_REQUIRED`.
5. Actor identity, arrival order, or lexical seniority grants no priority.
6. `FORUM_OBJECT_SEEN` is not a mutation and cannot hitchhike inside an admitted transaction.
7. Known conflicts and stale reads fail before mutation; no partial semantic write is permitted.

## Cost discipline

The hot commit path must not:

- `deepcopy` the full workspace;
- scan all edges;
- recompute the full semantic digest.

Instead it validates only declared read/write version stamps and applies the local delta through `ActiveRuntime`.

A full semantic digest remains available on demand for regression/audit outside the measured hot path.

The runtime maintains a separate incremental commit-chain digest:

`H_{t+1} = H(H_t, revision, committed writes)`.

This digest is an audit chain, not a replacement for the full semantic state digest.

## Success / STOP

PASS_WITH_BOUNDARY requires:

- same-snapshot independent writes commit atomically;
- final semantic state matches the previous deep-copy transaction oracle;
- an old snapshot may still commit if all its declared read/write slots are unchanged;
- stale declared read and stale write slot both require rebase;
- intra-batch read/write hazards fail closed;
- contradictory writes fail closed with no partial write;
- identical intents coalesce without actor priority;
- FORUM observation cannot hitchhike;
- scaling witness examines a fixed two version stamps while unrelated memory grows by 256x;
- previous memory regressions remain green.

Timing is measurement only and never a correctness oracle.

## Boundary

The reference implementation is single-process and assumes crash-free execution after successful preflight. It does not yet provide operating-system threads, durable WAL, crash recovery, distributed clocks, distributed consensus, live FORUM writes, or GPU execution. Read sets are explicit: undeclared semantic dependencies cannot be protected by MVCC automatically.
