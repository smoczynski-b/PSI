# PRINCIPIA SEMANTICA — TOM II
## II.9. Rekurencyjna aktualizacja ilorazu historii

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, z zachowanymi C45 oraz C59  
**Mapa twierdzeń:** `principia-v2-theorem-map-02.md`, II.9  
**Zależności:** II.6, II.7 i II.8.  
**Granica:** dobrze określona rekurencja matematyczna nie implikuje skończonej pamięci, obliczalności ani efektywności.

---

## 1. Typy i legalna dziedzina aktualizacji

Ustalamy kontrakt oraz chwilę \(t\). Niech \(\mathcal H_t\) będzie przestrzenią legalnych historii do chwili \(t\), \(\mathcal E_t\) zbiorem dopuszczalnych etykiet eksperymentu/interwencji/ruchu, a \(\mathcal Y_{t+1}\) zbiorem możliwych etykiet wyniku kolejnego kroku.

Legalność rozszerzenia nie musi być całkowita. Wprowadzamy więc

\[
\boxed{
D_t\subseteq\mathcal H_t\times\mathcal E_t\times\mathcal Y_{t+1}
}
\]

oraz aktualizację

\[
\boxed{\delta_t:D_t\to\mathcal H_{t+1}.}
\]

Jeżeli \((H,\varepsilon,y)\in D_t\), to \(\delta_t(H,\varepsilon,y)\) jest historią po legalnym rozszerzeniu \(H\) etykietą \((\varepsilon,y)\). Zapis poza \(D_t\) nie ma znaczenia w tym kontrakcie.

---

## 2. Kongruencja RED-1

Z II.7 mamy przyszłościową równoważność \(\equiv_{\mathcal T,t}\) na \(\mathcal H_t\), zdefiniowaną przez izomorfizm literalnie etykietowanych drzew przyszłości.

C59 daje dokładnie dwie własności potrzebne do aktualizacji. Jeżeli

\[
H\equiv_{\mathcal T,t}H',
\]

to dla każdej etykiety \((\varepsilon,y)\):

