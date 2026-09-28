# PRINCIPIA SEMANTICA — TOM II
## II.15. Holonomia zamkniętej ramy i globalna okresowość

**Status:** `CLASSICAL GEOMETRY / PSI BRIDGE / PROSE PASS 01 / LOCAL CROSS-CHECK PASS`  
**Źródło nadrzędne PSI:** fizyczny `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-13.md`, zachowane C22–C24  
**Źródło robocze:** `closed-frame-01.md`  
**Aktualizacja względem źródła roboczego:** odwołania do dawnego C19/MINI-01 są historyczne; bieżącym wynikiem przedziałowym jest C19-v3 / `cat-fact-norm-mini-02.md` po Freeze Errata 01.  
**Zakres:** regularne zamknięte krzywe z wystarczającą regularnością do zdefiniowania stycznej i transportu normalnego; dokładna geometria; brak twierdzenia o szumie, estymacji lub zamknięciu statystycznym.

---

## 1. Kontrakt zamkniętej krzywej

Niech

\[
\gamma:S^1\to\mathbb R^3
\]

będzie regularną, zorientowaną krzywą zamkniętą. Ustalamy orientację obiegu oraz punkt bazowy. Wzdłuż krzywej rozpatrujemy zorientowaną płaszczyznę normalną i względnie równoległy transport normalny (Bishop / rotation-minimizing transport).

Do zdefiniowania holonomii nie wymagamy globalnej legalności ramy Freneta. Mocniejsze założenie

\[
\kappa(s)>0
\]

będzie użyte dopiero przy porównaniu z całkowitą torsją.

Zadaniem FRAME jest rozstrzygnięcie, czy lokalnie prawidłowa rama transportowana po pełnym obiegu może być wybrana okresowo.

---

## 2. Holonomia powrotu

Wybierzmy w punkcie bazowym zorientowaną ortonormalną parę normalną

\[
(N_1(0),N_2(0)).
\]

Transport względnie równoległy wokół całej pętli daje po jednym obiegu parę

\[
(N_1(L),N_2(L)).
\]

Istnieje jednoznaczny obrót

\[
\boxed{H_\gamma\in SO(2)}
\]

taki, że

\[
(N_1(L),N_2(L))
=
(N_1(0),N_2(0))H_\gamma.
\]

Nazywamy go holonomią normalną / Bishopowską albo obrotem powrotu.

Obiektem podstawowym jest **mapa powrotu transportu**, nie całkowita torsja.

---

## 3. Twierdzenie II.15.A — okresowa rama a holonomia

Transportowana rama Bishopowska jest okresowa wtedy i tylko wtedy, gdy

\[
\boxed{H_\gamma=I.}
\]

### Dowód

Jeżeli rama jest okresowa, to para normalna po jednym obiegu pokrywa się z parą początkową, więc z definicji mapy powrotu \(H_\gamma=I\).

Odwrotnie, jeżeli \(H_\gamma=I\), transportowana para wraca dokładnie do wartości początkowej. Ponieważ krzywa jest zidentyfikowana na \(S^1\), rama domyka się okresowo. \(\square\)

Twierdzenie jest klasycznym faktem o holonomii transportu, nie nowym twierdzeniem PSI.

---

## 4. Twierdzenie II.15.B — legalny gauge nie usuwa holonomii

Zmiana początkowej zorientowanej bazy normalnej przez stały obrót

\[
R_\alpha\in SO(2)
\]

zmienia macierz powrotu przez sprzężenie:

\[
H_\gamma\mapsto
R_\alpha^{-1}H_\gamma R_\alpha.
\]

Ponieważ \(SO(2)\) jest abelowa,

\[
\boxed{
R_\alpha^{-1}H_\gamma R_\alpha=H_\gamma.
}
\]

Zatem holonomia nie jest artefaktem wyboru początkowej bazy normalnej.

Bardziej ogólnie, okresowa zmiana gauge na \(S^1\) może zmienić lokalny zapis połączenia, ale zachowuje klasę sprzężenia holonomii; tutaj klasa sprzężenia redukuje się do samego elementu \(H_\gamma\).

