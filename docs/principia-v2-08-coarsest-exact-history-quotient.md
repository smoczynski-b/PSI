# PRINCIPIA SEMANTICA — TOM II
## II.8. Najgrubszy dokładny iloraz historii

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, z zachowanym C44 z `claim-registry-09.md`  
**Mapa twierdzeń:** `principia-v2-theorem-map-02.md`, II.8  
**Zależności:** II.2 oraz II.7.  
**Granice:** najgrubszy dokładny iloraz w porządku ilorazów ≠ minimalna implementacja bitowa, wymiarowa, pamięciowa lub obliczeniowa; porządek reprezentacji dotyczy `im rho_t`, nie nieużywanej części przeciwdziedziny.

---

## 1. Punkt wyjścia

Ustalamy kontrakt oraz chwilę \(t\). Niech \(\mathcal H_t\) będzie przestrzenią legalnych historii, a

\[
\equiv_{\mathcal T,t}
\]

przyszłościową równoważnością zadaniową z II.7. Z Lematu II.7.A jest to relacja równoważności.

Definiujemy

\[
\boxed{
M_{\mathcal T,t}:=\mathcal H_t/\!\equiv_{\mathcal T,t}
}
\]

oraz

\[
q_{\mathcal T,t}:\mathcal H_t\to M_{\mathcal T,t},
\qquad
q_{\mathcal T,t}(H)=[H]_{\mathcal T,t}.
\]

Iloraz usuwa dokładnie te rozróżnienia historyczne, które nie zmieniają przyszłej semantyki zadania.

---

## 2. Porządek informacyjny

Dla reprezentacji

\[
\rho_1:\mathcal H_t\to Z_1,
\qquad
\rho_2:\mathcal H_t\to Z_2
\]

mówimy, że \(\rho_1\) jest informacyjnie drobniejsza od \(\rho_2\), gdy

\[
\boxed{
\ker_{\rm eq}\rho_1\subseteq\ker_{\rm eq}\rho_2.
}
\]

Im mniejsze jądro równoważności, tym więcej par historii reprezentacja nadal rozróżnia.

Z II.7 każda dokładnie adekwatna pamięć spełnia

\[
\boxed{
\ker_{\rm eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
}
\]

A zatem każda dokładna pamięć jest informacyjnie co najmniej tak drobna jak kanoniczny iloraz zadaniowy.

---

## 3. Twierdzenie II.8 — faktoryzacja każdej dokładnej pamięci

### Twierdzenie

Jeżeli

\[
\rho_t:\mathcal H_t\to Z_t
\]

jest dokładnie adekwatna, tj.

\[
\ker_{\rm eq}\rho_t\subseteq\equiv_{\mathcal T,t},
\]

to istnieje dokładnie jedna mapa

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

Istnienie i unikalność na \(\operatorname{im}\rho_t\) wynikają z II.7, czyli z kryterium faktoryzacji II.2 zastosowanego do przestrzeni historii.

Dla dowolnej klasy \([H]_{\mathcal T,t}\in M_{\mathcal T,t}\):

\[
[H]_{\mathcal T,t}
=q_{\mathcal T,t}(H)
=f_t(\rho_t(H)),
\]

więc \(f_t\) jest surjektywna. \(\square\)

**Rygiel F60.** Twierdzenie porównuje \(M_{\mathcal T,t}\) z \(\operatorname{im}\rho_t\). Punkty przeciwdziedziny

\[
Z_t\setminus\operatorname{im}\rho_t
\]

nie reprezentują żadnej historii i nie uczestniczą w porządku informacyjnym ani w roszczeniu o minimalność.

---

## 4. Ilorazy przez relacje równoważności

Niech \(Q\) będzie relacją równoważności na \(\mathcal H_t\) oraz

\[
q_Q:\mathcal H_t\to\mathcal H_t/Q.
\]

Iloraz \(q_Q\) jest dokładnie zadaniowo adekwatny wtedy i tylko wtedy, gdy

\[
\boxed{
Q\subseteq\equiv_{\mathcal T,t}.
}
\]

Wtedy istnieje jednoznaczna surjekcja

\[
\pi_Q:\mathcal H_t/Q\to M_{\mathcal T,t}
\]

spełniająca

\[
\boxed{
q_{\mathcal T,t}=\pi_Q\circ q_Q,
}
\]

a jawnie

\[
\pi_Q([H]_Q)=[H]_{\mathcal T,t}.
\]

Dobra określoność jest równoważna temu, że \(Q\) nie skleja par rozróżnianych przez \(\equiv_{\mathcal T,t}\).

---

## 5. Najgrubszy dokładny iloraz

Niech

\[
\mathfrak Q_{\mathcal T,t}
=
\{Q:\ Q\text{ jest relacją równoważności na }\mathcal H_t,
\ Q\subseteq\equiv_{\mathcal T,t}\}.
\]

W porządku inkluzji relacji większe \(Q\) skleja więcej par i daje grubszy iloraz. Sama relacja

\[
\equiv_{\mathcal T,t}
\]

należy do \(\mathfrak Q_{\mathcal T,t}\) i zawiera każdy jego element. Zatem

\[
\boxed{
\equiv_{\mathcal T,t}=\max\mathfrak Q_{\mathcal T,t}.
}
\]

Równoważnie:

\[
\boxed{
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}
}
\]

