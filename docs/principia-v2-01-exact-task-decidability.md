# PRINCIPIA SEMANTICA — TOM II
## II.1. Dokładna rozstrzygalność zadaniowa

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PENDING`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, C06 zachowane przez Freeze 01  
**Mapa twierdzeń:** `principia-v2-theorem-map-01.md`, T2.1  
**Zakres:** dokładna semantyka zbiorowa; bez stabilności, probabilistyki i obliczalności.

---

## 1. Typy i dane wejściowe

Niech

\[
\Omega
\]

będzie zbiorem kandydatów, a

\[
E\subseteq\Omega\times\Omega
\]

relacją równoważności. Niech

\[
q:\Omega\to\Omega/E
\]

będzie projekcją ilorazową.

Niech ponadto

\[
F\subseteq\Omega
\]

będzie dowolnym zbiorem kandydatów zgodnych z ustalonymi danymi.

W zastosowaniu PSI przyjmujemy

\[
E=E_{\mathcal T,c},
\qquad
q=q_{\mathcal T,c},
\qquad
F=F_c(Y).
\]

Przypominamy:

\[
F_c(Y)=\Psi_c^{-1}(\mathcal K_c^Y),
\]

oraz

\[
E_{\mathcal T,c}
=
\bigcap_{R\in\mathscr R_{\mathcal T,c}}
\ker_{\rm eq}R.
\]

Ponieważ przecięcie relacji równoważności jest relacją równoważności, iloraz

\[
M_{\mathcal T,c}=\Omega_c/E_{\mathcal T,c}
\]

jest dobrze określony.

---

## 2. Co znaczy dokładne rozstrzygnięcie zadania

Dane rozstrzygają zadanie dokładnie wtedy, gdy wszystkie kandydaty pozostające zgodne z obserwacją należą do jednej i tej samej klasy zadaniowej.

Nie wymagamy zatem

\[
|F_c(Y)|=1.
\]

Wymagamy jedynie

\[
\boxed{
|q_{\mathcal T,c}(F_c(Y))|=1.
}
\]

Jest to rozstrzygnięcie na poziomie zadania, a nie pełnego kandydata.

Warunek ten musi jednak jawnie wykluczać puste włókno. Obraz zbioru pustego jest pusty, więc

\[
|q(\varnothing)|=0,
\]

a nie \(1\).

---

## 3. Twierdzenie II.1 — dokładna rozstrzygalność zadaniowa

### Twierdzenie

Dla dowolnego zbioru \(\Omega\), relacji równoważności \(E\) na \(\Omega\), projekcji

\[
q:\Omega\to\Omega/E
\]

i dowolnego podzbioru \(F\subseteq\Omega\) zachodzi

\[
\boxed{
|q(F)|=1
\iff
F\neq\varnothing
\land
F\times F\subseteq E.
}
\]

Równoważnie, w notacji PSI:

\[
\boxed{
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)\times F_c(Y)
\subseteq
E_{\mathcal T,c}.
}
\]

Zapis

\[
F^2
\]

jeśli jest używany skrótowo, oznacza wyłącznie iloczyn kartezjański

\[
F\times F,
\]

nie potęgę, kompozycję ani inny obiekt.

---

## 4. Dowód

### Kierunek \(\Rightarrow\)

Załóżmy, że

\[
|q(F)|=1.
\]

W szczególności obraz \(q(F)\) jest niepusty, a więc

\[
F\neq\varnothing.
\]

Niech teraz

\[
x,y\in F.
\]

Ponieważ \(q(F)\) zawiera dokładnie jeden element, mamy

\[
q(x)=q(y).
\]

Dla projekcji ilorazowej zachodzi

\[
q(x)=q(y)
\iff
xEy.
\]

Stąd

\[
(x,y)\in E.
\]

Ponieważ \(x,y\in F\) były dowolne,

\[
F\times F\subseteq E.
\]

Otrzymaliśmy więc

\[
F\neq\varnothing
\land
F\times F\subseteq E.
\]

### Kierunek \(\Leftarrow\)

Załóżmy teraz, że

\[
F\neq\varnothing
\]

oraz

\[
F\times F\subseteq E.
\]

Wybierzmy dowolny

\[
x_0\in F.
\]

Dla każdego \(x\in F\) mamy

\[
(x,x_0)\in F\times F\subseteq E,
\]

a zatem

\[
q(x)=q(x_0).
\]

Wszystkie elementy \(F\) mają więc ten sam obraz pod \(q\). Ponieważ \(F\neq\varnothing\), obraz ten zawiera dokładnie jedną klasę:

\[
|q(F)|=1.
\]

To kończy dowód. \(\square\)

---

## 5. Interpretacja PSI

Twierdzenie rozdziela trzy różne pytania.

### 5.1. Czy istnieje kandydat zgodny z danymi?

\[
F_c(Y)\neq\varnothing.
\]

Jest to warunek istnienia zgodnej realizacji w bieżącym kontrakcie. Nie identyfikuje jeszcze przyczyny ewentualnego pustego włókna.

### 5.2. Czy wszyscy zgodni kandydaci są zadaniowo równoważni?

\[
F_c(Y)\times F_c(Y)
\subseteq
E_{\mathcal T,c}.
\]

Jest to warunek braku zadaniowo istotnej różnicy wewnątrz włókna.

### 5.3. Czy zadanie ma dokładnie jedną odpowiedź klasową?

\[
|q_{\mathcal T,c}(F_c(Y))|=1.
\]

Twierdzenie II.1 mówi, że w dokładnym reżimie zbiorowym pytanie trzecie jest równoważne koniunkcji dwóch pierwszych.

---

## 6. Czego twierdzenie nie wymaga

Twierdzenie nie wymaga, aby

\[
|F_c(Y)|=1.
\]

Może zachodzić

\[
|F_c(Y)|>1
\]

przy jednoczesnym

\[
|q_{\mathcal T,c}(F_c(Y))|=1,
\]

jeżeli wszystkie różnice pomiędzy zgodnymi kandydatami są nieistotne dla zadania.

To jest dokładnie powód, dla którego PSI rozróżnia identyfikację pełnego kandydata od rozstrzygalności zadaniowej.

---

## 7. Przypadki brzegowe i falsyfikatory

### B1 — puste włókno

Jeżeli

\[
F=\varnothing,
\]

to

\[
q(F)=\varnothing
\]

i

\[
|q(F)|=0.
\]

Dlatego warunku

\[
F\neq\varnothing
\]

nie wolno usuwać z prawej strony twierdzenia.

### B2 — dwa różne kandydaty, jedna klasa zadaniowa

Jeżeli

\[
x\neq y,
\qquad
xEy,
\]

i

\[
F=\{x,y\},
\]

to

\[
|F|=2,
\qquad
|q(F)|=1.
\]

Pełny kandydat nie jest zidentyfikowany, ale zadanie jest rozstrzygnięte.

### B3 — dwa kandydaty w różnych klasach

Jeżeli

\[
x\not E y
\]

i oba należą do \(F\), to

\[
|q(F)|\ge2.
\]

Jedna para zadaniowo nierównoważnych kandydatów we włóknie wystarcza do obalenia dokładnej rozstrzygalności.

---

## 8. Status źródłowy

Twierdzenie II.1 jest elementarnym faktem teorii zbiorów i ilorazów. Jego dowód został podany samodzielnie powyżej.

Status:

\[
\boxed{
\text{CLASSICAL ELEMENTARY QUOTIENT FACT / PSI-ADAPTED CENTRAL CRITERION}.
}
\]

PSI nie rości sobie pierwszeństwa do samego faktu ilorazowego. Wkład architektury PSI polega na jego osadzeniu w typowanym łańcuchu

\[
Y
\to
F_c(Y)
\to
E_{\mathcal T,c}
\to
q_{\mathcal T,c}(F_c(Y)),
\]

czyli na rozdzieleniu zgodności danych od rozróżnień wymaganych przez zadanie.

Dla ważności twierdzenia nie jest potrzebne dodatkowe źródło zewnętrzne.

---

## 9. Wiązanie z regresjami

Twierdzenie II.1 nie wymaga osobnego benchmarku z `Regression Bank 01`.

Jego obowiązkowym testem lokalnym jest przypadek pustego włókna B1. Każda przyszła redakcja, która usuwa

\[
F\neq\varnothing,
\]

albo utożsamia pusty obraz z jednoelementowym, łamie twierdzenie.

HCube (R01) i Go (R02) testują przede wszystkim adekwatność reprezentacji z późniejszego T2.4. FS-STAT (R03) testuje jeszcze dalszą granicę:

\[
\text{dokładna rozstrzygalność}
\not\Rightarrow
\text{stabilność / licencja statystyczna}.
\]

Nie należy więc przypisywać R01–R03 jako dowodu Twierdzenia II.1.

---

## 10. Zakres twierdzenia

Twierdzenie II.1 jest twierdzeniem **dokładnym i zbiorowym**.

Nie ustanawia:

- stabilności względem perturbacji danych;
- ciągłości mapy rozwiązania;
- odporności numerycznej;
- prawdopodobieństwa poprawnego rozstrzygnięcia;
- przedziału ufności;
- obliczalności włókna lub ilorazu;
- skończoności przestrzeni klas;
- procedury wyboru reprezentanta klasy;
- adekwatności samego katalogu.

Każde z tych pytań wymaga dodatkowych założeń lub osobnego twierdzenia.

---

## 11. Przejście do II.2

Twierdzenie II.1 mówi, kiedy **dany zbiór kandydatów** mieści się w jednej klasie zadaniowej.

Następne pytanie dotyczy reprezentacji:

> kiedy wielkość \(R\) albo iloraz zadaniowy można obliczać wyłącznie z reprezentacji \(\rho(x)\), bez utraty informacji?

Odpowiedzią będzie elementarne kryterium faktoryzacji:

\[
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,
\qquad
R=g\circ\rho.
\]

To jest przedmiot II.2.
