# PRINCIPIA SEMANTICA — TOM II
## II.4. Adekwatność reprezentacji względem zadania

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, C09 zachowane przez Freeze 01  
**Mapa twierdzeń:** `principia-v2-theorem-map-01.md`, T2.4  
**Zależność:** bezpośrednia specjalizacja Twierdzenia II.2 dla `R=q_{\mathcal T,c}`.  
**Granica:** F57 — adekwatność zadaniowa nie jest pełną legalnością kontraktu.

---

## 1. Typy

Niech

\[
\rho:\Omega_c\to Z
\]

będzie dowolną reprezentacją kandydatów w ustalonym kontrakcie \(c\).

Niech

\[
E_{\mathcal T,c}\subseteq\Omega_c\times\Omega_c
\]

będzie równoważnością zadaniową oraz

\[
q_{\mathcal T,c}:\Omega_c\to M_{\mathcal T,c}
=\Omega_c/E_{\mathcal T,c}
\]

projekcją na iloraz zadaniowy.

Definiujemy

\[
\ker_{\rm eq}\rho
=
\{(x,y)\in\Omega_c^2:\rho(x)=\rho(y)\}.
\]

Nie zakładamy, że \(\rho\) jest obserwatorem, ilorazem, statystyką, stanem pamięci ani mapą surjektywną. Jest dowolną jawnie otypowaną reprezentacją kandydatów.

---

## 2. Dokładna adekwatność informacyjna

Reprezentacja \(\rho\) jest dokładnie adekwatna informacyjnie względem zadania \(\mathcal T\), jeżeli żadne sklejenie wykonywane przez \(\rho\) nie usuwa rozróżnienia wymaganego przez zadanie.

Formalnie:

\[
\boxed{
\rho(x)=\rho(y)
\Longrightarrow
xE_{\mathcal T,c}y.
}
\]

Równoważnie:

\[
\boxed{
\ker_{\rm eq}\rho
\subseteq
E_{\mathcal T,c}.
}
\]

Jest to pojęcie **zadaniowo względne**. Ta sama reprezentacja może być adekwatna dla jednego zadania i nieadekwatna dla innego.

---

## 3. Twierdzenie II.4 — adekwatność reprezentacji

### Twierdzenie

Dla dowolnej reprezentacji

\[
\rho:\Omega_c\to Z
\]

zachodzi równoważność

\[
\boxed{
\ker_{\rm eq}\rho
\subseteq
E_{\mathcal T,c}
\iff
\exists!\,g:\operatorname{im}\rho\to M_{\mathcal T,c},
\qquad
q_{\mathcal T,c}=g\circ\rho.
}
\]

Inaczej:

\[
\boxed{
\rho\text{ jest dokładnie zadaniowo adekwatna}
\iff
\text{klasę zadaniową można wyznaczyć z samej }\rho(x).
}
\]

Unikalność mapy \(g\) obowiązuje wyłącznie na \(\operatorname{im}\rho\).

---

## 4. Dowód

Stosujemy Twierdzenie II.2 do map

\[
\rho:\Omega_c\to Z
\]

oraz

\[
R=q_{\mathcal T,c}:\Omega_c\to M_{\mathcal T,c}.
\]

Dla projekcji ilorazowej zachodzi

\[
\ker_{\rm eq}q_{\mathcal T,c}
=
E_{\mathcal T,c}.
\]

Twierdzenie II.2 daje więc

\[
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}q_{\mathcal T,c}
\iff
\exists!\,g:\operatorname{im}\rho\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=g\circ\rho.
\]

Po podstawieniu

\[
\ker_{\rm eq}q_{\mathcal T,c}=E_{\mathcal T,c}
\]

otrzymujemy dokładnie

\[
\ker_{\rm eq}\rho
\subseteq
E_{\mathcal T,c}
\iff
\exists!\,g:\operatorname{im}\rho\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=g\circ\rho.
\]

To kończy dowód. \(\square\)

---

## 5. Najkrótszy falsyfikator adekwatności

Jedna para

\[
x,y\in\Omega_c
\]

spełniająca

\[
\rho(x)=\rho(y)
\]

oraz

\[
x\not E_{\mathcal T,c}y
\]

wystarcza do obalenia dokładnej adekwatności reprezentacji.

