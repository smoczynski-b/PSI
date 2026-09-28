# PRINCIPIA SEMANTICA — TOM I
## I.2. Obserwacja, włókno zgodności i adekwatność katalogu

**Status:** `PROSE PASS 01 / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`  
**Zakres:** C02, C11, C64; bez twierdzenia o rozstrzygalności zadaniowej z Tomu II.

---

## 1. Obserwacja nie wybiera obiektu

Po ustaleniu kontraktu dysponujemy przestrzenią kandydatów

\[
\Omega_c,
\]

kanałem obserwacji

\[
\Psi_c:\Omega_c\to\mathcal B_c
\]

oraz relacją zgodności

\[
\mathcal K_c\subseteq\mathcal B_c\times\mathcal Y_c.
\]

Dane

\[
Y\in\mathcal Y_c
\]

nie są elementem przestrzeni kandydatów. Nie są też z definicji wartością ukrytego stanu. Są rekordem, wobec którego sprawdzamy zgodność przewidywanego wyniku obserwatora.

Pierwszym krokiem po otrzymaniu danych nie jest więc wybór jednego \(x\in\Omega_c\), lecz wyznaczenie **wszystkich** kandydatów, których kontrakt nie wyklucza.

To odwraca częsty, lecz nielegalny schemat:

\[
Y
\longrightarrow
\widehat x
\]

na schemat

\[
\boxed{
Y
\longrightarrow
\text{zbiór kandydatów zgodnych z }Y.
}
\]

Dopiero później wolno pytać, czy zadanie pozwala ten zbiór zredukować do jednej klasy istotnej dla celu wnioskowania.

---

## 2. Przekrój relacji zgodności

Dla ustalonych danych \(Y\) definiujemy przekrój relacji zgodności

\[
\boxed{
\mathcal K_c^Y
=
\{b\in\mathcal B_c:(b,Y)\in\mathcal K_c\}.
}
\]

Jest to zbiór wyników obserwatora uznanych przez kontrakt za zgodne z rekordem \(Y\).

W najprostszym modelu dokładnym relacja może być diagonalą:

\[
(b,Y)\in\mathcal K_c
\iff
b=Y.
\]

Wtedy

\[
\mathcal K_c^Y=\{Y\}.
\]

Nie jest to jednak definicja ogólna. Kontrakt może dopuszczać tolerancję, przedział niepewności, wielowartościowy zapis danych, cenzurowanie, agregację albo inną jawnie otypowaną regułę zgodności. Wtedy \(\mathcal K_c^Y\) może zawierać więcej niż jeden element przestrzeni obserwacyjnej.

Rozdzielenie

\[
\Psi_c
\quad\text{oraz}\quad
\mathcal K_c
\]

ma więc znaczenie zasadnicze. Pierwszy obiekt mówi, **co model wystawia na kanał obserwacyjny**. Drugi mówi, **co kontrakt uznaje za zgodne z faktycznymi danymi**.

Zmiana \(\mathcal K_c\) bez zmiany \(\Psi_c\) nadal jest zmianą problemu wnioskowania.

---

## 3. Włókno zgodności

### Definicja I.2.1 — włókno zgodności

Dla danych \(Y\in\mathcal Y_c\) definiujemy

\[
\boxed{
F_c(Y)
=
\Psi_c^{-1}(\mathcal K_c^Y).
}
\]

Równoważnie,

\[
F_c(Y)
=
\{x\in\Omega_c:\Psi_c(x)\in\mathcal K_c^Y\}.
\]

Włókno \(F_c(Y)\) jest pełnym zbiorem kandydatów dopuszczonych przez kontrakt, których obserwacja jest zgodna z danymi.

Nie jest to estymator punktowy. Nie jest to wybrany model. Nie jest to „najbardziej prawdopodobny” stan, dopóki kontrakt nie zawiera struktury probabilistycznej i reguły takiego wyboru.

