# PSI-MEMORY-R1-JOURNAL-RECOVERY-01

**Status:** PASS_WITH_BOUNDARY  
**Date:** 2026-09-30  
**Branch:** `psi-memory-map-01`  
**Input HEAD:** `81c9f9292b83f2732ce2672df61703282b39e77a`  
**Implementation:** `9bb7ace0b546e74fbcdc323a2b3a70790b2981c6`  
**Separating tests:** `9250dbd79a3543968aedbdaa5a88866aa1bc5013`  
**CI gate:** `3169cec52ab8aee1686e88ef96431c30d8d5894f`  
**Workflow run:** `36769885146` — `success`

## 1. Object

R1 concerns every institutional journal that delegates persistence to the shared
`JSONLWAL` writer in `scripts/durable_shared_memory.py`.

The required invariant is:

```text
verified prefix P + incomplete final bytes u
    -> restart
    -> P is preserved exactly
    -> u is removed before any later append
```

and, independently:

```text
complete invalid record OR sequence/hash-chain failure
    -> WALCorruption
    -> no automatic truncation
```

R1 does not reconcile cross-journal semantic outcomes; that is R2.

## 2. Correction

`JSONLWAL` now owns one recovery policy for all wrappers:

1. construction verifies the journal and repairs only an incomplete final line;
2. repair uses `ftruncate` at the byte boundary immediately after the verified
   prefix, rather than reopening the entire journal with `wb`;
3. newline-terminated invalid JSON is corruption, not a disposable crash tail;
4. append uses a write-all loop over `os.write`, followed by `fsync`;
5. if write or `fsync` fails, the live writer is blocked from further appends;
   restart must re-verify the durable bytes before writing again.

This removes the former failure mode in which a later append could concatenate
with a torn tail and then turn that malformed tail into interior corruption.

## 3. Separating witnesses

`scripts/test_jsonl_journal_recovery.py` checks:

- valid record -> torn tail -> restart -> two later appends -> restart;
- complete newline-terminated invalid JSON fails closed;
- simulated interruption after prefix truncation preserves all verified records;
- repeated short writes are completed before append returns;
- partial failed write blocks continuation in the same process and is repaired
  only after restart;
- `ServantChronicle` and `AccessChronicle` inherit the shared repair policy;
- `DurableSharedMemoryRuntime` survives a torn tail, then accepts two later
  committed transactions, and reconstructs revision 3 after another restart.

## 4. Regression gate

Workflow `PSI memory journal recovery R1`, run `36769885146`, job
`journal-recovery` (`110073276484`) completed with `success`.

Passed steps:

```text
R1 separating cases
Shared WAL regression
Servant regression
Access steward regression
Immune regression
Archive regression
Archive usage regression
Curator regression
```

The pre-existing ACCESS_STEWARD workflow triggered by the shared-writer change
also completed successfully on implementation commit `9bb7ace`.

## 5. Boundary

The result is limited to the repository's current single-host, single-process
JSONL durability model with local filesystem `O_APPEND` / `ftruncate` / `fsync`
semantics. It does not establish:

- multi-process writer serialization;
- distributed consensus;
- storage-controller or hardware power-loss guarantees beyond the OS/filesystem
  contract;
- cross-journal exactly-once reconciliation after a semantic COMMIT.

The last item is the next repair unit.

## 6. Verdict

```text
R1 JOURNAL CONTINUATION = PASS_WITH_BOUNDARY
NEXT = R2 RESULT RECONCILIATION
```

No change to CORE5, CANON-03, theorem status, four-role constitution or live
FORUM state.
