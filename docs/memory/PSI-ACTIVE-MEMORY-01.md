# PSI-ACTIVE-MEMORY-01 — aktywne środowisko pamięciowe

Status: **EXPERIMENTAL / NON-CANONICAL / CPU REFERENCE**. Data: 2026-09-30.

Nie tworzy nowego prymitywu PSI, nie zmienia CORE5 i nie zmienia CANON-03. To warstwa wykonawcza nad istniejącą eksperymentalną pamięcią relacyjną.

## 1. Pytanie

Czy agent może uniknąć wielokrotnej rekonstrukcji kontekstu, zachowując prawo do wniosku, jeśli zamiast pełnego ponownego odczytu utrzymuje zadaniowy stan roboczy i aktualizuje go tylko przez istotne delty?

Schemat:

\[
\mathcal M_t \xrightarrow{C_c} W_{t,c},
\qquad
W_{t+1,c}=U(W_{t,c},\Delta\mathcal M_t).
\]

`M_t` pozostaje autorytatywną pamięcią relacyjną ze źródłami, statusem i pochodzeniem. `W_{t,c}` jest efemerycznym widokiem roboczym dla kontraktu `c`.

## 2. Kontrakt fazy 01

Obiekt: aktywny, lokalny widok istniejącej pamięci PSI.

Źródło: wynik legalnego `memory_retrieval` / równoważny jawnie dostarczony widok `RETRIEVED` i kontrakt `COMPILED`.

Operacje:

1. kompilacja widoku do `Workspace`;
2. przyrostowa aktualizacja przez typowane zdarzenia;
3. kompilacja relacji do backend-neutralnych rzadkich płaszczyzn COO;
4. konsolidacja stanu roboczego jako obiektu pochodnego (`WORKSPACE_SNAPSHOT`);
5. odtworzenie i kontrola skrótu;
6. selektywna invalidacja przez zależności;
7. konserwatywny adapter obiektów PSI-FORUM.

STOP tej fazy: referencyjna implementacja CPU i regresja muszą przejść bez rozszerzenia kanonu i bez modyfikacji żywego gatewayu FORUM.

## 3. Stan roboczy

Referencyjnie:

\[
W=(c,a,E,S,n,h),
\]

gdzie `c` jest kontraktem, `a` kotwicą, `E` zbiorem aktywnych typowanych krawędzi, `S` stanami węzłów, `n` rewizją, a `h` skrótem stanu.

Stan nie jest prawdą niezależną od pamięci źródłowej. Jest skompilowanym widokiem zadaniowym.

## 4. Tensorowa realizacja bez zależności od GPU

Dla każdego typu relacji `r` budowana jest osobna rzadka płaszczyzna:

\[
A^{(r)}_{ij}=1
\quad\Longleftrightarrow\quad
v_i\xrightarrow{r}v_j.
\]

Eksport referencyjny ma postać COO:

`relation -> [[i,j,value], ...]`.

Typy relacji nie są zwijane do jednej macierzy bliskości. Jest to warunek zachowania rozróżnień pamięci. Ten format można później odwzorować na rzadkie tensory PyTorch/CUDA bez zmiany semantyki eksperymentu.

GPU nie jest wymagane w fazie 01. Najpierw musi istnieć wariant referencyjny, względem którego można sprawdzać zgodność backendu GPU.

## 5. Delta

Obsługiwane zdarzenia fazy 01:

- `EDGE_UPSERT`;
- `EDGE_REMOVE`;
- `NODE_STATUS_SET`;
- `FORUM_OBJECT_SEEN`.

Delta niezwiązana z aktywnymi węzłami nie zmienia lokalnego `Workspace`. Delta dotykająca aktywnego komponentu może dołączyć nowy węzeł i relację. Identyfikator zdarzenia zapewnia idempotencję ponownego dostarczenia. Czasy zdarzeń muszą być jawnie strefowe; faza 01 rozróżnia `event_time` i `ingest_time`.

Nie dowodzi to jeszcze asymptotycznej przewagi. Faza 01 ustanawia semantykę, którą później trzeba zmierzyć względem pełnej rekonstrukcji.

## 6. Pamięć w pamięci

Stan roboczy może zostać skonsolidowany:

\[
W_t\longrightarrow m_t\in\mathcal M_{candidate},
\]

jako `WORKSPACE_SNAPSHOT` zawierający:

- identyfikator i skrót kontraktu;
- skrót stanu;
- zależności od krawędzi i źródeł;
- pełny deterministyczny payload potrzebny do odtworzenia;
- status.

Odtworzenie jest legalne tylko wtedy, gdy skrót stanu zgadza się z payloadem. Zmiana zależności oznacza `STALE` kandydata do ponownego użycia; snapshot nie rozszerza własnego zakresu.

## 7. Granica FORUM

Faza 01 **nie zmienia PSI-FORUM**. Dostarcza wyłącznie funkcję tłumaczącą obiekt FORUM na lokalne zdarzenie.

Zwykłe `CLAIM`, `PROOF`, `COUNTEREX`, `UNRESOLVED` lub `TEST` są na tym poziomie tylko `FORUM_OBJECT_SEEN`; samo zobaczenie obiektu nie mutuje semantycznego grafu.

Również samo istnienie jawnego obiektu `RELATION` z payloadem `from/relation/to` **nie wystarcza do dopuszczenia relacji**. Domyślnie adapter zwraca tylko `FORUM_OBJECT_SEEN`. Dopiero wywołujący, który wcześniej przeszedł odpowiednią bramę źródło/kontrakt/FORUM, może jawnie ustawić `admitted=True`; wtedy powstaje `EDGE_UPSERT` z pochodzeniem `forum:<OID>` i statusem `ADMITTED_FORUM_RELATION`.

Zatem:

\[
\boxed{\text{FORUM object observed}\neq\text{relation admitted}.}
\]

Docelowy kierunek po przejściu fazy 01:

\[
\text{FORUM ledger}\to\Delta\mathcal M\to\Delta W_i
\]

z selektywną propagacją do tych agentów, których aktywne światy zależą od zmienionych obiektów.

## 8. Kryteria regresji

`test_active_memory.py` sprawdza:

1. trzy różne typy relacji pozostają trzema płaszczyznami;
2. niezwiązana delta nie zmienia stanu roboczego;
3. związana delta zmienia tylko dotknięty komponent;
4. ponowne dostarczenie tego samego eventu jest idempotentne;
5. snapshot odtwarza identyczny skrót stanu;
6. invalidacja reaguje tylko na zależności snapshota;
7. `CLAIM` FORUM nie mutuje grafu;
8. nieadmitowany `RELATION` FORUM nie mutuje grafu;
9. jawnie dopuszczony `RELATION` może wejść do aktywnego widoku z zachowaniem pochodzenia;
10. czas bez strefy jest odrzucany.

## 9. Następne fazy — nie wykonane w tym kroku

- pomiar `full reconstruction` vs `delta update`;
- indeks odwrotnych zależności i propagacja invalidacji;
- równoległe workspaces wielu agentów;
- `processing_time` oraz polityka reorder window;
- adapter PyTorch sparse i test zgodności CPU/GPU;
- subskrypcje FORUM i routing delty;
- test, czy koszt kroku zależy od `|Delta|` bardziej niż od `|M|`.

Dopiero wynik tych pomiarów może uzasadnić twierdzenia o przewadze szybkościowej lub jakości współpracy agentów.
