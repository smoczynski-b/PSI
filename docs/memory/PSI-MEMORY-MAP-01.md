# PSI-MEMORY-MAP-01 — seed dependency map

**Status:** EXPERIMENTAL / OBSERVATIONAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Baseline:** `7f4aecdccb353994bf09df96847fe9ca9a4ab17e`  
**Date:** 2026-09-29

Current experimental objective and next evaluation:
[shared-memory entry](README.md). This seed remains historical evidence.

## 0. Purpose

This experiment does **not** define the final PSI memory architecture. It reconstructs a first typed dependency map from current PSI control records and theorem maps, then uses the reconstruction itself to discover the architecture that a shared agent memory actually needs.

The working object is a directed typed graph

\[
\mathcal M_{PSI}=(V,E),
\]

while a dependency tree is only a task-relative view

\[
T_{r,R}=\operatorname{View}_{r,R}(\mathcal M_{PSI})
\]

obtained from root `r` and a selected relation family `R`.

Seed data:

- `psi-memory-nodes-01.tsv`
- `psi-memory-edges-01.tsv`

Only source-attested relations are admitted to the seed verified layer. Semantic bridges suggested by an agent but not yet bound to evidence belong later to a separate `CANDIDATE` layer.

## 1. Source boundary

Initial extraction uses the current control surface only:

- `docs/control-state.json`;
- `docs/theorem-map-v2.md`;
- `docs/theorem-map-v3.md`;
- `docs/principia-v2-13-cat-fact-canonical-scope.md`;
- `docs/principia-v2-14-cat-fact-norm-mini.md`;
- `docs/principia-v3-p9h-composition-crosscheck-01.md`.

The seed is therefore deliberately incomplete. Missing relation != false relation.

## 2. First tree views

### 2.1 Control / provenance tree

```text
CONTROL-STATE
├── CLAIM-REGISTRY
├── FALSIFIER-REGISTRY
├── THEOREM-MAP-V2
│   ├── II.1 ... II.16
└── THEOREM-MAP-V3
    ├── III.1 ... III.12
    └── P9-I [OPEN gate for III.13]
```

This is an indexing/provenance tree, **not** a proof tree.

### 2.2 Exact-history dependency view

```text
II.9 --DEPENDS_ON------> II.7
II.9 --ANALOGY_TO------> II.6
II.9 --NOT_DEPENDS_ON--> II.8
```

The current theorem map explicitly states that II.9 depends on II.7/C57-C58 plus typed extension definitions, is structurally analogous to II.6, and does not require II.8 as a proof prerequisite.

This already falsifies an untyped edge model.

### 2.3 CAT / FACT / normalization view

```text
CANON-03
   |
   +--> II.13 [CAT/FACT canonical scope]
             |
             +--SCOPE_FOR--> II.14 [finite Frenet/Bishop normalization MINI]

II.13 --> PSI-CAT
II.13 --> PSI-FACT
II.15 --> FRAME
II.16 --> HIGHER
```

II.14 is not general PSI-FACT. It is a bounded exact-noiseless realization under two typed observation/gauge contracts. Therefore the edge from II.14 to II.13 must preserve **scope**, not merely say `RELATED_TO`.

### 2.4 P9 / operator view

```text
III.7  MOST -------------------+
                               | COMPATIBLE_WITH
III.11 P9-G --SPECIAL_CASE_OF-> III.12 P9-H
                                  |
                                  +--NEXT_GATE--> P9-I
                                                     |
                                                     +--GATE_FOR--> III.13
```

III.11 is explicitly a special case of III.12 under `Q=G`; III.12 remains norm-contract sensitive and is checked for compatibility with III.7 MOST. P9-I is a scheduling/source-contract gate, not a proved theorem dependency.

## 3. Architectural findings from the seed

### A1. Logical relations form a graph; trees are task views

The same node participates simultaneously in proof, scope, provenance, genealogy and scheduling relations. The logical relation model is therefore a graph; trees are generated views. This does not prescribe physical storage: typed tables or files can preserve the same graph. Neither a graph database nor a coordinate embedding follows from this observation.

### A2. Edge typing is mandatory

At minimum the seed already needs distinct relations:

- `CURRENT_POINTER`
- `INDEXES`
- `SOURCE_CANON`
- `DEFINES`
- `DEPENDS_ON`
- `ANALOGY_TO`
- `NOT_DEPENDS_ON`
- `SCOPE_FROM`
- `REALIZES`
- `SPECIAL_CASE_OF`
- `COMPATIBLE_WITH`
- `CLASSIFIES_AS`
- `NEXT_GATE_AFTER`
- `GATE_FOR`
- `EVIDENCE_FOR`

Collapsing them to one adjacency relation would produce invalid inference paths.

### A3. Negative structural information is first-class memory

`NOT_DEPENDS_ON` is useful knowledge. A memory that stores only positive links will cause agents to repeat rejected dependency reconstructions.

### A4. Proof dependence, evidence provenance and work scheduling are orthogonal

`P9-I -> III.13` is a gate relation. `III.11 -> III.12` is a mathematical inclusion relation. `CONTROL-STATE -> THEOREM-MAP-V3` is a control pointer. They must not participate in the same automatic transitive closure.

### A5. Status belongs to nodes; validity propagation belongs to selected edge types

A future `REVOKED`/`STALE` propagation rule must operate only over dependency-bearing relation families. It must not propagate through `ANALOGY_TO`, `INDEXES` or mere scheduling edges.

### A6. Version identity will probably be necessary

Current records already distinguish withdrawn/current claim versions (for example C19-v2 vs C19-v3). The seed therefore treats stable IDs and version/status as separate concerns. Exact version-node semantics remain OPEN for the experiment.

### A7. Hyperedges remain an open architectural question

The current seed does not yet prove a need for hyperedges. If later reconstruction finds a result valid only under a conjunction such as `{C1,C2,C3} => C4` that cannot be represented safely by independent binary prerequisite edges, introduce a typed hyperedge only then.

## 4. Tests for the next extraction pass

### M1 — ancestry correctness

For a selected theorem node, compute ancestry separately for:

1. proof dependencies;
2. scope/contract dependencies;
3. evidence provenance;
4. genealogy;
5. scheduling.

The five closures must not be silently merged.

### M2 — invalidation simulation

Temporarily mark one prerequisite node `REVOKED` in a copy of the map. Determine exactly which descendants become `STALE` under dependency-bearing edge types. Unrelated analogies and index links must remain unaffected.

### M3 — distant bridge

Introduce one explicitly evidenced long-range bridge and measure whether a bounded local view can reach a useful remote cluster without loading the full repository.

### M4 — context compression

For one real PSI task compare:

\[
A+\text{broad repository context}
\]

against

\[
A+\operatorname{View}_{task}(\mathcal M_{PSI}).
\]

Measure reads, repeated reconstruction, tokens/context volume, errors and result quality.

## 5. Stop condition for MAP-01 seed

This unit stops when:

1. the seed nodes and typed edges are materialized;
2. every seed edge is traceable to an inspected source;
3. first architectural findings are recorded;
4. no claim is made that the schema is final.

