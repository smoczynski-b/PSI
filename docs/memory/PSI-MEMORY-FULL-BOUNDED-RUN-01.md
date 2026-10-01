# PSI-MEMORY-FULL-BOUNDED-RUN-01

**Status:** `PASS_WITH_BOUNDARY`  
**Date:** 2026-09-30  
**Branch:** `psi-memory-map-01`  
**Accepted implementation:** `98dab44c1af3238c4f342413afc99d1d421f3e90`  
**Acceptance workflow:** `36781418888`  
**Acceptance job:** `110112332931`

## 1. Cel

Po zamknięciu lokalnych napraw R1, R2, R6, R7 i R8 wykonano jeden ograniczony przebieg kompozycyjny na rzeczywistych rekordach mapy PSI. Celem nie było dodanie nowego mechanizmu, lecz sprawdzenie, czy istniejące gwarancje przeżywają wspólny epizod:

```text
wersja bieżąca
-> dozwolony dostęp
-> potwierdzone zużycie dokładnej wersji
-> wynik zależny od przesłanki
-> późniejsza zmiana przesłanki
-> nowa wersja bieżąca
-> przerwanie / restart
-> próba ponownego użycia starego wyniku
-> odmowa cichego reuse / NEEDS_RECHECK
-> kontrola receiptów, reconciliation, kosztu i Curatora
```

Zgodnie z kontraktem frontu nowy numer naprawy miał powstać tylko po wykryciu nowego kontrprzykładu systemowego. Takiego kontrprzykładu nie wykryto. **R9 nie powstaje.**

## 2. Rzeczywisty wycinek PSI

Świadek jest zakotwiczony w istniejących plikach:

- `docs/memory/psi-memory-nodes-01.tsv`,
- `docs/memory/psi-memory-edges-01.tsv`.

Użyty stan źródłowy:

```text
P9-I   status = OPEN
P9-I   GATE_FOR   III.13
III.13 status = UNAUTHORIZED
source = docs/control-state.json
```

Test sprawdza te wartości przed rozpoczęciem epizodu. Zmiana `P9-I -> PASSED_INTEGRATION_TEST` zachodzi wyłącznie w izolowanym runtime testowym. Nie modyfikuje `docs/control-state.json`, nie zmienia statusu twierdzeń i **nie oznacza, że P9-I faktycznie przeszedł bramkę matematyczną**.

## 3. Epizod

### A. Wersja V1 i potwierdzone zużycie

Z rzeczywistego wycinka zbudowano wersję archiwalną `version:PSI-P9-I:1` z `P9-I=OPEN`. Ustawiono ją jako bieżącą wersję mapy `PSI:P9-I-GATE`.

Agent przeszedł przez `ACCESS_STEWARD`; zachowano semantykę R6:

```text
cost evidence = PREEXECUTION_QUOTE
quoted compute = 1
incurred cost = None
```

Następnie `consume_version()` zwróciło dokładnie V1 i zapisało trwały receipt. Osobno zapisano:

```text
VERIFIED_CONSUMPTION(V1)
MAP_ASSOCIATION(V1)
```

Drugi rekord pozostał tylko skojarzeniem i nie został awansowany do potwierdzonego zużycia.

### B. Wynik zależny

Przy rzeczywistym stanie `P9-I=OPEN` utworzono wynik zależny odpowiadający stanowi `III.13:UNAUTHORIZED_WHILE_P9-I_OPEN`. Widok wyniku miał status `VALID`.

### C. Curator

Curator otrzymał obserwację poniżej progu. Zgodnie z R8 zapisano trwałą tożsamość z wynikiem `NO_PROPOSAL`; nie powstała propozycja ani mutacja strukturalna.

### D. Zmiana przesłanki i V2

W izolowanym runtime wykonano hipotetyczną zmianę statusu `P9-I`. Mechanizm zależności oznaczył wynik pochodny jako:

```text
NEEDS_RECHECK
```

Stary wynik pozostał przechowywany jako historia, lecz jego obecność nie dawała prawa do ponownego użycia.

Z nowego stanu utworzono `version:PSI-P9-I:2` i ustawiono V2 jako bieżącą wersję mapy.

### E. Restart

Po ponownym zbudowaniu stosu z trwałych dzienników sprawdzono równocześnie:

