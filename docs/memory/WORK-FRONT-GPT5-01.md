# WORK-FRONT-GPT5-01 — front robót pamięci współdzielonej

**Status:** EXPERIMENTAL / NON-CANONICAL / WORK SELECTION  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.  
**Primary rule:** integrity and replay before new roles; source state before visualization; semantics before GPU.

## 0. Cel

Doprowadzić eksperymentalną pamięć PSI do jednego sprawdzonego przebiegu, w którym późniejszy agent może odzyskać wynik razem z warunkami jego legalnego użycia, historią zmian, lokalizacją w mapach oraz kosztem przejść — bez pomylenia reprezentacji z autorytatywnym stanem.

Architektura robocza:

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

## F0 — naprawić integralność istniejącego runtime

Kolejność jest zamrożona:

1. **SERVANT restart/collision — PASS.** Pierwotny ukończony werdykt pozostaje rozstrzygający po kolizji identyfikatora i restarcie; kolizja ma osobny zapis kronikarski.
2. **IMMUNE numeric domain — PASS.** NaN, ±∞, wartości logiczne i tekst są odrzucane przed oceną sygnatury; skończone wartości muszą należeć do jawnej dziedziny sygnatury (`NONNEGATIVE_INTEGER` / `BINARY_FLAG`). Wartość spoza dziedziny nie może uruchomić reakcji ani zwiększyć licznika sygnatury.
3. **IMMUNE recovered-view binding — PASS.** `RECOVER` zachowuje tożsamość publicznych uchwytów `shared` i `shared.views`, podmieniając ich odzyskany stan in-place. Długowieczne role instytucjonalne nie pozostają więc przy martwym indeksie; regresja wymusza, by stary uchwyt IMMUNE widział nowo zarejestrowany widok i jego zależności po recovery.
4. **Cost accounting — NEXT.** Oddzielić liczbę wybranych widoków od rzeczywistej pracy: odświeżenie indeksów, odwiedzone krawędzie i historia zdarzeń.

**Gate F0:** wszystkie istniejące regresje + osobne regresje kontrprzykładów przechodzą; żadna naprawa nie zmienia kompetencji ról.

## F1 — jeden pełny przebieg zadaniowy

Wykonać jeden source-bound scenariusz end-to-end:

```text
source + contract
→ bounded retrieval
→ workspace/map compile
→ admitted update
→ selective invalidation
→ institutional handling
→ durable commit/WAL
→ restart
→ replay/rebind
→ rechecked reuse by later agent
```

Sprawdzić równocześnie:

- semantyczną równoważność przed i po restarcie;
- zachowanie provenance/status/version;
- właściwe unieważnienie tylko licencjonowanych zależności;
- pełny koszt przebiegu, nie tylko liczbę dotkniętych widoków.

**Gate F1:** drugi agent może użyć wyniku bez ponownej rekonstrukcji źródła i potrafi wykazać, dlaczego użycie jest legalne lub dlaczego wymaga ponownego sprawdzenia.

## F2 — rozdzielić istniejącego Sługę od Nadzorcy Ruchu

Nie rozszerzać obecnego `SERVANT`, którego obiektem jest legalność przejść stanu pamięci.

Nowa kandydacka rola robocza: **NADZORCA RUCHU / `ACCESS_STEWARD`** — sługa Strażnika pełniący funkcję szefa ochrony środowiska map.

Jego obiekt:

```text
agent/session
+ map_from
+ map_to
+ declared_purpose
+ authorization
+ time
+ transition_cost
+ result
```

Zakres:

- wejścia i wyjścia;
- obecność sesji w mapach;
- przejścia między mapami;
- koszt przejścia;
- telemetria ruchu;
- kontrola ujawnienia telemetrii według osobnych uprawnień.

Obowiązuje rygiel:

\[
\boxed{
\text{prawo przejścia}
\neq
\text{prawo działania w mapie}
\neq
\text{prawo wglądu w telemetrię}
}
\]

`ACCESS_STEWARD` nie rozstrzyga prawdy, nie modyfikuje konstytucji i nie zastępuje `GUARDIAN`, `SERVANT`, `IMMUNE` ani `CURATOR`.

**Gate F2:** najpierw kontrakt i konflikt-registry, potem implementacja. Brak implementacji przed PASS kontraktu roli.

## F3 — Kustosz + Nadzorca: archiwum „pamięci w pamięci”

Zbudować archiwum jako rekurencyjną historię stanów i operacji, bez kopiowania całej pamięci przy każdym kroku.

Minimalny model:

```text
L0 — źródła, obiekty, relacje
L1 — wersjonowane mapy/workspace'y + lineage
L2 — historia tworzenia, używania, przejść i kosztów L1
```

Realizacja ma używać snapshotów, odwołań, hashy i delt.

`CURATOR` odpowiada za tożsamość, wersję, rodowód i `CURRENT_POINTER`; ponadto może projektować i wnosić do Agenta PSI zapotrzebowanie na `EXPAND / SPLIT / MERGE / REINDEX / MIGRATE / ARCHIVE / COMPACT / REBALANCE`, ale nie może samodzielnie wykonywać przebudowy ani przydzielać sobie zasobów.  
`ACCESS_STEWARD` odpowiada za historię dostępu, obecności, przejść i kosztów.

