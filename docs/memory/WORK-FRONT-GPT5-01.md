# WORK-FRONT-GPT5-01 — front robót pamięci współdzielonej

**Status:** EXPERIMENTAL / NON-CANONICAL / HISTORICAL FRONT  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.  
**Primary rule:** integrity and replay before new roles; source state before visualization; semantics before GPU.

> Current selection: [CURRENT-WORK-FRONT-01](CURRENT-WORK-FRONT-01.md).
> This document preserves the earlier phase plan. Its NEXT paragraphs do not
> override the current repair queue or later implementation results.

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

\[
\boxed{
\text{selective routing across workspaces}
\not\Rightarrow
\text{full local update }O(|\Delta|)
}
\]

## F1 — source-bound end-to-end reuse/restart — PASS_WITH_BOUNDARY

Wykonano pełny przebieg:

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

Wynik: źródło odczytane raz; po czystym restarcie Agent B ma `REUSE_ALLOWED` bez rekonstrukcji źródła; po zmianie przesłanki stary wynik pozostaje zapisany, ale przechodzi do `NEEDS_RECHECK`, także po kolejnym restarcie.

\[
\boxed{\text{stored result}\neq\text{permission to reuse result}}
\]

## F2 — Nadzorca Ruchu / `ACCESS_STEWARD`

### F2.0 — kontrakt + rejestr konfliktów — CONTRACT_PASS

`ACCESS_STEWARD` jest podporządkowanym wykonawcą Strażnika, nie piątą rolą konstytucyjną:

\[
\boxed{GUARDIAN\triangleright ACCESS\_STEWARD}
\]

\[
\boxed{policy\_owner=GUARDIAN,\qquad executor=ACCESS\_STEWARD}
\]

Zamrożono:

\[
\boxed{ENTER\neq ACT\neq EXPORT\neq VIEW\_TELEMETRY}
\]

oraz dla różnych map:

\[
\boxed{M_i\neq M_j\Rightarrow\|\kappa(\tau)\|_1>0}.
\]

### F2.1 — referencyjny runtime — PASS_WITH_BOUNDARY

Zaimplementowano deterministyczny przebieg:

```text
Guardian policy snapshot
→ ACCESS_STEWARD
→ purpose/capability/location/target/budget
→ cost meter
→ SERVANT TRANSACT
→ MVCC + WAL
→ authoritative session presence
→ append-only movement telemetry
```

Autorytatywna obecność sesji nie jest zapisywana bocznym kanałem:

\[
\boxed{ACCESS\_STEWARD\to SERVANT\to MVCC\to WAL}
\]

Regresje obejmują wejście/tranzyt/wyjście, pojedynczą lokalizację sesji, koszt, rozdział capability, policy-version, health gate, replay, collision, telemetrię i recovery.

**Boundary:** pojedynczy proces, jawny snapshot polityki Strażnika, brak live FORUM i rozproszonej współbieżności.

## F3 — Kustosz + Nadzorca: archiwum „pamięci w pamięci”

### F3.0 — kontrakt L0/L1/L2 + rekonstrukcja — CONTRACT_PASS

Zamrożono trzy warstwy administracyjne:

```text
L0 — źródła, obiekty, relacje i zdarzenia autorytatywne
L1 — wersjonowane mapy/workspace'y + manifest + lineage
L2 — historia tworzenia, używania, przejść, kosztów i operacji na L1
```

Archiwum używa:

\[
\boxed{\text{stable refs}+\text{snapshot}+\text{ordered deltas}+\text{digests}+\text{lineage}}
\]

z warunkiem rekonstrukcji:

\[
\boxed{R(S_k,\Delta_{k+1:n})=S_n}
\]

i sprawdzeniem `content_digest`.

„Pamięć w pamięci pamięci” nie oznacza rekurencyjnego pełnego kopiowania archiwum:

\[
\boxed{\text{record about record}=\text{reference}+\text{digest}+\text{typed relation}}
\]

Zamrożono także:

\[
\boxed{CURRENT\neq TRUE\neq REUSABLE}
\]

\[
\boxed{ARCHIVE(x)\not\Rightarrow status(x)\uparrow}
\]

\[
\boxed{RESTORE(x)\not\Rightarrow ADMIT(x)}.
\]

Archiwizacja nie rozszerza uprawnień; L2 nie może ujawniać ograniczonej telemetrii bez `VIEW_TELEMETRY`; trwałe mutacje pozostają w ścieżce `SERVANT/MVCC/WAL`. Kustosz może projektować i wnosić potrzebę przebudowy, lecz nie wykonuje jej sam i nie przydziela sobie zasobów.

Artefakty:

