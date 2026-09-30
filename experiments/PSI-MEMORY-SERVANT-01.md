# PSI-MEMORY-SERVANT-01

**Status:** EXPERIMENT / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Depends on:** `PSI-MEMORY-INSTITUTION-01`, active-memory MVCC/shared/WAL experiments.

## Goal

Implement the first institutional actor from `PSI-MEMORY-INSTITUTION-01`: a deliberately narrow deterministic `SERVANT` that supervises procedural state transitions without natural-language deliberation or domain epistemic authority.

The servant accepts only typed `ServantCommand` objects and returns one of:

\[
\boxed{
ACK\_TRANSITION,
\quad BLOCK\_ILLEGAL\_TRANSITION,
\quad STOP\_ESCALATE\_CHRONICLE.
}
\]

It does not decide whether a domain claim is true or false.

## Architecture

```text
typed ServantCommand
        |
        v
 procedural classifier
   /       |       \
 ACK      BLOCK     STOP+ESCALATE
  |                   |
  v                   v
MVCC/WAL          append-only servant chronicle
```

Legal memory mutations still pass through `DurableSharedMemoryRuntime`; the servant never writes authoritative workspace state directly.

## Legal transition classes

- `TRANSACT`: submit a typed MVCC proposal batch through durable WAL/MVCC;
- `RECOVER`: invoke the already defined deterministic WAL replay;
- `COMPENSATE`: execute a new transaction only through a pre-authorized runbook and only against a previously durable `COMMIT`.

A compensation must use a fresh `txid`:

\[
\boxed{
correction\neq history\ rewrite.
}
\]

## Explicitly blocked classes

- `REWRITE_DURABLE_HISTORY`;
- `DELETE_COMMITTED_HISTORY`;
- `DIRECT_WORKSPACE_MUTATION`;
- `SEMANTIC_VERDICT`.

Constitution changes/conflicts and unknown transition classes do not trigger ad hoc repair. They yield:

```text
STOP
ESCALATE
CHRONICLE
```

## Chronicle

The servant has a separate fsync-backed JSONL hash-chain chronicle. It records observed commands, escalation events and procedural results. Corruption of an existing complete record fails closed.

Repeated commands are idempotent at the servant boundary:

- same `command_id` + same command fingerprint: preserve the original disposition without re-executing memory mutation;
- same `command_id` + different fingerprint: `STOP_ESCALATE_CHRONICLE` with `COMMAND_ID_COLLISION`.

Thus replay of a prior `BLOCK` or `STOP` can never silently become `ACK`.

## Frozen witnesses

1. legal transaction -> durable `COMMIT` -> `ACK_TRANSITION`;
2. exact command replay -> same disposition, no second authoritative commit;
3. history rewrite/direct mutation/semantic verdict -> `BLOCK_ILLEGAL_TRANSITION` before memory WAL mutation;
4. constitution change or unknown typed transition -> `STOP_ESCALATE_CHRONICLE`;
5. free natural-language input -> rejected by type boundary, not interpreted;
6. transaction-shaped but MVCC-invalid request -> procedural `BLOCK`, not truth verdict;
7. compensation -> requires authorized runbook, prior committed tx and fresh txid;
8. crash after durable `COMMIT` -> typed `RECOVER` delegates to existing WAL replay;
9. tampered servant chronicle -> fail closed.

## Pass condition

`PASS_WITH_BOUNDARY` requires all frozen witnesses above and no regression of the existing memory stack.

## Boundary

This is a deterministic single-process reference automaton. It has no anomaly detector, no natural-language reasoning, no autonomous constitution changes, no domain-truth authority, no distributed coordination and no immunity behavior. `IMMUNE` remains the next separate role only after this servant is stable.