1. V2 pozostaje wersją bieżącą;
2. receipt V1 nadal wskazuje dokładnie historyczne V1 i ten sam digest;
3. V1 pozostaje jawnie rekonstruowalne po swoim `version_id`;
4. wynik zależny pozostaje `NEEDS_RECHECK`;
5. replay tego samego ruchu nie tworzy drugiego ruchu ani drugiego COMMIT;
6. replay wyniku przez Sługę jest idempotentny i nie przywraca `VALID`;
7. kontrola telemetrii nadal odmawia zapytania bez właściwego celu/uprawnienia;
8. dokładny replay obserwacji Curatora jest idempotentny;
9. ten sam `observation_id` z innym payloadem pozostaje `OBSERVATION_ID_COLLISION`.

## 4. Wynik wykonany

Workflow `36781418888`, job `110112332931` zakończył się `success`.

Główny świadek wyemitował:

```text
PSI-MEMORY-FULL-BOUNDED-RUN-01 PASS_WITH_BOUNDARY
real_records=P9-I:OPEN|GATE_FOR|III.13:UNAUTHORIZED
verified_v1_consumption=PASS
association_not_upgraded=PASS
hypothetical_premise_change_invalidates_result=PASS
restart_preserves_current_v2_and_historical_v1_receipt=PASS
stale_result_reuse=NEEDS_RECHECK
access_reconciliation_no_duplicate_movement_or_commit=PASS
cost_quote_unknown_semantics=PASS
curator_no_proposal_identity_after_restart=PASS
telemetry_gate_after_restart=PASS
```

W tym samym jobie przeszły ponownie:

- R1 journal recovery;
- R2 result reconciliation;
- R6 cost semantics;
- R7 exact consumed version;
- R8 no-proposal observation identity;
- F3.3 Curator planner.

## 5. Dwa wcześniejsze FAIL-e świadka

Dwa wcześniejsze przebiegi nie były kontrprzykładami systemu i nie są liczone jako R9.

### FAIL-H1 — błędna obserwacja warstwy

Run `36780724729`, job `110110009515` zatrzymał się na próbie odczytania z `ServantDecision` pól należących do niższego rezultatu routingu (`delivered_workspaces` / `invalidated_workspaces`). Po usunięciu tej błędnej asercji test doszedł dalej.

### FAIL-H2 — skażony seed restartu

Run `36781220017`, job `110111670479` ujawnił `RESULT_VIEW != NEEDS_RECHECK` po restarcie. Analiza wykazała błąd samego świadka: `ActiveRuntime` mutuje przekazany `Workspace` in place, a test ponownie używał tych samych obiektów-seedów. Restart startował więc z już zmodyfikowanej bazy. Po rejestracji świeżych `deepcopy` — zgodnie z istniejącym wzorcem F1 — właściwy restart zachował `NEEDS_RECHECK` i cały przebieg przeszedł.

Te dwa przypadki są błędami konstrukcji eksperymentu, nie nowymi lukami semantycznymi systemu.

## 6. Granica wyniku

`PASS_WITH_BOUNDARY` oznacza dokładnie:

- jeden deterministyczny, jednoprocresowy epizod kompozycyjny;
- wejście zakotwiczone w rzeczywistych rekordach PSI z repozytorium;
- rzeczywisty mechanizm wersjonowania, receiptów, access/reconciliation, WAL, invalidation i Curatora;
- hipotetyczna zmiana P9-I wyłącznie jako bodziec testowy;
- jawna historyczność V1 i bieżącość V2;
- brak cichego reuse wyniku po zmianie przesłanki.

Wynik **nie** dowodzi:

- że P9-I matematycznie przeszedł;
- poprawności całego PSI dla wszystkich rekordów;
- rozproszonego exactly-once;
- autentyczności zewnętrznego źródła;
- że model przeczytał, zrozumiał lub przyczynowo wykorzystał zwrócony payload;
- przewagi PSI nad zwykłym kontekstem lub prostym retrievalem;
- opłacalności ekonomicznej całego systemu.

Ostatnie dwa punkty należą do osobnego F5.

## 7. Konkluzja operacyjna

Lokalne hardeningi R1/R2/R6/R7/R8 przeszły pierwszy wspólny przebieg z przerwaniem i restartem. Nie znaleziono nowego kontrprzykładu wymagającego kolejnej naprawy.

```text
R9 = NOT_CREATED
FULL_BOUNDED_RUN = PASS_WITH_BOUNDARY
```

Po tym wyniku należy dokonać jawnego wyboru kolejnego frontu pomiędzy:

```text
F5 — porównanie skuteczności modelowej
R5 — kierunkowość relacji wizualnych -> F4.4
```

Nie należy rozpoczynać żadnego z nich jako części tego samego przebiegu.
