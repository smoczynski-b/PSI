# Te same dane — różne reprezentacje

Status: FINITE / CONTRACT-RELATIVE. Data: 2026-09-30.
Korekta przedmiotu doświadczenia z rozmowy 04.

## Dane i zadanie

Stały zbiór D tworzą trzy zapisane relacje wychodzące z II.9:

| Cel | Zapisany typ relacji |
|---|---|
| II.7 | DEPENDS_ON |
| II.6 | ANALOGY_TO |
| II.8 | NOT_DEPENDS_ON |

Źródło tabeli: `psi-memory-edges-01.tsv` z przypiętego commitu
`772bd92eb67f314bf99402462e9ec69392abcb5f`. Jest to świadek wierności
reprezentacji zapisanym danym; nie nowy audyt dowodów tych twierdzeń.

Zadanie q przypisuje każdemu rekordowi jego dokładny typ relacji. Dla
reprezentacji rho:D→Z sprawdza się skończony warunek II.4:

\[
\ker_{\rm eq}\rho\subseteq\ker_{\rm eq}q.
\]

Świadek nieadekwatności to para rekordów o tej samej reprezentacji i różnym
typie relacji. Liczy się takie pary; dodatkowo sprawdza się wynik zapytania
o przesłankę dowodową II.9.

## Zmienne reprezentacje

Tabela i typowany graf zachowują całe rekordy. Dwa rysunki tego samego grafu
różnią się wyłącznie współrzędnymi. Pełny odczyt rysunku obejmuje identyfikatory,
typy, kierunki i źródła krawędzi, więc powinien odtworzyć D i tę samą odpowiedź.

Kontrola ujemna celowo zapisuje **wyłącznie** przynależność końca krawędzi do
kuli o promieniu 1.5 wokół II.9. Nie przypisuje się tego uproszczenia użytkownikowi.
Jest to jawny przykład stratnego odczytu obrazu, który filtr PSI ma odrzucić.

- ALL_NEAR: wszystkie trzy cele leżą w kuli — oczekiwane trzy kolidujące pary.
- PROOF_FAR: II.7 leży poza kulą, a II.6 i II.8 wewnątrz — oczekiwana jedna
  kolidująca para; utożsamienie bliskości z przesłanką pomija II.7 i dodaje dwa
  nieuprawnione cele.

Dane, ich źródło i q pozostają stałe. Zmienia się przedstawienie i jawnie
wybrany odczyt z przedstawienia. Nie dodaje się fotografii ani nowych danych.

```bash
python scripts/test_memory_representation.py
```

Wykonanie z 2026-09-30 potwierdziło obie pełne rekonstrukcje D. Kontrole
ujemne dały odpowiednio 3 i 1 parę utraconych rozróżnień. W obu układach
przypisanie bliskości znaczenia przesłanki dodało II.6 i II.8; w PROOF_FAR
dodatkowo pominęło II.7. Skrót SHA-256 stałego wybranego zbioru D:
`6118ee5aca8119b05aa3d3e9b3af7788562b202e649f3dd1262d4b480839f299`.

## Granica wniosku

Przejście kontroli oznacza wykrycie zadeklarowanej utraty informacji oraz
zachowanie treści w dwóch pełnych przedstawieniach. Nie dowodzi, że obraz
polepsza pamięć modelu, że model poprawnie go odczyta, ani że graf przewyższa
tekst. Ten wpływ wymaga osobnego pomiaru wykonania tego samego zadania przy
tych samych danych. Zmiana reprezentacji może pomagać dostrzec relację, lecz
sama zgodność odległości lub klastrów nie poświadcza jej prawdziwości.

## Uściślenie użytkownika: geometria wynikająca z procesu

Chemia była przykładem wiedzy o fizycznych ograniczeniach, możliwej do
przekazywania przez wzory i relacje przy niewielkim udziale języka naturalnego.
Pozwala to badać geometryczne przedstawienie procesów i połączeń. Powyższa
kontrola ujemna dotyczy wyłącznie arbitralnej bliskości rysunku; nie jest
kontrprzykładem do geometrii wynikającej z zadeklarowanego modelu fizycznego.

Przykład klasyczny, poza nowymi prymitywami PSI: ustalamy skończony katalog
n substancji i m skierowanych reakcji oraz model zamkniętego, jednorodnego
układu o stałej objętości i temperaturze. Niech \(x\in\mathbb R^n_{\ge0}\)
oznacza ilości substancji [mol], \(S\in\mathbb Z^{n\times m}\) bezwymiarową
macierz stechiometryczną, a v(x;c) szybkości postępu reakcji [mol/s]. Kontrakt
c określa warunki i kinetykę zachowującą nieujemność; rozpatrujemy przedział,
na którym istnieje rozwiązanie. Dla ustalonego x₀:

\[
\dot x=S\,v(x;c),\qquad
x(t)\in\mathcal C(x_0):=(x_0+\operatorname{im}S)\cap\mathbb R^n_{\ge0}.
\]

Uzasadnienie ograniczenia: x(t)−x₀=S∫₀ᵗv(x(s);c)ds należy do im S.
Kolumny S wyznaczają kierunki zmian składu, a C(x₀) zawiera trajektorię.
Nie wynika z tego osiągalność każdego punktu C(x₀). Kinetyka i warunki c
ograniczają ruch dodatkowo; sama stechiometria nie określa progów energetycznych.

Macierz składu pierwiastkowego \(A\in\mathbb N_0^{p\times n}\), dla p wybranych pierwiastków, daje
kontrolę bilansu AS=0, skąd Ax(t)=Ax₀. Bilans jest warunkiem koniecznym,
nie wystarcza do stwierdzenia fizycznej wykonalności reakcji.
To przykład ograniczenia, które można sprawdzać algebraicznie. Zapis formalny
nie wymaga parafrazy słownej przy każdym użyciu. Nie dowodzi to jeszcze przewagi
danego modelu AI w operowaniu takim zapisem.

Źródła klasycznej realizacji:
[Feinberg 1987, §§3 i 5.2](https://www.mit.edu/~jadbabai/ESE680/Fei87a.pdf),
[Helton, Klep, Katsnelson 2009](https://arxiv.org/abs/0904.2960).
Jest to uściślenie kierunku i zakresu, nie nowy eksperyment ani twierdzenie PSI.
