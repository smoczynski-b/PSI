# PRINCIPIA SEMANTICA — TOM II
## II.14. CAT–FACT–NORM–MINI: dokładna identyfikowalność klasy normalnej

**Status:** `BRIDGE / EXACT-NOISELESS MINI / THEOREM PROSE PASS 02 / ERRATA-CORRECTED`  
**Źródło nadrzędne PSI:** fizyczny `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-13.md`, C19-v3 + C20 + C67  
**Źródło robocze:** `cat-fact-norm-mini-02.md`  
**Falsifikatory:** F55, F56, F59, F62  
**Errata:** `principia-v1-v2-freeze-01-errata-01.md`  
**Zakres:** regularne krzywe `C^3` na zwartym przedziale; dokładna obserwacja; zachowany parametr czasu; skończona gramatyka `{F,B}`.

---

## 1. Dwa legalne kontrakty

Niech

\[
\gamma:[0,T]\to\mathbb R^3,
\qquad
\gamma\in C^3,
\qquad
\|\dot\gamma(t)\|>0.
\]

Parametr czasu jest częścią kontraktu.

### Kontrakt absolutny

\[
P_0^{abs}:Y_{abs}=\gamma(t),
\qquad
G_{abs}=SO(2)_{normal}.
\]

Zewnętrzne `SE(3)` nie jest automatycznie gauge stałego włókna współrzędnościowego.

### Kontrakt kształtu

\[
P_0^{shape}:Y_{shape}=[\gamma]_{SE(3)},
\qquad
G_{shape}=SE(3)\times SO(2)_{normal}.
\]

To rozdzielenie pozostaje trwałym wynikiem audytu F55.

---

## 2. Gramatyka i rewrite

Używamy skończonej gramatyki

\[
\mathcal L_{FB}=\{F,B\}.
\]

Terminy zawierają dane realizacji na kolejnych przedziałach jednej dokładnej
krzywej: położenie, styczną i, dla atomu Bishopa, zorientowaną ramę normalną.
Same trójki skalarów wymagają tych danych początkowych do rekonstrukcji.
W kontrakcie kształtu najpierw wybieramy wspólny reprezentant przez `SE(3)`.
Stosujemy długość łuku \(s\); znana prędkość zachowuje zadany parametr czasu.

Na przedziale Frenet-legalnym:

\[
F_I=(v,\kappa,\tau)_I
\longrightarrow
B_I=(v,k_1,k_2)_I,
\]

przy czym wszystkie wybory stałej całkowania są dozwolonymi wynikami recode.
Obrót nowej ramy tylko na tym atomie nie jest globalnym gauge całego terminu.

Dla sąsiednich atomów Bishopa:

\[
B_{I_1}\oplus B_{I_2}
\longrightarrow
B_{I_1\cup I_2}
\]

Łączenie zachowuje ramę lewego atomu. Jedyny stały obrót `SO(2)` wyrównujący
ramę prawego atomu na wspólnym końcu stosujemy do całego prawego atomu i jego
współrzędnych krzywizny. Jest to krok normalizacji. Zbieżność położenia i
stycznej wynika z kompatybilności z tą samą dokładną krzywą; samo dopasowanie
końców dwóch dowolnych krzywych nie jest wystarczającą przesłanką.

Globalny `SO(2)` działa jednym obrotem na wszystkie ramy Bishopa terminu;
nie dodajemy iloczynu niezależnych obrotów segmentów do relacji gauge.
Relacja recode jest ekwiwariantna: globalny obrót danych i wybranego wyniku
daje ponownie legalny krok. Dlatego schodzi na zadeklarowane klasy gauge.

Rewrite jest formułowany na legalnych klasach gauge; gauge i rewrite nie są tą samą relacją.

---

## 3. Terminacja i konfluencja

Dla terminu `X` definiujemy

\[
\mu(X)=\bigl(n_F(X),n_{seg}(X)\bigr)
\]

z porządkiem leksykograficznym.

