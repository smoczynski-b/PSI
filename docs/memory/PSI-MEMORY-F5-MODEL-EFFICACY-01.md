# PSI-MEMORY-F5-MODEL-EFFICACY-01

**Status:** `SELECTED / PREPARED / MODEL_RUN_PENDING`  
**Date:** 2026-09-30  
**Branch:** `psi-memory-map-01`  
**Source revision:** `f3cee544d7642be1b74d53e233b7149a0e2c7dcd`  
**Does not modify:** CORE5, CANON-03, theorem status, R5/F4.4.

## 1. Pytanie F5

F5 ma sprawdzić nie poprawność infrastruktury, lecz skuteczność epistemiczną:

```text
czy pamięć PSI poprawia odpowiedź modelu względem
(1) zwykłego ograniczonego kontekstu i
(2) prostego wyszukiwania leksykalnego,
bez wzrostu liczby nieuprawnionych twierdzeń?
```

Poprzedni pełny przebieg wykazał jedynie, że komponenty R1/R2/R6/R7/R8 mogą działać razem. Nie wykazał, że model rozumie zwrócone dane ani że odpowiada dzięki nim lepiej.

## 2. M4b pozostaje kalibracją

Istniejący `M4b-ABC-CALIBRATION` nie jest F5. Zadanie Go G4 było używane przy budowie pamięci, więc jego wynik może służyć do kalibracji i regresji, ale nie do twierdzenia o generalizacji.

Dodatkowo wariant A M4b ma około 206 kB pełnego wejścia, podczas gdy aktualnie dostępny zewnętrzny runner agenta przyjmuje najwyżej 100 000 znaków promptu. Nie wolno po cichu obciąć A i zachować tej samej etykiety eksperymentu.

## 3. Held-out F5

Zestaw właściwy F5 powstaje po M4 i obejmuje cztery późniejsze problemy, które nie służyły do strojenia pierwotnego testu G4:

```text
H1 COST
R6: PREEXECUTION_QUOTE vs incurred_cost=None; unknown != zero.

H2 ARCHIVE
R7: MAP_ASSOCIATION vs VERIFIED_CONSUMPTION; receipt v1 nie może dowodzić v2.

H3 CURATOR
R8: NO_PROPOSAL musi zachować identity; ten sam observation_id + inny payload ma zostać odrzucony także po restarcie.

H4 STALE PREMISE
FULL RUN: historyczna V1 pozostaje dostępna, ale po zmianie przesłanki wynik zależny ma NEEDS_RECHECK; historical availability != current authority.
```

Każde zadanie wymaga: odpowiedzi rzeczowej, jawnego wskazania granicy wniosku oraz lokalizatorów źródeł. Brak przesłanki ma zostać nazwany jako brak/UNKNOWN, nie uzupełniony z domysłu.

## 4. Trzy ramiona

Wszystkie ramiona używają tego samego zamrożonego korpusu źródłowego, tego samego zadania, modelu, ustawień, limitu odpowiedzi i maksymalnego budżetu serializowanego kontekstu.

### A — ORDINARY_BOUNDED_CONTEXT

Deterministyczny naiwny pakiet źródeł z manifestu, bez grafu PSI i bez rankingu BM25. Fragmenty są dokładane w ustalonej kolejności do wspólnego limitu. To kontrola zwykłego podania kontekstu, nie nieograniczony dump repozytorium.

### B — BM25_BASELINE

Ten sam korpus dzielony na stałe fragmenty; ranking wyłącznie tekstem zadania, bez grafu, gold answer, ręcznych boostów ani informacji o wynikach pozostałych ramion.

### C — PSI_MEMORY

Zadanie jest kompilowane do istniejącego kontraktu pamięci; retrieval używa zadeklarowanych anchorów, relacji, finite budget i istniejących reguł attestation. Wybrane rekordy prowadzą do dokładnych źródeł. Nie wolno ręcznie dopisywać brakującego dokumentu po obejrzeniu wyniku.

