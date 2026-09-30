# PSI-MEMORY-ACCESS-STEWARD-01 — Nadzorca Ruchu jako sługa Strażnika

**Status:** EXPERIMENTAL / NON-CANONICAL / ROLE SUBCONTRACT  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Extends:** `PSI-MEMORY-INSTITUTION-01` GUARDIAN execution boundary.  
**Does not modify:** CORE5, CANON-03, the four-role constitution, epistemic status, live FORUM gateway.

## 1. Status roli

`ACCESS_STEWARD` nie jest piątym równorzędnym urzędem konstytucyjnym. Jest podporządkowanym aparatem wykonawczym Strażnika:

\[
\boxed{GUARDIAN \triangleright ACCESS\_STEWARD}
\]

Strażnik jest właścicielem polityki dostępu. Nadzorca Ruchu wykonuje i rejestruje decyzje ruchowe zgodnie z konkretną wersją tej polityki.

\[
\boxed{policy\_owner=GUARDIAN,\qquad executor=ACCESS\_STEWARD}
\]

Nadzorca nie może sam tworzyć, rozszerzać, reinterpretować ani przyznawać uprawnień.

## 2. Obiekt kontroli

Pamięć roboczo traktujemy jako sieć map i legalnych bram:

\[
\mathfrak B=(\mathcal M,\mathcal G),
\]

z bramami

\[
g_{ij}:M_i\to M_j.
\]

Topologiczna lub techniczna osiągalność nie stanowi prawa przejścia:

\[
\boxed{\text{reachable}(M_j)\neq\text{authorized}(M_i\to M_j)}.
\]

Jednostką pracy Nadzorcy jest żądanie przejścia:

\[
\tau_{req}=(request\_id,session\_id,actor\_id,M_i,M_j,p,Cap,v_{policy},B).
\]

Minimalne pola:

- `request_id`;
- `session_id`;
- `actor_id`;
- `map_from`;
- `map_to`;
- `declared_purpose`;
- `requested_capability`;
- `policy_version`;
- `budget`;
- czas/identyfikator zdarzenia.

## 3. Obecność

Nadzorca utrzymuje sesyjny stan obecności:

\[
Loc_t(session)=M_i.
\]

Jeden aktor może mieć wiele sesji, ale jedna sesja w kontrakcie F2.0 znajduje się najwyżej w jednej mapie naraz. Przejście z mapy innej niż bieżąca jest niedozwolone — brak teleportacji logicznej.

## 4. Rozłączne zdolności

Uprawnienia są rozłączne i nie wynikają z siebie automatycznie:

- `ENTER_MAP` — wejście do mapy;
- `TRANSIT_TO_MAP` — przejście z jednej mapy do drugiej;
- `ACT_IN_MAP` — wykonanie operacji w mapie;
- `EXPORT_FROM_MAP` — wyniesienie/przeniesienie danych z mapy;
- `VIEW_TELEMETRY` — dostęp do telemetrii ruchu.

Obowiązuje:

\[
\boxed{
ENTER\neq ACT\neq EXPORT\neq VIEW\_TELEMETRY
}
\]

oraz

\[
\boxed{MOVE(agent,M_i\to M_j)\neq EXPORT(data,M_i\to M_j)}.
\]

## 5. Legalność przejścia

Przejście może zostać wykonane tylko wtedy, gdy łącznie zachodzi:

\[
\boxed{
LEGAL(\tau)=Policy\land Purpose\land Capability\land SourceLocation\land TargetState\land Budget
}
\]

Znaczenie:

1. `Policy` — istnieje jawna, obowiązująca wersja polityki Strażnika;
2. `Purpose` — deklarowany cel mieści się w zakresie polityki;
3. `Capability` — sesja/aktor ma dokładnie potrzebne uprawnienie;
4. `SourceLocation` — `map_from` zgadza się z bieżącą lokalizacją sesji;
5. `TargetState` — mapa docelowa istnieje i przyjmuje dany typ przejścia;
6. `Budget` — koszt przejścia mieści się w jawnie przydzielonym budżecie.

Brak któregokolwiek materialnego pola oznacza fail-closed. Nadzorca nie uzupełnia polityki domysłem.

## 6. Koszt przejścia

Przejście pomiędzy różnymi mapami jest kosztem. Minimalny model zachowuje wektor:

\[
\kappa(\tau)=(c_{compute},c_{transfer},c_{context},c_{latency},c_{disclosure},c_{sync},c_{risk}).
\]

Dla przejścia między różnymi mapami:

\[
\boxed{M_i\neq M_j\Rightarrow \|\kappa(\tau)\|_1>0}.
\]

Jeśli zadanie wymaga jednego skalara, wolno użyć dopiero kontraktowo podanych wag:

\[
c_{\mathcal T}(\tau)=w_{\mathcal T}\cdot\kappa(\tau).
\]

Nadzorca nie może ukryć kosztu, wyzerować go w celu przepuszczenia ruchu ani przekroczyć budżetu bez nowej autoryzacji.

