# PRINCIPIA SEMANTICA — TOM I
## I.2. Obserwacja, włókno zgodności i adekwatność katalogu

**Status:** `NORMALIZED PASS 01 / WHOLE-V1 N1 APPLIED`  
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

nie są elementem przestrzeni kandydatów ani z definicji wartością ukrytego stanu. Są rekordem, wobec którego sprawdzamy zgodność wyniku obserwatora. Pierwszym krokiem nie jest więc wybór jednego \(x\in\Omega_c\), lecz wyznaczenie wszystkich kandydatów, których kontrakt nie wyklucza.

\[
\boxed{
Y\longrightarrow\text{zbiór kandydatów zgodnych z }Y.
}
\]

Dopiero później wolno pytać, czy zadanie redukuje ten zbiór do jednej klasy zadaniowej.

---

## 2. Przekrój relacji zgodności

Dla ustalonych danych \(Y\) definiujemy

\[
\boxed{
\mathcal K_c^Y
=
\{b\in\mathcal B_c:(b,Y)\in\mathcal K_c\}.
}
\]

W modelu dokładnym może zachodzić

\[
(b,Y)\in\mathcal K_c\iff b=Y,
\]

ale nie jest to definicja ogólna. Kontrakt może dopuszczać tolerancję, cenzurowanie, agregację, wielowartościowy zapis danych albo inną jawnie otypowaną regułę zgodności.

Rozdzielenie

\[
\Psi_c\quad\text{oraz}\quad\mathcal K_c
\]

jest zasadnicze: \(\Psi_c\) określa, co model wystawia na kanał obserwacyjny, a \(\mathcal K_c\) — co kontrakt uznaje za zgodne z faktycznymi danymi.

---

## 3. Włókno zgodności

### Definicja I.2.1 — włókno zgodności

\[
\boxed{
F_c(Y)=\Psi_c^{-1}(\mathcal K_c^Y)
}
\]

czyli

\[
F_c(Y)=\{x\in\Omega_c:\Psi_c(x)\in\mathcal K_c^Y\}.
\]

Włókno \(F_c(Y)\) jest pełnym zbiorem kandydatów dopuszczonych przez kontrakt i zgodnych z danymi. Nie jest estymatorem punktowym, wybranym modelem ani „najbardziej prawdopodobnym” stanem, dopóki kontrakt nie zawiera probabilistycznej reguły takiego wyboru.

---

## 4. Trzy elementarne sytuacje

### 4.1. Włókno puste

\[
F_c(Y)=\varnothing.
\]

Oznacza to, że bieżąca kombinacja

\[
(\Omega_c,\Psi_c,\mathcal K_c,Y)
\]

nie posiada zgodnego kandydata. Nie lokalizuje to jeszcze przyczyny. Defekt może leżeć w katalogu, obserwacji, relacji zgodności, danych albo w ich wzajemnym niedopasowaniu.

### 4.2. Włókno jednoelementowe

\[
F_c(Y)=\{x\}.
\]

Wtedy dane i kontrakt rozstrzygają kandydata na poziomie \(\Omega_c\). Jest to przypadek silniejszy niż zwykle potrzebuje zadanie.

### 4.3. Włókno wieloelementowe

\[
|F_c(Y)|>1.
\]

Sam ten fakt nie oznacza nierozstrzygalności zadania. Kandydaci mogą różnić się tylko w cechach nieistotnych dla \(\mathcal T\). Dopiero I.3 wprowadzi relację zadaniową, która rozstrzyga, czy różnice pozostałe we włóknie mają znaczenie.

---

## 5. Klasa przed reprezentantem

Wybór

\[
\widehat x\in F_c(Y)
\]

jest dodatkową operacją. Może wymagać dodatkowego pomiaru, priora, funkcji kosztu, regularizacji, reguły optymalizacyjnej, konwencji reprezentacyjnej albo nowego twierdzenia.

Dlatego:

\[
\boxed{
\text{najpierw włókno, potem ewentualny wybór reprezentanta}.
}
\]

Regularizator może wskazać reprezentanta, ale sam fakt jego użycia nie dowodzi, że dane odróżniały go od pozostałych elementów włókna.

---

## 6. Adekwatność katalogu poprzedza identyfikowalność

PSI rozdziela:

1. **adekwatność katalogu** — czy bieżąca klasa kandydatów jest zdolna zawierać realizacje zgodne z problemem;
2. **identyfikowalność w katalogu** — które dopuszczone realizacje pozostają nierozróżnione dla danych i zadania.

Nie wolno używać drugiego pytania do naprawiania pierwszego.

