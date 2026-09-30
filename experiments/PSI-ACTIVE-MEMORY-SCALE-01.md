# PSI-ACTIVE-MEMORY-SCALE-01 — pełna rekonstrukcja kontra delta

Status: EXPERIMENTAL / NON-CANONICAL. Data: 2026-09-30.

## Cel

Sprawdzić pierwszą realizacyjną hipotezę aktywnej pamięci:

\[
W_t+\Delta_t\longrightarrow W_{t+1}
\]

powinno po jednorazowym zbudowaniu świata roboczego wymagać pracy związanej z
istotną deltą, a nie ponownego przetworzenia całej pamięci. Test nie zmienia
CORE5, CANON-03 ani M1–M19.

## Świadek błędu w wersji 01

Pierwsza implementacja `apply_delta` była semantycznie poprawna, lecz wykonywała
`deepcopy` całego `Workspace`, a test styczności budował `ws.nodes` przez skan
krawędzi. Zatem koszt pojedynczej delty pozostawał zależny od rozmiaru aktywnego
widoku. Nie wolno było interpretować tego jako implementacji hipotezy
\(|\Delta|\)-lokalnej.

## Naprawa wykonawcza

`scripts/active_memory_runtime.py` dodaje warstwę wykonawczą nad autorytatywnym
`Workspace`:

1. jednorazowy indeks liczby incydencji węzłów;
2. stałoczasowy test, czy zdarzenie dotyka aktywnego świata;
3. mutację single-writer bez kopiowania całego grafu;
4. stabilne, append-only indeksy węzłów;
5. rzadkie patche `SET/REMOVE` postaci `(relation, source_index, target_index)`,
   które mogą być później bez zmiany semantyki przekazane backendowi tensorowemu;
6. osobny `semantic_digest`, który porównuje treść roboczą bez metadanych
   operacyjnych `revision/processed_events`.

Indeksy nie są recyklingowane po usunięciu krawędzi. Jest to świadoma własność
referencyjnej wersji: stabilność identyfikatora wykonawczego ma pierwszeństwo
przed kompaktowaniem.

## Kontrakt testu

Dla rozmiarów

\[
N\in\{128,1024,8192,32768\}
\]

budujemy syntetyczny, lecz dokładnie kontrolowany widok z `ROOT` i `N` typowanymi
krawędziami. Następnie wykonujemy tę samą dopuszczoną zmianę:

\[
ROOT\xrightarrow{DELTA\_REL}NEW.
\]

Porównujemy dwa sposoby otrzymania stanu końcowego:

- **FULL** — ponowne `compile_workspace` z `N+1` rekordów;
- **DELTA** — jedna aktualizacja już istniejącego `ActiveRuntime`.

Warunek merytoryczny:

\[
\operatorname{SemDigest}(W_{\rm FULL})
=
\operatorname{SemDigest}(W_{\rm DELTA}).
\]

Dodatkowo test wymaga zachowania indeksów wszystkich wcześniej istniejących
węzłów, dopisania `NEW` na końcu przestrzeni indeksów i odrzucenia zdarzenia
całkowicie niezwiązanego z aktywnym światem.

## Pomiar

Test raportuje medianę czasu pięciu powtórzeń dla obu dróg, ale **czas nie jest
bramą CI**. Na współdzielonym runnerze czas ścienny jest zmienny i nie stanowi
samodzielnego dowodu złożoności.

Twarda kontrola pracy jest prostsza:

- FULL musi odczytać `N+1` rekordów krawędzi;
- DELTA po zbudowaniu indeksu bada dokładnie 1 zdarzenie i emituje 1 patch.

To jest świadek konstrukcyjny implementacji przyrostowej, nie dowód asymptotyczny
całego przyszłego systemu.

## Granice

- `ActiveRuntime` jest obecnie single-writer; brak transakcji współbieżnych i rollbacku.
- Odtworzenie po restarcie nadal wymaga rekonstrukcji indeksu z `Workspace`.
- Nie ma jeszcze backendu PyTorch/CUDA ani pomiaru GPU.
- Nie ma jeszcze propagacji invalidacji po grafie zależności; test dotyczy jednej
  lokalnej zmiany.
- Adapter FORUM nie jest podłączony do żywego gatewayu. Zdarzenia FORUM mogą
  mutować runtime dopiero po zewnętrznym, jawnym `admitted=True`.
- Syntetyczne skalowanie nie zastępuje benchmarku na rzeczywistej historii FORUM.

## Kryterium przejścia

PASS wymaga równocześnie:

1. semantycznej zgodności FULL i DELTA dla wszystkich `N`;
2. jednego badanego zdarzenia i jednej mutacji po stronie DELTA;
3. stabilności indeksów istniejących węzłów;
4. braku wpływu niezwiązanej delty;
5. przejścia wcześniejszych regresji pamięci.

Po PASS następnym legalnym krokiem jest indeks odwrotnych zależności i test
selektywnej invalidacji, a dopiero potem wieloagentowa współbieżność i backend GPU.