Wtedy

\[
(x,y)\in\ker_{\rm eq}\rho
\]

lecz

\[
(x,y)\notin E_{\mathcal T,c},
\]

a zatem

\[
\ker_{\rm eq}\rho
\not\subseteq
E_{\mathcal T,c}.
\]

Nie może więc istnieć mapa

\[
g:\operatorname{im}\rho\to M_{\mathcal T,c}
\]

spełniająca

\[
q_{\mathcal T,c}=g\circ\rho.
\]

To jest centralny falsyfikator reprezentacji w PSI.

---

## 6. Porządek informacyjny

Jeżeli dwie reprezentacje

\[
\rho_1:\Omega_c\to Z_1,
\qquad
\rho_2:\Omega_c\to Z_2
\]

spełniają

\[
\ker_{\rm eq}\rho_1
\subseteq
\ker_{\rm eq}\rho_2,
\]

to \(\rho_1\) rozróżnia co najmniej tyle par kandydatów co \(\rho_2\).

W tym sensie \(\rho_1\) jest informacyjnie co najmniej tak drobna jak \(\rho_2\).

Jeżeli \(\rho_2\) jest zadaniowo adekwatna, tj.

\[
\ker_{\rm eq}\rho_2\subseteq E_{\mathcal T,c},
\]

to z przechodniości inkluzji wynika

\[
\ker_{\rm eq}\rho_1\subseteq E_{\mathcal T,c}.
\]

Zatem każda reprezentacja informacyjnie drobniejsza od reprezentacji adekwatnej również zachowuje dokładną informację zadaniową.

Odwrotność nie musi zachodzić: reprezentacja może być znacznie drobniejsza niż wymaga zadanie i przechowywać nadmiarowe rozróżnienia.

---

## 7. Iloraz zadaniowy jako granica dokładnej kompresji

Sama projekcja

\[
q_{\mathcal T,c}:\Omega_c\to M_{\mathcal T,c}
\]

spełnia

\[
\ker_{\rm eq}q_{\mathcal T,c}
=
E_{\mathcal T,c}.
\]

Jest więc dokładnie adekwatna i usuwa wszystkie rozróżnienia, które zadanie uznaje za nieistotne.

Nie należy jednak z tego w tym miejscu wyciągać silniejszego wniosku o minimalnej liczbie bitów, minimalnym wymiarze, minimalnym koszcie pamięci ani najtańszej implementacji. Te pojęcia wymagają dodatkowej struktury kosztowej.

W porządku ilorazowym \(M_{\mathcal T,c}\) jest naturalnym celem faktoryzacji reprezentacji zachowujących dokładną informację zadaniową; techniczne twierdzenia o odpowiedniej własności uniwersalnej dla historii pojawią się później.

---

## 8. Szczególny przypadek: obserwator

Jeżeli

\[
\rho=\Psi_c,
\]

to Twierdzenie II.4 redukuje się do Twierdzenia II.3:

\[
\ker_{\rm eq}\Psi_c
\subseteq
E_{\mathcal T,c}
\iff
q_{\mathcal T,c}
\text{ faktoryzuje przez }\Psi_c.
\]

Globalna wystarczalność obserwatora nie jest więc osobną zasadą strukturalną. Jest szczególnym przypadkiem ogólnej adekwatności reprezentacji.

---

## 9. Szczególny przypadek: pamięć historii

Jeżeli dziedziną reprezentacji jest przestrzeń historii

\[
\mathcal H_t
\]

a rolę równoważności zadaniowej pełni przyszłościowa relacja

\[
\equiv_{\mathcal T,t},
\]

to ten sam schemat daje