Kanoniczna kolejność pracy brzmi:

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
\text{PROJEKTOWANIE / REDESIGN PROTOKOŁU}.
}
\]

### Normalizacja N1 — protokół początkowy i protokół kolejny

Powyższej sekwencji nie wolno czytać tak, jakby przed zbudowaniem włókna nie istniał żaden protokół. Włókno i obserwacja są już określone względem pewnego początkowego kontraktu/protokołu \(P_0\). Ostatnia strzałka oznacza projektowanie **kolejnej iteracji** protokołu na podstawie diagnozy uzyskanej dla \(P_0\):

\[
\boxed{
P_0
\to
\text{adekwatność / włókno / diagnoza ID}
\to
P_1.
}
\]

\(P_1\) może dodawać obserwację, interwencję, zmieniać tolerancję albo inaczej uszczegóławiać eksperyment. Jest to redesign lub refinacja protokołu, nie jego pierwsze pojawienie się.

---

## 7. Adekwatność katalogu nie jest jednym uniwersalnym skalarem

Bieżący kanon nie ustanawia jednego uniwersalnego

\[
D_{\rm ADEQ}^{cat}
\]

jako prymitywu CORE. Sposób badania adekwatności zależy od kontraktu.

Puste włókno jest świadkiem niespójności całego pakietu, ale staje się testem samego katalogu dopiero wtedy, gdy protokół zamraża pozostałe składniki i jawnie ustanawia katalog jako testowany element.

W kontrakcie metrycznym można użyć adaptera, np.

\[
D_{\rm ADEQ}^{cat}(Q;P,Y)
=
\inf_{b\in\widetilde{\mathcal B}^{P}_{Q}}
 d_{\mathcal Y}(\operatorname{Obs}_{P}(b),Y),
\]

z warunkiem

\[
D_{\rm ADEQ}^{cat}(Q;P,Y)\le\varepsilon,
\]

ale dopiero po jawnej specyfikacji przestrzeni zachowań, mapy obserwacji, metryki/straty i tolerancji. To adapter protokołu, nie definicja rdzenia PSI.

---

## 8. Nieadekwatność katalogu nie identyfikuje jego poprawki

Należy rozdzielić

\[
\boxed{\text{„bieżący katalog nie wystarcza”}}
\]

od

\[
\boxed{\text{„wiemy, jaka zmiana katalogu jest uzasadniona”}}.
\]

Drugie pytanie należy do PSI-CAT. Warunki dziedzinowe mogą eliminować niedopuszczalne propozycje zmiany katalogu, lecz nie stają się przez to nową obserwacją empiryczną.

---

## 9. Lokalna i globalna identyfikowalność — zapowiedź

Badanie lokalne może dotyczyć podzbioru

\[
U\subseteq\Omega_c
\]

i włókna \(F_c(Y)\cap U\), natomiast badanie globalne — całego \(F_c(Y)\). Lokalnego kryterium rangi, Hessianu, informacji Fishera ani innego testu nie wolno przenosić na globalną jednoznaczność bez dodatkowego twierdzenia.

W I.3 dopiero skonstruujemy

\[
\mathscr R_{\mathcal T,c},
\qquad
E_{\mathcal T,c},
\qquad
M_{\mathcal T,c},
\]

co nada dokładny sens pytaniu o rozstrzygalność względem zadania.

---

## 10. Konsekwencje metodologiczne

- Dane i kandydaci są różnymi typami.
- \(\Psi_c^{-1}(A)\) oznacza przeciwobraz zbioru, nie funkcjonalną odwrotność obserwatora.
- \(F_c(Y)=\varnothing\) nie lokalizuje przyczyny defektu.
- \(|F_c(Y)|>1\) nie przesądza nierozstrzygalności zadania.
- Przejście \(F_c(Y)\to\widehat x\) wymaga osobnej licencji.

---

## 11. Przejście do I.3

Po I.1 i I.2 znamy typowaną przestrzeń kandydatów, obserwację, zgodność, dane i pełne włókno. Następne pytanie brzmi:

\[
\boxed{
\text{czy wszystkie elementy }F_c(Y)
\text{ dają ten sam wynik dla zadania?}
}
\]

Odpowiedź wymaga relacji równoważności zadaniowej i jest przedmiotem I.3.

---

## Status redakcyjny I.2

Normalizacja `WHOLE-V1 N1` doprecyzowała relację pomiędzy protokołem początkowym i późniejszym redesignem. Nie zmieniła C11/C64 ani Freeze 01.

\[
\boxed{
\mathrm{I.2}=\mathrm{NORMALIZED\ PASS\ 01}.
}
\]