- `docs/memory/PSI-MEMORY-ARCHIVE-F3.0-01.md`;
- `docs/memory/psi-memory-archive-contract-01.tsv`;
- `docs/memory/psi-memory-archive-conflicts-01.tsv`;
- `scripts/test_memory_archive_contract.py`;
- `.github/workflows/memory-archive-contract.yml`.

Workflow `PSI memory archive contract`, run `36747572272`, zakończył się `success`. W tym samym jobie przeszły: F3.0, F2.0, czterorólna konstytucja i regresja Sługi.

### F3.1 — referencyjny runtime archiwum — NEXT

Następna jednostka ma zrealizować deterministyczny runtime bez garbage collection i bez autonomicznej przebudowy:

```text
Workspace/version state
→ immutable archive manifest
→ base snapshot or prior snapshot reference
→ ordered deltas
→ content digest
→ CURRENT_POINTER update by Curator path
→ reconstruct(version_id)
→ verify digest / contract / lineage
```

Minimalne regresje F3.1:

1. wersja bazowa + dwie delty rekonstruują dokładnie stan docelowy;
2. brak delty/snapshotu blokuje rekonstrukcję fail-closed;
3. digest mismatch blokuje reuse;
4. `version_id` collision daje STOP;
5. `CURRENT_POINTER` nie usuwa starej wersji i przeżywa restart;
6. archiwizacja zachowuje `NEEDS_RECHECK` lub inny status zamiast go podnosić;
7. restore nie daje automatycznie admission/access;
8. ograniczona telemetria pozostaje tylko referencją bez capability do treści;
9. lineage rodziców nie jest inferowany z czasu;
10. koszt snapshot/delta/reconstruction jest jawnie mierzony;
11. trwałe zapisy runtime przechodzą przez Sługę/WAL albo osobny jawnie zatwierdzony kontrakt trwałości — brak bocznego zapisu;
12. rekurencyjny zapis L2 używa referencji, a nie pełnych kopii całego archiwum.

## F4 — wizualizacja jako sprawdzalny widok

Rodowód ruchomej notacji PSI-VIZ pochodzi z rozmowy `Konstruowanie litery a`.

Każdy obraz/animacja musi wskazywać rewizję pamięci, kontrakt, identyfikatory obiektów, typ/kierunek relacji i dostęp do wymaganych provenance/status/version.

\[
\boxed{\text{structural relation}\neq\text{embedding geometry}\neq\text{display layout}}
\]

Pierwsze animacje: zawężanie włókna, rozszczepienie po obserwacji, invalidacja, przejście `M_i→M_j` z kosztem/uprawnieniem, genealogy/replay, ten sam stan w dwóch layoutach.

## F5 — zmierzyć korzyść dla modelu

Porównać przy stałym zadaniu/modelu/źródłach: szeroki kontekst, pamięć kierowaną, comparator leksykalny, formalny pakiet relacyjny i ten sam stan z wizualnym widokiem operacyjnym.

## F6 — tensor/GPU jako kompilacja sprawdzonego stanu

\[
\mathcal M_t\xrightarrow{C_c}\Theta_{t,c}
\]

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

## Priorytet wykonawczy

\[
\boxed{F0\to F1\to F2.0\to F2.1\to F3.0\to F3.1\to F4\to F5\to F6\to F7}
\]

Aktualnie:

```text
F0   PASS_WITH_BOUNDARY
F1   PASS_WITH_BOUNDARY
F2.0 CONTRACT_PASS
F2.1 PASS_WITH_BOUNDARY
F3.0 CONTRACT_PASS
F3.1 NEXT
```

## Czego teraz nie robić

- nie tworzyć CORE6 ani R4;
- nie scalać `psi-memory-map-01` z `main`;
- nie robić z `ACCESS_STEWARD` piątej roli konstytucyjnej;
- nie pozwalać Kustoszowi samodzielnie wykonywać przebudowy lub zwiększać własnego budżetu;
- nie utożsamiać `CURRENT_POINTER` z prawdą lub prawem do reuse;
- nie traktować restore jako admission;
- nie rozszerzać access przez archiwizację;
- nie kopiować całego archiwum rekurencyjnie;
- nie usuwać historii pod nazwą archiwizacji;
- nie robić z grafiki/COO stanu autorytatywnego;
- nie przechodzić do GPU przed zachowaniem semantyki i provenance.

## Najbliższa jednostka

**F3.1 — referencyjny runtime archiwum: snapshot + delta + manifest + deterministic reconstruct + CURRENT_POINTER persistence.**

Nie rozszerzać zakresu o garbage collection, autonomiczne `COMPACT/MIGRATE`, semantyczną kompresję ani FORUM przed przejściem tej regresji.
