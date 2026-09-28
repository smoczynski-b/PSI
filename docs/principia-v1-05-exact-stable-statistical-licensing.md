# PRINCIPIA SEMANTICA — TOM I
## I.5. Dokładna identyfikowalność, stabilność i licencja statystyczna

**Status:** `NORMALIZED PASS 01 / WHOLE-V1 N5 APPLIED`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md` z zachowanymi C48–C56  
**Zakres:** C51–C52 jako zamrożone zasady fundamentalne; FS-STAT/R03 wyłącznie jako świadek graniczny. Szczegóły techniczne pozostają w V2/V3.

---

## 1. Trzy odrębne klasy twierdzeń

Jednoznaczność przy ustalonych danych nie odpowiada jeszcze na pytanie o odporność na perturbacje ani o probabilistyczne pokrycie. Dlatego:

\[
\boxed{
\mathrm{ID}_{\rm exact}
\not\Rightarrow
\mathrm{ID}_{\rm stable},
\qquad
\mathrm{ID}_{\rm stable}
\not\Rightarrow
\mathrm{CONF}_{1-\alpha}.
}
\]

Są to relacje braku automatycznej implikacji między różnymi typami twierdzeń, nie „nierówności” między trzema wielkościami.

---

## 2. Dokładna identyfikowalność

Na poziomie zadaniowym pytamy o obraz włókna

\[
q_{\mathcal T,c}(F_c(Y)).
\]

Pytanie dokładne brzmi:

\[
\boxed{
\text{czy wszystkie kandydaty zgodne z }Y
\text{ należą do jednej klasy zadaniowej?}
}
\]

Twierdzenie o dokładnej rozstrzygalności i jego dowód należą do Tomu II. W tym rozdziale istotne jest tylko, że jest to twierdzenie o strukturze włókna i ilorazu przy ustalonych danych, a nie twierdzenie o perturbacjach.

---

## 3. Stabilność wymaga jawnej geometrii perturbacji

Twierdzenie stabilności musi wskazywać co najmniej:

- co jest perturbowane;
- w jakiej przestrzeni;
- względem jakiej topologii, normy lub metryki;
- jaki wynik zadaniowy jest kontrolowany;
- jaka tolerancja obowiązuje.

Schematycznie:

\[
\boxed{
\text{mała legalna perturbacja wejścia}
\to
\text{kontrolowana zmiana wyniku zadaniowego}.
}
\]

Z samego

\[
|q_{\mathcal T,c}(F_c(Y))|=1
\]

nie wynika żadna granica błędu dla danych bliskich \(Y\), dopóki kontrakt nie określa sensu „bliskości” i operatora rozwiązania, którego stabilność badamy.

---

## 4. FS-STAT jako świadek graniczny

FS-STAT pokazuje, że wielkość poprawnie określona w reżimie dokładnym może być źle uwarunkowana przy zbliżaniu się do warstwy osobliwej. Szczegóły rachunku pozostają w V2/V3.

W V1 zachowujemy wyłącznie wnioski:

\[
\boxed{
\text{dokładna definicja wielkości}
\not\Rightarrow
\text{jednolita stabilność jej odzyskiwania}
}
\]

oraz

\[
\boxed{
\text{brak certyfikacji warunku}
\neq
\text{certyfikacja jego negacji}.
}
\]

Dlatego legalnym wynikiem może być

\[
\boxed{\mathrm{UNRESOLVED}.}
\]

---

## 5. Próbkowanie, szum i regularizacja zmieniają kontrakt

Przejście od pełnych danych do próbek i zakłóceń wymaga jawnego określenia:

- schematu próbkowania;
- modelu błędu albo deterministycznej granicy zakłóceń;
- sposobu rekonstrukcji wielkości pośrednich;
- regularizacji;
- kryterium stabilności.

Regularizacja może stabilizować procedurę, ale jest dodatkową regułą wyboru. Nie należy przedstawiać jej jako informacji zawartej w samych danych.

---

## 6. Ufność wymaga kontraktu probabilistycznego

Deterministyczna granica błędu nie jest częstotliwościowym przedziałem ufności. Aby sformułować twierdzenie typu

\[
\Pr(\theta\in C_{1-\alpha}(Y))\ge 1-\alpha,
\]

potrzebny jest jawny model losowości, schemat próbkowania i procedura, dla której definiuje się pokrycie.

Dlatego:

\[
\boxed{
\text{ograniczony deterministycznie szum}
\not\Rightarrow
\text{przedział ufności}.
}
\]

PSI nie tworzy własnej interpretacji prawdopodobieństwa; wymaga jedynie jawnej licencji probabilistycznej.

---

## 7. Estymator nie jest identyfikowalnością

Można posiadać procedurę

\[
\widehat\theta=A(Y)
\]

zwracającą wynik dla każdego wejścia. Sam fakt istnienia algorytmu nie dowodzi identyfikowalności, stabilności, poprawnego pokrycia ani tego, że wybrany reprezentant jest jedynym kandydatem zgodnym z danymi.

\[
\boxed{
\text{istnienie procedury obliczeniowej}
\neq
\text{prawo do określonego wniosku}.
}
\]

---

## 8. Lokalna licencja nie daje globalnej

Wynik punktowy lub lokalny nie przechodzi automatycznie na cały przedział, trajektorię, przestrzeń parametrów lub wszystkie klasy reprezentacji.

\[
\boxed{
\text{lokalna licencja}
\not\Rightarrow
\text{globalna licencja}.
}
\]

Globalny test wymaga osobnego argumentu.

---

## 9. Niepewność na ilorazie jest osobnym problemem

Jeżeli właściwym obiektem zadaniowym jest klasa równoważności, przedział dla współrzędnych wybranego reprezentanta nie musi dawać poprawnego pokrycia na przestrzeni klas. Obecny freeze nie zawiera ogólnego twierdzenia o przedziałach ufności na takich ilorazach.

To problem przyszłej PSI-STAT, nie brakujący prymityw CORE5.

---

## 10. Trzy bramki bez kolizji z \(E_{\mathcal T,c}\)

Aby nie kolidować z centralnym oznaczeniem równoważności zadaniowej \(E_{\mathcal T,c}\), bramki jakości wniosku oznaczamy:

### Bramka dokładności

\[
\boxed{\mathsf G_{EX}}
\]

— czy przy ustalonych danych wynik zadaniowy jest jednoznaczny?

### Bramka stabilności

\[
\boxed{\mathsf G_{ST}}
\]

— czy legalne perturbacje powodują kontrolowaną zmianę wyniku?

### Bramka probabilistyczna

\[
\boxed{\mathsf G_{PR}}
\]

— czy jawny model probabilistyczny uzasadnia deklarowane pokrycie, test lub ryzyko?

Przejście przez wcześniejszą bramkę nie zastępuje następnej:

\[
\boxed{
\mathsf G_{EX}\not\Rightarrow\mathsf G_{ST},
\qquad
\mathsf G_{ST}\not\Rightarrow\mathsf G_{PR}.
}
\]

Legalny raport może mieć postać

\[
\boxed{
\mathsf G_{EX}:\mathrm{PASS},
\quad
\mathsf G_{ST}:\mathrm{UNRESOLVED},
\quad
\mathsf G_{PR}:\mathrm{NOT\ LICENSED}.
}
\]

---

## 11. Czego I.5 nie twierdzi

I.5 nie ustanawia:

- jednej uniwersalnej definicji stabilności;
- jednego modelu szumu;
- nowej teorii prawdopodobieństwa;
- uniwersalnego estymatora;
- automatycznego doboru regularizacji;
- ogólnego testu globalnego;
- ogólnej teorii ufności na ilorazach;
- prawa do przenoszenia wyników dokładnych na dane próbkowane bez nowego kontraktu.

---

## Status redakcyjny I.5

Normalizacja N5 usunęła kolizję bramki `E` z \(E_{\mathcal T,c}\). Semantyka C51–C52 i R03 nie uległa zmianie.

\[
\boxed{
\mathrm{I.5}=\mathrm{NORMALIZED\ PASS\ 01}.
}
\]
