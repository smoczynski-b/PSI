# PSI-MEMORY-F5-MODEL-EFFICACY-01

**Status:** `PREPARED / INPUTS_READY / MODEL_RUN_BLOCKED`  
**Date:** 2026-10-01  
**Branch:** `psi-memory-map-01`  
**Frozen source revision:** `f3cee544d7642be1b74d53e233b7149a0e2c7dcd`  
**Preparation workflow:** `36784242295`  
**Preparation job:** `110121688788`  
**Does not modify:** CORE5, CANON-03, theorem status, R5/F4.4.

## 1. Pytanie F5

F5 ma sprawdzić skuteczność epistemiczną, nie poprawność infrastruktury:

```text
czy pamięć PSI poprawia odpowiedź modelu względem
A zwykłego zamrożonego kontekstu
B prostego wyszukiwania BM25
C istniejącego pakietu pamięci PSI
```

przy stałym źródle, modelu, limicie odpowiedzi i ślepej rubryce. Tańsza, ale błędna odpowiedź nie jest sukcesem.

## 2. Korekta preflight przed pierwszym płatnym wynikiem

Pierwotnie rozważano zadania R6/R7/R8/full-run. Preflight wykazał jednak, że te obiekty nie są węzłami obsługiwanymi przez istniejący automatyczny tor `build_memory_pack.py` / bieżący graf routingu. Ręczne dopisanie im źródeł uczyniłoby ramię C ręcznie skonstruowanym adapterem, a nie testem istniejącej pamięci PSI.

Korekta została wykonana **przed uzyskaniem jakiejkolwiek odpowiedzi modelowej**, więc nie jest dostrojeniem do wyniku.

Właściwy `F5-HOLDOUT-V1` używa trzech istniejących, automatycznie routowalnych jednostek późniejszych niż kalibracja G4/M4:

```text
H10 = II.10 silna lumpowalność / granica task quotient -> Markov autonomy
H11 = II.11 Myhill-Nerode / kontrakt przyszłych testów i granice minimalności
H12 = II.12 Paige-Tarjan / PT1-PT4 i granica algorytmicznej uniwersalizacji
```

M4b/G4 pozostaje kalibracją i nie jest dowodem generalizacji.

## 3. Zamrożony kontrakt

Maszynowy kontrakt:

`experiments/f5-evaluation-contract.json`

wiąże:

- `source_ref = f3cee544d7642be1b74d53e233b7149a0e2c7dcd`;
- dokładne blob SHA trzech dokumentów II.10-II.12;
- blob SHA zamrożonego `scripts/build_memory_pack.py`;
- trzy zadania i ich rubryki;
- `prompt_char_limit = 80000`;
- `answer_word_limit = 600`;
- BM25 `k1=1.2`, `b=0.75`, fragmenty 60 linii;
- promień pakietu PSI = 3;
- pilot = `H10`;
- maksymalnie 3 płatne przebiegi w pilocie.

Generator:

`scripts/prepare_f5_evaluation.py`

nie wykonuje modelu. Buduje A/B/C, manifest, skróty promptów, ślepą rubrykę i osobną mapę unblind.

## 4. Ramiona

### A — `ORDINARY_FULL_FROZEN_CORPUS`

Pełny zamrożony korpus II.10-II.12. Brak grafu i rankingu.

### B — `BM25_TASK_TEXT_ONLY_MATCHED_TO_PSI_CONTEXT_BYTES`

Ten sam korpus, ranking wyłącznie tekstem zadania. Budżet źródłowy jest dopasowany do rozmiaru ramienia C dla danego zadania.

### C — `EXISTING_BUILD_MEMORY_PACK_AT_FROZEN_SOURCE_REF`

Semantyka istniejącego `build_memory_pack.py` odtwarzana dokładnie na zamrożonym `source_ref`; brak ręcznego dopisywania dokumentów po wyniku.

## 5. Wynik przygotowania

