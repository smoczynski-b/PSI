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

**Boundary F2.0:** kontrakt only. Brak runtime, trwałego rejestru obecności i wykonania ruchu.

### F2.1 — runtime Nadzorcy Ruchu — NEXT

Najbliższa jednostka wykonawcza ma zrealizować deterministyczny, typowany runtime bez natural-language deliberation:

```text
TransitionRequest
→ resolve explicit Guardian policy version
→ check purpose/capability/location/target/budget
→ ALLOW | DENY | STOP_ESCALATE
→ meter transition cost
→ update session presence only on legal movement
→ append typed telemetry
→ durable mutation only through SERVANT/MVCC/WAL
```

Minimalne regresje F2.1:

1. legalne wejście i przejście aktualizuje dokładnie jedną lokalizację sesji;
2. brak polityki/uprawnienia/budżetu/lokalizacji działa fail-closed;
3. `ENTER_MAP` nie umożliwia `ACT_IN_MAP`;
4. ruch nie umożliwia eksportu danych;
5. brak `VIEW_TELEMETRY` ukrywa telemetrię ograniczoną;
6. cross-map zero-cost jest odrzucane;
7. restart odtwarza obecność z trwałego dziennika bez „duchów” sesji;
8. powtarzalny legalny ruch może zostać obserwowany przez IMMUNE, ale Nadzorca nie diagnozuje patologii;
9. propozycja migracji Kustosza nie staje się autoryzacją bez właściwych bramek;
10. brak semantycznej władzy i brak samonadawania praw.

## F3 — Kustosz + Nadzorca: archiwum „pamięci w pamięci”

Minimalny model:

```text
L0 — źródła, obiekty, relacje
L1 — wersjonowane mapy/workspace'y + lineage
L2 — historia tworzenia, używania, przejść i kosztów L1
```

Realizacja ma używać snapshotów, odwołań, hashy i delt, a nie pełnych kopii świata.

`CURATOR` odpowiada za tożsamość, wersję, rodowód i `CURRENT_POINTER`; może wnosić do Agenta PSI propozycje `EXPAND / SPLIT / MERGE / REINDEX / MIGRATE / ARCHIVE / COMPACT / REBALANCE`, lecz nie wykonuje sam przebudowy. `ACCESS_STEWARD` odpowiada za historię obecności, przejść i kosztów.

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
F2.1 NEXT
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

**F2.1 — referencyjny runtime `ACCESS_STEWARD`.**

Nie rozszerzać zakresu przed przejściem regresji ruchu, kosztu, obecności, widoczności telemetrii i recovery.