Włókno jest tym, co pozostaje po zastosowaniu **wyłącznie informacji zawartej w kontrakcie obserwacyjnym i danych**.

---

## 4. Trzy elementarne sytuacje

Już na poziomie włókna pojawiają się trzy logicznie odmienne przypadki.

### 4.1. Włókno puste

\[
F_c(Y)=\varnothing.
\]

Oznacza to, że żaden kandydat dopuszczony przez bieżący kontrakt nie jest zgodny z danymi.

Nie wolno z tego automatycznie wnosić, że dane są „błędne”, ani że istnieje określony brakujący mechanizm. Puste włókno mówi jedynie, że bieżąca kombinacja

\[
\Omega_c,
\Psi_c,
\mathcal K_c,
Y
\]

nie posiada zgodnego kandydata.

Przyczyna może leżeć w katalogu, w modelu obserwacji, w kryterium zgodności, w danych albo w ich wzajemnym niedopasowaniu. Rozstrzygnięcie przyczyny wymaga dodatkowego testu.

### 4.2. Włókno jednoelementowe

\[
F_c(Y)=\{x\}.
\]

Wtedy dane i kontrakt rozstrzygają kandydata na poziomie przestrzeni \(\Omega_c\).

Jest to przypadek silny. PSI nie przyjmuje go jako domyślnego celu, ponieważ dla wielu zadań nie trzeba identyfikować całego kandydata. Wystarczy ustalić te jego własności, które mają znaczenie dla zadania. Formalizacja tej słabszej, zadaniowej jednoznaczności pojawi się po zdefiniowaniu równoważności zadaniowej.

### 4.3. Włókno wieloelementowe

\[
|F_c(Y)|>1.
\]

Jest to zwykły przypadek ograniczonej obserwacji. Sam fakt istnienia wielu kandydatów nie oznacza jeszcze porażki wnioskowania.

Możliwe są dwie sytuacje:

1. kandydaci różnią się tylko w cechach nieistotnych dla zadania;
2. co najmniej dwaj kandydaci różnią się w wyniku potrzebnym do wykonania zadania.

Dopiero rozróżnienie tych przypadków prowadzi do właściwego pojęcia identyfikowalności zadaniowej. Nie wolno więc przechodzić od

\[
|F_c(Y)|>1
\]

do zdania „problem jest nierozstrzygalny” bez określenia zadania.

---

## 5. Klasa przed reprezentantem

Włókno należy traktować jako obiekt pierwszoplanowy. Wybór jednego elementu

\[
\widehat x\in F_c(Y)
\]

jest dodatkową operacją.

Może wynikać z:

- dodatkowego pomiaru;
- priora;
- funkcji kosztu;
- regularizacji;
- reguły optymalizacyjnej;
- konwencji reprezentacyjnej;
- interwencji eksperymentalnej;
- dodatkowego twierdzenia o równoważności kandydatów dla zadania.

Każdy taki mechanizm zmienia podstawę wniosku i powinien zostać jawnie nazwany.

W szczególności regularizator może wskazać stabilnego reprezentanta, ale sam wybór regularizacyjny nie dowodzi, że dane rozróżniały go od innych elementów włókna.

Dlatego obowiązuje dyscyplina:

\[
\boxed{
\text{najpierw włókno, potem ewentualny wybór reprezentanta}.
}
\]

---

## 6. Adekwatność katalogu poprzedza identyfikowalność

Definicja włókna zakłada, że przestrzeń kandydatów \(\Omega_c\) jest katalogiem, względem którego pytanie w ogóle ma sens. To założenie nie może być ukryte.

PSI rozdziela dwa problemy:

1. **adekwatność katalogu** — czy bieżący katalog zawiera realizacje zdolne wyjaśnić dane w ramach kontraktu;
2. **identyfikowalność w katalogu** — które z dopuszczonych realizacji pozostają nierozróżnione po obserwacji i dla danego zadania.

Nie wolno używać drugiego pytania do naprawiania pierwszego.

