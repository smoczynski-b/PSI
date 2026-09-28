# PRINCIPIA SEMANTICA — TOM II
## II.9. Rekurencyjna aktualizacja ilorazu historii

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez / wynik migrowany:** `claim-registry-12.md`, C45 oraz C59  
**Mapa twierdzeń:** `principia-v2-theorem-map-02.md`, II.9  
**Ścisła zależność dowodowa:** II.7, w szczególności C57/C58 i literalnie etykietowana przyszłościowa równoważność historii.  
**Analogia strukturalna:** II.6 — ogólne deterministyczne zejście dynamiki na iloraz.  
**Nie jest przesłanką dowodu:** II.8 — najgrubszość/minimalność ilorazu historii.  
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

## 2. Kongruencja RED-1 — ponowne wyprowadzenie C59

Z II.7 mamy przyszłościową równoważność \(\equiv_{\mathcal T,t}\) na \(\mathcal H_t\), zdefiniowaną przez izomorfizm literalnie etykietowanych drzew przyszłości.

C59 jest identyfikatorem rejestrowym twierdzenia o kongruencji/aktualizacji, które w tej jednostce jest **ponownie wyprowadzane**, a nie używane jako wcześniejsza przesłanka.

Jeżeli

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

Pierwsza własność wynika z zachowania literalnych etykiet krawędzi przez izomorfizm przyszłych drzew; kierunek odwrotny otrzymujemy przez symetrię \(H'\equiv_{\mathcal T,t}H\). Druga wynika z izomorfizmu odpowiadających poddrzew następników.

Są to dokładnie dwie własności kongruencji potrzebne do zejścia aktualizacji na klasy.

---

## 3. Ilorazy historii

Definiujemy

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t},
\qquad
q_{\mathcal T,t}:\mathcal H_t\to M_{\mathcal T,t},
\]

oraz analogicznie \(M_{\mathcal T,t+1}\).

Definicja tego ilorazu pochodzi już z II.7; II.8 dowodzi później jego najgrubszości w porządku dokładnych ilorazów, lecz ta własność nie jest potrzebna do niniejszego dowodu.

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
([H]_{\mathcal T,t},\varepsilon,y)\in\overline D_t
\iff
(H,\varepsilon,y)\in D_t.
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

Jeżeli \(H'\equiv_{\mathcal T,t}H\), to z §2

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

Na legalnej dziedzinie zachodzi komutacja

\[
\boxed{
q_{\mathcal T,t+1}
\circ
\delta_t
=
U_{\mathcal T,t}
\circ
(q_{\mathcal T,t}\times\operatorname{id}_{\mathcal E_t}\times\operatorname{id}_{\mathcal Y_{t+1}})
}
\]

po ograniczeniu obu stron do \(D_t\).

Jest to czasowo zmienna i częściowa wersja ogólnego schematu zejścia dynamiki na iloraz z II.6, ale dowód nie wymaga II.6 jako przesłanki.

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

II.6 jest więc analogią strukturalną, nie wcześniejszym lematem wymaganym przez dowód II.9.

---

## 9. Matematyczna rekurencja nie oznacza skończonej pamięci

Istnienie dobrze określonego

\[
U_{\mathcal T,t}
\]

nie mówi nic samo przez się o:

- liczbie klas w \(M_{\mathcal T,t}\);
- długości kodu klasy;
- obliczalności relacji \(\equiv_{\mathcal T,t}\);
- możliwości wyznaczenia klasy bez reprezentanta historii;
- koszcie aktualizacji;
- istnieniu skończonego automatu realizującego iloraz.

Zatem

\[
\boxed{
\text{mathematical recursive update}
\not\Rightarrow
\text{finite-memory efficient implementation}.
}
\]

Jest to rygiel F43.

---

## 10. Go jako regres kongruencji

W regułach Go legalność tego samego literalnego ruchu może zależeć od historii. Jeżeli pamięć scala historie, po których ten sam ruch ma różną legalność, nie może reprezentować poprawnie klasy przyszłościowej.

R02 testuje więc nie tylko samą adekwatność pamięci, ale także warunki wymagane do dobrze określonej aktualizacji ilorazu:

1. legalność etykiety musi być klasowo niezmiennicza;
2. następca po tej etykiecie musi mieć klasę niezależną od reprezentanta.

---

## 11. Status źródłowy

C45 i C59 są migrowanymi wynikami RED-1. W tej jednostce ich treść jest odtwarzana z aktualnej definicji C57/C58 i jawnego typowania częściowej aktualizacji.

\[
\boxed{
\text{RED-1 HISTORY CONGRUENCE}
+
\text{CLASSICAL QUOTIENT WELL-DEFINEDNESS PATTERN}.
}
\]

Nie jest to nowy prymityw PSI.

---

## 12. Granice II.9

II.9 nie ustanawia:

- skończonej liczby klas historii;
- minimalności bitowej;
- algorytmu obliczania klasy;
- decidowalności równoważności historii;
- efektywnej implementacji aktualizacji;
- totalności \(U_{\mathcal T,t}\);
- stochastycznego odpowiednika bez osobnego typowania jądra przejścia;
- automatycznej adekwatności jakiejkolwiek konkretnej pamięci.

---

## 13. Cross-check po korekcie grafu zależności

### Typy
`PASS`: dziedzina częściowa, etykiety i przestrzenie historii są jawne.

### Proof dependency
`PASS`: dowód używa II.7/C57/C58 oraz własności literalnie etykietowanego izomorfizmu przyszłych drzew. C59 jest identyfikatorem wyniku dowodzonego/migrowanego w tej jednostce, a nie wcześniejszą przesłanką.

### II.6 / II.8
`PASS`: II.6 jest analogią strukturalną; II.8 nie jest przesłanką dowodu.

### Granica
`PASS`: F43 zachowany.

### Freeze impact
`NONE`: korekta dotyczy grafu zależności i prezentacji źródła wyniku, nie treści twierdzenia.

---

## 14. Werdykt

\[
\boxed{
\mathrm{II.9\ RECURSIVE\ HISTORY\ QUOTIENT\ UPDATE}
=\mathrm{PASS}.
}
\]

Treść C45/C59 pozostaje bez zmiany; poprawiono wyłącznie klasyfikację zależności dowodowych.
