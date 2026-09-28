# PRINCIPIA SEMANTICA — TOM II
## II.12. Paige–Tarjan jako algorytmiczny benchmark rafinacji partycji

**Status:** `CLASSICAL ALGORITHM / PSI BENCHMARK / PROSE PASS 01 / LOCAL CROSS-CHECK PASS`  
**Źródło nadrzędne PSI:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, zachowane C14  
**Mapa porównawcza:** `classical-compare-01.md`  
**Źródło klasyczne:** R. Paige, R. E. Tarjan, “Three Partition Refinement Algorithms”, *SIAM Journal on Computing* 16(6), 1987, 973–989, DOI `10.1137/0216062`.  
**Zakres:** skończona przestrzeń stanów, jedna jawna relacja binarna, jawna partycja początkowa, problem najgrubszej stabilnej rafinacji; brak twierdzenia o uniwersalnym algorytmie dla dowolnego kontraktu PSI.

---

## 1. Problem klasyczny — relational coarsest partition

Niech

\[
S
\]

będzie skończonym zbiorem stanów,

\[
R\subseteq S\times S
\]

relacją przejścia oraz

\[
\Pi_0
\]

partycją początkową zbioru \(S\).

Dla \(C\subseteq S\) definiujemy poprzednik relacyjny

\[
\operatorname{Pre}_R(C)
=
\{x\in S:\exists y\in C,\ xRy\}.
\]

Partycję \(\Pi\) nazywamy **stabilną względem \(R\)**, jeżeli dla każdych bloków \(B,C\in\Pi\)

\[
\boxed{
B\subseteq\operatorname{Pre}_R(C)
\quad\text{albo}\quad
B\cap\operatorname{Pre}_R(C)=\varnothing.
}
\]

Równoważnie, dla każdego bloku \(C\), zbiór \(\operatorname{Pre}_R(C)\) jest sumą bloków \(\Pi\).

Problem *relational coarsest partition* ma postać:

> znaleźć najgrubszą partycję \(\Pi_*\), która rafinuje \(\Pi_0\) i jest stabilna względem \(R\).

To jest cel matematyczny problemu. Algorytm Paige’a–Tarjana jest sposobem jego efektywnego obliczenia.

---

## 2. Porządek rafinacji

Dla partycji \(\Pi_1,\Pi_2\) piszemy

\[
\Pi_1\preceq\Pi_2
\]

gdy \(\Pi_1\) jest drobniejsza od \(\Pi_2\), tj. każdy blok \(\Pi_1\) zawiera się w pewnym bloku \(\Pi_2\).

Szukany wynik spełnia:

1. \(\Pi_*\preceq\Pi_0\);
2. \(\Pi_*\) jest \(R\)-stabilna;
3. jeżeli \(\Pi\preceq\Pi_0\) jest \(R\)-stabilna, to
   \[
   \Pi\preceq\Pi_*.
   \]

Zatem \(\Pi_*\) jest **najgrubszą dopuszczalną stabilną rafinacją** partycji początkowej.

---

## 3. Rafinacja przez splitter

Jeżeli dla bloków \(B,C\) zachodzi jednocześnie

\[
B\cap\operatorname{Pre}_R(C)\neq\varnothing
\]

i
\[
B\setminus\operatorname{Pre}_R(C)\neq\varnothing,
\]

to \(C\) rozdziela \(B\). Naturalny krok rafinacji zastępuje \(B\) dwoma niepustymi blokami

\[
B\cap\operatorname{Pre}_R(C),
\qquad
B\setminus\operatorname{Pre}_R(C).
\]

Powtarzanie legalnych rozdzieleń prowadzi do partycji stabilnej. Istotą algorytmiki Paige’a–Tarjana nie jest samo istnienie takiej iteracji, lecz organizacja splitterów i struktur danych tak, aby nie płacić kosztu naiwnej wielokrotnej rafinacji.

---

## 4. Klasyczny wynik algorytmiczny

Dla

\[
n=|S|,
\qquad
m=|R|,
\]

relational coarsest partition może być obliczona w czasie

\[
\boxed{O(m\log n)}
\]

w klasycznym modelu jawnej reprezentacji relacji.

Wynik ten należy do klasycznej algorytmiki rafinacji partycji. PSI nie rości autorstwa ani problemu, ani algorytmu, ani granicy złożoności.