Wspólny budżet wejścia F5 powinien zostać ustawiony poniżej technicznego limitu runnera; cel roboczy: `<= 80 000` znaków pełnego promptu na ramię, z twardą kontrolą braku obcięcia.

## 5. Zamrożone źródła held-out

Pierwszy korpus F5 obejmuje co najmniej:

```text
docs/memory/PSI-MEMORY-R6-COST-SEMANTICS-01.md
docs/memory/PSI-MEMORY-R7-CONSUMED-VERSION-01.md
docs/memory/PSI-MEMORY-R8-NO-PROPOSAL-IDENTITY-01.md
docs/memory/PSI-MEMORY-FULL-BOUNDED-RUN-01.md
docs/memory/PSI-MEMORY-ACCESS-STEWARD-01.md
docs/memory/PSI-MEMORY-ARCHIVE-F3.2-01.md
docs/memory/PSI-MEMORY-CURATOR-F3.3-01.md
scripts/access_steward_runtime.py
scripts/memory_archive_usage_runtime.py
scripts/curator_planner_runtime.py
```

Dokładny manifest i skróty treści muszą zostać zapisane przed pierwszym przebiegiem modelu. Po rozpoczęciu ewaluacji nie wolno zmieniać korpusu ani parametrów retrievalu na podstawie wyników.

## 6. Pomiar

Dla każdego zadania i ramienia zapisujemy osobno:

```text
correct_core_claims
correct_boundary_statements
correct_stale_refusal
unsupported_claims
wrongly_accepted_stale_claims
source_locator_accuracy
input_tokens      = UNKNOWN jeśli runner nie zwraca
output_tokens     = UNKNOWN jeśli runner nie zwraca
wall_latency      = UNKNOWN jeśli runner nie zwraca
external_tool_calls
source_rereads
```

Nie agregujemy jakości i kosztu do jednej liczby przez dobór wag po pomiarze.

Warunek minimalny przewagi PSI nad B:

```text
quality_C >= quality_B
unsupported_C <= unsupported_B
stale_errors_C <= stale_errors_B
oraz
co najmniej jedna jawnie mierzona wielkość kosztowa_C < kosztowa_B
```

Jeśli jakość C jest gorsza, niższy koszt nie stanowi sukcesu.

## 7. Ślepa ocena

Odpowiedzi są kodowane losowymi identyfikatorami bez A/B/C. Ewaluator dostaje zamrożoną rubrykę i odpowiedzi, ale nie zna ramienia podczas punktowania. Mapowanie identyfikator -> ramię ujawnia się dopiero po zapisaniu ocen.

Pierwszy przebieg powinien zawierać wszystkie `4 x 3 = 12` odpowiedzi. Powtórzenia stochasticzne są osobną fazą; nie zastępujemy brakującego wykonania trzema odpowiedziami wygenerowanymi w jednym kontekście rozmowy.

## 8. Ograniczenie wykonawcze

Dostępny zewnętrzny runner Brainbase potrafi uruchamiać niezależne zadania modelowe, ale takie wykonania mogą być płatne. Sam wybór F5 nie jest zgodą na nieograniczone zużycie kredytów. Do czasu jawnego uruchomienia modelu status pozostaje:

```text
F5 = PREPARED / MODEL_RUN_PENDING
```

Przygotowanie promptów, manifestów, hashy i automatycznych kontroli jest niepłatne i może być wykonane wcześniej.

## 9. Stop

F5 nie otrzymuje `PASS` na podstawie samego przygotowania wejść. Następny legalny krok:

1. zbudować i zamrozić manifest held-out oraz generator A/B/C;
2. wykazać identyczny budżet i brak silent truncation;
3. wykonać 12 niezależnych przebiegów modelu;
4. przeprowadzić ślepą ocenę;
5. opublikować wynik wielokryterialny wraz z pełną granicą wniosku.

R5 pozostaje otwarte, lecz odroczone do zakończenia lub jawnego zatrzymania F5.