## 7. Telemetria

Ruch generuje osobny zapis telemetrii. Minimalne klasy widoczności:

- `T0_SESSION_LOCAL` — dane potrzebne samej sesji;
- `T1_SECURITY_RESTRICTED` — operacyjna telemetria ochrony;
- `T2_AUDIT_DURABLE` — trwały ślad audytowy;
- `T3_AGGREGATED` — dane zagregowane, bez ujawniania pełnej obecności.

Prawo użycia bramy nie daje prawa oglądania telemetrii. Sesja może wiedzieć, że `M_j` istnieje i jest dla niej osiągalna, ale nie musi wiedzieć, kto jeszcze znajduje się w `M_j`.

Każdy rekord przejścia powinien wiązać co najmniej:

```text
request_id
session_id
actor_id
map_from
map_to
declared_purpose
policy_version
capabilities_used
event_time
estimated_cost
actual_cost
result
telemetry_class
```

## 8. Legalne działania Nadzorcy

Nadzorca może:

- `CHECK_ACCESS` względem jawnej polityki Strażnika;
- `ENTER` / `EXIT` / `TRANSIT` po spełnieniu kontraktu;
- utrzymywać `SESSION_LOCATION` i stan obecności;
- `METER_TRANSITION_COST`;
- `APPEND_MOVEMENT_TELEMETRY`;
- `DENY_ACCESS` lub `STOP_ESCALATE` fail-closed przy braku materialnego warunku;
- przekazać legalną, trwałą zmianę do `SERVANT`, jeśli operacja wymaga mutacji stanu trwałego.

## 9. Czego Nadzorca nie może

Zakazane:

- `MINT_POLICY` / `MODIFY_POLICY`;
- `SELF_AUTHORIZE`;
- `DECLARE_DOMAIN_TRUTH`;
- edycja semantycznej zawartości mapy;
- obejście Sługi przy trwałej mutacji;
- `CLEAR_IMMUNE_QUARANTINE`;
- przepisywanie lub usuwanie historii ruchu;
- ujawnienie `T1/T2` bez osobnej zdolności `VIEW_TELEMETRY`;
- wnioskowanie `ENTER_MAP => ACT_IN_MAP`;
- wnioskowanie `TRANSIT_TO_MAP => EXPORT_FROM_MAP`;
- traktowanie fizycznej/topologicznej osiągalności jako autoryzacji;
- zatwierdzanie przebudowy proponowanej przez Kustosza.

## 10. Styki z pozostałymi rolami

### GUARDIAN

Strażnik stanowi/wybiera obowiązującą politykę; Nadzorca wykonuje ją. Zmiana `policy_version` wymaga nowej decyzji względem nowej wersji — wcześniejsza zgoda nie jest automatycznie reinterpretowana.

### SERVANT

Nadzorca kontroluje ruch sesji i bramy. Sługa kontroluje legalność trwałych przejść stanu pamięci. Nadzorca nie zapisuje za plecami WAL/MVCC.

### IMMUNE

Seria pojedynczo legalnych ruchów może utworzyć wzorzec patologiczny. Nadzorca rejestruje zdarzenia; Immunologia odpowiada za wykrycie i reakcję na wzorzec. Legalność pojedynczego ruchu nie jest orzeczeniem zdrowia systemu.

### CURATOR

Kustosz może zaproponować migrację/przebudowę dzielnicy. Nadzorca może oszacować koszt i wykonać zatwierdzony ruch, ale nie zatwierdza samej przebudowy i nie tworzy genealogii zamiast Kustosza.

## 11. Relacja do epistemiki PSI

Telemetria, lokalizacja i częstotliwość przejść nie są dowodem prawdziwości treści mapy:

\[
\boxed{
traffic(M),presence(M),access(M)\not\Rightarrow truth(M).
}
\]

`ACCESS_STEWARD` jest mechanizmem wykonawczym i audytowym, nie bramką dowodową.

## 12. Gate F2.0

Kontrakt F2.0 przechodzi tylko wtedy, gdy maszynowo potwierdzono:

1. konstytucyjny rejestr nadal zawiera dokładnie cztery role;
2. `ACCESS_STEWARD` jest podporządkowany `GUARDIAN`;
3. właścicielem polityki jest `GUARDIAN`, wykonawcą `ACCESS_STEWARD`;
4. `ENTER`, `ACT`, `EXPORT`, `VIEW_TELEMETRY` są rozdzielone;
5. przejście między różnymi mapami ma niezerowy koszt;
6. klasy telemetrii są jawne i rozdzielone;
7. zakazano samonadawania praw, prawdy domenowej, edycji treści i przepisywania historii;
8. rejestr konfliktów zawiera świadki braku polityki, budżetu, lokalizacji, uprawnienia i widoczności telemetrii.

Dopiero po PASS kontraktu wolno rozpocząć F2.1 — referencyjny runtime Nadzorcy Ruchu.