Granica \(O(m\log n)\) jest przywoływana wyłącznie dla problemu o powyższym typie wejścia. Nie jest ogólną złożonością „obliczania PSI”.

---

## 5. Most PSI — kiedy Paige–Tarjan jest legalnym wykonawcą

Niech dany będzie skończony kontrakt PSI z przestrzenią kandydatów

\[
\Omega_c=S.
\]

Paige–Tarjan może być użyty do wyznaczania zadaniowej partycji tylko wtedy, gdy jawnie skonstruujemy redukcję problemu PSI do relational coarsest partition:

### PT1 — skończoność

\[
|S|<\infty.
\]

### PT2 — partycja początkowa

Istnieje partycja \(\Pi_0\), która dokładnie koduje rozróżnienia bazowe wymagane przez zadanie, np. bieżące etykiety/obserwable.

### PT3 — relacja przejścia

Istnieje jawna relacja binarna

\[
R\subseteq S\times S
\]

odpowiadająca tym przyszłym testom, dla których wymagana jest stabilność.

### PT4 — zgodność celu

Zadaniowa relacja równoważności ma być dokładnie relacją indukowaną przez najgrubszą \(R\)-stabilną rafinację \(\Pi_0\):

\[
\boxed{
E_{\mathcal T,c}=E_{\Pi_*}.
}
\]

Dopiero po wykazaniu PT1–PT4 algorytm Paige’a–Tarjana oblicza właściwy iloraz zadaniowy dla tego kontraktu.

---

## 6. Twierdzenie/zasada II.12.A — warunkowa stosowalność

Jeżeli skończony kontrakt PSI spełnia PT1–PT4, to algorytm rozwiązujący klasyczny relational coarsest partition dla \((S,R,\Pi_0)\) oblicza partycję klas

\[
S/E_{\mathcal T,c}.
\]

### Dowód

Z PT4 zadaniowa relacja równoważności jest z definicji relacją indukowaną przez klasyczny cel \(\Pi_*\). Algorytm Paige’a–Tarjana oblicza \(\Pi_*\). Zatem jego bloki są dokładnie klasami \(E_{\mathcal T,c}\). \(\square\)

Treść PSI jest tu całkowicie w **bramie redukcji PT1–PT4**. Sam algorytm pozostaje klasyczny.

---

## 7. Matematyczny cel ≠ algorytm

Należy zachować trzy poziomy:

\[
\boxed{
\text{task semantics}
\to
\text{target equivalence/partition}
\to
\text{algorithm computing it}.
}
\]

PSI definiuje, które rozróżnienia są zadaniowo istotne. To nie wybiera automatycznie algorytmu.

Paige–Tarjan przyjmuje już określony problem skończonej stabilnej rafinacji. Nie decyduje za kontrakt PSI:

- co jest obserwablą;
- jaka jest rodzina przyszłych testów;
- czy relacja przejścia ma właściwy typ;
- czy potrzebna jest jedna relacja, rodzina relacji, prawdopodobieństwa, historia, wyższe dane lub struktura ciągła;
- czy docelowy iloraz rzeczywiście jest najgrubszą stabilną rafinacją \(\Pi_0\).

Dlatego:

\[
\boxed{
\text{correct quotient target}
\neq
\text{choice of quotient algorithm}.
}
\]

---

## 8. Minimalny kontrprzykład do uniwersalizacji Paige–Tarjan

Weźmy skończony problem bez dynamiki, w którym zadanie rozróżnia stany wyłącznie przez jawny odczyt

\[
R_{task}:S\to\{0,1\}.
\]

Wtedy

\[
E_{\mathcal T}=\ker_{eq}R_{task}
\]

jest już bezpośrednio znane jako partycja poziomicowa odczytu. Nie istnieje żadna potrzeba importowania relacyjnej stabilności ani algorytmu Paige’a–Tarjana.

Jeszcze mocniej: dla problemu stochastycznego z istotnymi wartościami prawdopodobieństw sam warunek egzystencjalny

\[
x\in\operatorname{Pre}_R(C)
\]

nie zachowuje mas przejścia wymaganych przez II.10. Dwa stany mogą mieć przejścia do tych samych bloków, ale z różnymi prawdopodobieństwami.

Zatem:

\[
\boxed{
\text{finite PSI instance}
\not\Rightarrow
\text{Paige–Tarjan applicable without a reduction proof}.
}
\]

