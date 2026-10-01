# PSI-MEMORY-ACCESS-STEWARD-F2.1-01 — referencyjny runtime Nadzorcy Ruchu

**Status:** EXPERIMENTAL / NON-CANONICAL / IMPLEMENTATION REGRESSION  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Depends on:** `PSI-MEMORY-ACCESS-STEWARD-01`, `PSI-MEMORY-SERVANT-01`, durable shared memory / MVCC / WAL.  
**Does not modify:** CORE5, CANON-03, four-role constitution, epistemic status, live FORUM gateway.

## 1. Cel

F2.1 implementuje najwęższy runtime wykonawczy kontraktu F2.0:

```text
Guardian policy snapshot
        ↓
ACCESS_STEWARD
        ↓
check purpose/capability/location/target/budget
        ↓
SERVANT TRANSACT
        ↓
MVCC + durable WAL
        ↓
authoritative session presence
```

Nadzorca nie jest właścicielem polityki. Otrzymuje jawny snapshot `GuardianAccessPolicy` przez zewnętrzny resolver i wykonuje tylko dokładnie dopasowane reguły.

## 2. Stan obecności

Autorytatywna obecność sesji nie jest prywatnym słownikiem runtime'u. Jest materializowana w administracyjnym workspace jako relacja:

```text
ACCESS_PRESENCE_ROOT -- SESSION_AT::<session_id> --> <map_id>
```

Jedna sesja może mieć najwyżej jeden taki rekord. Runtime przy starcie skanuje stan odzyskany z durable shared memory i zatrzymuje się przy wykryciu wielu lokalizacji tej samej sesji.

`OUTSIDE` jest stanem braku relacji obecności, nie dodatkową mapą wiedzy.

## 3. Brak bocznego zapisu

Każde `ENTER`, `TRANSIT`, `EXIT` wymagające trwałej zmiany obecności jest tłumaczone na `MVCCProposal` i przekazywane jako:

```text
ServantCommand(kind="TRANSACT")
```

Nadzorca nie wywołuje `durable.commit` bezpośrednio.

\[
\boxed{
ACCESS\_STEWARD\to SERVANT\to MVCC\to WAL
}
\]

Jego własny `AccessChronicle` jest wyłącznie append-only audytem żądań, decyzji i telemetrii ruchu; nie jest źródłem prawdy o bieżącej lokalizacji.

## 4. Rozdzielenie praw

Runtime implementuje osobno:

- ruch: `ENTER_MAP` / `TRANSIT_TO_MAP`;
- sprawdzenie prawa działania: `ACT_IN_MAP`;
- sprawdzenie prawa eksportu: `EXPORT_FROM_MAP`;
- wgląd w telemetrię: `VIEW_TELEMETRY`.

Wejście lub tranzyt nie tworzą żadnego z pozostałych praw.

## 5. Koszt i budżet

Koszt zachowuje pełny wektor F2.0:

```text
compute
transfer
context
latency
disclosure
synchronization
risk
```

Dla zmiany lokalizacji zarówno koszt szacowany, jak i zmierzony muszą mieć dodatnią normę L1. Budżet jest sprawdzany składowo; runtime nie może kompensować przekroczenia jednej osi nadmiarem innej bez osobnego kontraktu wag.

Najpierw sprawdzany jest koszt szacowany, następnie zewnętrzny deterministyczny `cost_meter` dostarcza koszt rzeczywisty. Przekroczenie któregokolwiek rygla blokuje ruch przed trwałą mutacją.

## 6. Target/health gate

Mapa docelowa musi istnieć i jawnie przyjmować dany typ ruchu. `health_gate_open=False` blokuje ruch. Nadzorca nie ma operacji zwalniającej kwarantannę i nie może użyć samego żądania ruchu jako obejścia Immunologii.

## 7. Wersjonowanie polityki

Każde żądanie jest związane z `policy_version`. Jeżeli wersja aktywna Strażnika zmieniła się, stara decyzja nie jest reinterpretowana:

```text
old policy request -> DENY_ACCESS / re-evaluate under current policy
```

Brak aktywnej lub rozpoznanej polityki daje fail-closed `STOP_ESCALATE`.

## 8. Idempotencja i restart

`request_id` jest kluczem idempotencji:

- ten sam identyfikator + ten sam fingerprint -> zwrot pierwotnej decyzji bez drugiego ruchu;
- ten sam identyfikator + inny fingerprint -> `STOP_ESCALATE: REQUEST_ID_COLLISION`.

Po restarcie:

1. durable shared memory odtwarza skomitowane przejścia;
2. nowy `SERVANT` odtwarza własną kronikę;
3. nowy `ACCESS_STEWARD` odczytuje bieżącą obecność z autorytatywnego workspace;
4. `AccessChronicle` odtwarza ukończone `request_id`.

Wyjście usuwa relację obecności; kolejny restart nie może utworzyć obecności fantomowej.

## 9. Telemetria

Każdy wykonany ruch zapisuje `ACCESS_MOVEMENT` z klasą `T2_AUDIT_DURABLE`. API odczytu telemetrii wymaga osobnej reguły `VIEW_TELEMETRY` oraz jawnie dozwolonej klasy.

- `T0_SESSION_LOCAL` — rekordy własnej sesji;
- `T1_SECURITY_RESTRICTED` — pełne rekordy bezpieczeństwa;
- `T2_AUDIT_DURABLE` — trwały audyt;
- `T3_AGGREGATED` — tylko agregaty bez identyfikatorów sesji/aktorów.

## 10. Regresje

`test_access_steward_runtime.py` sprawdza co najmniej:

1. legalne wejście `OUTSIDE -> M1`;
2. brak automatycznego `ACT`, `EXPORT`, `VIEW_TELEMETRY` po wejściu;
3. brak cichej reinterpretacji starej wersji polityki;
4. fail-closed przy braku polityki;
5. blokadę teleportacji logicznej przez niezgodność `map_from`;
6. nieznaną mapę docelową;
7. zamknięty health gate;
8. zerowy koszt ruchu;
9. przekroczenie budżetu przez koszt szacowany;
10. przekroczenie budżetu przez koszt zmierzony;
11. legalny tranzyt `M1 -> M2`;
12. brak prawa eksportu po tranzycie;
13. kontrolę klas telemetrii i agregację;
14. obecność odpowiednich `COMMIT` w durable WAL oraz decyzji Sługi;
15. restart z rekonstrukcją `M2`;
16. idempotentny replay bez drugiego `ACCESS_MOVEMENT`;
17. kolizję `request_id`;
18. legalny `EXIT` i brak fantomowej obecności po kolejnym restarcie;
19. brak bezpośredniego `durable.commit` w runtime Nadzorcy;
20. brak autorytetu prawdy domenowej.

## 11. Granica wyniku

Jeżeli regresje przejdą, status brzmi:

```text
PSI-MEMORY-ACCESS-STEWARD-F2.1 PASS_WITH_BOUNDARY
```

Granica:

- deterministyczny runtime pojedynczego procesu;
- polityka Strażnika jest dostarczona, nie tworzona przez Nadzorcę;
- brak implementacji runtime'u Strażnika;
- brak rozproszonej współbieżności i blokad wielu writerów;
- brak żywego FORUM;
- brak autonomicznego wykrywania patologii (to domena IMMUNE);
- brak mutacji semantycznej zawartości map;
- koszt jest kontraktowym wektorem administracyjnym, nie twierdzeniem o optymalności globalnej.

Po PASS F2.1 legalnym następnym frontem pozostaje F3: Kustosz + Nadzorca i archiwum „pamięci w pamięci”.
