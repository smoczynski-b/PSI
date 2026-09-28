# PRINCIPIA SEMANTICA — TOM II
## II.2. Kryterium faktoryzacji przez reprezentację

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, C07 zachowane przez Freeze 01  
**Mapa twierdzeń:** `principia-v2-theorem-map-01.md`, T2.2  
**Falsifier:** F60 — unikalność tylko na `im rho`.

---

## 1. Typy

Niech

\[
\rho:\Omega\to Z,
\qquad
R:\Omega\to W
\]

będą dowolnymi mapami zbiorów o wspólnej dziedzinie \(\Omega\). Definiujemy

\[
\ker_{\rm eq}\rho
=\{(x,y)\in\Omega^2:\rho(x)=\rho(y)\},
\]

\[
\ker_{\rm eq}R
=\{(x,y)\in\Omega^2:R(x)=R(y)\},
\]

oraz

\[
\operatorname{im}\rho
=\{\rho(x):x\in\Omega\}\subseteq Z.
\]

Nie zakładamy surjektywności \(\rho\) na \(Z\).

---

## 2. Pytanie faktoryzacyjne

Mapa \(R\) zależy wyłącznie od reprezentacji \(\rho(x)\), jeśli istnieje

\[
g:\operatorname{im}\rho\to W
\]

taka, że

\[
R=g\circ\rho.
\]

Jest to równoważne pytaniu, czy \(R\) jest stała na każdym włóknie \(\rho\).

---

## 3. Twierdzenie II.2 — kryterium faktoryzacji

Dla map

\[
\rho:\Omega\to Z,
\qquad
R:\Omega\to W
\]

zachodzi

\[
\boxed{
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W,
\quad
R=g\circ\rho.
}
\]

Unikalność dotyczy wyłącznie mapy na \(\operatorname{im}\rho\). Twierdzenie nie ustanawia unikalnego rozszerzenia \(g\) na całe \(Z\).

---

## 4. Dowód

### Kierunek \(\Rightarrow\)

Załóżmy

\[
\ker_{\rm eq}\rho\subseteq\ker_{\rm eq}R.
\]

Dla \(z\in\operatorname{im}\rho\) definiujemy \(g(z)\) jako jedyną wartość \(R(x)\) wspólną dla wszystkich \(x\in\Omega\) spełniających \(\rho(x)=z\).

Definicja jest dobrze określona: jeśli

\[
\rho(x)=\rho(y)=z,
\]

to

\[
(x,y)\in\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R,
\]

a więc

\[
R(x)=R(y).
\]

Zatem dla każdego \(x\in\Omega\)

\[
g(\rho(x))=R(x),
\]

czyli

\[
R=g\circ\rho.
\]

Jeżeli także

\[
h:\operatorname{im}\rho\to W
\]

spełnia \(R=h\circ\rho\), to dla dowolnego \(z\in\operatorname{im}\rho\) i dowolnego \(x\) z \(\rho(x)=z\):

\[
h(z)=h(\rho(x))=R(x)=g(\rho(x))=g(z).
\]

Stąd \(h=g\) na \(\operatorname{im}\rho\).

### Kierunek \(\Leftarrow\)

Załóżmy

\[
R=g\circ\rho
\]

dla pewnego \(g:\operatorname{im}\rho\to W\). Jeżeli

\[
\rho(x)=\rho(y),
\]

to

\[
R(x)=g(\rho(x))=g(\rho(y))=R(y).
\]

Zatem

\[
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R.
\]

To kończy dowód. \(\square\)

### Przypadek pustej dziedziny

Jeżeli

\[
\Omega=\varnothing,
\]

to

\[
\operatorname{im}\rho=\varnothing
\]

i istnieje dokładnie jedna mapa

\[
\varnothing\to W.
\]

Obie relacje jąder są puste, więc twierdzenie pozostaje prawdziwe bez dodatkowej hipotezy niepustości i bez użycia aksjomatu wyboru.

---

## 5. Sens informacyjny

Warunek

\[
\ker_{\rm eq}\rho\subseteq\ker_{\rm eq}R
\]

mówi dokładnie, że reprezentacja \(\rho\) nie skleja żadnej pary kandydatów, którą wielkość \(R\) nadal rozróżnia.

Ta sama reprezentacja może więc faktoryzować jedną wielkość, a nie faktoryzować innej.

---

## 6. Granica F60 — tylko obraz reprezentacji

Twierdzenie mówi

\[
\exists!\,g:\operatorname{im}\rho\to W,
\]

a nie w ogólności

\[
\exists!\,g:Z\to W.
\]