---

## 9. Relacja do II.10 i II.11

### II.10 — Markowowska lumpowalność

II.10 wymaga równości mas przejścia

\[
P(x,C)=P(y,C),
\]

nie tylko zgodności istnienia krawędzi do bloku. Klasyczny relational coarsest partition na zwykłej relacji binarnej nie jest więc automatycznie algorytmem silnej lumpowalności dla ważonego jądra Markowa.

### II.11 — Myhill–Nerode

Dla automatów deterministycznych istnieją wyspecjalizowane algorytmy minimalizacji, a klasyczna minimalność Nerode’a wynika z kontraktu wszystkich kontynuacji. Paige–Tarjan jest szerszym narzędziem rafinacji relacyjnej, ale nie należy utożsamiać go z samym twierdzeniem Myhilla–Nerode’a ani z każdym algorytmem minimalizacji DFA.

---

## 10. Bisymulacja — poprawny, lecz warunkowy most

W skończonych systemach przejść partycyjna rafinacja Paige’a–Tarjana stanowi klasyczny fundament efektywnego wyznaczania bisymulacyjnych/stabilnych klas w odpowiednio otypowanych strukturach.

Nie wolno jednak odwracać tego związku:

\[
\boxed{
\text{Paige–Tarjan computes a coarsest stable partition}
\not\Rightarrow
\text{every PSI task equivalence is a bisimulation}.
}
\]

Równoważność PSI może być:

- grubsza od bisymulacji, jeśli zadanie ignoruje część zachowania;
- drobniejsza, jeśli zawiera dodatkowe obserwable;
- innego typu, jeśli kandydaci nie tworzą skończonego relacyjnego systemu przejść.

---

## 11. Granice złożoności

Klasyczne

\[
O(m\log n)
\]

dotyczy relational coarsest partition w jego jawnie skończonym modelu wejścia.

Nie wynika z niego:

- \(O(m\log n)\) dla dowolnego problemu PSI;
- taki sam koszt dla rodzin relacji bez uwzględnienia kodowania;
- taki sam koszt dla jąder probabilistycznych;
- taki sam koszt dla nieskończonych przestrzeni;
- koszt skonstruowania samego kontraktu, obserwabli lub partycji początkowej;
- koszt sprawdzenia PT4;
- koszt wyznaczenia zadaniowej semantyki z danych.

Złożoność algorytmu klasycznego zaczyna się **po legalnej redukcji problemu do jego typu wejścia**.

---

## 12. Status źródłowy

Paige–Tarjan jest klasycznym algorytmem. C14 ma status

`CLASSICAL / BENCHMARK`.

W PSI nie jest to nowe twierdzenie o identyfikowalności, lecz test poprawnej separacji:

\[
\boxed{
\text{what quotient is justified?}
\neq
\text{how an eligible finite quotient is computed?}
}
\]

To rozdzielenie jest zasadnicze dla całego projektu.

---

## 13. Lokalny cross-check

### Typy
`PASS`: skończony zbiór, relacja binarna, partycja początkowa i porządek rafinacji są jawne.

### Źródło
`PASS`: Paige–Tarjan 1987 obejmuje relational coarsest partition; bibliografia i DOI związane.

### Złożoność
`PASS WITH SCOPE LOCK`: \(O(m\log n)\) tylko dla klasycznego relational coarsest partition w jawnej reprezentacji.

### PSI bridge
`PASS`: stosowalność wymaga jawnego dowodu PT1–PT4.

### Boundary
`PASS`: skończoność samego problemu PSI nie wystarcza; przypadki statyczne i probabilistyczne pokazują brak uniwersalności.

### Originality
`PASS`: brak przypisania algorytmu lub klasycznego problemu PSI.

### Agent impact
`PASS`: brak Freeze 01 erraty, brak CORE5 zmiany, brak Agent v03.

---

## 14. Werdykt II.12

\[
\boxed{
\mathrm{II.12\ PAIGE\!\!-\!TARJAN\ BENCHMARK}
=\mathrm{PASS}.
}
\]

Klasyczna warstwa mostów II.10–II.12 jest lokalnie kompletna. Następny legalny krok: **cross-check całej warstwy klasycznych mostów przed przejściem do CAT/FACT/FRAME/HIGHER**.
