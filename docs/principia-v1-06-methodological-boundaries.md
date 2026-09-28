# PRINCIPIA SEMANTICA — TOM I
## I.6. Granice metodologiczne i dyscyplina prymitywów

**Status:** `PROSE PASS 01 / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md` z zachowanymi C12, C34–C36, C60–C66  
**Zakres:** zasady graniczne i dyscyplina wnioskowania; bez nowych twierdzeń matematycznych i bez rozszerzania CORE5.

---

## 1. Po co potrzebny jest rozdział graniczny

Pierwsze pięć jednostek Tomu I ustaliło kolejno:

1. role semantyczne kontraktu;
2. obserwację, zgodność i włókno kandydatów;
3. równoważność zadaniową oraz legalną utratę informacji;
4. historię i pamięć względem przyszłej semantyki zadania;
5. rozdzielenie dokładności, stabilności i licencji statystycznej.

Sama obecność tych konstrukcji nie chroni jednak przed błędnym przejściem pomiędzy poziomami. Można poprawnie zdefiniować włókno, a potem bezprawnie wybrać reprezentanta; poprawnie skonstruować quotient, a potem uznać go za pełny stan świata; poprawnie znaleźć symetrię, a potem bez sprawdzenia uczynić z niej gauge; poprawnie dowieść jednoznaczności, a potem uznać ją za stabilność.

Dlatego fundamenty PSI wymagają nie tylko obiektów, lecz także jawnych **granic prawa do wniosku**.

W tym rozdziale nie wprowadzamy szóstego elementu rdzenia. Porządkujemy jedynie zakazy przejść, których wcześniejsze rozdziały nie licencjonują.

---

## 2. Reprezentacja nie jest reprezentowanym obiektem

Pierwsza granica ma postać

\[
\boxed{
\text{REPREZENTACJA}\neq\text{REPREZENTOWANY OBIEKT}.
}
\]

Jeżeli

\[
\rho:\Omega_c\to Z
\]

jest reprezentacją, to element \(\rho(x)\) nie staje się przez sam fakt istnienia mapy \(\rho\) obiektem \(x\). Jest jego obrazem w określonej strukturze reprezentacyjnej.

To samo dotyczy obserwacji:

\[
\Psi_c(x)
\]

nie jest automatycznie pełnym stanem \(x\), a włókno

\[
F_c(Y)
\]

nie jest jednym „ukrytym prawdziwym stanem”.

Również klasa zadaniowa

\[
[x]_{\mathcal T,c}
\]

nie jest ontologicznym utożsamieniem wszystkich jej reprezentantów. Oznacza tylko, że kontrakt i zadanie nie wymagają ich dalszego rozróżniania.

Dlatego żadna redukcja opisu nie może być bez osobnego argumentu interpretowana jako redukcja samej rzeczywistości badanego układu.

---

## 3. Nieobserwowane nie znaczy zero

Drugi rygiel jest elementarny, lecz krytyczny:

\[
\boxed{
\text{NIEOBSERWOWANE}\neq 0.
}
\]

Jeżeli kanał obserwacji nie wyznacza pewnej wielkości, nie oznacza to, że wielkość ta ma wartość zerową. Oznacza tylko, że bieżący kontrakt obserwacyjny nie dostarczył podstawy do jej ustalenia.

Podobnie:

\[
\boxed{
\text{UNRESOLVED}\neq\text{NEGATED}.
}
\]

Brak prawa do potwierdzenia warunku nie jest prawem do potwierdzenia jego negacji.

Ta sama zasada pojawiła się w I.5 przy bramce stabilności: brak certyfikacji sektora Freneta nie dowodzi zerowej krzywizny. Ma jednak szerszy zakres i obowiązuje wszędzie tam, gdzie informacja jest częściowa.

---

## 4. Dwa porządki, których nie wolno mieszać

PSI utrzymuje kanoniczną kolejność problemu identyfikacji:

\[
\boxed{
\text{ADEKWATNOŚĆ KATALOGU}
\to
\text{WŁÓKNO}
\to
\text{IDENTYFIKOWALNOŚĆ LOKALNA}
\to
\text{IDENTYFIKOWALNOŚĆ GLOBALNA}
\to
\text{PROJEKTOWANIE PROTOKOŁU}.
}
\]

Jest to porządek pytań o katalog, dane i rozstrzygalność.

Osobno, gdy konkretny wniosek został już sformułowany, można badać jego jakość:

