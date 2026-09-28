# PRINCIPIA SEMANTICA — TOM II
## II.16. Wyższa kompatybilność, stabilizatory i legalność truncacji

**Status:** `CLASSICAL GROUPOID FACT / PSI BRIDGE / PROSE PASS 01 / LOCAL CROSS-CHECK PASS`  
**Źródło nadrzędne PSI:** fizyczny `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-13.md`, zachowane C29–C33  
**Źródło robocze:** `higher-fibre-01.md`  
**Zakres:** jawny świadek w kategorii małych 1-groupoidów; dokładna kompatybilność; brak uniwersalnego twierdzenia o wszystkich strukturach wyższych lub wszystkich homotopijnych włóknach PSI-FACT.

---

## 1. Minimalny świadek

Rozważmy diagram groupoidów

\[
*\longrightarrow B\mathbb Z_2\longleftarrow *,
\]

gdzie \(B\mathbb Z_2\) ma jeden obiekt oraz grupę automorfizmów

\[
\mathbb Z_2=\{e,s\}.
\]

Obie mapy wybierają jedyny obiekt groupoidu środkowego.

Jeżeli najpierw zapomnimy wszystkie morfizmy i pozostawimy tylko zbiory obiektów, otrzymujemy diagram jednoelementowych zbiorów. Jego ścisły pullback jest jednoelementowy:

\[
\boxed{
\{*\}\times_{\{*\}}\{*\}=\{*\}.
}
\]

---

## 2. 2-pullback / weak pullback groupoidów

W iso-comma modelu 2-pullbacku obiekt ma postać

\[
(*,*,\alpha),
\]

gdzie

\[
\alpha:*\to *
\]

jest izomorfizmem w \(B\mathbb Z_2\).

Zatem istnieją dwa obiekty:

\[
(*,*,e),
\qquad
(*,*,s).
\]

Groupoidy źródłowe są terminalne, więc ich jedyne morfizmy są identycznościami. Warunek morfizmu w iso-comma object nie identyfikuje \(e\) z \(s\). Otrzymujemy więc groupoid równoważny dyskretnemu dwuelementowemu groupoidowi:

\[
\boxed{
*\times^{h}_{B\mathbb Z_2}*
\simeq
\mathbb Z_2^{\mathrm{disc}}.
}
\]

W szczególności

\[
\boxed{
\left|\pi_0\!\left(*\times^{h}_{B\mathbb Z_2}*\right)\right|=2,
}
\]

podczas gdy po wcześniejszym coarse truncation

\[
\boxed{
\left|*\times_{\pi_0(B\mathbb Z_2)}*\right|=1.
}
\]

Dlatego w tym świadku

\[
\boxed{
\pi_0(A\times_C^hB)
\not\cong
\pi_0(A)\times_{\pi_0(C)}\pi_0(B).
}
\]

Jest to klasyczny fakt groupoidowy. PSI nie rości nowości dla konstrukcji.

---

## 3. Świadek zadaniowy

Na dwuelementowym weak fibre zdefiniujmy wielkość

\[
R_\alpha(*,*,\alpha)=\alpha\in\mathbb Z_2.
\]

Wtedy

\[
R_\alpha(e)\neq R_\alpha(s).
\]

Niech coarse representation będzie

\[
\rho_{\rm coarse}:\{e,s\}\to\{*\}.
\]

Mamy

\[
\ker_{eq}\rho_{\rm coarse}
\not\subseteq
\ker_{eq}R_\alpha.
\]

Z II.4 wynika więc:

\[
\boxed{
\rho_{\rm coarse}\text{ jest nieadekwatna dla zadania rozróżniającego }\alpha.
}
\]

Jeżeli zadanie jest niewrażliwe na \(\alpha\), ta sama coarse representation może być legalna. Relewancja higher data jest zatem względna wobec kontraktu.

---

## 4. Kolejność operacji

Świadek daje trwały no-go:

\[
\boxed{
\text{truncate first}
\to
\text{form strict fibre}
}
\]

nie musi zachować wyniku

\[
\boxed{
\text{form witness-sensitive fibre}
\to
\text{take only task-legal truncation}.
}
\]

Poprawna dyscyplina PSI brzmi:

\[
\boxed{
\text{zachowaj dane kompatybilności wymagane przez zadanie}
\to
\text{sprawdź }\ker q\subseteq E_{\mathcal T}
\to
\text{dopiero wtedy truncuj}.
}
\]

To jest zastosowanie II.5, nie nowy prymityw.

---

## 5. Stabilizatory

Rozważmy osobno

\[
B1
\qquad\text{i}\qquad
B\mathbb Z_2.
\]

Oba groupoidy mają jedną składową spójności:

\[
\pi_0(B1)=\pi_0(B\mathbb Z_2)=\{*\}.
\]

Jednak

\[
\operatorname{Aut}_{B1}(*)=1,
\qquad
\operatorname{Aut}_{B\mathbb Z_2}(*)\cong\mathbb Z_2.
\]

Dlatego \(\pi_0\) nie jest adekwatną reprezentacją dla zadania wrażliwego na stabilizator/isotropię.

