# PRINCIPIA SEMANTICA — TOM II
## II.10. Silna lumpowalność jako stochastyczne zejście dynamiki na iloraz

**Status:** `CLASSICAL THEOREM / PSI BRIDGE / PROSE PASS 01 / LOCAL CROSS-CHECK PASS`  
**Źródło nadrzędne PSI:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, zachowane C13  
**Mapa porównawcza:** `classical-compare-01.md`  
**Zależności PSI:** II.5–II.6 jako warstwa rozróżnienia statyczna/dynamiczna; nie jako dowód klasycznego twierdzenia  
**Źródło klasyczne:** J. G. Kemeny, J. L. Snell, *Finite Markov Chains*, Chapter VI, §6.3, Theorem 6.3.2 (warunek lumpowalności względem partycji).  
**Zakres:** skończony jednorodny łańcuch Markowa w czasie dyskretnym; dokładna partycja stanów; brak twierdzenia o lumpowalności słabej, przybliżonej lub ciągłoczasowej.

---

## 1. Kontrakt i typy

Niech

\[
S=\{1,\ldots,n\}
\]

będzie skończoną przestrzenią stanów, a

\[
P:S\times S\to[0,1]
\]

macierzą przejścia jednorodnego łańcucha Markowa, z

\[
\sum_{y\in S}P(x,y)=1
\qquad\forall x\in S.
\]

Niech \(E\) będzie relacją równoważności na \(S\). Oznaczamy

\[
\bar S=S/E,
\qquad
q:S\to\bar S,
\qquad
q(x)=[x]_E.
\]

Dla bloku \(C\in\bar S\) definiujemy masę przejścia z \(x\) do tego bloku:

\[
P(x,C)
:=
\sum_{z\in q^{-1}(C)}P(x,z).
\]

Jest to prawdopodobieństwo, że po jednym kroku proces znajdzie się w klasie \(C\), gdy bieżącym stanem mikro jest \(x\).

---

## 2. Warunek Kemeny'ego–Snella

Partycyjny warunek lumpowalności ma postać

\[
\boxed{
 xEy
 \Longrightarrow
 P(x,C)=P(y,C)
 \quad
 \forall C\in\bar S.
}
\]

Innymi słowy, dwa stany należące do tego samego bloku muszą wysyłać **taką samą całkowitą masę przejścia do każdego bloku ilorazowego**.

W terminologii Kemeny'ego–Snella jest to warunek `lumpability`; w znacznej części późniejszej literatury odpowiada on `strong lumpability`, dla odróżnienia od słabszych pojęć zależnych od rozkładu początkowego.

---

## 3. Twierdzenie II.10.A — równoważne postacie silnej lumpowalności

Dla skończonego jednorodnego łańcucha Markowa \((S,P)\) i relacji równoważności \(E\) następujące warunki są równoważne.

### (L1) Stabilność mas blokowych

\[
\boxed{
 xEy
 \Longrightarrow
 P(x,C)=P(y,C)
 \quad\forall C\in\bar S.
}
\]

### (L2) Istnienie jednoznacznej macierzy przejścia na ilorazie

Istnieje dokładnie jedna macierz stochastyczna

\[
\bar P:\bar S\times\bar S\to[0,1]
\]

spełniająca

\[
\boxed{
\bar P([x]_E,C)=P(x,C)
}
\]

dla każdego \(x\in S\) i \(C\in\bar S\).

### (L3) Markowowskość procesu blokowego dla każdego rozkładu początkowego

Jeżeli \((X_t)_{t\ge0}\) jest łańcuchem z macierzą \(P\), to

\[
Z_t=q(X_t)
\]

jest jednorodnym łańcuchem Markowa na \(\bar S\) z tą samą macierzą \(\bar P\), niezależnie od wyboru rozkładu początkowego \(X_0\).

---

## 4. Dowód

### (L1) \(\Rightarrow\) (L2)

Definiujemy

\[
\bar P([x]_E,C):=P(x,C).
\]

Jeżeli \([x]_E=[y]_E\), to \(xEy\), więc z (L1)

\[
P(x,C)=P(y,C)
\]

dla każdego bloku \(C\). Definicja nie zależy więc od reprezentanta.

Ponadto

\[
\sum_{C\in\bar S}\bar P([x]_E,C)
=
\sum_{C\in\bar S}\sum_{z\in q^{-1}(C)}P(x,z)
=
\sum_{z\in S}P(x,z)
=1.
\]