\[
\boxed{
\mathrm{ID}_{exact}
\not\Rightarrow
\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}
\not\Rightarrow
\mathrm{CONF}_{1-\alpha}.
}
\]

Ta druga relacja nie jest dalszym odcinkiem pierwszej sekwencji. Jest **ortogonalną kontrolą jakości wniosku**. Nie każdy problem wymaga warstwy statystycznej, a projektowanie protokołu może następować zarówno w problemie dokładnym, jak i probabilistycznym.

Dlatego nie wolno skracać ani mieszać obu porządków przez utożsamienia:

\[
\boxed{
\text{adekwatność}\neq\text{identyfikowalność}\neq\text{stabilność}\neq\text{ufność}.
}
\]

Każdy poziom wymaga własnego kontraktu i własnego testu wtedy, gdy jest częścią deklarowanego problemu.

---

## 5. PSI-ID nie jest PSI-CAT

Identyfikacja w ustalonym katalogu i identyfikacja konieczności zmiany katalogu są różnymi problemami.

Dlatego obowiązuje

\[
\boxed{
\mathrm{PSI\!-\!ID}\neq\mathrm{PSI\!-\!CAT}.
}
\]

`PSI-ID` pyta, jakie rozróżnienia można uzasadnić **wewnątrz ustalonej klasy kandydatów**.

`PSI-CAT` pyta, czy dane i protokół uzasadniają zmianę tej klasy oraz jakiego typu zmiana jest dopuszczalna.

Puste włókno może być sygnałem niespójności bieżącego pakietu kontraktowego, lecz samo nie identyfikuje jeszcze nowego katalogu. Z kolei dobra identyfikowalność wewnątrz złego katalogu nie naprawia jego nieadekwatności.

Warunki dziedzinowe \(ADM_D\) mogą eliminować niedopuszczalne propozycje katalogu, lecz nie stają się przez to nową obserwacją empiryczną.

---

## 6. Równoważność realizacyjna nie jest recodem behawioralnym

Należy także oddzielić dwa typy relacji pomiędzy realizacjami.

**Równoważność realizacyjna** usuwa różnice, które kontrakt uznaje za czysto prezentacyjne lub izomorficzne.

**Recode behawioralny** może zachowywać określone zachowanie przy przejściu do innej, nawet nieizomorficznej realizacji.

Dlatego:

\[
\boxed{
\text{realization equivalence}
\neq
\text{behavioural recoding}.
}
\]

W szczególności recode jednokierunkowy nie musi być równoważnością.

Rozróżnienie to jest ważne dla PSI-FACT: quotient przez gauge jest legalny wtedy, gdy kontrakt ustanawia odpowiednią równoważność; nie wolno zastępować jej dowolnym mapowaniem zachowującym część zachowania.

---

## 7. Symetria nie jest automatycznie gauge

Z istnienia działania grupy lub grupoidu na przestrzeni realizacji nie wynika automatycznie prawo do quotientu w konkretnym problemie obserwacyjnym.

Obowiązuje:

\[
\boxed{
\text{symetria geometryczna}
\not\Rightarrow
\text{legalny gauge ustalonego włókna obserwacyjnego}.
}
\]

Aby redukcja była zadaniowo adekwatna, musi przejść test

\[
\ker_{\rm eq}q\subseteq E_{\mathcal T,c}.
\]

Aby była w pełni legalna kontraktowo, może ponadto wymagać zgodności obserwacji, poprawnych dziedzin, legalnego działania, zachowania interfejsu i innych warunków kontraktu.

Dlatego nawet poprawna symetria fizyczna lub geometryczna może być nielegalnym quotientem dla danych zapisanych w ustalonym układzie odniesienia.

---

## 8. Zakaz candidate stuffing

Najważniejszym rygorem antytautologicznym jest zakaz sztucznego ratowania teorii przez wpisywanie odpowiedzi do przestrzeni kandydatów.

Nie wolno argumentować:

> „CORE5 jest wystarczający, ponieważ każdą brakującą informację można dopisać do \(\Omega\)”.

Taki ruch byłby pusty, gdyby dodawana informacja w rzeczywistości należała do innej roli: obserwacji, historii protokołu, zadania, dynamiki, zgodności albo zewnętrznego warunku kontraktu.

Dlatego:

\[
\boxed{
\text{candidate stuffing}
\neq
\text{dowód wystarczalności CORE5}.
}
\]

Legalne rozszerzenie \(\Omega_c\) musi zachować semantyczną rolę kandydata: ma opisywać to, co w badanym problemie może być realizacją lub stanem, a nie ukryty klucz odpowiedzi.

