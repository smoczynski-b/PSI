# M4b — wykonanie porównania A/B/C

Status: PREPARED / MODEL_RUN_NOT_EXECUTED. Data: 2026-09-30.
Korekta kierunku rozmowy 04; bez zmiany CORE5 i bez nowego numeru M.

Zakres po doprecyzowaniu użytkownika: A/B/C porównuje dobór kontekstu
tekstowego. Nie bada jeszcze zasadniczej hipotezy o pracy i wymianie agentów
przez formalne zapisy procesów ani o geometrii opartej na ograniczeniach
fizycznych. Korzystny wynik M4b nie uprawnia do uznania tych hipotez za sprawdzone.
Chemiczną motywację opisuje [bieżący cel pamięci](../docs/memory/README.md).

## Obiekt → warunki → pomiar

Obiekt: wykonanie jednego zadania Go G4 przez ten sam model w trzech świeżych,
odizolowanych kontekstach. Zadanie i siedem kryteriów oceny zachowuje
[pierwotny protokół](PSI-MEMORY-M4-01.md). Dodano polskie brzmienie zadania
wspólne wszystkim wejściom. Polecenie wyszukiwawcze C zawiera wyłącznie
oba brzmienia zadania, bez wzorca odpowiedzi i ręcznych premii dla źródeł.

| Warunek | Wejście | Rola |
|---|---|---|
| A | Pełne pliki z zamrożonego `m4-broad-manifest.txt` | Historyczny punkt odniesienia M4 |
| B | Pełne pliki z zamrożonego `m4-guided-manifest.txt` | Dotychczasowy wybór kierowany pamięcią |
| C | Fragmenty korpusu A wybrane przez BM25 | Prosty konkurencyjny wybór źródeł |

B zawiera także istniejący indeks relacji, którego wytworzenie i utrzymanie
ma koszt. Źródłowy korpus C jest ten sam co w A. C nie dostaje indeksu grafowego,
gold rubric, raportów wyników ani ręcznej listy źródeł poprawnej odpowiedzi.
To jawny mały wzorzec leksykalny, nie najlepszy możliwy system wyszukiwania.

Kontrakt maszynowy: `m4-evaluation-contract.json`. Źródła wszystkich warunków
są pobierane z commitu `772bd92eb67f314bf99402462e9ec69392abcb5f`, niezależnie
od zmian w katalogu roboczym. C dzieli pliki na kolejne bloki po 80 wierszy,
stosuje BM25 z `k1=1.2`, `b=0.75`, a następnie dobiera całe fragmenty do limitu
równego rozmiarowi serializowanego kontekstu B. Limit obejmuje UTF-8 oraz
lokalizatory i skróty fragmentów. Parametrów nie dostraja się po obejrzeniu
wyników modelu; ich zmiana wymaga nowego oznaczenia warunku.

Limit bajtów kontroluje przygotowanie wejścia. Nie jest przybliżeniem liczby
tokenów. A jest szerszym punktem odniesienia; bezpośrednie porównanie wyboru
materiału przy ograniczeniu wejścia dotyczy B i C.

## Odtwarzalne wejścia

```bash
python scripts/prepare_memory_evaluation.py --out /tmp/psi-m4-evaluation
```

Katalog wyjściowy musi być nowy. Powstają `A.txt`, `B.txt`, `C.txt` i
`manifest.json` z przypięciem źródeł oraz skrótami kontraktu, wykonawcy
i dokładnych wejść. Bez `--out` polecenie wypisuje tylko pomiar przygotowania.
Potrzebna jest historia Git zawierająca wskazany commit; CI pobiera ją jawnie.

Pomiar przygotowania z 2026-09-30:

| Warunek | Kontekst UTF-8 [bajty] | Pełne wejście [bajty] | Liczba reprezentowanych plików |
|---|---:|---:|---:|
| A | 205062 | 206337 | 16 |
| B | 40553 | 41828 | 7 |
| C | 40532 | 41807 | 10 |

C wybrało 19 fragmentów z 10 plików. Obecność pliku nie jest potwierdzeniem
kompletności przesłanek ani poprawności przyszłej odpowiedzi. Nie dostrajano
wyszukiwania do uzyskanej listy. Wynik przygotowania: INPUTS_READY;
wynik porównania modeli: NOT_RUN.

Wykonawca modelu dostaje tylko jedno wejście, bez dostępu do repozytorium,
pozostałych odpowiedzi, kryteriów oceny ani historii tej rozmowy. W trzech
przebiegach muszą zgadzać się model, ustawienia i limit 650 słów odpowiedzi.
Wszystkie trzy pełne wejścia muszą mieścić się w oknie wybranego modelu;
ukryte obcięcie kontekstu unieważnia porównanie.
Ocena odpowiedzi następuje z ukrytym oznaczeniem wariantu; przypisanie A/B/C
ujawnia się po zakończeniu oceny. Wyników nie wolno wytwarzać przez udawanie
trzech niezależnych modeli w jednym kontekście.

## Wielkości mierzone i warunek wniosku

Osobno zapisuje się:

1. Punkty 0–7 według istniejącego wzorca oraz każde twierdzenie bez podstawy.
2. Trafność lokalizatorów, zachowanie G1 jako luki oraz granic minimalności.
3. Rzeczywiste tokeny wejściowe i wyjściowe, czas oraz odczyty, jeżeli wykonawca
   je udostępnia. Brak pomiaru ma wartość `UNKNOWN`, nigdy zero.
4. Koszt przygotowania, kontroli i utrzymania pamięci, oddzielnie od pojedynczego
   odczytu. Historyczny koszt budowy nie został zmierzony.

Korzyść B w tej próbie wymaga co najmniej zachowania jakości względem C,
braku wzrostu liczby nieuprawnionych twierdzeń oraz zmierzonej oszczędności
w jawnie wybranej wielkości kosztowej. Sam mniejszy pakiet tego nie ustanawia.
Wynik mieszany pozostaje wielokryterialny; nie wprowadza się wag po pomiarze.

Zadanie Go G4 było używane przy budowie pamięci. Nawet korzystny wynik A/B/C
jest kalibracją, nie dowodem generalizacji. Przed twierdzeniem o przewadze
potrzebny będzie zamrożony, niezależny zestaw zadań niewykorzystanych do budowy
mapy, z aktualizacjami, konfliktami, brakiem odpowiedzi i powtarzanymi próbami.
Nie wytworzono tutaj pozornie niezależnego zbioru przez przemianowanie znanych przykładów.

## Status i STOP

Trzy wejścia są przygotowywane bez usług płatnych. Niezależne przebiegi modeli
pozostają NOT_RUN; nie wybrano w tej jednostce wykonawcy spełniającego ograniczenie
zerowego kosztu. Przygotowanie wejść i regresje nie usuwają tego ograniczenia.

Jednostka korekty kończy się po przygotowaniu, weryfikacji i zapisaniu wejść
odtwarzalnych z kodu. Domyślny następny krok: wykonać ten sam kontrakt w trzech
niezależnych kontekstach po uzyskaniu właściwego wykonawcy. Nie otwierać M20
ani kolejnego obszaru zastosowań wyłącznie dlatego, że przygotowanie przeszło.