Nie wynika stąd, że stabilizatory są istotne dla każdego zadania.

---

## 6. Gauge i coarse orbit set

Wyrażenie „po quotient gauge” nie może znaczyć automatycznie „weź coarse orbit/component set”.

Dla proponowanej redukcji

\[
q_G:\Omega\to Z
\]

pierwsza zadaniowa bramka pozostaje

\[
\boxed{
\ker_{eq}q_G\subseteq E_{\mathcal T}.
}
\]

Jeżeli coarse quotient usuwa stabilizator, świadectwo kompatybilności albo inną strukturę rozróżnianą przez zadanie, warunek nie przechodzi.

To jest dokładnie C32/C37 po II.5.

---

## 7. Relacja do PSI-FACT

C63 definiuje kanoniczny PSI-FACT minimalnie jako włókno faktoryzacji zgodnych z `ADM_D`, interfejsem, protokołem i danymi, z gauge tylko wtedy, gdy ustanawia go kontrakt.

II.16 **nie** zmienia tej definicji na uniwersalny homotopy fibre.

Poprawna relacja brzmi:

\[
\boxed{
\text{jeżeli stabilizatory / świadectwa / koherencje są task-relevant,}
\quad
\text{FACT representation musi je zachować}.}
\]

Groupoid/homotopy formulation jest wtedy legalnym rozszerzeniem strukturalnym C66. Nie jest obowiązkową formą każdego problemu PSI-FACT.

F59 pozostaje aktywny.

---

## 8. Anti-tautology / role preservation

Zapisanie świadka \(\alpha\) w kandydacie nie jest legalne dlatego, że „do kandydata można zapakować wszystko”. Jest legalne tylko wtedy, gdy \(\alpha\) jest rzeczywistą częścią struktury kompatybilności/realizacji, którą tworzy rozpatrywany diagram i której zadanie jawnie potrzebuje.

Nie wolno pakować do \(\Omega\) gotowej odpowiedzi zadaniowej wyłącznie po to, aby wymusić adekwatność CORE5.

C35 pozostaje obowiązującą blokadą `candidate stuffing`.

---

## 9. CORE5

Minimalny świadek mieści się w istniejących rolach:

- **candidate:** structured/witness-decorated realization;
- **observation:** coarse albo enriched readout zgodnie z kontraktem;
- **compatibility:** relacja/struktura zgodności;
- **task quantities:** witness/stabilizer-sensitive tests, jeśli wymagane;
- **dynamics/transport:** ewolucja struktury, jeśli występuje;
- **contract:** legalność truncacji i gauge.

Nie pozostaje task-relevant distinction wymagające szóstej roli semantycznej.

Zatem dla tego świadka:

\[
\boxed{
\mathrm{HIGHER\!-\!FIBRE}:
\mathrm{CORE5\ SURVIVES}.
}
\]

Nie jest to uniwersalne twierdzenie o kompletności CORE5.

---

## 10. Co II.16 ustanawia

1. konkretny 1-groupoid witness, w którym coarse-first truncation zmienia liczbę klas zgodności;
2. zadaniową nieadekwatność coarse representation, gdy \(\alpha\) jest rozróżniane;
3. niewystarczalność \(\pi_0\) dla zadań stabilizer-sensitive;
4. legalność coarse quotient tylko po teście adekwatności;
5. możliwość potrzeby richer representation bez potrzeby nowego CORE primitive.

---

## 11. Czego II.16 nie ustanawia

Nie ustanawia:

- że każdy PSI-FACT powinien być homotopy fibre;
- że \(\pi_0\) jest zawsze nieadekwatne;
- że wszystkie problemy higher-categorical redukują się do skończonego witness set;
- że wszystkie koherencje dają się skończenie zakodować;
- że stabilizatory są zawsze obserwowalne lub zadaniowo istotne;
- że obecny witness dowodzi uniwersalnej kompletności CORE5;
- teorii \(\infty\)-kategorii w ramach tej jednostki.

---

## 12. Lokalny cross-check

### Groupoid calculation
`PASS`: iso-comma/2-pullback ma dwa obiekty odpowiadające \(e,s\) i brak morfizmów między nimi w tym świadku.

### Coarse comparison
`PASS`: coarse object-set pullback jest jednoelementowy.

### Task bridge
`PASS`: nieadekwatność wynika z II.4 przez jawny \(R_\alpha\).

### Gauge
`PASS`: coarse quotient nie jest automatycznie legalny.

### FACT scope
`PASS`: homotopy/groupoid FACT pozostaje derived extension, nie definicją C63.

### CORE
`PASS`: richer candidate representation nie implikuje CORE6.

### Freeze impact
`PASS`: brak nowej erraty Freeze 01; Errata 01 dotyczy tylko MINI singleton claim.

---

## 13. Werdykt II.16

\[
\boxed{
\mathrm{II.16\ HIGHER\ COMPATIBILITY}
=\mathrm{PASS}.
}

Następny krok: globalny cross-check HIGHER, a następnie cały V2.