Jeżeli katalog jest nieadekwatny, doskonalenie procedury wyboru wewnątrz tego katalogu nie odzyska brakującej klasy realizacji.

Z tego powodu kolejność pracy jest zamrożona jako

\[
\boxed{
\text{ADEKWATNOŚĆ KATALOGU}
\to
\text{WŁÓKNO}
\to
\text{IDENTYFIKOWALNOŚĆ LOKALNA}
\to
\text{IDENTYFIKOWALNOŚĆ GLOBALNA}
\to
\text{PROJEKTOWANIE PROTOKOŁU}.
}
\]

Kolejność ta jest metodologicznym rygorem PSI. Nie jest twierdzeniem, że dla każdego problemu istnieje jeden uniwersalny test adekwatności katalogu.

---

## 7. Adekwatność katalogu nie jest jednym uniwersalnym skalarem

Bieżący kanon wymaga, aby pytanie o adekwatność katalogu zostało postawione **przed** identyfikowalnością. Nie ustanawia jednak jednego uniwersalnego funkcjonału

\[
D_{\rm ADEQ}^{cat}
\]

jako szóstego składnika rdzenia albo obowiązującej definicji dla wszystkich dziedzin.

Sposób testowania adekwatności zależy od kontraktu.

Puste włókno

\[
F_c(Y)=\varnothing
\]

jest jednoznacznym świadkiem, że **cały bieżący pakiet** katalog–obserwacja–zgodność–dane nie posiada rozwiązania. Nie lokalizuje jednak przyczyny w samym katalogu. Może pełnić rolę falsyfikatora katalogu dopiero w protokole, który zamraża pozostałe składniki i jawnie ustanawia katalog jako testowany element.

W problemach przybliżonych kontrakt może posługiwać się metryką, pseudometryką, funkcją straty, testem zgodności albo inną dziedzinowo legalną procedurą.

### Przykład adaptera metrycznego — nie definicja rdzenia

Jeżeli protokół \(P\) wyznacza rodzinę zachowań manifestowanych przez katalog \(Q\), oznaczoną

\[
\widetilde{\mathcal B}^{P}_{Q},
\]

a przestrzeń danych posiada jawną metrykę lub pseudometrykę \(d_{\mathcal Y}\), można zdefiniować adapter

\[
D_{\rm ADEQ}^{cat}(Q;P,Y)
=
\inf_{b\in\widetilde{\mathcal B}^{P}_{Q}}
 d_{\mathcal Y}(\operatorname{Obs}_{P}(b),Y).
\]

Następnie, dla tolerancji \(\varepsilon\), można przyjąć kontraktowe kryterium

\[
D_{\rm ADEQ}^{cat}(Q;P,Y)\le\varepsilon.
\]

Taki zapis jest legalny tylko po określeniu co najmniej:

- dziedziny zachowań;
- mapy \(\operatorname{Obs}_P\);
- metryki lub straty;
- tolerancji \(\varepsilon\);
- sposobu traktowania zmiennych uciążliwych i domknięć, jeśli występują.

Adapter ten jest przykładem realizacji pytania o adekwatność katalogu. Nie jest uniwersalną definicją PSI.

---

## 8. Nieadekwatność katalogu nie mówi jeszcze, jak katalog zmienić

Stwierdzenie, że bieżący katalog jest niewystarczający, nie wyznacza automatycznie nowego katalogu.

Należy rozdzielić:

\[
\boxed{
\text{„bieżący katalog nie wystarcza”}
}
\]

od

\[
\boxed{
\text{„wiemy, jaka zmiana katalogu jest uzasadniona”}.
}
\]

Pierwsze może wynikać z odpowiedniego testu niezgodności bieżącego katalogu przy zamrożonych pozostałych składnikach kontraktu. Drugie jest osobnym problemem identyfikacji zmiany katalogu, rozwijanym później jako PSI-CAT.

