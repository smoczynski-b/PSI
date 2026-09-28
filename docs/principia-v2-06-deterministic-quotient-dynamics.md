# PRINCIPIA SEMANTICA — TOM II
## II.6. Deterministyczna dynamika ilorazowa

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PENDING`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, C10 zachowane przez Freeze 01  
**Mapa twierdzeń:** `principia-v2-theorem-map-02.md`, II.6  
**Klasa:** klasyczne kryterium kongruencji / adaptacja do dynamiki ilorazowej PSI.  
**Granica:** twierdzenie deterministyczne; nie jest twierdzeniem o lumpowalności łańcuchów Markowa.

---

## 1. Typy

Niech

\[
\Omega
\]

będzie zbiorem, niech

\[
E\subseteq\Omega\times\Omega
\]

będzie relacją równoważności, a

\[
q_E:\Omega\to\Omega/E
\]

projekcją ilorazową.

Niech

\[
\delta:\Omega\to\Omega
\]

będzie całkowitą deterministyczną mapą jednego kroku.

Pytamy, kiedy istnieje mapa

\[
\bar\delta:\Omega/E\to\Omega/E
\]

spełniająca diagram komutatywny

\[
\boxed{
\bar\delta\circ q_E=q_E\circ\delta.
}
\]

Jeżeli taka mapa istnieje, dynamika \(\delta\) **schodzi na iloraz**.

---

## 2. Kongruencja dynamiki

Relację \(E\) nazywamy kongruencją dla \(\delta\), jeżeli

\[
\boxed{
xEy\Longrightarrow\delta(x)E\delta(y).}
\]

Warunek mówi dokładnie, że wybór reprezentanta klasy \([x]_E\) nie może zmienić klasy następnego stanu.

Jest to warunek dynamiczny. Nie wynika z samego faktu, że \(E\) jest rozsądną lub zadaniowo adekwatną relacją statyczną.

---

## 3. Twierdzenie II.6 — kryterium zejścia dynamiki na iloraz

### Twierdzenie

Dla relacji równoważności \(E\) na \(\Omega\), projekcji

\[
q_E:\Omega\to\Omega/E
\]

i deterministycznej mapy

\[
\delta:\Omega\to\Omega
\]

następujące warunki są równoważne:

1. zachodzi kongruencja
   \[
   xEy\Longrightarrow\delta(x)E\delta(y);
   \]

2. istnieje dokładnie jedna mapa
   \[
   \bar\delta:\Omega/E\to\Omega/E
   \]
   taka, że
   \[
   \boxed{\bar\delta\circ q_E=q_E\circ\delta.}
   \]

W takim przypadku

\[
\boxed{
\bar\delta([x]_E)=[\delta(x)]_E.
}
\]

---

## 4. Dowód

### Kierunek \(1\Rightarrow2\)

Załóżmy

\[
xEy\Longrightarrow\delta(x)E\delta(y).
\]

Definiujemy

\[
\bar\delta([x]_E):=[\delta(x)]_E.
\]

Musimy sprawdzić dobrą określoność.

Jeżeli

\[
[x]_E=[y]_E,
\]

to

\[
xEy.
\]

Z kongruencji wynika

\[
\delta(x)E\delta(y),
\]

a więc

\[
[\delta(x)]_E=[\delta(y)]_E.
\]

Definicja \(\bar\delta\) nie zależy zatem od wyboru reprezentanta.

Dla każdego \(x\in\Omega\):

\[
(\bar\delta\circ q_E)(x)
=
\bar\delta([x]_E)
=
[\delta(x)]_E
=
(q_E\circ\delta)(x).
\]

Stąd

\[
\bar\delta\circ q_E=q_E\circ\delta.
\]

Pozostaje unikalność. Jeżeli

\[
h:\Omega/E\to\Omega/E
\]

również spełnia

\[
h\circ q_E=q_E\circ\delta,
\]

to dla każdej klasy \([x]_E\):

\[
h([x]_E)
=h(q_E(x))
=q_E(\delta(x))
=[\delta(x)]_E
=\bar\delta([x]_E).
\]

Zatem

\[
h=\bar\delta.
\]

### Kierunek \(2\Rightarrow1\)

Załóżmy, że istnieje

\[
\bar\delta:\Omega/E\to\Omega/E
\]

taka, że

\[
\bar\delta\circ q_E=q_E\circ\delta.
\]

Niech

\[
xEy.
\]

Wtedy

\[
q_E(x)=q_E(y).
\]

Stąd

\[
q_E(\delta(x))
=(\bar\delta\circ q_E)(x)
=(\bar\delta\circ q_E)(y)
=q_E(\delta(y)).
\]

Równość klas ilorazowych oznacza

\[
\delta(x)E\delta(y).
\]

Zatem \(E\) jest kongruencją dla \(\delta\). \(\square\)

---

## 5. Statyczna adekwatność nie wystarcza

II.5 odpowiadało na pytanie, czy sklejenie zachowuje dokładną informację zadaniową. II.6 odpowiada na inne pytanie:

\[
\boxed{
\text{czy dynamika jest zgodna z tym sklejeniem?}
}
\]

Może więc zachodzić

\[
E\subseteq E_{\mathcal T,c}
\]

— nawet z równością \(E=E_{\mathcal T,c}\) — a mimo to \(\delta\) nie musi schodzić na \(\Omega/E\).

### Kontrprzykład

Niech

\[
\Omega=\{a,b,c\},
\]

a klasy relacji \(E\) będą

\[
\{a,b\},\qquad\{c\}.
\]

Niech

\[
\delta(a)=a,
\qquad
\delta(b)=c,
\qquad
\delta(c)=c.
\]

Mamy

\[
aEb,
\]

ale

\[
\delta(a)=a
\not E
c=\delta(b).
\]

Zatem \(E\) nie jest kongruencją dla \(\delta\).

Próba zdefiniowania

\[
\bar\delta([a]_E)
\]

zależy od reprezentanta:

\[
[a]_E=[b]_E,
\]

lecz

\[
[\delta(a)]_E=[a]_E,
\qquad
[\delta(b)]_E=[c]_E.
\]

Nie istnieje więc jednoznaczna dynamika ilorazowa.

Ten świadek utrwala rygiel:

\[
\boxed{
\text{statyczna legalność informacyjna redukcji}
\not\Rightarrow
\text{dynamiczna projektowalność}.
}
\]

---

## 6. Specjalizacja PSI do równoważności zadaniowej

Dla

\[
E=E_{\mathcal T,c}
\]

i

\[
M_{\mathcal T,c}=\Omega_c/E_{\mathcal T,c}
\]

dynamika

\[
\delta_c:\Omega_c\to\Omega_c
\]

schodzi do jednoznacznej mapy

\[
\bar\delta_{\mathcal T,c}:M_{\mathcal T,c}\to M_{\mathcal T,c}
\]

takiej, że

\[
\boxed{
\bar\delta_{\mathcal T,c}\circ q_{\mathcal T,c}
=
q_{\mathcal T,c}\circ\delta_c
}
\]

wtedy i tylko wtedy, gdy

\[
\boxed{
xE_{\mathcal T,c}y
\Longrightarrow
\delta_c(x)E_{\mathcal T,c}\delta_c(y).}
\]

Wtedy

\[
\bar\delta_{\mathcal T,c}([x]_{\mathcal T,c})
=
[\delta_c(x)]_{\mathcal T,c}.
\]

Warunek ten nie wynika automatycznie z definicji \(E_{\mathcal T,c}\), chyba że użyte domknięcie zadaniowe i kontrakt zostały skonstruowane tak, by zapewnić odpowiednią stabilność transportu. W każdym konkretnym zastosowaniu należy sprawdzić hipotezy, a nie zakładać zejścia dynamiki przez sam zapis ilorazu.

---

## 7. Dowolny iloraz pośredni

Niech

\[
Q\subseteq\Omega\times\Omega
\]

będzie dowolną relacją równoważności i

\[
q_Q:\Omega\to\Omega/Q.
\]

Jeżeli \(Q\) jest zadaniowo legalna informacyjnie,

\[
Q\subseteq E_{\mathcal T},
\]

to nadal osobno trzeba sprawdzić

\[
\boxed{
xQy\Longrightarrow\delta(x)Q\delta(y).}
\]

Pierwszy warunek kontroluje **utrzymanie rozróżnień zadaniowych**. Drugi kontroluje **dobrą określoność dynamiki zredukowanej**.

Są to odrębne bramki.

---

## 8. Status źródłowy

Twierdzenie II.6 jest elementarnym klasycznym kryterium projektowalności mapy na iloraz przez relację kongruencji.

Status:

\[
\boxed{
\text{CLASSICAL CONGRUENCE / QUOTIENT-DYNAMICS FACT}
\; / \;
\text{PSI-ADAPTED DYNAMIC BRIDGE}.
}
\]

PSI nie rości sobie autorstwa ogólnego twierdzenia o funkcji indukowanej na ilorazie. Rola PSI polega na związaniu tego kryterium z zadaniową relacją równoważności oraz z obowiązkiem oddzielenia statycznej adekwatności reprezentacji od dynamicznej projektowalności.

---

## 9. Granica deterministyczna

Twierdzenie II.6 dotyczy mapy

\[
\delta:\Omega\to\Omega.
\]

Nie wolno automatycznie zastępować \(\delta\) przez kernel przejścia Markowa i zachować tego samego twierdzenia słowo w słowo.

Dla procesów stochastycznych właściwym klasycznym warunkiem jest odpowiednia lumpowalność: rozkład masy przejścia do każdego bloku musi być zgodny między reprezentantami. Ta warstwa zostanie omówiona później jako klasyczny most, nie jako część dowodu II.6.

W szczególności:

\[
\boxed{
\text{deterministyczna kongruencja}
\neq
\text{stochastyczna lumpowalność}.
}
\]

---

## 10. Czego Twierdzenie II.6 nie ustanawia

Nie ustanawia automatycznie:

- zadaniowej adekwatności samego ilorazu;
- pełnej legalności kontraktowej redukcji;
- stabilności numerycznej \(\bar\delta\);
- ciągłości, mierzalności albo gładkości \(\bar\delta\);
- odwracalności dynamiki;
- istnienia generatora lub półgrupy ciągłoczasowej;
- lumpowalności procesu stochastycznego;
- skończoności lub efektywnej obliczalności przestrzeni ilorazowej.

Każda z tych własności wymaga dodatkowych hipotez.

---

## 11. Przejście do historii i pamięci

W warstwie historii obiektami będą

\[
H_t\in\mathcal H_t,
\]

a równoważność

\[
\equiv_{\mathcal T,t}
\]

będzie kodować zgodność przyszłej semantyki zadania.

Najpierw zastosujemy kryterium reprezentacji II.4 do pamięci

\[
\rho_t:\mathcal H_t\to Z_t,
\]

otrzymując

\[
\boxed{
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

Dopiero potem wrócimy do warunku kongruencji, aby zbudować dobrze określoną aktualizację ilorazową historii.

To będzie warstwa II.7–II.9.
