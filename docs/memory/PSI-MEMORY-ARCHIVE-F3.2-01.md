# PSI-MEMORY-ARCHIVE-F3.2-01 — L2 usage / movement integration

**Status:** EXPERIMENTAL / NON-CANONICAL / RUNTIME TEST  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Extends:** F2.1 `ACCESS_STEWARD`, F3.0 archive contract, F3.1 archive runtime.  
**Does not modify:** CORE5, CANON-03, epistemic status, Guardian policy, live FORUM.

## 1. Cel

F3.2 łączy wersjonowaną mapę L1 z historią użycia L2 bez kopiowania ograniczonej telemetrii Nadzorcy Ruchu.

Dla legalnego ruchu `request_id = r` do mapy `M` i wersji archiwalnej `v` obiektu `M` zapisujemy minimalne wiązanie:

```text
usage_id
version_id
movement_request_id
session_id
map_from
map_to
telemetry_class
movement_digest
actual_cost
policy_version
created_at
```

Pełny rekord ruchu pozostaje w `ACCESS_STEWARD`.

\[
\boxed{L2\ usage = reference + digest + bounded metadata}
\]

nie:

\[
L2\ usage = copy(ACCESS\ telemetry).
\]

## 2. Granica prywatności

`ACCESS_MOVEMENT` zawiera m.in. `actor_id`, deklarowany cel, estymowany koszt, `servant_command_id` i `txid`. F3.2 **nie kopiuje** tych pól do L2.

L2 zachowuje sesję, trasę i koszt rzeczywisty, ponieważ są konieczne dla genealogii użycia i planowania infrastruktury, ale rekord jest klasyfikowany zgodnie z klasą źródłowej telemetrii (obecnie `T2_AUDIT_DURABLE`).

\[
\boxed{archive\ storage\neq permission\ to\ read}
\]

Odczyt szczegółowego rekordu L2 ponownie przechodzi przez `ACCESS_STEWARD.view_telemetry(...)` i aktualną politykę Strażnika.

## 3. T3

Dla `T3_AGGREGATED` F3.2 nie ujawnia `session_id`, `movement_request_id`, trasy pojedynczego ruchu ani danych aktora. Zwraca tylko agregat dla wskazanej wersji:

```text
version_id
usage_count
total_cost_l1
```

## 4. Spójność mapy i ruchu

Wiązanie jest legalne tylko wtedy, gdy:

\[
manifest(version).object\_id = movement.map\_to.
\]

Ruch do `M2` nie może zostać zapisany jako użycie wersji obiektu `M1`.

Źródłowy `ACCESS_MOVEMENT` musi istnieć dokładnie raz i mieć wynik `MOVED`. Jego kanoniczny skrót jest zapisywany w L2. Restart ponownie sprawdza digest, sesję, trasę, klasę telemetrii, politykę i koszt.

## 5. Koszt

F3.2 przechowuje rzeczywisty `CostVector` ruchu, nie estymację. Koszt jest częścią administracyjnej genealogii użycia, nie dowodem jakości ani prawdziwości treści.

\[
\boxed{cost\ of\ access\neq epistemic\ strength}
\]

## 6. Trwałość i Sługa

L2 ma osobny hash-chained journal `ARCHIVE_USAGE`. Każdy nowy wpis musi przejść przez autoryzowany runbook Kustosza w istniejącej bramce proceduralnej Sługi.

Brak `CURATOR-ARCHIVE-01` => brak trwałego wpisu L2.

## 7. Regresje

`scripts/test_memory_archive_usage_runtime.py` sprawdza:

1. legalne wiązanie `version <-> movement <-> actual_cost`;
2. idempotentny replay tego samego `usage_id`;
3. brak kopiowania aktora, celu, estymacji i danych transakcyjnych;
4. brak przecieku przy nieautoryzowanym odczycie T2;
5. legalny szczegółowy odczyt T2 po `VIEW_TELEMETRY`;
6. bezpieczny agregat T3 bez identyfikatora sesji;
7. blokadę ruchu do innej mapy niż `manifest.object_id`;
8. blokadę brakującego `movement_request_id`;
9. restart z odtworzeniem obecności, wersji i L2 usage ref;
10. blokadę zapisu L2 bez runbooku Sługi.

## 8. Boundary

F3.2 jest jednowątkowym referencyjnym mostem L2. Nie implementuje jeszcze:

- rozproszonego magazynu telemetrii;
- silnika retencji/redakcji danych;
- autonomicznego Kustosza-planisty;
- wykonania `SPLIT/MERGE/MIGRATE`;
- live FORUM;
- wizualizacji.

Po PASS F3.2 archiwum posiada już trzy operacyjne osie: **stan wersji, genealogia oraz historia użycia/kosztu**. Następny krok powinien rozstrzygnąć, czy F3 zamykamy testem planistycznym Kustosza, czy przechodzimy do F4 PSI-VIZ. Domyślna kolejność: najpierw F3.3 — minimalny Kustosz-planista bez prawa wykonawczego.
