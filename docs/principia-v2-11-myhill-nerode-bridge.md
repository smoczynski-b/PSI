# PRINCIPIA SEMANTICA — TOM II
## II.11. Równoważność Myhilla–Nerode’a jako dokładny iloraz przyszłych testów

**Status:** `CLASSICAL THEOREM / EXACT PSI REALIZATION / PROSE PASS 01 / LOCAL CROSS-CHECK PASS`  
**Źródło nadrzędne PSI:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, zachowane C18  
**Mapa porównawcza:** `classical-compare-01.md`  
**Zależności PSI:** I.4 / II.7–II.8 jako ogólna architektura przyszłych testów i ilorazu; identyczność z Nerode’em jest wyprowadzana bezpośrednio z kontraktu językowego  
**Źródła klasyczne:** J. Myhill, *Finite Automata and the Representation of Events* (1957); A. Nerode, “Linear Automaton Transformations”, *Proceedings of the AMS* 9 (1958), 541–544.  
**Zakres:** język \(L\subseteq\Sigma^*\) nad skończonym alfabetem; wszystkie prawostronne kontynuacje jako dopuszczalne przyszłe testy; deterministyczna akceptacja.

---

## 1. Kontrakt językowy

Niech \(\Sigma\) będzie skończonym alfabetem i

\[
L\subseteq\Sigma^*
\]

językiem.

Przestrzenią kandydatów/historii jest

\[
\boxed{\Omega_L=\Sigma^*.}
\]

Dla każdego słowa \(w\in\Sigma^*\) definiujemy prawostronny transport

\[
T_w:\Sigma^*\to\Sigma^*,
\qquad
T_w(u)=uw.
\]

Zadaniową obserwablą bazową jest wskaźnik akceptacji

\[
A_L:\Sigma^*\to\{0,1\},
\qquad
A_L(u)=\mathbf 1_L(u).
\]

Kontrakt dopuszcza jako przyszłe eksperymenty **wszystkie** kontynuacje \(w\in\Sigma^*\). Dlatego domknięcie zadaniowe zawiera rodzinę

\[
\boxed{
R_w=A_L\circ T_w,
\qquad
R_w(u)=\mathbf 1_L(uw),
\qquad w\in\Sigma^*.
}
\]

To „wszystkie” jest hipotezą istotną. Ograniczony zbiór kontynuacji definiuje inną relację zadaniową.

---

## 2. Klasyczna równoważność Nerode’a

Definiujemy

\[
\boxed{
u\equiv_L v
\iff
\forall w\in\Sigma^*:
uw\in L
\Longleftrightarrow
vw\in L.
}
\]

Dwa prefiksy są równoważne dokładnie wtedy, gdy żadna prawostronna kontynuacja nie potrafi rozdzielić ich ze względu na późniejszą akceptację.

---

## 3. Twierdzenie II.11.A — dokładna identyczność PSI/Nerode

Dla powyższego kontraktu językowego zadaniowa relacja PSI

\[
E_{\mathcal T,L}
=
\bigcap_{w\in\Sigma^*}\ker_{eq}R_w
\]

jest dokładnie równoważnością Nerode’a:

\[
\boxed{
E_{\mathcal T,L}
=
\equiv_L.
}
\]

### Dowód

Dla \(u,v\in\Sigma^*\):

\[
\begin{aligned}
uE_{\mathcal T,L}v
&\iff
\forall w\in\Sigma^*:\ R_w(u)=R_w(v)\\
&\iff
\forall w\in\Sigma^*:\ \mathbf 1_L(uw)=\mathbf 1_L(vw)\\
&\iff
\forall w\in\Sigma^*:\ uw\in L\Longleftrightarrow vw\in L\\
&\iff
u\equiv_L v.
\end{aligned}
\]

Zatem relacje są identyczne. \(\square\)

Nie jest to nowe twierdzenie o językach formalnych. Jest to dokładne osadzenie klasycznej relacji w architekturze PSI po jawnej specyfikacji rodziny testów przyszłości.

---

## 4. Iloraz zadaniowy

Z Twierdzenia II.11.A:

