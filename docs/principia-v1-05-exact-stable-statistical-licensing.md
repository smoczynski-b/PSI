# PRINCIPIA SEMANTICA — TOM I
## I.5. Dokładna identyfikowalność, stabilność i licencja statystyczna

**Status:** `FIRST PROSE PASS / FROM V1-V2 FREEZE 01`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md` z zachowanymi C48–C56  
**Zakres:** C51–C52 jako zasady fundamentalne; C48–C50, C53–C55 jako granice i odsyłacze do warstwy technicznej FS-STAT. Bez ogólnej teorii statystycznej PSI.

---

## 1. Jednoznaczność dokładna nie kończy problemu wnioskowania

W I.2 i I.3 rozdzieliliśmy kandydatów zgodnych z danymi od klas zadaniowych. Na poziomie dokładnym można więc pytać, czy dane wyznaczają jedną klasę w ilorazie zadaniowym.

To pytanie jest logiczne i zbiorowe. Dotyczy tego, czy przy **dokładnie ustalonym kontrakcie i dokładnie podanych danych** pozostaje więcej niż jedna możliwość istotna dla zadania.

Nie odpowiada jednak na dwa dalsze pytania:

1. co stanie się z wynikiem, gdy dane zostaną nieznacznie zaburzone;
2. z jakim prawdopodobieństwem procedura pokrywa prawdziwą wielkość lub klasę, gdy obserwacja jest losowa.

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

Nie jest to zapis nierówności między trzema wielkościami. Jest to zapis **braku automatycznych implikacji** pomiędzy trzema odmiennymi rodzajami twierdzeń.

---

## 2. Poziom pierwszy — identyfikowalność dokładna

Przez identyfikowalność dokładną rozumiemy w tym miejscu rozstrzygalność przy ustalonych danych i bez perturbacji wymagającej osobnego modelu błędu.

Na poziomie zadaniowym jej naturalnym obiektem jest obraz włókna zgodności w ilorazie zadaniowym:

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

Twierdzenie o dokładnej rozstrzygalności zostanie podane i udowodnione w Tomie II. Dla obecnego rozdziału istotne jest tylko to, że taki wynik jest twierdzeniem o **strukturze włókna i ilorazu**, nie o odporności na zaburzenia danych.

Możliwe jest zatem, że dla każdego ustalonego \(Y\) odpowiedź jest jednoznaczna, lecz mapa

\[
Y\longmapsto q_{\mathcal T,c}(F_c(Y))
\]

jest bardzo czuła na małe zmiany \(Y\).

Wtedy identyfikowalność dokładna zachodzi, ale problem jest źle uwarunkowany albo niestabilny.

---

## 3. Poziom drugi — stabilność wymaga geometrii perturbacji

Słowo „stabilny” nie ma samodzielnego znaczenia matematycznego bez wskazania:

- co jest perturbowane;
- w jakiej przestrzeni;
- względem jakiej topologii, metryki lub normy;
- jaka wielkość wyjściowa jest kontrolowana;
- jaka tolerancja jest wymagana przez zadanie.

Dlatego twierdzenie stabilności musi mieć co najmniej postać schematu

\[
\boxed{
\text{perturbacja wejścia}
\to
\text{kontrola zmiany wyniku zadaniowego}.
}
\]

Jeżeli dane należą do przestrzeni metrycznej \((\mathcal Y,d_Y)\), a wynik do przestrzeni z odległością zadaniową \(d_{\mathcal T}\), stabilność może być wyrażona warunkowo przez oszacowanie typu

\[
d_{\mathcal T}(S(Y),S(Y'))
\le
\omega(d_Y(Y,Y')),
\]

gdzie \(S\) jest odpowiednio otypowanym operatorem rozwiązania lub reprezentacją wyniku, a \(\omega(r)\to0\) dla \(r\to0\).

Ten schemat nie jest nowym twierdzeniem PSI. Pokazuje jedynie, że **stabilność wymaga dodatkowej struktury**, której nie ma w samym stwierdzeniu dokładnej identyfikowalności.

W szczególności z

\[
|q_{\mathcal T,c}(F_c(Y))|=1
\]

nie wynika żadna granica błędu dla danych \(Y'\) bliskich \(Y\), dopóki kontrakt nie określi sensu „bliskości” oraz mapy, której ciągłość lub uwarunkowanie badamy.

---

## 4. Świadek graniczny: torsja przy zanikającej krzywiźnie

FS-STAT dostarcza konkretnego kontrprzykładu przeciwko utożsamieniu dokładnej definicji współrzędnej z jej stabilnym odzyskiwaniem.

Dla rodziny

\[
\gamma_{\varepsilon,\omega}(s)
=
\bigl(s,\varepsilon\cos(\omega s),
\varepsilon\sin(\omega s)\bigr)
\]

mamy dokładnie

\[
\kappa_{\varepsilon,\omega}
=
\frac{\varepsilon\omega^2}
{1+\varepsilon^2\omega^2},
\]

oraz

\[
\tau_{\varepsilon,\omega}
=
\frac{\omega}
{1+\varepsilon^2\omega^2}.
\]

Dla ustalonego \(\omega\), gdy

\[
\varepsilon\to0,
\]

krzywa zbiega do prostej, krzywizna dąży do zera, ale torsja dąży do \(\omega\).

Dla dwóch różnych \(\omega_1\neq\omega_2\) otrzymujemy więc dwie rodziny krzywych zbiegające do tej samej prostej, podczas gdy ich torsje pozostają rozdzielone.

Stąd:

\[
\boxed{
\text{klasyczna torsja Freneta nie ma ciągłego przedłużenia przez warstwę }\kappa=0.
}
\]

Wniosek jest ograniczony. Nie mówi, że „torsja jest zła” ani że Frenet jest zawsze niestabilny. Mówi, że nie można żądać **jednolitej stabilności torsji Freneta na klasie dopuszczającej zbliżanie się do zerowej krzywizny**.

To wystarcza, aby obalić automatyczną implikację

\[
\mathrm{ID}_{\rm exact}
\Rightarrow
\mathrm{ID}_{\rm stable}.
\]

---

## 5. `UNRESOLVED` jest legalnym wynikiem

Jeżeli warunki potrzebne do stabilnego wniosku nie są certyfikowane, system nie powinien zastępować braku prawa do wniosku wygodną wartością liczbową.

Legalny status może brzmieć:

\[
\boxed{\mathrm{UNRESOLVED}.}
\]

W przykładzie Frenet/Bishop, jeżeli nie można certyfikować mianownika torsji dostatecznie daleko od zera przy zadanej tolerancji, właściwy wynik ma postać

\[
\boxed{
\mathrm{FRENET\ UNRESOLVED}
\to
\mathrm{BISHOP}.
}
\]

Nie oznacza to

\[
\kappa=0.
\]

Oznacza jedynie, że bieżący protokół nie daje prawa do stabilnego użycia współrzędnych Freneta z wymaganą dokładnością.

To rozdzielenie jest ogólne:

\[
\boxed{
\text{brak certyfikacji warunku}
\neq
\text{certyfikacja jego negacji}.
}
\]

---

## 6. Próbkowanie i szum tworzą nowy kontrakt

Twierdzenie dokładne, sformułowane dla pełnych danych \(Y\), nie może zostać automatycznie przeniesione na skończone, zaszumione próbki.

Jeżeli obserwujemy

\[
Y_j=\gamma(t_j)+\varepsilon_j,
\]

to zmienia się kontrakt obserwacyjny. Trzeba określić co najmniej:

- schemat próbkowania;
- model błędu albo deterministyczną granicę szumu;
- sposób estymacji pochodnych lub innych wielkości pośrednich;
- regularizację;
- kryterium stabilności wymagane przez zadanie.

FS-STAT pokazuje jawnie, że surowe różnicowanie numeryczne wzmacnia szum wraz z rzędem pochodnej. Dla jednego z badanych kontraktów otrzymano oszacowania

\[
\|\widehat d_1-\gamma'\|
\le
\frac{M_3}{6}h^2+\frac{\delta}{h},
\]

\[
\|\widehat d_2-\gamma''\|
\le
\frac{M_4}{12}h^2+\frac{4\delta}{h^2},
\]

\[
\|\widehat d_3-\gamma'''\|
\le
\frac{M_5}{4}h^2+\frac{3\delta}{h^3}.
\]

W Tomie I oszacowania te mają status **świadka kondycji**, nie uniwersalnego twierdzenia o wszystkich estimatorach i wszystkich modelach szumu.

Ich funkcja jest metodologiczna: pokazują, że „więcej próbek” i „dokładna formuła różniczkowa” nie wystarczają jeszcze do stabilnej rekonstrukcji.

---

## 7. Poziom trzeci — ufność wymaga modelu probabilistycznego

Stabilność deterministyczna nie jest tym samym co pokrycie probabilistyczne.

Załóżmy, że potrafimy wykazać deterministycznie

\[
\|\widehat\theta-	heta\|
\le
\eta.
\]

Taki wynik może być bardzo użyteczny, ale sam w sobie nie definiuje zdarzenia losowego o prawdopodobieństwie \(1-\alpha\).

Aby sformułować częstotliwościowe stwierdzenie ufności, potrzebny jest model probabilistyczny, na przykład jawnie określony rozkład błędów, schemat losowania albo inna struktura pozwalająca zdefiniować prawdopodobieństwo procedury pokrycia.

Dlatego:

\[
\boxed{
\text{ograniczony deterministycznie szum}
\not\Rightarrow
\text{przedział ufności}.
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

Stwierdzenie ufności jest legalne dopiero po wskazaniu jawnego kontraktu probabilistycznego i założeń, na których opiera się pokrycie.

---

## 8. Model probabilistyczny nie jest dekoracją

Jeżeli wprowadza się model, na przykład

\[
\varepsilon_j
\stackrel{iid}{\sim}
N(0,\sigma^2I),
\]

to nie jest to neutralny sposób zapisania „małego szumu”. Jest to dodatkowa część kontraktu.

Zmiana rozkładu, zależności czasowej, heteroskedastyczności, mechanizmu brakujących danych albo schematu próbkowania może zmienić poprawność przedziałów, testów i asymptotyk.

Dlatego każde stwierdzenie typu

\[
\Pr(\theta\in C_{1-\alpha}(Y))\ge1-\alpha
\]

musi być czytane jako twierdzenie względem jawnie ustalonego modelu/procedury, a nie jako własność samej wielkości \(\theta\).

PSI nie tworzy tu nowej semantyki prawdopodobieństwa. Wymaga jedynie, aby probabilistyczna licencja była jawna i nie była zastępowana językiem dokładnej identyfikowalności.

---

## 9. Estymator nie jest tym samym co identyfikowalność

W praktyce można posiadać algorytm

\[
\widehat\theta=A(Y),
\]

który zawsze zwraca liczbę lub reprezentanta.

Sam fakt, że algorytm zwraca wynik, nie dowodzi:

- że parametr jest dokładnie identyfikowalny;
- że estimator jest stabilny;
- że jest zgodny;
- że ma małe ryzyko;
- że jego przedział ma deklarowane pokrycie;
- że wybrany reprezentant jest jedynym kandydatem dopuszczonym przez dane.

Regularizacja może być niezbędna do obliczeń i stabilności, ale wprowadza dodatkową regułę wyboru. Nie należy przedstawiać jej jako informacji, którą zawierały same dane.

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

---

## 10. Punktowy test nie jest automatycznie twierdzeniem globalnym

FS-STAT daje jeszcze jedną użyteczną granicę.

Nawet jeśli w certyfikowanym sektorze można zbudować punktowy test

\[
H_{0,t}:\tau(t)=0,
\]

nie wynika z tego automatycznie poprawny test twierdzenia

\[
H_0:\tau\equiv0
\quad\text{na całym przedziale}.
\]

Przejście od punktowych decyzji do twierdzenia globalnego wymaga osobnego aparatu: na przykład jednoczesnego pasma, statystyki globalnej albo innej procedury kontrolującej błąd dla całego obiektu funkcyjnego.

W obecnym stanie projektu globalny test płaskości pozostaje otwartym problemem warstwy FS-STAT.

Zasada ogólna brzmi:

\[
\boxed{
\text{lokalna licencja statystyczna}
\not\Rightarrow
\text{globalna licencja statystyczna}.
}
\]

---

## 11. Niepewność na współrzędnych i niepewność na ilorazie

Jeżeli właściwym obiektem zadaniowym jest klasa równoważności, przedziały ufności dla poszczególnych współrzędnych reprezentanta nie muszą automatycznie definiować poprawnego zbioru ufności na ilorazie.

Przykładowo dane Bishopa posiadają prezentacyjną swobodę

\[
SO(2),
\]

a więc naturalnym obiektem może być klasa modulo obrót płaszczyzny normalnej.

Wtedy statystyczne pytanie powinno dotyczyć odpowiednio zdefiniowanego zbioru w przestrzeni klas, a nie przypadkowo wybranych współrzędnych jednego reprezentanta.

Obecny projekt nie posiada zamrożonego ogólnego twierdzenia o pokryciu na takich ilorazach.

Dlatego:

\[
\boxed{
\text{coordinate confidence}
\not\Rightarrow
\text{quotient-level confidence}.
}
\]

Jest to **otwarta granica**, nie nowy wynik statystyczny.

---

## 12. Trzy niezależne bramki

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
\text{czy małe legalne perturbacje danych powodują kontrolowaną zmianę wyniku?}
}
\]

### Bramka P — licencja probabilistyczna

\[
\boxed{
\text{czy jawny model probabilistyczny uzasadnia deklarowane pokrycie/test/ryzyko?}
}
\]

Przejście przez wcześniejszą bramkę nie zastępuje następnej:

\[
\boxed{
E
\not\Rightarrow
S,
\qquad
S
\not\Rightarrow
P.
}
\]

W szczególności legalny raport może mieć postać:

\[
\boxed{
\mathrm{EXACT:PASS},
\quad
\mathrm{STABLE:UNRESOLVED},
\quad
\mathrm{CONF:NOT\ LICENSED}.
}
\]

Nie jest to sprzeczność. Jest to poprawne rozdzielenie poziomów wiedzy.

---

## 13. Czego ten rozdział nie twierdzi

I.5 nie ustanawia:

- jednej uniwersalnej definicji stabilności dla wszystkich dziedzin;
- jednego modelu szumu dla PSI;
- nowego rachunku prawdopodobieństwa;
- uniwersalnego estymatora;
- automatycznej procedury wyboru regularizacji;
- ogólnego testu globalnej płaskości;
- gotowej teorii przedziałów ufności na przestrzeniach ilorazowych;
- twierdzenia, że Bishop usuwa wszystkie problemy estymacyjne;
- prawa do przenoszenia wyników dokładnych na dane próbkowane bez nowego kontraktu.

FS-STAT pozostaje laboratorium/regresem stabilności i statystycznej licencji, nie fundamentem osobnej ontologii statystycznej PSI.

---

## 14. Przejście do I.6

Po I.1–I.5 aparat ma już trzy rodzaje granic:

1. **semantyczne** — role CORE5 nie mogą być mieszane;
2. **informacyjne** — reprezentacja nie może sklejać rozróżnień potrzebnych zadaniu;
3. **inferencyjne** — dokładność, stabilność i ufność wymagają osobnych licencji.

Pozostaje zebrać zasady, które zapobiegają ich cichemu obchodzeniu podczas rozbudowy teorii.

Następna jednostka będzie więc poświęcona metodologicznym granicom PSI: statusom twierdzeń, źródłom, zakazowi automatycznej promocji starszych aparatów, zasadzie `NO R4 WITHOUT COUNTEREXAMPLE` oraz rozdzieleniu reprezentacji od świata.
