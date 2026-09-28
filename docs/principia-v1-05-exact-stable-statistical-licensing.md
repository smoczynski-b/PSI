# PRINCIPIA SEMANTICA — TOM I
## I.5. Dokładna identyfikowalność, stabilność i licencja statystyczna

**Status:** `PROSE PASS 01 / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md` z zachowanymi C48–C56  
**Zakres:** C51–C52 jako zamrożone zasady fundamentalne; FS-STAT/R03 wyłącznie jako świadek graniczny. Szczegółowe rachunki kondycji, torsji, estymacji i testów pozostają w V2/V3.

---

## 1. Jednoznaczność dokładna nie kończy problemu wnioskowania

W I.2 i I.3 rozdzieliliśmy kandydatów zgodnych z danymi od klas zadaniowych. Na poziomie dokładnym można więc pytać, czy dane wyznaczają jedną klasę w ilorazie zadaniowym.

To pytanie jest logiczne i zbiorowe. Dotyczy tego, czy przy **ustalonym kontrakcie i ustalonych danych** pozostaje więcej niż jedna możliwość istotna dla zadania.

Nie odpowiada jednak automatycznie na dwa dalsze pytania:

1. co stanie się z wynikiem, gdy dane zostaną nieznacznie zaburzone;
2. czy istnieje probabilistyczna podstawa dla deklarowanego przedziału ufności, testu albo ryzyka.

Są to trzy różne poziomy wnioskowania.

Dlatego obowiązuje rygiel:

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

Nie jest to nierówność pomiędzy trzema wielkościami. Jest to zapis **braku automatycznych implikacji** pomiędzy trzema odmiennymi klasami twierdzeń.

---

## 2. Poziom pierwszy — identyfikowalność dokładna

Przez identyfikowalność dokładną rozumiemy tu rozstrzygalność przy ustalonych danych, zanim wprowadzimy osobny problem perturbacji albo model losowy.

Na poziomie zadaniowym naturalnym obiektem jest obraz włókna zgodności w ilorazie zadaniowym:

\[
q_{\mathcal T,c}(F_c(Y)).
\]

Pytanie dokładne brzmi:

\[
\boxed{
\text{czy wszystkie kandydaty zgodne z }Y
\text{ należą do tej samej klasy zadaniowej?}
}
\]

Twierdzenie o dokładnej rozstrzygalności zostanie podane i udowodnione w Tomie II. Dla obecnego rozdziału istotne jest tylko to, że wynik dokładny jest twierdzeniem o **strukturze włókna i ilorazu**, a nie jeszcze o odporności na zmianę danych.

Możliwe jest zatem, że dla danego \(Y\) wynik jest jednoznaczny, lecz mała perturbacja danych prowadzi do dużej zmiany wyniku albo do utraty jednoznaczności.

Wtedy dokładna identyfikowalność nie wystarcza do twierdzenia stabilności.

---

## 3. Poziom drugi — stabilność wymaga jawnej struktury perturbacji

Słowo „stabilny” nie ma dostatecznie określonego sensu matematycznego bez wskazania:

- co jest perturbowane;
- w jakiej przestrzeni;
- względem jakiej topologii, metryki, normy albo innej struktury kontroli;
- jaka wielkość wyjściowa jest śledzona;
- jaka tolerancja jest wymagana przez zadanie.

Dlatego twierdzenie stabilności ma inny typ niż twierdzenie dokładnej identyfikowalności. Schematycznie wymaga ono relacji postaci

\[
\boxed{
\text{mała legalna perturbacja wejścia}
\to
\text{kontrolowana zmiana wyniku zadaniowego}.
}
\]

Sama równość

\[
|q_{\mathcal T,c}(F_c(Y))|=1
\]

nie zawiera jeszcze topologii perturbacji ani oszacowania ciągłości. Nie daje więc automatycznie granicy błędu dla danych bliskich \(Y\).

Stabilność jest dodatkowym wymaganiem kontraktu i musi być dowiedziona w geometrii właściwej dla danego problemu.

---

## 4. FS-STAT jako świadek granicy, nie fundament statystyki PSI

Regres FS-STAT dostarcza konkretnego przykładu, w którym wielkość poprawnie zdefiniowana w reżimie dokładnym staje się źle uwarunkowana przy zbliżaniu się do osobliwej warstwy geometrycznej.

