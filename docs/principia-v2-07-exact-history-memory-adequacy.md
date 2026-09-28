# PRINCIPIA SEMANTICA — TOM II
## II.7. Dokładna adekwatność pamięci historii

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md` z zachowanymi C42 oraz C57–C59  
**Mapa twierdzeń:** `principia-v2-theorem-map-02.md`, II.7  
**Zależność:** specjalizacja Twierdzenia II.4 do przestrzeni historii, po jawnej definicji przyszłościowej równoważności C57/C58.  
**Regresja:** R02 Go; LAZARUS jako świadek bieżącego włókna niewystarczającego dla przyszłej semantyki.

---

## 1. Typy i tłumienie indeksu kontraktu

Ustalamy kontrakt \(c\) oraz chwilę \(t\). Niech

\[
\mathcal H_t
\]

będzie przestrzenią legalnych historii do chwili \(t\).

Pełna notacja może mieć postać

\[
\mathcal H_{c,t},
\qquad
\operatorname{Beh}_{\mathcal T,c,t}(H),
\qquad
\equiv_{\mathcal T,c,t},
\]

ale zgodnie z I.4 tłumimy indeks \(c\), gdy kontrakt jest ustalony.

Nie zakładamy, że \(\mathcal H_t\) jest minimalną reprezentacją pamięci. Jest przestrzenią odniesienia zawierającą co najmniej strukturę potrzebną do zdefiniowania legalnych przyszłych rozszerzeń.

---

## 2. Przyszłe drzewo zadaniowe

Dla historii \(H\in\mathcal H_t\) definiujemy

\[
\operatorname{Beh}_{\mathcal T}(H)
\]

jako ukorzenione drzewo wszystkich legalnych przyszłych rozszerzeń \(H\), w którym:

1. korzeń reprezentuje bieżącą historię;
2. krawędzie niosą literalne etykiety przejścia zadeklarowane przez kontrakt, np. parę eksperyment/wynik;
3. węzły niosą etykiety zadaniowe wymagane przez kontrakt;
4. relacja rodzic–dziecko odpowiada legalnemu rozszerzeniu historii.

Nie jest to drzewo wszystkich ontologicznie możliwych przyszłości. Jest obiektem kontraktowym.

---

## 3. Przyszłościowa równoważność historii

### Definicja II.7.1

Dla \(H,H'\in\mathcal H_t\) definiujemy

\[
\boxed{
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H')
}
\]

przez izomorfizm zachowujący korzeń, etykiety węzłów, etykiety krawędzi i relację rodzic–dziecko.

Dwie różne historie mogą więc być równoważne, jeżeli żadna ich różnica nie zmienia już przyszłej semantyki zadania.

---

## 4. Lemat II.7.A — relacja równoważności

Relacja \(\equiv_{\mathcal T,t}\) jest relacją równoważności na \(\mathcal H_t\).

**Dowód.** Refleksyjność daje identyczność drzewa \(\operatorname{Beh}_{\mathcal T}(H)\). Symetrię daje odwrotność izomorfizmu. Przechodniość daje złożenie dwóch izomorfizmów zachowujących korzeń, etykiety i relację rodzic–dziecko. Zatem relacja jest refleksyjna, symetryczna i przechodnia. \(\square\)

Dowód nie wymaga skończonego horyzontu przyszłości.

---

## 5. Pamięć jako reprezentacja historii

Niech

\[
\rho_t:\mathcal H_t\to Z_t
\]

będzie dowolną jawnie otypowaną reprezentacją pamięci.

Może kodować bieżący stan, część historii, zbiór zdarzeń, stan automatu, klasę abstrakcji albo inną strukturę. Nie zakładamy jej skończoności, minimalności, obliczalności ani surjektywności.

Jej jądro równoważności ma postać

\[
\ker_{\rm eq}\rho_t
=
\{(H,H')\in\mathcal H_t^2:\rho_t(H)=\rho_t(H')\}.
\]

---

## 6. Twierdzenie II.7 — dokładna adekwatność pamięci historii

Reprezentacja

\[
\rho_t:\mathcal H_t\to Z_t
\]

jest dokładnie adekwatna względem przyszłej semantyki zadania wtedy i tylko wtedy, gdy

\[
\boxed{
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

Równoważnie, dla projekcji

\[
q_{\mathcal T,t}:
\mathcal H_t
\to
M_{\mathcal T,t}
:=
\mathcal H_t/\!\equiv_{\mathcal T,t}
\]

zachodzi

\[
\boxed{
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}
\iff
\exists!\,f_t:\operatorname{im}\rho_t\to M_{\mathcal T,t},
\qquad
q_{\mathcal T,t}=f_t\circ\rho_t.
}
\]

Unikalność \(f_t\) obowiązuje wyłącznie na \(\operatorname{im}\rho_t\).

### Dowód

Z Lematu II.7.A relacja \(\equiv_{\mathcal T,t}\) jest relacją równoważności na \(\mathcal H_t\). Stosujemy więc Twierdzenie II.4 do

\[
\Omega=\mathcal H_t,
\qquad
E_{\mathcal T}=\equiv_{\mathcal T,t},
\qquad
\rho=\rho_t.
\]

Otrzymujemy dokładnie podaną równoważność i faktoryzację. \(\square\)

---

## 7. Najkrótszy falsyfikator pamięci

Jedna para historii \(H,H'\in\mathcal H_t\) spełniająca

\[
\rho_t(H)=\rho_t(H')
\]

oraz

\[
H\not\equiv_{\mathcal T,t}H'
\]

wystarcza do wykazania

\[
\ker_{\rm eq}\rho_t
\not\subseteq
\equiv_{\mathcal T,t}.
\]

Taka pamięć jest za gruba dla zadania.

---

## 8. Bieżący stan nie jest z definicji pamięcią wystarczającą

Niech

\[
s_t:\mathcal H_t\to X_t
\]

będzie dowolną jawnie otypowaną reprezentacją bieżącego stanu. Może zachodzić

\[
s_t(H)=s_t(H')
\]

przy jednoczesnym

\[
H\not\equiv_{\mathcal T,t}H'.
\]

Wtedy \(s_t\) nie jest wystarczającą pamięcią zadaniową.

W świadku LAZARUS używamy dodatkowo mapy

\[
F_t:\mathcal H_t\to\mathcal P(X_t),
\]

gdzie \(F_t(H)\) jest bieżącym włóknem świata indukowanym przez historię. Może zachodzić

\[
F_t(H)=F_t(H')
\]

przy

\[
H\not\equiv_{\mathcal T,t}H'.
\]

To jest dokładny sens świadka LAZARUS. Nie ustanawia on nowego prymitywu „sprawczości”; wykazuje niewystarczalność wybranej reprezentacji pamięci.

---

## 9. R02 — Go jako regres pamięci

W regresie Go kolejne reprezentacje pamięci były testowane względem różnych kontraktów reguł:

\[
(B_t,\sigma_t),
\qquad
(B_t,\sigma_t,B_{t-1}),
\qquad
(B_t,\sigma_t,V_t),
\qquad
(B_t,\sigma_t,U_t).
\]

Każda jest oceniana przez ten sam warunek

\[
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
\]

Jeżeli po zmianie reguły istnieją dwie historie o tej samej reprezentacji, ale różnej legalności przyszłego ruchu, otrzymujemy bezpośredni kontrprzykład do adekwatności tej pamięci.

Sekwencja Go nie jest uniwersalną hierarchią pamięci; odpowiada różnym kontraktom zadaniowym.

---

## 10. Pełna historia nie jest twierdzeniem o minimalnej pamięci

Twierdzenie II.7 nie mówi, że należy przechowywać pełną historię. Dopuszcza każdą kompresję \(\rho_t\), która spełnia

\[
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
\]

Nie wynika z niego minimalność liczby bitów, liczby stanów implementacji, wymiaru reprezentacji, kosztu pamięci, kosztu aktualizacji ani czasu obliczeń. Te własności wymagają dodatkowej struktury kosztowej lub algorytmicznej.

---

## 11. Dokładna pamięć może być nadmiarowa

Jeżeli

\[
\ker_{\rm eq}\rho_t^{(1)}
\subseteq
\ker_{\rm eq}\rho_t^{(2)}
\subseteq
\equiv_{\mathcal T,t},
\]

to obie reprezentacje są dokładnie adekwatne, lecz \(\rho_t^{(1)}\) zachowuje więcej rozróżnień historycznych niż wymaga zadanie.

Adekwatność nie jest więc równoznaczna z maksymalną kompresją.

---

## 12. Status źródłowy

Definicja przyszłego drzewa i relacji \(\equiv_{\mathcal T,t}\) jest bieżącą migracją RED-1 zapisaną jako C57. Fakt, że jest to relacja równoważności, jest C58. Kryterium pamięci C42 jest specjalizacją ogólnego kryterium adekwatności reprezentacji II.4.

\[
\boxed{
\text{RED-1 FUTURE-TASK DEFINITION}
\; + \;
\text{CLASSICAL FACTORIZATION SPECIALIZATION / PSI HISTORY BRIDGE}.
}
\]

PSI nie rości sobie autorstwa abstrakcyjnej teorii relacji równoważności ani lematu faktoryzacyjnego. Właściwą treścią tej warstwy jest wybór przyszłego drzewa zadaniowego jako kryterium tego, które różnice historyczne mogą zostać bezpiecznie zapomniane.

---

## 13. Granice II.7

Twierdzenie II.7 nie ustanawia jeszcze:

- że \(M_{\mathcal T,t}\) jest najgrubszym dokładnym ilorazem historii — to II.8;
- że klasy historii mają dobrze określoną rekurencyjną aktualizację — to II.9;
- że liczba klas jest skończona;
- że istnieje skończony automat realizujący pamięć;
- że reprezentacja jest bitowo minimalna;
- że aktualizacja jest obliczalna lub efektywna;
- że bieżący stan świata wystarcza bez testu C42;
- że reprezentacja wystarczająca dla jednego kontraktu pozostaje wystarczająca po zmianie zadania.

---

## 14. Przejście do II.8

Skoro \(\equiv_{\mathcal T,t}\) jest relacją równoważności, możemy utworzyć

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}.
\]

Twierdzenie II.7 mówi, kiedy dowolna pamięć zachowuje całą przyszłą informację zadaniową. Następny krok pyta o pozycję samego ilorazu \(M_{\mathcal T,t}\) w porządku wszystkich dokładnie wystarczających reprezentacji.

To będzie II.8 — najgrubszy dokładny iloraz historii.