Ten rygiel nie zakazuje bogatych przestrzeni stanu. Zakazuje wyłącznie zmiany roli semantycznej bez jawnej zmiany kontraktu.

---

## 9. Nowy prymityw wymaga nowej roli semantycznej

CORE5 pozostaje pięcioelementowym schematem:

\[
\mathfrak P_c
=
(\Omega_c,\Psi_c,\mathcal K_c,
\mathscr O_{\mathcal T,c},\delta_c).
\]

Nie oznacza to twierdzenia, że żaden szósty rodzaj obiektu nie może nigdy okazać się potrzebny.

Dyscyplina projektu jest słabsza i bardziej falsyfikowalna:

\[
\boxed{
\text{nowy prymityw dopuszczamy dopiero wtedy,
gdy kontrprzykład wymusza nową rolę semantyczną}.
}
\]

Nowa notacja, bogatsza reprezentacja, dodatkowy parametr, inny model danych albo bardziej złożony quotient nie są jeszcze nowym prymitywem, jeśli można je poprawnie umieścić w już istniejących rolach.

Nowy prymityw byłby uzasadniony dopiero wtedy, gdy istnieje zadaniowo istotne rozróżnienie, którego nie można zachować przez legalne rozszerzenie lub przetypowanie żadnej z istniejących ról bez zmiany ich znaczenia.

---

## 10. Aktualny R4-stop jest polityką projektu, nie twierdzeniem o świecie

Dotychczasowe próby naciskowe obejmowały między innymi:

\[
\mathrm{CAT/FACT},
\quad
\mathrm{CLOSED\!-\!FRAME},
\quad
\mathrm{LAZARUS},
\quad
\mathrm{HIGHER\ FIBRE}.
\]

W obecnym zbiorze świadków nie znaleziono przypadku wymuszającego nową rolę semantyczną poza CORE5.

Poprawny wniosek brzmi zatem:

\[
\boxed{
\text{żaden z dotąd przebadanych świadków nie wymusił R4}.
}
\]

Nie wolno wzmacniać go do:

\[
\boxed{
\text{CORE5 jest uniwersalnie zupełny}.
}
\]

Drugie zdanie nie zostało dowiedzione.

Z tego powodu obowiązujący w projekcie zapis

\[
\boxed{
\mathrm{NO\ R4\ WITHOUT\ NEW\ TYPED\ COUNTEREXAMPLE}
}
\]

jest **regułą zarządzania wzrostem teorii**, ustanowioną po obecnych testach. Nie jest aksjomatem matematycznym ani twierdzeniem o wszystkich przyszłych dziedzinach.

Reguła ta nie blokuje:

- nowych twierdzeń;
- bogatszych reprezentacji;
- modułów pochodnych;
- laboratoriów;
- nowych protokołów;
- errat;
- napraw dokumentacyjnych.

Blokuje wyłącznie nieuzasadnione mnożenie podstawowych ról semantycznych.

---

## 11. Brak kontrprzykładu nie jest dowodem kompletności

Ogólna zasada metodologiczna ma postać

\[
\boxed{
\text{brak znanego kontrprzykładu}
\not\Rightarrow
\text{dowód kompletności}.
}
\]

Pressure court może zwiększyć wiarygodność architektury wobec przebadanych klas problemów. Nie zmienia jednak skończonego zbioru testów w twierdzenie uniwersalne.

Każdy późniejszy wynik musi więc zachować informację o zakresie:

- jaka klasa obiektów była badana;
- jaki kontrakt obowiązywał;
- jakie zadanie definiowało istotne rozróżnienia;
- jaki typ kontrprzykładu próbowano skonstruować;
- czego dany test nie obejmował.

Zakres jest częścią twierdzenia, nie przypisem stylistycznym.

---

## 12. Sukces benchmarku nie ustanawia reprezentacji kanonicznej

HCube, Go, FS-STAT, LAZARUS i inne laboratoria pełnią rolę świadków granicznych.

Jeżeli reprezentacja \(\rho_1\) rozdziela parę, której nie rozdziela \(\rho_0\), wynika z tego tylko, że \(\rho_0\) jest niewystarczająca dla badanego zadania i że \(\rho_1\) zachowuje co najmniej rozróżnienie obecne w tym świadku.

Nie wynika automatycznie:

\[
\boxed{
\rho_1
=
\text{reprezentacja minimalna, jedyna lub uniwersalna}.
}
\]

