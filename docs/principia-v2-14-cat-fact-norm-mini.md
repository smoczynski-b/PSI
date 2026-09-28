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

Na przedziale Frenet-legalnym:

\[
F_I=(v,\kappa,\tau)_I
\longrightarrow
B_I=(v,k_1,k_2)_I,
\]

przy czym zmiana stałej całkowania odpowiada stałemu gauge `SO(2)_{normal}`.

Dla sąsiednich atomów Bishopa:

\[
B_{I_1}\oplus B_{I_2}
\longrightarrow
B_{I_1\cup I_2}
\]

po wyrównaniu normal-frame gauge.

Rewrite jest formułowany na legalnych klasach gauge; gauge i rewrite nie są tą samą relacją.

---

## 3. Terminacja i konfluencja

Dla terminu `X` definiujemy

\[
\mu(X)=\bigl(n_F(X),n_{seg}(X)\bigr)
\]

z porządkiem leksykograficznym.

`F→B` zmniejsza `n_F`, a merge Bishopa zmniejsza `n_seg` bez zwiększania `n_F`. Zatem rewrite terminates.

Lokalne interakcje są następujące:

1. rozłączne recode Freneta komutują;
2. dwa merge w potrójnym ciągu Bishopa prowadzą do tej samej globalnej klasy po wyrównaniu gauge;
3. rozłączne recode/merge komutują.

Zatem rewrite jest lokalnie konfluentny. Z lematu Newmana:

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

Konfluencja definiuje mapę normalizacji

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

Każdy legalny termin redukuje się, przez terminację, do terminu normalnego. Terminu normalnego nie może zawierać atomu Freneta ani dwóch sąsiednich atomów Bishopa. Jest więc pojedynczym globalnym atomem Bishopa. Konfluencja gwarantuje, że wszystkie ciągi redukcji prowadzą do tej samej klasy normalnej. `\square`

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
`PASS`: confluence jest stosowana dopiero po zejściu rewrite na klasy gauge.

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
