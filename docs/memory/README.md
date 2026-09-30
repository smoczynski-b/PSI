# Shared PSI memory / Pamięć współdzielona PSI

## English

Status: EXPERIMENTAL / NON-CANONICAL. Current objective: let a later agent reuse
a result together with the conditions that license its use, at a measured cost
and without losing task-relevant distinctions. A graph is a logical relation
model; no particular database, embedding or drawing follows from it.

### Current implementation and GPT-5 handoff — 2026-09-30

Reviewed baseline: `fce89bde2d8bb6e95292d435bed84e1702c6b26c`.
The complete new active-memory section, its runtime code, registries, experiments
and regression programs were inspected: 46 changed files in 51 commits after
`cf9d91a`. All 12 new regression programs passed locally. The targeted witnesses
in the [audit supplement](AUDIT-ROZMOWY-04.md#active-memory-review-2026-09-30)
expose additional failures; the earlier PASS results retain their tested scope.

| Layer | Implemented/recorded state | Scope |
|---|---|---|
| [Typed memory](PSI-MEMORY-MAP-01.md) | M1–M19, source binding, bounded retrieval | Finite task contracts; model-quality benefit unmeasured |
| [Active memory](PSI-ACTIVE-MEMORY-01.md) | Task workspace, typed deltas, relation-specific COO planes | CPU reference; plane data alone omits provenance/status |
| [Routing](../../experiments/PSI-ACTIVE-MEMORY-MULTIWORKSPACE-01.md) and [invalidation](../../experiments/PSI-ACTIVE-MEMORY-INVALIDATION-01.md) | Reverse indices and declared dependency closure | Affected-view refresh still scans that view's edges |
| [MVCC](../../experiments/PSI-ACTIVE-MEMORY-MVCC-01.md) and [shared state](../../experiments/PSI-ACTIVE-MEMORY-SHARED-01.md) | Versioned proposal checks and selective propagation | Explicit read sets; single process, no distributed concurrency claim |
| [WAL](../../experiments/PSI-ACTIVE-MEMORY-WAL-01.md) | Commit/replay from a caller-supplied baseline | Selected injected crash points; no full-stack recovery guarantee |
| [Institution](PSI-MEMORY-INSTITUTION-01.md) | Four role contracts; separate admission/health/lifecycle/epistemic axes | Guardian and Curator remain role contracts |
| [Servant](../../experiments/PSI-MEMORY-SERVANT-01.md) / [Immune](../../experiments/PSI-MEMORY-IMMUNE-01.md) | Deterministic runtimes and licensed reactions | Open restart, numeric-domain and recovered-view-binding defects |
| [Map genealogy](PSI-MAP-GENEALOGY-01.md) | Sources and typed role correspondences | Registry consistency checked; novelty remains unresolved |

Current direction for GPT-5: stabilize one task-scoped shared-memory execution
path before expanding the architecture. The next bounded unit is preservation
of the original SERVANT verdict across a colliding command and restart. Then
address IMMUNE numeric-domain validation and its binding to recovered views,
as separate reviewable repairs. Exact witnesses and acceptance conditions are
in the audit; naming a model grants no additional epistemic authority.

After those repairs, test one complete source-bound task through retrieval,
workspace compilation, admitted update, dependency invalidation, restart and
rechecked reuse. Keep its visual projection tied to the same contract, data
and revision. A changed layout alone must not change the semantic state.
Measure full end-to-end cost, including view-index refresh and event history,
before claiming delta-local cost for the entire stack.

M4b remains the prepared model-quality comparison below. It is not evidence for
the new transaction stack or for visual/formal communication. The zero-cost
execution constraint remains; no model run was added by this inspection.
GPU, live FORUM integration and new roles require a separately selected task.

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

Zbadany stan: `fce89bde2d8bb6e95292d435bed84e1702c6b26c`.
Przeczytano cały nowy dział aktywnej pamięci: specyfikacje, kod wykonawczy,
rejestry, protokoły i testy — 46 zmienionych plików, 51 commitów po `cf9d91a`.
Wykonano z powodzeniem 12 nowych programów regresyjnych. Dodatkowe świadki
z [uzupełnienia audytu](AUDIT-ROZMOWY-04.md#active-memory-review-2026-09-30)
wykazują luki poza zakresem tych testów.

| Warstwa | Stan wykonania | Granica |
|---|---|---|
| M1–M19 | Typowane relacje, źródła, ograniczony odczyt | Skończone kontrakty; korzyść dla modeli niezmierzona |
| Aktywna pamięć | Widok zadaniowy, delty, osobne macierze rzadkie relacji | Sam zapis COO nie zawiera pochodzenia i statusu |
| Rozsyłanie i unieważnianie | Indeksy odwrotne i domknięcie jawnych zależności | Odświeżenie dotkniętego widoku nadal skanuje jego krawędzie |
| Wspólny stan i MVCC | Kontrola wersji odczytów/zapisów, selektywna propagacja | Jeden proces; zależności odczytu muszą być zadeklarowane |
| Dziennik WAL | Odtwarzanie zatwierdzonych zmian z podanej bazy | Sprawdzone wybrane punkty awarii; pełny cykl ról ma luki |
| Instytucja pamięci | Rozdzielone kompetencje i cztery osie stanu | Strażnik i Kustosz pozostają kontraktami ról |
| Sługa i Immunologia | Działające automaty deterministyczne | Otwarte usterki restartu, dziedziny liczbowej i powiązania widoków |
| Genealogia map | Rejestr źródeł i typowanych odpowiedniości | Kontrola spójności rejestru; oryginalność nierozstrzygnięta |

Kierunek dla GPT-5: ustabilizować jeden zadaniowy przebieg pamięci współdzielonej.
Pierwsza jednostka: zachować pierwotną decyzję Sługi po kolizji identyfikatora
polecenia i restarcie. Następnie, w osobnych naprawach, ustalić legalną dziedzinę
liczbową Immunologii i jej powiązanie z odtworzonymi widokami. Audyt podaje
odtworzone błędy i warunki odbioru. Nazwa modelu nie zmienia rygoru weryfikacji.

Po naprawach sprawdzić jeden pełny przebieg: źródło i kontrakt → odczyt → widok
roboczy → dopuszczona zmiana → unieważnienie zależnych wyników → restart →
ponownie sprawdzone użycie. Wizualizacja ma pokazywać ten sam stan, kontrakt
i rewizję; przemieszczenie punktów nie zmienia zapisanych zależności.
Koszt całego przebiegu obejmuje również odświeżanie indeksów widoku i historię
zdarzeń. Liczba wybranych widoków nie mierzy całej wykonanej pracy.

M4b pozostaje przygotowaną próbą jakości modeli, opisaną niżej. Nie sprawdza
całego wykonania transakcyjnego ani komunikacji obrazowej/formalnej. Obowiązuje
ograniczenie zerowego kosztu uruchomień; ta inspekcja nie uruchamiała modeli.
GPU, żywe FORUM i kolejne role wymagają osobno wybranego zadania.

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
