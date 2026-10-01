# PSI-MEMORY-IMMUNE-01

**Status:** EXPERIMENTAL / NON-CANONICAL / PASS TARGET  
**Branch:** `psi-memory-map-01`  
**Depends on:** `PSI-MEMORY-INSTITUTION-01`, `PSI-MEMORY-SERVANT-01`, selective dependency routing.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## 1. Cel

Pierwsza implementacja warstwy immunologicznej ma sprawdzić, czy system może reagować na jawnie licencjonowane wzorce patologiczne bez nadawania detektorowi władzy epistemicznej i bez wywoływania lawinowej autoimmunizacji.

Minimalny cykl:

```text
licensed observation
-> NOTICE
-> optional POST_QUARANTINE
-> optional REQUEST_RECHECK (declared dependency paths only)
-> bounded reaction / escalation
```

## 2. Zakres kompetencji

IMMUNE może:

- rozpoznać wyłącznie zarejestrowaną sygnaturę;
- działać wyłącznie po `ADMITTED`;
- prowadzić własną pamięć sygnatur i reakcji;
- emitować `NOTICE`;
- emitować `POST_QUARANTINE`;
- emitować `REQUEST_RECHECK` dla workspace'ów znalezionych przez istniejący indeks zależności;
- emitować `CLEAR_ANOMALY`, gdy jawnie licencjonowany warunek wygaszenia zostanie spełniony.

IMMUNE nie może:

- orzekać `TRUE/FALSE`;
- kasować obiektów, źródeł lub historii;
- bezpośrednio ustawiać `VALID/STALE/NEEDS_RECHECK/REVOKED`;
- zwalniać obiektu z kwarantanny do aktywnej wymiany;
- zmieniać własnych progów lub sygnatur;
- reagować na nieznany wzorzec przez analogię;
- omijać SŁUGI.

## 3. Sygnatury

Rejestr `docs/memory/psi-memory-immune-signatures-01.tsv` jest częścią kontraktu wykonawczego. Sygnatura wiąże:

```text
signature_id
observation_kind
threshold
quarantine?
request_recheck?
clear?
runbook_id
```

Brak zgodnej sygnatury oznacza:

\[
\boxed{\text{NO LICENSED SIGNATURE} \Rightarrow \text{NO AUTONOMOUS ACTION}}
\]

## 4. Rozdział zdrowia i epistemiki

Stan zdrowia IMMUNE:

\[
H\in\{NORMAL,POST\_QUARANTINED,RECOVERED\}.
\]

jest odrębny od epistemicznego stanu workspace'u.

`REQUEST_RECHECK` jest żądaniem proceduralnym; nie zmienia samo przez się:

```text
VALID -> NEEDS_RECHECK
```

Takie przejście musi zostać wykonane przez właściwy mechanizm zależności/epistemiki po zaakceptowanym kontrakcie.

## 5. Budżet reakcji

Aby ograniczyć autoimmunizację, reakcja posiada dwa limity:

- `max_actions` — maksymalna liczba akcji instytucjonalnych w jednej reakcji;
- `max_rechecks` — maksymalna liczba workspace'ów, do których można wysłać `REQUEST_RECHECK`.

Jeśli tranzytywne domknięcie zależności przekracza budżet:

\[
\boxed{\text{NO ARBITRARY PREFIX}}
\]

czyli IMMUNE nie wybiera pierwszych N ofiar. Może zachować lokalną kwarantannę źródła i emituje eskalację `BUDGET_EXHAUSTED_ESCALATE` bez częściowej propagacji recheck.

## 6. SŁUGA jako proceduralny ogranicznik

Każda akcja IMMUNE przechodzi jako typed `INSTITUTION_ACTION` przez `ServantRuntime` z uprzednio autoryzowanym `runbook_id`.

SŁUGA może ACK/BLOCK/STOP akcję proceduralną, ale nie diagnozuje anomalii i nie ustala prawdy treści.

## 7. Testy

Regresja `scripts/test_immune_runtime.py` wymaga:

1. tylko licencjonowane sygnatury powodują reakcję;
2. obiekty przed admission pozostają poza kompetencją IMMUNE;
3. `NOTICE + POST_QUARANTINE + REQUEST_RECHECK` przechodzi przez SŁUGĘ;
4. recheck targets są wyłącznie z indeksu zależności;
5. IMMUNE nie mutuje epistemicznego statusu workspace'ów;
6. budżet blokuje lawinę i nie wybiera arbitralnego prefiksu;
7. `CLEAR_ANOMALY` wymaga aktywnej kwarantanny;
8. `CLEAR_ANOMALY` daje `RECOVERED`, ale nadal wymaga Strażnika do release;
9. replay tej samej obserwacji jest idempotentny;
10. kolizja `observation_id` zatrzymuje lokalne wykonanie;
11. pamięć immunologiczna odtwarza zdrowie/sygnatury po restarcie.

## 8. Granica

To nie jest system uczący się. Nie ma:

- ML/anomaly scoring;
- adaptacji progów;
- uczenia sygnatur;
- diagnozy językowej;
- globalnej polityki zagrożeń;
- automatycznego release;
- rozproszonej koordynacji.

Pierwszy cel to dowód rozdziału kompetencji i ograniczonej homeostazy wykonawczej.
