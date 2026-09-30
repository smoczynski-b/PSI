# Shared PSI memory / Pamięć współdzielona PSI

> Current work selection: [CURRENT-WORK-FRONT-01](CURRENT-WORK-FRONT-01.md).
> Latest evidence and acceptance cases: [memory and agent review](AUDIT-ROZMOWY-04.md#memory-and-agent-review-2026-09-30).
> Older phase plans retain their historical scope; they do not select the next unit.

## English

Status: EXPERIMENTAL / NON-CANONICAL. Current objective: let a later agent reuse
a result together with the conditions that license its use, at a measured cost
and without losing task-relevant distinctions. A graph is a logical relation
model; no particular database, embedding or drawing follows from it.

### Current implementation and GPT-5 handoff — 2026-09-30

Reviewed code: `53bdc36c44c0b2d6d2621339ec65dc0f00de9b80`.
The latest review covers the 88-commit / 67-file delta with targeted inspection
of contracts, runtime boundaries, tests and CI evidence. The earlier three F0
defects are repaired. New source-derived findings have executable acceptance
cases planned; this review did not run Python locally.

| Layer | Implemented state | Evidence boundary |
|---|---|---|
| Typed/active memory, MVCC, WAL | Typed records, task views, bounded retrieval, selective invalidation and replay | Explicit read sets/dependencies; reference implementation |
| SERVANT / IMMUNE | Original verdict recovery, numeric-domain validation and live recovered-view binding repaired | Further journal and cross-layer interruption cases remain open |
| F1 reuse | Derived answer survives clean restart; changed premise blocks reuse with NEEDS_RECHECK | Deterministic A/B fixtures, no live model-quality result |
| ACCESS_STEWARD | Guardian policy execution, session movement, capability and telemetry separation | Subordinate apparatus within four roles; R1/R2/R6 open |
| Archive and Curator | Snapshot/delta versions, CURRENT, usage references, proposal-only planning | R1/R7/R8 open; no autonomous restructuring |
| PSI-VIZ | Contract-bound frames, SVG and an actual Manim MP4 | R3–R5 open: consumed hashes, node-status redaction, visible direction |
| Evaluation | Existing M4b preparation; F5 remains planned | Model-quality benefit and total cost reduction remain unmeasured |

**Next for GPT-5: R1 — safe journal continuation after interrupted writes.**
Then follow the bounded repair queue in the current front. F4.4 SPLIT is deferred
until its durability and projection prerequisites pass. Each unit starts with a
separating regression and ends after its acceptance case and affected gates.
The [audit](AUDIT-ROZMOWY-04.md#memory-and-agent-review-2026-09-30) distinguishes
source-derived defects, existing CI results and unmeasured claims.

Logical work counters now include index refresh and event history. They do not
establish full end-to-end latency, normalized transition cost or model savings.
M4b below remains a separate text-context comparison; no model run was added.
The zero-cost model-execution constraint remains. GPU and live FORUM require
separately selected work. Names of models or institutional roles grant no
additional epistemic authority.

Chemistry motivates an additional design aim clarified by the user on
2026-09-30: preserve physically constrained process knowledge through formulas,
quantities, reaction conditions and typed connections, with little dependence
on natural-language narration. Formal notation is a representation; the modeled
constraints have to be grounded in physics and observation. A finite elemental
vocabulary does not make the space of compounds, reactions or continuous states
finite. A bounded model must declare its species, reactions and conditions.

This supports studying process-derived geometry: states, reaction directions,
conservation constraints and trajectories. The [geometric scope clarification](representation-check.md)
separates this from arbitrary drawing coordinates. Formal records can be the
proposed working and exchange format, while prose serves human communication.
Whether a particular agent handles them better is still an experimental question.

The current implementation separates source archives, typed records with
provenance/status/version, bounded task retrieval, and checked updates.
Candidate discoveries and disputed records remain separate from admitted use.
A source-fragment certificate establishes a source binding, not a general proof
of the statement. Agent identity grants no additional authority.

The prepared model-quality evaluation is [M4b A/B/C](../../experiments/PSI-MEMORY-M4-EVALUATION.md):
broad source context, the existing guided pack, and a plain lexical comparator.
The same commit and task are frozen. This known task is a calibration case,
not held-out evidence. Model efficacy remains NOT_RUN; byte counts, regression
success and input preparation cannot upgrade that status.
M4b measures text-context selection only; it does not test formal communication
against natural language or process geometry against a textual representation.

Preparation measured on 2026-09-30, including source locators and fragment hashes:
A = 205062 bytes; B = 40553 bytes; C = 40532 bytes. These are UTF-8 context
sizes, not token counts or quality scores. Five preparation regressions pass.
The finite representation check preserves the typed answer in both layouts and
detects three/one lost distinction pairs in the two nearness-only controls.

The separate [representation check](representation-check.md) keeps the data
fixed while changing representations. Chemistry-photo fixtures are auxiliary
ambiguity witnesses, not evidence of memory quality or of the benefit of an
image representation. Follow the bounded repair order above; the existing
visual experiment and representation boundary are recorded in that document.

Core and CANON-03 remain frozen. This page governs the experimental memory
branch only; it does not replace the general project work map.

## Polski

Status: EKSPERYMENT / POZA KANONEM. Bieżący cel: kolejny agent ma odzyskać wynik
wraz z warunkami jego zastosowania, przy zmierzonym koszcie i zachowaniu
rozróżnień potrzebnych zadaniu. Graf opisuje relacje; nie wynika z niego wybór
konkretnej bazy danych, zanurzenia ani rysunku.

### Bieżące wykonanie i przekazanie GPT-5 — 2026-09-30

Zbadany kod: `53bdc36c44c0b2d6d2621339ec65dc0f00de9b80`.
Przyrost obejmuje 88 commitów i 67 plików. Inspekcja skupiła się na kontraktach,
granicach wykonania, testach i zapisach CI. Trzy wcześniejsze usterki F0 zostały
naprawione. Nowe ustalenia wynikają z analizy kodu; ich kontrprzykładów nie
uruchomiono lokalnie podczas tej inspekcji.

Działają już referencyjne wykonania: ponowne użycie wyniku po czystym restarcie
i zatrzymanie po zmianie przesłanki, Nadzorca ruchu, archiwum wersji, planista
Kustosza oraz SVG i rzeczywisty film Manima. Nadzorca jest aparatem Strażnika
w obrębie czterech ról. Kustosz wnosi propozycje, nie wykonuje sam przebudów.

**Następna jednostka dla GPT-5: R1 — bezpieczny zapis po przerwaniu dziennika.**
Dalszą kolejność i warunki zakończenia podaje
[bieżący front](CURRENT-WORK-FRONT-01.md), a świadki i granice dowodów —
[najnowszy audyt](AUDIT-ROZMOWY-04.md#memory-and-agent-review-2026-09-30).
F4.4 SPLIT czeka na wskazane naprawy trwałości i projekcji. Nie należy ponownie
wybierać zakończonych napraw F0 z dawnych instrukcji.

Pozostałe luki dotyczą zgodności zatwierdzonego stanu z decyzją po przerwaniu,
sprawdzania skrótów danych wizualnych, ukrywania statusu węzłów, kierunku relacji,
znaczenia kosztów oraz przypisania użycia do konkretnej wersji. Rejestrowanie
obserwacji Kustosza bez propozycji wymaga doprecyzowania tożsamości.
Dotychczasowe PASS zachowują zakres swoich testów.

Przebieg F1 używa deterministycznych zastępników agentów A/B. Liczniki pracy
obejmują teraz indeksy i historię, lecz nie mierzą pełnego kosztu wykonania.
Korzyść dla jakości odpowiedzi modeli pozostaje niezmierzona; M4b i przyszłe F5
nie są zakończonymi badaniami. Ta inspekcja nie uruchamiała modeli ani płatnych
prób. GPU i żywe FORUM wymagają osobno wybranego zadania.

Chemia uzasadnia dodatkowy cel doprecyzowany przez użytkownika 2026-09-30:
zachowanie wiedzy o procesach ograniczonych fizyką przez wzory, wielkości,
warunki reakcji i typowane połączenia, przy małej zależności od opisu w języku
naturalnym. Notacja jest reprezentacją; opisywane ograniczenia muszą mieć
podstawę fizyczną i obserwacyjną. Skończony zbiór pierwiastków nie oznacza
skończoności zbioru związków, reakcji ani ciągłych stanów. Ograniczony model
musi określić katalog substancji, reakcji i warunki.

To uzasadnia badanie geometrii wynikającej z procesu: stanów, kierunków reakcji,
ograniczeń zachowania i trajektorii. [Uściślenie zakresu geometrycznego](representation-check.md)
oddziela ją od dowolnego układu współrzędnych rysunku. Formalny zapis może być
projektowanym formatem pracy i wymiany między agentami, a proza służyć
komunikacji z człowiekiem. Sprawność konkretnego agenta wymaga pomiaru.

Wykonanie rozdziela archiwum źródeł, typowane zapisy z pochodzeniem, statusem
i wersją, ograniczony odczyt zadaniowy oraz sprawdzaną aktualizację.
Propozycje i zapisy sporne pozostają oddzielone od dopuszczonych zastosowań.
Certyfikat fragmentu poświadcza związanie ze źródłem, nie ogólną prawdziwość
zdania. Tożsamość agenta nie nadaje dodatkowego autorytetu.

Przygotowaną jednostką oceny modeli jest [M4b A/B/C](../../experiments/PSI-MEMORY-M4-EVALUATION.md):
szeroki kontekst źródłowy, dotychczasowy pakiet kierowany pamięcią i proste
wyszukiwanie leksykalne. Commit i zadanie są zamrożone. Znane zadanie jest
próbą kalibracyjną, nie niezależnym zbiorem sprawdzającym. Skuteczność modeli
ma nadal status NOT_RUN; liczba bajtów, przejście regresji i przygotowanie wejść
nie zmieniają tego statusu.
M4b mierzy wyłącznie dobór kontekstu tekstowego; nie porównuje wymiany formalnej
z językiem naturalnym ani geometrii procesu z przedstawieniem tekstowym.

Pomiar przygotowania z 2026-09-30, wraz z lokalizatorami i skrótami fragmentów:
A = 205062 bajty; B = 40553 bajty; C = 40532 bajty. To rozmiary kontekstu UTF-8,
nie liczby tokenów ani oceny jakości. Pięć regresji przygotowania przeszło.
Skończony test reprezentacji zachował odpowiedź typowaną w obu układach oraz
wykrył trzy/jedną parę utraconych rozróżnień w kontrolach opartych tylko na bliskości.

Oddzielny [test reprezentacji](representation-check.md) zachowuje dane i zmienia
ich przedstawienie. Przykłady fotografii chemicznych są pomocniczymi świadkami
niejednoznaczności; nie świadczą o jakości pamięci ani korzyści z obrazu.
Obowiązuje kolejność napraw wskazana wyżej. Istniejącą próbę wizualną i granice
reprezentacji odnotowano we wskazanym dokumencie.

CORE5 i CANON-03 pozostają zamrożone. Ta strona określa kierunek eksperymentalnej
pamięci, nie zastępuje ogólnej mapy pracy projektu.