\[
\boxed{
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

To jest dokładna adekwatność pamięci z Tomu I i późniejszego rozdziału o ilorazie historii. Nie jest nowym prymitywem: jest specjalizacją tego samego testu reprezentacji.

---

## 10. Zadaniowa adekwatność nie jest pełną legalnością kontraktu

To najważniejsza granica zakresu Twierdzenia II.4.

Z

\[
\ker_{\rm eq}\rho
\subseteq
E_{\mathcal T,c}
\]

wynika, że \(\rho\) zachowuje wszystkie dokładne rozróżnienia wymagane przez zadanie.

Nie wynika automatycznie, że \(\rho\) jest **w pełni legalna w kontrakcie**.

Pełna legalność może dodatkowo wymagać między innymi:

- poprawnego typu i dziedziny;
- zgodności z obserwacją lub jej ekwiwariantności;
- legalnego działania gauge;
- zachowania interfejsu zewnętrznego;
- warunków dziedzinowych `ADM_D`;
- warunków regularności, mierzalności albo topologii, jeśli kontrakt je ustanawia.

Dlatego obowiązuje rygiel F57:

\[
\boxed{
\text{task-information adequacy}
\neq
\text{full contract legality}
}
\]

w ogólności.

---

## 11. Status źródłowy

Twierdzenie II.4 jest bezpośrednim zastosowaniem klasycznego elementarnego lematu faktoryzacyjnego II.2 do ilorazu zadaniowego PSI.

Status:

\[
\boxed{
\text{PSI CENTRAL STRUCTURAL BRIDGE / DIRECT FACTORIZATION COROLLARY}.
}
\]

PSI nie rości sobie autorstwa ogólnego lematu o faktoryzacji map. Treścią właściwą architekturze PSI jest wybór zadaniowej równoważności

\[
E_{\mathcal T,c}
\]

jako kryterium tego, które sklejenia reprezentacji są informacyjnie legalne dla zadania.

---

## 12. Wiązanie z regresjami

### R01 — HCube

Dla zadania, którego domknięcie zadaniowe zawiera wielkość rezolwentową \(R_{1/2}\), HCube dostarcza reprezentacji \(\rho_0\), która utożsamia dwie macierze o tej samej informacji grubej, podczas gdy zadanie nadal je rozróżnia:

\[
\rho_0(A)=\rho_0(B),
\qquad
R_{1/2}(A)\neq R_{1/2}(B).
\]

Z definicji \(E_{\mathcal T}\) wynika wtedy

\[
A\not E_{\mathcal T}B,
\]

a więc jest to konkretny świadek

\[
\ker_{\rm eq}\rho_0
\not\subseteq
E_{\mathcal T}.
\]

### R02 — Go

Go dostarcza analogicznego świadka dla kompresji historii: dwie historie mogą mieć tę samą reprezentację pamięci, lecz różną przyszłą legalność tego samego ruchu. Wtedy

\[
\ker_{\rm eq}\rho_t
\not\subseteq
\equiv_{\mathcal T,t}.
\]

### R03 — FS-STAT

FS-STAT nie falsyfikuje Twierdzenia II.4. Wyznacza jego granicę interpretacyjną:

\[
\boxed{
\text{exact task adequacy}
\not\Rightarrow
\text{stable or statistically licensed inference}.
}
\]

Regresje pełnią więc różne role: R01 i R02 testują samo kryterium zachowania rozróżnień; R03 testuje zakaz rozszerzania jego zakresu.

---

## 13. Czego twierdzenie nie ustanawia

Twierdzenie II.4 nie ustanawia automatycznie:

- pełnej legalności kontraktowej reprezentacji;
- stabilności względem perturbacji;
- licencji probabilistycznej;
- ciągłości lub mierzalności mapy faktoryzującej;
- obliczalności reprezentacji albo ilorazu;
- minimalnej liczby bitów;
- minimalnego kosztu pamięci lub obliczeń;
- prawa do quotientowania dowolnej symetrii geometrycznej;
- adekwatności katalogu kandydatów.

Każdy z tych wniosków wymaga osobnej bramki.

---

## 14. Domknięcie pierwszego kręgosłupa V2

Pierwsze cztery jednostki Tomu II tworzą teraz łańcuch:

\[
\boxed{
\begin{aligned}
\mathrm{II.1}:&\quad
\text{rozstrzygalność jednego włókna},\\
\mathrm{II.2}:&\quad
\text{ogólne kryterium faktoryzacji},\\
\mathrm{II.3}:&\quad
\text{obserwator jako szczególna reprezentacja},\\
\mathrm{II.4}:&\quad
\text{dowolna reprezentacja względem zadania}.
\end{aligned}
}
\]

Następnym legalnym krokiem nie jest jeszcze kolejny most klasyczny. Najpierw należy sprawdzić II.1–II.4 jako jeden system pod kątem typów, zakresów, zależności, statusów źródłowych i regresji.