jest **najgrubszym dokładnym ilorazem historii** względem zadania.

Każdy dokładny iloraz \(\mathcal H_t/Q\) zachowuje co najmniej tyle rozróżnień, ile \(M_{\mathcal T,t}\), i posiada kanoniczną surjekcję

\[
\mathcal H_t/Q\twoheadrightarrow M_{\mathcal T,t}.
\]

---

## 6. Dowolna reprezentacja jako iloraz przez jądro

Dla dowolnej reprezentacji

\[
\rho_t:\mathcal H_t\to Z_t
\]

istnieje kanoniczna bijekcja

\[
\boxed{
\mathcal H_t/\ker_{\rm eq}\rho_t
\cong
\operatorname{im}\rho_t
}
\]

dana przez

\[
[H]_{\ker\rho_t}\longmapsto\rho_t(H).
\]

Jeżeli \(\rho_t\) jest dokładna, to

\[
\ker_{\rm eq}\rho_t\subseteq\equiv_{\mathcal T,t},
\]

więc otrzymujemy

\[
\mathcal H_t
\to
\mathcal H_t/\ker_{\rm eq}\rho_t
\cong
\operatorname{im}\rho_t
\xrightarrow{f_t}
M_{\mathcal T,t}.
\]

To formalizuje nadmiar informacji: dokładna pamięć może zachowywać więcej rozróżnień niż wymaga zadanie, a \(M_{\mathcal T,t}\) usuwa dokładnie ten nadmiar.

---

## 7. Kanoniczność nie oznacza jedynego kodowania

Nie należy mówić, że \(M_{\mathcal T,t}\) jest jedyną minimalną reprezentacją w sensie dosłownej równości kodów.

Jeżeli

\[
b:M_{\mathcal T,t}\to Z
\]

jest bijekcją, to

\[
\rho_t=b\circ q_{\mathcal T,t}
\]

ma to samo jądro:

\[
\ker_{\rm eq}\rho_t=\equiv_{\mathcal T,t}.
\]

Istnieje więc wiele bijektywnych przekodowań tej samej najgrubszej informacji zadaniowej. Kanoniczny jest iloraz wyznaczony przez relację \(\equiv_{\mathcal T,t}\), nie szczególny alfabet, numeracja klas ani fizyczny format pamięci.

---

## 8. Zakres minimalności

Twierdzenie II.8 ustanawia minimalność wyłącznie w porządku informacyjnym/ilorazowym. Nie ustanawia automatycznie minimalności:

- liczby bitów;
- wymiaru kodu;
- rozmiaru struktur danych;
- kosztu pamięci fizycznej;
- kosztu aktualizacji;
- czasu obliczeń;
- złożoności algorytmicznej;
- wygody implementacji.

Dla skończonej dokładnej reprezentacji surjekcja

\[
f_t:\operatorname{im}\rho_t\twoheadrightarrow M_{\mathcal T,t}
\]

daje

\[
|M_{\mathcal T,t}|\le|\operatorname{im}\rho_t|,
\]

ale minimalna liczba klas nadal nie jest tym samym co minimalny koszt kodowania lub aktualizacji.

---

## 9. Falsyfikator

Jeżeli proponowany dokładny iloraz przez \(Q\) zawiera parę

\[
H Q H'
\]

z

\[
H\not\equiv_{\mathcal T,t}H',
\]

to

\[
Q\not\subseteq\equiv_{\mathcal T,t}
\]

i iloraz jest za gruby. Nie istnieje wówczas mapa

\[
\pi_Q:\mathcal H_t/Q\to M_{\mathcal T,t}
\]

spełniająca

\[
q_{\mathcal T,t}=\pi_Q\circ q_Q.
\]

Jeden taki świadek wystarcza.

---

## 10. Relacja do Go i LAZARUS

Go pokazuje reprezentacje, które przy zmianie kontraktu mogą stać się zbyt grube albo nadal wystarczające. II.8 nie przypisuje żadnej konkretnej reprezentacji Go statusu uniwersalnie minimalnej.

LAZARUS pokazuje przypadki, w których bieżące włókno świata ma jądro większe niż dopuszcza przyszła równoważność zadaniowa; wtedy nie jest nawet dokładną reprezentacją pamięci.

Oba przypadki są regresami zakresu, nie dowodami Twierdzenia II.8.

---

## 11. Status źródłowy

C44 łączy klasyczną faktoryzację przez jądro z przyszłościową równoważnością zadaniową RED-1.

\[
\boxed{
\text{CLASSICAL FACTORIZATION / QUOTIENT ORDER}
\; + \;
\text{PSI TASK-HISTORY BRIDGE}.
}
\]

PSI nie rości sobie autorstwa ogólnej teorii ilorazów. Treścią tej warstwy jest wskazanie \(\equiv_{\mathcal T,t}\) jako maksymalnego dopuszczalnego sklejenia historii, które zachowuje całą przyszłą semantykę zadania.

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

II.8 odpowiada na pytanie o najgrubszy dokładny iloraz historii:

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}.
\]

Pozostaje pytanie dynamiczne: czy po nowej parze eksperyment/wynik klasę historii można aktualizować bez wyboru reprezentanta? To wymaga kongruencji przyszłościowej równoważności względem legalnego rozszerzenia historii i prowadzi do II.9.