Szczegóły rachunku — rodzina krzywych, dokładne wzory krzywizny i torsji, oszacowania błędów różnic skończonych oraz regularizacja pochodnych — należą do warstwy technicznej V2/V3.

W Tomie I zachowujemy tylko konsekwencję metodologiczną:

\[
\boxed{
\text{dokładna definicja współrzędnej}
\not\Rightarrow
\text{jednolita stabilność jej odzyskiwania}.
}
\]

oraz drugi rygiel:

\[
\boxed{
\text{brak certyfikacji warunku}
\neq
\text{certyfikacja jego negacji}.
}
\]

Jeżeli protokół nie potrafi wykazać warunków potrzebnych do stabilnego użycia danej reprezentacji, legalnym wynikiem może być

\[
\boxed{\mathrm{UNRESOLVED}.}
\]

Nie należy zastępować tej odpowiedzi arbitralną wartością tylko dlatego, że procedura obliczeniowa wymaga liczby.

---

## 5. Próbkowanie, szum i regularizacja zmieniają problem

Twierdzenie dokładne sformułowane dla pełnych danych nie może zostać automatycznie przeniesione na dane skończone, zaszumione albo pośrednio rekonstruowane.

Wprowadzenie próbkowania i błędu wymaga jawnego określenia między innymi:

- schematu próbkowania;
- modelu błędu albo deterministycznej granicy zakłóceń;
- sposobu rekonstrukcji wielkości pośrednich;
- regularizacji, jeśli jest używana;
- kryterium stabilności względem zadania.

Są to dodatkowe elementy protokołu. Nie wolno przedstawiać ich jako konsekwencji samego twierdzenia dokładnego.

Regularizacja może być potrzebna do uzyskania stabilnej procedury, lecz stanowi dodatkową regułę. Nie należy jej traktować jak informacji, którą zawierały same dane.

---

## 6. Poziom trzeci — ufność wymaga kontraktu probabilistycznego

Stabilność deterministyczna nie jest tym samym co pokrycie probabilistyczne.

Nawet jeśli dla pewnego protokołu potrafimy podać deterministyczną granicę błędu, nie wynika z niej automatycznie stwierdzenie o prawdopodobieństwie \(1-\alpha\).

Aby sformułować częstotliwościowe stwierdzenie ufności, potrzebna jest jawna struktura probabilistyczna: model losowości, założenia dotyczące próbkowania lub zakłóceń oraz procedura, dla której definiuje się pokrycie.

Dlatego:

\[
\boxed{
\text{ograniczony deterministycznie szum}
\not\Rightarrow
\text{przedział ufności}
}
\]

oraz ogólniej:

\[
\boxed{
\mathrm{ID}_{\rm stable}
\not\Rightarrow
\mathrm{CONF}_{1-\alpha}.
}
\]

Częstotliwościowa licencja statystyczna istnieje dopiero względem jawnie ustalonego modelu i jego założeń.

---

## 7. Model probabilistyczny jest częścią kontraktu

Jeżeli kontrakt wprowadza rozkład błędów, zależność czasową, schemat losowania albo inny mechanizm probabilistyczny, nie jest to dekoracja zapisu. Zmienia typ problemu wnioskowania.

Zmiana modelu może zmienić poprawność przedziałów, testów, oszacowań ryzyka i asymptotyk. Dlatego twierdzenie probabilistyczne powinno zawsze wskazywać model, względem którego jest prawdziwe.

PSI nie wprowadza tu własnej interpretacji prawdopodobieństwa. Wymaga tylko, aby przejście od danych do twierdzenia probabilistycznego miało jawną licencję, zamiast korzystać z języka dokładnej identyfikowalności jako substytutu.

---

## 8. Estymator nie jest identyfikowalnością

Można posiadać algorytm

\[
\widehat\theta=A(Y),
\]

który dla każdego wejścia zwraca liczbę, model albo reprezentanta.

Sam fakt istnienia takiej procedury nie dowodzi:

- dokładnej identyfikowalności;
- stabilności;
- poprawnego pokrycia probabilistycznego;
- że wybrany reprezentant jest jedynym kandydatem dopuszczonym przez dane.

Dlatego należy rozdzielić:

\[
\boxed{
\text{istnienie procedury obliczeniowej}
}
\]

od

\[
\boxed{
\text{prawa do określonego wniosku o badanym obiekcie}.
}
\]

