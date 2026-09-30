# WORK-FRONT-GPT5-01 — front robót pamięci współdzielonej

**Status:** EXPERIMENTAL / NON-CANONICAL / WORK SELECTION  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.  
**Primary rule:** integrity and replay before new roles; source state before visualization; semantics before GPU.

## 0. Cel

Doprowadzić eksperymentalną pamięć PSI do sprawdzonego przebiegu, w którym późniejszy agent odzyskuje wynik razem z warunkami jego legalnego użycia, historią zmian, lokalizacją w mapach oraz kosztem przejść — bez pomylenia reprezentacji z autorytatywnym stanem.

```text
SOURCE / LEDGER
      ↓
AUTHORITATIVE MEMORY
      ↓
TASK WORKSPACES / MAPS
      ↓
CONTROLLED TRANSITIONS + TELEMETRY
      ↓
DERIVED ARCHIVE / MEMORY-OF-MEMORY
      ↓
VISUAL / TENSOR EXECUTION VIEWS
```

Każda warstwa jest projekcją lub wykonaniem warstwy wcześniejszej; żadna nie podnosi samodzielnie statusu epistemicznego treści.

## F0 — integralność istniejącego runtime — PASS_WITH_BOUNDARY

Wykonano:

1. **SERVANT restart/collision — PASS.** Pierwszy ukończony werdykt przeżywa kolizję identyfikatora i restart.
2. **IMMUNE numeric domain — PASS.** NaN, ±∞, bool i tekst nie trafiają do progów; sygnatury mają jawne dziedziny.
3. **IMMUNE recovered-view binding — PASS.** `RECOVER` zachowuje tożsamość publicznych uchwytów `shared` i `shared.views`.
4. **Full cost accounting — PASS_WITH_BOUNDARY.** Globalny routing jest selektywny, lecz pełna lokalna aktualizacja ma nadal składniki `O(|E_workspace|)` i `O(|history|)`.

Zamrożona korekta:

\[
\boxed{
\text{selective routing across workspaces}
\not\Rightarrow
\text{full local update }O(|\Delta|)
}
\]

Szczegóły: `experiments/PSI-ACTIVE-MEMORY-COST-ACCOUNTING-01.md`.

## F1 — source-bound end-to-end reuse/restart — PASS_WITH_BOUNDARY

Wykonano:

```text
source + contract
→ bounded retrieval
→ source workspace
→ Agent A result
→ SERVANT / MVCC / WAL
→ restart/replay
→ Agent B reuse
→ source premise change
→ selective invalidation
→ second restart/replay
→ Agent B NEEDS_RECHECK
```

Wynik `PSI-MEMORY-F1-END-TO-END-01`:

- źródło odczytane dokładnie raz;
- Agent B po czystym restarcie: `REUSE_ALLOWED` i `agent_b_source_reconstruction=0`;
- zmiana przesłanki unieważnia dokładnie zależny wynik;
- stary wynik pozostaje zapisany, lecz otrzymuje `NEEDS_RECHECK`;
- drugi restart zachowuje jednocześnie treść wyniku i jego status zależnościowy;
- telemetria kosztu F0.4 jest dostępna przez decyzję Sługi, ale nie wpływa na legalność.

\[
\boxed{
\text{stored result}\neq\text{permission to reuse result}
}
\]

Szczegóły: `experiments/PSI-MEMORY-F1-END-TO-END-01.md`.

## F2 — Nadzorca Ruchu / `ACCESS_STEWARD`

### F2.0 — kontrakt + rejestr konfliktów — CONTRACT_PASS

`ACCESS_STEWARD` został zamrożony jako **podporządkowany wykonawca Strażnika**, nie jako piąty równorzędny urząd konstytucyjny:

\[
\boxed{GUARDIAN\triangleright ACCESS\_STEWARD}
\]

oraz:

\[
\boxed{policy\_owner=GUARDIAN,\qquad executor=ACCESS\_STEWARD}
\]

Kontrakt: `docs/memory/PSI-MEMORY-ACCESS-STEWARD-01.md`.  
Rejestry maszynowe:

- `docs/memory/psi-memory-access-steward-contract-01.tsv`;
- `docs/memory/psi-memory-access-steward-conflicts-01.tsv`.

