# PSI-MEMORY-F1-END-TO-END-01 — source-bound durable reuse

Status: **PASS_WITH_BOUNDARY / EXPERIMENTAL / NON-CANONICAL**  
Branch: `psi-memory-map-01`  
Date: 2026-09-30

## Cel

Sprawdzić pierwszy pełny przebieg pamięci PSI, w którym późniejszy agent może użyć wcześniej wyprowadzonego wyniku bez ponownego rekonstruowania źródła, ale zostaje zatrzymany, gdy zadeklarowana przesłanka tego wyniku ulegnie zmianie.

Badany łańcuch:

```text
source + contract
→ bounded retrieval
→ source workspace
→ Agent A result
→ SERVANT
→ MVCC
→ WAL
→ result workspace
→ process-style restart/replay
→ Agent B reuse
→ source premise change
→ selective invalidation
→ restart/replay
→ Agent B NEEDS_RECHECK
```

Nie zmienia to CORE5 ani CANON-03.

## Konstrukcja

Źródło `SOURCE:A` jest czytane dokładnie raz i tworzy ograniczony widok z faktem:

```text
SOURCE:A --STATE--> VALUE:V1
```

Wynik Agenta A jest osobnym workspace'em `resultA`, którego kontrakt deklaruje zależność:

```text
workspace:sourceA
```

Agent A zapisuje przez Sługę:

```text
RESULT:A --ANSWER--> VALUE:ALPHA
```

z provenance wskazującym źródło `artifact:A:v1` i kontrakt `F1-RESULT-A-01`.

Proposal Agenta A deklaruje w MVCC read-set dokładny slot źródłowy:

```text
EDGE|SOURCE:A|STATE|VALUE:V1
```

więc wynik nie może zostać przyjęty z nieaktualnego snapshotu tej przesłanki.

## Reguła reuse Agenta B

Agent B nie dostaje dostępu do pierwotnego `SourceOracle`. Jego decyzja używa wyłącznie odzyskanej pamięci:

1. `resultA.status == VALID`;
2. `contract_id == F1-RESULT-A-01`;
3. zależność `workspace:sourceA` jest obecna;
4. włókno `RESULT:A --ANSWER--> ?` jest jednoelementowe.

Wtedy:

```text
REUSE_ALLOWED
```

Jeżeli status workspace'u jest `NEEDS_RECHECK`, obecność starej odpowiedzi nie daje prawa do użycia.

## Wynik dodatni — czysty restart

Po trwałym zapisie wyniku A tworzony jest nowy `DurableSharedMemoryRuntime` i nowy `ServantRuntime` z tego samego seed + WAL + kroniki.

Sprawdzone:

- semantyczny stan przed i po restarcie jest identyczny;
- `resultA` pozostaje `VALID`;
- provenance i kontrakt przeżywają restart;
- Agent B zwraca `REUSE_ALLOWED`;
- liczba odczytów źródła pozostaje dokładnie `1`;
- liczba rekonstrukcji źródła przez B = `0`;
- replay polecenia Agenta A jest idempotentny i nie tworzy drugiej transakcji.

## Wynik ujemny — zmiana przesłanki

Źródło zmienia się transakcyjnie:

```text
remove SOURCE:A --STATE--> VALUE:V1
add    SOURCE:A --STATE--> VALUE:V2
```

Zmiana aktualizuje bezpośrednio `sourceA`, po czym indeks zależności propaguje:

```text
workspace:sourceA → resultA
```

Skutek:

```text
sourceA = VALID
resultA = NEEDS_RECHECK
```

Stary obiekt:

```text
RESULT:A --ANSWER--> VALUE:ALPHA
```

pozostaje fizycznie zapisany. To celowe: invalidacja nie jest kasowaniem historii.

Agent B dostaje jednak:

```text
NEEDS_RECHECK
```

Po drugim pełnym restarcie/replay wynik nadal istnieje, a status `NEEDS_RECHECK` jest zachowany.

Zatem:

\[
\boxed{
\text{stored result} \neq \text{permission to reuse result}
}
\]

oraz

\[
\boxed{
\text{restart} \not\Rightarrow \text{loss of dependency status}
}
\]

## Koszt tego samego legalnego przebiegu

Sługa został rozszerzony wyłącznie o obserwacyjne liczniki pracy kopiowane z `SharedCommitResult`. Liczniki nie uczestniczą w autoryzacji ani w statusie epistemicznym.

Dla zapisu wyniku A CI zmierzył logicznie:

```text
examined_versions = 2
examined_workspaces = 1
index_refresh_edge_visits = 4
```

Dla zmiany źródła:

```text
examined_versions = 2
examined_workspaces = 2
examined_dependency_links = 1
index_refresh_edge_visits = 6
```

Są to liczniki pracy referencyjnej implementacji, nie pomiary cykli CPU.

## Kryteria przejścia

PASS_WITH_BOUNDARY wymaga jednocześnie:

1. tylko jednego pierwotnego odczytu źródła;
2. trwałego zapisu wyniku A przez Sługę i WAL;
3. semantycznej równoważności po czystym restarcie;
4. legalnego reuse przez B bez source reconstruction;
5. selective invalidation po zmianie przesłanki;
6. zachowania `NEEDS_RECHECK` po kolejnym restarcie;
7. braku uznania samej obecności starego wyniku za prawo do użycia;
8. zachowania regresji Sługi, restart/collision, WAL i cost accounting.

## Wynik CI

Workflow `PSI memory F1 end-to-end reuse`, run `36742791245`, zakończył się `success` dla SHA:

```text
a1606ca9e358b9064bbad48ae98b0c56b2864213
```

W logu:

```text
PSI-MEMORY-F1-END-TO-END-01 PASS_WITH_BOUNDARY
source_reads_total=1
agent_b_source_reconstruction=0
clean_restart_semantic_equivalence=PASS
clean_restart_reuse=REUSE_ALLOWED
source_change_invalidates_result=PASS
changed_restart_preserves_NEEDS_RECHECK=PASS
stored_answer_does_not_override_status=PASS
```

## Granica

Świadek jest deterministyczny i lokalny. Nie obejmuje jeszcze:

- żywego wykonania LLM jako Agent A/B;
- Strażnika jako jawnej bramy admission/release;
- Nadzorcy Ruchu / `ACCESS_STEWARD`;
- Kustosza i rekurencyjnego archiwum;
- sieci i FORUM live;
- learned retrieval;
- GPU/tensor backendu.

F1 dowodzi działania mechanizmu source-bound reuse/restart w referencyjnym runtime, a nie jakości poznawczej modelu.

## Następny legalny front

Po F1 kolejnym krokiem jest F2: kontrakt Nadzorcy Ruchu / `ACCESS_STEWARD` jako sługi Strażnika. Najpierw kontrakt, konflikt-registry i test kompetencji; dopiero potem runtime.
