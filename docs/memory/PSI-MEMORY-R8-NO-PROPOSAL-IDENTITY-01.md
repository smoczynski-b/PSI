# PSI-MEMORY-R8-NO-PROPOSAL-IDENTITY-01

**Status:** `PASS_WITH_BOUNDARY`  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Scope:** F3.3 Curator observation identity hardening.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Defect

Before R8, `CuratorPlannerRuntime` persisted an observation fingerprint only when
that observation generated a `STRUCTURE_PROPOSAL`. A below-threshold evaluation
returned `()` and left no durable observation identity.

Therefore this sequence was legal:

```text
OBS-R8 + payload A -> below threshold -> no record
OBS-R8 + payload B -> above threshold -> accepted as a new observation
```

although `payload B != payload A`.

The separating workflow `36777747371`, job `110099835492`, failed exactly on
that witness:

```text
AssertionError: same observation_id with changed payload was accepted after a
no-proposal observation
```

## Selected identifier semantics

R8 selects the stronger and explicit contract:

```text
observation_id identifies every successfully evaluated Curator observation
within one Curator chronicle, whether or not a proposal is emitted.
```

The observation fingerprint binds:

```text
district_id
metrics
observed_at
policy_version
```

Thus:

```text
same observation_id + same fingerprint -> idempotent replay
same observation_id + different fingerprint -> OBSERVATION_ID_COLLISION
```

The namespace claim is local to one Curator chronicle. R8 does not establish a
distributed/global observation-ID namespace.

## Correction

Implementation commit:

`ea4e1b7e0837a7769f9edfbb780f051c4cc5221e`

For a first-seen observation that matches no planning rule, the Curator now:

1. passes a bounded `NOTICE` through the authorized `CURATOR-PLANNER-01`
   Servant runbook;
2. appends one `CURATOR_OBSERVATION` record;
3. stores the observation fingerprint and bounded outcome `NO_PROPOSAL`;
4. records district, policy version and observation time without fabricating a
   proposal;
5. treats exact replay as idempotent;
6. rejects changed-payload reuse before rule evaluation;
7. reconstructs the identity/outcome from WAL after restart.

A persisted `NO_PROPOSAL` observation and a persisted proposal for the same
observation ID are treated as contradictory outcomes and fail closed at load.

## Regression alignment

F3.3 previously asserted:

```text
below threshold -> no proposal -> no durable record
```

R8 changes only the last implication. The valid contract is now:

```text
below threshold -> no proposal + one bounded durable identity/outcome record
```

The F3.3 regression was aligned at:

`5f30ae6a1ac58c4d3ef346445c5ba9057d3d0a24`

It additionally verifies:

- exact no-proposal replay does not append a second WAL row or Servant notice;
- changed metrics under the same ID fail closed;
- restart preserves the no-proposal identity;
- the no-proposal path cannot bypass the Servant runbook gate;
- authoritative memory revision and workspace digest remain unchanged.

## Acceptance evidence

### Dedicated R8 gate

Workflow run `36778081234`, job `110100949623`: **success**.

Passed together:

- R8 same-process separating witness;
- R8 restart witness;
- F3.3 Curator regression;
- R1 WAL regression;
- Servant regression.

### Independent Curator integration gate

Workflow run `36778081173`, job `110100949251`: **success**.

Passed:

- F3.0 archive contract;
- F3.1 archive runtime;
- F3.2 archive usage;
- F3.3 Curator planner;
- ACCESS_STEWARD;
- Servant;
- institutional constitution.

### Independent WAL gate

Workflow run `36778081276`, job `110100949508`: **success**.

Passed journal recovery plus shared-memory, Servant, access, immune, archive,
archive-usage and Curator regressions.

## Result

```text
R8 no-proposal observation identity = PASS_WITH_BOUNDARY
same ID / changed payload before restart = BLOCKED
same ID / changed payload after restart = BLOCKED
same ID / same payload = IDEMPOTENT
below threshold = NO_PROPOSAL + durable bounded identity
proposal authority expansion = ABSENT
memory mutation by no-proposal record = ABSENT
```

## Boundary

R8 proves durable identity and bounded outcome semantics for observations handled
by this deterministic single-process Curator chronicle. It does **not** prove:

- authenticity or truth of the incoming metrics;
- semantic correctness of the planning threshold;
- that an external sensor emitted the observation only once;
- cross-process or distributed uniqueness of `observation_id`;
- semantic understanding by a model;
- restructuring execution authority.

The correction therefore closes the collision/identity defect without enlarging
Curator authority.
