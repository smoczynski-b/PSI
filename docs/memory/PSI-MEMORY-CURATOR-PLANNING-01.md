# PSI-MEMORY-CURATOR-PLANNING-01 — Kustosz jako planista infrastruktury pamięci

**Status:** EXPERIMENTAL / NON-CANONICAL / ROLE AMENDMENT  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Extends:** `PSI-MEMORY-INSTITUTION-01` section CURATOR.  
**Does not modify:** CORE5, CANON-03, epistemic status, live FORUM gateway.

## 1. Cel

Kustosz nie jest wyłącznie archiwistą. Na podstawie własnej, jawnie ograniczonej wiedzy o stanie pamięci ma także pełnić funkcję **planisty infrastruktury pamięci**: wykrywać potrzeby pojemnościowe i strukturalne oraz wnosić do Agenta PSI audytowalne wnioski o przebudowę.

Kustosz **nie otrzymuje prawa samodzielnego przydziału zasobów ani przebudowy pamięci**.

\[
\boxed{
CURATOR:\ observe\ memory\ structure\to propose\ restructuring
}
\]

ale

\[
\boxed{
CURATOR\not\to execute\ structural\ mutation\ unilaterally.
}
\]

## 2. Dzielnice pamięci

Roboczo dzielnica pamięci jest kontraktowo wskazanym obszarem zasobu:

\[
\mathcal D_i\subseteq\mathcal M,
\]

wydzielonym przez jawne kryterium: funkcję, zakres, kontrakt, linię genealogiczną, profil dostępu, obciążenie albo kombinację tych cech.

`DISTRICT` nie jest nowym prymitywem PSI ani ontologią wiedzy. Jest jednostką administracji pamięcią.

## 3. Co Kustosz obserwuje

Kustosz może utrzymywać metryki administracyjne takie jak:

- rozmiar i tempo wzrostu dzielnicy;
- liczba i gęstość relacji;
- częstotliwość odczytu i aktualizacji;
- historia wersji i supersesji;
- fan-out zależności;
- koszt retrieval i koszt przejść;
- udział zasobu archiwalnego/zimnego;
- liczba konfliktów związanych ze strukturą przechowywania;
- wykorzystanie przydzielonego budżetu pamięci;
- częstotliwość wspólnego użycia map/dzielnic.

Są to dane administracyjne. Same nie nadają treści statusu epistemicznego.

## 4. Legalne wnioski planistyczne

Kustosz może emitować tylko propozycję, np.:

```text
EXPAND(district, requested_capacity)
SPLIT(district, proposed_partition)
MERGE(district_a, district_b)
REINDEX(district, index_contract)
MIGRATE(district, target_tier)
ARCHIVE(district_or_map)
COMPACT(district, representation_contract)
REBALANCE(district_set)
```

Każdy wniosek musi zawierać co najmniej:

```text
proposal_id
subject / district
observed_problem
supporting_metrics
proposed_operation
expected_benefit
estimated_cost
risk / information-loss risk
required_dependencies
rollback/recovery requirement
```

## 5. Agent PSI jako odbiorca wniosku

Wniosek Kustosza trafia do Agenta PSI jako problem zadaniowy, nie jako polecenie wykonawcze:

\[
CURATOR
\to STRUCTURE\_PROPOSAL
\to PSI\_AGENT
\to evaluation.
\]

Agent PSI ocenia m.in.:

1. czy diagnoza Kustosza jest wsparta danymi;
2. czy przebudowa zachowuje kontrakt i wymagane rozróżnienia;
3. czy istnieje tańsza realizacja tej samej funkcji;
4. jaki jest koszt migracji/przejść;
5. które role muszą zatwierdzić wykonanie;
6. jaki test rozstrzyga powodzenie przebudowy.

## 6. Dwa rodzaje przebudowy

### 6.1 Przebudowa wykonawcza

Zmienia realizację przechowywania bez zamierzonej zmiany semantycznego stanu:

\[
M\to M',\qquad Sem(M')=Sem(M)
\]

w zadanym kontrakcie.

