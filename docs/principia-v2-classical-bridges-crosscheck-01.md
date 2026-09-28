# PRINCIPIA SEMANTICA — V2 CLASSICAL BRIDGES CROSS-CHECK 01

**Status:** `PASS AFTER PAIGE–TARJAN COMPLEXITY SCOPE NORMALIZATION / NO FREEZE ERRATA`  
**Date:** 2026-09-29  
**Scope:** II.10–II.12 as one classical-comparison layer  
**Canonical basis:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0, Claim Registry v12, Falsifier Registry v11, Freeze 01  
**Units:** `principia-v2-10-strong-lumpability-bridge.md`, `principia-v2-11-myhill-nerode-bridge.md`, `principia-v2-12-paige-tarjan-benchmark.md`

---

## 0. Pytanie audytu

Warstwa ma odpowiedzieć na trzy różne pytania bez ich zlewania:

1. kiedy probabilistyczna dynamika schodzi na zadaniowy iloraz? — II.10;
2. kiedy przyszłościowa równoważność PSI jest dokładnie klasyczną relacją Nerode’a? — II.11;
3. kiedy klasyczny algorytm rafinacji może obliczyć już właściwie zdefiniowany skończony iloraz? — II.12.

Główny test antyinflacyjny:

\[
\boxed{
\text{classical coincidence}
\neq
\text{universal identity of frameworks}.
}
\]

---

## 1. Typy trzech mostów są różne

### II.10 — typ probabilistyczny

Obiekt:

\[
P:S\times S\to[0,1].
\]

Warunek:

\[
\boxed{
xEy\Rightarrow P(x,C)=P(y,C)
\quad\forall C\in S/E.
}
\]

Mierzoną strukturą są **masy przejścia do bloków**.

### II.11 — typ językowo-testowy

Obiekt:

\[
L\subseteq\Sigma^*.
\]

Rodzina testów:

\[
R_w(u)=\mathbf 1_L(uw),
\qquad w\in\Sigma^*.
\]

Warunek równoważności:

\[
\boxed{
E_{\mathcal T,L}=\equiv_L.
}
\]

Mierzoną strukturą są **wyniki wszystkich prawych kontynuacji**.

### II.12 — typ relacyjno-algorytmiczny

Obiekt:

\[
R\subseteq S\times S,
\qquad
\Pi_0.
\]

Cel:

\[
\boxed{
\Pi_*=	ext{najgrubsza }R\text{-stabilna rafinacja }\Pi_0.
}
\]

Mierzoną strukturą jest **egzystencjalna relacyjna stabilność bloków**, a wynik dotyczy algorytmu obliczającego taki cel.

**VERDICT:** `TYPE SEPARATION = PASS`.

---

## 2. Nie istnieje automatyczny łańcuch II.10 → II.12

Silna lumpowalność Markowa wymaga zgodności wartości liczbowych:

\[
P(x,C)=P(y,C).
\]

Relational coarsest partition używa warunku typu

\[
x\in\operatorname{Pre}_R(C)
\iff
y\in\operatorname{Pre}_R(C)
\]

wewnątrz stabilnego bloku.

Dwa stany mogą mieć krawędzie do tych samych bloków, ale różne masy przejścia. Zatem

\[
\boxed{
\text{relational stability}
\not\Rightarrow
\text{strong Markov lumpability}
}
\]

bez dodatkowego kodowania wag i twierdzenia redukcyjnego.

F61 zachowuje przeciwległy rygiel:

\[
\boxed{
\text{task quotient}
\not\Rightarrow
\text{Markov lumpability}.
}
\]

**VERDICT:** `PASS`.

---

## 3. Nie istnieje automatyczny łańcuch II.11 → II.12

Nerode definiuje cel przez wszystkie prawostronne kontynuacje:

\[
u\equiv_Lv
\iff
\forall w\in\Sigma^*:
uw\in L\Longleftrightarrow vw\in L.
\]

Paige–Tarjan przyjmuje skończony relacyjny problem rafinacji jako **już zbudowane wejście**.

Dlatego samo twierdzenie Myhilla–Nerode’a nie wybiera Paige’a–Tarjana jako algorytmu minimalizacji, a samo istnienie minimalnego DFA nie jest dowodem PT1–PT4.

Poprawny porządek brzmi:

\[
\boxed{
\text{future-test semantics}
\to
\text{Nerode target}
\to
\text{wybór odpowiedniego algorytmu}.
}
\]

**VERDICT:** `PASS`.

---

