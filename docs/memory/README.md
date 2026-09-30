# Shared PSI memory / Pamięć współdzielona PSI

## English

Status: EXPERIMENTAL / NON-CANONICAL. Current objective: let a later agent reuse
a result together with the conditions that license its use, at a measured cost
and without losing task-relevant distinctions. A graph is a logical relation
model; no particular database, embedding or drawing follows from it.

The current implementation separates source archives, typed records with
provenance/status/version, bounded task retrieval, and checked updates.
Candidate discoveries and disputed records remain separate from admitted use.
A source-fragment certificate establishes a source binding, not a general proof
of the statement. Agent identity grants no additional authority.

The immediate evaluation is [M4b A/B/C](../../experiments/PSI-MEMORY-M4-EVALUATION.md):
broad source context, the existing guided pack, and a plain lexical comparator.
The same commit and task are frozen. This known task is a calibration case,
not held-out evidence. Model efficacy remains NOT_RUN; byte counts, regression
success and input preparation cannot upgrade that status.

Preparation measured on 2026-09-30, including source locators and fragment hashes:
A = 205062 bytes; B = 40553 bytes; C = 40532 bytes. These are UTF-8 context
sizes, not token counts or quality scores. Five preparation regressions pass.
The finite representation check preserves the typed answer in both layouts and
detects three/one lost distinction pairs in the two nearness-only controls.

The separate [representation check](representation-check.md) keeps the data
fixed while changing representations. Chemistry-photo fixtures are auxiliary
ambiguity witnesses, not evidence of memory quality or of the benefit of an
image representation. New architecture is not the default next step: complete
the comparison first, unless an explicit task or failure witness selects a repair.

Core and CANON-03 remain frozen. This page governs the experimental memory
branch only; it does not replace the general project work map.

## Polski

Status: EKSPERYMENT / POZA KANONEM. Bieżący cel: kolejny agent ma odzyskać wynik
wraz z warunkami jego zastosowania, przy zmierzonym koszcie i zachowaniu
rozróżnień potrzebnych zadaniu. Graf opisuje relacje; nie wynika z niego wybór
konkretnej bazy danych, zanurzenia ani rysunku.

Wykonanie rozdziela archiwum źródeł, typowane zapisy z pochodzeniem, statusem
i wersją, ograniczony odczyt zadaniowy oraz sprawdzaną aktualizację.
Propozycje i zapisy sporne pozostają oddzielone od dopuszczonych zastosowań.
Certyfikat fragmentu poświadcza związanie ze źródłem, nie ogólną prawdziwość
zdania. Tożsamość agenta nie nadaje dodatkowego autorytetu.

Bieżącą jednostką oceny jest [M4b A/B/C](../../experiments/PSI-MEMORY-M4-EVALUATION.md):
szeroki kontekst źródłowy, dotychczasowy pakiet kierowany pamięcią i proste
wyszukiwanie leksykalne. Commit i zadanie są zamrożone. Znane zadanie jest
próbą kalibracyjną, nie niezależnym zbiorem sprawdzającym. Skuteczność modeli
ma nadal status NOT_RUN; liczba bajtów, przejście regresji i przygotowanie wejść
nie zmieniają tego statusu.

Pomiar przygotowania z 2026-09-30, wraz z lokalizatorami i skrótami fragmentów:
A = 205062 bajty; B = 40553 bajty; C = 40532 bajty. To rozmiary kontekstu UTF-8,
nie liczby tokenów ani oceny jakości. Pięć regresji przygotowania przeszło.
Skończony test reprezentacji zachował odpowiedź typowaną w obu układach oraz
wykrył trzy/jedną parę utraconych rozróżnień w kontrolach opartych tylko na bliskości.

Oddzielny [test reprezentacji](representation-check.md) zachowuje dane i zmienia
ich przedstawienie. Przykłady fotografii chemicznych są pomocniczymi świadkami
niejednoznaczności; nie świadczą o jakości pamięci ani korzyści z obrazu.
Domyślnym następnym krokiem jest wykonanie porównania. Rozbudowa architektury
wymaga wybranego zadania albo świadka błędu uzasadniającego naprawę.

CORE5 i CANON-03 pozostają zamrożone. Ta strona określa kierunek eksperymentalnej
pamięci, nie zastępuje ogólnej mapy pracy projektu.