\[
\boxed{
M_{\mathcal T,L}
=
\Sigma^*/E_{\mathcal T,L}
=
\Sigma^*/\!\equiv_L.
}
\]

Każda dokładna pamięć/reprezentacja

\[
\rho:\Sigma^*\to Z
\]

spełniająca

\[
\ker_{eq}\rho\subseteq\equiv_L
\]

faktoryzuje zadaniowy iloraz na swoim obrazie:

\[
q_L=f\circ\rho.
\]

Jest to bezpośrednia specjalizacja II.7–II.8 do kontraktu językowego.

---

## 5. Prawa kongruencja i aktualizacja po symbolu

Równoważność Nerode’a jest prawą kongruencją.

Jeżeli

\[
u\equiv_L v,
\]

to dla każdego symbolu \(a\in\Sigma\)

\[
\boxed{
ua\equiv_L va.
}
\]

### Dowód

Dla dowolnego \(w\in\Sigma^*\):

\[
(ua)w=u(aw),
\qquad
(va)w=v(aw).
\]

Ponieważ \(aw\in\Sigma^*\), z \(u\equiv_L v\) otrzymujemy

\[
u(aw)\in L
\Longleftrightarrow
v(aw)\in L.
\]

Zatem \(ua\equiv_L va\). \(\square\)

Wobec tego aktualizacja klasy

\[
\boxed{
\delta_a([u]_L)=[ua]_L
}
\]

jest dobrze określona.

To jest konkretny, klasyczny przykład mechanizmu historii z II.9: przyszłościowa równoważność jest kongruencją dla legalnego rozszerzenia.

---

## 6. Automat ilorazowy

Na ilorazie

\[
Q_L=\Sigma^*/\!\equiv_L
\]

można zdefiniować deterministyczny automat:

- stan początkowy:
  \[
  q_0=[\varepsilon]_L;
  \]
- przejście:
  \[
  \delta([u]_L,a)=[ua]_L;
  \]
- stany akceptujące:
  \[
  F_L=\{[u]_L:u\in L\}.
  \]

Akceptacja jest dobrze określona, ponieważ kontynuacja \(w=\varepsilon\) należy do rodziny testów Nerode’a; zatem

\[
u\equiv_L v
\Rightarrow
(u\in L\iff v\in L).
\]

Jeżeli iloraz ma skończenie wiele klas, otrzymujemy skończony DFA rozpoznający \(L\).

---

## 7. Klasyczne twierdzenie Myhilla–Nerode’a — granica nowości

Klasyczne twierdzenie głosi:

\[
\boxed{
L\text{ jest regularny}
\iff
|\Sigma^*/\!\equiv_L|<\infty.
}
\]

Ponadto, gdy \(L\) jest regularny, liczba klas Nerode’a jest liczbą stanów minimalnego osiągalnego DFA rozpoznającego \(L\), a automat klas resztowych jest minimalny z dokładnością do izomorfizmu.

**Status:** `CLASSICAL`. PSI nie rości autorstwa ani warunku skończonego indeksu, ani twierdzenia o minimalnym DFA.

Warstwa PSI dostarcza jedynie następującego odczytania:

\[
\boxed{
\text{minimal deterministic automaton state}
=
\text{coarsest exact future-test quotient}
}
\]

**pod tym konkretnym kontraktem automatu/języka**.

Nie wolno eksportować tego zdania na dowolne zadanie PSI bez zachowania klasy reprezentacji i testów.

---

## 8. Minimalność automatu a minimalność ogólnej reprezentacji

Twierdzenie o minimalnym DFA mówi o minimalnej liczbie stanów w klasie deterministycznych automatów rozpoznających \(L\).

Nie wynika z niego automatycznie minimalność:

- liczby bitów dowolnego kodu;
- wymiaru dowolnej reprezentacji numerycznej;
- kosztu obliczeniowego;
- czasu aktualizacji;
- pamięci w dowolnym innym modelu obliczeń.

Zatem pozostaje zgodne z II.8:

\[
\boxed{
\text{quotient-order / DFA-state minimality}
\not\Rightarrow
\text{universal coding or compute minimality}.
}
\]

---

## 9. Kontrakt jest konieczny — świadek ograniczonego zbioru testów

Niech

