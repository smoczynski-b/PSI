# Semantica Rozmowy — 04: audyt i korekta wykonania

Current selection: [shared-memory entry](README.md). The later
[active-memory review](#active-memory-review-2026-09-30) supplements the
historical audit below; its findings are not repaired runtime behavior.

Data: 2026-09-30, Europe/Warsaw.
Podstawa: gałąź `psi-memory-map-01`, stan
`db230e498c7f2808164ab4e0ac462b5b7da24751`; dokumenty i wykonania M1–M19,
odzyskane streszczenia ustaleń rozmowy oraz dwa źródłowe archiwa MHTML
z dostarczonego ZIP-u. Pełnego eksportu rozmowy 04 nie odnaleziono.
Nie jest to deklaracja przeczytania wszystkich jej wypowiedzi.

## Ocena wyniku rozmowy

Rozmowa doprowadziła do użytecznego, skończonego laboratorium pamięci:
typowanego grafu, kontroli proweniencji, kontraktów odczytu i jawnych włókien
kandydatów. Rozdzielenie zależności dowodowej, analogii, genealogii i planu
pracy jest poprawne i pozostaje zachowane. M15–M19 zachowują niejednoznaczność
językową zamiast wybierać najbliższą odpowiedź.

Dokumentowane granice są zasadniczo trafne: M4a mierzy bajty przygotowanych
pakietów, M8 rozmiar wybranych fragmentów; żaden z tych pomiarów nie dowodzi
poprawy rozumowania modelu. M4b ma status NOT_RUN. Próby M9 są syntetycznymi
zmianami dwóch uczestników, nie niezależnym badaniem dwóch modeli.

Gałąź ma 117 commitów po bazowym `7f4aecd`; część rozdziela jedną jednostkę
na zapisy pojedynczych plików. Liczba commitów nie mierzy jakości. Historii
nie przepisano; bieżąca naprawa jest jednym spójnym pakietem z testami.

Główna usterka leży między kontraktem a wykonaniem: wybrane przykłady
przechodziły testy, chociaż zmiana węzła, źródła lub typu danych naruszała
deklarowane warunki. Poniższe świadki sprawdzono przez wykonanie kodu.

## Potwierdzone błędy → jednostki → konsekwencje

| Błąd | Jednostka i świadek sprzed poprawki | Wdrożona korekta |
|---|---|---|
| Inny punkt startowy niż w kontrakcie | M12–M15: zadanie o II.7 zwracało także krawędzie wychodzące z II.9; selektor miał stałe `ANCHOR=II.9` | Wspólny wykonawca otrzymuje węzeł z kontraktu; test porównuje zadania o II.7 i II.9. |
| Dowolny wybór jednego z kilku węzłów | M13: „II.9 i II.7” wybierało II.7 według porządku identyfikatorów | NEEDS_ANCHOR_POLICY i brak odczytu. |
| Zakaz odczytany jako dodatnia intencja | M13–M15: „Pomiń zależności dowodowe II.9; pokaż granice” wybierało także przesłanki | Niewspierany zakres wyłączenia daje NEEDS_CONTRACT; obsługiwane „czego nie implikuje” nadal działa. |
| Etykieta zastępowała bieżącą kontrolę źródła | M14/M15 i ścieżka M9: `VALID`/`VERIFIED` wystarczało bez ponownego skrótu | Porównanie fragmentu i całego pliku w chwili użycia; nieaktualny certyfikat nie wraca jako słabsza wskazówka. |
| Tryb certyfikowany wymagał drugiego przełącznika | Pomocnicze wykonanie M14 wymagało `strict=True` niezależnie od kontraktu | Tryb odczytu wykonuje się bez dodatkowej decyzji wywołującego. |
| Ucięcie budżetem nie było oznaczone | M14: budżet 4 wybierał 4 z 5 dostępnych certyfikowanych granic II.9 | Jawne `budget_truncated`; nie utożsamia się limitu ze zbadaniem całego lokalnego zbioru. |
| Nieznany predykat stawał się sprzecznością | M16/M18: literówka `MAESURES` dawała INCONSISTENT | NO_RELATION_CONTRACT, bez pozornego pustego włókna. |
| Nieustalona dziedzina tolerancji | M18 dopuszczało ułamki, NaN i wartości logiczne jako liczbę konfliktów | Wymagane `b∈N₀`; wartości obserwacji są skończonym zbiorem napisów, nie pojedynczym napisem. |
| Pusty wybór omijał kontrolę schematu | M19: błędna relacja z pustym wyborem obiektów przechodziła jako wynik zerowy | Najpierw kontrola relacji i identyfikatorów, potem projekcja. |

Wykonanie kontraktu przeniesiono z pomocniczych procedur testowych do
`scripts/memory_retrieval.py`. Dotychczasowe testy M12–M15 korzystają teraz
z tej samej ścieżki, którą ma stosować agent. Widok M19 nad grafem deklaruje,
że pokazuje zapisane relacje bez ponownej certyfikacji; nie podszywa się pod
odczyt dowodowy.

## Warunek matematyczny

Dla ustalonej dziedziny `W`, poprawnie określonego predykatu `r` i obserwacji `a`:

\[
F_{k+1}=F_k\cap\{x\in W:r(x)=a\}.
\]

Brak definicji `r` oznacza brak legalnego kroku. Nie oznacza, że zbiór po prawej
stronie jest pusty. Dopiero sprzeczne dane dotyczące zdefiniowanego predykatu
mogą legalnie dać `F=∅`.

Dla M18:

\[
F_b=\left\{x\in F_0:
\sum_i\mathbf1\{r_i(x)\notin A_i\}\le b\right\},
\qquad b\in\mathbb N_0.
\]

Przy stałym `b` dodanie poprawnej obserwacji nie powiększa włókna. Zmiana `b`
zmienia kontrakt tolerancji; nie jest nowym świadectwem o świecie. Naprawa
dotyczy dziedziny tych działań, nie ustanawia nowego prymitywu PSI.

## Zegarek: tożsamość i zadanie

Dodany świadek obejmuje dwa zegarki `A,B` o tych samych obserwowanych cechach
materialnych, lecz różnych historiach. Po obserwacji położenia i mierzonej
wielkości pozostaje `F={A,B}`. Dopiero zadeklarowana obserwacja historii
wyodrębnia jeden egzemplarz. Jest to skończony model rozróżnienia zgłoszonego
przez użytkownika; nie twierdzenie o naturalnej ontologii.

Należy rozdzielać:

\[
|q_{\mathrm{cechy}}(F)|=1,
\qquad |q_{\mathrm{historia}}(F)|=2.
\]

Jednoznaczność odpowiedzi na zadanie nie wymaga jednoznaczności całego
obiektu. Nazwa językowa i zgodność kilku cech nie kasują różnicy historii.

## Genealogia źródeł

Skróty całych plików `Principia Semantica Uzupełnienie.mhtml` i
`Kontynuacja projektu PSI.mhtml` zgadzają się z rejestrem:

- `0e69aa1b4b0004edb7a2a40f0d9703e15da5eca38eaa2f8e03e4026c2efebee5`;
- `b93e3a406b6dccd9884d6036121c149e5f928feeed1f34a1156dd9190a467493`.

To weryfikacja tożsamości archiwów. Nie poświadcza automatycznie cytatu,
autorstwa wypowiedzi ani relacji PRECURSOR_OF. Trzy wpisy
CONVERSATION_RECOVERED mają odtworzone lokalizacje/streszczenia, lecz bez
utrwalonego certyfikatu surowego eksportu. Test genealogii nazwano zgodnie
z wykonaniem: REGISTRY_CONSISTENCY_PASS. Nie wykonuje on odzyskiwania archiwów.

## Reguła pracy dla kolejnych modeli

1. Ustal obiekt zadania, kontrakt, źródło i warunek zakończenia.
2. Wykonaj jeden ograniczony odczyt ze wskazanego węzła; zachowaj kierunki i typy relacji.
3. Sprawdź aktualne źródła użytych certyfikatów. Wskazówka wyszukiwawcza nie zastępuje dowodu.
4. Zachowaj wielość kandydatów, brak kontraktu i ucięcie odczytu jako różne stany.
5. Zakończ jednostkę po kontrprzykładzie naprawczym i testach dotkniętych ścieżek.
   Kolejny numer eksperymentu wymaga nowego wybranego zadania.

Przykład właściwego wejścia:

```bash
python scripts/memory_retrieval.py 'dla II.9 pokaż granice, tylko pełne certyfikaty'
```

Pozostają otwarte: niezależny pomiar jakości modeli (M4b), ogólna semantyka
języka i wyłączeń, kompozycja wielu węzłów, certyfikacja historycznych
fragmentów rozmów oraz zastosowanie poza zadanymi skończonymi dziedzinami.
Nie uruchomiono płatnych badań ani nie scalono laboratorium z `main`.

## Active memory review 2026-09-30

Reviewed commit: `fce89bde2d8bb6e95292d435bed84e1702c6b26c`.
Scope: all 46 changed files in the 51 commits after `cf9d91a`, including three
memory specifications, nine experiment protocols, seven TSV registries, ten
runtime modules, twelve regression programs and five workflows. The twelve
new regression programs passed locally. This is a source/code/test inspection,
not a complete transcript review, model-quality trial or fresh literature audit.
Additional boundary witnesses below remain OPEN in the inspected runtime.

### Obiekt → warunki → wielkość → test

Obiekt: lokalna pamięć współdzielona z widokami zadaniowymi, MVCC, dziennikiem
WAL, Sługą i Immunologią. Warunki: jeden proces, jawne zbiory odczytów i
zależności, dostarczona baza odtworzenia oraz jawnie dopuszczone zdarzenia.
Mierzone: równość decyzji po restarcie, legalność reakcji na dane liczbowe,
kompletność wskazania zależnych widoków i rzeczywista liczba odwiedzonych
krawędzi. Źródłem oceny są wykonane kontrprzykłady, nie nazwy ról.

Przejście 12 programów dotyczy ich zapisanych przypadków. Grupy:
aktywna pamięć, skalowanie, unieważnianie, wiele widoków, współbieżne propozycje,
MVCC, integracja współdzielona, WAL, Sługa, Immunologia, instytucja i genealogia.
Test genealogii kontroluje rejestr; etykiet `SOURCE_VERIFIED` nie zweryfikowano
ponownie przez lekturę wszystkich publikacji. Oryginalność pozostaje OPEN.

### Potwierdzone świadki i kierunek napraw

| Jednostka | Odtworzone zachowanie | Warunek odbioru naprawy przez GPT-5 |
|---|---|---|
| Sługa: decyzja po kolizji i restarcie | `C/SEMANTIC_VERDICT` daje BLOCK. `C/RECOVER` daje kolizję. Po ponownym utworzeniu `ServantRuntime` oryginalne `C/SEMANTIC_VERDICT` daje kolizję zamiast powtórzenia BLOCK. | Pierwszy ukończony zapis identyfikatora pozostaje rozstrzygający przed i po restarcie; kolizja jest kronikowana oddzielnie. Powtórzenie nie wykonuje drugiej transakcji. |
| Immunologia: dziedzina liczbowa | `value=NaN` dla `IMM-CONFLICT-BURST` zmienia `NORMAL` na `POST_QUARANTINED` i emituje NOTICE oraz POST_QUARANTINE. | Niepoprawna wartość nie może uruchomić reakcji. Jawnie ustalić dziedzinę progów, obserwacji i całkowitych budżetów; sprawdzić NaN, nieskończoności, wartości logiczne i granice. |
| Immunologia po `RECOVER` | `durable.shared.views` zostaje zastąpione, lecz istniejące `immune.views` wskazuje poprzedni obiekt. Nowy zależny widok `late` nie trafia do REQUEST_RECHECK. | Po odtworzeniu używany jest bieżący indeks albo stara instancja zostaje jawnie wyłączona do ponownego związania. Brak cichego odczytu dawnego indeksu. |
| Koszt rozsyłania | Przy jednej delcie licznik wskazuje jeden widok, lecz `_refresh_indices` odwiedza 18 krawędzi dla początkowego N=8 i 2050 dla N=1024. | Rozdzielić liczbę wybranych widoków od pracy w nich; uwzględnić przebudowę indeksów i narastającą historię zdarzeń. To granica obecnego pomiaru, nie utrata poprawności wyniku. |
| Rzadkie macierze relacji | Zmiana tylko pochodzenia krawędzi z `doc:one` na `doc:two` daje identyczne COO, lecz inny skrót semantycznego stanu. | Przy zadaniu wymagającym pochodzenia zachować metadane obok macierzy. Samo COO sprawdza strukturę relacji, nie cały zapis pamięci. |

Przyczyna pierwszej luki: `_load_completed_commands` bierze ostatni
`SERVANT_RESULT`, również wynik kolizji zapisany przez `_stop(..., remember=False)`.
Wyłączenie zapamiętania działa w żywym słowniku, ale nie w odtwarzaniu kroniki.
Przyczyna drugiej: warunek `value < min_value` nie odrzuca NaN.
Trzecia powstaje na styku poprawnie działających osobno warstw; sam test
odtworzenia dziennika nie obejmuje związania istniejącej Immunologii.

Odtworzenie trzech usterek na wskazanym commicie, bez usług zewnętrznych:

```bash
PYTHONPATH=scripts python - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
from test_servant_runtime import make_durable
from servant_runtime import ServantRuntime, ServantCommand
from test_immune_runtime import make_stack, workspace, obs
from immune_runtime import ReactionBudget

with TemporaryDirectory() as td:
    root = Path(td)
    durable = make_durable(root / 'memory.wal')
    servant = ServantRuntime(durable, root / 'servant.wal')
    original = ServantCommand('C', 'SEMANTIC_VERDICT')
    print(servant.handle(original).disposition)
    servant.handle(ServantCommand('C', 'RECOVER'))
    restarted = ServantRuntime(durable, root / 'servant.wal')
    print(restarted.handle(original).disposition)

with TemporaryDirectory() as td:
    durable, servant, immune = make_stack(td, budget=ReactionBudget())
    result = immune.observe(obs('NAN', 'IMM-CONFLICT-BURST',
        'PROTOCOL_CONFLICT_COUNT', 'proof', float('nan')))
    print(result.status)

with TemporaryDirectory() as td:
    durable, servant, immune = make_stack(td, budget=ReactionBudget())
    servant.handle(ServantCommand('R', 'RECOVER'))
    durable.shared.register('late', workspace('L', 'LROOT', 'L'),
        extra_dependencies=('workspace:proof',))
    result = immune.observe(obs('RECOVERED', 'IMM-INVALIDATION-FANOUT',
        'INVALIDATION_FANOUT', 'proof', 8))
    print(durable.shared.views.direct_dependents('workspace:proof'))
    print(result.requested_rechecks)
PY
```

Zaobserwowane wyniki: `BLOCK_ILLEGAL_TRANSITION`, następnie
`STOP_ESCALATE_CHRONICLE`; `POST_QUARANTINED` dla NaN; bieżący indeks ma
bezpośrednich zależnych `down1, late`, natomiast żądania obejmują `down1, down2`
i pomijają `late`. Program jest historycznym odtworzeniem błędów, nie wzorcem
oczekiwanych poprawnych wyników.

### Co wynika dla projektu

Nowy dział realizuje większą część infrastruktury, niż obejmowała wcześniejsza
ocena M4b. Utrzymywanie widoków przez delty jest już implementacją referencyjną,
a nie samą metaforą. Mierzone przyspieszenia dotyczą skończonych prób
syntetycznych; 12 PASS nie ustanawia jeszcze niezawodności całej integracji
ani poprawy wyników modeli.

Pierwsza jednostka dla GPT-5: naprawa odtwarzania decyzji Sługi i regresja
`oryginał → kolizja → restart → oryginał`. STOP po zachowaniu pierwotnej decyzji,
braku dodatkowego COMMIT i przejściu testów Sługi oraz dotkniętych wywołań
Immunologii. Pozostałe naprawy są kolejnymi, odrębnymi jednostkami.
Nie potrzeba nowego prymitywu, kolejnej roli ani nowej numeracji architektury.

Po naprawach: jeden pełny przebieg z rzeczywistymi rekordami PSI, a następnie
oddzielne badanie jakości modeli i pełnego kosztu. M4b pozostaje NOT_RUN.
Wskazana kolejność jest decyzją wykonawczą tego przeglądu, nie twierdzeniem
o optymalności ani odzyskanym dosłownym poleceniem z rozmowy 04.

### Zakres odzyskania rozmowy i grafiki

Ponowne wyszukiwanie nie dostarczyło pełnego eksportu rozmowy 04. Streszczenia
odtworzyły chmurę punktów z odległymi istotnymi połączeniami, różne obrazy tych
samych danych oraz wymóg ustalania intencji przed zamrożeniem kontraktu.
Zwrócone parafrazy nie są tu traktowane jako dosłowne cytaty, nawet gdy opis
wyniku wyszukiwania nazywał je pełnym cytatem.

W osobnym wątku wizualnym istnieje `PSI-VIZ-TEST-01_factorization.mp4`
(14 s, 1080×1920) i `PSI-VIZ-TEST-01_final-frame.png`. Obejrzano klatki filmu
w 3 s i 8 s oraz planszę końcową; nie deklaruje się obejrzenia każdej klatki.
Świadek rozróżnia `rho(u,v)=u, R(u,v)=u²` od `rho(u,v)=u, R(u,v)=v`.
To prezentacja faktoryzacji i jej niepowodzenia, nie pomiar pamięci modelu.
Pliki nie są częścią tego commitu; ich skróty wiążą oglądane artefakty:

- film: `118b86f5b1e07f6ace014d7dd174ae3d80b0a2a8503cbe0eb93def951b8681bf`;
- plansza: `b3121ba24e6483cba75ccd12ed107af79cc951e5daa20845018a7a81c12791ba`.

Cel użytkownika obejmuje wizualizację wzorów, przekształceń i zależności oraz
możliwość filmu. Zapis formalny dla wykonania, geometria procesu i plansza
dla człowieka mają odrębne zadania. Zasady ich zgodności są w
[kontrakcie reprezentacji](representation-check.md).