Next unit after this seed: expand one dependency sector deeply enough to run M1 and M2. The preferred sector is the exact-history/memory chain II.7–II.12 because it directly concerns memory adequacy and already contains explicit distinctions between proof dependency, analogy, quotient minimality and algorithmics.


---

## 6. Nakładka MATH-28–76 (2026-10-24) — mapa matematyki M, NIE nowy kanon

**Status:** \`CANDIDATE / EDITORIAL / NON-CANONICAL / INDEPENDENT_REVIEW_PENDING\`.
Ten aneks jest późniejszą nakładką na historyczny seed MAP-01 z 29 września. **Nie zmienia jego ówczesnego zbioru świadków ani zdania o granicy seed.** Nowe serie MATH-N powstały później i nie dziedziczą statusów \`PASS\` starych II.1–II.16.

Rzeczywista, maszynowo czytelna **warstwa kandydacka**:
- [węzły MATH](psi-memory-nodes-math-migration-20261024.tsv);
- [typowane relacje MATH → poprzedniki Tomu II](psi-memory-edges-math-migration-20261024.tsv).

Historyczne \`psi-memory-nodes-01.tsv\`, \`psi-memory-edges-01.tsv\`, certyfikaty dowodowe i wcześniejsze testy pozostają bez zmian. Nakładka nie jest częścią oryginalnego zweryfikowanego seed ani automatycznego przejścia statusów. Oba pliki mają zgodny z oryginalnym schemat tabulatorowy, lecz **ich relacje są kandydackie i nie mogą uczestniczyć w propagowaniu \`STALE/VALID\` po krawędziach \`DEPENDS_ON\`**.

### 6.1. Dwa różne kierunki organizacji

Rozróżniamy **źródła badań MATH-N** i **istniejące twierdzenia Tomu II**. Krawędzie \`INDEXES / SOURCE_OF\` porządkują źródła; \`OVERLAP_TO_AUDIT / FINITE_REALIZATION_CANDIDATE / SCOPE_EXTENSION_CANDIDATE\` wskazują zadanie porównawcze. Nie stanowią przesłanek dowodu, przyjęcia twierdzenia ani produkcyjnej propagacji ważności. Nawet wspólny wzór może dotyczyć różnych alfabetów działań, legalności lub etykiet terminalnych.

### 6.2. Mapa merytoryczna w skrócie

| Strumień | Odpowiednik / obszar | Ustalony zakres |
|---|---|---|
| MATH-28–40 | Podpory i ważone wycofanie | 13 wpisów jednostkowych; kombinatoryka i ograniczenia zakresowe, §6.7. |
| MATH-41–56 | Aktualizacja kosztu, profile informacji, pamięć dodawania | 16 wpisów jednostkowych; nie utożsamiać dodawania z nazwanym usuwaniem, §6.8. |
| MATH-57–69 | II.4, II.7–II.9, proweniencja i certyfikaty awarii | 13 wpisów; aktywna errata MATH-57 i oddzielny odbiór E-001 MATH-69, §6.9. |
| MATH-70–74 | Minimalne konflikty oznaczonych katalogów | 5 wpisów jednostkowych; [E-001 PASS_SCOPED](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353594375) **bez niezależnej enumeracji**; specjalizacje §6.11. |
| MATH-75 | Audyt zakresowy MATH-70–74 | Oddzielny SELF_CHECKED, nieobjęty odbiorem E-001. |
| MATH-76/T1–T4 | II.7–II.8: pamięć historii | Przyczynowe przypisanie korekty ≠ sama adekwatność pamięci. |
| MATH-76/T5–T21 | II.4: obserwacja, odporność i koszt | Oddzielne kontrakty błędów, adaptacji i kosztów. |
| MATH-76/T22–T25 | II.6/II.9: dynamika | Zachować cel historyczny mimo interwencji. |
| MATH-76/T26–T27 | II.7–II.9, II.11; II.12 jako granica | Porównanie **wykonane**: zakresowe ponowne użycie i klasyczna rafinacja, §6.5. |
| MATH-76/T28–T34 | II.4/II.6/II.9; polityki i cele | Audyt **wykonany**, wynik SELF_CHECKED, §6.6; aktywna errata K14. |

Tabela jest **spisem orientacyjnym**, nie osobnym rejestrem twierdzeń ani stwierdzeniem naukowej nowości. Rozstrzygnięcia i świadkowie znajdują się w wskazanych sekcjach oraz oryginałach Issue #13.

### 6.3. Źródła bieżące i zachowanie granic

Źródłowy rejestr: [Issue #13](https://github.com/smoczynski-b/psi-model/issues/13); indeks [MATH76_SHARED_INDEX](https://github.com/smoczynski-b/psi-model/blob/5d41732861f02fd65f20e93ab7b824be14196502/psi-agent/handoff/MATH76_SHARED_INDEX_20261024.md); wcześniejsza [PRINCIPIA_MIGRATION_01 §6](https://github.com/smoczynski-b/psi-model/blob/e1de79e7ffd6a72186f4dcfee287a8beaafc09ee/psi-agent/PRINCIPIA_MIGRATION_01.md).

**Przed nowym dowodem:** odczytać źródło i erraty; sprawdzić \`TYP / DZIEDZINA / ZAŁOŻENIA / ZAKRES\`; sklasyfikować \`REUSE / ADAPT_CONTRACT / REAL_GAP / CONTRADICTION\`. Nowy numer MATH nie oznacza nowego rozdziału ani niezależnego odkrycia.

**Stan faktyczny indeksu:** w nakładce jest 66 węzłów i 156 typowanych relacji. Osobne węzły obejmują MATH-28–74, istnieje grupowanie MATH-70–74 i oddzielny MATH-75. Nie oznacza to zakończenia powiązań jednostkowych: w szczególności MATH-70–74 mają źródłowe węzły, lecz nie mają jeszcze osobnych relacji \`INDEXES\` do węzła grupującego ani osobnych krawędzi do odbioru E-001. Wciąż poza pełną migracją są MATH-1–27. **Niepotwierdzone** pozostają produkcyjny odczyt nakładki i rzeczywiste wykorzystanie całej mapy przez role agentów. Szczegóły wykonawcze i odroczony odbiór — §6.10 i Issue #15.

Stan \`CANDIDATE / NON-CANONICAL\` jest niezmienny; CORE5/IFX bez zmian.

### 6.4. Rozdzielenie odbiorów i wykonania — korekta 24.10.2026

Odbiór [E-001 dla MATH-70–74](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353594375) dotyczy dowodów i kontrprzykładów **bez odtworzenia enumeracji**. Nie obejmuje MATH-75 (SELF_CHECKED). Statusu grupy nie wolno bezwarunkowo rozszerzać na inne zadania, ani traktować publikacji węzła jako odbioru testowego.

Bieżącą orientację Tomu II zapewnia [theorem-map-v2.md](../theorem-map-v2.md); dawny plan 01 nie zastępuje aktualnej mapy twierdzeń. Wynik redakcyjny M, niezależny odbiór matematyczny E i świadectwo wykonawcze Node stanowią **odrębne zdarzenia**. Wykonawczy stan Node: [PASS_SCOPED dla ręcznej nawigacji i świadka MATH-57/MATH-69](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383537912), lecz \`DEFAULT_RUNTIME_INTEGRATION=PARTIAL/HOLD\`. Próby integracyjne pozostają [odroczone na podstawie decyzji właściciela](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383640277). Node i E korzystają z kosztownego Sola; nie należy zlecać nowych prób bez osobnego zezwolenia. Dokładny kontrakt przyszłego odbioru zawiera §6.10.

### 6.5. Wynik porównania T26–T27 z II.7–II.12 — 24.10.2026

[Pełny argument M i warunki odwzorowania w Issue #13](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383015907); status `DERIVED / SELF_CHECKED / INDEPENDENT_REVIEW_PENDING`. Źródła wcześniejszych jednostek II.7/8/9/11/12 przypięte do commita `b4c21748fc855b01d8b89dfed36ca57842bad863`; oryginał T26–T27 [#6377888676](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377888676). To **wynik samokontroli**, nie recenzja E/Node ani uruchomienie LAB.

**Rozstrzygnięcie pod jawnie ograniczonym kontraktem:** Przy skończonym pełnym stanie Markowa S, globalnie legalnych akcjach, aktualizacji belief F, zachowanym celu historycznym q (T25), domknięciu na obserwacje i etykietach przyszłości ograniczonych dokładnie do `tau={v,?,BOT}`, równoważność T26 na **osiągalnych** B(H) jest realizacją przyszłościowej równoważności II.7, a jej najgrubszy iloraz — **ponownym użyciem** II.8. Nie jest nowym prymitywem/rozdziałem PSI. Kongruencja daje aktualizację klas II.9, ale nie zależy dowodowo od najgrubszości II.8.

**Granice:** T26 nie odwzorowuje automatycznie kontraktu II.7 zawierającego bogatsze etykiety niż tau (np. cały zbiór q(B)), działań częściowo legalnych z II.9/T30, historii o niezapisanym celu pierwotnym, brakujących trwałych zmiennych operacyjnych, czasu wpływającego na przyszłość ani nieosiągalnych stanów wiedzy. `BOT` jest oznaczeniem obserwacji niemożliwej, nie legitymizacją nielegalnego działania.

**T27:** skończona rafinacja od `ker(tau)` przez wspólne następniki stabilizuje się po ≤ `N-|im(tau)|` ostrych rozdrobnieniach (N — liczba stanów rodziny po dołączeniu `BOT`); jest to klasyczna adaptacja skończonego udoskonalania partycji, nie nowy twór matematyczny. **Nie wynika** z tego algorytm Paige’a–Tarjana, oszacowanie czasu ani pamięci; wymaga osobnego wykazania PT1–PT4 oraz kosztów konstrukcji wejścia. Dla celów historycznych T28–T34 i erraty K14 porównanie pozostaje zadaniem odrębnym.

**Zmiana warstwy krawędzi:** w kandydackim pliku TSV nadano relacje `SCOPED_REUSE_SELF_CHECKED` do II.7/II.8 i `SCOPED_UPDATE_SELF_CHECKED` do II.9, nie zmieniono `DEPENDS_ON`, `NOT_DEPENDS_ON` ani historycznych węzłów PASS. Relacje `II.11` i `II.12` pozostają odpowiednio klasycznym mostem-kandydatem i analogią algorytmiczną. To status **powiązania redakcyjnego**, nie automatyczna promocja twierdzenia.

**Odbiór wykonawczy:** opis przypadku odzyskania mapy dla Node w [Issue #13](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383015907); realny test należy wyłącznie do Node i musi mieć własne świadectwo. Stara historyczna mapa i zweryfikowane dowody pozostały nienaruszone.

### 6.6. Audyt T28–T34 — pamięć wybranej polityki, legalność i wiele zadań (24.10.2026)

[Pełna analiza MATH-76/T28–T34, ze ścisłym świadkiem i oceną ograniczeń](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383100190); oryginały [T28–T29](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377894286), [T30](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377935903), [T31](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377942281), [T32–T34](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377949608), [obowiązująca errata K14](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377898833). Status **SELF_CHECKED / EDITORIAL CANDIDATE / INDEPENDENT_REVIEW_PENDING**; nie nowy CORE5, tom ani numer MATH.

**T28–T29:** nie są powtórzeniem dokładnej pamięci wszystkich przyszłych doświadczeń z II.7–II.9. W określonej klasie deterministycznych stacjonarnych sterowników i kodowań `rho(B)` wymagają tylko (P1) adekwatnej decyzji STOP (II.4), (P2) wspólnego działania optymalnego w klasie, (P3) reprezentantowo niezależnej aktualizacji kodu **po wybranym działaniu** (II.6 / II.9). Bellman i koszty są częścią nowego *kontraktu decyzyjnego*, nie nowej teorii ogólnych ilorazów. Istnieje ścisły świadek osłabienia: dwa stany informacji `B0,B1` wymagają osobnych klas, jeśli zachowujemy możliwość wszystkich przyszłych sond, ale optymalna polityka wybiera tę samą sondę i może je skleić; kompletne dane świadectwa w powyższym źródle. T29 to dolny kres pokryciowy, nie dokładny wzór kosztu rzeczywistego pamiętania.

**T30:** formuła `A(B)=∩_{s∈B} A(s)` dotyczy bezpiecznej LEGALNOŚCI CZYNNOŚCI dla całego włókna, a nie *informacyjnej legalności redukcji* z II.5. II.9 już rozpoznaje częściową dziedzinę rozszerzenia, ale konkretne przecięcie katalogów wynika z dodatkowego kontraktu epistemicznego.

**T31–T32:** wspólne kodowanie wielu zadań **uruchamianych oddzielnie**, przy zewnętrznym `task_id`; to nie pamięć gwarantująca późniejsze przełączenie między celami. Dolny kres `max_i(kappa_i+r_i)` jest ponownym użyciem T29; nie sumować kosztów kodów zadań bez dowodu braku możliwości współdzielenia.

**T33/K17:** osobna identyfikowalność historycznych współrzędnych nie implikuje identyfikowalności wspólnej przy destrukcyjnych działaniach. Kryterium rozstrzygalności dla całego `q_joint` **już daje** T23/T30; nie ogłaszać tej decyzji kolejnym otwartym twierdzeniem. **T34:** monotoniczność `V_i(B')≤V_i(B)` po poprawnym zawężeniu `B'⊆B` w tym samym kontrakcie Γ, A, kosztów jest adaptacją zasady zawężania zbioru scenariuszy, nie prawem o opłacalności kosztownej obserwacji.

**Proponowane miejsce w Tomie II:** **jeden kandydacki podrozdział** o wystarczalności pamięci dla optymalnej polityki w skończonym układzie dynamicznym, z T28 jako rdzeniem, T29–T34 jako ograniczeniami i zastosowaniami. Unikać siedmiu nowych jednostek książkowych. Nie promować bez recenzji kontraktu.

**Późniejszy wynik Node:** [#15 / 6383537912](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383537912) potwierdził ręcznie skonfigurowaną nawigację i świadka MATH-57/MATH-69 jako `PASS_SCOPED`, lecz nie domyślną integrację (`PARTIAL/HOLD`, brak adaptacji pola `effect` i odbioru zabezpieczeń propagacji). Dalsze próby są odroczone; §6.10.

### 6.7. Jednostkowa mapa MATH-28–40 — pierwsza konsolidacja 24.10.2026

**Zakres pracy:** odczyt trzynastu pierwotnych wyników MATH-28–40 z [Issue #13](https://github.com/smoczynski-b/psi-model/issues/13), rozdzielenie oryginałów od zakresowych recenzji i korekt. Dalsze pliki nakładki rozszerzono bez zmiany oryginalnego `psi-memory-*-01.tsv`, kanonu ani typowanych krawędzi dowodowych. Warstwa redakcyjna **nie uczestniczy w produkcyjnej propagacji statusów** (Node wcześniej wykazał brak adaptera: `KeyError: 'effect'`).

| Wyniki źródłowe | Treść, porównanie i docelowe miejsce |
|---|---|
| [MATH-28](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6349643488), [29](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6349855541), [30](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6349963228) | Grafowe wycofanie → graf ważony → zbiór trafiający w hipergrafie rangi r. `MATH-28 SPECIAL_CASE_OF MATH-29 SPECIAL_CASE_OF MATH-30`. Przykłady grafowe, LP i ostrość współczynników zebrać razem, bez trzech odrębnych twierdzeń książkowych. Są to klasyczne narzędzia kombinatoryczne; oryginalność PSI dotyczy znaczenia modeli świadectw i kontraktów, nie klasycznego zaokrąglania LP. |
| [MATH-31](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350196435), [32](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350231747), [33](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350235307), [34](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350239727) | Semantyka aktywnych minimalnych podpór; koszt dla drzew `read-once`; kontrprzykład dzielenia kosztu wspólnej etykiety w DAG; bezstratna redukcja do antyłańcucha. `MATH-31 REDUCES_TO MATH-30` tylko przy jawnej semantyce monotonicznej; `MATH-33` koryguje niedozwolone rozszerzenie wzoru OR, nie obala poprawnego MATH-32. **MATH-32 ma samokorektę enumeracji przykładu (3) w tym samym komentarzu**; zachować poprawioną listę `{a,b},{c,d}`. |
| [MATH-35](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350257688), [36](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350263953) | Minimalne zbiory wycofań i ich dokładna rekurencja w DAG; `Tr(Tr(E))=Min(E)`, odróżniając pustą rodzinę podpór od pustej podpory. Ten sam kontrakt monotonicznej funkcji w dwóch dualnych opisach, **nie** dualność programowania liniowego MATH-30. |
| [MATH-37](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350358291), [38](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350363160), [39](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350375932), [40](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350382780) | Dwie rodziny `F_m` i `G_m`; kolejno liczba minimalnych podpor/wycofań, minimalny koszt i liczba operacji, liczba rozwiązań optymalnych i warunki ich jednoznaczności oraz margines perturbacji kosztów. Rozmiar antyłańcucha, koszt minimum i liczba optymalnych rozwiązań to **odrębne niezmienniki**. Wnioski i przykłady z poprzednich jednostek, nie osobny szereg czterech niezależnych podstaw teorii. |

**Niezależne statusy źródeł:**
- **28:** [E-001 PASS_SCOPED](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6349736445) po kontroli wyniku i przykładu z MATH-12; **29:** [E-001 PASS_SCOPED/ACCEPTED](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6349930315); **30:** [E-001 PASS_SCOPED/ACCEPTED](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350170345). Każdy odbiór ma własny zakres; brak roszczenia nowości.
- **31–36:** [zapisany przegląd logiczny MATH-31–36](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350331320) nie wykrył błędu zmieniającego wnioski w ocenianych modelach. **Nie utożsamiać** tego z odrębnym pełnym certyfikatem wszystkich elementów ani z audytem implementacji.
- **37–40:** `SELF_CHECKED / REVIEW_PENDING`. Nie odziedziczyły przyjęcia MATH-28–30 ani przeglądu 31–36.

**Klasyfikacja mapowania:** w istniejących TSV dopisano 13 węzłów `RESEARCH_CLAIM`, 13 relacji `INDEXES` z grupującego `MATH-28-40` i 15 odrębnych relacji tematycznie/dowodowo udokumentowanych w źródłach (`SPECIAL_CASE_OF`, `REDUCES_TO`, `DUALIZES`, itd.), **wszystkie na warstwie `EDITORIAL`**. Nie nadano im `DEPENDS_ON` produkcyjnego grafu, nie zmieniono historycznych statusów.

**Granica migracji:** rezultaty są kandydatami do jednej spójnej redakcyjnej części Tomu II (podpory i koszty wycofania) z klasycznymi rezultatami i kontrprzykładami, a nie trzynastoma nowymi twierdzeniami PSI. Łączenie w gotowe twierdzenia monografii wymaga porównania z pozostałymi MATH-1–27 i MATH-41–75 oraz literaturą. Oryginalne komentarze i historyczne źródła pozostają jako proweniencja. Node jako jedyny upoważniony wykonuje rzeczywiste próby integracji grafu z istniejącym programem; publikacja TSV nie stanowi PASS wykonawczego.

### 6.8. Jednostkowa mapa MATH-41–56 — profile, aktualizacje i pamięć (24.10.2026)

**Zakres:** 16 historycznych MATH z [Issue #13](https://github.com/smoczynski-b/psi-model/issues/13), źródła sprawdzone indywidualnie, w tym dwuczęściowe MATH-50, MATH-52 i MATH-54 oraz [errata MATH-51](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351135835). Nowe węzły i relacje mają charakter `RESEARCH_CLAIM / EDITORIAL`; zachowują `SELF_CHECKED / INDEPENDENT_REVIEW_PENDING` i nie otrzymują produkcyjnych krawędzi `DEPENDS_ON` ani statusu `PASS` wcześniejszych II.x.

| Jednostki | Treść z oryginalnych dowodów | Decyzja redakcyjna |
|---|---|---|
| [41](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350435107)–[45](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350632775) | Monotoniczność kosztu po dodaniu jednej podpory, brak pod-/nadmodularności, separacja składowych i laminarność, pojedyncza podpora mostowa, wymuszenia zbiorowe `B_E(T)` i dwie podpory. | Jeden podrozdział: **aktualizowanie kosztu trafiania**, po redukcji MATH-28–40. Przykłady i warunki zakresowe nie powinny być niezależnymi rozdziałami. |
| [46](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350664499)–[48](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6350961047) | Profil wymuszeń singletonowych nie wystarcza dla dwóch dodatków; ogólnie `P_k(E)` wystarcza dla k dodatków. Dla określonej nowej rodziny Q próg uniwersalny to `h(Q)=max{|T|:T∈Tr(Q)}`, a nie `tau(Q)=min |T|`; ostrość wymaga kontraktu z dopuszczalnym dodatkowym źródłem i dodatnimi kosztami. | Wspólna jednostka: **ograniczenia informacji wystarczającej do przewidywania aktualizacji**. Bez automatycznego wniosku o liczbie bitów lub algorytmicznej złożoności. |
| [49](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351010655)–[53](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351323175) | `F_d(p)` = włókno rodzin E zgodnych z P_d, certyfikowane lecz nie zawsze ostre oszacowania; rekurencja aktualizacji profilu [50 A](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351064562) i [50 B](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351075806); próg `n-1` do pełnej semantyki [51](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351120228); trójdzielna klasyfikacja wycofań [52 A](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351254928) i [52 B](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351278240); dokładne osiągalne ekstrema [53](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351323175). | Kandydat do jednej jednostki o **identyfikowalności wartości i semantyki z ograniczonych profili**, jako realizacja wcześniejszego schematu PSI włókno–obserwacja–wielkość, a nie nowy CORE5. |
| [54 A](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351394154) i [54 B](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351411133), [55](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351455779), [56](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351498118) | `K_E=Min(U_E)` odtwarza przyszłe koszty przy samym DODAWANIU; pełny profil i nawet zaobserwowane minima rzędu d mogą być za słabe; nieodwracalność operatora `U→U∩U_Q`; usunięcie oznaczonego wpisu wymaga relacji `znacznik→podpora`. | Jeden blok o **dostatecznej pamięci kontynuacji i granicach rollbacku**, z osobną granicą proweniencji, prowadzącą do MATH-57–69. Nie utożsamiać semantyki z historią wpisów. |

**Krytyczne rozróżnienie:** `K_E` jest stanem wystarczającym dla przyszłego dodawania podpór i dla zadanej dodatniej wektorowej funkcji kosztu; **nie** jest automatycznie stanem wystarczającym dla usuwania historycznie wskazanego wpisu ani cofnięcia poprzedniego stanu. MATH-54/T4 bada dokładność wszystkich przyszłych aktualizacji względem ustalonego kontraktu i jest mostem-kandydatem do II.7/II.8. **Nie utożsamiać** całej historii PSI z samą rodziną minimalnych wycofań, nie dopisywać nowej zależności dowodowej II.9 od II.8.

**Errata obowiązująca:** [MATH-51 / 6351135835](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351135835) poprawia lokalną ilustrację: gdy `c_b=0`, właściwym aktywnym zbiorem rozdzielającym `E_1={{b}}` i `E_2=∅` jest `B={b}`, **nie** `B={a}`. Korekta jest osobnym węzłem `MATH-51-ERRATA`, powiązanym z MATH-51 typem `HAS_ERRATA`; nie zmienia zakresu twierdzenia dla dodatnich kosztów.

**Sfera źródłowa / statusy:** MATH-41–56 = `SELF_CHECKED / INDEPENDENT_REVIEW_PENDING`; nie przypisywać im odbiorów E-001 dotyczących MATH-28–30 lub MATH-69. Rezultaty są klasyfikowane jako `REUSE / ADAPT_CONTRACT / BRIDGE_CANDIDATE`; nie przedstawiać uogólnień klasycznego hipergrafowego trafiania jako już dowiedzionej nowości naukowej PSI. Dane TSV to warstwa orientacji, nie wdrożona pamięć agentów. Późniejszy wynik Node potwierdził tylko ograniczoną nawigację MATH-57/MATH-69; domyślny adapter pozostaje `HOLD` (§6.10). MATH-70–74 mają już osobne węzły źródłowe i odbiór E-001, ale jeszcze nie analogiczne osobne krawędzie relacyjne; MATH-75 zachowuje oddzielny status, MATH-1–27 pozostają poza migracją. CORE5/IFX bez zmian.

### 6.9. MATH-57–69 — pamięć oznaczonych wpisów, proweniencja i próg odporności (24.10.2026)

**Źródła i zakres:** [analiza M-012 z dowodem](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383455470), [MATH-57](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351600087) wraz z **obowiązującą [erratą](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351774428)**, [MATH-61](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6351811767) i źródłowe komentarze MATH-58–60, 62–69. Porównano z istniejącymi [II.4](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-04-representation-adequacy.md), [II.7](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-07-exact-history-memory-adequacy.md), [II.8](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-08-coarsest-exact-history-quotient.md) i [II.9](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-09-recursive-history-quotient-update.md) @`b4c21748`. Rejestracja oznaczonego wpisu i filtr zgodności rzeczywistej proweniencji to **dwa różne typy operacji**.

| Jednostki | Wynik i warunki | Kwalifikacja |
|---|---|---|
| **MATH-57 + errata, MATH-61** | Przy `V≠∅`, skończonym V, literalnym `+j:e` legalnym tylko dla `j∉Used` i `−j` tylko dla `j∈dom A`, pełne przyszłościowe drzewo legalności i semantyki spełnia `Beh(h)≅Beh(h') ⇔ (A(h),Used(h))=(A(h'),Used(h'))`. | **PONOWNE_UŻYCIE** II.7–II.9 po ADAPTACJI kontraktu. Z II.8 wynika iloraz `H/≈ ≅ im(A,Used)`; II.9 daje częściową aktualizację. Nie wynika minimalna liczba bitów; pula znaczników I nie musi być skończona. |
| **MATH-57 errata** | `h1=(+λ:{a})`, `h2=(+λ:{a},+μ:{a},−μ)`: identyczne aktywne A, różne Used. Żądanie `+μ:{a}` legalne tylko dla h1. | **AKTYWNA KOREKTA ZAKRESU.** Odczyt MATH-57 bez erraty i MATH-61 daje błędną odpowiedź na pytanie o legalność. |
| **MATH-58–61** | Rejestr formalny nie identyfikuje rzeczywistego `θ(j)`; filtrowanie `W↦W∩A_e` zachodzi w przestrzeni możliwych źródeł, nie w rodzinie katalogowych podpór. `|q(W)|=1` nie certyfikuje `θ_real∈W`. | **REALIZACJA SCHEMATU WŁÓKNA II.4**, z osobnym kontraktem prawdziwości świadectw. |
| **MATH-62–64** | Wycofanie filtrów i dopuszczalna liczba/koszt błędnych deklaracji. Progi `min|J(ω)|`, `min w(J(ω))` przy zadanych operacjach; trafność warunkowa wymaga poprawnej przestrzeni W0 i dopuszczalnego budżetu błędów rzeczywistego świata. | **ROZWINIĘCIE ZADANIOWE**. Liczba wpisów nie jest liczbą niezależnych przyczyn awarii. |
| **MATH-65–69** | Przy **zweryfikowanych** równaniach i nierównościach jednostek awarii: po ilorazie `E_=`, graf `H` koduje różność klas, `ρ_cert=min χ(H[C(J(ω))])`. MATH-66: przypadek dwudzielny; 67: dodanie krawędzi; 68: scalenie; 69: zgodne wielokrotne scalenia i oszacowanie `0≤ρ'−ρ≤r`. | **ROZWINIĘCIE KOMBINATORYCZNE** w odrębnej dziedzinie: krawędź grafu kolorowania ≠ krawędź zależności dowodowej w Mapie PSI. MATH-69 ma własny [E-001 PASS_SCOPED](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353231221), bez powtórzenia enumeracji. |

**Rozdział kontraktów.** Dla samego anonimowego **dodawania** monotonicznych podpór `K_E` z MATH-54 wystarcza do wszystkich przyszłych odpowiedzi kosztowych. Dla nazwanych usunięć i historycznie świeżych znaczników potrzebny jest dokładniejszy niezmiennik `(A,Used)`. Dla poznania rzeczywistej proweniencji nawet ten niezmiennik nie wystarcza bez dodatkowej obserwacji `θ`. Wszystkie trzy wyniki są względne wobec jawnie określonego zbioru dopuszczalnych zapytań: zmiana zapytań zmienia relację nierozróżnialności.

**Statusy i program wykonawczy:** MATH-57–68 `SELF_CHECKED/REVIEW_PENDING`; MATH-69 `E001_ACCEPTED_PROOF_SCOPED_ENUM_NOT_RERUN`. Węzły i relacje w `psi-memory-{nodes,edges}-math-migration-20261024.tsv` należą do warstwy orientacyjnej `EDITORIAL/SCOPE/INDEX`, bez produkcyjnej propagacji. Późniejszy [odbiór Node](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383537912) wykazał **PASS_SCOPED ręcznej nawigacji** MATH-57 → errata → MATH-61 oraz odzyskania odbioru MATH-69. Nie uruchomiono domyślnego importera: `stale_closure` surowej nakładki nadal zgłasza `KeyError: 'effect'`; integracja pozostaje `PARTIAL/HOLD` (§6.10). Nie jest to certyfikat produkcyjny ani nowe twierdzenie CORE5.

### 6.10. Kontrakt odczytu nakładki MATH przez istniejący program — warstwa nawigacji ≠ propagacja (24.10.2026)

**Pochodzenie wymagań:** rzeczywisty [odbiór Node M57/M69](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383537912) na PSI `8637e6bf` oraz lektura [`scripts/test_memory_map.py`](https://github.com/smoczynski-b/PSI/blob/8637e6bfb377042ce958eb7c4f6bbe49d1e1833c/scripts/test_memory_map.py), blob `9cb49087`. **Ten rozdział jest specyfikacją semantyczną dla Node, nie twierdzeniem o wdrożonym programie ani o wykonanej próbie.** Istniejący program-test M1–M3 czyta `psi-memory-{nodes,edges}-{history,bridges}-01.tsv`; odrębna nakładka `*-math-migration-20261024.tsv` nie jest wczytywana. Dawne krawędzie mają `effect ∈ {VALIDITY,BRIDGE_VALIDITY,NONE}`; nowa nakładka ma `layer ∈ {INDEX,EDITORIAL,SCOPE,EVIDENCE,...}` i **nie ma** `effect`.

**Wymagane rozdzielenie typów:**

1. Odczyt nawigacyjny: jawnie wskazane `psi-memory-nodes-math-migration-20261024.tsv` i `psi-memory-edges-math-migration-20261024.tsv`, z zachowaniem **oryginalnych** pól `(from,relation,to,layer,source,note)`; ścieżka źródłowa i status węzła nie mogą zostać zredukowane do samego `from/to`. Relacje o nieweryfikowanym zakresie nie stają się automatycznie `DEPENDS_ON`.
2. Odczyt propagacyjny: stary graf `history + bridges` ze sprawdzonym `effect`. Jedyną podstawą w `prerequisite_closure` i `stale_closure` pozostaje jawnie zatwierdzony `effect∈{VALIDITY,BRIDGE_VALIDITY}` **z tego grafu**, nie przekształcenie `layer` w `effect`. Nakładka MATH **nie uczestniczy** w tej propagacji.
3. Widok incydencji dla użytkownika może chodzić po relacjach z obu końców, lecz zapisuje **oryginalny kierunek** każdego `from→to`, aby wycofanie przesłanki nie było mylone z nawigacją bibliograficzną. W `MATH-57` musi odzyskać `HAS_ERRATA` i `QUALIFIES_SCOPE_OF` z MATH-57-ERRATA oraz relację do MATH-61 (skierowaną od MATH-61 do starego wyniku/erraty). Zakres dwukrokowy bez niekontrolowanego transytywnego rozszerzenia katalogu.
4. Odrębne pola odbioru: lokalny `readback/pass` potwierdza odczyt rekordu; `E001_ACCEPTED_PROOF_SCOPED_ENUM_NOT_RERUN` dotyczy zakresu oceny dowodu MATH-69, nie automatycznego potwierdzenia enumeracji ani całego podrozdziału.

**Minimalne warunki przyszłego odbioru przez Node (jedna zintegrowana próba, nie powtórzenie ręcznego świadka):**

| Wejście | Wynik oczekiwany |
|---|---|
| Zwykłe zapytanie istniejącą ścieżką `MATH-57` | Dostępne bez ręcznie składanego pliku próby źródło 6351600087 → aktywna errata 6351774428 → MATH-61 6351811767; pełna odpowiedź musi wymagać `(A,Used)` dla nazwanych operacji. |
| Zwykłe zapytanie `MATH-69` | Oryginał 6352758335 oraz osobno świadectwo E-001 6353231221 ze statusem `PASS_SCOPED`, wyraźnie bez ponownej enumeracji. |
| Wycofanie `MATH-57-ERRATA` albo `MATH-61` jako korzenia nawigacyjnego | Bez uprawnienia dowodowego **nie wolno** oznaczyć `MATH-57`, `II.7`, `II.8`, `II.9` jako przestarzałych jedynie wskutek incydencji redakcyjnej. |
| Wycofanie dawnego `C57` | Dawne potomki ważności M2 nadal zostają oznaczone zgodnie z history/bridges, ale kandydackie węzły MATH nie mogą dostać propagacji na podstawie samych relacji INDEX/EDITORIAL/SCOPE/EVIDENCE. |
| Brak pola, błędny typ, nieznany koniec, rozbieżny commit/blob | Odczyt ma przerwać lub jednoznacznie zgłosić `HOLD`; brak cichego `NONE`, `VALIDITY` lub ignorowania rekordu jako pozornego PASS. |

**Granica implementacyjna:** istniejący `test_memory_map.py` jest skryptem kontrolnym, nie udokumentowanym produkcyjnym importerem wszystkich map. Node powinien wskazać faktyczną ścieżkę zwykłego zapytania i zakres integracji; same zmiany w testach lub lokalnej próbce nie stanowią wdrożenia. Realne wykonanie i zatwierdzenie należą do Node. M zajmuje się klasyfikacją semantyczną i redakcją, bez testu LAB. `CORE5/IFX = FREEZE`, `C1 = HOLD`.

### 6.11. Redukcja M-012 — jeden schemat pamięci zadaniowej i jego granice (24.10.2026)

**Stan redakcyjny:** SYNTHESIS / SELF_CHECKED / NON-CORE / INDEPENDENT_REVIEW_NOT_REQUESTED. Niniejsza sekcja zastępuje w *aktywnej Mapie* osiem opisów historycznych §6.11–6.18, lecz **nie zmienia dowodów, ich statusów ani rdzenia PSI**. Pełne pierwotne rozwinięcia, kontrprzykłady i sformułowania są dostępne [w niezmiennej wersji Mapy przed redukcją](https://github.com/smoczynski-b/PSI/blob/2ce841828892ec8f6cc563e82efaa2c7f0d70c7d/docs/memory/PSI-MEMORY-MAP-01.md) oraz w historii Git. To **archiwum dowodów**, nie osobna obowiązkowa pamięć robocza.

#### A. Twierdzenie nadrzędne — II.7–II.9, bez nowego prymitywu

Dla ustalonego kontraktu `c` niech `H_c` będzie przestrzenią legalnych historii, `Beh_c(h)` ich drzewem przyszłości z literalnymi etykietami legalnych kroków i obserwacji, a `h≈_c h'` oznacza izomorfizm tych drzew **w semantyce zadeklarowanej przez c**. Wtedy:

\[
\boxed{\text{dokładność pamięci }\rho:H_c\to Z
\iff \ker_{\rm eq}\rho\subseteq\approx_c.}
\]

Iloraz `H_c/≈_c` jest najgrubszy informacyjnie dokładny (II.7–II.8). Jeżeli chcemy aktualizować **sam kod** `ρ`, a nie wyłącznie obliczać z niego klasę zadaniową, konieczna i wystarczająca jest dodatkowo kongruencja: stany o równym kodzie muszą mieć te same legalne etykiety oraz równy kod następcy po każdej wspólnej legalnej etykiecie (w wersji deterministycznej). To jest warunek II.9 dla zejścia dynamiki na obraz kodu; **sama dokładność zadaniowa nie dowodzi aktualizowalności wybranego `ρ`**.

Poniższe punkty B–F są *kontraktowymi specjalizacjami* tego schematu, a nie samodzielnymi podstawami rdzenia.

#### B. Jedna konstrukcja dla usuwanych, oznaczonych certyfikatów (dawne §6.11, §6.14–6.16)

Niech `K` będzie skończonym zbiorem aktywnych **oznaczonych** ograniczeń równości/nierówności, `A|_K` ich treścią, a `Cons` boolowskim wynikiem spełnialności przy **nieograniczonej** liczbie grup. Skreślenie ograniczeń może przywrócić spójność, lecz nie może jej zniszczyć. Stan sterowania `s` zawiera wszystkie dane wymagane do rozpoznania legalności (w szczególności stan automatu i aktywne nazwy `K`). Niech `𝓡_s` oznacza rodzinę zbiorów nazw możliwych do wycofania za pomocą **jakiegokolwiek** legalnego przyszłego słowa od `s`; nie zakładamy, że jest dziedziczna. Legalność i aktualizacja sterowania zależą od `s`, nie od nieujawnionej treści `A`. Jedyną obserwacją wynikową jest `Cons`.

Definiujemy *minimalne osiągalne naprawy*:

\[
\boxed{\mathcal T_s(A)=\operatorname{Min}_{\subseteq}
\{R\in\mathcal R_s:\operatorname{Cons}(A|_{K\setminus R})\}.}
\]

Dla **każdego osiągalnego** `R∈𝓡_s`:

\[
\boxed{\operatorname{Cons}(A|_{K\setminus R})
\iff \exists T\in\mathcal T_s(A):T\subseteq R.}
\tag{B1}
\]

**Dowód bez ukrytej dziedziczności:** z `T⊆R` i monotoniczności spełnialności mamy kierunek „jeśli”. Jeśli `R` jest osiągalną naprawą, to skończony niepusty zbiór osiągalnych napraw zawartych w `R` ma element minimalny; jest on minimalny również w całej rodzinie osiągalnych napraw. Nie trzeba zakładać, że *każdy* podzbiór `R` jest osiągalny.

Dla dwóch katalogów z identycznym `s,K` i tym samym automatem niezależnym od treści:

\[
\boxed{\operatorname{Beh}_s(A)\cong\operatorname{Beh}_s(B)
\iff \mathcal T_s(A)=\mathcal T_s(B).}
\tag{B2}
\]

Konieczność: każde `R∈𝓡_s` jest wynikiem pewnego literalnie legalnego słowa, więc równość drzew określa jednakowe odpowiedzi `Cons` i jednakowe minimalne osiągalne naprawy. Dostateczność: legalne słowa są wspólne, a (B1) określa wszystkie ich etykiety. **To jest jawna postać najgrubszego ilorazu treści katalogu, lecz tylko przy ustalonych `s,K` i kontrakcie.**

Jeżeli legalny krok `e:s→s'` wycofuje `Δ_e⊆K`, mamy **jeden wzór aktualizacji**, obejmujący także strażniki zależne od wcześniejszych wycofań:

\[
\boxed{\mathcal T_{s'}=
\operatorname{Min}_{\subseteq}
\{R'\in\mathcal R_{s'}:
\exists T\in\mathcal T_s,\ T\subseteq\Delta_e\cup R'\}.}
\tag{B3}
\]

Wywód: legalny prefiks `e` z przyszłą kontynuacją `R'` realizuje łącznie `Δ_e∪R'`, więc (B1) określa jego spójność; minimalizacja po `𝓡_{s'}` daje następną rodzinę. Wzór jest dobrze określony, jeżeli `s` rzeczywiście zawiera historię istotną dla legalności; nie dowodzi taniej implementacji.

**Świadek strażnika:** redundantne `a:(x=x)`, konflikt `b:(x≠y),λ:(x=y)`. Wolno wykonać `−a`, a dopiero potem `−b`. Rodzina `𝓡_s={∅,{a},{a,b}}` nie jest dziedziczna, choć jedyna minimalna osiągalna naprawa to `{{a,b}}`. Warunek osiągalności jest **operacyjny**, nie logiczny.

#### C. Projekcja, prawa, koszty i przełączenia — przypadki B, nie nowe twierdzenia podstawowe

W szczególnym kontrakcie dowolnych nazwanych usunięć z ustalonego `D⊆K` osiągalność wynosi `𝓡_s=2^D`. Niech `𝓜(A)` będzie pełną rodziną minimalnych konfliktów. Z MATH-70–72:

\[
\mathcal F_D=\operatorname{Min}_{\subseteq}\{C\cap D:C\in\mathcal M(A)\},
\qquad
\mathcal T_D=\operatorname{Min}\{R\subseteq D:\forall F\in\mathcal F_D,\ R\cap F\ne\varnothing\}.
\]

`𝓕_D` to *minimalne przeszkody*, a `𝓣_D` to *minimalne naprawy*. Są wzajemnie wyznaczane przez blocker (dualność rodzin minimalnych transwersali na skończonym D), **ale nie należy ich utożsamiać**. `𝓕_D=∅` oznacza brak konfliktów; `𝓕_D={∅}` oznacza konflikt nietrafialny legalnym usunięciem. Odpowiednio `𝓣_D={∅}` oraz `𝓣_D=∅`.

**Ograniczenie praw** z D do E⊆D ma postać `P_E(𝓕_D)=Min{F∩E:F∈𝓕_D}`; projekcje składają się: `P_K P_E=P_K` przy K⊆E⊆D. Przy rzeczywistym `−j` pozostają tylko przeszkody `F` niezawierające j; przy **samym zakazie przyszłego `−j`** projektujemy przeszkody przez `F↦F\setminus{j}`. Rozróżnienie tych dwóch działań jest istotne. Rozszerzenie praw **nie** jest w ogólności odwracalne z samej `𝓕_D`: zmiana kontraktu może odtworzyć wcześniej sklejone różnice.

Dla jawnych dodatnich wag `w_j`, minimalny koszt naprawy spełnia elementarną rekurencję ważonego trafiania:

\[
\beta(D,\mathcal F)=
\min\big\{
\beta(D\setminus\{j\},\operatorname{Min}\{F\setminus\{j\}:F\in\mathcal F\}),
\ \ w_j+\beta(D\setminus\{j\},\{F\in\mathcal F:j\notin F\})
\big\}.
\]

To podział na gałąź „nie usuń j” i „usuń j”; **nie** dowodzi wielomianowej złożoności.

Dla kilku reżimów `D_i`: osobne sesje o stałym i identyfikuje krotka `(𝓕_{D_i})_i`, lecz przy **swobodnym przełączaniu w jednej trajektorii** potrzebna jest `𝓕_H` dla `H=⋃D_i`. Przy najwyżej r przełączeniach i dowolnym wyborze pierwszego reżimu zbiór R jest osiągalny dokładnie wtedy, gdy można go pokryć co najwyżej r+1 zbiorami `D_i`. Najmniejsza liczba przełączeń potrzebnych do naprawy katalogu to liczba wybranych reżimów trafiających wszystkie minimalne przeszkody **minus jeden** (przy wyjątkach: stan już spójny = 0, niemożliwa naprawa = ∞). Przy skierowanych, ograniczonych przełączeniach trzeba wyznaczać legalne spacery sterowania; przy strażnikach zależnych od wycofań obowiązuje ogólna `𝓡_s` z B. Żadne z tych ograniczeń nie wymaga nowej definicji dokładności pamięci.

#### D. Granica — legalność zależna od treści (dawne §6.17)

Gdy legalność ruchu zależy od samego `A`, założenie o wspólnym drzewie legalnych słów w (B2) przestaje obowiązywać. Przykład: katalog `A={λ:(x=x)}` i `B={λ:(x=y)}` są spójne, a bez usunięć mają to samo `𝓣={∅}`, lecz ruch dopuszczany wyłącznie dla nietrywialnej równości może być legalny tylko w B.

Przy skończonej **jawnej przestrzeni stanów** S, obserwacji o(s), legalnych etykietach En(s) i deterministycznej, częściowej aktualizacji δ(s,e) pełną dokładność daje zwykła rafinacja:

\[
R_0=\{(s,t):o(s)=o(t)\},
\]

\[
sR_{n+1}t\iff o(s)=o(t)\land
\operatorname{En}(s)=\operatorname{En}(t)\land
\forall e\in\operatorname{En}(s)\ 
\delta(s,e)R_n\delta(t,e).
\]

Relacje stabilizują się po co najwyżej `|S|−1` ścisłych uszczegółowieniach, a stabilna równoważność odpowiada izomorfizmowi literalnie etykietowanych drzew przyszłości. Przy wybranym kodzie η:S→Z **jego własna aktualizacja** wymaga dodatkowo zgodności kodów następników dla każdej pary z równym kodem (II.9). To jest granica B, a nie niezależny prymityw pamięci.

#### E. Granica — niedeterminizm i semantyka rozgałęzień (dawne §6.18)

Jeżeli po jednej etykiecie mogą istnieć liczne różne następniki, trzeba wybrać poziom informacji wymagany przez zadanie:

\[
\boxed{\text{izomorfizm pełnych drzew realizacji}
\ \Longrightarrow\ \text{bisymulacja}
\ \Longrightarrow\ \text{równość możliwych śladów}.}
\]

Odwrotności nie zachodzą ogólnie. Śladami zgodne są: dwaj następnicy po `a`, dopuszczający osobno tylko `b` i tylko `c`, oraz jeden następnik po `a` dopuszczający oba `b,c`; nie są bisymilarne. Z kolei dwa terminalne następniki po `a` mogą być bisymilarne jednemu, lecz nie tworzą izomorficznych pełnych drzew zachowujących liczność gałęzi.

Dla skończonego systemu niedeterministycznego `Γ(s,e)⊆S` największą bisymulację daje stabilizacja dwustronnego dopasowania następników (po najwyżej `|S|−1` ścisłych uszczegółowieniach); iloraz ma **relację**, a nie funkcję aktualizacji:

\[
\overline\Gamma([s],e)=\{[u]:u\in\Gamma(s,e)\}.
\]

Nie jest ona automatycznie dokładna dla pełnego izomorfizmu drzew, który zachowuje odrębność gałęzi. Zachowanie śladów, zachowanie możliwości rozgałęzień i zachowanie wielokrotności fizycznych realizacji to **różne kontrakty**, którym odpowiadają różne ilorazy. Wersja probabilistyczna wymaga kolejnego jawnego wyboru znaczenia rozkładu wyników; nie została tu udowodniona.

#### F. Decyzja redukcyjna — co pozostaje aktywne, co nie

| Zakres dawny | Status po redukcji | Gdzie pełne uzasadnienie |
|---|---|---|
| §6.11–6.12: stałe prawa, projekcja, koszty | **PRZYPADEK C** | [Wyniki M-012](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383746530), [rekurencja kosztu](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383815322) |
| §6.13–6.14: przełączanie i budżet | **PRZYPADEK C** | [Świadek przełączania](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383874210), [pełna wersja Mapy](https://github.com/smoczynski-b/PSI/blob/2ce841828892ec8f6cc563e82efaa2c7f0d70c7d/docs/memory/PSI-MEMORY-MAP-01.md) |
| §6.15–6.16: skierowane przejścia i strażniki | **SCHEMAT B** | [Pełne pierwotne dowody](https://github.com/smoczynski-b/PSI/blob/2ce841828892ec8f6cc563e82efaa2c7f0d70c7d/docs/memory/PSI-MEMORY-MAP-01.md), [Issue #13](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6384243682) |
| §6.17: zależność od treści | **GRANICA D** | [Pierwotny dowód](https://github.com/smoczynski-b/PSI/blob/2ce841828892ec8f6cc563e82efaa2c7f0d70c7d/docs/memory/PSI-MEMORY-MAP-01.md), [Issue #13](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6384307698) |
| §6.18: niedeterminizm | **GRANICA E** | [Pierwotny dowód](https://github.com/smoczynski-b/PSI/blob/2ce841828892ec8f6cc563e82efaa2c7f0d70c7d/docs/memory/PSI-MEMORY-MAP-01.md), [Issue #13](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6384356729) |

**Wyłączenia niezmienne:** §6.9 (źródłowa migracja i aktywna errata MATH-57), §6.10 (kontrakt importu i ograniczenia prób Node), statusy E-001, niepropagujące typowanie INDEX/EDITORIAL/SCOPE/EVIDENCE. Głosowanie nad prawdziwością dowodu przez liczbę pochodnych zapisów jest niedozwolone: przekształcenia i streszczenia **nie stanowią niezależnych świadectw**. Celem redukcji jest zmniejszenie kosztu aktywnej pamięci, nie ogłoszenie nowych twierdzeń ani rezygnacja ze źródeł. `CORE5/IFX=FREEZE`, `C1=HOLD`, `NODE/SOL/LUNA_NEW_TESTS=HOLD_BY_OWNER_BUDGET`.
