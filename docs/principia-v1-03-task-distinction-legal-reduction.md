# PRINCIPIA SEMANTICA — TOM I
## I.3. Rozróżnienie zadaniowe i legalna redukcja

**Status:** `FIRST PROSE PASS / FROM V1-V2 FREEZE 01`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`  
**Zakres:** C03–C05, C09, C32, C37, C60; dowody faktoryzacyjne pozostają w Tomie II.

---

## 1. Włókno nie jest jeszcze odpowiedzią na pytanie zadaniowe

Po I.2 dla danych \(Y\) dysponujemy włóknem zgodności

\[
F_c(Y)=\Psi_c^{-1}(\mathcal K_c^Y).
\]

Włókno mówi, które kandydaty pozostają zgodne z danymi. Nie mówi jeszcze, które różnice pomiędzy tymi kandydatami mają znaczenie dla zadania \(\mathcal T\).

To rozróżnienie jest centralne. Możliwe jest bowiem, że

\[
|F_c(Y)|>1,
\]

a mimo to wszystkie elementy włókna dają ten sam wynik w każdym aspekcie potrzebnym do wykonania zadania.

Dlatego PSI nie utożsamia

\[
\boxed{
\text{jednoznaczności całego kandydata}
}
\]

z

\[
\boxed{
\text{jednoznacznością wyniku zadaniowego}.
}
\]

Druga własność jest słabsza i często wystarcza.

---

## 2. Lokalna rodzina wielkości zadaniowych

Kontrakt zawiera rodzinę

\[
\mathscr O_{\mathcal T,c},
\]

której elementy są wielkościami uznanymi za istotne dla zadania.

Nie należy jednak zakładać, że ta początkowa lista wyczerpuje wszystkie rozróżnienia, które mogą stać się potrzebne po dopuszczalnych operacjach lub ewolucjach. Jeżeli zadanie wymaga przewidywania, transportu, aktualizacji albo złożenia wielkości, znaczenie zadaniowe może rozciągać się poza pierwotny zbiór lokalnych obserwabli.

Z tego powodu wprowadzamy domknięcie zadaniowe.

### Definicja I.3.1 — domknięcie zadaniowe

Niech

\[
\boxed{
\mathscr R_{\mathcal T,c}
=
\operatorname{Cl}^{\mathcal T}_{\delta_c}(\mathscr O_{\mathcal T,c})
}
\]

oznacza najmniejszą rodzinę wielkości zadaniowych, która:

1. zawiera \(\mathscr O_{\mathcal T,c}\);
2. jest domknięta względem operacji dopuszczonych przez zadanie i kontrakt;
3. zawiera wymagane przez zadanie transporty przez \(\delta_c\), jeżeli takie transporty są częścią kontraktu.

Symbol

\[
\operatorname{Cl}^{\mathcal T}_{\delta_c}
\]

nie oznacza dowolnego „domknięcia wszystkiego, co może być użyteczne”. Jego sens musi być określony przez kontrakt.

Jeżeli kontrakt nie dopuszcza określonej operacji, nie wolno wprowadzić jej do \(\mathscr R_{\mathcal T,c}\) tylko dlatego, że ułatwia rozstrzygnięcie.

W szczególności domknięcie zadaniowe nie jest ukrytym mechanizmem dodawania nowych danych.

---

## 3. Jądro równoważności pojedynczej wielkości

Dla mapy

\[
R:\Omega_c\to W_R
\]

definiujemy

### Definicja I.3.2 — jądro równoważności

\[
\boxed{
\ker_{\rm eq}R
=
\{(x,y)\in\Omega_c^2:R(x)=R(y)\}.
}
\]

Dwa kandydaty należą do \(\ker_{\rm eq}R\), jeżeli wielkość \(R\) ich nie rozróżnia.

Nie jest to jądro liniowe w sensie algebry liniowej. Notacja \(\ker_{\rm eq}\) podkreśla, że chodzi o relację równoważności wyznaczoną przez równość wartości mapy.

Dla każdej mapy \(R\) relacja \(\ker_{\rm eq}R\) jest relacją równoważności.

---

## 4. Równoważność zadaniowa

Kandydaci są nierozróżnialni dla zadania wtedy, gdy żadna wielkość z pełnego domknięcia zadaniowego nie wymaga ich rozróżnienia.

### Definicja I.3.3 — równoważność zadaniowa

\[
\boxed{
E_{\mathcal T,c}
=
\bigcap_{R\in\mathscr R_{\mathcal T,c}}
\ker_{\rm eq}R.
}
\]

Równoważnie,

\[
x\,E_{\mathcal T,c}\,y
\iff
R(x)=R(y)
\quad
\text{dla każdego }R\in\mathscr R_{\mathcal T,c}.
\]

Relacja \(E_{\mathcal T,c}\) nie mówi, że \(x\) i \(y\) są tym samym obiektem. Mówi tylko, że przy bieżącym kontrakcie i zadaniu nie istnieje zadaniowa podstawa, aby je rozróżniać.

Dlatego należy zachować rozdzielenie

\[
\boxed{
 x\neq y
\quad\text{może współistnieć z}\quad
x\,E_{\mathcal T,c}\,y.
}
\]

To jest dokładnie punkt, w którym PSI odchodzi od wymagania identyfikacji pełnego stanu.

---

## 5. Iloraz zadaniowy

Skoro \(E_{\mathcal T,c}\) jest relacją równoważności, możemy utworzyć przestrzeń klas zadaniowych.

### Definicja I.3.4 — iloraz zadaniowy

\[
\boxed{
M_{\mathcal T,c}
=
\Omega_c/E_{\mathcal T,c}.
}
\]

Niech

\[
q_{\mathcal T,c}:\Omega_c\to M_{\mathcal T,c}
\]

będzie projekcją ilorazową.

Element

\[
q_{\mathcal T,c}(x)=[x]_{\mathcal T,c}
\]

nie jest „pełnym stanem świata”. Jest klasą wszystkich kandydatów, które są nierozróżnialne względem pełnej semantyki zadania ustalonej przez kontrakt.

Z tego powodu iloraz zadaniowy może być znacznie grubszy niż identyfikacja ontologiczna lub realizacyjna.

Różnicę tę można zapisać schematycznie:

\[
\boxed{
\text{realizacja}
\longrightarrow
\text{klasa zadaniowa}
}
\]

bez prawa do odwrotnego wniosku, że jedna klasa zadaniowa odpowiada jednej realizacji.

---

## 6. Reprezentacja jako kompresja informacji

Niech

\[
\rho:\Omega_c\to Z
\]

będzie dowolną reprezentacją kandydatów.

Może to być zapis parametrów, wektor cech, pamięć stanu, klasa izomorfizmu, zestaw niezmienników, kompresja historii albo inny jawnie otypowany obiekt.

Każda reprezentacja dokonuje pewnych identyfikacji. Jeżeli

\[
\rho(x)=\rho(y),
\]

to reprezentacja przestaje odróżniać \(x\) od \(y\).

Pytanie PSI nie brzmi więc:

> Czy \(\rho\) zachowuje wszystkie informacje o \(x\)?

lecz:

> Czy \(\rho\) zachowuje wszystkie różnice potrzebne dla zadania?

### Zasada I.3.5 — dokładna adekwatność zadaniowa reprezentacji

Zamrożone kryterium ma postać

\[
\boxed{
\ker_{\rm eq}\rho
\subseteq
E_{\mathcal T,c}.
}
\]

Jeżeli reprezentacja utożsamia tylko kandydatów już równoważnych zadaniowo, nie traci żadnego rozróżnienia potrzebnego do zadania.

Jeżeli natomiast istnieją \(x,y\) takie, że

\[
\rho(x)=\rho(y)
\]

oraz

\[
(x,y)\notin E_{\mathcal T,c},
\]

to \(\rho\) jest zbyt gruba dla tego zadania.

Pełny dowód równoważności tego kryterium z faktoryzacją projekcji \(q_{\mathcal T,c}\) przez \(\rho\) znajduje się w Tomie II. W Tomie I używamy go jako zamrożonej zasady konstrukcyjnej.

---

## 7. Adekwatność jest względna wobec zadania

Ta sama reprezentacja może być wystarczająca dla jednego zadania i niewystarczająca dla innego.

Nie istnieje więc bezwarunkowe pojęcie „dobrej reprezentacji” niezależne od tego, co ma zostać zachowane.

Jeżeli

\[
\mathcal T_1
\]

wymaga mniejszej liczby rozróżnień niż

\[
\mathcal T_2,
\]

to możliwe jest, że

\[
\ker_{\rm eq}\rho
\subseteq
E_{\mathcal T_1,c}
\]

ale

\[
\ker_{\rm eq}\rho
\not\subseteq
E_{\mathcal T_2,c}.
\]

Dlatego zmiana zadania może zmienić status reprezentacji bez zmiany samej mapy \(\rho\).

W szczególności stwierdzenie

\[
\boxed{
\text{„ta reprezentacja jest wystarczająca”}
}
\]

bez podania zadania i kontraktu jest niepełne.

---

## 8. Redukcja, quotient i gauge

Niech

\[
q:\Omega_c\to Z
\]

będzie proponowaną redukcją: ilorazem, truncacją, kompresją, przejściem do klas orbit, redukcją pamięci albo inną mapą, która celowo usuwa rozróżnienia.

Dokładny test zachowania informacji zadaniowej ma tę samą postać:

\[
\boxed{
\ker_{\rm eq}q
\subseteq
E_{\mathcal T,c}.
}
\]

Jeżeli warunek ten nie zachodzi, redukcja skleja co najmniej jedną parę kandydatów, którą zadanie musi nadal rozróżniać.

Wtedy redukcja jest **zadaniowo nieadekwatna**.

### Ważne ograniczenie

Warunek

\[
\ker_{\rm eq}q\subseteq E_{\mathcal T,c}
\]

nie wyczerpuje pełnej legalności kontraktu.

Redukcja może zachowywać informację zadaniową, a mimo to być niedopuszczalna z innego powodu, na przykład dlatego, że:

- działanie nie jest zdefiniowane na właściwej dziedzinie;
- proponowany gauge nie jest ustanowiony przez kontrakt;
- obserwacja nie schodzi na quotient ani nie jest odpowiednio ekwiwariantna;
- naruszony zostaje twardy warunek dziedzinowy;
- zmienia się interfejs albo typ danych;
- redukcja wymaga informacji niedostępnej w deklarowanym protokole.

Dlatego obowiązuje rozdzielenie

\[
\boxed{
\text{zadaniowo adekwatna redukcja}
\neq
\text{w pełni legalna redukcja kontraktowa}
}
\]

w ogólności.

Pierwszy warunek jest dokładnym testem zachowania rozróżnień zadaniowych. Drugi obejmuje również pozostałe wymagania kontraktu.

---

## 9. Symetria nie daje automatycznie quotientu

W I.1 rozdzieliliśmy deklarację symetrii od prawa do redukcji. Teraz możemy sformułować część zadaniową tego prawa dokładnie.

Jeżeli działanie grupy \(G\) prowadzi do projekcji

\[
q_G:\Omega_c\to\Omega_c/G,
\]

to zadaniowa utrata informacji jest kontrolowana przez

\[
\boxed{
\ker_{\rm eq}q_G
\subseteq
E_{\mathcal T,c}.
}
\]

Jeżeli dwie realizacje należą do tej samej orbity, lecz zadanie wymaga ich rozróżnienia, coarse quotient przez \(G\) jest za gruby dla tego zadania.

Nawet spełnienie tej inkluzji nie zwalnia z warunków obserwacyjnych i dziedzinowych. W szczególności geometryczna symetria realizacji nie musi być gauge ustalonego problemu danych.

Zasada pozostaje więc dwustopniowa:

\[
\boxed{
\text{czy wolno utożsamić?}
\to
\text{czy wolno to utożsamienie zastosować w tym kontrakcie?}
}
\]

Pierwsze pytanie jest zadaniowe. Drugie jest pełnym pytaniem kontraktowym.

---

## 10. Klasa przed reprezentantem — wersja zadaniowa

I.2 wprowadził zasadę „najpierw włókno, potem reprezentant”. Po zdefiniowaniu \(E_{\mathcal T,c}\) możemy ją wzmocnić.

Jeżeli obserwacja nie wyznacza pojedynczego \(x\in\Omega_c\), ale wszystkie elementy włókna należą do tej samej klasy zadaniowej, wybór reprezentanta nie jest potrzebny do rozstrzygnięcia zadania.

Dlatego naturalnym celem nie jest zawsze

\[
|F_c(Y)|=1,
\]

lecz jednoznaczność obrazu włókna w ilorazie zadaniowym.

Dokładny warunek tej jednoznaczności zostanie sformułowany i udowodniony w Tomie II. W tym miejscu istotna jest sama zmiana poziomu pytania:

\[
\boxed{
\text{„który kandydat?”}
\quad\longrightarrow\quad
\text{„która klasa zadaniowa?”}.
}
\]

To jest podstawowy ruch redukcyjny PSI.

---

## 11. Trzy typowe błędy redukcji

### 11.1. Redukcja zbyt gruba

Istnieją \(x,y\) takie, że

\[
q(x)=q(y),
\qquad
(x,y)\notin E_{\mathcal T,c}.
\]

Redukcja usuwa rozróżnienie potrzebne zadaniu.

### 11.2. Redukcja matematycznie poprawna, ale kontraktowo nielegalna

Mapa \(q\) może spełniać warunek zadaniowy, ale nie być dopuszczona przez protokół, dziedzinę albo obserwację.

Jest to inna klasa błędu niż niewystarczalność reprezentacji.

### 11.3. Redukcja poprawna dla innego zadania

Mapa \(q\) może być adekwatna dla \(\mathcal T_1\), lecz nie dla \(\mathcal T_2\).

Przeniesienie wyniku bez jawnej zmiany zadania jest dryfem kontraktu.

---

## 12. Co zostało zdefiniowane, a co dopiero będzie dowiedzione

W tym rozdziale zdefiniowaliśmy:

\[
\mathscr R_{\mathcal T,c},
\qquad
\ker_{\rm eq}R,
\qquad
E_{\mathcal T,c},
\qquad
M_{\mathcal T,c}.
\]

Przyjęliśmy również jako zamrożoną zasadę adekwatności:

\[
\ker_{\rm eq}\rho\subseteq E_{\mathcal T,c}.
\]

W Tomie II zostaną jawnie udowodnione:

1. kryterium faktoryzacji przez reprezentację;
2. globalna wystarczalność obserwatora;
3. równoważność warunku adekwatności z faktoryzacją \(q_{\mathcal T,c}\) przez \(\rho\);
4. dokładne kryterium rozstrzygalności zadaniowej na włóknie;
5. warunek legalnego zejścia dynamiki na quotient.

Tom I zachowuje więc granicę:

\[
\boxed{
\text{definicja i sens}
\neq
\text{pełny dowód strukturalny}.
}
\]

---

## 13. Przejście do historii i pamięci

Dotychczas kandydatem był element \(x\in\Omega_c\). W zadaniach sekwencyjnych bieżący stan lub bieżące włókno może jednak nie zachowywać wszystkich różnic potrzebnych do przyszłych decyzji.

Wtedy naturalnym obiektem staje się historia

\[
H_t
\]

oraz pytanie, które różnice między historiami muszą zostać zapamiętane, aby zachować przyszłą semantykę zadania.

To będzie temat I.4.

Centralne kryterium pozostanie tego samego typu:

\[
\boxed{
\text{reprezentacja może zapominać tylko to, czego zadanie nie potrzebuje}.
}
\]
