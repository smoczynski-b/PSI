# PRINCIPIA SEMANTICA — TOM II
## II.2. Kryterium faktoryzacji przez reprezentację

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PENDING`  
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

będą dowolnymi mapami zbiorów o wspólnej dziedzinie \(\Omega\).

Definiujemy relacje nierozróżnialności

\[
\ker_{\rm eq}\rho
=
\{(x,y)\in\Omega^2:\rho(x)=\rho(y)\},
\]

oraz

\[
\ker_{\rm eq}R
=
\{(x,y)\in\Omega^2:R(x)=R(y)\}.
\]

Obraz reprezentacji oznaczamy

\[
\operatorname{im}\rho
=
\{\rho(x):x\in\Omega\}\subseteq Z.
\]

Nie zakładamy surjektywności \(\rho\) na \(Z\).

---

## 2. Pytanie faktoryzacyjne

Mapa \(R\) zależy wyłącznie od reprezentacji \(\rho(x)\), jeśli istnieje mapa

\[
g:\operatorname{im}\rho\to W
\]

taka, że

\[
R=g\circ\rho.
\]

Warunek ten oznacza, że wartość \(R(x)\) można wyznaczyć z samego obrazu \(\rho(x)\), bez potrzeby odzyskiwania reprezentanta \(x\).

Pytanie brzmi zatem:

\[
\boxed{
\text{kiedy }R\text{ jest stała na wszystkich włóknach }\rho?
}
\]

Odpowiedzią jest inkluzja jąder równoważności.

---

## 3. Twierdzenie II.2 — kryterium faktoryzacji

### Twierdzenie

Dla map

\[
\rho:\Omega\to Z,
\qquad
R:\Omega\to W
\]

zachodzi równoważność

\[
\boxed{
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R
\iff
\exists!\,g:\operatorname{im}\rho\to W
\quad
R=g\circ\rho.
}
\]

Unikalność dotyczy wyłącznie mapy

\[
g:\operatorname{im}\rho\to W.
\]

Nie jest to twierdzenie o unikalnym rozszerzeniu \(g\) na całe \(Z\).

---

## 4. Dowód

### Kierunek \(\Rightarrow\)

Załóżmy

\[
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R.
\]

Dla każdego

\[
z\in\operatorname{im}\rho
\]

istnieje co najmniej jeden \(x\in\Omega\) taki, że

\[
\rho(x)=z.
\]

Definiujemy

\[
\boxed{
g(z)=R(x).}
\]

Musimy sprawdzić, że definicja nie zależy od wyboru reprezentanta.

Jeżeli również \(y\in\Omega\) spełnia

\[
\rho(y)=z,
\]

to

\[
\rho(x)=\rho(y),
\]

a więc

\[
(x,y)\in\ker_{\rm eq}\rho.
\]

Z założonej inkluzji wynika

\[
(x,y)\in\ker_{\rm eq}R,
\]

a zatem

\[
R(x)=R(y).
\]

Definicja \(g\) jest więc dobrze określona.

Dla każdego \(x\in\Omega\):

\[
g(\rho(x))=R(x),
\]

czyli

\[
R=g\circ\rho.
\]

Pozostaje unikalność. Niech

\[
h:\operatorname{im}\rho\to W
\]

również spełnia

\[
R=h\circ\rho.
\]

Dla dowolnego \(z\in\operatorname{im}\rho\) wybierzmy \(x\in\Omega\) z \(\rho(x)=z\). Wtedy

\[
h(z)=h(\rho(x))=R(x)=g(\rho(x))=g(z).
\]

Zatem

\[
h=g
\]

na \(\operatorname{im}\rho\).

### Kierunek \(\Leftarrow\)

Załóżmy, że istnieje

\[
g:\operatorname{im}\rho\to W
\]

taka, że

\[
R=g\circ\rho.
\]

Jeżeli

\[
(x,y)\in\ker_{\rm eq}\rho,
\]

to

\[
\rho(x)=\rho(y).
\]

Stąd

\[
R(x)=g(\rho(x))=g(\rho(y))=R(y),
\]

czyli

\[
(x,y)\in\ker_{\rm eq}R.
\]

Zatem

\[
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R.
\]

To kończy dowód. \(\square\)

---

## 5. Sens informacyjny

Warunek

\[
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R
\]

mówi dokładnie, że reprezentacja \(\rho\) nie skleja żadnej pary kandydatów, którą wielkość \(R\) nadal rozróżnia.

Jeżeli więc

\[
\rho(x)=\rho(y),
\]

to dla faktoryzacji konieczne jest

\[
R(x)=R(y).
\]

Kryterium jest całkowicie względne wobec wybranej wielkości \(R\). Ta sama reprezentacja może faktoryzować jedną wielkość, a nie faktoryzować innej.

---

## 6. Najważniejsza granica: obraz reprezentacji

Twierdzenie nie mówi

\[
\exists!\,g:Z\to W.
\]

Mówi tylko

\[
\exists!\,g:\operatorname{im}\rho\to W.
\]

Jeżeli \(\rho\) nie jest surjektywna, wartości mapy poza \(\operatorname{im}\rho\) nie są ograniczone przez równanie

\[
R=g\circ\rho.
\]

### Kontrprzykład F60

Niech

\[
\Omega=\{a\},
\qquad
Z=\{0,1\},
\qquad
W=\{u,v\},
\]

oraz

\[
\rho(a)=0,
\qquad
R(a)=u.
\]

Na obrazie

\[
\operatorname{im}\rho=\{0\}
\]

jedyna możliwa mapa faktoryzująca spełnia

\[
g(0)=u.
\]

Ale na całym \(Z\) istnieją co najmniej dwa rozszerzenia:

\[
g_1(0)=u,\quad g_1(1)=u,
\]

oraz

\[
g_2(0)=u,\quad g_2(1)=v.
\]

Oba spełniają

\[
R=g_i\circ\rho,
\]

lecz

\[
g_1\neq g_2.
\]

Dlatego każde przyszłe sformułowanie „istnieje unikalne \(g:Z\to W\)” wymaga dodatkowej hipotezy, np. surjektywności \(\rho\), albo osobnego prawa rozszerzenia.

---

## 7. Przypadki szczególne

### 7.1. \(\rho\) surjektywna

Jeżeli

\[
\operatorname{im}\rho=Z,
\]

to twierdzenie daje rzeczywiście unikalną mapę

\[
g:Z\to W.
\]

Nie jest to nowa treść; jest to specjalny przypadek głównego twierdzenia.

### 7.2. \(\rho\) injektywna

Jeżeli \(\rho\) jest injektywna, to

\[
\ker_{\rm eq}\rho=\Delta_\Omega,
\]

gdzie \(\Delta_\Omega\) jest diagonalą. Ponieważ

\[
\Delta_\Omega\subseteq\ker_{\rm eq}R
\]

dla każdej mapy \(R\), każda \(R\) faktoryzuje przez injektywną reprezentację na \(\operatorname{im}\rho\).

### 7.3. Reprezentacja stała

Jeżeli \(\rho\) jest stała, to

\[
\ker_{\rm eq}\rho=\Omega\times\Omega.
\]

Faktoryzacja istnieje wtedy i tylko wtedy, gdy \(R\) także jest stała.

---

## 8. Status źródłowy

Twierdzenie II.2 jest elementarnym klasycznym faktem o faktoryzacji map przez ich włókna. Dowód został podany samodzielnie.

Status:

\[
\boxed{
\text{CLASSICAL ELEMENTARY FACTORIZATION LEMMA / PSI-ADAPTED TOOL}.
}
\]

PSI nie rości sobie autorstwa samego lematu. Jego rola w PSI jest centralna dlatego, że późniejsze twierdzenia o wystarczalności obserwatora, adekwatności reprezentacji, pamięci i legalnych redukcjach są jego bezpośrednimi specjalizacjami.

---

## 9. Wiązanie z regresjami

Bezpośrednim obowiązkowym falsyfikatorem zakresu jest F60:

\[
\boxed{
\text{unikalność faktoryzacji tylko na }\operatorname{im}\rho.
}
\]

R01 HCube i R02 Go dostarczają później przykładów, w których warunek

\[
\ker_{\rm eq}\rho
\subseteq
\ker_{\rm eq}R
\]

lub jego zadaniowa specjalizacja nie zachodzi dla zbyt grubej reprezentacji.

Nie są one jednak dowodem samego lematu.

---

## 10. Czego twierdzenie nie mówi

Twierdzenie II.2 nie daje automatycznie:

- ciągłości \(g\);
- mierzalności \(g\);
- liniowości \(g\);
- gładkości \(g\);
- obliczalności \(g\);
- stabilności numerycznej faktoryzacji;
- rozszerzenia \(g\) poza \(\operatorname{im}\rho\);
- unikalnego takiego rozszerzenia;
- legalności reprezentacji w całym kontrakcie PSI.

Każda z tych własności wymaga osobnych założeń.

---

## 11. Przejście do II.3

W następnym kroku podstawimy

\[
\rho=\Psi_c
\]

oraz

\[
R=q_{\mathcal T,c}.
\]

Wtedy Twierdzenie II.2 da dokładnie globalne kryterium wystarczalności obserwatora:

\[
\ker_{\rm eq}\Psi_c
\subseteq
E_{\mathcal T,c}
\iff
\exists!\,f:\operatorname{im}\Psi_c\to M_{\mathcal T,c},
\quad
q_{\mathcal T,c}=f\circ\Psi_c.
\]

To będzie Twierdzenie II.3.
