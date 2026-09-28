# PRINCIPIA SEMANTICA — TOM I
## I.4. Historia, pamięć i przyszła semantyka zadania

**Status:** `PROSE PASS 01 / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md` z zachowanymi C42, C44–C46 oraz C57–C59  
**Zakres:** C25–C27, C42, C57 jako fundamenty/granice; C44–C45 i dowody pozostają w Tomie II; Go i LAZARUS występują wyłącznie jako świadki regresyjne.

---

## 1. Bieżący stan nie zawsze wystarcza do przewidywania przyszłej legalności

W poprzednich rozdziałach kandydat był traktowany jako element przestrzeni

\[
\Omega_c,
\]

a jego zadaniowa wartość była określana przez to, które rozróżnienia zachowuje iloraz

\[
M_{\mathcal T,c}=\Omega_c/E_{\mathcal T,c}.
\]

W problemach dynamicznych może jednak wystąpić dodatkowe zjawisko: dwie sytuacje mogą mieć ten sam bieżący obraz świata, a mimo to różnić się tym, **co będzie dalej legalne, wykonalne albo zadaniowo osiągalne**.

Przyczyną nie musi być nowa ukryta własność chwili obecnej. Różnica może wynikać z historii eksperymentów, wcześniejszych stanów, wykonanych interwencji, obowiązujących reguł pamięci albo korelacji, które nie są odzyskiwalne z samego bieżącego przekroju stanu.

Dlatego należy rozdzielić:

\[
\boxed{
\text{bieżący opis}
}
\]

od

\[
\boxed{
\text{informacji wystarczającej do zachowania przyszłej semantyki zadania}.
}
\]

Rozdzielenie to nie oznacza, że każde zadanie wymaga pełnej historii. Oznacza tylko, że nie wolno zakładać z góry, iż bieżący stan jest wystarczającą pamięcią.

---

## 2. Przestrzeń historii jako obiekt odniesienia

Niech

\[
\mathcal H_t
\]

oznacza przestrzeń legalnych historii do chwili \(t\).

W najprostszym przypadku historia może być zapisem kolejnych eksperymentów i wyników:

\[
H_t
=
(\varepsilon_0,y_1,\varepsilon_1,y_2,\ldots,
\varepsilon_{t-1},y_t),
\]

gdzie \(\varepsilon_i\) oznacza wykonaną interwencję, test lub ruch, a \(y_{i+1}\) — odpowiadający mu wynik obserwacji.

Nie jest to uniwersalny format historii. Kontrakt może wymagać innego zapisu, jeżeli dla legalnych rozszerzeń potrzebne są dodatkowe etykiety, czasy, decyzje, koszty albo elementy stanu operacyjnego.

Istotna jest zasada:

\[
\boxed{
\mathcal H_t
\text{ musi zawierać co najmniej strukturę potrzebną do zdefiniowania legalnej przyszłości.}
}
\]

Może zawierać więcej informacji niż ostatecznie wymaga zadanie; usuwanie takich nadmiarowych rozróżnień należy do problemu reprezentacji pamięci i ilorazu zadaniowego, nie do samej definicji przestrzeni historii.

Przestrzeń historii jest w tym rozdziale **przestrzenią odniesienia dla semantyki przyszłości**, a nie automatycznie zalecaną implementacją pamięci.

---

## 3. Przyszłość jako drzewo legalnych rozszerzeń

Aby porównać dwie historie, nie wystarczy zapytać, czy mają ten sam bieżący stan. Trzeba zapytać, czy prowadzą do tej samej struktury przyszłych możliwości istotnych dla zadania.

### Definicja I.4.1 — przyszłe drzewo zadaniowe

Dla historii

\[
H\in\mathcal H_t
\]

definiujemy

\[
\operatorname{Beh}_{\mathcal T}(H)
\]

jako ukorzenione drzewo wszystkich legalnych przyszłych rozszerzeń historii \(H\), przy czym:

1. korzeń reprezentuje bieżącą historię;
2. krawędzie są etykietowane literalnymi parami eksperyment/wynik albo innymi jawnie zadeklarowanymi zdarzeniami przejścia;
3. węzły niosą dokładnie te etykiety zadaniowe, które kontrakt nakazuje zachować;
4. relacja rodzic–dziecko odpowiada legalnemu rozszerzeniu historii.

Drzewo to nie jest „wszystkim, co może się wydarzyć” w sensie ontologicznym. Jest obiektem kontraktowym: zawiera tylko przyszłe rozszerzenia legalne w zadanym problemie oraz tylko te etykiety, które są wymagane przez zadanie.

Jeżeli kontrakt zmienia reguły legalności albo zakres etykiet zadaniowych, zmienia się również

