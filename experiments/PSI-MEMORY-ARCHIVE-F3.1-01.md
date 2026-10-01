# PSI-MEMORY-ARCHIVE-F3.1-01 — referencyjny runtime archiwum

**Status:** EXPERIMENTAL / NON-CANONICAL / REGRESSION-GATED  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Requires:** `PSI-MEMORY-ARCHIVE-F3.0-01` CONTRACT_PASS.

## Cel

Sprawdzić minimalną implementację:

```text
base snapshot
+ ordered delta records
+ version manifest
+ content digest
+ CURRENT_POINTER
→ deterministic reconstruction
→ restart/replay
```

bez utożsamiania archiwizacji z prawdą, admission lub prawem do reuse.

## Implementacja

`scripts/memory_archive_runtime.py` wprowadza:

- `ArchiveManifest`;
- `ArchiveChronicle` oparty o hash-chained `JSONLWAL`;
- `MemoryArchiveRuntime`;
- stabilne identyfikatory snapshotów, delt i wersji;
- deterministyczną rekonstrukcję `snapshot + ordered deltas`;
- obowiązkową kontrolę `content_digest`;
- append-only `CURRENT_POINTER`;
- read-only `restore_candidate`;
- restart przez replay dziennika archiwum.

Każdy nowy trwały wpis archiwum jest poprzedzony autoryzowanym typed `INSTITUTION_ACTION` Sługi pod runbookiem `CURATOR-ARCHIVE-01`. W F3.1 używany jest istniejący proceduralny action `NOTICE`; szczegół semantyczny operacji pozostaje w typed `subject_id` i dzienniku archiwum. To jest świadoma granica implementacyjna, nie nowa władza Sługi.

## Świadek

Jedna baza `snapshot:alpha:0`, jedna delta `delta:alpha:1`, dwie wersje:

```text
version:alpha:1 = snapshot
version:alpha:2 = snapshot + delta
```

`version:alpha:2` ma jawny `epistemic_status_ref=NEEDS_RECHECK`.

Test wymaga:

1. rekonstrukcji v2 do dokładnego `state_digest`;
2. trwałości `CURRENT_POINTER` po zmianie v1 → v2;
3. zachowania `NEEDS_RECHECK` przez restart;
4. braku nowego pełnego snapshotu dla v2;
5. fail-closed dla brakującej delty;
6. fail-closed dla mismatchu digestu;
7. blokady kolizji `version_id`;
8. blokady pointera do nieistniejącej lub obcej wersji;
9. read-only candidate restore bez admission/status mutation;
10. blokady trwałego zapisu bez autoryzowanego runbooku Sługi;
11. wykrycia semantycznie uszkodzonego, choć hash-poprawnego dziennika przy restarcie.

## Zamrożone rozróżnienia

\[
\boxed{CURRENT\neq TRUE\neq REUSABLE}
\]

\[
\boxed{RESTORE\_CANDIDATE\neq ADMIT}
\]

\[
\boxed{version\ manifest\neq reconstructed\ state}
\]

\[
\boxed{one\ snapshot+many\ versions\neq full\ copy\ per\ version}
\]

## Boundary

F3.1 jest referencyjnym, pojedynczoprocesowym archiwum. Nie implementuje jeszcze:

- runtime Strażnika dla ponownego admission po restore;
- materializacji ograniczonej telemetrii T1/T2;
- rozproszonego object store;
- automatycznej polityki snapshot/compaction;
- runtime planistycznego Kustosza;
- optymalizacji kosztu rekonstrukcji;
- live FORUM.

Status końcowy zależy od `scripts/test_memory_archive_runtime.py` i workflow `memory-archive-runtime.yml`.