Benchmark jest falsyfikatorem lub separatorem. Nie staje się przez sukces nowym prymitywem ani obowiązkowym językiem całej teorii.

---

## 13. Źródło, status i rola to trzy różne rzeczy

Twierdzenie może być matematycznie poprawne, a jednocześnie mieć nieustaloną proweniencję. Może być klasyczne, ale pełnić nową rolę w PSI. Może być własnym wynikiem projektu, ale tylko benchmarkiem, nie fundamentem.

Dlatego należy oddzielać:

\[
\boxed{
\text{ŹRÓDŁO}
\mid
\text{STATUS EPISTEMICZNY}
\mid
\text{ROLA W ARCHITEKTURZE}.
}
\]

Przykładowo:

- klasyczny lemat może mieć rolę `BRIDGE`;
- własny kontrprzykład może mieć rolę `BENCHMARK`;
- starszy poprawny formalizm może mieć status `GENEALOGY / DERIVED`, jeśli nie należy do bieżącego kanonu;
- brak fizycznego źródła nie czyni twierdzenia automatycznie fałszywym, ale blokuje określony poziom redakcyjnego freeze.

Starsze źródło nie awansuje do bieżącego kanonu tylko dlatego, że jest bardziej rozbudowane.

---

## 14. Filtr wejścia do kanonu

Dla nowego silnego twierdzenia obowiązuje minimalny ciąg kontroli:

\[
\boxed{
\text{OBIEKT}
\to
\text{TYP/DZIEDZINA}
\to
\text{WARUNKI}
\to
\text{WIELKOŚĆ ZADANIOWA}
\to
\text{TEST}.
}
\]

Brak któregoś elementu oznacza brak prawa do wpisania twierdzenia do kanonu w silnej postaci. Nie oznacza automatycznie jego fałszu.

Dla twierdzeń o większym ciężarze dochodzi kontrola:

\[
\boxed{
\text{ŹRÓDŁO}
\to
\text{TYP}
\to
\text{DZIEDZINA}
\to
\text{WARUNKI}
\to
\text{MATEMATYKA}
\to
\text{WARUNKI ZEWNĘTRZNE}
\to
\text{LITERATURA}
\to
\text{KONTRPRZYKŁAD}
\to
\text{TWIERDZENIE}.
}
\]

Jest to rygor redakcyjno-badawczy, nie nowy obiekt matematyczny PSI.

---

## 15. Granica Tomu I

Po I.1–I.6 fundamenty PSI można streścić jako sześć kolejnych ograniczeń prawa do wniosku:

\[
\boxed{
\begin{array}{rcl}
\mathrm{I.1}&:&\text{nie mieszaj ról kontraktu},\\
\mathrm{I.2}&:&\text{nie zastępuj włókna reprezentantem},\\
\mathrm{I.3}&:&\text{nie usuwaj rozróżnień potrzebnych zadaniu},\\
\mathrm{I.4}&:&\text{nie utożsamiaj bieżącego opisu z pamięcią przyszłości},\\
\mathrm{I.5}&:&\text{nie rozszerzaj dokładności na stabilność i ufność},\\
\mathrm{I.6}&:&\text{nie rozszerzaj zakresu twierdzenia poza jego kontrakt i świadki}.
\end{array}
}
\]

Tom I nie dowodzi jeszcze wszystkich twierdzeń stojących za tymi zasadami. Ustala ich obiekty, typy, zakresy oraz właściwe granice interpretacyjne.

Dowody faktoryzacyjne, twierdzenie o dokładnej rozstrzygalności, dynamika ilorazowa, własności ilorazu historii i mosty do klasycznych konstrukcji należą do Tomu II.

---

## 16. Status po pierwszym przebiegu

Po I.6 nie wolno jeszcze traktować Tomu I jako redakcyjnie zamrożonego.

Następny krok musi być globalnym cross-checkiem I.1–I.6 jako jednego systemu. Należy sprawdzić w szczególności:

1. zgodność symboli i typów;
2. brak sprzecznych definicji kontraktu, włókna i ilorazu;
3. poprawną kolejność logiczną;
4. brak powtórnego awansu materiału laboratoryjnego do fundamentu;
5. zgodność wszystkich odwołań do V2;
6. brak cichego przesunięcia statusu `POLICY` w `THEOREM`;
7. zgodność z Freeze 01 i Claim Registry v12.

Dopiero po takim przebiegu można nadać Tomowi I status pierwszego spójnego przebiegu fundamentów.
