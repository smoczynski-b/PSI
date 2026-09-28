# PRINCIPIA SEMANTICA — TOM II
## II.5. Zadaniowa legalność informacyjna redukcji i ilorazu

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, C32/C37 zachowane przez Freeze 01  
**Mapa twierdzeń:** `principia-v2-theorem-map-02.md`, II.5  
**Zależność:** bezpośrednia specjalizacja Twierdzenia II.4.  
**Granice:** F57 — adekwatność zadaniowa ≠ pełna legalność kontraktowa; F55 — symetria geometryczna ≠ automatycznie legalny gauge.

---

## 1. Typy

Niech

\[
q:\Omega_c\to Z
\]

będzie proponowaną redukcją reprezentacji kandydatów w ustalonym kontrakcie \(c\).

Nie zakładamy na początku, że \(q\) jest projekcją ilorazową, mapą orbit, kompresją pamięci ani mapą surjektywną. Jest po prostu mapą, która ma zastąpić pełnego kandydata \(x\in\Omega_c\) przez zredukowaną reprezentację \(q(x)\).

Niech

\[
E_{\mathcal T,c}\subseteq\Omega_c\times\Omega_c
\]

będzie równoważnością zadaniową, a

\[
q_{\mathcal T,c}:\Omega_c\to M_{\mathcal T,c}
=\Omega_c/E_{\mathcal T,c}
\]

projekcją na iloraz zadaniowy.

Definiujemy relację sklejenia redukcji:

\[
\ker_{\rm eq}q
=
\{(x,y)\in\Omega_c^2:q(x)=q(y)\}.
\]

---

## 2. Co znaczy „zadaniowo legalna informacyjnie”

Redukcja \(q\) jest **zadaniowo legalna informacyjnie** wtedy, gdy nie usuwa żadnego rozróżnienia wymaganego przez zadanie.

Formalnie:

\[
\boxed{
q(x)=q(y)
\Longrightarrow
xE_{\mathcal T,c}y.
}
\]

Równoważnie:

\[
\boxed{
\ker_{\rm eq}q
\subseteq
E_{\mathcal T,c}.
}
\]

Termin „legalna” w tym rozdziale jest zawsze kwalifikowany słowem **informacyjnie** albo **zadaniowo**. Nie oznacza jeszcze pełnej legalności całego kontraktu.

---

## 3. Wniosek II.5 — kryterium zadaniowej legalności informacyjnej redukcji

### Wniosek

Dla dowolnej redukcji

\[
q:\Omega_c\to Z
\]

zachodzi równoważność

\[
\boxed{
\ker_{\rm eq}q
\subseteq
E_{\mathcal T,c}
\iff
\exists!\,h:\operatorname{im}q\to M_{\mathcal T,c},
\qquad
q_{\mathcal T,c}=h\circ q.
}
\]

Inaczej:

\[
\boxed{
\text{redukcja zachowuje całą dokładną informację zadaniową}
\iff
\text{klasa zadaniowa daje się odtworzyć z samego }q(x).
}
\]

Unikalność \(h\) obowiązuje wyłącznie na \(\operatorname{im}q\).

### Dowód

Jest to Twierdzenie II.4 zastosowane do reprezentacji

\[
\rho=q.
\]

Twierdzenie II.4 daje

\[
\ker_{\rm eq}q
\subseteq
E_{\mathcal T,c}
\iff
\exists!\,h:\operatorname{im}q\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=h\circ q.
\]

Nie potrzeba żadnej dodatkowej hipotezy. \(\square\)

---

## 4. Redukcja przez relację równoważności

Niech

\[
Q\subseteq\Omega_c\times\Omega_c
\]

będzie relacją równoważności i niech

\[
q_Q:\Omega_c\to\Omega_c/Q
\]

będzie projekcją ilorazową.

Wtedy

\[
\ker_{\rm eq}q_Q=Q.
\]

Dlatego Wniosek II.5 przyjmuje szczególnie prostą postać:

\[
\boxed{
Q\subseteq E_{\mathcal T,c}
\iff
q_Q\text{ zachowuje dokładną informację zadaniową}.
}
\]

To jest właściwe kryterium dla każdego proponowanego „sklejenia” kandydatów przez relację równoważności.

Jeżeli istnieją

\[
xQy
\]

oraz

\[
x\not E_{\mathcal T,c}y,
\]

