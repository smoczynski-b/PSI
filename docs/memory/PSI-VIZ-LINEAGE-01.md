# PSI-VIZ-LINEAGE-01 — rodowód języka wizualnego PSI

**Status:** EXPERIMENTAL / NON-CANONICAL / PROVENANCE CORRECTION  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Source conversation:** `Konstruowanie litery a` (user-provided conversation extract).  
**Does not modify:** CORE5, CANON-03, theorem status, current F0 repair order.

## 1. Korekta proweniencji

Materiał ustanawiający język PSI-VIZ nie pochodzi z `Semantica Rozmowy — 04`.
Jego bezpośrednim źródłem jest rozmowa `Konstruowanie litery a`.

`Semantica Rozmowy — 04` pozostaje źródłem kontroli reprezentacji, pamięci aktywnej,
rozróżnienia stanu autorytatywnego od widoku i ograniczeń kosztu. `Konstruowanie
litery a` jest natomiast źródłem koncepcji ruchomej notacji i pierwszego prototypu
PSI-VIZ.

Nie scalać tych dwóch rodowodów tylko dlatego, że oba dotyczą reprezentacji.

## 2. Zasady odzyskane z rozmowy

### 2.1 Byrne Dynamic

Zasada bazowa:

\[
\boxed{\text{symbol matematyczny}=\text{ten sam obiekt graficzny w całym wywodzie}}
\]

Kolor nie jest dekoracją. Jest składnikiem notacji i ma zachowywać tożsamość
obiektu przez kolejne sceny i reprezentacje.

### 2.2 Ruch wykonuje matematykę

\[
\boxed{\text{animacja nie ilustruje przejścia — animacja jest przejściem}}
\]

Ilorazowanie powinno być widoczne jako sklejenie, rozdzielenie jako rozszczepienie,
a faktoryzacja jako zachowana korespondencja pomiędzy zsynchronizowanymi panelami.

### 2.3 Zsynchronizowane reprezentacje

Ten sam stan/parametr jest śledzony równocześnie w wielu odwzorowaniach:

\[
X(t)\mapsto F_1(X(t)),F_2(X(t)),\ldots
\]

Linie korespondencji reprezentują operator lub mapowanie, a nie dekoracyjne
połączenie ekranowe.

### 2.4 Kolor + ruch + położenie = notacja

Kandydacka gramatyka:

- kolor — trwała identyfikacja typu/obiektu;
- ruch — przejście/operator/dynamika;
- położenie — jawnie określona rola reprezentacyjna;
- linia korespondencji — mapowanie pomiędzy reprezentacjami;
- sklejenie — utrata rozróżnienia/iloraz;
- rozszczepienie — obserwacja rozdzielająca lub kontrprzykład.

Położenie ekranowe samo z siebie nie uzyskuje semantyki. Gdy koduje koszt,
czas, tolerancję lub wielkość fizyczną, znaczenie musi być jawne w kontrakcie.

## 3. PSI-VIZ-TEST-01 — faktoryzacja

Pierwszy prototyp rozmowy używał:

\[
\Omega=\mathbb R^2,\qquad \rho(u,v)=u.
\]

Przypadek dodatni:

\[
R(u,v)=u^2,\qquad g(s)=s^2,
\]

więc

\[
R=g\circ\rho.
\]

Przypadek ujemny:

\[
R(u,v)=v.
\]

Dla

\[
x_+=(u,v),\qquad x_-=(u,-v)
\]

zachodzi

\[
\rho(x_+)=\rho(x_-),\qquad R(x_+)\neq R(x_-),
\]

co wizualnie pokazuje pęknięcie faktoryzacji po wcześniejszym sklejeniu przez
\(\rho\).

Prototyp ustanowił mechanizm:

```text
jeden parametr
→ równoległe reprezentacje
→ trwała identyfikacja kolorem
→ operator widoczny jako ruch
→ kontrprzykład widoczny jako zerwanie korespondencji
```

## 4. Styl wykonawczy

Źródłowa koncepcja preferuje estetykę ożywionej karty traktatu matematycznego:

- kość słoniowa / czerń / czerwień / błękit / żółć;
- brak gradientów i poświaty;
- duże marginesy;
- antykwa;
- wzór i figura dominują nad komentarzem;
- kluczowa klatka powinna działać także jako plansza drukowana.

Manim został wskazany jako naturalne główne narzędzie dla dowodów,
faktoryzacji, włókien, diagramów i operatorów; Blender tylko dla scen naprawdę
przestrzennych. Jest to decyzja robocza PSI-VIZ, nie część kanonu matematycznego.

## 5. Relacja do pamięci aktywnej

Późniejsza pamięć aktywna narzuca dodatkowy rygiel na ten język wizualny.
Wizualizacja musi być widokiem konkretnego stanu:

```text
memory_revision
+ contract_id
+ object ids
+ typed relations
+ required provenance/status/version
```

Zatem:

\[
\boxed{\text{PSI-VIZ notation}\neq\text{authoritative memory}}
\]

oraz

\[
\boxed{\text{structural relation}\neq\text{embedding geometry}\neq\text{display layout}}.
\]

Rodowód `Konstruowanie litery a` dostarcza gramatyki ruchomej; `Rozmowy — 04`
dostarczają późniejszych rygli adekwatności reprezentacji. Obie warstwy są
komplementarne, ale nie są tym samym źródłem.

## 6. Status

Ta korekta nie przesuwa F4 przed aktualne naprawy F0/F1. Zachowuje tylko poprawny
rodowód i materiał projektowy, który ma zostać użyty, gdy front dojdzie do F4.

Nie wynika z niej jeszcze, że wizualizacja poprawia jakość rozumowania modelu.
To pozostaje zadaniem pomiarowym F5.
