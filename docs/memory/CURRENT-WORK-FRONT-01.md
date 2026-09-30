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
F3.3 PASS_WITH_BOUNDARY
F3   FUNCTIONALLY_CLOSED_REFERENCE_LEVEL
F4   NEXT
```

## F3.3 — wynik

Minimalny Kustosz-planista działa jako deterministyczny automat propozycji nad jawnymi metrykami administracyjnymi i zewnętrzną, wersjonowaną polityką `authority=PSI_AGENT`.

```text
administrative metrics
+ licensed planning rule
+ explicit threshold
→ STRUCTURE_PROPOSAL(PROPOSED)
→ SERVANT procedural gate
→ append-only Curator planning chronicle
```

Dopuszczone typy propozycji:

```text
EXPAND | SPLIT | MERGE | REINDEX | MIGRATE | ARCHIVE | COMPACT | REBALANCE
```

Świadek: `district:alpha` ma `capacity_utilization=0.95`; przy regule `GTE 0.90` Kustosz emituje audytowalne `EXPAND` z kosztem, ryzykiem, zależnościami, rollbackiem i testem odbioru.

Zamrożone:

\[
\boxed{PROPOSAL\neq AUTHORIZATION\neq EXECUTION}
\]

\[
\boxed{planning\ metric\neq epistemic\ status}
\]

\[
\boxed{CURATOR\ does\ not\ self-author\ thresholds}
\]

Sama propozycja nie zmienia autorytatywnej pamięci (`durable.revision=0`, digest workspace bez zmian), nie zwiększa budżetu, nie zmienia polityki Strażnika ani statusu epistemicznego. Replay jest idempotentny; kolizje obserwacji/propozycji działają fail-closed; restart odtwarza status `PROPOSED`; brak autoryzowanego runbooku blokuje trwały wpis.

Workflow `PSI memory curator planner`, run `36756411723`, zakończył się `success`; w jednym jobie ponownie przeszły F3.0, F3.1, F3.2, F3.3, runtime Nadzorcy, regresja Sługi i konstytucja instytucji.

Szczegóły: `docs/memory/PSI-MEMORY-CURATOR-F3.3-01.md`.

## F3 — domknięcie referencyjne

Na poziomie referencyjnym działają łącznie:

```text
F3.0 archive contract
F3.1 snapshot + delta + manifest + CURRENT_POINTER + restart
F3.2 version ↔ movement ↔ cost with restricted telemetry
F3.3 Curator proposal-only planner
```

To nie jest wdrożenie produkcyjne ani system rozproszony. Nie oznacza też, że przebudowy Kustosza są automatycznie wykonywane.

## F4 — następna jednostka

**PSI-VIZ — sprawdzalny widok konkretnej rewizji pamięci.**

Pierwszy eksperyment F4 powinien wykorzystać już istniejący język z `Konstruowanie litery a` i aktualny stan pamięci, bez tworzenia nowej ontologii.

Minimalny świadek:

1. jedna zamrożona wersja/mapa pamięci i jeden kontrakt zadaniowy;
2. dwa lub więcej layoutów tej samej relacyjnej struktury;
3. identyczne typed relations/provenance/status/version we wszystkich widokach;
4. ruch punktu bez zmiany relacji nie może zmieniać stanu semantycznego;
5. zmiana relacji ma być widoczna jako jawne zdarzenie, nie jako arbitralne przesunięcie grafiki;
6. kolor/symbol/ruch mają jawny kontrakt wizualny;
7. jedna klatka kluczowa ma nadawać się do druku, a sekwencja do animacji;
8. pierwsza demonstracja: faktoryzacja / włókno i rozróżnienie `|F(Y)|>1` przy `|q_T(F(Y))|=1` albo równoważny świadek już obecny w PSI-VIZ;
9. widok nie może ujawniać telemetrii lub metadanych, do których odbiorca nie ma prawa;
10. `visual projection != authoritative memory` pozostaje rygielkiem nadrzędnym.

Dopiero po F4.0/F4.1 należy przejść do porównania efektywności reprezentacji i później do tensor/GPU.