to iloraz przez \(Q\) jest za gruby dla zadania.

---

## 5. Gauge jako przypadek redukcji

Niech grupa \(G\) działa na \(\Omega_c\), a

\[
q_G:\Omega_c\to\Omega_c/G
\]

będzie mapą orbit.

Jej jądro równoważności jest relacją orbitową:

\[
(x,y)\in\ker_{\rm eq}q_G
\iff
\exists g\in G:\ y=g\cdot x.
\]

Dlatego zadaniowa legalność informacyjna gauge wymaga

\[
\boxed{
\ker_{\rm eq}q_G
\subseteq
E_{\mathcal T,c}.
}
\]

Równoważnie, każda para kandydatów leżących w tej samej orbicie \(G\) musi być zadaniowo nierozróżnialna.

Nie wystarcza sam fakt, że \(G\) jest naturalną symetrią geometryczną, fizyczną albo prezentacyjną modelu.

---

## 6. Najkrótszy falsyfikator redukcji

Jedna para

\[
x,y\in\Omega_c
\]

spełniająca

\[
q(x)=q(y)
\]

oraz

\[
x\not E_{\mathcal T,c}y
\]

wystarcza do wykazania

\[
\ker_{\rm eq}q
\not\subseteq
E_{\mathcal T,c}.
\]

Wtedy nie istnieje mapa

\[
h:\operatorname{im}q\to M_{\mathcal T,c}
\]

spełniająca

\[
q_{\mathcal T,c}=h\circ q.
\]

Jest to dokładny, jednoparowy falsyfikator zbyt grubej redukcji.

---

## 7. Dwie odrębne bramki: informacja zadaniowa i kontrakt

Wniosek II.5 odpowiada tylko na pytanie:

\[
\boxed{
\text{czy redukcja zachowuje wszystkie dokładne rozróżnienia wymagane przez zadanie?}
}
\]

Nie odpowiada samo na pytanie:

\[
\boxed{
\text{czy redukcja jest legalna w całym kontrakcie?}
}
\]

Pełna legalność może dodatkowo wymagać między innymi:

- poprawnego typu dziedziny i przeciwdziedziny;
- działania zdefiniowanego na właściwym obiekcie;
- zgodności lub ekwiwariantności z mapą obserwacji;
- zachowania zewnętrznego interfejsu;
- spełnienia warunków `ADM_D`;
- poprawnej dziedziny operatorowej;
- regularności, mierzalności lub topologii, jeśli kontrakt ich wymaga.

Dlatego obowiązuje rygiel F57:

\[
\boxed{
\ker_{\rm eq}q\subseteq E_{\mathcal T,c}
\not\Rightarrow
q\text{ jest automatycznie w pełni legalna kontraktowo}.
}
\]

Warunek II.5 jest dokładnym testem **zachowania informacji zadaniowej**, nie kompletnym automatem legalności kontraktu.

---

## 8. F55 — dlaczego symetria nie wystarcza

Skorygowany benchmark Frenet/Bishop pokazuje różnicę pomiędzy symetrią geometryczną a legalnym gauge problemu obserwacyjnego.

W kontrakcie absolutnym

\[
P_0^{abs}:Y=\gamma(t)
\]

zewnętrzne przekształcenie

\[
g\in SE(3)
\]

na ogół zmienia obserwację:

\[
\Psi(g\cdot\gamma)\neq\Psi(\gamma).
\]

Dlatego samo geometryczne istnienie działania \(SE(3)\) nie daje prawa do quotientowania tego działania **wewnątrz tego samego włókna obserwacyjnego**.

W kontrakcie kształtowym

\[
P_0^{shape}:Y=[\gamma]_{SE(3)}
\]

sytuacja jest inna, bo kontrakt obserwacyjny sam ustanawia niezmienniczość względem \(SE(3)\).

Wniosek:

\[
\boxed{
\text{zadaniowa adekwatność gauge}
\quad\text{i}\quad
\text{zgodność gauge z obserwacją}
}
\]

są dwiema odrębnymi kontrolami. W odpowiednim kontrakcie obie mogą być wymagane; żadna nie zastępuje drugiej.

---

## 9. HIGHER-FIBRE — kolejność truncacji

W świadku

\[
*\to B\mathbb Z_2\leftarrow *
\]