Zatem \(\bar P\) jest macierzą stochastyczną. Jednoznaczność jest natychmiastowa, ponieważ wzór wymusza każdą wartość \(\bar P([x]_E,C)\).

### (L2) \(\Rightarrow\) (L1)

Jeżeli \(xEy\), to \([x]_E=[y]_E\). Z (L2)

\[
P(x,C)
=
\bar P([x]_E,C)
=
\bar P([y]_E,C)
=
P(y,C)
\]

dla każdego \(C\in\bar S\).

### (L1) \(\Rightarrow\) (L3)

Dla dowolnego stanu \(x\in S\):

\[
\Pr(Z_{t+1}=C\mid X_t=x)
=P(x,C)
=\bar P(q(x),C).
\]

Wartość po prawej zależy wyłącznie od klasy \(q(x)=Z_t\), a nie od mikroreprezentanta \(x\). Warunkując po historii procesu blokowego i używając prawa całkowitego prawdopodobieństwa, otrzymujemy

\[
\Pr(Z_{t+1}=C\mid Z_t=A,Z_{t-1},\ldots,Z_0)
=\bar P(A,C).
\]

Zatem \((Z_t)\) jest jednorodnym łańcuchem Markowa z macierzą \(\bar P\), dla dowolnego rozkładu początkowego.

### (L3) \(\Rightarrow\) (L1)

Weźmy \(xEy\). Uruchommy łańcuch najpierw z rozkładu punktowego \(X_0=x\), a następnie z \(X_0=y\). W obu przypadkach

\[
Z_0=[x]_E=[y]_E.
\]

Jeżeli proces blokowy ma tę samą macierz \(\bar P\) niezależnie od rozkładu początkowego, to dla każdego \(C\in\bar S\)

\[
P(x,C)
=
\Pr(Z_1=C\mid X_0=x)
=
\bar P([x]_E,C)
=
\bar P([y]_E,C)
=
P(y,C).
\]

Zatem zachodzi (L1). \(\square\)

---

## 5. Korolarium PSI — zadaniowy iloraz jako stan Markowa

Niech teraz skończona przestrzeń kandydatów PSI będzie \(\Omega_c=S\), a zadaniowa relacja równoważności

\[
E_{\mathcal T,c}
\]

wyznacza iloraz

\[
M_{\mathcal T,c}=S/E_{\mathcal T,c}.
\]

Niech stochastyczna dynamika kontraktu będzie jawnie otypowana macierzą przejścia \(P_c\).

Wtedy zadaniowy iloraz posiada autonomiczną jednorodną dynamikę Markowa dokładnie wtedy, gdy

\[
\boxed{
 xE_{\mathcal T,c}y
 \Longrightarrow
 \sum_{z\in C}P_c(x,z)
 =
 \sum_{z\in C}P_c(y,z)
 \quad
 \forall C\in M_{\mathcal T,c}.
}
\]

Jeżeli warunek zachodzi, definiujemy

\[
\boxed{
\bar P_{\mathcal T,c}([x],C)
=
\sum_{z\in C}P_c(x,z).
}
\]

Jest to stochastyczny odpowiednik zejścia dynamiki na iloraz z II.6, lecz **nie jest mechanicznym przepisaniem warunku deterministycznego**.

W wersji deterministycznej wystarcza kongruencja

\[
xEy\Rightarrow\delta(x)E\delta(y).
\]

W wersji Markowa wymagana jest równość całych mas przejścia do **każdego bloku** ilorazowego.

---

## 6. Najważniejsze rozróżnienie PSI

Warunek

\[
\ker_{eq}q_{\mathcal T}=E_{\mathcal T}
\]

mówi, które różnice stanów są nieistotne dla zadania.

Nie mówi sam przez się, że proces po tych klasach jest autonomicznym łańcuchem Markowa.

Dlatego należy zachować:

\[
\boxed{
\text{task quotient}
\not\Rightarrow
\text{Markov lumpability}.
}
\]

Poprawny most ma postać

\[
\boxed{
E_{\mathcal T}
+
\text{block-transition stability}
\Longrightarrow
\text{autonomous Markov quotient}.
}
\]

A dla skończonego jednorodnego łańcucha warunek stabilności blokowej jest także konieczny.

---

## 7. Minimalny kontrprzykład do automatycznej lumpowalności

Niech

\[
S=\{a,b,c\},
\qquad
E=\{\{a,b\},\{c\}\}.
\]