## 4. Trzy rodzaje „najgrubszości” nie mogą być utożsamione bez typu

W warstwie pojawiają się podobne słowa:

- najgrubszy dokładny iloraz historii — II.8;
- klasy Nerode’a / minimalny DFA — II.11;
- najgrubsza stabilna rafinacja relacyjna — II.12.

Są one zgodne strukturalnie jako problemy utraty rozróżnień, ale mają inne kontrakty i porządki dopuszczalności.

Nie wolno pisać bez dodatkowego twierdzenia:

\[
M_{\mathcal T,t}
=
\Sigma^*/\!\equiv_L
=
\Pi_*.
\]

Równość może zachodzić w konkretnym modelu po dopasowaniu typów, ale nie jest tożsamością architektury.

**VERDICT:** `PASS`.

---

## 5. Status klasyczny / PSI

### II.10

Klasyczne:
- kryterium Kemeny’ego–Snella;
- dobrze określona macierz ilorazowa;
- silna lumpowalność.

PSI:
- osadzenie względem zadaniowego ilorazu;
- rozdział task adequacy od stochastic projectability.

### II.11

Klasyczne:
- relacja Nerode’a;
- skończony indeks iff regularność;
- minimalny DFA.

PSI:
- dokładne dopasowanie kontraktu przyszłych testów i wynik
  \[
  E_{\mathcal T,L}=\equiv_L.
  \]

### II.12

Klasyczne:
- relational coarsest partition;
- Paige–Tarjan;
- standardowa asymptotyka rafinacji.

PSI:
- brama PT1–PT4;
- rozdział celu semantycznego od algorytmu.

Nie znaleziono `CLASSICAL-ERASURE` ani przypisania klasycznych twierdzeń PSI.

**VERDICT:** `SOURCE/STATUS = PASS`.

---

## 6. Złożoność Paige–Tarjana — korekta zakresu

Literatura standardowo podaje dla relational coarsest partition

\[
O(m\log n)
\]

czasu i

\[
O(n+m)
\]

pamięci, przy \(n=|S|\), \(m=|R|\).

Aby uniknąć błędnego odczytania tego skrótu jako pełnego kosztu nawet przy pustej relacji, II.12 rozdziela:

- klasyczną fazę rafinacji: \(O(m\log n)\);
- jawną liniową inicjalizację/odczyt wejścia;
- konserwatywne pełne księgowanie Principiów: \(O(n+m\log n)\).

Jest to normalizacja modelu kosztowego, nie zmiana klasycznego wyniku.

**VERDICT:** `PASS AFTER SCOPE NORMALIZATION`.

---

## 7. Regresje i no-go

Warstwa pozostawia trzy trwałe bariery:

\[
\boxed{
\text{task quotient}
\not\Rightarrow
\text{Markov lumpability}
}
\]

(F61),

\[
\boxed{
\text{arbitrary task equivalence}
\neq
\text{Nerode equivalence}
}
\]

bez pełnego continuation-test contract,

oraz

\[
\boxed{
\text{finite PSI instance}
\not\Rightarrow
\text{Paige–Tarjan applicability}
}
\]

bez redukcji PT1–PT4.

**VERDICT:** `REGRESSION BINDING = PASS`.

---

## 8. Blast radius

Warstwa II.10–II.12:

- nie zmienia CORE5;
- nie zmienia Freeze 01;
- nie zmienia definicji C13/C14/C18;
- nie wymaga Agent v03;
- nie promuje probabilistycznej bisymulacji do C-ID;
- nie zmienia R01–R03;
- rozszerza jedynie prose/bridge layer i F61.

**VERDICT:** `IMPACT = DERIVED / CLASSICAL-BRIDGE ONLY`.

---

## 9. Werdykt warstwy

\[
\boxed{
\mathrm{V2\ CLASSICAL\ BRIDGES\ II.10:II.12}
=
\mathrm{GLOBAL\ CROSSCHECK\ PASS}.
}
\]

Z jedną wykonaną normalizacją:

\[
\boxed{
\text{Paige–Tarjan complexity statement}
\to
\text{explicit cost-model scope}.
}
\]

Nie ma podstaw do erraty Freeze 01 ani do wzrostu rdzenia.

Następny legalny front:

\[
\boxed{
\mathrm{CAT/FACT/NORM}
\to
\mathrm{FRAME}
\to
\mathrm{HIGHER\ COMPATIBILITY}
\to
\mathrm{V2\ WHOLE\ CROSSCHECK}.
}
\]
