# PRINCIPIA SEMANTICA — TOM II
## II.14. CAT–FACT–NORM–MINI: dokładna klasa normalna Freneta/Bishopa

**Status:** `BRIDGE / EXACT-NOISELESS MINI / THEOREM PROSE PASS 01 / LOCAL CROSS-CHECK PASS`  
**Źródło nadrzędne PSI:** fizyczny `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, zachowane C19-v2 i C20  
**Źródło robocze:** `cat-fact-norm-mini-01.md` po audycie kontraktu  
**Falsifikatory:** F55, F56, F59  
**Źródło klasyczne użyte w dowodzie:** lemat Newmana — terminacja + lokalna konfluencja implikuje konfluencję  
**Zakres:** regularne krzywe `C^3` na zwartym przedziale; dokładna obserwacja; zachowany parametr czasu; skończona gramatyka `{F,B}`; bez twierdzenia o stabilności statystycznej, pętlach zamkniętych, reparametryzacji czasu lub ogólnym PSI-FACT.

---

## 1. Krzywa i dwa legalne kontrakty obserwacji

Niech

\[
\gamma:[0,T]\to\mathbb R^3
\]

będzie klasy `C^3` i regularna:

\[
\|\dot\gamma(t)\|>0
\qquad\forall t\in[0,T].
\]

Parametr czasu jest częścią kontraktu i nie podlega reparametryzacji.

Wewnętrzny gauge prezentacyjny ramy Bishopa jest stałym obrotem z

\[
SO(2)_{\rm normal}.
\]

Rozpatrujemy dwa różne kontrakty obserwacji.

### (A) Kontrakt współrzędnych absolutnych

\[
\boxed{
P_0^{\rm abs}:\quad Y_{\rm abs}=\gamma(t).
}
\]

Obserwowana jest pełna krzywa w ustalonym układzie współrzędnych. Zewnętrzne `SE(3)` nie jest automatycznie gauge tego samego włókna obserwacyjnego.

### (B) Kontrakt kształtu

\[
\boxed{
P_0^{\rm shape}:\quad Y_{\rm shape}=[\gamma]_{SE(3)}.
}
\]

lub równoważny jawnie `SE(3)`-niezmienniczy odczyt. W tym kontrakcie legalny zewnętrzny gauge zawiera `SE(3)`.

Dlatego odpowiednie grupy ilorazowe są różne:

\[
G_{\rm abs}=SO(2)_{\rm normal},
\]

\[
G_{\rm shape}=SE(3)\times SO(2)_{\rm normal}.
\]

To rozdzielenie jest trwałą korektą F55.

---

## 2. Atomy Freneta i Bishopa

Na przedziale, na którym

\[
\kappa>0,
\]

dopuszczalny atom Freneta zapisujemy jako

\[
F_I=(v,\kappa,\tau)_I.
\]

Atom Bishopa ma postać

\[
B_I=(v,k_1,k_2)_I,
\]

gdzie rama względnie równoległa spełnia

\[
T'=k_1N_1+k_2N_2,
\]

\[
N_1'=-k_1T,
\qquad
N_2'=-k_2T.
\]

Zmiana początkowej zorientowanej bazy płaszczyzny normalnej przez stały element `SO(2)` obraca parę `(k_1,k_2)`. Dane kanoniczne są więc klasą

\[
[k_1,k_2]_{SO(2)},
\]

a nie wyróżnioną parą współrzędnych.

---

## 3. Skończona gramatyka

Ustalmy

\[
\mathcal L_{FB}=\{F,B\}.
\]

Termin gramatyki jest skończoną konkatenacją legalnych atomów na kolejnych podprzedziałach pokrywających całą krzywą i rekonstruujących tę samą regularną realizację z poprawnym sklejeniem położenia i stycznej.

Rewrite będzie rozpatrywany **na klasach stałego gauge `SO(2)_{normal}`**, a nie na dowolnie wybranych reprezentantach ramy.

To jest wymagane przez F56.

---

## 4. Reguła recode Frenet → Bishop

Na przedziale Frenet-legalnym wybieramy `\theta` spełniające

\[
\theta'=-\tau.
\]

W ustalonej konwencji:

\[
k_1=\kappa\cos\theta,
\qquad
k_2=-\kappa\sin\theta.
\]

Stała całkowania zmienia tylko globalną rotację normalną.

Definiujemy więc legalny recode

\[
\boxed{
R_F:F_I\longrightarrow B_I.
}
\]

Nie jest to `birth` ani gauge; jest to zmiana reprezentacji w tym samym katalogu realizacyjnym.

---

## 5. Reguła sklejenia Bishopa

Dla dwóch sąsiednich atomów Bishopa reprezentujących tę samą krzywą

\[
B_{I_1}\oplus B_{I_2}
\]

ich ramy normalne na wspólnym końcu różnią się jednym stałym obrotem `SO(2)`. Po wyrównaniu tego gauge transport względnie równoległy daje jedną ramę na sumie przedziałów:

\[
\boxed{
R_M:B_{I_1}\oplus B_{I_2}\longrightarrow B_{I_1\cup I_2}.
}
\]

---

## 6. Terminacja

Dla terminu `X` zdefiniujmy

\[
\mu(X)=\bigl(n_F(X),n_{\rm seg}(X)\bigr)
\in\mathbb N^2
\]

z porządkiem leksykograficznym.

- `R_F` zmniejsza `n_F`;
- `R_M` nie zwiększa `n_F` i zmniejsza `n_seg`.

Każdy krok rewrite ściśle zmniejsza `\mu`, więc nie istnieje nieskończony łańcuch redukcji.

\[
\boxed{
\text{rewrite terminates}.
}
\]

---

## 7. Lokalna konfluencja

Na klasach gauge występują trzy typy lokalnych interakcji:

1. dwa rozłączne recode Freneta — kroki komutują;
2. dwa możliwe sklejenia w potrójnym ciągu Bishopa — oba porządki prowadzą do tej samej globalnej klasy ramy po wyrównaniu gauge;
3. recode Freneta i merge Bishopa — nie tworzą tego samego nakładającego się redexu; rozłączne kroki komutują.

Zatem rewrite jest lokalnie konfluentny na klasach `SO(2)_{normal}`.

Wraz z terminacją lemat Newmana daje:

\[
\boxed{
\text{rewrite jest konfluentny modulo legalny gauge}.
}
\]

PSI nie rości nowości dla lematu Newmana.

---

## 8. Twierdzenie II.14.A — jednoznaczna klasa normalna MINI

Dla każdego legalnego skończonego terminu Frenet/Bishop reprezentującego tę samą regularną krzywą na `[0,T]`, w jednym z dwóch poprawnie otypowanych kontraktów obserwacji, wszystkie maksymalne ciągi rewrite prowadzą do tej samej klasy Bishopa modulo stały gauge normalny.

Normalne dane mają postać

\[
\boxed{
N_{FB}(\gamma)
=
\bigl(v(t),[k_1(s),k_2(s)]_{SO(2)}\bigr).
}
\]

### Dowód

Terminacja została wykazana w §6, lokalna konfluencja w §7. Z lematu Newmana otrzymujemy konfluencję. Normalny termin nie może zawierać atomu Freneta, bo wtedy działa `R_F`, ani więcej niż jednego atomu Bishopa, bo wtedy działa `R_M`. Każdy maksymalny ciąg kończy się więc pojedynczym globalnym atomem Bishopa, a konfluencja identyfikuje jego klasę modulo `SO(2)_{normal}`. `\square`

---

## 9. Wniosek II.14.B — jednoelementowe włókno faktoryzacji MINI

Dla kontraktu absolutnego definiujemy ograniczone włókno

\[
\operatorname{Fact}^{0,\rm abs}_{FB,P_0}(Y_{\rm abs})
=
\operatorname{RawFact}^{0,\rm abs}_{FB,P_0}(Y_{\rm abs})
/SO(2)_{\rm normal}.
\]

Dla kontraktu kształtu:

\[
\operatorname{Fact}^{0,\rm shape}_{FB,P_0}(Y_{\rm shape})
=
\operatorname{RawFact}^{0,\rm shape}_{FB,P_0}(Y_{\rm shape})
/(SE(3)\times SO(2)_{\rm normal}).
\]

W obu przypadkach, w ograniczonej gramatyce MINI:

\[
\boxed{
\left|\operatorname{Fact}^{0}_{FB,P_0}(Y)\right|=1
}
\]

po zastosowaniu właściwego dla kontraktu legalnego quotientu.

Jest to twierdzenie o **tym konkretnym włóknie gramatycznym**, nie o generalnym PSI-FACT.

---

## 10. Punkt `\kappa=0`: recode/domain repair, nie automatyczny birth

Jeżeli krzywa pozostaje regularna, lecz

\[
\kappa=0
\]

w punkcie lub na części dziedziny, klasyczna rama Freneta traci legalność. Rama Bishopa pozostaje jednak naturalnym regularnym opisem w znacznie szerszym sektorze regularnych krzywych.

Dlatego w MINI:

\[
\boxed{
\text{Frenet failure at }\kappa=0
\to
\text{recode/domain repair},
}
\]

nie zaś automatycznie

\[
\boxed{
\text{catalog birth}.
}
\]

To jest C20 i konkretny świadek zasady II.13 §6.

---

## 11. Granice II.14

Twierdzenie nie obejmuje:

- punktów, w których `\dot\gamma=0`;
- reparametryzacji czasu jako gauge;
- statystycznej identyfikowalności z danych próbkowanych/szumowych;
- stabilności estymacji `\kappa` lub `\tau`;
- zamkniętych krzywych i globalnego problemu okresowości ramy;
- automatycznego quotientu przez odbicia, skoro kontrakt kształtu używa `SE(3)`, nie całego `O(3)`;
- generalnego PSI-FACT poza gramatyką `{F,B}`;
- zadań, w których stabilizatory, świadkowie kompatybilności lub wyższa struktura są istotne.

Te przypadki wymagają osobnych kontraktów lub późniejszych warstw.

---

## 12. Lokalny cross-check

### F55 — gauge/observation
`PASS`: kontrakt absolutny i kształtu są rozdzielone; `SE(3)` nie działa automatycznie w stałym włóknie `Y_abs`.

### F56 — rewrite/gauge
`PASS`: rewrite jest formułowany na klasach gauge przed zastosowaniem lematu Newmana.

### F59 — MINI/general FACT
`PASS`: wynik kardynalności jeden dotyczy wyłącznie ograniczonego włókna `{F,B}`.

### Źródła klasyczne
`PASS`: geometria Freneta/Bishopa i lemat Newmana są importowane, nie przypisywane PSI.

### Zakres
`PASS`: brak statystyki, pętli zamkniętych, reparametryzacji czasu i twierdzenia o wszystkich faktoryzacjach.

### Primitive growth
`PASS`: brak CORE6 i brak Agent v03.

---

## 13. Werdykt II.14

\[
\boxed{
\mathrm{II.14\ CAT\!-\!FACT\!-\!NORM\ MINI}
=\mathrm{PASS}.
}
\]

Blok CAT/FACT/NORM ma teraz dwie warstwy: II.13 ustala bieżący zakres kanoniczny, a II.14 dostarcza ograniczony dokładny benchmark. Następny krok: globalny cross-check II.13–II.14 przed przejściem do FRAME.
