# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Supersedes only:** historical `NEXT` prose in `WORK-FRONT-GPT5-01.md`.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Stan

```text
F0   PASS_WITH_BOUNDARY
F1   PASS_WITH_BOUNDARY
F2.0 CONTRACT_PASS
F2.1 PASS_WITH_BOUNDARY
F3.0 CONTRACT_PASS
F3.1 PASS_WITH_BOUNDARY
F3.2 PASS_WITH_BOUNDARY
F3.3 NEXT
```

## F3.2 — wynik

Warstwa L2 łączy wersję mapy z legalnym ruchem i jego rzeczywistym kosztem bez kopiowania pełnego rekordu Nadzorcy:

```text
archive version
+ ACCESS_MOVEMENT request_id
+ session / route
+ actual CostVector
+ telemetry_class
+ movement_digest
→ restricted L2 usage reference
```

Zamrożone rozróżnienia:

\[
\boxed{archive\ storage\neq permission\ to\ read}
\]

\[
\boxed{usage\ reference\neq copy(ACCESS\ telemetry)}
\]

\[
\boxed{cost\ of\ access\neq epistemic\ strength}
\]

Szczegółowy odczyt L2 ponownie przechodzi przez `ACCESS_STEWARD.view_telemetry(...)` i aktualną politykę Strażnika. Brak `VIEW_TELEMETRY` nie usuwa audytowego odwołania, ale blokuje materializację treści ograniczonej. `T3_AGGREGATED` zwraca wyłącznie agregat wersji (`usage_count`, `total_cost_l1`) bez sesji i identyfikatora ruchu.

Ruch do `M2` nie może zostać podpięty pod wersję obiektu `M1`. Restart odtwarza jednocześnie obecność sesji, wersję archiwalną i L2 usage ref oraz ponownie weryfikuje digest źródłowego `ACCESS_MOVEMENT`.

Workflow `PSI memory archive usage`, run `36752648832`, zakończył się `success`; w jednym jobie przeszły F3.0, F3.1, F3.2, runtime Nadzorcy, regresja Sługi i konstytucja instytucji.

Szczegóły: `docs/memory/PSI-MEMORY-ARCHIVE-F3.2-01.md`.

## F3.3 — następna jednostka

**MINIMAL CURATOR PLANNER RUNTIME — propozycja bez prawa wykonawczego.**

Zrealizować najmniejszy automat Kustosza, który na jawnych metrykach administracyjnych potrafi zgłosić audytowalną propozycję:

```text
EXPAND | SPLIT | MERGE | REINDEX | MIGRATE | ARCHIVE | COMPACT | REBALANCE
```

ale nie może sam wykonać przebudowy, zwiększyć własnego budżetu, zmienić polityki dostępu ani statusu epistemicznego.

Minimalny świadek F3.3:

1. sztuczna dzielnica przekracza jawny próg pojemności/obciążenia;
2. Kustosz tworzy `EXPAND` lub `SPLIT` proposal z metrykami, kosztem, ryzykiem i wymaganym testem;
3. pamięć nie zmienia się od samej propozycji;
4. replay jest idempotentny, a kolizja `proposal_id` fail-closed;
5. restart odtwarza propozycję i jej status;
6. propozycja nie jest autoryzacją wykonania;
7. nie ma semantycznej władzy ani samonadawania zasobów.

Po PASS F3.3 można uznać F3 za funkcjonalnie domknięty na poziomie referencyjnym i przejść do F4/PSI-VIZ.