\[
\boxed{
(H,\varepsilon,y)\in D_t
\iff
(H',\varepsilon,y)\in D_t
}
\]

oraz — gdy rozszerzenie jest legalne —

\[
\boxed{
\delta_t(H,\varepsilon,y)
\equiv_{\mathcal T,t+1}
\delta_t(H',\varepsilon,y).
}
\]

Pierwsza własność wynika z zachowania literalnych etykiet krawędzi; kierunek odwrotny otrzymujemy, stosując tę samą własność do symetrycznej relacji \(H'\equiv_{\mathcal T,t}H\). Druga wynika z izomorfizmu odpowiadających poddrzew następników.

---

## 3. Ilorazy historii

Definiujemy

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t},
\qquad
q_{\mathcal T,t}:\mathcal H_t\to M_{\mathcal T,t},
\]

oraz analogicznie \(M_{\mathcal T,t+1}\).

Celem jest zdefiniowanie aktualizacji klas, której **wartość i legalna dziedzina nie zależą od wyboru reprezentanta historii**.

---

## 4. Dziedzina częściowej aktualizacji ilorazowej

Definiujemy

\[
\boxed{
\overline D_t
\subseteq
M_{\mathcal T,t}\times\mathcal E_t\times\mathcal Y_{t+1}
}
\]

przez

\[
\boxed{
([H]_{\mathcal T,t},\varepsilon,y)\in\overline D_t
\iff
(H,\varepsilon,y)\in D_t.
}
\]

Definicja jest reprezentantowo niezmiennicza, ponieważ dla \(H\equiv_{\mathcal T,t}H'\)

\[
(H,\varepsilon,y)\in D_t
\iff
(H',\varepsilon,y)\in D_t.
\]

---

## 5. Twierdzenie II.9 — rekurencyjna aktualizacja ilorazu historii

Przy powyższych hipotezach istnieje dokładnie jedna mapa

\[
\boxed{
U_{\mathcal T,t}:\overline D_t\to M_{\mathcal T,t+1}
}
\]

spełniająca

\[
\boxed{
U_{\mathcal T,t}
([H]_{\mathcal T,t},\varepsilon,y)
=
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}.
}
\]

### Dowód

Niech \(([H]_{\mathcal T,t},\varepsilon,y)\in\overline D_t\). Wybierzmy reprezentanta \(H\) z \((H,\varepsilon,y)\in D_t\) i zdefiniujmy prawą stronę wzoru.

Jeżeli \(H'\equiv_{\mathcal T,t}H\), to z C59

\[
(H',\varepsilon,y)\in D_t
\]

oraz

\[
\delta_t(H,\varepsilon,y)
\equiv_{\mathcal T,t+1}
\delta_t(H',\varepsilon,y).
\]

Zatem

\[
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}
=
[\delta_t(H',\varepsilon,y)]_{\mathcal T,t+1}.
\]

Wartość nie zależy od reprezentanta. Unikalność jest natychmiastowa: każda mapa spełniająca podany wzór musi na każdej klasie i legalnej etykiecie przyjmować klasę zadaniową odpowiedniego następcy. \(\square\)

---

## 6. Diagram aktualizacji

Na legalnej dziedzinie zachodzi

\[
\boxed{
q_{\mathcal T,t+1}
\bigl(\delta_t(H,\varepsilon,y)\bigr)
=
U_{\mathcal T,t}
\bigl(q_{\mathcal T,t}(H),\varepsilon,y\bigr).
}
\]

Jest to czasowo zmienna i częściowa wersja zejścia dynamiki na iloraz z II.6.

---

## 7. Dlaczego częściowość jest istotna

Nie każda para \((\varepsilon,y)\) musi być legalna po każdej historii. Legalność może zależeć od reguł gry, wcześniejszych interwencji, stanu operacyjnego, ograniczeń domeny lub protokołu.

Dlatego zapis całkowitej mapy

\[
M_{\mathcal T,t}\times\mathcal E_t\times\mathcal Y_{t+1}
\to
M_{\mathcal T,t+1}
\]

byłby zbyt mocny bez dodatkowej hipotezy totalności.

---

## 8. Relacja do II.6

II.6 dotyczyło mapy \(\delta:\Omega\to\Omega\) na stałej przestrzeni. W II.9:

- przestrzeń zmienia się z \(\mathcal H_t\) do \(\mathcal H_{t+1}\);
- aktualizacja jest częściowa;
- krok ma jawne etykiety \((\varepsilon,y)\);
- trzeba kontrolować zarówno dziedzinę, jak i klasę następcy.

Nie jest to więc mechaniczne przepisanie II.6 bez typowania dziedziny.

---

## 9. Rekurencja abstrakcyjna a implementacja

Z istnienia \(U_{\mathcal T,t}\) wynika, że **na poziomie matematycznym** istnieje reprezentantowo niezależna aktualizacja klas zadaniowych.

Nie wynika z tego, że istnieje algorytm obliczający \(U_{\mathcal T,t}\) bez dostępu do reprezentanta historii ani że rozpoznawanie klas \(\equiv_{\mathcal T,t}\) jest efektywne lub w ogóle obliczalne.

W szczególności nie wynika:

\[
|M_{\mathcal T,t}|<\infty,
\]

ani:

- skończona liczba bitów lub stanów implementacji;
- efektywna procedura rozpoznawania klasy;
- obliczalność \(U_{\mathcal T,t}\);
- tania aktualizacja online;
- istnienie skończonego automatu;
- stabilność numeryczna.

Dlatego

\[
\boxed{
\text{rekurencyjność matematyczna}
\not\Rightarrow
\text{skończona lub efektywna pamięć}.
}
\]

---

## 10. R02 Go jako regres dziedziny i następcy

Jeżeli kandydacka pamięć skleja dwie historie, dla których ta sama etykieta ruchu jest legalna w jednej, a nielegalna w drugiej, nie da się dobrze określić dziedziny aktualizacji na klasie tej pamięci.

Jeżeli etykieta jest legalna w obu, ale następcy mają różną przyszłą semantykę zadania, nie jest dobrze określona wartość aktualizacji.

R02 testuje więc dwa warunki:

\[
\boxed{
\text{legalność etykiety}
\quad+\quad
\text{równoważność następcy}.
}
\]

Jest regressem zastosowania, nie dowodem Twierdzenia II.9.

---

## 11. Status źródłowy

C59 pochodzi z migracji RED-1 i ustanawia kongruencję literalnie etykietowanego przyszłego drzewa dla legalnego rozszerzenia historii. C45 zapisuje wynik jako rekurencyjną aktualizację zadaniowego ilorazu historii.

\[
\boxed{
\text{RED-1 CONGRUENCE RESULT}
\; + \;
\text{CLASSICAL QUOTIENT-UPDATE PRINCIPLE / PSI HISTORY BRIDGE}.
}
\]

PSI nie rości sobie autorstwa abstrakcyjnej zasady schodzenia kongruentnej aktualizacji na iloraz.

---

## 12. Czego Twierdzenie II.9 nie ustanawia

Nie ustanawia automatycznie:

- skończoności \(M_{\mathcal T,t}\);
- obliczalności relacji \(\equiv_{\mathcal T,t}\);
- obliczalności lub efektywności \(U_{\mathcal T,t}\);
- implementacyjnej minimalności pamięci;
- stabilności na szum;
- lumpowalności stochastycznej;
- stacjonarności w czasie;
- istnienia jednego stałego zbioru stanów dla wszystkich \(t\).

---

## 13. Domknięcie własnej warstwy historii

II.7–II.9 dają kolejno:

\[
\boxed{
\text{adekwatność pamięci}
\to
\text{najgrubszy dokładny iloraz historii}
\to
\text{dobrze określoną częściową aktualizację ilorazową}.
}
\]

W symbolach:

\[
\ker_{\rm eq}\rho_t\subseteq\equiv_{\mathcal T,t},
\]

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t},
\]

\[
U_{\mathcal T,t}
([H_t],\varepsilon_t,y_{t+1})
=
[\delta_t(H_t,\varepsilon_t,y_{t+1})]_{\mathcal T,t+1}.
\]

Po II.9 własna warstwa quotient/history PSI jest gotowa do porównania z klasycznymi konstrukcjami: lumpowalnością, Myhill–Nerode oraz algorytmicznym refinementem partycji.
