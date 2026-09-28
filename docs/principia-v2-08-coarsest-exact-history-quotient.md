# PRINCIPIA SEMANTICA — TOM II
## II.8. Najgrubszy dokładny iloraz historii

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PENDING`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, z zachowanym C44 z `claim-registry-09.md`  
**Mapa twierdzeń:** `principia-v2-theorem-map-02.md`, II.8  
**Zależności:** II.2 oraz II.7.  
**Granica:** najgrubszy dokładny iloraz w porządku ilorazów ≠ minimalna implementacja bitowa, wymiarowa, pamięciowa lub obliczeniowa.

---

## 1. Punkt wyjścia

Ustalamy kontrakt oraz chwilę \(t\). Niech

\[
\mathcal H_t
\]

będzie przestrzenią legalnych historii, a

\[
\equiv_{\mathcal T,t}
\]

przyszłościową równoważnością zadaniową z II.7.

Z Lematu II.7.A jest to relacja równoważności. Definiujemy więc kanoniczny iloraz historii

\[
\boxed{
M_{\mathcal T,t}
:=
\mathcal H_t/\!\equiv_{\mathcal T,t}
}
\]

oraz projekcję

\[
q_{\mathcal T,t}:\mathcal H_t\to M_{\mathcal T,t},
\qquad
q_{\mathcal T,t}(H)=[H]_{\mathcal T,t}.
\]

Iloraz ten usuwa dokładnie te rozróżnienia historyczne, które nie zmieniają przyszłej semantyki zadania.

---

## 2. Porządek informacyjny reprezentacji

Dla dwóch reprezentacji historii

\[
\rho_1:\mathcal H_t\to Z_1,
\qquad
\rho_2:\mathcal H_t\to Z_2
\]

piszemy, że \(\rho_1\) jest **informacyjnie drobniejsza** od \(\rho_2\), gdy

\[
\boxed{
\ker_{\rm eq}\rho_1
\subseteq
\ker_{\rm eq}\rho_2.
}
\]

Im mniejsze jądro równoważności, tym więcej par historii reprezentacja nadal rozróżnia.

W szczególności dokładna adekwatność II.7 ma postać

\[
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
\]

Zatem każda dokładna pamięć jest informacyjnie co najmniej tak drobna jak kanoniczny iloraz zadaniowy.

---

## 3. Twierdzenie II.8 — faktoryzacja każdej dokładnej pamięci

### Twierdzenie

Niech

\[
\rho_t:\mathcal H_t\to Z_t
\]

będzie dokładnie adekwatną reprezentacją pamięci, tj.

\[
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
\]

Wtedy istnieje dokładnie jedna mapa

\[
\boxed{
f_t:\operatorname{im}\rho_t\to M_{\mathcal T,t}}
\]

taka, że

\[
\boxed{
q_{\mathcal T,t}=f_t\circ\rho_t.
}
\]

Ponadto \(f_t\) jest surjektywna.

### Dowód

Istnienie i unikalność na \(\operatorname{im}\rho_t\) są dokładnie Twierdzeniem II.7, a ostatecznie specjalizacją kryterium faktoryzacji II.2.

Pozostaje surjektywność. Niech

\[
[H]_{\mathcal T,t}\in M_{\mathcal T,t}
\]

będzie dowolną klasą. Ponieważ

\[
q_{\mathcal T,t}=f_t\circ\rho_t,
\]

mamy

\[
[H]_{\mathcal T,t}
=q_{\mathcal T,t}(H)
=f_t(\rho_t(H)).
\]

A zatem każda klasa zadaniowa należy do obrazu \(f_t\). \(\square\)

---

## 4. Ilorazy przez relacje równoważności

Niech

\[
Q\subseteq\mathcal H_t\times\mathcal H_t
\]

będzie relacją równoważności i

\[
q_Q:\mathcal H_t\to\mathcal H_t/Q
\]

projekcją ilorazową.

Z II.5/II.7 iloraz \(q_Q\) jest dokładnie zadaniowo adekwatny wtedy i tylko wtedy, gdy

\[
\boxed{
Q\subseteq\equiv_{\mathcal T,t}.
}
\]

Jeżeli warunek zachodzi, istnieje jednoznaczna mapa

\[
\pi_Q:\mathcal H_t/Q\to M_{\mathcal T,t}
\]

taka, że

\[
\boxed{
q_{\mathcal T,t}=\pi_Q\circ q_Q.
}
\]

Jawnie:

\[
\pi_Q([H]_Q)=[H]_{\mathcal T,t}.
\]

Dobra określoność wynika właśnie z

\[
Q\subseteq\equiv_{\mathcal T,t}.
\]

Mapa \(\pi_Q\) jest surjektywna.

---

## 5. Najgrubszy dokładny iloraz

W porządku relacji równoważności przez inkluzję większa relacja skleja więcej par, a więc daje grubszy iloraz.

Rodzina dokładnie dopuszczalnych relacji ilorazowych ma postać

\[
\mathfrak Q_{\mathcal T,t}
=
\{Q:\ Q\text{ jest relacją równoważności na }\mathcal H_t,
\ Q\subseteq\equiv_{\mathcal T,t}\}.
\]

Sama relacja

\[
\equiv_{\mathcal T,t}
\]

należy do tej rodziny i zawiera każdą inną jej relację.

Dlatego:

\[
\boxed{
\equiv_{\mathcal T,t}
=
\max\mathfrak Q_{\mathcal T,t}
}
\]

w porządku inkluzji relacji równoważności.

Równoważnie:

\[
\boxed{
M_{\mathcal T,t}
=
\mathcal H_t/\!\equiv_{\mathcal T,t}
}
\]

jest **najgrubszym dokładnym ilorazem historii** względem zadania \(\mathcal T\).

Każdy dokładny iloraz \(\mathcal H_t/Q\) zachowuje co najmniej tyle rozróżnień, ile \(M_{\mathcal T,t}\), i posiada kanoniczną surjekcję

\[
\mathcal H_t/Q\twoheadrightarrow M_{\mathcal T,t}.
\]

---

## 6. Dowolna reprezentacja a iloraz przez jej jądro

Dla dowolnej reprezentacji

\[
\rho_t:\mathcal H_t\to Z_t
\]

jej obraz jest kanonicznie bijektywny z ilorazem przez jądro równoważności:

\[
\boxed{
\mathcal H_t/\ker_{\rm eq}\rho_t
\cong
\operatorname{im}\rho_t.
}
\]

Bijekcja jest dana przez

\[
[H]_{\ker\rho_t}
\longmapsto
\rho_t(H).
\]

Jeżeli \(\rho_t\) jest dokładna, to

\[
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t},
\]

a więc otrzymujemy ciąg

\[
\mathcal H_t
\longrightarrow
\mathcal H_t/\ker_{\rm eq}\rho_t
\cong
\operatorname{im}\rho_t
\xrightarrow{\ f_t\ }
M_{\mathcal T,t}.
\]

To jest dokładny sens stwierdzenia, że każda adekwatna pamięć może zawierać nadmiar informacji, który zadaniowy iloraz następnie usuwa.

---

## 7. Kanoniczność nie oznacza jedynego kodowania

Nie należy pisać, że \(M_{\mathcal T,t}\) jest „jedyną minimalną reprezentacją” w sensie dosłownej równości zbiorów lub kodów.

Jeżeli

\[
b:M_{\mathcal T,t}\to Z
\]

jest bijekcją, to

\[
\rho_t=b\circ q_{\mathcal T,t}
\]

ma dokładnie to samo jądro:

\[
\ker_{\rm eq}\rho_t
=
\equiv_{\mathcal T,t}.
\]

Zatem istnieje wiele równoważnych przekodowań tej samej najgrubszej informacji zadaniowej.

Kanoniczny jest iloraz przez relację

\[
\equiv_{\mathcal T,t},
\]

a nie szczególny zapis symboli, numeracja klas ani fizyczny format pamięci.

---

## 8. Co dokładnie znaczy „minimalność”

Twierdzenie II.8 ustanawia minimalność wyłącznie w porządku informacyjnym/ilorazowym:

\[
\boxed{
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}
}
\]

dla każdej dokładnej reprezentacji.

Nie ustanawia automatycznie minimalności:

- liczby bitów;
- wymiaru wektora kodującego;
- rozmiaru struktur danych;
- kosztu pamięci fizycznej;
- kosztu aktualizacji;
- czasu obliczeń;
- złożoności algorytmicznej;
- wygody konkretnego kodowania.

Dla skończonej reprezentacji dokładnej surjekcja

\[
f_t:\operatorname{im}\rho_t\twoheadrightarrow M_{\mathcal T,t}
\]

daje oczywiście

\[
|M_{\mathcal T,t}|
\le
|\operatorname{im}\rho_t|,
\]

ale nawet wtedy minimalna liczba klas nie jest tym samym co minimalny koszt implementacji.

---

## 9. Najkrótszy falsyfikator roszczenia o dokładność

Jeżeli proponowany iloraz przez \(Q\) ma być dokładny, ale istnieją

\[
H Q H'
\]

oraz

\[
H\not\equiv_{\mathcal T,t}H',
\]

to

\[
Q\not\subseteq\equiv_{\mathcal T,t}
\]

i iloraz jest zbyt gruby.

Nie ma wtedy mapy

\[
\pi_Q:\mathcal H_t/Q\to M_{\mathcal T,t}
\]

spełniającej

\[
q_{\mathcal T,t}=\pi_Q\circ q_Q.
\]

Jeden taki świadek wystarcza.

---

## 10. Relacja do Go i LAZARUS

Regres Go pokazuje kolejne reprezentacje, które przy zmianie kontraktu reguł mogą okazać się zbyt grube lub nadal wystarczające. II.8 nie mówi, że któraś konkretna reprezentacja Go jest uniwersalnie minimalna.

LAZARUS pokazuje z kolei, że bieżące włókno świata może mieć jądro większe niż dopuszcza przyszła równoważność zadaniowa. W takim przypadku mapa bieżącego włókna nie może być nawet dokładną reprezentacją, a więc tym bardziej nie jest kandydatem na najgrubszy dokładny iloraz.

Oba świadki testują granicę zastosowania, nie dowodzą ogólnego Twierdzenia II.8.

---

## 11. Status źródłowy

C44 łączy klasyczną faktoryzację przez jądro z przyszłościową równoważnością zadaniową RED-1.

Status:

\[
\boxed{
\text{CLASSICAL FACTORIZATION / QUOTIENT ORDER}
\; + \;
\text{PSI TASK-HISTORY BRIDGE}.
}
\]

PSI nie rości sobie autorstwa ogólnego porządku ilorazów ani faktoryzacji przez jądro. Wkład tej warstwy polega na wskazaniu

\[
\equiv_{\mathcal T,t}
\]

jako maksymalnego dopuszczalnego sklejenia historii, które zachowuje całą przyszłą semantykę danego zadania.

---

## 12. Czego Twierdzenie II.8 nie ustanawia

Nie ustanawia:

- skończonej liczby klas \(M_{\mathcal T,t}\);
- skończonego automatu pamięci;
- efektywnej procedury obliczania klasy historii;
- efektywnej aktualizacji klasy;
- minimalnego kodowania bitowego;
- minimalnej reprezentacji liniowej lub geometrycznej;
- minimalnego czasu obliczeń;
- niezależności od kontraktu lub zadania;
- dobrze określonej rekurencyjnej aktualizacji klas — to jest II.9.

---

## 13. Przejście do II.9

II.8 odpowiada na pytanie:

> jaki jest najgrubszy dokładny iloraz historii względem przyszłej semantyki zadania?

Odpowiedź brzmi:

\[
M_{\mathcal T,t}
=
\mathcal H_t/\!\equiv_{\mathcal T,t}.
\]

Pozostaje jednak pytanie dynamiczne:

> czy po otrzymaniu nowej pary eksperyment/wynik klasę historii można aktualizować bez wyboru reprezentanta?

To wymaga kongruencji przyszłościowej równoważności względem legalnego rozszerzenia historii i prowadzi do II.9.