Archiwizacja nie zmienia statusu epistemicznego i nie rozszerza uprawnień odwołanego obiektu.

**Gate F3:** wskazany stan pamięci da się odtworzyć z właściwym kontraktem, provenance, wersją, uprawnieniami i historią użycia.

## F4 — wizualizacja jako sprawdzalny widok, nie dekoracja

Dopiero po F1–F3 ustalić wspólną gramatykę wizualną dla WWW, analizy i animacji. Rodowód ruchomej notacji PSI-VIZ pochodzi z rozmowy `Konstruowanie litery a`; późniejsze rygory pamięci aktywnej ograniczają sposób jej użycia.

Każdy obraz/animacja musi wskazywać:

- `memory_revision` / snapshot;
- `contract_id`;
- identyfikatory obiektów;
- typ i kierunek relacji;
- dostęp do wymaganych provenance/status/version;
- znaczenie położenia, odległości, barwy, grubości i animacji.

Rozróżniać bez wyjątku:

\[
\boxed{
\text{structural relation}
\neq
\text{embedding geometry}
\neq
\text{display layout}
}
\]

Zmiana układu graficznego przy tym samym stanie nie może zmieniać odpowiedzi semantycznej. Jeżeli odległość koduje koszt, tolerancję, czas lub wielkość fizyczną, jednostka i kontrakt muszą być jawne.

Pierwsze animacje powinny pokazywać operacje, nie „ładne grafy”:

1. zawężanie włókna kandydatów;
2. rozszczepienie po obserwacji rozdzielającej;
3. invalidację po zmianie przesłanki;
4. przejście agenta `M_i → M_j` z kosztem i uprawnieniem;
5. genealogy/version replay;
6. ten sam stan w dwóch układach graficznych.

**Gate F4:** ta sama treść i zadanie dają tę samą odpowiedź z pełnego zapisu i z wizualnego widoku zawierającego wymagane metadane; kontrola stratna zostaje odrzucona przez warunek PSI.

## F5 — zmierzyć korzyść dla modelu

Dopiero po ustabilizowaniu wykonania porównać:

- szeroki kontekst źródłowy;
- pamięć kierowaną M4b;
- prosty comparator leksykalny;
- formalny/relacyjny pakiet pamięci;
- ten sam formalny stan z wizualnym widokiem operacyjnym.

Stałe: zadanie, dane, źródła, kontrakt, model i kryterium oceny.  
Zmienne: sposób reprezentacji/doboru kontekstu.

Nie utożsamiać niższego kosztu wejścia z lepszym rozumowaniem.

## F6 — tensor/GPU dopiero jako kompilacja sprawdzonego stanu

Po F1–F5:

\[
\mathcal M_t \xrightarrow{C_c} \Theta_{t,c}
\]

z trwałymi indeksami, rzadkimi patchami i zachowanym mapowaniem do rekordów autorytatywnych.

GPU służy propagacji, wyszukiwaniu motywów, przecięciom, transportowi i lokalnym aktualizacjom. Nie jest warstwą prawdy.

\[
\boxed{
\text{tensor geometry proposes; PSI licenses inference}
}
\]

**Gate F6:** wynik tensorowy ma deterministyczny ślad do kontraktu i rekordów, a utrata metadanych jest jawnie wykrywana.

## F7 — FORUM/live multi-agent dopiero po stabilizacji lokalnej

Żywe FORUM, subskrypcje i wieloagentowe routing/cost accounting są późniejszym frontem. Najpierw musi przejść lokalny scenariusz F1 z archiwum F3.

Docelowo:

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
F0 \rightarrow F1 \rightarrow F2 \rightarrow F3 \rightarrow F4 \rightarrow F5 \rightarrow F6 \rightarrow F7
}
\]

Wyjątek: dokumentacja kontraktu F2/F3 może powstawać równolegle z F0, ale nie wolno rozszerzać runtime przed PASS F0/F1.

## Czego teraz nie robić

- nie tworzyć CORE6 ani R4;
- nie scalać `psi-memory-map-01` z `main`;
- nie przeciążać istniejącego `SERVANT` funkcją ochrony budynku;
- nie robić z grafiki lub COO stanu autorytatywnego;
- nie implementować rekursywnego archiwum przez pełne kopiowanie wszystkich map;
- nie twierdzić, że „wszystkie połączenia są realizowalne”; każda krawędź musi mieć typ, warunki, uprawnienia i koszt;
- nie przechodzić do GPU przed wykazaniem równoważności semantycznej i pełnego kosztu lokalnego przebiegu;
- nie używać popularności, roli instytucjonalnej ani telemetrii jako dowodu prawdziwości.

## Najbliższa jednostka kodowa

**F0.4 — full cost accounting for local update/index refresh.**

Po jej PASS następny ruch jest wyznaczony przez powyższą kolejność, bez ponownego wyboru architektury.