Przykłady: nowy indeks, shard, tier pamięci, lokalizacja fizyczna, układ cache, format wykonawczy.

### 6.2 Przebudowa reprezentacyjna/semantycznie ryzykowna

Może scalać lub przekształcać reprezentacje. Wtedy obowiązuje bramka PSI. Dla reprezentacji \(\rho\):

\[
\boxed{\ker_{eq}\rho\subseteq E_{\mathcal T}}
\]

w zadaniu, dla którego nowa organizacja ma być używana.

Kustosz nie może uznać utraconego rozróżnienia za nieistotne bez takiej bramki.

## 7. Rozdział ról podczas przebudowy

Roboczy cykl:

```text
CURATOR        -> diagnoza + propozycja przebudowy
PSI AGENT      -> ocena zadaniowa / projekt / test
GUARDIAN       -> skutki dla admission/access/policy
ACCESS_STEWARD -> koszt i legalność ruchu/migracji między mapami
SERVANT        -> legalność wykonawczych przejść stanu
IMMUNE         -> obserwacja patologii podczas/po przebudowie
CURATOR        -> zapis genealogii przebudowy i nowego CURRENT_POINTER
```

Żadna z tych ról nie może samotnie wykonać całego cyklu.

## 8. Plan zagospodarowania pamięci

Kustosz może utrzymywać pochodny, audytowalny stan planistyczny:

\[
\mathfrak Z_t=(\mathcal D_t,C_t,L_t,A_t,H_t),
\]

gdzie odpowiednio:

- \(\mathcal D_t\) — dzielnice;
- \(C_t\) — przydzielone/żądane pojemności;
- \(L_t\) — obciążenia i koszty;
- \(A_t\) — dostępność/osiągalność administracyjna;
- \(H_t\) — historia przebudów.

To jest **mapa administracyjna pamięci**, nie autorytatywna treść wiedzy.

## 9. Rygiel władzy

\[
\boxed{
\text{Kustosz może projektować potrzebę, ale nie ma kluczy do buldożera.}
}
\]

Zabronione bez zewnętrznego zatwierdzenia i legalnej ścieżki wykonawczej:

- samodzielne zwiększenie własnego budżetu;
- samodzielna zmiana granic dzielnicy;
- fizyczne przeniesienie zasobu;
- usunięcie historii;
- kompresja kasująca rozróżnienia wymagane przez zadanie;
- zmiana polityki dostępu;
- zmiana konstytucji ról.

## 10. Relacja z frontem robót

Bieżącą kolejność określa [CURRENT-WORK-FRONT-01](CURRENT-WORK-FRONT-01.md).
Poniżej zachowano pierwotną zależność faz; nie jest to aktualne wskazanie NEXT.

- F0/F1: najpierw integralność i pełny przebieg pamięci;
- F2: kontrakt `ACCESS_STEWARD`;
- F3: implementacja Kustosza i archiwum może już obejmować moduł planistyczny opisany tutaj;
- wykonanie przebudów wymaga osobnych eksperymentów po PASS odpowiednich bramek.

## 11. Minimalny przyszły test

Dla sztucznej dzielnicy o kontrolowanym wzroście Kustosz powinien:

1. wykryć przekroczenie jawnego progu administracyjnego;
2. utworzyć `EXPAND` lub `SPLIT` proposal z metrykami;
3. nie zmienić pamięci samodzielnie;
4. po zaakceptowanej przebudowie zachować pełną genealogię starego i nowego układu;
5. wykazać, że wskazane zadanie daje tę samą odpowiedź przed i po przebudowie wykonawczej.

Current implementation: the proposal-only planner is implemented in
[F3.3](PSI-MEMORY-CURATOR-F3.3-01.md) with PASS_WITH_BOUNDARY for its reference
cases. Execution of restructuring and its post-change equivalence test remain
NOT IMPLEMENTED. Journal continuation and no-proposal observation identity
are open R1/R8 findings in the [current audit](AUDIT-ROZMOWY-04.md#memory-and-agent-review-2026-09-30).
