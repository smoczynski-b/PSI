# PRINCIPIA SEMANTICA — TOM I
## I.1. Kontrakt i role semantyczne

**Status:** `PROSE PASS 01 / CROSS-CHECK PASS`  
**Źródło nadrzędne:** `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`  
**Zakres:** C01, C60–C61 jako granice i odsyłacze; bez dowodów z Tomu II.

---

## 1. Prawo do wniosku jest względne wobec kontraktu

PSI nie rozpoczyna od pytania, czym „naprawdę” jest badany układ. Rozpoczyna od pytania bardziej ograniczonego i matematycznie kontrolowalnego:

\[
\boxed{
\text{co wolno wywnioskować z danych przy zadanym sposobie obserwacji i zadaniu?}
}
\]

Odpowiedź na to pytanie nie jest absolutna. Zależy od tego, jakie realizacje dopuszczamy, co mierzymy, jakie dane uznajemy za zgodne z obserwacją, jakie rozróżnienia są istotne dla zadania oraz jakie ewolucje lub aktualizacje są legalne. Całość tych założeń nazywamy **kontraktem**.

Kontrakt oznaczamy przez

\[
c.
\]

Nie jest on pojedynczym parametrem ani dodatkową współrzędną stanu. Jest metapoziomową specyfikacją, względem której typowane są obiekty używane przez PSI. Zmiana kontraktu może zmienić przestrzeń kandydatów, kanał obserwacji, sens zgodności danych, rodzinę wielkości zadaniowych lub dynamikę. Dlatego wynik uzyskany dla kontraktu \(c\) nie może być bez dowodu przeniesiony do kontraktu \(c'\).

W szczególności niedozwolona jest cicha zamiana:

\[
\boxed{
(c,\text{wynik dla }c)
\longrightarrow
(c',\text{ten sam wynik})
}
\]

bez jawnej mapy transportu albo osobnego twierdzenia.

---

## 2. Minimalny rdzeń: pięć ról, nie pięć dowolnych pól

Dla kontraktu \(c\) i zadania \(\mathcal T\) minimalny rdzeń PSI ma postać

\[
\boxed{
\mathfrak P_c=
(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
}
\]

Jest to pięcioelementowy układ **ról semantycznych**. Znaczenie zapisu nie polega na liczbie pięciu składników jako takiej, lecz na rozdzieleniu pięciu funkcji, których nie wolno mieszać.

### Definicja I.1.1 — przestrzeń kandydatów

\[
\Omega_c
\]

jest zbiorem realizacji lub kandydatów dopuszczonych przez kontrakt \(c\).

Jeżeli kontrakt ustanawia równoważność realizacyjną, \(\Omega_c\) może być już przestrzenią po odpowiednim ilorazie. Nie oznacza to jednak, że każdy zauważony układ symetrii wolno automatycznie potraktować jako gauge. Zadaniowa adekwatność takiej redukcji jest osobnym problemem i zostanie rozstrzygnięta dopiero po zdefiniowaniu równoważności zadaniowej; pełna legalność kontraktowa może wymagać dodatkowych warunków.

Przestrzeń kandydatów nie jest zbiorem wszystkiego, co potrafimy nazwać. Jej elementy muszą spełniać warunki dopuszczalności kontraktu. Niedopuszczalne jest rozszerzanie \(\Omega_c\) ad hoc wyłącznie po to, aby uratować żądany wniosek.

### Definicja I.1.2 — kanał obserwacji

\[
\Psi_c:\Omega_c\longrightarrow\mathcal B_c
\]

jest mapą obserwacji.

Jej wartość nie musi być „surowym pomiarem” w potocznym sensie. Może być całym rekordem obserwacyjnym, sygnałem, trajektorią, klasą zachowania albo innym typowanym obiektem. Istotne jest, że przeciwdziedzina \(\mathcal B_c\) oraz znaczenie mapy \(\Psi_c\) są jawne.

Kanał obserwacji jest częścią kontraktu. Ta sama realizacja może być nierozróżnialna pod jednym obserwatorem i rozróżnialna pod innym.

### Definicja I.1.3 — relacja zgodności

\[
\mathcal K_c\subseteq\mathcal B_c\times\mathcal Y_c
\]

jest typowaną relacją zgodności między wynikiem obserwatora a danymi \(Y\in\mathcal Y_c\).

Relacja ta oddziela **obserwację modelową** od **danych**. W przypadku dokładnym może redukować się do równości, lecz PSI nie zakłada tego z góry. Może uwzględniać tolerancję, błąd pomiaru, przedział dopuszczalności albo inne jawnie określone warunki zgodności.

Z tego powodu nie należy utożsamiać mapy \(\Psi_c\) z całą semantyką obserwacyjną. O tym, czy kandydat jest zgodny z danymi, decyduje para

\[
(\Psi_c,\mathcal K_c),
\]

a nie sama wartość \(\Psi_c(x)\).

### Definicja I.1.4 — lokalne wielkości zadaniowe

\[
\mathscr O_{\mathcal T,c}
\]

jest rodziną wielkości istotnych dla zadania \(\mathcal T\), każdą z jawnie określoną dziedziną i przeciwdziedziną.

Rodzina ta odpowiada na pytanie: **które rozróżnienia między kandydatami mają znaczenie dla zadania?**

Nie jest to lista wszystkich własności realizacji. Dwa różne elementy \(\Omega_c\) mogą być dla zadania równoważne, jeśli żadna wielkość potrzebna do wykonania zadania nie wymaga ich rozróżnienia. Formalna relacja takiej równoważności zostanie skonstruowana w I.3.

### Definicja I.1.5 — dynamika lub aktualizacja

\[
\delta_c
\]

opisuje dopuszczalną ewolucję albo aktualizację w kontrakcie.

W przypadku deterministycznym może mieć typ

\[
\delta_c:\Omega_c\to\Omega_c.
\]

Nie wolno jednak używać tego zapisu jako uniwersalnej notacji dla dynamiki stochastycznej. Jeżeli kontrakt jest probabilistyczny, należy jawnie wprowadzić odpowiednio otypowane jądro przejścia lub inny właściwy obiekt.

Dynamika należy do rdzenia dlatego, że rozróżnienie nieistotne w jednej chwili może stać się istotne po dopuszczalnej ewolucji. Zadaniowe znaczenie stanu nie jest więc w ogólności określone wyłącznie przez chwilową listę obserwabli.

---

## 3. Rozdzielenie ról

Pięć składników rdzenia nie może służyć jako pięć pojemników, do których można dowolnie wkładać brakujące informacje. Każdy ma inną funkcję logiczną:

\[
\begin{array}{c|c}
\text{obiekt} & \text{pytanie} \\
\hline
\Omega_c & \text{co jest dopuszczalnym kandydatem?} \\
\Psi_c & \text{co z kandydata obserwujemy?} \\
\mathcal K_c & \text{co znaczy zgodność obserwacji z danymi?} \\
\mathscr O_{\mathcal T,c} & \text{które różnice są potrzebne zadaniu?} \\
\delta_c & \text{jakie ewolucje/aktualizacje są dopuszczalne?}
\end{array}
\]

Ta separacja jest warunkiem kontroli wnioskowania.

Jeżeli brakującą informację potrzebną do zadania „naprawimy” przez dopisanie jej bez uzasadnienia do \(\Omega_c\), zmieniamy katalog kandydatów. Jeżeli wprowadzimy ją do \(\Psi_c\), zmieniamy protokół obserwacji. Jeżeli wpiszemy ją do \(\mathcal K_c\), zmieniamy kryterium zgodności. Jeżeli dodamy nową wielkość do \(\mathscr O_{\mathcal T,c}\), zmieniamy zadanie. Jeżeli zaszyjemy ją w \(\delta_c\), zmieniamy prawo aktualizacji.

W każdym z tych przypadków należy powiedzieć, **który składnik kontraktu zmieniono**.

To prowadzi do zasady antydryfowej:

\[
\boxed{
\text{nie naprawiaj braku informacji przez zmianę roli semantycznej bez zmiany kontraktu}.
}
\]

---

## 4. Zakaz „candidate stuffing”

Szczególnie groźnym błędem jest sztuczne poszerzanie przestrzeni kandydatów o informacje należące do innej roli tylko po to, aby otrzymać żądaną wystarczalność albo jednoznaczność.

Przykładowy schemat błędu ma postać

\[
\Omega_c
\longmapsto
\widetilde\Omega_c=\Omega_c\times Z,
\]

po czym dodatkową współrzędną \(Z\) traktuje się tak, jakby od początku była częścią badanego obiektu. Jeżeli \(Z\) w rzeczywistości pochodzi z historii eksperymentu, protokołu, dodatkowego pomiaru albo reguły decyzyjnej, taka operacja nie dowodzi wystarczalności pierwotnej reprezentacji. Konstruuje nowy kontrakt.

Dopuszczalne rozszerzenie przestrzeni kandydatów musi więc mieć własne uzasadnienie semantyczne i źródłowe. Sam fakt, że rozszerzony model „działa”, nie pokazuje, że pierwotne dane identyfikowały dodaną informację.

---

## 5. Symetria, równoważność realizacyjna i gauge

Kontrakt może uznać pewne różnice między realizacjami za czysto reprezentacyjne. Wtedy dopuszcza relację równoważności albo działanie grupy/grupoidu, względem którego rozważamy klasy realizacji.

Należy jednak rozdzielić dwa twierdzenia:

\[
\boxed{
\text{„mamy symetrię”}
}
\]

oraz

\[
\boxed{
\text{„wolno nam przejść do ilorazu w tym problemie”}.
}
\]

Pierwsze jest deklaracją struktury. Drugie wymaga sprawdzenia, czy redukcja zachowuje informacje wymagane przez zadanie oraz pozostałe warunki kontraktu.

Już na poziomie obserwacji obowiązuje podstawowa kontrola typu: przekształcenie geometryczne kandydata nie staje się automatycznie gauge danego włókna danych. Dla obserwacji niezmienniczej można mieć

\[
\Psi_c(g\cdot x)=\Psi_c(x),
\]

lecz w innym kontrakcie działanie \(g\) może zmieniać obserwację. Wtedy dwa geometrycznie równoważne obiekty nie należą automatycznie do tego samego problemu zgodności z ustalonym \(Y\).

Dokładne kryterium zachowania informacji zadaniowej przez redukcję pojawi się dopiero po konstrukcji \(E_{\mathcal T,c}\) w I.3. Nie będzie ono samo w sobie wyczerpywało pełnej legalności kontraktowej: kontrakt może ponadto wymagać poprawnych typów i dziedzin, dopuszczalności działania gauge, zgodności obserwacji lub innych jawnych warunków protokołu.

W tym miejscu zamrażamy jedynie zasadę:

\[
\boxed{
\text{zadeklarowana symetria}
\neq
\text{licencja na utratę informacji}.
}
\]

---

## 6. Reprezentacja nie jest reprezentowanym obiektem

PSI utrzymuje rozdzielenie

\[
\boxed{
\text{REPREZENTACJA}\neq\text{ŚWIAT}.
}
\]

Nie jest to teza metafizyczna. Jest to reguła typowania.

Element \(x\in\Omega_c\), jego obraz \(\Psi_c(x)\), rekord danych \(Y\), klasa równoważności realizacyjnej i późniejsza klasa zadaniowa są różnymi obiektami matematycznymi. Mogą być ze sobą powiązane mapami, ale nie wolno ich utożsamiać bez twierdzenia.

Analogicznie:

\[
\boxed{
\text{NIEOBSERWOWANE}\neq 0.
}
\]

Brak składnika w obserwacji nie uprawnia do nadania mu wartości zerowej. Oznacza tylko, że przy bieżącym kontrakcie jego wartość nie została wyznaczona przez dany kanał obserwacji.

Ta zasada będzie miała konkretną postać zbiorową w następnym rozdziale, gdy obserwację zastąpimy pełnym włóknem kandydatów zgodnych z danymi.

---

## 7. Kontrakt jako granica obowiązywania twierdzenia

Każde twierdzenie PSI powinno wskazywać co najmniej:

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

Jeżeli któryś z tych elementów zostaje zmieniony, nie mamy automatycznie „tego samego twierdzenia w nowej sytuacji”. Mamy nowe zadanie transportu wyniku.

W szczególności zmiana:

- przestrzeni kandydatów;
- protokołu obserwacji;
- tolerancji zgodności;
- dopuszczalnego gauge;
- rodziny wielkości zadaniowych;
- dynamiki;
- horyzontu lub reguły aktualizacji

może zmienić prawo do wniosku nawet wtedy, gdy fizyczny układ, którego dotyczy eksperyment, pozostaje ten sam.

Kontrakt nie twierdzi więc, czym świat jest. Określa dziedzinę, w której dane twierdzenie o identyfikowalności, wystarczalności lub decyzji ma sens i może być sprawdzone.

---

## 8. Granice jednostki I.1

W tej jednostce **nie** definiujemy jeszcze:

- włókna zgodności \(F_c(Y)\);
- domknięcia zadaniowego \(\mathscr R_{\mathcal T,c}\);
- równoważności zadaniowej \(E_{\mathcal T,c}\);
- ilorazu zadaniowego \(M_{\mathcal T,c}\);
- kryterium \(\ker_{eq}\rho\subseteq E_{\mathcal T}\);
- dokładnej identyfikowalności;
- stabilności ani prawdopodobieństwa ufności.

Nie jest to brak. Jest to kolejność logiczna.

Najpierw ustalamy typy i role. Dopiero potem wolno pytać, które kandydatury pozostają zgodne z obserwacją i które różnice między nimi są potrzebne zadaniu.

---

## 9. Przejście do I.2

Mając kontrakt

\[
\mathfrak P_c=
(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c),
\]

możemy zadać pierwsze właściwe pytanie identyfikacyjne.

Dla otrzymanych danych \(Y\) nie pytamy jeszcze:

\[
\text{„jaki jest ukryty obiekt?”}
\]

lecz:

\[
\boxed{
\text{„które elementy }\Omega_c\text{ pozostają zgodne z }Y\text{?”}
}
\]

Odpowiedzią będzie włókno zgodności. Jego konstrukcja jest przedmiotem I.2.

---

## Status redakcyjny I.1

Cross-check względem `V1/V2 FREEZE 01`, C01 i C60–C61 wykrył i usunął jedno pierwotne przeszacowanie: kryterium zadaniowej adekwatności redukcji nie zostało utożsamione z pełną legalnością kontraktową.

\[
\boxed{
\mathrm{I.1}=\mathrm{PROSE\ PASS\ 01 / CROSS\!-
CHECK\ PASS}.
}
\]

Tekst nie wprowadza nowego prymitywu ani nowego twierdzenia względem `V1/V2 FREEZE 01`. Rozwija zamrożony C01, zachowuje rozdzielenie kontraktu i ról oraz pozostawia kryteria ilorazowe do I.3/Tomu II.