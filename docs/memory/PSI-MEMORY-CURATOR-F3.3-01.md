# PSI-MEMORY-CURATOR-F3.3-01 — minimalny Kustosz-planista

**Status:** EXPERIMENTAL / NON-CANONICAL / PASS_WITH_BOUNDARY candidate  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Implements:** `PSI-MEMORY-CURATOR-PLANNING-01` minimal proposal-only runtime.  
**Does not modify:** CORE5, CANON-03, epistemic status, Guardian policy, live FORUM gateway.

## 1. Wynik

F3.3 materializuje minimalny automat planistyczny Kustosza:

```text
explicit administrative metrics
+ PSI_AGENT-owned planning policy
+ licensed threshold rule
→ STRUCTURE_PROPOSAL(PROPOSED)
→ SERVANT procedural gate
→ append-only Curator planning chronicle
```

Nie istnieje ścieżka:

```text
proposal → execute / apply / allocate
```

w runtime Kustosza.

## 2. Typowane operacje

Warstwa propozycji dopuszcza tylko:

```text
EXPAND | SPLIT | MERGE | REINDEX | MIGRATE | ARCHIVE | COMPACT | REBALANCE
```

Każda reguła planistyczna jest własnością zewnętrznej, wersjonowanej polityki o authority=`PSI_AGENT`. Kustosz nie tworzy ani nie zmienia sam progów.

## 3. Świadek

Dzielnica `district:alpha` ma metrykę:

```text
capacity_utilization = 0.95
```

przy jawnej regule:

```text
CAPACITY-HIGH:
  operation = EXPAND
  capacity_utilization GTE 0.90
```

Kustosz emituje propozycję zawierającą co najmniej:

- `proposal_id`;
- dzielnicę;
- obserwowany problem;
- metrykę i wartość;
- operację `EXPAND`;
- oczekiwaną korzyść;
- oszacowany koszt;
- ryzyko i ryzyko utraty informacji;
- zależności (`budget:memory`, `guardian:access-review`);
- wymaganie rollback/recovery;
- wymagany test odbioru;
- wersję polityki, `rule_id`, `observation_id`;
- status wyłącznie `PROPOSED`.

Jednocześnie:

```text
durable.revision = 0
workspace.state_digest = unchanged
```

czyli sama propozycja nie przebudowuje pamięci.

## 4. Rygle

Zamrożone:

\[
\boxed{PROPOSAL\neq AUTHORIZATION\neq EXECUTION}
\]

\[
\boxed{CURATOR\ planning\ metric\neq epistemic\ status}
\]

\[
\boxed{threshold\ policy\neq self-authored\ by\ CURATOR}
\]

Kustosz nie może przez ten runtime:

- zwiększyć budżetu;
- zmienić granic dzielnicy;
- wykonać migracji;
- zmienić polityki Strażnika;
- zmienić statusu epistemicznego;
- zmienić konstytucji;
- uznać propozycji za wdrożoną.

## 5. Trwałość i kolizje

Proposal chronicle jest append-only i hash-chained przez `JSONLWAL`.

Sprawdzane są:

- idempotentny replay tej samej obserwacji;
- `OBSERVATION_ID_COLLISION` dla zmienionej obserwacji pod tym samym ID;
- `PROPOSAL_ID_COLLISION` gdy ta sama wersja polityki/rule id próbuje wygenerować inną propozycję;
- odrzucenie nieaktualnej wersji polityki;
- restart/recovery propozycji i jej statusu `PROPOSED`;
- brak trwałego wpisu bez autoryzowanego runbooku Sługi.

## 6. Bramka proceduralna

Każda nowa trwała propozycja przechodzi przez:

```text
CURATOR planner
→ SERVANT / INSTITUTION_ACTION:NOTICE
→ authorized runbook CURATOR-PLANNER-01
→ Curator planning WAL
```

Sługa nie ocenia sensu przebudowy; sprawdza wyłącznie legalność proceduralnej ścieżki zapisu propozycji.

## 7. Granica

F3.3 nie bada jakości strategii planowania ani nie wykonuje przebudów. To deterministyczny single-process proposal engine na jawnych metrykach administracyjnych i jawnych progach.

Po zielonym CI F3 można uznać za funkcjonalnie domknięty na poziomie referencyjnym:

```text
F3.0 archive contract
F3.1 versioned archive runtime
F3.2 usage/movement L2 integration
F3.3 Curator proposal-only planner
```

Następny front: F4 / PSI-VIZ — sprawdzalny widok konkretnej rewizji pamięci, bez utożsamiania geometrii rysunku z relacją semantyczną.
