# Memory map runtime adapter

Disclosure: PUBLIC for the adapter, CLI change, acceptance test, this document,
and the generated receipt below. Inputs are already versioned map metadata.
No conversation exports, private drafts, credentials, or host telemetry are included.

## Ordinary entry point

From the repository root:

```text
python -B scripts/memory_retrieval.py MATH-57
python -B scripts/memory_retrieval.py MATH-69
python -B scripts/memory_retrieval.py --map-node MATH-57
python -B scripts/memory_retrieval.py --revoke MATH-57-ERRATA
python -B scripts/memory_retrieval.py --revoke C57
```

An exact MATH node ID uses the pinned map reader. Other positional tasks retain
the existing multilingual contract compiler and retrieval behavior. This adds
an explicit structured query mode; it is not general semantic question answering.

Navigation returns original node records and original directed edge records,
within two incidence steps. It reports SOURCE_SEEN for metadata, does not fetch
source bodies, and never executes source content. MATH-57 returns the active
errata and MATH-61, preserving the declared (A,Used) correction. MATH-69 returns
its original source and a separate independent-review record. Their stored
proof-review statuses are not new mathematical certifications. Enumeration is
not rerun.

Revocation is a read-only simulation using the existing stale_closure algorithm
over history + bridges with explicit effect in VALIDITY, BRIDGE_VALIDITY, NONE.
The navigation overlay is never passed to that algorithm and never gains a
synthetic effect. No persisted node status is changed.

## Provenance and HOLD

Source commit: 38adb94c7f1f99374621017c33fbe4048602d922.
The loader checks exact TSV schemas, nonempty fields, unique node IDs, node
types/statuses, layer/effect types, and all endpoints. It compares all eight
input files to Git blobs at the source commit, with independently declared
pins for the two overlay tables and the map document. Missing or divergent
inputs produce HOLD with exit code 2 and no partial result.

The source commit must be available in the local Git object database. Later
changes to pinned input files intentionally require a reviewed pin update;
the loader does not silently accept the current branch tip. Code commits can
advance independently while input files remain pinned.

## Acceptance and limits

```text
python -B scripts/test_memory_map_runtime.py --receipt receipt.json
```

Receipt: [memory-map-runtime-20261024-receipt.json](../../experiments/memory-map-runtime-20261024-receipt.json).

The integrated acceptance returned PASS_SCOPED for:
- Ordinary MATH-57/MATH-69 CLI queries and exact source locators, statuses,
  original edge directions and the declared (A,Used) correction.
- No stale descendants from either navigation root MATH-57-ERRATA or MATH-61.
- C57 descendants equal to the original algorithm, with no MATH propagation.
- Explicit HOLD for malformed schema/fields, invalid node/layer/effect/relation,
  unknown endpoint/query, unavailable commit, changed worktree blob, and a
  divergent declared blob. Conflicting query modes also HOLD.
- Existing M1/M2/M3 and M13 task-contract regression programs, exit code 0.

Scope: a real ordinary CLI running in an isolated local repository checkout,
with reproducible source and test code. This is not a certificate of production
deployment, agent-session adoption, theorem truth, or independent enumeration.
No services, schedules, source PDFs, CORE5, IFX, or PostgreSQL were changed.