`F→B` zmniejsza `n_F`, a merge Bishopa zmniejsza `n_seg` bez zwiększania `n_F`. Zatem rewrite terminates.

Każdy termin nieredukowalny jest jednym globalnym atomem Bishopa: atom
Freneta dopuszcza recode, a dwa sąsiednie atomy Bishopa dopuszczają merge.
Lemat geometryczny i dowód w §5 pokazują, że każde dwa takie wyniki nad
ustalonym `Y` różnią się jednym globalnym obrotem. Zatem dowolne dwie
redukcje można doprowadzić do tej samej klasy normalnej. To dowodzi:

\[
\boxed{
\text{rewrite jest konfluentny modulo legalny gauge}.
}
\]

Wynikiem jest jedna **klasa normalna**, nie kanoniczny reprezentant ramy.

---

## 4. Gauge-only factorization candidate space

Dla ustalonego kontraktu `P` definiujemy

\[
\operatorname{RawFact}^{0}_{FB,P}(Y)
\]

jako zbiór legalnych skończonych terminów `{F,B}` zgodnych z obserwacją oraz

\[
\boxed{
\mathfrak F^{0}_{FB,P}(Y)
:=
\operatorname{RawFact}^{0}_{FB,P}(Y)/G_P.
}
\]

Ten obiekt może mieć wiele elementów.

Kontrprzykład do dawnej tezy o singletonie:

\[
B_{[0,L]}
\quad\text{oraz}\quad
B_{[0,a]}\oplus B_{[a,L]}
\]

są różnymi segmentacjami. Stały obrót normalny nie usuwa granicy segmentacji, więc terminy nie muszą być gauge-equivalent.

Dlatego wycofujemy:

\[
|\mathfrak F^{0}_{FB,P}(Y)|=1.
\]

To jest F62.

---

## 5. Twierdzenie II.14.A — jednoznaczna klasa normalna

### Lemat — jednoznaczność między różnymi terminami wejściowymi

Niech \(T(s)\) będzie styczną jednostkową dokładnej regularnej krzywej.
Rama Bishopa spełnia liniowe równanie

\[
N_i'(s)=-\langle T'(s),N_i(s)\rangle T(s),\qquad i=1,2.
\]

