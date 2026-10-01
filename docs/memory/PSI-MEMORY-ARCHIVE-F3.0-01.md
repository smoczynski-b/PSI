# PSI-MEMORY-ARCHIVE-F3.0-01 — archiwum „pamięci w pamięci”

**Status:** EXPERIMENTAL / NON-CANONICAL / CONTRACT ONLY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Extends:** `PSI-MEMORY-INSTITUTION-01`, `PSI-MEMORY-CURATOR-PLANNING-01`, `PSI-MEMORY-ACCESS-STEWARD-01`.  
**Does not modify:** CORE5, CANON-03, epistemic status, four-role constitution, live FORUM gateway.

## 1. Cel

F3.0 definiuje archiwum jako trwałą, wersjonowaną pamięć o stanach pamięci i o sposobie ich używania. Archiwum ma umożliwić odtworzenie wskazanej rewizji wraz z kontraktem, pochodzeniem, statusem, uprawnieniami i historią ruchu bez kopiowania całej pamięci przy każdym kroku.

\[
\boxed{\text{archive}=\text{versioned references}+\text{snapshots}+\text{deltas}+\text{lineage}}
\]

Archiwum nie jest źródłem prawdy i nie podnosi statusu epistemicznego treści.

## 2. Trzy poziomy

Poziomy są warstwami administracji i rekonstrukcji, nie nowymi poziomami ontologicznymi PSI.

### L0 — zasób źródłowy

Obejmuje źródła, obiekty, relacje i zdarzenia autorytatywnej pamięci. Archiwum L0 przechowuje przede wszystkim trwałe identyfikatory i skróty treści, a kopię treści tylko wtedy, gdy wymaga tego jawny kontrakt retencji.

### L1 — wersjonowane mapy i workspace'y

L1 przechowuje manifesty wersji map/workspace'ów:

```text
archive_id
object_id / map_id
version_id
parent_version_ids
base_snapshot_id
delta_ids
content_digest
contract_id / contract_digest
provenance_refs
epistemic_status_ref
access_policy_ref
lifecycle_state
created_at
```

Stan wersji nie jest utożsamiany z samym manifestem. Manifest wskazuje dane potrzebne do deterministycznej rekonstrukcji.

### L2 — pamięć użycia pamięci

L2 przechowuje odwołania do historii operacji na L1:

- utworzenie wersji;
- materializacja lineage;
- publikacja `CURRENT_POINTER`;
- wejście/wyjście i ruch między mapami;
- odczyt/retrieval;
- koszt przejścia i użycia;
- archiwizacja/odtworzenie;
- zatwierdzona migracja/przebudowa;
- wynik testu rekonstrukcji.

L2 może wskazywać telemetrię Nadzorcy Ruchu, ale nie kopiuje automatycznie jej treści ograniczonej.

## 3. Rekurencja bez nieskończonej regresji

„Pamięć w pamięci pamięci” nie oznacza tworzenia pełnej kopii L2 po każdym zdarzeniu L2. Rekurencję zatrzymuje się przez niezmienne identyfikatory i skierowane referencje do wcześniejszych rekordów.

\[
\boxed{\text{record about record}=\text{reference}+\text{digest}+\text{typed relation}}
\]

Nie wolno tworzyć nieskończonego łańcucha `snapshot(snapshot(snapshot(...)))` bez kontraktowej potrzeby.

## 4. Jednostka wersji

Minimalny identyfikowalny rekord wersji:

\[
V=(id,parent,base,\Delta,h,c,p,a,s,l,t),
\]

gdzie odpowiednio:

- `id` — stabilny `version_id`;
- `parent` — jawne poprzedniki genealogiczne;
- `base` — snapshot bazowy;
- `Δ` — uporządkowany zbiór delt;
- `h` — skrót rekonstruowanego stanu;
- `c` — kontrakt;
- `p` — proweniencja;
- `a` — referencja polityki dostępu;
- `s` — referencja statusu epistemicznego;
- `l` — stan cyklu życia;
- `t` — czas/rewizja.

`version_id` nie może być ponownie użyty dla innej zawartości.

## 5. Snapshot + delta

Archiwum ma wspierać:

\[
S_k \xrightarrow{\Delta_{k+1}} S_{k+1}\xrightarrow{\Delta_{k+2}}\cdots\xrightarrow{\Delta_n}S_n.
\]

Rekonstrukcja wersji `n`:

\[
\boxed{R(S_k,\Delta_{k+1:n})=S_n}
\]

musi zostać zweryfikowana przez `content_digest` oraz kontrakt wersji.

Pełny snapshot wolno wykonać jako punkt kontrolny, ale nie jest on wymagany przy każdej zmianie. Polityka częstotliwości snapshotów jest osobnym kontraktem wykonawczym.

## 6. CURRENT_POINTER

Kustosz może publikować audytowalny wskaźnik:

\[
CURRENT(object)=version_id.
\]

`CURRENT_POINTER`:

- wskazuje wersję bieżącą w zadanym cyklu życia;
- musi być odwracalny i audytowalny;
- nie usuwa poprzednich wersji;
- nie oznacza automatycznie `TRUE`, `VALID` ani `REUSABLE`;
- nie może być wyprowadzony wyłącznie z daty lub numeru wersji.