Jeżeli \(\rho\) nie jest surjektywna, równanie

\[
R=g\circ\rho
\]

nie ogranicza wartości \(g\) poza \(\operatorname{im}\rho\).

### Kontrprzykład F60

Niech

\[
\Omega=\{a\},
\quad
Z=\{0,1\},
\quad
W=\{u,v\},
\]

\[
\rho(a)=0,
\qquad
R(a)=u.
\]

Na

\[
\operatorname{im}\rho=\{0\}
\]

faktoryzacja wymusza jednoznacznie

\[
g(0)=u.
\]

Na całym \(Z\) istnieją jednak dwa różne rozszerzenia:

\[
g_1(0)=u,\quad g_1(1)=u,
\]

\[
g_2(0)=u,\quad g_2(1)=v.
\]

Oba spełniają

\[
R=g_i\circ\rho,
\]

ale \(g_1\neq g_2\). Unikalność na całym \(Z\) wymaga więc dodatkowej hipotezy, np. surjektywności \(\rho\), albo osobnego prawa rozszerzenia.

---

## 7. Przypadki szczególne

### 7.1. Reprezentacja surjektywna

Jeżeli

\[
\operatorname{im}\rho=Z,
\]

to twierdzenie daje unikalne

\[
g:Z\to W.
\]

### 7.2. Reprezentacja injektywna

Jeżeli \(\rho\) jest injektywna, to

\[
\ker_{\rm eq}\rho=\Delta_\Omega
\subseteq
\ker_{\rm eq}R
\]

dla każdej mapy \(R\). Każda \(R\) faktoryzuje więc przez \(\rho\) na \(\operatorname{im}\rho\).

### 7.3. Reprezentacja stała

Jeżeli \(\rho\) jest stała, to

\[
\ker_{\rm eq}\rho=\Omega\times\Omega.
\]

Faktoryzacja istnieje wtedy i tylko wtedy, gdy \(R\) jest stała na \(\Omega\).

---

## 8. Status źródłowy

Twierdzenie II.2 jest elementarnym klasycznym faktem o faktoryzacji map przez ich włókna. Dowód został podany samodzielnie.

\[
\boxed{
\text{CLASSICAL ELEMENTARY FACTORIZATION LEMMA / PSI-ADAPTED TOOL}.
}
\]

PSI nie rości sobie autorstwa lematu. Jego znaczenie dla PSI polega na tym, że wystarczalność obserwatora, adekwatność reprezentacji, pamięć i legalne redukcje są jego bezpośrednimi specjalizacjami.

---

## 9. Wiązanie z regresjami

Bezpośrednim obowiązkowym falsyfikatorem zakresu jest F60:

\[
\boxed{
\text{unikalność tylko na }\operatorname{im}\rho.
}
\]

R01 HCube i R02 Go dostarczają później przykładów, w których zbyt gruba reprezentacja narusza odpowiednią inkluzję jąder. Nie są one dowodem samego lematu.

---

## 10. Czego twierdzenie nie mówi

Twierdzenie II.2 nie daje automatycznie:

- ciągłości, mierzalności, liniowości ani gładkości \(g\);
- obliczalności lub stabilności numerycznej faktoryzacji;
- rozszerzenia \(g\) poza \(\operatorname{im}\rho\);
- unikalności takiego rozszerzenia;
- pełnej legalności reprezentacji w kontrakcie PSI.

Każda z tych własności wymaga dodatkowych hipotez.

---

## 11. Cross-check

Sprawdzono:

1. dobrą określoność \(g\) na włóknach \(\rho\);
2. unikalność wyłącznie na \(\operatorname{im}\rho\);
3. przypadek \(\Omega=\varnothing\);
4. brak niejawnej hipotezy surjektywności;
5. brak importu topologii, miary, liniowości, stabilności lub obliczalności;
6. zgodność z F60.

Nie stwierdzono potrzeby erraty Freeze 01.

\[
\boxed{
\mathrm{II.2}=\mathrm{THEOREM\ PROSE\ PASS\ 01 / PROOF\ PASS / CROSS\!-
CHECK\ PASS}.
}
\]

---

## 12. Przejście do II.3

W II.3 podstawimy

\[
\rho=\Psi_c,
\qquad
R=q_{\mathcal T,c}.
\]

Otrzymamy globalne kryterium wystarczalności obserwatora:

\[
\ker_{\rm eq}\Psi_c
\subseteq
E_{\mathcal T,c}
\iff
\exists!\,f:\operatorname{im}\Psi_c\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=f\circ\Psi_c.
\]
