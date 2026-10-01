# PSI-MEMORY-R7-CONSUMED-VERSION-01

**Status:** `PASS_WITH_BOUNDARY`  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Implementation:** `77d67e3fa3c433f99a9db01ded271ef96d3d2fa8`  
**Acceptance regression:** `1b1d3ed636f7839af6088b6e54374adc962df458`

## Problem

F3.2 linked an archive `version_id` to a committed ACCESS_STEWARD movement and
verified that the version named the movement destination map. That established
an association with map `M`, but not that the consumer had read the named
historical version `V`.

With two versions of the same map,

```text
M@v1 -> H1
M@v2 -> H2
```

a movement into `M` could be attached to either version. The old bridge therefore
allowed the stronger claim

```text
consumer used version V
```

without evidence at the read boundary.

## FAIL-before

Workflow `36776680607`, job `110096241121`, executed the separating case before
the correction. The test reconstructed `version:M2:1` but then successfully
linked the same movement to `version:M2:2`, which names the same map.

Observed failure:

```text
AssertionError:
unconsumed archive version was accepted as usage merely because it names the same map
```

This establishes the original R7 defect by execution rather than source
inspection alone.

## Correction

The bridge now distinguishes two evidence classes:

```text
MAP_ASSOCIATION
VERIFIED_CONSUMPTION
```

`link_movement()` without a receipt remains legal, but can claim only
`MAP_ASSOCIATION`.

A stronger claim requires the new typed read path:

```text
consume_version(receipt_id, version_id, movement_request_id)
```

That operation reconstructs and returns the exact archive version and durably
records an `ArchiveConsumptionReceipt` binding:

```text
receipt_id
version_id
movement_request_id
session_id
object_id
movement_digest
content_digest
source_revision
created_at
```

Only a `link_movement()` carrying that matching receipt can obtain
`VERIFIED_CONSUMPTION`. A receipt for `v1` cannot be reassigned to `v2`, even
when both versions have the same `object_id` / map.

The receipt and usage record are both content-digested and revalidated on
restart. Existing old usage history loads as `MAP_ASSOCIATION`; it is not
retroactively upgraded.

## Acceptance witness

Workflow `36777234075`, job `110098092894`, passed all three steps:

1. R7 two-version separating witness;
2. F3.2 archive-usage regression;
3. archive-runtime regression.

The witness verifies:

- association-only and verified-consumption states are distinct;
- the exact read of `version:M2:1` returns and records its digest/revision;
- the matching receipt authorizes the strong `VERIFIED_CONSUMPTION` claim;
- the same receipt is rejected for `version:M2:2`;
- restart preserves receipt and usage binding;
- Guardian telemetry authorization is re-applied after restart;
- unauthorized reads expose no usage body.

Independent existing workflow `36777234008`, job `110098092529`, also passed:
F3.0, F3.1, F3.2, ACCESS_STEWARD, Servant and institutional-constitution
regressions.

Because consumption receipts share the JSONL WAL machinery, R1 workflow
`36777234023`, job `110098092732`, was also checked and passed its journal,
shared WAL, Servant, ACCESS_STEWARD, Immune, archive, archive-usage and Curator
regressions.

## Legal claim after R7

We may now distinguish:

```text
MAP_ASSOCIATION:
movement is associated with historical archive version V of destination map M
```

from:

```text
VERIFIED_CONSUMPTION:
the typed archive read path returned version V at revision r with digest H,
and the durable receipt is bound to the same movement
```

The second claim no longer follows merely from map identity or `CURRENT`.

## Boundary

R7 proves **which archive payload was returned by the typed read path**. It does
not prove that a downstream model read every field, semantically understood the
payload, relied on it in reasoning, or improved its answer because of it.

Those stronger efficacy claims remain for the bounded full PSI run / F5. R7 adds
no distributed exactly-once guarantee and does not alter CORE5, CANON-03 or
mathematical theorem status.