\[
\boxed{CURRENT\neq TRUE\neq REUSABLE}
\]

## 7. Status epistemiczny i archiwizacja

Archiwum przechowuje lub wskazuje status epistemiczny, ale go nie ustanawia.

\[
\boxed{ARCHIVE(x)\not\Rightarrow status(x)\uparrow}
\]

\[
\boxed{RESTORE(x)\not\Rightarrow ADMIT(x)}
\]

Stary wynik może pozostać fizycznie dostępny, a jednocześnie mieć `NEEDS_RECHECK`, `STALE`, `POST_QUARANTINED` lub inny status określony przez właściwą warstwę.

## 8. Uprawnienia

Archiwizacja nie rozszerza praw dostępu.

Każdy manifest wersji zawiera `access_policy_ref` oraz identyfikator wersji polityki, jeśli jest istotny. Odtworzenie do aktywnej mapy podlega bieżącej polityce Strażnika i wykonaniu przez Nadzorcę Ruchu.

\[
\boxed{ARCHIVE\_ACCESS\neq ACTIVE\_MAP\_ACCESS}
\]

Telemetria `T1_SECURITY_RESTRICTED` i `T2_AUDIT_DURABLE` zachowuje własne zasady widoczności; L2 nie staje się skrótem omijającym `VIEW_TELEMETRY`.

## 9. Podział ról

### CURATOR

Kustosz:

- materializuje lineage;
- tworzy manifest wersji;
- publikuje `CURRENT_POINTER` po spełnieniu jawnego warunku cyklu życia;
- archiwizuje bez usuwania historii;
- wnosi propozycje przebudowy infrastruktury;
- zapisuje genealogię zatwierdzonej przebudowy.

Kustosz nie zmienia źródłowej treści, statusu epistemicznego, polityki dostępu ani konstytucji.

### ACCESS_STEWARD

Nadzorca:

- dostarcza referencje historii obecności, przejść i kosztów;
- egzekwuje ruch do/z map archiwalnych zgodnie z polityką Strażnika;
- nie nadaje `CURRENT_POINTER` i nie interpretuje lineage.

### SERVANT

Sługa:

- jest jedyną legalną ścieżką trwałych zmian stanu wykonywanych przez runtime;
- zachowuje WAL/MVCC i append-only audit;
- nie wybiera wersji bieżącej i nie interpretuje genealogii.

### GUARDIAN / PSI GATE

Strażnik kontroluje aktywne wejście/wyjście i politykę dostępu. PSI gate kontroluje zadaniową adekwatność przy reprezentacyjnie ryzykownej przebudowie lub ponownym promowaniu mapy do reuse.

## 10. Koszt archiwum

Koszt archiwizacji i odtworzenia jest jawny. Minimalnie śledzimy:

```text
storage_bytes
snapshot_bytes
delta_bytes
reconstruction_steps
reconstruction_io
transition_cost
telemetry_reference_count
```

Kustosz może na tej podstawie zgłaszać `COMPACT`, `REINDEX`, `MIGRATE`, `EXPAND`, `SPLIT` lub `REBALANCE`, lecz sama obserwacja kosztu nie jest autoryzacją przebudowy.

## 11. Konflikty i rygiel fail-closed

Fail-closed obowiązuje m.in. gdy:

- brakuje snapshotu bazowego lub delty;
- skrót rekonstruowanego stanu nie zgadza się z manifestem;
- `version_id` wskazuje dwie różne zawartości;
- brak kontraktu/proweniencji/polityki dostępu wymaganej przez manifest;
- `CURRENT_POINTER` wskazuje nieistniejącą lub niepowiązaną wersję;
- próba restore omija Strażnika/Nadzorcę;
- Kustosz próbuje sam zatwierdzić własną przebudowę;
- L2 próbuje ujawnić telemetrię bez właściwej capability.

## 12. Gate F3.0

Kontrakt przechodzi tylko wtedy, gdy maszynowo potwierdzono:

1. rozdział L0/L1/L2;
2. `snapshot + ordered deltas + digest` jako mechanizm rekonstrukcji;
3. stabilną tożsamość `version_id` i jawnych rodziców;
4. `CURRENT != TRUE != REUSABLE`;
5. archiwizacja i restore nie zmieniają statusu epistemicznego;
6. archiwizacja nie rozszerza uprawnień;
7. restricted telemetry nie staje się publiczna przez L2;
8. trwałe mutacje nadal przechodzą przez SERVANT/MVCC/WAL;
9. Kustosz może proponować przebudowę, ale nie wykonuje jej sam;
10. konflikt-registry obejmuje brak delty/snapshotu, mismatch digestu, kolizję wersji, błędny pointer, nielegalny restore i bypass uprawnień;
11. rekurencja archiwum jest realizowana przez referencje, nie pełne kopiowanie całego archiwum.

Dopiero po `CONTRACT_PASS` wolno rozpocząć F3.1 — referencyjny runtime archiwum i deterministyczną rekonstrukcję wskazanej wersji.
