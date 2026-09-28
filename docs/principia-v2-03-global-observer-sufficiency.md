# PRINCIPIA SEMANTICA — TOM II
## II.3. Globalna wystarczalność obserwatora

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PENDING`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, C08 zachowane przez Freeze 01  
**Mapa twierdzeń:** `principia-v2-theorem-map-01.md`, T2.3  
**Zależność:** bezpośrednia specjalizacja Twierdzenia II.2.

---

## 1. Typy

Niech

\[
\Psi_c:\Omega_c\to\mathcal B_c
\]

będzie dokładną deterministyczną mapą obserwacji w ustalonym kontrakcie \(c\).

Niech

\[
E_{\mathcal T,c}
\subseteq
\Omega_c\times\Omega_c
\]

będzie równoważnością zadaniową oraz

\[
q_{\mathcal T,c}:\Omega_c\to M_{\mathcal T,c}
=\Omega_c/E_{\mathcal T,c}
\]

projekcją na iloraz zadaniowy.

Definiujemy równoważność indukowaną przez obserwatora:

\[
\boxed{
E_{\Psi,c}
:=
\ker_{\rm eq}\Psi_c
=
\{(x,y)\in\Omega_c^2:\Psi_c(x)=\Psi_c(y)\}.
}
\]

Nie zakładamy, że \(\Psi_c\) jest surjektywna na całą przestrzeń \(\mathcal B_c\).

---

## 2. Sens globalnej wystarczalności

Obserwator jest globalnie wystarczający dla zadania \(\mathcal T\), jeżeli znajomość samej wartości

\[
\Psi_c(x)
\]

wystarcza do wyznaczenia klasy zadaniowej

\[
q_{\mathcal T,c}(x).
\]

Oznacza to istnienie mapy

\[
f:\operatorname{im}\Psi_c\to M_{\mathcal T,c}
\]

takiej, że

\[
q_{\mathcal T,c}=f\circ\Psi_c.
\]

Jest to własność całej mapy obserwacji na \(\Omega_c\), a nie własność pojedynczego rekordu \(Y\) ani pojedynczego włókna zgodności.

Dlatego należy rozróżnić:

\[
\boxed{
\text{globalna wystarczalność obserwatora}
\neq
\text{dokładna rozstrzygalność dla jednego }Y.
}
\]

Pierwsza jest twierdzeniem o wszystkich parach kandydatów w \(\Omega_c\). Druga jest twierdzeniem o jednym zbiorze \(F_c(Y)\).

---

## 3. Twierdzenie II.3 — globalna wystarczalność obserwatora

### Twierdzenie

Dla mapy obserwacji

\[
\Psi_c:\Omega_c\to\mathcal B_c
\]

i ilorazu zadaniowego

\[
q_{\mathcal T,c}:\Omega_c\to M_{\mathcal T,c}
\]

zachodzi równoważność

\[
\boxed{
E_{\Psi,c}
\subseteq
E_{\mathcal T,c}
\iff
\exists!\,f:\operatorname{im}\Psi_c\to M_{\mathcal T,c},
\qquad
q_{\mathcal T,c}=f\circ\Psi_c.
}
\]

Równoważnie:

\[
\boxed{
\ker_{\rm eq}\Psi_c
\subseteq
E_{\mathcal T,c}
\iff
q_{\mathcal T,c}
\text{ faktoryzuje przez }\Psi_c
\text{ na }\operatorname{im}\Psi_c.
}
\]

Unikalność mapy \(f\) obowiązuje wyłącznie na \(\operatorname{im}\Psi_c\).

---

## 4. Dowód

Stosujemy Twierdzenie II.2 do map

\[
\rho=\Psi_c
\]

oraz

\[
R=q_{\mathcal T,c}.
\]

Dla projekcji ilorazowej mamy

\[
\ker_{\rm eq}q_{\mathcal T,c}
=
E_{\mathcal T,c}.
\]

Twierdzenie II.2 daje więc

\[
\ker_{\rm eq}\Psi_c
\subseteq
\ker_{\rm eq}q_{\mathcal T,c}
\iff
\exists!\,f:\operatorname{im}\Psi_c\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=f\circ\Psi_c.
\]

Po podstawieniu

\[
\ker_{\rm eq}q_{\mathcal T,c}=E_{\mathcal T,c}
\]

otrzymujemy dokładnie

\[
E_{\Psi,c}
\subseteq
E_{\mathcal T,c}
\iff
\exists!\,f:\operatorname{im}\Psi_c\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=f\circ\Psi_c.
\]

To kończy dowód. \(\square\)

---

## 5. Interpretacja

Inkluzja

\[
E_{\Psi,c}\subseteq E_{\mathcal T,c}
\]

mówi:

> jeżeli obserwator nie rozróżnia dwóch kandydatów, zadanie również nie może wymagać ich rozróżnienia.

Inaczej:

\[
\Psi_c(x)=\Psi_c(y)
\Longrightarrow
xE_{\mathcal T,c}y.
\]

Wtedy obserwacja jest wystarczająco bogata, aby odtworzyć **klasę zadaniową**, choć niekoniecznie pełny kandydat.

Może więc zachodzić

\[
\Psi_c(x)=\Psi_c(y),
\qquad
x\neq y,
\]

bez utraty informacji potrzebnej zadaniu, jeżeli

\[
xE_{\mathcal T,c}y.
\]

Globalna wystarczalność nie wymaga injektywności obserwatora.

---

## 6. Lokalny falsyfikator

Jedna para

\[
x,y\in\Omega_c
\]

spełniająca

\[
\Psi_c(x)=\Psi_c(y)
\]

oraz

\[
(x,y)\notin E_{\mathcal T,c}
\]

wystarcza do obalenia globalnej wystarczalności obserwatora.

Wtedy

\[
(x,y)\in E_{\Psi,c}
\]

lecz

\[
(x,y)\notin E_{\mathcal T,c},
\]

a zatem

\[
E_{\Psi,c}\not\subseteq E_{\mathcal T,c}.
\]

Nie może więc istnieć mapa

\[
f:\operatorname{im}\Psi_c\to M_{\mathcal T,c}
\]

spełniająca

\[
q_{\mathcal T,c}=f\circ\Psi_c.
\]

Jest to najkrótszy możliwy świadek niewystarczalności obserwatora.

---

## 7. Globalna wystarczalność a pojedyncze włókno danych

Może się zdarzyć, że obserwator nie jest globalnie wystarczający, lecz konkretne dane \(Y\) mimo to rozstrzygają zadanie.

Globalna niewystarczalność oznacza istnienie co najmniej jednej pary

\[
\Psi_c(x)=\Psi_c(y),
\qquad
x\not E_{\mathcal T,c}y.
\]

Nie wynika z tego, że taka para leży w każdym włóknie zgodnym z każdym rekordem \(Y\).

Dlatego

\[
E_{\Psi,c}\not\subseteq E_{\mathcal T,c}
\]

nie implikuje

\[
|q_{\mathcal T,c}(F_c(Y))|>1
\]

dla każdego \(Y\).

Twierdzenie II.1 i Twierdzenie II.3 odpowiadają więc na różne pytania:

- II.1: czy **ten rekord danych** rozstrzyga zadanie?
- II.3: czy **sam obserwator jako reprezentacja** jest wystarczający dla zadania na całej przestrzeni kandydatów?

---

## 8. Obraz obserwatora, nie cała przestrzeń obserwacyjna

Tak jak w II.2, faktoryzacja daje unikalną mapę tylko na

\[
\operatorname{im}\Psi_c.
\]

Jeżeli

\[
\operatorname{im}\Psi_c
\subsetneq
\mathcal B_c,
\]

to wartości ewentualnego rozszerzenia

\[
\widetilde f:\mathcal B_c\to M_{\mathcal T,c}
\]

poza obrazem obserwatora nie są wyznaczone przez równanie

\[
q_{\mathcal T,c}=\widetilde f\circ\Psi_c.
\]

Dlatego twierdzenie nie ustanawia unikalnej mapy na całej \(\mathcal B_c\), chyba że \(\Psi_c\) jest surjektywna albo zadano dodatkową zasadę rozszerzenia.

Jest to bezpośrednia specjalizacja rygla F60.

---

## 9. Status źródłowy

Twierdzenie II.3 jest bezpośrednim zastosowaniem klasycznego elementarnego lematu faktoryzacyjnego II.2 do architektury PSI.

Status:

\[
\boxed{
\text{PSI STRUCTURAL BRIDGE / DIRECT COROLLARY OF CLASSICAL FACTORIZATION}.
}
\]

Nie ma tu roszczenia, że samo twierdzenie o faktoryzacji map jest nowe. Treścią właściwą PSI jest identyfikacja:

\[
\rho=\Psi_c,
\qquad
R=q_{\mathcal T,c},
\qquad
\ker_{\rm eq}R=E_{\mathcal T,c},
\]

oraz interpretacja inkluzji jąder jako globalnej wystarczalności kanału obserwacyjnego względem zadania.

---

## 10. Czego twierdzenie nie ustanawia

Twierdzenie II.3 nie daje automatycznie:

- globalnej injektywności \(\Psi_c\);
- identyfikacji pełnego kandydata;
- rozstrzygalności dla każdego rekordu przy nieadekwatnym katalogu;
- stabilności na perturbacje danych;
- probabilistycznej wystarczalności/statystycznej sufficiency;
- mierzalności, ciągłości ani obliczalności mapy \(f\);
- legalności całego kontraktu tylko z samej inkluzji jąder;
- unikalnego rozszerzenia \(f\) na całą \(\mathcal B_c\).

W szczególności termin „wystarczalność” w tym twierdzeniu oznacza **dokładną wystarczalność zadaniową w sensie faktoryzacji**, a nie klasyczne statystyczne pojęcie statystyki dostatecznej.

---

## 11. Wiązanie z regresjami

HCube i Go pokazują ten sam schemat błędu dla innych reprezentacji:

\[
\text{reprezentacja skleja parę, którą zadanie nadal rozróżnia}.
\]

Nie są jednak dowodami II.3.

Dla samego obserwatora obowiązkowy lokalny falsyfikator ma postać

\[
\boxed{
\Psi_c(x)=\Psi_c(y),
\qquad
x\not E_{\mathcal T,c}y.
}
\]

FS-STAT dotyczy innej warstwy i przypomina, że nawet dokładna globalna faktoryzacja nie daje automatycznie stabilności ani licencji statystycznej.

---

## 12. Przejście do II.4

Twierdzenie II.3 jest specjalizacją kryterium faktoryzacji do konkretnej reprezentacji \(\Psi_c\).

Następny krok usuwa szczególną rolę obserwatora i wraca do dowolnej reprezentacji

\[
\rho:\Omega_c\to Z.
\]

Otrzymamy centralne kryterium adekwatności reprezentacji:

\[
\boxed{
\ker_{\rm eq}\rho
\subseteq
E_{\mathcal T,c}
\iff
q_{\mathcal T,c}
\text{ faktoryzuje przez }\rho
\text{ na }\operatorname{im}\rho.
}
\]

To będzie Twierdzenie II.4.