Ciągłe współczynniki dają istnienie i jednoznaczność na całym zwartym
przedziale dla każdej początkowej zorientowanej pary normalnej. Równanie
zachowuje \(\langle N_i,T\rangle=0\) i \(\langle N_i,N_j\rangle=\delta_{ij}\),
co wynika przez różniczkowanie. Dwie początkowe pary różnią się jednym
\(R\in SO(2)\). Stała kombinacja \((N_1,N_2)R\) spełnia to samo równanie
i drugie dane początkowe, więc przez jednoznaczność zgadza się z drugą
ramą na całym przedziale. Współrzędne \(k_i=\langle T',N_i\rangle\)
transformują się odpowiednio tym samym stałym wyborem bazy.

W merge wyrównane rozwiązania mają te same dane na wspólnym końcu,
więc są ograniczeniami jednego rozwiązania globalnego. Wynik kolejnych
merge nie zależy od nawiasowania. W kontrakcie kształtu argument stosujemy
po wyrównaniu realizacji przez jeden element `SE(3)`; dla obserwacji
absolutnej położenie jest już ustalone i nie bierzemy tego ilorazu.

W szczególności porównanie dotyczy także ram otrzymanych z **różnych**
segmentacji i różnych terminów wejściowych, nie tylko dwóch redukcji
tego samego terminu. Globalny atom Bishopa istnieje, więc włókno nie jest puste.

### Mapa normalizacji

Terminacja i powyższa jednoznaczność definiują mapę normalizacji

\[
\operatorname{NF}_{FB,P,Y}:
\mathfrak F^{0}_{FB,P}(Y)
\to
\mathcal N_{FB,P}(Y).
\]

Dla dokładnego interwałowego kontraktu:

\[
\boxed{
|\operatorname{im}\operatorname{NF}_{FB,P,Y}|=1.
}
\]

### Dowód

Każdy legalny termin redukuje się do pojedynczego globalnego atomu Bishopa.
Lemat porównuje wyniki dowolnych dwóch terminów nad tym samym `Y` i daje
ich równoważność modulo zadeklarowany globalny gauge. Obraz `NF` jest więc
niepusty i ma jeden element. Sama terminacja i konfluencja nie wystarczyłyby:
zbiór dwóch nieredukowalnych symboli bez reguł jest terminujący i konfluentny,
ale ma dwie postacie normalne. `\square`

---

## 6. Wniosek II.14.B — task-level singleton

Definiujemy na `\mathfrak F^{0}_{FB,P}(Y)` relację

\[
X\equiv_{NF}X'
\iff
\operatorname{NF}(X)=\operatorname{NF}(X').
\]

Wtedy

\[
\boxed{
\left|
\mathfrak F^{0}_{FB,P}(Y)/\!\equiv_{NF}
\right|=1.
}
\]

To jest dokładna identyfikowalność **normal-form task quotient**, nie dosłowna jednoznaczność faktoryzacji modulo realizacyjny gauge.

---

## 7. Gauge ≠ recode

Poprawka jest istotna semantycznie:

\[
\boxed{
\text{realization equivalence}
\neq
\text{behavioural recoding / normalization}.
}
\]

`SO(2)` i — w kontrakcie kształtu — `SE(3)` są gauge.

Natomiast

\[
F\to B
\]

i

\[
B\oplus B\to B
\]

są operacjami normalizacji/recode. Mogą identyfikować terminy względem zadania normalnej postaci, lecz nie wolno ich po cichu dodawać do realizacyjnej relacji gauge.

---

## 8. Punkt `\kappa=0`

Jeżeli `\kappa=0`, ale krzywa pozostaje regularna, rama Freneta może przestać być legalna, podczas gdy opis Bishopa pozostaje legalny.

Dlatego:

\[
\boxed{
\text{Frenet failure at }\kappa=0
\to
\text{recode/domain repair},
}
\]

nie automatyczny catalog birth.

C20 przeżywa erratę bez zmiany.

---

## 9. Granice

II.14 nie ustanawia:

- singletonu gauge-only factorization fibre;
- generalnej identyfikowalności PSI-FACT;
- stabilności z danych próbkowanych/szumowych;
- periodicznej normalizacji dla krzywych zamkniętych;
- gauge przez reparametryzację czasu;
- quotientu przez odbicia bez osobnego kontraktu;
- nieistotności stabilizatorów lub wyższych świadków w innych zadaniach;
- nowego twierdzenia Freneta/Bishopa.

---

## 10. Lokalny cross-check po Errata 01

### F55
`PASS`: kontrakt absolutny i kształtu pozostają rozdzielone.

### F56
`PASS AFTER CORRECTION`: recode jest ekwiwariantny; lokalne wyrównanie ram
pozostaje normalizacją, a lemat ODE porównuje różne terminy wejściowe.
Dowód i zakres korekty: [targeted repair evidence](repair-audit.md).

### F59
`PASS`: MINI nie redefiniuje generalnego PSI-FACT.

### F62
`PASS`: singleton dotyczy obrazu `NF` / task quotient, nie `RawFact/G`.

### C67
`PASS`: normal-form identifiability pozostaje słabsza od literal factorization uniqueness.

### Freeze impact
`PASS WITH ERRATA`: Freeze 01 pozostaje aktywny subject to `principia-v1-v2-freeze-01-errata-01.md`.

---

## 11. Werdykt II.14

\[
\boxed{
\mathrm{II.14\ NORMAL\!-\!FORM\ MINI}
=\mathrm{PASS\ AFTER\ ERRATA\ 01}.
}
\]

Następny krok: globalny cross-check II.13–II.14 przed przejściem do FRAME.
