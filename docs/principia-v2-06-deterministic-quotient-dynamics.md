# PRINCIPIA SEMANTICA — TOM II
## II.6. Deterministyczna dynamika ilorazowa

**Status:** `THEOREM PROSE PASS 01 / PROOF PASS / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, C10 zachowane przez Freeze 01  
**Mapa twierdzeń:** `principia-v2-theorem-map-02.md`, II.6  
**Klasa:** klasyczne kryterium kongruencji / adaptacja do dynamiki ilorazowej PSI.  
**Granica:** twierdzenie deterministyczne; nie jest twierdzeniem o lumpowalności łańcuchów Markowa.

---

## 1. Typy

Niech \(\Omega\) będzie zbiorem, \(E\subseteq\Omega\times\Omega\) relacją równoważności,

\[
q_E:\Omega\to\Omega/E
\]

projekcją ilorazową, a

\[
\delta:\Omega\to\Omega
\]

całkowitą deterministyczną mapą jednego kroku.

Pytamy, kiedy istnieje mapa

\[
\bar\delta:\Omega/E\to\Omega/E
\]

spełniająca

\[
\boxed{\bar\delta\circ q_E=q_E\circ\delta.}
\]

Jeżeli taka mapa istnieje, dynamika \(\delta\) schodzi na iloraz.

---

## 2. Kongruencja dynamiki

Relację \(E\) nazywamy kongruencją dla \(\delta\), jeżeli

\[
\boxed{xEy\Longrightarrow\delta(x)E\delta(y).}
\]

Warunek mówi dokładnie, że wybór reprezentanta klasy \([x]_E\) nie może zmienić klasy następnego stanu. Jest to bramka dynamiczna; nie wynika z samej statycznej adekwatności ilorazu.

---

## 3. Twierdzenie II.6 — kryterium zejścia dynamiki na iloraz

Dla \(E\), \(q_E\) i \(\delta\) jak wyżej następujące warunki są równoważne:

1. \(E\) jest kongruencją dla \(\delta\):
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
\boxed{\bar\delta([x]_E)=[\delta(x)]_E.}
\]

---

## 4. Dowód

### \(1\Rightarrow2\)

Definiujemy

\[
\bar\delta([x]_E):=[\delta(x)]_E.
\]

Jeżeli \([x]_E=[y]_E\), to \(xEy\), a więc z kongruencji

\[
\delta(x)E\delta(y),
\]

czyli

\[
[\delta(x)]_E=[\delta(y)]_E.
\]

Mapa jest dobrze określona. Ponadto

\[
(\bar\delta\circ q_E)(x)
=\bar\delta([x]_E)
=[\delta(x)]_E
=(q_E\circ\delta)(x).
\]

Jeżeli \(h:\Omega/E\to\Omega/E\) również spełnia \(h\circ q_E=q_E\circ\delta\), to dla każdej klasy

\[
h([x]_E)=h(q_E(x))=q_E(\delta(x))=[\delta(x)]_E=\bar\delta([x]_E),
\]

więc \(h=\bar\delta\).

### \(2\Rightarrow1\)

Jeżeli \(xEy\), to \(q_E(x)=q_E(y)\). Z komutatywności:

\[
q_E(\delta(x))
=(\bar\delta\circ q_E)(x)
=(\bar\delta\circ q_E)(y)
=q_E(\delta(y)).
\]

Zatem

\[
\delta(x)E\delta(y).
\]

To kończy dowód. \(\square\)

---

## 5. Statyczna adekwatność nie wystarcza

II.5 odpowiada na pytanie, czy sklejenie zachowuje dokładną informację zadaniową. II.6 odpowiada na inne pytanie:

\[
\boxed{\text{czy dynamika jest zgodna z tym sklejeniem?}}
\]

Może zachodzić \(E\subseteq E_{\mathcal T,c}\), nawet \(E=E_{\mathcal T,c}\), a mimo to \(\delta\) nie musi schodzić na \(\Omega/E\).

### Kontrprzykład

Niech

\[
\Omega=\{a,b,c\},
\]

z klasami \(E\):

\[
\{a,b\},\qquad\{c\}.
\]

Niech

\[
\delta(a)=a,\qquad\delta(b)=c,\qquad\delta(c)=c.
\]

Mamy \(aEb\), ale

\[
\delta(a)=a\not E c=\delta(b).
\]

Zatem \(E\) nie jest kongruencją. Próba zdefiniowania \(\bar\delta([a]_E)\) zależy od reprezentanta, ponieważ

\[
[a]_E=[b]_E,
\]

lecz

\[
[\delta(a)]_E=[a]_E,
\qquad
[\delta(b)]_E=[c]_E.
\]

Stąd rygiel:

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
E=E_{\mathcal T,c},
\qquad
M_{\mathcal T,c}=\Omega_c/E_{\mathcal T,c},
\]

dynamika

\[
\delta_c:\Omega_c\to\Omega_c
\]

schodzi do jednoznacznej

\[
\bar\delta_{\mathcal T,c}:M_{\mathcal T,c}\to M_{\mathcal T,c}
\]

wtedy i tylko wtedy, gdy

\[
\boxed{xE_{\mathcal T,c}y\Longrightarrow\delta_c(x)E_{\mathcal T,c}\delta_c(y).}
\]

Wtedy

\[
\boxed{
\bar\delta_{\mathcal T,c}\circ q_{\mathcal T,c}
=
q_{\mathcal T,c}\circ\delta_c
}
\]

i

\[
\bar\delta_{\mathcal T,c}([x]_{\mathcal T,c})
=[\delta_c(x)]_{\mathcal T,c}.
\]

Publiczny rdzeń definiuje

\[
\mathscr R_{\mathcal T,c}
=
\operatorname{Cl}^{\mathcal T}_{\delta_c}(\mathscr O_{\mathcal T,c})
\]

jako domknięcie zawierające te transporty przez \(\delta_c\), których wymaga kontrakt. Nie oznacza to bez dodatkowego zapisu automatycznie pełnej stabilności względem prekompozycji przez \(\delta_c\).

### Warunek wystarczający wynikający z domknięcia

Jeżeli kontrakt zapewnia

\[
\boxed{
R\in\mathscr R_{\mathcal T,c}
\Longrightarrow
R\circ\delta_c\in\mathscr R_{\mathcal T,c}
}
\]

dla każdego \(R\in\mathscr R_{\mathcal T,c}\), to \(E_{\mathcal T,c}\) jest automatycznie kongruencją dla \(\delta_c\).

Istotnie, jeśli \(xE_{\mathcal T,c}y\), to dla każdego \(R\in\mathscr R_{\mathcal T,c}\)

\[
(R\circ\delta_c)(x)=(R\circ\delta_c)(y),
\]

bo \(R\circ\delta_c\in\mathscr R_{\mathcal T,c}\). Stąd

\[
R(\delta_c(x))=R(\delta_c(y))
\]

dla każdego \(R\), a więc

\[
\delta_c(x)E_{\mathcal T,c}\delta_c(y).
\]

Jest to konsekwencja definicji domknięcia przy tej dodatkowej własności, nie nowy prymityw PSI.

---

## 7. Dowolny iloraz pośredni

Dla relacji równoważności \(Q\) i projekcji

\[
q_Q:\Omega\to\Omega/Q
\]

zadaniowa legalność informacyjna

\[
Q\subseteq E_{\mathcal T}
\]

nie wystarcza do zdefiniowania dynamiki na \(\Omega/Q\). Osobno trzeba sprawdzić

\[
\boxed{xQy\Longrightarrow\delta(x)Q\delta(y).}
\]

Pierwszy warunek kontroluje utrzymanie rozróżnień zadaniowych. Drugi kontroluje dobrą określoność dynamiki zredukowanej. Są to odrębne bramki.

---

## 8. Status źródłowy

Twierdzenie II.6 jest elementarnym klasycznym kryterium projektowalności mapy na iloraz przez relację kongruencji.

\[
\boxed{
\text{CLASSICAL CONGRUENCE / QUOTIENT-DYNAMICS FACT}
\; / \;
\text{PSI-ADAPTED DYNAMIC BRIDGE}.
}
\]

PSI nie rości sobie autorstwa ogólnego twierdzenia o funkcji indukowanej na ilorazie. Rola PSI polega na związaniu tego kryterium z zadaniową relacją równoważności oraz na oddzieleniu statycznej adekwatności reprezentacji od dynamicznej projektowalności.

---

## 9. Granica deterministyczna

Twierdzenie II.6 dotyczy mapy

\[
\delta:\Omega\to\Omega.
\]

Nie wolno automatycznie zastępować \(\delta\) przez kernel przejścia Markowa i zachować tego samego kryterium słowo w słowo. Dla procesów stochastycznych właściwą klasyczną warstwą jest lumpowalność.

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

W warstwie historii obiektami będą \(H_t\in\mathcal H_t\), a równoważność

\[
\equiv_{\mathcal T,t}
\]

będzie kodować zgodność przyszłej semantyki zadania.

Najpierw zastosujemy II.4 do pamięci

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

Dopiero potem wrócimy do kongruencji, aby zbudować dobrze określoną aktualizację ilorazową historii. To będzie warstwa II.7–II.9.