\[
\Sigma=\{0,1\},
\qquad
L=\{0\}.
\]

Jeżeli zadanie obserwuje tylko **bieżącą** akceptację

\[
A_L(u)=\mathbf 1_L(u)
\]

bez domknięcia po wszystkich kontynuacjach, to

\[
A_L(\varepsilon)=A_L(1)=0.
\]

Taki zubożony kontrakt identyfikuje \(\varepsilon\) i `1`.

Jednak dla kontynuacji \(w=0\):

\[
\varepsilon 0=0\in L,
\qquad
10\notin L.
\]

Stąd

\[
\varepsilon\not\equiv_L1.
\]

Zatem:

\[
\boxed{
\text{arbitrary task equivalence}
\neq
\text{Nerode equivalence}
}
\]

bez kontraktu zawierającego wszystkie prawostronne testy akceptacji.

To jest granica mostu, nie kontrprzykład do twierdzenia Myhilla–Nerode’a.

---

## 10. Relacja do pamięci historii PSI

W II.7 przyszłościową równoważność definiowaliśmy abstrakcyjnie przez izomorfizm wszystkich legalnych przyszłych drzew zadaniowych.

W kontrakcie językowym przyszłość ma szczególnie prostą postać:

- legalne rozszerzenia = prawe konkatenacje;
- etykieta zadaniowa = akceptacja;
- dwa prefiksy są równoważne wtedy i tylko wtedy, gdy każda przyszła kontynuacja daje ten sam wynik akceptacji.

Dlatego Myhill–Nerode nie jest jedynie „podobny” do C57. Jest dokładną realizacją przyszłościowej semantyki zadania po tej specjalizacji kontraktu.

---

## 11. Granice II.11

II.11 nie ustanawia:

- że każda relacja zadaniowa PSI jest relacją Nerode’a;
- że każdy iloraz PSI ma skończony indeks;
- że każda dokładna pamięć ma realizację jako skończony DFA;
- że minimalny DFA jest minimalny w każdym modelu obliczeń;
- że ograniczony zbiór testów przyszłości wystarcza do relacji Nerode’a;
- odpowiednika probabilistycznego lub niedeterministycznego bez osobnego kontraktu;
- nowości PSI dla klasycznego twierdzenia Myhilla–Nerode’a.

---

## 12. Status źródłowy

Klasyczna relacja i twierdzenie są przypisane Myhillowi i Nerode’owi. Własna treść PSI w tej jednostce jest ograniczona do dokładnego dopasowania typów:

\[
\boxed{
\text{histories}=\Sigma^*,
\quad
\text{futures}=\text{right continuations},
\quad
\text{task test}=\text{acceptance}.
}
\]

Po tym dopasowaniu

\[
E_{\mathcal T,L}=\equiv_L
\]

jest bezpośrednią tożsamością definicyjną.

---

## 13. Lokalny cross-check

### Typy
`PASS`: alfabet, język, przestrzeń słów, transporty i obserwabla akceptacji są jawne.

### Źródło
`PASS`: Myhill/Nerode są klasycznym źródłem relacji i twierdzenia o skończonym indeksie/minimalnym DFA.

### Dowód PSI bridge
`PASS`: identyczność `E_T,L = ≡_L` wynika bezpośrednio z definicji rodziny `R_w`.

### Kongruencja
`PASS`: prawa kongruencja jest sprawdzona przez zastąpienie przyszłości `w` przyszłością `aw`.

### Scope
`PASS`: minimal-DFA theorem pozostaje klasyczny i jest ograniczony do automatu deterministycznego.

### Boundary witness
`PASS`: język `L={0}` pokazuje, że bieżąca akceptacja bez pełnego domknięcia przyszłości nie daje relacji Nerode’a.

### Agent impact
`PASS`: brak Freeze 01 erraty, brak CORE5 zmiany, brak Agent v03.

---

## 14. Werdykt II.11

\[
\boxed{
\mathrm{II.11\ MYHILL\!\!-\!NERODE\ BRIDGE}
=\mathrm{PASS}.
}
\]

Następny klasyczny element po synchronizacji sterowania: **Paige–Tarjan C14 jako algorytmiczny benchmark, nie twierdzenie PSI**.