Warunki dziedzinowe mogą eliminować część propozycji zmiany katalogu, lecz nie stają się przez to nową obserwacją empiryczną.

Dlatego przy pustym włóknie lub przy osobno wykazanej nieadekwatności katalogu obowiązuje rygiel:

\[
\boxed{
\text{brak zgodnego kandydata}
\not\Rightarrow
\text{jednoznacznie zidentyfikowana nowa realizacja}.
}
\]

---

## 9. Lokalna i globalna identyfikowalność — tylko zapowiedź

Po ustaleniu katalogu i włókna można pytać o identyfikowalność.

Na poziomie lokalnym badanie może dotyczyć ograniczonego podzbioru

\[
U\subseteq\Omega_c
\]

i włókna

\[
F_c(Y)\cap U.
\]

Na poziomie globalnym rozpatruje się całe \(F_c(Y)\).

Nie wolno przenosić lokalnego kryterium rangi, Hessianu, informacji Fishera ani innego lokalnego testu na globalną jednoznaczność bez dodatkowego twierdzenia.

W Tomie I nie definiujemy jeszcze pełnego kryterium identyfikowalności zadaniowej. Najpierw w I.3 skonstruujemy rodzinę domkniętych wielkości zadaniowych, równoważność \(E_{\mathcal T,c}\) oraz iloraz \(M_{\mathcal T,c}\). Dopiero wtedy pytanie

\[
\text{„czy dane wystarczają?”}
\]

otrzyma dokładny sens względem zadania.

---

## 10. Konsekwencje metodologiczne

Z definicji włókna i pierwszeństwa adekwatności katalogu wynikają następujące zasady pracy.

### 10.1. Dane nie są kandydatem

\[
Y\notin\Omega_c
\]

w ogólności. Dane i kandydaci należą do odrębnych typów.

### 10.2. Obserwacja nie jest odwrotnością

Nie zakładamy istnienia mapy

\[
\Psi_c^{-1}:\mathcal B_c\to\Omega_c
\]

jako funkcji. Zapis

\[
\Psi_c^{-1}(A)
\]

oznacza przeciwobraz zbioru \(A\subseteq\mathcal B_c\), nie funkcjonalne odwrócenie obserwatora.

### 10.3. Puste włókno nie identyfikuje przyczyny błędu

\[
F_c(Y)=\varnothing
\]

jest świadkiem braku zgodności w bieżącym kontrakcie, lecz nie diagnozą źródła niezgodności.

### 10.4. Wieloelementowe włókno nie przesądza nierozstrzygalności zadania

\[
|F_c(Y)|>1
\]

nie wystarcza do wniosku o braku rozstrzygnięcia zadaniowego.

### 10.5. Reprezentant wymaga prawa wyboru

Każde przejście

\[
F_c(Y)
\longrightarrow
\widehat x
\]

musi wskazać dodatkową regułę, informację albo twierdzenie, które je licencjonuje.

---

## 11. Punkt wyjścia do równoważności zadaniowej

Po I.1 i I.2 znamy już:

1. typowaną przestrzeń kandydatów \(\Omega_c\);
2. kanał obserwacji \(\Psi_c\);
3. relację zgodności \(\mathcal K_c\);
4. dane \(Y\);
5. pełne włókno kandydatów zgodnych z danymi \(F_c(Y)\).

Nie wiemy jeszcze, które różnice pomiędzy elementami włókna naprawdę mają znaczenie dla zadania.

To jest następne pytanie PSI.

Nie brzmi ono:

\[
\text{„czy w }F_c(Y)\text{ pozostał dokładnie jeden obiekt?”}
\]

lecz:

\[
\boxed{
\text{„czy wszystkie obiekty pozostające w }F_c(Y)
\text{ dają ten sam wynik dla zadania?”}
}
\]

Aby odpowiedzieć, potrzebujemy formalnej relacji równoważności zadaniowej. Jej konstrukcja jest przedmiotem I.3.