Niech statyczny task observable rozróżnia jedynie blok \(\{a,b\}\) od \(\{c\}\), więc \(aEb\) jest legalne dla tego zadania statycznego.

Ustalmy dynamikę

\[
P(a,a)=1,
\qquad
P(b,c)=1,
\qquad
P(c,c)=1.
\]

Dla bloku

\[
A=\{a,b\}
\]

mamy

\[
P(a,A)=1,
\qquad
P(b,A)=0.
\]

Zatem

\[
\boxed{aEb\quad\text{ale partycja nie jest lumpowalna}.}
\]

Statyczny iloraz zadaniowy istnieje i jest poprawny dla zadania statycznego, lecz nie przenosi autonomicznie dynamiki Markowa.

Jeżeli kontrakt zadaniowy zostanie rozszerzony tak, aby przyszłe prawdopodobieństwa blokowe były wielkościami istotnymi, wtedy pierwotna relacja \(E\) może przestać być właściwą relacją zadaniową. To jest zmiana kontraktu/zadania, a nie naprawa dowodu przez retorykę.

---

## 8. Relacja do II.6

II.6 i II.10 mają wspólny schemat:

\[
\text{mikrodynamika}
\to
\text{warunek niezależności od reprezentanta}
\to
\text{dynamika na ilorazie}.
\]

Ale warunki są różne typowo:

### deterministycznie

\[
\delta(x)\in[\delta(y)]_E
\quad\text{dla }xEy;
\]

### stochastycznie

\[
P(x,C)=P(y,C)
\quad\forall C\in S/E.
\]

Dlatego

\[
\boxed{
\text{deterministic congruence}
\neq
\text{Markov lumpability condition}.
}
\]

Nie wolno transportować II.6 do jąder Markowa przez prostą zamianę symbolu \(\delta\) na \(P\).

---

## 9. Granice twierdzenia

II.10 nie ustanawia:

- lumpowalności słabej;
- lumpowalności zależnej od szczególnego rozkładu początkowego;
- lumpowalności przybliżonej;
- bisymulacji probabilistycznej;
- minimalności liczby bloków;
- algorytmu wyznaczania optymalnej partycji;
- wyników dla nieskończonych przestrzeni bez dodatkowej teorii mierzalności;
- wyników dla czasu ciągłego bez osobnego typu generatora;
- automatycznej lumpowalności każdego zadaniowego ilorazu PSI.

Paige–Tarjan, probabilistyczna bisymulacja i inne konstrukcje pozostają osobnymi porównaniami.

---

## 10. Status źródłowy

Twierdzenie Kemeny'ego–Snella jest klasyczne. PSI nie rości nowości dla kryterium lumpowalności ani dla konstrukcji macierzy \(\bar P\).

Wkład warstwy PSI polega wyłącznie na precyzyjnym osadzeniu klasycznego kryterium względem zadaniowego ilorazu:

\[
\boxed{
\text{task equivalence identifies allowed forgetting;}
\quad
\text{lumpability tests dynamic autonomy after forgetting.}
}
\]

To rozdzielenie chroni przed utożsamieniem adekwatności reprezentacji ze stochastyczną projektowalnością dynamiki.

---

## 11. Lokalny cross-check

### Typy
`PASS`: skończona przestrzeń, macierz stochastyczna, partycja i iloraz są jawne.

### Źródło
`PASS`: Kemeny–Snell jest klasycznym źródłem warunku koniecznego i wystarczającego.

### Dowód
`PASS`: dobrze określona macierz ilorazowa jest równoważna stałości mas blokowych; markowowskość procesu blokowego wynika z reprezentantowej niezmienniczości prawdopodobieństw następnego bloku.

### Scope
`PASS`: brak eksportu do weak/approximate/continuous-time lumpability.

### PSI status
`PASS`: C13 pozostaje `CLASSICAL CONDITION + PSI BRIDGE / BENCHMARK`; brak nowego prymitywu.

### Falsifier
`PASS`: trzystanowy przykład rozdziela statyczną task-equivalence od dynamicznej lumpowalności.

### Agent impact
`PASS`: brak Freeze 01 erraty, brak CORE5 zmiany, brak Agent v03.

---

## 12. Werdykt II.10

\[
\boxed{
\mathrm{II.10\ STRONG\ LUMPABILITY\ BRIDGE}
=\mathrm{PASS}.
}
\]

Następny klasyczny most po synchronizacji sterowania: **Myhill–Nerode C18**.