Algorytm może rozstrzygać nawet wtedy, gdy matematyczna podstawa do tak silnego wniosku nie istnieje. Wtedy wynik algorytmu jest wynikiem procedury, a nie automatycznie identyfikacją właściwości świata.

---

## 9. Lokalna licencja nie daje automatycznie globalnej

Także po wprowadzeniu warstwy statystycznej trzeba pilnować zakresu twierdzenia.

Wynik punktowy, lokalny lub ważny na certyfikowanym podzbiorze dziedziny nie może być automatycznie rozszerzony na całą trajektorię, przedział, przestrzeń parametrów albo wszystkie klasy reprezentacji.

Pełne przejście od lokalnego testu do globalnego twierdzenia wymaga osobnego argumentu i pozostaje poza fundamentem tego rozdziału.

Zatem:

\[
\boxed{
\text{lokalna licencja}
\not\Rightarrow
\text{globalna licencja}.
}
\]

Szczegółowy problem globalnego testu płaskości z FS-STAT pozostaje poza bieżącym freeze V1.

---

## 10. Niepewność na ilorazach pozostaje osobnym problemem

Jeżeli właściwym obiektem zadaniowym jest klasa równoważności, zwykłe przedziały dla współrzędnych wybranego reprezentanta nie muszą automatycznie dostarczać poprawnej procedury pokrycia na przestrzeni klas.

Obecny freeze V1/V2 nie zawiera ogólnego twierdzenia o statystycznym pokryciu na takich ilorazach.

Dlatego temat ten pozostaje poza fundamentem I.5 jako **otwarta warstwa przyszłej PSI-STAT**, a nie jako brakujące twierdzenie CORE5.

---

## 11. Trzy niezależne bramki

Cały rozdział można skondensować do trzech pytań.

### Bramka E — dokładność

\[
\boxed{
\text{czy przy ustalonych danych wynik zadaniowy jest jednoznaczny?}
}
\]

### Bramka S — stabilność

\[
\boxed{
\text{czy legalne perturbacje danych powodują kontrolowaną zmianę wyniku?}
}
\]

### Bramka P — licencja probabilistyczna

\[
\boxed{
\text{czy jawny model probabilistyczny uzasadnia deklarowane pokrycie, test lub ryzyko?}
}
\]

Przejście przez wcześniejszą bramkę nie zastępuje następnej:

\[
\boxed{
E\not\Rightarrow S,
\qquad
S\not\Rightarrow P.
}
\]

Legalny raport może zatem mieć postać

\[
\boxed{
\mathrm{EXACT:PASS},
\quad
\mathrm{STABLE:UNRESOLVED},
\quad
\mathrm{CONF:NOT\ LICENSED}.
}
\]

Nie jest to sprzeczność. Jest to jawne rozdzielenie poziomów wiedzy.

---

## 12. Czego ten rozdział nie twierdzi

I.5 nie ustanawia:

- jednej uniwersalnej definicji stabilności dla wszystkich dziedzin;
- jednego modelu szumu dla PSI;
- nowej teorii prawdopodobieństwa;
- uniwersalnego estymatora;
- automatycznej procedury doboru regularizacji;
- ogólnego testu globalnej płaskości;
- ogólnej teorii przedziałów ufności na przestrzeniach ilorazowych;
- prawa do przenoszenia wyników dokładnych na dane próbkowane bez nowego kontraktu.

Szczegóły FS-STAT pozostają laboratorium i regresem stabilności/statystycznej licencji. Nie stają się fundamentem osobnej ontologii statystycznej PSI.

---

## 13. Przejście do I.6

Po I.1–I.5 aparat ma już trzy rodzaje granic:

1. **semantyczne** — role CORE5 nie mogą być mieszane;
2. **informacyjne** — reprezentacja nie może sklejać rozróżnień potrzebnych zadaniu;
3. **inferencyjne** — dokładność, stabilność i ufność wymagają osobnych licencji.

Pozostaje zebrać zasady, które zapobiegają ich cichemu obchodzeniu podczas rozbudowy teorii.

Następna jednostka będzie więc poświęcona metodologicznym granicom PSI: statusom twierdzeń, źródłom, zasadzie pierwszeństwa późniejszego kanonu, zakazowi automatycznej promocji starszych aparatów, rygorowi kontrprzykładu oraz zamrożeniu rozrostu rdzenia.
