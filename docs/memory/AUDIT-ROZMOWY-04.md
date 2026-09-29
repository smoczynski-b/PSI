# Semantica Rozmowy — 04: audyt i korekta wykonania

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
