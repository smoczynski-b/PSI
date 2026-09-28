# PRINCIPIA SEMANTICA — TOM II
## II.9. Rekurencyjna aktualizacja ilorazu historii

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PENDING`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, z zachowanymi C45 oraz C59  
**Mapa twierdzeń:** `principia-v2-theorem-map-02.md`, II.9  
**Zależności:** II.6, II.7 i II.8.  
**Granica:** dobrze określona rekurencja matematyczna nie implikuje skończonej pamięci, obliczalności ani efektywności.

---

## 1. Typy i legalna dziedzina aktualizacji

Ustalamy kontrakt oraz chwilę \(t\). Niech

\[
\mathcal H_t
\]

będzie przestrzenią legalnych historii do chwili \(t\), a

\[
\mathcal E_t
\]

zbiorem dopuszczalnych etykiet eksperymentu/interwencji/ruchu w chwili \(t\). Niech

\[
\mathcal Y_{t+1}
\]

będzie zbiorem możliwych etykiet wyniku kolejnego kroku.

Legalność rozszerzenia nie musi być całkowita. Dlatego wprowadzamy jawnie

\[
\boxed{
D_t
\subseteq
\mathcal H_t\times\mathcal E_t\times\mathcal Y_{t+1}
}
\]

oraz częściową aktualizację historii

\[
\boxed{
\delta_t:D_t\to\mathcal H_{t+1}.
}
\]

Jeżeli

\[
(H,\varepsilon,y)\in D_t,
\]

to \(\delta_t(H,\varepsilon,y)\) jest historią po legalnym rozszerzeniu \(H\) etykietą \((\varepsilon,y)\).

To typowanie jest obowiązkowe: zapis \(\delta_t(H,\varepsilon,y)\) poza \(D_t\) nie ma znaczenia w tym kontrakcie.

---

## 2. Równoważność historii i własność kongruencji RED-1

Z II.7 mamy przyszłościową równoważność

\[
\equiv_{\mathcal T,t}
\]

na \(\mathcal H_t\), zdefiniowaną przez izomorfizm literalnie etykietowanych drzew przyszłości.

C59 zamraża dwie własności potrzebne do aktualizacji.

Jeżeli

\[
H\equiv_{\mathcal T,t}H',
\]

to dla każdej etykiety \((\varepsilon,y)\):

1. legalność tej etykiety jest zgodna między reprezentantami:
   \[
   (H,\varepsilon,y)\in D_t
   \iff
   (H',\varepsilon,y)\in D_t;
   \]
2. jeżeli rozszerzenie jest legalne, to następcy są przyszłościowo równoważni:
   \[
   \delta_t(H,\varepsilon,y)
   \equiv_{\mathcal T,t+1}
   \delta_t(H',\varepsilon,y).
   \]

Pierwszy punkt wynika z tego, że izomorfizm drzew zachowuje literalne etykiety krawędzi; drugi z izomorfizmu odpowiadających poddrzew następników.

To jest dokładna postać kongruencji potrzebna w warstwie historii.

---

## 3. Ilorazy historii

Definiujemy

\[
M_{\mathcal T,t}
=
\mathcal H_t/\!\equiv_{\mathcal T,t},
\qquad
q_{\mathcal T,t}:\mathcal H_t\to M_{\mathcal T,t}.
\]

Analogicznie

\[
M_{\mathcal T,t+1}
=
\mathcal H_{t+1}/\!\equiv_{\mathcal T,t+1}.
\]

Chcemy zdefiniować aktualizację bez potrzeby wybierania konkretnego reprezentanta historii.

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

Trzeba sprawdzić, że definicja nie zależy od wyboru reprezentanta \(H\).

Jeżeli

\[
H\equiv_{\mathcal T,t}H',
\]

to z własności C59

\[
(H,\varepsilon,y)\in D_t
\iff
(H',\varepsilon,y)\in D_t.
\]

Zatem członkostwo w \(\overline D_t\) jest dobrze określone na klasach.

---

## 5. Twierdzenie II.9 — rekurencyjna aktualizacja ilorazu historii

### Twierdzenie

Przy hipotezach z §1–§4 istnieje dokładnie jedna częściowa mapa

\[
\boxed{
U_{\mathcal T,t}:
\overline D_t
\to
M_{\mathcal T,t+1}
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

Jest ona dobrze określona niezależnie od wyboru reprezentanta \(H\).

### Dowód

Niech

\[
([H]_{\mathcal T,t},\varepsilon,y)
\in
\overline D_t.
\]

Z definicji dziedziny możemy wybrać reprezentanta \(H\) z

\[
(H,\varepsilon,y)\in D_t.
\]

Definiujemy

\[
U_{\mathcal T,t}
([H]_{\mathcal T,t},\varepsilon,y)
:=
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}.
\]

Niech teraz \(H'\) będzie innym reprezentantem tej samej klasy:

\[
H'\equiv_{\mathcal T,t}H.
\]

Z C59 legalność jest reprezentantowo niezmiennicza, więc

\[
(H',\varepsilon,y)\in D_t.
\]

Ponadto następcy spełniają

\[
\delta_t(H,\varepsilon,y)
\equiv_{\mathcal T,t+1}
\delta_t(H',\varepsilon,y).
\]

Stąd

\[
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}
=
[\delta_t(H',\varepsilon,y)]_{\mathcal T,t+1}.
\]

Wartość \(U_{\mathcal T,t}\) nie zależy więc od reprezentanta.

Unikalność jest natychmiastowa: każda mapa spełniająca podany wzór musi na każdej klasie i legalnej etykiecie przyjmować dokładnie klasę następcy określoną przez prawą stronę. \(\square\)

---

## 6. Diagram aktualizacji

Na legalnej dziedzinie mamy komutację

\[
\boxed{
q_{\mathcal T,t+1}
\bigl(\delta_t(H,\varepsilon,y)\bigr)
=
U_{\mathcal T,t}
\bigl(q_{\mathcal T,t}(H),\varepsilon,y\bigr).
}
\]

Jest to odpowiednik Twierdzenia II.6 dla czasowo zmiennej przestrzeni historii i częściowej aktualizacji z jawną etykietą kroku.

Nie jest to nowy prymityw. Jest to zejście legalnej aktualizacji historii na zadaniowy iloraz historii.

---

## 7. Dlaczego częściowość jest istotna

Nie każda para \((\varepsilon,y)\) musi być legalna po każdej historii. Legalność może zależeć od:

- reguł gry;
- poprzednich interwencji;
- stanu operacyjnego;
- ograniczeń domeny;
- protokołu eksperymentalnego;
- innych warunków kontraktu.

Dlatego zapis całkowitej mapy

\[
M_{\mathcal T,t}\times\mathcal E_t\times\mathcal Y_{t+1}
\to
M_{\mathcal T,t+1}
\]

byłby zbyt mocny bez dodatkowej hipotezy totalności.

---

## 8. Relacja do II.6

II.6 mówiło, że dla stałej przestrzeni i deterministycznej mapy \(\delta:\Omega\to\Omega\) zejście na iloraz wymaga kongruencji

\[
xEy\Rightarrow\delta(x)E\delta(y).
\]

II.9 jest wersją historii, w której:

- przestrzeń zmienia się z \(\mathcal H_t\) do \(\mathcal H_{t+1}\);
- aktualizacja jest częściowa;
- krok ma jawne etykiety \((\varepsilon,y)\);
- trzeba kontrolować zarówno dziedzinę, jak i klasę następcy.

Nie wolno więc traktować II.9 jako mechanicznego przepisania II.6 bez typowania dziedziny.

---

## 9. Matematyczna rekurencja nie oznacza skończonej pamięci

Z istnienia \(U_{\mathcal T,t}\) wynika, że zadaniową klasę historii można aktualizować matematycznie bez odtwarzania konkretnego reprezentanta historii.

Nie wynika jednak:

\[
|M_{\mathcal T,t}|<\infty.
\]

Nie wynika również:

- skończona liczba stanów implementacji;
- skończona liczba bitów;
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

W regułach Go legalność następnego ruchu może zależeć od historii. Jeżeli pamięć skleja dwie historie, dla których ta sama etykieta ruchu jest legalna w jednej, a nielegalna w drugiej, nie da się nawet dobrze określić dziedziny aktualizacji na klasie pamięci.

Jeżeli ruch jest legalny w obu, ale prowadzi do przyszłości zadaniowo różnych, wartość aktualizacji również nie jest dobrze określona.

R02 testuje więc oba warunki:

\[
\boxed{
\text{legalność etykiety}
\quad+\quad
\text{równoważność następcy}.
}
\]

Nie jest dowodem Twierdzenia II.9; jest jego skończonym regressem zastosowania.

---

## 11. Status źródłowy

C59 pochodzi z migracji RED-1 i ustanawia kongruencję literalnie etykietowanego przyszłego drzewa dla legalnego rozszerzenia historii. C45 zapisuje wynik jako rekurencyjną aktualizację zadaniowego ilorazu historii.

Status:

\[
\boxed{
\text{RED-1 CONGRUENCE RESULT}
\; + \;
\text{CLASSICAL QUOTIENT-UPDATE PRINCIPLE / PSI HISTORY BRIDGE}.
}
\]

PSI nie rości sobie autorstwa abstrakcyjnej zasady schodzenia kongruentnej aktualizacji na iloraz. Specyficzna treść PSI polega na wyborze przyszłej semantyki zadania i literalnie etykietowanej legalnej historii jako obiektu, względem którego wolno zapominać przeszłość.

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

Każda z tych własności wymaga osobnej hipotezy.

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
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t},
\]

\[
M_{\mathcal T,t}
=
\mathcal H_t/\!\equiv_{\mathcal T,t},
\]

\[
U_{\mathcal T,t}
([H_t],\varepsilon_t,y_{t+1})
=
[\delta_t(H_t,\varepsilon_t,y_{t+1})]_{\mathcal T,t+1}.
\]

Po II.9 własna warstwa quotient/history PSI jest gotowa do porównania z klasycznymi konstrukcjami: lumpowalnością, Myhill–Nerode oraz algorytmicznym refinementem partycji.