Regresja: `scripts/test_access_steward_contract.py`.

Dedykowany workflow `PSI memory access steward contract`, run `36745045308`, zakończył się `success` i ponownie przepuścił czterorólną konstytucję pamięci.

Zamrożone rozdziały:

\[
\boxed{
ENTER\neq ACT\neq EXPORT\neq VIEW\_TELEMETRY
}
\]

\[
\boxed{
MOVE(agent,M_i\to M_j)\neq EXPORT(data,M_i\to M_j)
}
\]

oraz dla różnych map:

\[
\boxed{
M_i\neq M_j\Rightarrow\|\kappa(\tau)\|_1>0
}
\]

Nadzorca wykonuje ruch tylko wobec jawnej wersji polityki, celu, zdolności, zgodnej lokalizacji sesji, legalnego stanu celu i budżetu. Telemetria ma osobne klasy widoczności; prawo do przejścia nie daje prawa do oglądania obecności innych sesji.

### F2.1 — referencyjny runtime Nadzorcy Ruchu — PASS_WITH_BOUNDARY

Wykonano deterministyczny runtime:

```text
Guardian policy snapshot
→ ACCESS_STEWARD
→ purpose/capability/location/target/budget
→ cost meter
→ SERVANT TRANSACT
→ MVCC + durable WAL
→ authoritative session presence
→ append-only movement telemetry
```

Najważniejsze rozstrzygnięcie implementacyjne:

\[
\boxed{
\text{ACCESS_STEWARD nie utrwala obecności bezpośrednio}
}
\]

Autorytatywna obecność sesji jest zapisywana w administracyjnym workspace jako relacja `SESSION_AT::<session_id>` wyłącznie przez:

\[
\boxed{
ACCESS\_STEWARD\to SERVANT\to MVCC\to WAL.
}
\]

`AccessChronicle` jest osobnym append-only audytem ruchu i nie jest źródłem prawdy o bieżącej lokalizacji.

Regresja `scripts/test_access_steward_runtime.py` potwierdziła:

1. legalne `ENTER`, `TRANSIT`, `EXIT` i najwyżej jedną lokalizację sesji;
2. rozdział `ENTER / ACT / EXPORT / VIEW_TELEMETRY`;
3. brak cichej reinterpretacji starej `policy_version`;
4. fail-closed przy braku polityki, nieznanym celu, złej lokalizacji i zamkniętym health gate;
5. dodatni koszt szacowany i rzeczywisty dla ruchu oraz twardy budżet składowy;
6. brak eksportu wynikającego z samego tranzytu;
7. klasy telemetrii oraz agregację `T3` bez identyfikatorów sesji/aktorów;
8. trwałe `COMMIT` ruchu przez Sługę;
9. restart z rekonstrukcją obecności z autorytatywnego stanu;
10. idempotentny replay bez drugiego ruchu;
11. `REQUEST_ID_COLLISION -> STOP_ESCALATE`;
12. `EXIT` bez fantomowej obecności po kolejnym restarcie;
13. brak bezpośredniego `durable.commit` w Nadzorcy;
14. brak semantycznej władzy Nadzorcy.

Dedykowany workflow `PSI memory access steward runtime`, run `36746498419`, zakończył się `success`. W tym samym jobie przeszły ponownie: F2.0 contract, F2.1 runtime, regresja Sługi i czterorólna konstytucja instytucji.

Szczegóły: `experiments/PSI-MEMORY-ACCESS-STEWARD-F2.1-01.md`.

**Boundary F2.1:** pojedynczy proces i deterministyczny snapshot polityki Strażnika; brak runtime'u tworzącego politykę Strażnika, brak rozproszonej współbieżności, live FORUM i autonomicznej diagnostyki patologii. Koszt pozostaje administracyjnym wektorem kontraktowym, nie globalnym optimum.

## F3 — Kustosz + Nadzorca: archiwum „pamięci w pamięci” — NEXT

Minimalny model:

```text
L0 — źródła, obiekty, relacje
L1 — wersjonowane mapy/workspace'y + lineage
L2 — historia tworzenia, używania, przejść i kosztów L1
```

Realizacja ma używać snapshotów, odwołań, hashy i delt, a nie pełnych kopii świata.