zgrubienie do poziomu komponentów może utożsamić dwa świadectwa kompatybilności, które zadanie nadal rozróżnia.

Jeżeli reprezentacja zgrubiona \(\rho_{\rm coarse}\) spełnia

\[
\rho_{\rm coarse}(e)=\rho_{\rm coarse}(s)
\]

przy jednoczesnym

\[
e\not E_{\mathcal T,c}s,
\]

to

\[
\ker_{\rm eq}\rho_{\rm coarse}
\not\subseteq
E_{\mathcal T,c}.
\]

Dlatego bezpieczna kolejność brzmi:

\[
\boxed{
\text{zachowaj dane kompatybilności istotne dla zadania}
\to
\text{dopiero potem wykonaj zadaniowo legalną truncację}.
}
\]

Nie jest to twierdzenie, że struktura wyższa jest potrzebna dla każdego zadania.

---

## 10. Kompresja pamięci

Ta sama zasada obejmuje pamięć historii. Dla

\[
q_t:\mathcal H_t\to Z_t
\]

redukcja pamięci jest dokładnie zadaniowo legalna wtedy, gdy

\[
\ker_{\rm eq}q_t
\subseteq
\equiv_{\mathcal T,t}.
\]

Go R02 dostarcza przykładów, gdzie reprezentacja wystarczająca dla jednej reguły staje się za gruba po zmianie zadania/reguły.

Zmiana wymaganej pamięci nie oznacza wzrostu liczby prymitywów PSI. Oznacza zmianę granicy dopuszczalnej kompresji względem nowego kontraktu zadaniowego.

---

## 11. Redukcja informacyjnie drobniejsza

Jeżeli dwie redukcje

\[
q_1:\Omega_c\to Z_1,
\qquad
q_2:\Omega_c\to Z_2
\]

spełniają

\[
\ker_{\rm eq}q_1
\subseteq
\ker_{\rm eq}q_2,
\]

a \(q_2\) jest zadaniowo legalna informacyjnie, to

\[
\ker_{\rm eq}q_1
\subseteq
\ker_{\rm eq}q_2
\subseteq
E_{\mathcal T,c}.
\]

Zatem \(q_1\) również zachowuje dokładną informację zadaniową.

Czyli przejście do reprezentacji drobniejszej informacyjnie nie może samo zniszczyć dokładnej adekwatności zadaniowej. Może natomiast zwiększyć koszt, wymiar lub nadmiar informacji — tych własności II.5 nie ocenia.

---

## 12. Status źródłowy

Wniosek II.5 jest bezpośrednią specjalizacją Twierdzenia II.4.

Status:

\[
\boxed{
\text{PSI SCOPE COROLLARY / REPRESENTATION-ADEQUACY SPECIALIZATION}.
}
\]

Nie jest nowym twierdzeniem o teorii ilorazów. Wkład PSI polega na użyciu zadaniowej równoważności \(E_{\mathcal T,c}\) jako jawnego testu tego, które sklejenia można wykonać bez utraty dokładnej informacji potrzebnej zadaniu.

C32 i C37 nie tworzą nowego prymitywu CORE.

---

## 13. Czego Wniosek II.5 nie ustanawia

Nie ustanawia automatycznie:

- legalności pełnego kontraktu;
- legalności działania grupowego względem obserwacji;
- poprawności dziedziny operatorowej;
- zachowania stabilizatorów lub świadectw zgodności, jeśli zadanie ich nie modeluje jawnie;
- stabilności numerycznej;
- licencji probabilistycznej;
- obliczalności ilorazu;
- minimalnego kosztu reprezentacji;
- prawa do zastąpienia groupoidu/stacka jego zbiorem orbit w każdym zadaniu;
- prawa do wykonania truncacji przed utworzeniem właściwego włókna kompatybilności.

---

## 14. Przejście do dynamiki

II.5 rozstrzyga, kiedy **statyczne sklejenie** zachowuje informację zadaniową.

Następne pytanie brzmi:

> kiedy dynamika na \(\Omega\) schodzi jednoznacznie na zadeklarowany iloraz?

Dla relacji równoważności \(E\) i mapy

\[
\delta:\Omega\to\Omega
\]

warunkiem będzie kongruencja:

\[
\boxed{
xEy\Longrightarrow\delta(x)E\delta(y).}
\]

To jest przedmiot II.6 — deterministycznej dynamiki ilorazowej.
