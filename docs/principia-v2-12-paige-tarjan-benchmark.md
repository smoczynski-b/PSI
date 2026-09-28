# PRINCIPIA SEMANTICA — TOM II
## II.12. Paige–Tarjan jako algorytmiczny benchmark rafinacji partycji

**Status:** `CLASSICAL ALGORITHM / PSI BENCHMARK / PROSE PASS 01 / LOCAL CROSS-CHECK PASS AFTER COMPLEXITY SCOPE NORMALIZATION`  
**Źródło nadrzędne PSI:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, zachowane C14  
**Mapa porównawcza:** `classical-compare-01.md`  
**Źródło klasyczne:** R. Paige, R. E. Tarjan, “Three Partition Refinement Algorithms”, *SIAM Journal on Computing* 16(6), 1987, 973–989, DOI `10.1137/0216062`.  
**Zakres:** skończona przestrzeń stanów, jawna relacja binarna, jawna partycja początkowa, problem najgrubszej stabilnej rafinacji; brak twierdzenia o uniwersalnym algorytmie dla dowolnego kontraktu PSI.

---

## 1. Relational coarsest partition

Niech \(S\) będzie skończonym zbiorem, \(R\subseteq S\times S\) relacją, a \(\Pi_0\) partycją początkową. Dla \(C\subseteq S\):

\[
\operatorname{Pre}_R(C)=\{x\in S:\exists y\in C,\ xRy\}.
\]

Partycja \(\Pi\) jest **\(R\)-stabilna**, gdy dla każdych bloków \(B,C\in\Pi\)

\[
\boxed{
B\subseteq\operatorname{Pre}_R(C)
\quad\text{albo}\quad
B\cap\operatorname{Pre}_R(C)=\varnothing.
}
\]

Równoważnie: \(\operatorname{Pre}_R(C)\) jest sumą bloków \(\Pi\) dla każdego bloku \(C\).

Klasyczny problem ma postać:

\[
\boxed{
\Pi_*=	ext{najgrubsza }R\text{-stabilna rafinacja }\Pi_0.
}
\]

Jeżeli \(\Pi_1\preceq\Pi_2\) oznacza, że \(\Pi_1\) jest drobniejsza od \(\Pi_2\), to:

\[
\Pi_*\preceq\Pi_0,
\]

\(\Pi_*\) jest stabilna, a każda stabilna \(\Pi\preceq\Pi_0\) spełnia

\[
\Pi\preceq\Pi_*.
\]

---

## 2. Splittery

Jeżeli dla bloków \(B,C\) zachodzi

\[
B\cap\operatorname{Pre}_R(C)\neq\varnothing
\]

oraz

\[
B\setminus\operatorname{Pre}_R(C)\neq\varnothing,
\]

to \(C\) rozdziela \(B\). Krok rafinacji zastępuje \(B\) blokami

\[
B\cap\operatorname{Pre}_R(C),
\qquad
B\setminus\operatorname{Pre}_R(C).
\]

Sama idea kolejnych rozdzieleń jest elementarna. Wkład algorytmiczny Paige’a–Tarjana polega na organizacji splitterów i struktur danych tak, aby obliczyć najgrubszą stabilną rafinację efektywnie.

---

## 3. Klasyczna złożoność — rygiel modelu kosztowego

Niech

\[
n=|S|,
\qquad
m=|R|.
\]

Literatura klasyczna i późniejsze zastosowania standardowo podają dla relational coarsest partition granicę

\[
\boxed{O(m\log n)}
\]

oraz pamięć

\[
O(n+m).
\]

Ten zapis należy czytać w standardowym modelu analizy właściwej rafinacji na jawnie przygotowanej strukturze danych. Jeżeli w całkowity koszt wliczamy jawne odczytanie/utworzenie zbioru \(n\) stanów, relacji i partycji początkowej, bezpieczne księgowanie Principiów ma postać

\[
\boxed{O(n+m\log n)}
\]

jako „liniowa inicjalizacja + klasyczna rafinacja”. Nie jest to zmiana twierdzenia Paige’a–Tarjana, lecz jawne rozdzielenie modelu kosztowego od skrótu literaturowego.

W szczególności \(O(m\log n)\) nie jest ogólną złożonością „obliczania PSI”.

---

## 4. Most PSI — brama PT1–PT4

Niech skończony kontrakt PSI ma \(\Omega_c=S\). Paige–Tarjan jest legalnym wykonawcą zadaniowego ilorazu dopiero po redukcji do klasycznego typu wejścia:

### PT1 — skończoność

\[
|S|<\infty.
\]

### PT2 — partycja początkowa

Istnieje \(\Pi_0\), która dokładnie koduje bazowe rozróżnienia wymagane przez zadanie.

### PT3 — relacja

Istnieje jawna relacja

\[
R\subseteq S\times S
\]

kodująca przyszłą stabilność istotną dla zadania.

### PT4 — zgodność celu

Zadaniowa relacja równoważności jest dokładnie relacją indukowaną przez najgrubszą \(R\)-stabilną rafinację:

\[
\boxed{
E_{\mathcal T,c}=E_{\Pi_*}.
}
\]

Dopiero wtedy klasyczny algorytm oblicza bloki \(S/E_{\mathcal T,c}\).

---

## 5. Zasada II.12.A — warunkowa stosowalność

Jeżeli PT1–PT4 zachodzą, algorytm rozwiązujący relational coarsest partition dla \((S,R,\Pi_0)\) oblicza partycję klas