`CURATOR` odpowiada za tożsamość, wersję, rodowód i `CURRENT_POINTER`; może wnosić do Agenta PSI propozycje `EXPAND / SPLIT / MERGE / REINDEX / MIGRATE / ARCHIVE / COMPACT / REBALANCE`, lecz nie wykonuje sam przebudowy. `ACCESS_STEWARD` odpowiada za historię obecności, przejść i kosztów.

Pierwsza jednostka F3 ma zamrozić format archiwalnego rekordu L2 i odtworzenie wskazanego stanu przez snapshot + deltę + referencje, bez kopiowania całej pamięci przy każdym kroku.

**Gate F3:** wskazany stan pamięci daje się odtworzyć z właściwym kontraktem, provenance, wersją, uprawnieniami i historią użycia.

## F4 — wizualizacja jako sprawdzalny widok

Rodowód ruchomej notacji PSI-VIZ pochodzi z rozmowy `Konstruowanie litery a`.

Każdy obraz/animacja musi wskazywać rewizję pamięci, kontrakt, identyfikatory obiektów, typ/kierunek relacji i dostęp do wymaganych provenance/status/version.

\[
\boxed{
\text{structural relation}
\neq
\text{embedding geometry}
\neq
\text{display layout}
}
\]

Pierwsze animacje: zawężanie włókna, rozszczepienie po obserwacji, invalidacja, przejście `M_i→M_j` z kosztem/uprawnieniem, genealogy/replay, ten sam stan w dwóch layoutach.

## F5 — zmierzyć korzyść dla modelu

Porównać przy stałym zadaniu/modelu/źródłach:

- szeroki kontekst źródłowy;
- pamięć kierowaną M4b;
- comparator leksykalny;
- formalny/relacyjny pakiet pamięci;
- ten sam stan z wizualnym widokiem operacyjnym.

Niższy koszt wejścia nie jest sam w sobie lepszym rozumowaniem.

## F6 — tensor/GPU jako kompilacja sprawdzonego stanu

\[
\mathcal M_t\xrightarrow{C_c}\Theta_{t,c}
\]

GPU może służyć propagacji, przecięciom, transportowi, wyszukiwaniu motywów i lokalnym aktualizacjom. Nie jest warstwą prawdy.

\[
\boxed{\text{tensor geometry proposes; PSI licenses inference}}
\]

## F7 — FORUM/live multi-agent

Dopiero po stabilizacji lokalnej i archiwum F3:

```text
FORUM durable ledger
↕
shared authoritative memory
↕
active task maps/workspaces
↕
controlled map transitions
```

Agent konsumuje istotne delty, nie odczytuje ponownie całej historii.

## Priorytet wykonawczy

\[
\boxed{
F0\to F1\to F2.0\to F2.1\to F3\to F4\to F5\to F6\to F7
}
\]

Aktualnie:

```text
F0   PASS_WITH_BOUNDARY
F1   PASS_WITH_BOUNDARY
F2.0 CONTRACT_PASS
F2.1 PASS_WITH_BOUNDARY
F3   NEXT
```

## Czego teraz nie robić

- nie tworzyć CORE6 ani R4;
- nie scalać `psi-memory-map-01` z `main`;
- nie przeciążać istniejącego `SERVANT` funkcją ochrony budynku;
- nie robić z `ACCESS_STEWARD` piątej równorzędnej roli konstytucyjnej;
- nie pozwalać Nadzorcy tworzyć polityki dostępu ani własnych uprawnień;
- nie utożsamiać ruchu z eksportem ani wejścia z działaniem;
- nie ukrywać kosztu przejść między mapami;
- nie robić z grafiki lub COO stanu autorytatywnego;
- nie implementować archiwum przez pełne kopiowanie wszystkich map;
- nie przechodzić do GPU przed zachowaniem semantyki i pełnej telemetrii kosztu;
- nie używać telemetrii, popularności ani obecności jako dowodu prawdziwości.

## Najbliższa jednostka

**F3.0 — kontrakt archiwum L0/L1/L2 oraz rekonstrukcji snapshot + delta + referencje.**

Najpierw zamrozić typy rekordów, tożsamość wersji, zależności, regułę rekonstrukcji i konflikt-registry między Kustoszem, Nadzorcą, Sługą i PSI gate. Dopiero po PASS tego kontraktu implementować archiwum.
