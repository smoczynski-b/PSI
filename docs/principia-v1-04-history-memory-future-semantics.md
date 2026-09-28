# PRINCIPIA SEMANTICA — TOM I
## I.4. Historia, pamięć i przyszła semantyka zadania

**Status:** `NORMALIZED PASS 01 / WHOLE-V1 N2–N4 APPLIED`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md` z zachowanymi C42, C44–C46 oraz C57–C59  
**Zakres:** C25–C27, C42, C57 jako fundamenty/granice; C44–C45 i dowody pozostają w Tomie II; Go i LAZARUS wyłącznie jako świadki regresyjne.

---

## 1. Kontrakt jest ustalony, indeks `c` bywa tłumiony

W całym I.4 ustalamy kontrakt \(c\) oraz chwilę \(t\). Historyczne źródło RED-1 zapisuje dla czytelności

\[
\operatorname{Beh}_{\mathcal T}(H),
\qquad
\equiv_{\mathcal T,t},
\]

z tłumionym indeksem kontraktu. Gdy porównujemy kilka kontraktów, pełna notacja może mieć postać

\[
\operatorname{Beh}_{\mathcal T,c,t}(H),
\qquad
\equiv_{\mathcal T,c,t}.
\]

Ta normalizacja nie zmienia obiektu RED-1. Przypomina jedynie, że przyszła semantyka zadania nie jest kontraktowo absolutna.

---

## 2. Bieżący opis nie zawsze wystarcza dla przyszłości

Dwie sytuacje mogą mieć ten sam bieżący obraz świata, a mimo to różnić się tym, co będzie dalej legalne, wykonalne albo zadaniowo osiągalne. Różnica może zależeć od wcześniejszych stanów, wykonanych interwencji, reguł pamięci lub korelacji niewidocznych w bieżącym przekroju.

Dlatego:

\[
\boxed{
\text{bieżący opis}
\not\Rightarrow
\text{wystarczająca informacja o przyszłej semantyce zadania}.
}
\]

Nie oznacza to, że każde zadanie wymaga pełnej historii.

---

## 3. Przestrzeń historii

Niech

\[
\mathcal H_t
\]

oznacza przestrzeń legalnych historii do chwili \(t\). Przykładowo

\[
H_t=(\varepsilon_0,y_1,\varepsilon_1,y_2,\ldots,\varepsilon_{t-1},y_t),
\]

gdzie \(\varepsilon_i\) jest interwencją/testem/ruchiem, a \(y_{i+1}\) odpowiadającym wynikiem.

Format nie jest uniwersalny. Kontrakt może wymagać czasu, kosztów, decyzji lub innych etykiet. Wymóg brzmi tylko:

\[
\boxed{
\mathcal H_t
\text{ zawiera co najmniej strukturę potrzebną do zdefiniowania legalnych rozszerzeń przyszłości.}
}
\]

Przestrzeń historii może zawierać nadmiar. Nie jest z definicji minimalną implementacją pamięci.

---

## 4. Przyszłe drzewo zadaniowe

### Definicja I.4.1

Dla \(H\in\mathcal H_t\) obiekt

\[
\operatorname{Beh}_{\mathcal T}(H)
\]

jest ukorzenionym drzewem wszystkich legalnych przyszłych rozszerzeń historii \(H\), gdzie:

1. korzeń reprezentuje bieżącą historię;
2. krawędzie niosą jawnie zadeklarowane etykiety przejścia, np. eksperyment/wynik;
3. węzły niosą etykiety zadaniowe wymagane przez kontrakt;
4. relacja rodzic–dziecko odpowiada legalnemu rozszerzeniu historii.

Nie jest to drzewo „wszystkich ontologicznie możliwych przyszłości”, lecz obiekt kontraktowy.

---

## 5. Równoważność przyszłościowa

### Definicja I.4.2

\[
\boxed{
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H')
}
\]

przez izomorfizm zachowujący korzeń, etykiety węzłów, etykiety krawędzi i relację rodzic–dziecko.

Może więc zachodzić

\[
H\neq H'
\]

i jednocześnie

\[
H\equiv_{\mathcal T,t}H',
\]

gdy różnice historyczne nie zmieniają już żadnej legalnej przyszłości zadaniowej.

Dowód, że \(\equiv_{\mathcal T,t}\) jest relacją równoważności oraz odpowiednią kongruencją dla zamrożonego RED-1, należy do Tomu II.

---

## 6. Pamięć jako reprezentacja historii

Aby uniknąć kolizji z oznaczeniem

\[
R\in\mathscr R_{\mathcal T,c},
\]

przeciwdziedzinę pamięci oznaczamy w V1 przez \(Z_t\):

\[
\boxed{
\rho_t:\mathcal H_t\to Z_t.
}
\]

Reprezentacja pamięci może kodować bieżący stan, część historii, zbiór zdarzeń, stan automatu lub inny jawnie otypowany skrót.

### Zasada I.4.3 — dokładna adekwatność pamięci

\[
\boxed{
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

Jeśli

\[
\rho_t(H)=\rho_t(H')
\]

ale

\[
H\not\equiv_{\mathcal T,t}H',
\]

to pamięć jest zbyt gruba dla zadania. Jedna taka para jest pełnym kontrprzykładem do dokładnej wystarczalności reprezentacji.

---

## 7. Świadek LAZARUS — lokalne typowanie

W świadku LAZARUS niech:

- \(X_t\) — bieżąca fizyczna przestrzeń kandydatów/stanu świata;
- \(F_t(H)\subseteq X_t\) — bieżące włókno świata indukowane przez historię \(H\);
- \(\Gamma_t\in\mathcal G_t^{op}\) — aktywny stan lub konfiguracja operacyjna;
- \(J_t\subseteq X_t\times\mathcal G_t^{op}\) — wspólny zbiór zadaniowo dopuszczalnych par.

Może zachodzić

\[
F_t(H)=F_t(H')
\]

przy

\[
H\not\equiv_{\mathcal T,t}H'.
\]

Wtedy sama mapa

\[
\rho_F(H)=F_t(H)
\]

nie jest wystarczającą pamięcią zadaniową.

Poprawne stwierdzenie brzmi:

\[
\boxed{
\text{to samo bieżące włókno świata}
\not\Rightarrow
\text{ta sama przyszła semantyka zadania}.
}
\]

LAZARUS nie ustanawia prymitywu „sprawczości”; wykazuje niewystarczalność wybranej reprezentacji.

---

## 8. Marginesy nie zachowują automatycznie korelacji

Znajomość osobnych marginesów świata i stanu operacyjnego nie wyznacza w ogólności wspólnego zbioru

\[
J_t\subseteq X_t\times\mathcal G_t^{op}.
\]

Dwie historie mogą mieć te same marginesy, lecz różne legalne pary \((x_t,\Gamma_t)\), a przez to różną przyszłą semantykę zadania.

\[
\boxed{
\text{marginesy}
\not\Rightarrow
\text{wspólny stan zadaniowo istotny}.
}
\]

Nie wynika z tego, że należy przechowywać pełny iloczyn kartezjański; każda kompresja wymaga po prostu testu adekwatności.

---

## 9. Historia nie jest pamięcią minimalną

W Tomie II zdefiniujemy

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}
\]

i wykażemy, że jest najgrubszym dokładnym ilorazem historii w porządku ilorazów.

Już tutaj zamrażamy granice:

\[
\boxed{
\text{najgrubszy dokładny iloraz}
\not\Rightarrow
\text{minimum bitów}
}
\]

oraz

\[
\boxed{
\text{najgrubszy dokładny iloraz}
\not\Rightarrow
\text{minimum kosztu implementacji}.
}
\]

Minimalizacja pamięci fizycznej, wymiaru, liczby stanów i kosztu obliczeń jest osobnym problemem.

---

## 10. Rekurencyjność matematyczna nie oznacza pamięci skończonej

Przy odpowiedniej kongruencji można definiować aktualizację klas historii

\[
[H_t]_{\mathcal T,t}
\xrightarrow{(\varepsilon_t,y_{t+1})}
[H_{t+1}]_{\mathcal T,t+1}.
\]

Z dobrze określonej aktualizacji nie wynika jednak skończona liczba klas, efektywna obliczalność ani tania aktualizacja online.

\[
\boxed{
\text{rekurencyjność matematyczna}
\not\Rightarrow
\text{skończona lub efektywna pamięć}.
}
\]

---

## 11. Świadek Go — lokalne typowanie

W regresie Go używamy:

- \(B_t\) — pozycji planszy po \(t\) półruchach;
- \(\sigma_t\) — gracza na ruchu;
- \(V_t=\{B_0,\ldots,B_t\}\) — zbioru odwiedzonych plansz w świadku PSK;
- \(U_t=\{(B_i,\sigma_i):i\le t\}\) — zbioru odwiedzonych sytuacji w świadku SSK.

Zamrożona sekwencja

\[
(B_t,\sigma_t)
\to
(B_t,\sigma_t,B_{t-1})
\to
(B_t,\sigma_t,V_t)
\to
(B_t,\sigma_t,U_t)
\]

nie jest uniwersalną drabiną pamięci. Każdy etap odpowiada innemu kontraktowi reguł. Wspólna lekcja brzmi:

\[
\boxed{
\text{reprezentacja wystarczająca dla jednego zadania}
\not\Rightarrow
\text{wystarczalność dla innego}.
}
\]

Pełne laboratorium Go pozostaje w Tomie III.

---

## 12. Trzy warstwy pozostają rozdzielone

### Obserwacja bieżąca

\[
F_t(H)
\]

— jakie stany świata pozostają zgodne z przebiegiem obserwacji?

### Pamięć

\[
\rho_t(H)
\]

— jakie rozróżnienia historii zachowuje wybrana reprezentacja?

### Przyszła semantyka zadania

\[
[H]_{\mathcal T,t}
\]

— które różnice historyczne mogą jeszcze zmienić legalną przyszłość zadaniową?

Te obiekty mogą się pokrywać w szczególnym kontrakcie, lecz nie są definicyjnie tym samym.

---

## 13. Granice rozdziału

I.4 nie dowodzi jeszcze:

1. równoważności \(\equiv_{\mathcal T,t}\);
2. minimalności ilorazu w porządku ilorazów;
3. dobrze określonej aktualizacji klas;
4. istnienia skończonej pamięci;
5. algorytmicznej minimalizacji pamięci.

Punkty 1–3 należą do Tomu II. Punkty 4–5 wymagają dodatkowych założeń.

---

## 14. Wniosek

Centralny warunek ma postać

\[
\boxed{
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

Nie oznacza „pamiętaj wszystko”. Oznacza:

\[
\boxed{
\text{nie zapominaj niczego, co może jeszcze zmienić przyszły wynik zadania}.
}
\]

---

## Status redakcyjny I.4

Normalizacja N2–N4 dodała jawne tłumienie indeksu kontraktu, usunęła kolizję \(R_t\) przez \(Z_t\) oraz lokalnie otypowała świadki Go/LAZARUS. Semantyka C42/C57–C59 i Freeze 01 nie uległa zmianie.

\[
\boxed{
\mathrm{I.4}=\mathrm{NORMALIZED\ PASS\ 01}.
}
\]