\[
S/E_{\mathcal T,c}.
\]

**Dowód.** Z PT4 zadaniowa relacja jest relacją indukowaną przez klasyczny cel \(\Pi_*\). Paige–Tarjan oblicza \(\Pi_*\), więc jego bloki są dokładnie klasami \(E_{\mathcal T,c}\). \(\square\)

Treść PSI leży w bramie PT1–PT4. Algorytm pozostaje klasyczny.

---

## 6. Semantyka ≠ cel ilorazowy ≠ algorytm

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

Paige–Tarjan nie rozstrzyga za kontrakt PSI:

- co jest obserwablą;
- jaka rodzina przyszłych testów jest wymagana;
- czy dynamika ma postać jednej relacji binarnej;
- czy potrzebna jest rodzina relacji, prawdopodobieństwa, historia, wyższa struktura lub przestrzeń ciągła;
- czy zadaniowy iloraz jest właśnie najgrubszą stabilną rafinacją \(\Pi_0\).

Dlatego

\[
\boxed{
\text{correct quotient target}
\neq
\text{choice of quotient algorithm}.
}
\]

---

## 7. Granica uniwersalizacji

### Przypadek statyczny

Jeżeli zadanie rozróżnia skończone stany wyłącznie przez

\[
R_{task}:S\to\{0,1\},
\]

to

\[
E_{\mathcal T}=\ker_{eq}R_{task}
\]

jest bezpośrednio znane. Nie ma potrzeby importowania relacyjnej stabilności ani Paige’a–Tarjana.

### Przypadek probabilistyczny

W II.10 ważne są masy

\[
P(x,C).
\]

Sama relacja egzystencjalna

\[
x\in\operatorname{Pre}_R(C)
\]

nie zachowuje prawdopodobieństw. Dwa stany mogą mieć krawędzie do tych samych bloków, a różne masy przejścia.

Zatem

\[
\boxed{
\text{finite PSI instance}
\not\Rightarrow
\text{Paige–Tarjan applicable without a reduction proof}.
}
\]

---

## 8. Relacja do II.10 i II.11

### II.10 — lumpowalność Markowa

Warunek

\[
P(x,C)=P(y,C)
\]

jest liczbowy. Relacyjna stabilność egzystencjalna nie jest automatycznie testem silnej lumpowalności ważonego jądra Markowa.

### II.11 — Myhill–Nerode

Minimalność Nerode’a wynika z pełnego kontraktu kontynuacji. Paige–Tarjan jest algorytmem rafinacji relacyjnej, nie samym twierdzeniem Myhilla–Nerode’a ani nazwą każdego algorytmu minimalizacji DFA.

---

## 9. Bisymulacja — most warunkowy

W odpowiednio otypowanych skończonych systemach przejść relational coarsest partition wiąże się klasycznie z obliczaniem stabilnych/bisymulacyjnych klas.

Nie wynika stąd:

\[
\boxed{
\text{Paige–Tarjan computes a stable partition}
\not\Rightarrow
\text{every PSI task equivalence is a bisimulation}.
}
\]

Równoważność PSI może być grubsza, drobniejsza albo innego typu zależnie od zadania i kontraktu.

---

## 10. Granice złożoności

Ani klasyczne \(O(m\log n)\), ani konserwatywne pełne księgowanie \(O(n+m\log n)\) nie obejmuje automatycznie:

- skonstruowania semantyki zadania;
- sprawdzenia PT4;
- rodzin relacji bez uwzględnienia ich kodowania;
- jąder probabilistycznych;
- przestrzeni nieskończonych;
- danych wyższego rzędu;
- kosztu identyfikacji z obserwacji.

Złożoność algorytmu rozpoczyna się po legalnym sprowadzeniu problemu do jego typu wejścia.

---

## 11. Status źródłowy

C14 pozostaje

`CLASSICAL / BENCHMARK`.

PSI nie rości nowości dla problemu, algorytmu ani jego złożoności. Rola benchmarku brzmi:

\[
\boxed{
\text{what quotient is justified?}
\neq
\text{how an eligible finite quotient is computed?}
}
\]

---

## 12. Lokalny cross-check

- **Typy:** `PASS` — skończony zbiór, relacja, partycja i porządek rafinacji jawne.
- **Źródło:** `PASS` — Paige–Tarjan 1987 obejmuje relational coarsest partition.
- **Stabilność:** `PASS` — zgodna ze standardową definicją przez \(R^{-1}(C)\).
- **Złożoność:** `PASS AFTER SCOPE NORMALIZATION` — literatura: \(O(m\log n)\), pamięć \(O(n+m)\); Principia jawnie oddzielają liniową inicjalizację wejścia.
- **PSI bridge:** `PASS` — wymagany dowód PT1–PT4.
- **Boundary:** `PASS` — sama skończoność nie wystarcza.
- **Originality:** `PASS` — brak klasycznej inflacji do PSI.
- **Agent impact:** `PASS` — brak Freeze 01 erraty, CORE5 zmiany i Agent v03.

---

## 13. Werdykt II.12

\[
\boxed{
\mathrm{II.12\ PAIGE\!\!-\!TARJAN\ BENCHMARK}
=\mathrm{PASS}.
}
\]

Klasyczna warstwa II.10–II.12 jest lokalnie kompletna. Następny krok: **whole-layer cross-check klasycznych mostów przed CAT/FACT/FRAME/HIGHER**.