Workflow `36784242295`, job `110121688788`: **success**.

Sprawdzono:

- wszystkie 9 promptów istnieją;
- żaden nie przekracza 80 000 znaków;
- B nie przekracza budżetu kontekstu C;
- C ma dokładnie zadeklarowany budżet źródłowy;
- wszystkie źródła są przypięte do zamrożonej rewizji;
- `model_status = NOT_RUN` podczas przygotowania;
- ślepa rubryka i mapa unblind są oddzielone.

Artefakt `f5-prepared-inputs`, ID `11128514047`, ma SHA-256:

`1a8a10cbb4aa32ac90a563d29911ac5aad61b142e551d2565146ffac9bfc289c`.

### Rozmiary promptów

```text
H10 A 27710 chars   B 10172   C 10544
H11 A 27669 chars   B  9505   C  9861
H12 A 27656 chars   B  8541   C  8940
```

Dla pilota H10:

```text
B context = 9616 bytes
C context = 9999 bytes
```

czyli porównanie B/C nie korzysta z przewagi dużego budżetu C.

## 6. Czysty runner

Do F5 utworzono odrębnego agenta wykonawczego `PSI F5 Clean Runner`:

- runtime `kafka_cloud`;
- model `claude-sonnet-4-6`;
- brak MCP;
- brak skills;
- brak pamięci projektu;
- instrukcja: korzystać wyłącznie ze źródeł w bieżącym promptcie.

Nie użyto agenta PSI-FORUM, ponieważ jego instrukcje i MCP skażałyby izolację.

Pierwsza próba na profilu `kafka` zakończyła się technicznym `422` przed wykonaniem modelu; nie jest wynikiem F5.

## 7. Pilot i blokada kredytowa

Po przygotowaniu uruchomiono tylko pierwszy planowany przebieg pilota:

```text
H10-C
blind id = ANS-25E4942F7A3F
model = claude-sonnet-4-6
```

Runner zakończył zadanie przed inferencją komunikatem:

```text
CREDITS_EXHAUSTED
used = 0
allocated = 0
HTTP 402
```

Zatem:

```text
MODEL ANSWERS OBTAINED = 0
BRAINBASE CREDITS USED BY F5 PILOT = 0
F5 EFFICACY RESULT = NOT_RUN
```

Nie uruchomiono H10-A ani H10-B i nie rozpoczęto H11/H12. Zachowano całą możliwą pulę na później.

## 8. Pomiar po odblokowaniu

Dla każdego zadania/ramienia należy zapisać osobno:

```text
correct_core_claims
correct_boundary_statements
unsupported_claims
wrongly_accepted_claims
source_locator_accuracy
input_tokens      = UNKNOWN jeśli runner nie zwraca
output_tokens     = UNKNOWN jeśli runner nie zwraca
wall_latency      = UNKNOWN jeśli runner nie zwraca
external_tool_calls
source_rereads
```

Ocena pozostaje ślepa wobec A/B/C do zapisania wyników rubryki.

## 9. Następny legalny krok

Po pojawieniu się kredytów nie wolno przebudowywać benchmarku na podstawie przyszłych wyników.

Wznowienie:

```text
1. H10-C — ten sam zamrożony prompt / blind id;
2. jeśli wykonanie techniczne poprawne: H10-A i H10-B;
3. ślepa ocena pilota 3-arm;
4. dopiero po pilocie decyzja, czy wydać kredyty na H11/H12.
```

To zachowuje zapas kredytów i daje koszt jednostkowy przed pełnym przebiegiem.

## 10. Werdykt bieżący

```text
F5 PREPARATION = PASS
F5 MODEL EFFICACY = NOT_RUN
F5 EXECUTION = BLOCKED_BY_ZERO_ALLOCATED_CREDITS
R5 = OPEN / DEFERRED
```

Nie wolno interpretować przygotowania benchmarku jako dowodu przewagi pamięci PSI.