\[
\operatorname{Beh}_{\mathcal T}(H).
\]

---

## 4. Równoważność historii względem przyszłej semantyki

Dwie historie należy uznać za równoważne dla zadania wtedy, gdy po ich osiągnięciu pozostaje ta sama struktura legalnych przyszłych rozgałęzień i tych samych przyszłych wyników zadaniowych.

### Definicja I.4.2 — równoważność przyszłościowa historii

\[
\boxed{
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H')
}
\]

przez izomorfizm, który zachowuje:

- korzeń;
- etykiety węzłów;
- etykiety krawędzi;
- relację rodzic–dziecko.

Relacja ta nie twierdzi, że historie są identyczne jako zapisy zdarzeń. Może zachodzić

\[
H\neq H'
\]

oraz jednocześnie

\[
H\equiv_{\mathcal T,t}H',
\]

jeżeli wszystkie różnice między historiami są już nieistotne dla dalszego wykonania zadania.

W Tomie II zostanie wykazane, że \(\equiv_{\mathcal T,t}\) jest relacją równoważności oraz — przy zamrożonym kontrakcie RED-1 — odpowiednią kongruencją dla legalnych rozszerzeń historii.

W Tomie I potrzebujemy przede wszystkim interpretacji:

\[
\boxed{
\text{historie są zadaniowo takie same wtedy,
gdy mają tę samą legalną przyszłość zadaniową}.}
\]

---

## 5. Pamięć jako reprezentacja historii

Niech

\[
\rho_t:\mathcal H_t\to R_t
\]

będzie reprezentacją pamięci.

Może ona przechowywać:

- bieżący stan;
- skończoną liczbę poprzednich stanów;
- zbiór zdarzeń historycznych;
- klasę równoważności historii;
- stan automatu;
- wystarczającą statystykę historyczną;
- inny jawnie otypowany skrót historii.

Każda taka pamięć jest kompresją:

\[
\rho_t(H)=\rho_t(H')
\]

oznacza, że system pamięci nie rozróżnia już historii \(H\) i \(H'\).

Pytanie jest więc dokładnie analogiczne do I.3:

> czy wszystkie sklejenia wykonywane przez pamięć są bezpieczne dla zadania?

### Zasada I.4.3 — dokładna adekwatność pamięci

\[
\boxed{
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

Równoważnie:

\[
\rho_t(H)=\rho_t(H')
\Longrightarrow
H\equiv_{\mathcal T,t}H'.
\]

Jeżeli pamięć utożsamia dwie historie o różnej przyszłej semantyce zadaniowej, jest zbyt gruba.

Jedna para

\[
H,H'
\]

spełniająca

\[
\rho_t(H)=\rho_t(H')
\]

oraz

\[
H\not\equiv_{\mathcal T,t}H'
\]

jest kompletnym kontrprzykładem do dokładnej wystarczalności tej reprezentacji pamięci.

Dowód faktoryzacyjny i własności ilorazu historii należą do Tomu II.

---

## 6. Bieżące włókno świata nie musi być pamięcią zadaniową

W problemach obserwacyjnych można zbudować mapę

\[
\rho_F:\mathcal H_t\to\mathcal P(X_t),
\qquad
\rho_F(H)=F_t(H),
\]

która każdej historii przypisuje bieżące włókno kompatybilnych stanów świata.

Może się jednak zdarzyć, że

\[
F_t(H)=F_t(H')
\]

przy jednoczesnym

\[
H\not\equiv_{\mathcal T,t}H'.
\]

Wtedy

\[
\boxed{
\ker_{\rm eq}\rho_F
\not\subseteq
\equiv_{\mathcal T,t}
}
\]

i samo bieżące włókno nie jest wystarczającym stanem pamięci dla zadania.

To jest precyzyjna wersja wniosku z laboratorium LAZARUS.

Nie należy mówić bez doprecyzowania:

\[
\text{„ta sama informacja, różna sprawczość”.}
\]

Takie zdanie byłoby za mocne. Jeżeli dwie historie są identyczne w **pełnej informacji zadaniowej**, ich zadaniowo istotna przyszłość nie może różnić się z definicji.

Poprawne zdanie brzmi:

\[
\boxed{
\text{to samo bieżące włókno stanu świata}
\not\Rightarrow
\text{ta sama przyszła semantyka zadania}.
}
\]

LAZARUS nie ustanawia nowego prymitywu „sprawczości”. Pokazuje tylko, że wybrana reprezentacja

\[
\rho_F(H)=F_t(H)
\]

może zapomnieć dane potrzebne zadaniu.

---

## 7. Marginesy nie muszą zachowywać korelacji

Historia może być potrzebna nie dlatego, że brakuje pojedynczej współrzędnej, ale dlatego, że kompresja usuwa korelację pomiędzy składnikami stanu.

Załóżmy, że przyszłość zależy wspólnie od:

\[
x_t
\]

— stanu świata, oraz

\[
\Gamma_t
\]

— aktywnej kompozycji operacyjnej.

Można znać dwa zbiory marginalne:

\[
F_t^X
\]

i

\[
F_t^{\Gamma},
\]

a mimo to nie znać właściwego wspólnego zbioru dopuszczalnego

\[
J_t
\subseteq
X_t\times\operatorname{Comp}(\mathcal R_t).
\]

Dwie historie mogą mieć te same marginesy, lecz różne dopuszczalne pary

\[
(x_t,\Gamma_t)
\]

i przez to różne przyszłe drzewa zadaniowe.

Dlatego obowiązuje rygiel:

\[
\boxed{
\text{marginesy}
\neq
\text{wspólny stan zadaniowo istotny}
}
\]

w ogólności.

Nie oznacza to, że zawsze należy przechowywać pełny iloczyn kartezjański albo pełną historię. Oznacza tylko, że kompresja do osobnych marginesów wymaga testu adekwatności, jeżeli zadanie zależy od korelacji.

---

## 8. Historia nie jest automatycznie pamięcią minimalną

Z faktu, że pełna historia jest przestrzenią, na której można zdefiniować przyszłą semantykę zadania, nie wynika, że należy ją przechowywać dosłownie.

Wiele różnych historii może należeć do tej samej klasy

\[
[H]_{\mathcal T,t}
\]

i nie istnieje zadaniowy powód, aby pamięć rozróżniała je dalej.

W Tomie II zdefiniujemy iloraz

\[
M_{\mathcal T,t}
=
\mathcal H_t/\!\equiv_{\mathcal T,t}
\]

i wykażemy jego własność jako najgrubszego dokładnego ilorazu historii względem zadania.

W Tomie I należy jednak od razu postawić granicę interpretacyjną:

\[
\boxed{
\text{najgrubszy dokładny iloraz}
\not\Rightarrow
\text{najmniej bitów}
}
\]

oraz

\[
\boxed{
\text{najgrubszy dokładny iloraz}
\not\Rightarrow
\text{najtańsza implementacja}.
}
\]

Porządek ilorazów jest własnością informacyjną. Minimalizacja pamięci fizycznej, wymiaru, kodu, liczby stanów implementacyjnych albo kosztu obliczeń jest osobnym problemem.

---

## 9. Rekurencyjność matematyczna nie oznacza pamięci skończonej

Jeżeli równoważność historii jest kongruencją względem legalnych rozszerzeń, można aktualizować klasy zadaniowe bez wybierania pełnego reprezentanta historii.

Schematycznie:

\[
[H_t]_{\mathcal T,t}
\xrightarrow{(\varepsilon_t,y_{t+1})}
[H_{t+1}]_{\mathcal T,t+1}.
\]

Dokładny operator aktualizacji zostanie zdefiniowany i uzasadniony w Tomie II.

Już tutaj należy jednak zamrozić granicę:

\[
\boxed{
\text{dobrze określona aktualizacja matematyczna}
\not\Rightarrow
\text{skończona pamięć}.
}
\]

Nie wynika z niej również:

- efektywna obliczalność klas;
- skończona liczba klas;
- tania aktualizacja online;
- istnienie prostego kodu stanu;
- minimalność implementacyjna.

Te własności wymagają odrębnych twierdzeń.

---

## 10. Świadek regresyjny: Go

Go dostarcza prostego laboratorium pokazującego, że adekwatność pamięci zależy od reguły zadania.

W zamrożonym banku regresyjnym pojawia się ciąg reprezentacji:

\[
(B_t,\sigma_t)
\to
(B_t,\sigma_t,B_{t-1})
\to
(B_t,\sigma_t,V_t)
\to
(B_t,\sigma_t,U_t).
\]

Odpowiadają one kolejno kontraktom:

- bez ko;
- proste ko;
- pozycyjne superko;
- sytuacyjne superko.

Ten ciąg nie jest uniwersalną drabiną „coraz lepszych stanów”. Jest serią odpowiedzi na **różne zadania legalności ruchu**.

Reprezentacja wystarczająca pod słabszą regułą może być zbyt gruba po zmianie kontraktu.

Regres R02 można streścić jako:

\[
\boxed{
\text{jedna ustalona kompresja teraźniejszości}
\not\Rightarrow
\text{wystarczalność dla różnych reguł przyszłości}.
}
\]

Pełny przebieg testów Go należy do Tomu III.

---

## 11. Świadek graniczny: LAZARUS

LAZARUS testuje inny typ utraty informacji.

Dwie historie mogą mieć ten sam bieżący zbiór możliwych stanów fizycznych, lecz różnić się aktywną strukturą wykonawczą albo korelacją między stanem świata i stanem operacyjnym. Wtedy legalne działania i osiągalne wyniki mogą się różnić.

Nie jest to dowód, że „historia” albo „sprawczość” powinny zostać dodane jako szósty składnik CORE5.

Naprawa mieści się w istniejącej architekturze:

1. wybieramy bogatszy, poprawnie otypowany kandydat/stanu zadaniowy; albo
2. pozostajemy na przestrzeni historii i stosujemy iloraz względem \(\equiv_{\mathcal T,t}\); albo
3. znajdujemy inną reprezentację \(\rho_t\), która spełnia
   \[
   \ker_{\rm eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
   \]

Dlatego lekcja LAZARUS ma status:

\[
\boxed{
\text{błąd reprezentacji, nie brak nowego prymitywu}.
}
\]

---

## 12. Nie każda historia jest zadaniowo istotna

Należy unikać przeciwnego błędu: skoro historia **czasem** jest potrzebna, nie wynika z tego, że zadanie powinno pamiętać wszystko.

Dopuszczalna reprezentacja może całkowicie zapominać fragment historii, jeżeli wszystkie historie przez nią sklejana są równoważne przyszłościowo:

\[
\rho_t(H)=\rho_t(H')
\Longrightarrow
H\equiv_{\mathcal T,t}H'.
\]

W szczególności:

- zadanie bez pamięci reguł historycznych może zależeć tylko od bieżącego stanu;
- zadanie z pamięcią jednego kroku może wymagać tylko poprzedniej konfiguracji;
- inne zadanie może wymagać zbioru odwiedzonych sytuacji;
- jeszcze inne może mieć wystarczający stan automatu znacznie mniejszy niż dosłowna historia.

PSI nie uprzywilejowuje żadnej z tych form z góry.

Zasada brzmi:

\[
\boxed{
\text{przechowuj nie „historię”, lecz wszystkie rozróżnienia historyczne wymagane przez zadanie}.}
\]

---

## 13. Historia, obserwacja i zadanie są różnymi warstwami

Warto zebrać trzy odrębne pytania:

### Obserwacja bieżąca

\[
F_t(H)
\]

odpowiada na pytanie:

> jakie stany świata pozostają zgodne z dotychczasowym przebiegiem obserwacji?

### Pamięć

\[
\rho_t(H)
\]

odpowiada na pytanie:

> jakie rozróżnienia historii zachowuje wybrana reprezentacja?

### Przyszła semantyka zadania

\[
[H]_{\mathcal T,t}
\]

odpowiada na pytanie:

> które różnice pomiędzy historiami mogą jeszcze zmienić legalną przyszłość zadaniową?

Te trzy obiekty mogą się pokrywać w szczególnym kontrakcie, ale nie wolno utożsamiać ich definicyjnie.

Właściwa zależność jest warunkowa:

\[
\boxed{
\rho_t\text{ jest wystarczająca}
\iff
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

---

## 14. Granice rozdziału

W I.4 nie dowodzimy jeszcze:

1. że \(\equiv_{\mathcal T,t}\) jest relacją równoważności;
2. że iloraz
   \[
   \mathcal H_t/\!\equiv_{\mathcal T,t}
   \]
   jest najgrubszym dokładnym ilorazem historii;
3. że aktualizacja klas jest dobrze określona;
4. że istnieje skończona reprezentacja pamięci;
5. że istnieje algorytm minimalizacji takiej pamięci;
6. że pełna historia jest kiedykolwiek implementacyjnie optymalna.

Punkty 1–3 należą do Tomu II. Punkty 4–6 wymagają dodatkowych założeń i w ogólności nie wynikają z samej architektury PSI.

---

## 15. Wniosek

Rozdział I.3 ustalił, że reprezentacja jest wystarczająca wtedy, gdy nie skleja kandydatów różniących się zadaniowo. Dla problemów historycznych ta sama zasada działa na przestrzeni historii.

Centralny warunek przyjmuje postać

\[
\boxed{
\ker_{\rm eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

Nie oznacza on „pamiętaj wszystko”. Oznacza:

\[
\boxed{
\text{nie zapominaj niczego, co może jeszcze zmienić przyszły wynik zadania}.
}
\]

W następnym rozdziale przejdziemy do innej granicy prawa do wniosku: nawet gdy wynik jest jednoznaczny dokładnie, nie musi być stabilny na małe perturbacje danych, a stabilność nie daje jeszcze prawa do probabilistycznego poziomu ufności.