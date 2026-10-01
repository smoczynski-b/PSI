# PSI-ACTIVE-MEMORY-CONCURRENCY-01

Status: EXPERIMENTAL / NON-CANONICAL  
Branch: `psi-memory-map-01`

## Object

Reference transaction semantics for concurrent agent proposals targeting one active PSI workspace.

This is an execution-layer experiment. It does not add a PSI primitive, does not create M20, and does not modify CORE5.

## Contract

Each proposal is

`P = (proposal_id, actor_id, base_revision, event)`.

The active workspace has an explicit revision `r`.

A batch may commit only if every proposal was authored against `base_revision = r` and the batch is semantically conflict-free.

Semantic target slots in the reference implementation are:

- `EDGE|source|relation|target`
- `NODE_STATUS|node`

Two proposals are independent when they target different slots. Two proposals with the same slot and the same normalized intent are duplicates and may coalesce. Two proposals with the same slot and distinct normalized intents conflict.

No actor identity, name, arrival position, or lexical ordering grants epistemic authority.

## Transaction rules

1. **Optimistic revision check** — stale/future `base_revision` returns `REBASE_REQUIRED`; there is no silent rebase.
2. **Independent merge** — independent proposals from the same base revision may commit in one atomic transaction.
3. **Duplicate coalescing** — identical intents produce one semantic mutation.
4. **Conflict fail-closed** — contradictory intents on one semantic slot return `CONFLICT`; no proposal in that batch is published.
5. **Atomicity** — a mixed batch containing a conflict or inadmissible event publishes nothing.
6. **FORUM boundary** — `FORUM_OBJECT_SEEN` is not transaction-admissible. Observation cannot hitchhike with a valid semantic mutation.
7. **Order invariance** — permutation of an independent or conflicting batch must not change the semantic result.

## Reference implementation

`ConcurrentWorkspace` applies a candidate batch to a deep-copied trial `ActiveRuntime`. The trial runtime becomes visible only after the full batch succeeds.

This intentionally gives a strong, simple atomicity oracle at the cost of `O(|W|)` copying. It is a correctness reference for a later journal/MVCC implementation, not the scalable target.

## Success / STOP

PASS_WITH_BOUNDARY requires:

- two independent proposals at revision 0 commit together as exactly revision 1;
- all tested proposal permutations produce the same semantic digest;
- identical concurrent intents coalesce to one mutation;
- contradictory intents fail closed with no partial write;
- SET vs REMOVE of the same edge conflicts;
- a proposal from revision 0 is rejected after revision 1 exists;
- a non-admitted FORUM observation causes the entire mixed batch to fail closed;
- all earlier memory/active-memory regressions remain passing.

## Boundary

The experiment models concurrency as proposals sharing one explicit base revision. It does not run OS threads, distributed processes, locks, network transport, consensus, crash recovery, write-ahead logging, MVCC, or live FORUM mutation. `CONFLICT` means the reference transaction layer refuses to choose between incompatible writes; it does not determine which substantive claim is true.