Natomiast funkcja obrotu zadana na przeciętym przedziale \([0,L]\), która nie spełnia warunku okresowości na końcach, **nie jest legalną globalną zmianą gauge na \(S^1\)**. Może wyzerować lokalny współczynnik na przedziale, lecz endpoint mismatch jest dokładnie globalnym obiektem, który mierzy holonomia.

Dlatego:

\[
\boxed{
\text{lokalne usunięcie współczynnika}
\not\Rightarrow
\text{globalna trywializacja okresowa}.
}
\]

---

## 5. Mocniejszy sektor Freneta

Załóżmy teraz dodatkowo, że

\[
\gamma\in C^3,
\qquad
\kappa(s)>0
\quad\text{na całym }S^1,
\]

tak że rama Freneta jest globalnie legalna i okresowa.

Niech para Bishopowska powstaje przez obrót normalnej/binormalnej Freneta o kąt \(\theta(s)\). W ustalonej konwencji

\[
\theta'(s)=-\tau(s).
\]

Stąd po pełnym obiegu

\[
\theta(L)-\theta(0)
=-\int_0^L\tau(s)\,ds.
\]

Zatem, z dokładnością do konwencji znaku dla obrotu normalnej płaszczyzny,

\[
\boxed{
H_\gamma
=
R_{-\Theta_\gamma},
\qquad
\Theta_\gamma
:=
\int_0^L\tau(s)\,ds
\pmod{2\pi}.
}
\]

W szczególności:

\[
\boxed{
H_\gamma=I
\iff
\Theta_\gamma\in2\pi\mathbb Z.
}
\]

Jest to **współrzędna holonomii w sektorze Freneta**, a nie definicja holonomii w ogólności.

---

## 6. Dlaczego holonomia jest obiektem pierwotniejszym niż całkowita torsja

Jeżeli krzywizna zanika w pewnym punkcie, rama Freneta i torsja mogą przestać być legalne, mimo że sama regularna krzywa oraz względnie równoległy transport normalny pozostają dobrze określone.

Dlatego poprawna hierarchia brzmi:

\[
\boxed{
\text{normal transport}
\to
H_\gamma
\to
\text{periodicity task}.
}
\]

Dopiero na mocniejszej dziedzinie Freneta możemy użyć współrzędnej

\[
H_\gamma
\leftrightarrow
\int\tau\,ds\pmod{2\pi}.
\]

Nie wolno odwracać tej zależności i definiować globalnego obiektu wyłącznie przez torsję.

---

## 7. Relacja do C19-v3 / MINI-02

C19-v3 jest twierdzeniem **przedziałowym**. Dla regularnej krzywej na \([0,T]\) wszystkie legalne skończone segmentacje Freneta/Bishopa mają tę samą klasę normalną po normalizacji:

\[
|\operatorname{im}\operatorname{NF}|=1.
\]

Nie zawiera to warunku, że wybrana rama normalna domyka się po identyfikacji końców.

Dla pętli mamy nową globalną bramkę:

\[
\boxed{H_\gamma=I.}
\]

Zatem:

\[
\boxed{
\text{jedna klasa normalna lokalnie/przedziałowo}
\not\Rightarrow
\text{istnienie okresowego reprezentanta na }S^1.
}
\]

FRAME nie obala MINI-02. Ujawnia dodatkową informację globalną, której kontrakt przedziałowy nie pytał.

---

## 8. PSI — status holonomii

Holonomia nie wymusza nowego prymitywu CORE.

Jeżeli okresowość ramy jest istotna dla zadania, możemy włączyć

\[
R_H(\gamma)=H_\gamma
\]

do rodziny wielkości zadaniowych / jej domknięcia transportowego.

Transport normalny należy do deklarowanej warstwy transportu/dynamiki, a warunek

\[
H_\gamma=I
\]

jest zwykłym warunkiem zadaniowym/zgodnościowym.

Schemat pozostaje:

\[
\boxed{
\text{kandydat}
\xrightarrow{\text{transport wokół pętli}}
H_\gamma
\xrightarrow{\text{zadanie}}
\text{okresowa / nieokresowa klasa ramy}.
}
\]

Nie pojawia się szósta rola semantyczna.

---

## 9. Bundle ≠ connection holonomy

Nie wolno utożsamiać dwóch stwierdzeń:

