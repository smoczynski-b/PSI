# PRINCIPIA SEMANTICA — TOM II
## II.13. Kanoniczny zakres PSI-CAT i PSI-FACT

**Status:** `CANONICAL DEFINITIONS / SCOPE BRIDGE / PROSE PASS 01 / LOCAL CROSS-CHECK PASS`  
**Źródło nadrzędne:** fizyczny `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Rejestr tez:** `claim-registry-12.md`, C62–C66  
**Źródło migracyjne:** `cat-fact-migration-01.md`  
**Falsifikatory:** F55, F58, F59  
**Zakres:** bieżące minimalne definicje CAT/FACT oraz status starszych rozszerzeń; bez twierdzenia o wyczerpującej klasyfikacji wszystkich zmian katalogu i bez uniwersalnego homotopijnego modelu FACT.

---

## 1. PSI-ID i PSI-CAT są różnymi pytaniami

Ustalmy kontrakt `c`, protokół `P`, dane `Y` oraz bieżący katalog kandydatów.

`PSI-ID` pyta o identyfikowalność **wewnątrz ustalonego katalogu**.

`PSI-CAT` pyta natomiast, czy dane i protokół uzasadniają zmianę katalogu, a jeżeli tak — jakiego rodzaju zmiana jest licencjonowana.

Dlatego kanonicznie:

\[
\boxed{
\mathrm{PSI\!-\!ID}\neq\mathrm{PSI\!-\!CAT}.
}
\]

Różnica nie jest terminologiczna. W pierwszym problemie przestrzeń kandydatów jest częścią zamrożonego kontraktu. W drugim sama adekwatność katalogu staje się przedmiotem metaidentyfikacji.

---

## 2. PSI-CAT^D i warunki dziedzinowe

Dla dziedziny realizacji `D` wprowadzamy warunki dopuszczalności

\[
\operatorname{ADM}_D.
\]

Mogą one eliminować hipotezy nielegalne mechanicznie, chemicznie, geometrycznie, biologicznie lub z innego powodu właściwego dziedzinie.

Nie wolno jednak utożsamiać eliminacji dziedzinowej z nową obserwacją empiryczną:

\[
\boxed{
\text{domain restriction}
\neq
\text{new observation}.
}
\]

Warunki `ADM_D` ograniczają zbiór hipotez; nie dopisują nowych danych do `Y`.

---

## 3. Adekwatność katalogu jest bramką, nie jednym skalarem

Bieżący kanon zamraża kolejność:

\[
\boxed{
\text{ADEKWATNOŚĆ KATALOGU}
\to
\text{WŁÓKNO}
\to
\text{ID LOKALNA}
\to
\text{ID GLOBALNA}
\to
\text{REDESIGN PROTOKOŁU}.
}
\]

Nie ustanawia natomiast jednego uniwersalnego skalara

\[
D_{\rm ADEQ}^{cat}
\]

jako prymitywu CORE.

Jeżeli konkretny kontrakt zawiera metrykę, pseudometrykę, funkcję straty, topologię lub tolerancję, można definiować metryczne adaptery adekwatności. Są one jednak zależne od kontraktu.

Zatem:

\[
\boxed{
\text{catalog adequacy is canonical as a question,}
\quad
D_{\rm ADEQ}^{cat}\text{ is adapter-dependent}.
}
\]

---

## 4. Kanoniczna definicja PSI-FACT

Dla dziedziny `D`, protokołu `P`, tolerancji `\varepsilon` i danych `Y` PSI-FACT bada włókno

\[
\boxed{
\operatorname{Fact}^{\varepsilon}_{D,P}(Y).
}
\]

Jego obiekty są faktoryzacjami zgodnymi równocześnie z:

1. `ADM_D`;
2. zadeklarowanym interfejsem zewnętrznym;
3. zadeklarowanym kryterium zgodności danych z protokołem.

Realizacyjny gauge/relacja równoważności jest ilorazowana **tylko wtedy, gdy ustanawia ją kontrakt**.

Nie ma więc legalnej reguły:

\[
\text{natural symmetry}
\Rightarrow
\text{automatic FACT quotient}.
\]

Obowiązuje F55.

---

## 5. Równoważność realizacyjna i recode

Kanonicznie rozdzielamy:

\[
\boxed{
\text{realization equivalence}
\neq
\text{behavioural recoding}.
}
\]

Równoważność realizacyjna usuwa różne prezentacje tego samego obiektu zgodnie z legalnym gauge kontraktu.

Recode może natomiast zachowywać istotne zachowanie przy zmianie sposobu realizacji. Jednokierunkowy recode nie musi mieć odwrotności i dlatego nie musi być równoważnością.

To rozdzielenie jest konieczne, aby nie traktować każdej zmiany reprezentacji jako czystego gauge ani każdej naprawy reprezentacji jako narodzin nowego katalogu.

---

## 6. Awaria reprezentacji nie implikuje narodzin katalogu

Z faktu, że konkretna reprezentacja przestaje być legalna lub regularna, nie wynika jeszcze:

\[
\boxed{
\text{representation failure}
\Rightarrow
\text{catalog birth}.
}
\]

Poprawna zasada jest negatywna:

\[
\boxed{
\text{representation failure}
\not\Rightarrow
\text{catalog birth}.
}
\]

Twierdzenie o `birth` wymaga wykazania, że w bieżącym katalogu nie istnieje legalna reprezentacja/recode zachowująca wymagane interfejsy i semantykę zadania.

MINI Frenet/Bishop będzie w II.14 przykładem, w którym utrata legalności Freneta przy `\kappa=0` jest naprawą domeny/recode, a nie automatycznym `birth`.

---

## 7. Starszy rachunek CAT ma status pochodny

Starsze źródła wprowadzają klasy m.in.

\[
\mathsf{ISO}_{CAT},
\quad
\mathsf{HOR}_{CAT},
\quad
\mathsf{REF}_{CAT},
\quad
\mathsf{CRS}_{CAT}
\]

oraz workflow

\[
\mathrm{GEN}\neq\mathrm{TEST}\neq\mathrm{SELECT}.
\]

Pozostają użytecznym **pochodnym rachunkiem typowanym**, ale bieżący kanon nie ustanawia twierdzenia, że każda możliwa zmiana katalogu należy dokładnie do jednej z tych klas.

Nie wolno zatem wykonywać przejścia:

\[
\text{older typed source}
\Rightarrow
\text{current canonical definition}.
\]

Obowiązuje F58.

---

## 8. Groupoid / homotopy FACT jest rozszerzeniem, nie definicją uniwersalną

Starszy aparat FACT może zachowywać:

- automorfizmy i stabilizatory realizacji;
- wielość świadków kompatybilności;
- dane morfizmów;
- homotopijne/weak-fibre informacje.

Taki model jest właściwy, gdy kontrakt lub zadanie rozróżnia te dane.

Nie wynika z tego jednak:

\[
\boxed{
\operatorname{Fact}^{\varepsilon}_{D,P}(Y)
\text{ musi być zawsze homotopy fibre}.}
\]

Kanoniczny minimalny FACT pozostaje definicją kontraktową C63; bogatsza struktura jest dołączana wtedy, gdy jest potrzebna do zachowania informacji zadaniowej.

To dokładnie blokuje F59.

---

## 9. Relacja do HIGHER-FIBRE

HIGHER-FIBRE nie redefiniuje FACT. Pokazuje jedynie, że niekiedy przedwczesna truncacja do zbioru klas/składowych usuwa informację istotną dla zadania.

Zasada operacyjna:

\[
\boxed{
\text{preserve required structured compatibility data first}
\to
\text{apply only task-legal truncation later}.
}
\]

Jest to zastosowanie ogólnego kryterium adekwatności reprezentacji, nie nowy prymityw FACT.

---

## 10. Co jest kanoniczne, a co pochodne

### Kanoniczne teraz

- `PSI-ID != PSI-CAT`;
- CAT jako metaidentyfikacja konieczności/klasy zmiany katalogu;
- `PSI-CAT^D` z `ADM_D`;
- `Fact^epsilon_{D,P}(Y)` jako włókno zgodnych faktoryzacji;
- gauge FACT tylko, gdy ustanawia go kontrakt;
- realization equivalence != behavioural recoding;
- catalog adequacy jako bramka poprzedzająca identyfikację.

### Pochodne / opcjonalne

- `ISO/HOR/REF/CRS`;
- `GEN/TEST/SELECT`;
- szczególne progi `birth/death`;
- skalary `D_ADEQ^cat`;
- factorization groupoids;
- homotopy/weak ADEQ fibres.

Ich legalność i przydatność zależą od jawnego kontraktu.

---

## 11. Lokalny cross-check

### Zgodność z fizycznym CANON-03
`PASS`: C62/C63 pozostają mniejszymi definicjami nadrzędnymi; starsza aparatura nie została awansowana.

### F58 — old-source promotion
`PASS`: wszystkie starsze rachunki są jawnie oznaczone jako pochodne.

### F59 — MINI/general FACT conflation
`PASS`: MINI nie definiuje generalnego FACT.

### F55 — gauge/observation
`PASS`: quotient FACT wymaga legalności kontraktowej; brak automatycznego gauge z samej symetrii.

### Primitive growth
`PASS`: brak CORE6, brak Agent v03.

### Scope
`PASS`: tekst nie ustanawia wyczerpującej ontologii zmian katalogu ani uniwersalnego homotopy FACT.

---

## 12. Werdykt II.13

\[
\boxed{
\mathrm{II.13\ CAT/FACT\ CANONICAL\ SCOPE}
=
\mathrm{PASS}.
}
\]

Następny krok: II.14 — ograniczone twierdzenie `CAT–FACT–NORM–MINI`, które musi pozostać zgodne z dwoma poprawnie otypowanymi kontraktami obserwacji/gauge i nie może zostać rozciągnięte na generalny PSI-FACT.