1. normalna wiązka nad pętlą jest globalnie trywializowalna;
2. zadany transport/połączenie ma trywialną holonomię.

Trywialna wiązka może nieść transport z nietrywialną mapą powrotu.

Dlatego świadek FRAME nie mówi „wiązka normalna nie istnieje”. Mówi:

\[
\boxed{
\text{zadany transport ma nietrywialny return map}.
}
\]

---

## 10. Falsyfikatory / granice

### F-R1 — interval-to-loop inflation

Zakaz:

\[
\text{interval normal form}
\Rightarrow
\text{periodic closed-loop representative}.
\]

Kontrprzykładem jest dowolna zamknięta krzywa z \(H_\gamma\neq I\).

### F-R2 — torsion-first inflation

Zakaz definiowania globalnej holonomii wyłącznie przez

\[
\int\tau ds
\]

bez globalnej legalności Freneta.

### F-R3 — nonperiodic-gauge repair

Zakaz traktowania nieokresowej zmiany bazy na przeciętym przedziale jako legalnego gauge na \(S^1\).

### F-R4 — representation-only dismissal

Holonomia nie jest zadaniowo relewantna dla każdego kontraktu, ale dla zadań o okresowej orientacji/materialnej ramie może być obserwablą zadaniową. Nie wolno z faktu „to dane ramy” wnioskować „to zawsze nieistotne”.

---

## 11. Co II.15 ustanawia

1. holonomia normalna jest mapą powrotu \(H_\gamma\in SO(2)\);
2. okresowa RMF/Bishop rama istnieje dokładnie wtedy, gdy \(H_\gamma=I\);
3. legalne okresowe gauge nie usuwają nietrywialnej holonomii;
4. na globalnie Frenet-legalnej pętli holonomia jest opisana całkowitą torsją modulo \(2\pi\), z konwencją znaku;
5. holonomia jest derived transport/task datum w CORE5;
6. przejście interval → closed loop wymaga osobnej globalnej bramki.

---

## 12. Czego II.15 nie ustanawia

Nie ustanawia:

- stabilnej estymacji holonomii z danych zaszumionych;
- istnienia ramy Freneta przy \(\kappa=0\);
- że total torsion jest definicją holonomii poza sektorem Freneta;
- że każda struktura globalna redukuje się do jednej liczby/elementu \(SO(2)\);
- że holonomia jest istotna dla każdego zadania;
- nowego prymitywu PSI;
- twierdzenia o ogólnych wiązkach/połączeniach poza zakresem normalnego transportu tej krzywej.

---

## 13. Status źródłowy

Geometria Bishopa/RMF, holonomia, związek z całkowitą torsją i kryterium okresowości są klasyczne. `closed-frame-01.md` wiąże je z literaturą Bishopa oraz późniejszymi pracami o okresowych ramach zamkniętych krzywych.

Wkład PSI w tej jednostce jest wyłącznie architektoniczny:

\[
\boxed{
\text{globalna informacja transportowa może być zadaniowo konieczna,}
\quad
\text{ale nie wymusza nowej roli semantycznej}.}
\]

---

## 14. Lokalny cross-check

### Typy
`PASS`: pętla, płaszczyzna normalna, transport i mapa powrotu są rozdzielone.

### Interval / loop
`PASS`: C19-v3 nie jest rozszerzane po cichu na `S^1`.

### Holonomy / torsion
`PASS`: holonomia jest podstawowa; całkowita torsja pojawia się tylko na globalnie Frenet-legalnej dziedzinie.

### Gauge
`PASS`: stały lub okresowy gauge nie usuwa globalnej przeszkody; nieokresowy gauge na cut interval nie jest globalną transformacją na pętli.

### CORE
`PASS`: C22–C24 pozostają derived/bridge; brak CORE6.

### Freeze impact
`PASS`: Freeze Errata 01 dotyczy MINI singleton claim i nie zmienia twierdzeń C22–C24.

---

## 15. Werdykt II.15

\[
\boxed{
\mathrm{II.15\ CLOSED\ FRAME/HOLONOMY}
=\mathrm{PASS}.
}
\]

Następny legalny krok: globalny cross-check FRAME jako warstwy jednoelementowej, a następnie HIGHER C29–C33.
