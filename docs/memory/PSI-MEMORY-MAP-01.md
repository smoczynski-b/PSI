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

\`\`\`text
MATH-N = źródło historycznego zadania/argumentu
  | INDEXES / SOURCE_OF
  v
Mapa migracji Principiów -> Tom II (hipotezy i dowody), Tom III (świadki), Tom IV (genealogia)
  ^
  | OVERLAP_TO_AUDIT / FINITE_REALIZATION_CANDIDATE / SCOPE_EXTENSION_CANDIDATE
  |
Wcześniejsze jednostki II.4, II.6–II.12 (już napisane)
\`\`\`

**Zwrot i typ krawędzi są ważne:** zapis \`MATH76-T26-T27 --FINITE_REALIZATION_CANDIDATE--> II.8\` oznacza obowiązek porównania z wcześniejszym twierdzeniem, **nie** jego logiczną przesłankę ani potwierdzoną tożsamość. Nawet gdy istnieje wspólny wzór, zmiana alfabetu, dziedziny legalności lub etykiet terminalnych może zmienić twierdzenie. \`INDEXES\` nie jest \`PROVES\`.

### 6.2. Mapa merytoryczna w skrócie

| Strumień | Skojarzenie w starszej mapie | Ocena |
|---|---|---|
| MATH-28–40 | Tom II, podpory i ważone wycofanie świadectw | brak automatycznego przypisania do dawnego II.x |
| MATH-41–56 | II.9 jako pokrewny problem aktualizacji/pamięci | \`TOPIC_BRIDGE_CANDIDATE\`; brak dowodu równoważności |
| MATH-57–69 | II.4: adekwatność a źródłowość danych | \`TOPIC_BRIDGE_CANDIDATE\`, wymagane sprawdzenie errat |
| MATH-70–75 | Tom II, konflikty oznaczonych katalogów | \`CANDIDATE_SECTION_COMPLETE\` według MATH-75, nie automatycznie \`CANON\` |
| MATH-76/T1–T4 | II.7–II.8: pamięć historii | odróżnić przyczynowe przypisanie korekty od wystarczalności reprezentacji |
| MATH-76/T5–T21 | II.4: eksperymenty, odporność, koszty | osobne kontrakty błędów, adaptacji i kosztu |
| MATH-76/T22–T25 | II.6/II.9: dynamika/rekurencja | q historyczne nie jest bieżącym q po interwencji |
| MATH-76/T26–T27 | II.8/II.9/II.11/II.12 | możliwa redukcja do znanej klasyki; II.12 to benchmark, nie to samo co zwykły refinament |
| MATH-76/T28–T29 | II.8/II.9 | polityka z optymalnym kosztem zachowuje mniej operacji niż pełna kongruencja |
| MATH-76/T30–T34 | II.6/II.9 | legalność epistemiczna i wiele celów; nie utożsamiać z dawną częściowością II.9 |

**Konkretny priorytet:** MATH-76/T26–T27 [źródło](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377888676) sprawdzić kontra gotowe [II.8](../principia-v2-08-coarsest-exact-history-quotient.md), [II.9](../principia-v2-09-recursive-history-quotient-update.md), [II.11](../principia-v2-11-myhill-nerode-bridge.md) i [II.12](../principia-v2-12-paige-tarjan-benchmark.md) przed pisaniem kolejnego rozdziału. MATH-76/T28–T34 wymagają niezależnego audytu; [errata K14](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377898833) ogranicza twierdzenie o czterech kodach do jawnej rodziny punktów wznowienia.

### 6.3. Źródła bieżące i zachowanie granic

Pełny historyczny rejestr: [psi-model Issue #13](https://github.com/smoczynski-b/psi-model/issues/13). Wersjonowany indeks: [MATH76_SHARED_INDEX](https://github.com/smoczynski-b/psi-model/blob/5d41732861f02fd65f20e93ab7b824be14196502/psi-agent/handoff/MATH76_SHARED_INDEX_20261024.md). Zapis przeznaczenia: [PRINCIPIA_MIGRATION_01 §6](https://github.com/smoczynski-b/psi-model/blob/e1de79e7ffd6a72186f4dcfee287a8beaafc09ee/psi-agent/PRINCIPIA_MIGRATION_01.md).

Przed rozpoczęciem nowego dowodu należy odczytać związane węzły, sprawdzić \`TYP / DZIEDZINA / ZAŁOŻENIA / ZAKRES / ERRATA\`, następnie sklasyfikować: \`REUSE / ADAPT_CONTRACT / REAL_GAP / CONTRADICTION\`. Tylko ostatnie trzy przypadki mogą uzasadniać nowe rozumowanie, a nowy numer MATH nie stanowi automatycznie jednostki monografii.

**Niepotwierdzone:** pełna jednostkowa migracja wszystkich T z MATH-28–75; MATH-1–27; rzeczywiste zastosowanie mapy przez wszystkie żywe role. To mapa strukturalna **kandydacka**, nie zakończona recenzja matematyczna ani wdrożenie pamięci produkcyjnej. Brak nowego CORE5, IFX, gałęzi lub kosztownej sesji E/Sol.


### 6.4. Rozdzielenie odbiorów i wykonania — korekta 24.10.2026

Nakładka rozróżnia teraz węzły `MATH-70-74` i `MATH-75`. Pierwszy wskazuje [odbiór E-001](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353594375): dowody i przykłady, bez ponownej enumeracji. Drugi wskazuje własny wynik samokontroli MATH-75 i kandydackiego domknięcia redakcyjnego. Statusów tych nie wolno scalać ani przenosić z całego zakresu na pojedyncze twierdzenie.

Bieżącą orientację Tomu II zapewnia [theorem-map-v2.md](../theorem-map-v2.md), z odsyłaczami do mapy 04, audytu całego tomu i erraty. Mapa 01 pozostaje wcześniejszym planem. Dla odtwarzalnego porównania należy przypiąć commit i zakres obu źródeł.

Na polecenie właściciela wyłącznie Node przeprowadza realne próby działania mapy i całego środowiska LAB. M opracowuje porównanie matematyczne, zakres odwzorowania i kryteria odbioru; odczyt Git nie jest wykonaniem w środowisku. Commander ma ograniczony budżet wywołań i służy doraźnej obsłudze; przyszłe odnowienie dostępu nie jest warunkiem pracy M ani podstawą ciągłości wykonania. Obecna nakładka pozostaje kandydacka i nie zostaje automatycznie dołączona do produkcyjnej propagacji statusów.

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

**Rozdzielenie środowiska:** [Node LAB #15 / 6383074872](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383074872) odczytał poprawnie dawne źródła, lecz w istniejącym programie nie wczytał nakładki MATH; jej kolumny nie dostarczają pola `effect` do starego algorytmu propagacji, co dało `KeyError`. **Integracja grafu źródeł = PARTIAL wykonawczo**, bez świadectwa działania nowej nawigacji i blokady propagowania kandydatów. Naprawa adaptera i próba na LAB należą do Node, nie do M.

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

**Sfera źródłowa / statusy:** MATH-41–56 = `SELF_CHECKED / INDEPENDENT_REVIEW_PENDING`; nie przypisywać im odbiorów E-001 dotyczących MATH-28–30 lub MATH-69. Rezultaty są klasyfikowane jako `REUSE / ADAPT_CONTRACT / BRIDGE_CANDIDATE`; nie przedstawiać uogólnień klasycznego hipergrafowego trafiania jako już dowiedzionej nowości naukowej PSI. Dane TSV to warstwa orientacji, nie wdrożona pamięć agentów. Ostatnia znana próba Node wykazała brak adaptera i `KeyError: effect` dla nakładki; Node obsługuje próby środowiskowe, M — audyt matematyczny. CORE5/IFX bez zmian. MATH-1–27 oraz MATH-70–75 nie mają jeszcze analogicznej pełnej jednostkowej integracji (MATH-57–69: zob. §6.9).

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

**Statusy i program wykonawczy:** MATH-57–68 `SELF_CHECKED/REVIEW_PENDING`; MATH-69 `E001_ACCEPTED_PROOF_SCOPED_ENUM_NOT_RERUN`. Węzły i relacje w `psi-memory-{nodes,edges}-math-migration-20261024.tsv` należą do warstwy orientacyjnej `EDITORIAL/SCOPE/INDEX`, bez produkcyjnej propagacji. Według [ostatniego pokwitowania Node](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383074872) nakładka MATH **nie była wczytywana**, a `stale_closure` dla jej surowych krawędzi zwróciło `KeyError: 'effect'`. Żaden `PASS` starych programów nie certyfikuje nowej integracji; jej rzeczywistą próbę wykonuje tylko Node. Brak nowych twierdzeń CORE5 lub roszczeń pierwszeństwa w literaturze.

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

### 6.11. Ograniczone prawa wycofania — najgrubszy iloraz i dwa operatory (24.10.2026)

**Wynik redakcyjny M, nieodbierany dziś przez E:** [pełny dowód i dwa kontrprzykłady](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383746530), oparty na [MATH-70](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353258865), [MATH-71](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353300614), [MATH-72](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353389796), [MATH-73](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353429618), a także II.7–II.9 @`b4c21748`. **Status:** `DERIVED / SELF_CHECKED / INDEPENDENT_REVIEW_NOT_REQUESTED`; odrębny odbiór E-001 dla MATH-70–74 pozostaje ważny wyłącznie w swoim zakresie.

Niech `L` będzie ustalonym katalogiem aktywnych oznaczonych certyfikatów równości/nierówności, `D⊆L` zbiorem **jedynych legalnie wycofywalnych identyfikatorów**, a `𝓜(L)` pełną rodziną minimalnych konfliktów. Przy wyniku obserwacyjnym ograniczonym do `Cons` i przyszłych czynnościach wyłącznie nazwanych usunięć `−j` dla `j∈D`, definiujemy:

\[
\boxed{\mathcal F_D(L)=\operatorname{Min}_{\subseteq}\{C\cap D:C\in\mathcal M(L)\}.}
\]

Dla każdego `R⊆D` mamy

\[
\operatorname{Cons}(L\setminus R)\iff
(\forall F\in\mathcal F_D(L))\quad R\cap F\ne\varnothing.
\]

Oznacza to dokładny iloraz przyszłych historii:

\[
\boxed{
\operatorname{Beh}_{D_A}(A)\cong\operatorname{Beh}_{D_B}(B)
\iff (D_A,\mathcal F_{D_A}(A))=(D_B,\mathcal F_{D_B}(B)).
}
\]

Konieczność wynika z odzyskania `D` po legalnych nazwach ruchów, a `𝓕_D` jako antyłańcucha minimalnych `S⊆D`, dla których pozostawienie dokładnie `S` spośród prawnie wycofywalnych ID daje konflikt. Dostateczność: wzór na `Cons` daje identyczne wyniki i legalne gałęzie po wszystkich sekwencjach. **Nie** jest to twierdzenie o minimalnej liczbie bitów ani o identyfikacji faktycznej proweniencji.

Dwa operatory muszą pozostać rozdzielone:

| Operacja | Aktualizacja reprezentacji `(D,𝓕)` | Znaczenie |
|---|---|---|
| Faktycznie usuń certyfikat `j∈D` | `(D\{j}, {F∈𝓕:j∉F})` | Ograniczenia konfliktowe zawierające usunięty wpis zostały trafione i znikają. |
| Odbierz tylko uprawnienie wycofania `j∈D` | `(D\{j}, Min{F\{j}:F∈𝓕})` | Certyfikat pozostaje; nieusuwalny wpis nie może już trafić konfliktu. |

**Rozstrzygający świadek:** niewycofywalna równość `λ:a=b`, wycofywalna nierówność `j:a≠b`, `D={j}`, `𝓕={{j}}`. Po fizycznym usunięciu j: `𝓕=∅` (brak konfliktów); po odebraniu prawa do `−j`: `𝓕={∅}` (konflikt nieusuwalny). **Pusta rodzina i rodzina zawierająca pustą podporę to dwa różne stany.**

**Ścisłe osłabienie pamięci MATH-72:** dla `D={ν}`, katalogi `A={λ:a=b, μ:b=c, ν:a≠c}` i `B={λ:a=c, μ:b=c, ν:a≠c}` mają odpowiednio `𝓜(A)={{λ,μ,ν}}`, `𝓜(B)={{λ,ν}}`, ale to samo `𝓕_D={{ν}}` i te same wszystkie legalne przyszłe odpowiedzi. Dla `D=L` odzyskujemy całe `𝓜`. Kosztowo optymalne naprawy można wyznaczać z `𝓕_D`, o ile osobno zadano koszty i legalność (MATH-71); nie wolno wnioskować wag ani grup pochodzenia z samej rodziny konfliktów.

**Granice:** dodawanie nowych certyfikatów, zwiększanie praw do usuwania, odtwarzanie znaczników `Used`, pełna historia lub empiryczne dane o pochodzeniu zmieniają kontrakt; reprezentacja `(D,𝓕)` nie jest w tych zadaniach automatycznie dokładna. Jest to `PONOWNE_UŻYCIE` II.7–II.9 przy ścisłej `ADAPTACJI_KONTRAKTU` MATH-70–72; żadnych nowych prymitywów ani `DEPENDS_ON` w produkcyjnym grafie.

**Zasoby:** wszystkie próby Node/LAB, sprawdziany Sol/E i dodatkowe angażowanie Luny pozostają `HOLD_BY_OWNER_BUDGET`; odroczony pakiet jest w [Issue #15](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383640277). Redakcyjny zapis nie jest uruchomieniem próby środowiskowej.

### 6.12. Projekcje uprawnień i koszt naprawy — semantyka dwóch gałęzi (24.10.2026)

**Wynik M, SELF_CHECKED, bez nowego MATH:** [pełny dowód, kontrprzykład i rekurencja](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383815322). Zależności źródłowe: [MATH-70](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353258865), [MATH-71](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353300614), [MATH-72](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353389796), wcześniejszy §6.11 i II.7–II.9. Nie przenosić statusu E-001 \`PASS_SCOPED\` dla MATH-70–74 na niniejszy wynik.

Ustalono skończony oznaczony katalog L, stałe deklaracje i nieograniczoną liczbę grup spełniania. W kontrakcie zadania obserwujemy tylko \`Cons\`; legalne są nazwane usunięcia spośród \`D⊆L\`. Reprezentacja dokładna z §6.11:

\[
\mathcal F_D=\operatorname{Min}_{\subseteq}\{C\cap D:C\in\mathcal M(L)\}.
\]

**Składanie utraty uprawnień:** dla \`K⊆E⊆D\` i \`P_E(\mathcal F)=Min\{F\cap E:F\in\mathcal F\}\`:

\[
\boxed{P_K(P_E(\mathcal F_D))=P_K(\mathcal F_D).}
\]

Zawężenie praw do E, a następnie do K nie wymaga pamięci o wyciętych elementach. Jest to dobrze określone zejście na iloraz przy malejącej legalnej dziedzinie przyszłości. **Rozszerzenie praw nie ma ogólnie odwrotnego operatora.** Świadek: L={λ,μ,ν}, D={ν}, V={a,b,c}; A={λ:a=b, μ:b=c, ν:a≠c}, B={λ:a=c, μ:b=c, ν:a≠c}. Obie rodziny \`F_D={{ν}}\`, ale po dopuszczeniu wycofania μ, dla \`E={μ,ν}\` zachodzi \`F_E(A)={{μ,ν}}\` i \`F_E(B)={{ν}}\`. Usunięcie μ naprawia A, lecz nie naprawia B. Samo \`F_D\` utraciło potrzebne rozróżnienie.

**Koszt naprawy** wymaga osobno określonych \`w_j>0\`. Dla \`j∈D\`:

\[
\boxed{
\beta_w(D,\mathcal F)=\min\left\{
\beta_w(D\setminus\{j\},\operatorname{Min}\{F\setminus\{j\}:F\in\mathcal F\}),
\quad
w_j+\beta_w(D\setminus\{j\},\{F\in\mathcal F:j\notin F\})
\right\}.
}
\]

Pierwsza gałąź **zabrania wycofania** j, ale nie usuwa certyfikatu; druga **wykonuje wycofanie** za cenę \`w_j\`. Podział napraw na \`j∈R\` i \`j∉R\` dowodzi równości. Przy \`F=∅\`, \`β=0\`; przy \`F={∅}\`, \`β=+∞\`. Dla \`E⊆D\` zachodzi \`β_w(E,P_E F_D)≥β_w(D,F_D)\`, pod warunkiem identycznych kosztów i treści katalogu. Nie jest to twierdzenie o obliczeniach wielomianowych, adaptacyjnym minimaksie ani identyfikacji rzeczywistych źródeł.

**Granica architektury pamięci:** dla znanej górnej granicy przyszłych praw \`H\` wystarczy zachować \`(H,F_H)\`, aby obsługiwać późniejsze zawężenia. Jeżeli prawa mogą wzrosnąć poza H lub zmieniać się wraz z fizyczną dynamiką, konieczne są dodatkowe dane lub nowa przestrzeń historii. Nie dopisywać relacji produkcyjnych \`DEPENDS_ON\`, nie promować redakcyjnego dowodu do statusu E-001.

**Reżim wykonawczy:** \`DERIVED / SELF_CHECKED / INDEPENDENT_REVIEW_NOT_REQUESTED\`; Node/LAB, Luna i Sol nie wykonują nowych prób na podstawie tej notatki. Pakiet testów Mapy pozostaje odroczony w [Issue #15](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383640277). CORE5/IFX = FREEZE, C1 = HOLD.

### 6.13. Przełączane prawa wycofania — osobne zadania ≠ wspólna trajektoria (24.10.2026)

**Nowy wynik analityczny bez recenzji zewnętrznej:** [M-012 / Issue #13 / 6383874210](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6383874210). Podstawa: [MATH-70](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353258865), [MATH-72](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353389796), [MATH-76/T31](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377942281) i II.7–II.9 @`b4c21748`.

Ustalamy wspólny zbiór aktywnych znaczników `L`, skończony katalog równości/nierówności (nieograniczona liczba grup) i etykietę wyjścia `Cons`. Reżim `i` dopuszcza nazwane usunięcia `D_i⊆L`. Działania nie zmieniają nic poza usunięciem wpisu, a przełączanie uprawnień jest dowolne, nieodpłatne i dostępne przed każdym krokiem. Nie ma dopisywania ani historycznej legalności ponownego użycia ID.

**Dwa kontrakty:** przy stałym `i` przez cały epizod wspólna dokładność obserwacyjna wielu osobnych zadań odpowiada krotce `(𝓕_{D_i})_i`; gdy wolno przełączać zadania w jednej historii, niezbędny i wystarczający jest iloraz zadany przez `𝓕_H` przy `H=⋃_i D_i`. Każdą rodzinę usunięć `R⊆H` można zrealizować, wybierając w kolejnych krokach reżimy dopuszczające poszczególne `j∈R`. Zgodność `Cons(L\\R)` dla wszystkich `R` jest równoważna równości antyłańcuchów `𝓕_H` (MATH-72 i II.7–II.8). To wymaga dokładnie opisanej swobody przełączania; nie wynika z samej unii praw w kontrakcie z ograniczeniem liczby przełączeń.

**Kontrprzykład w dwuelementowej przestrzeni etykiet:** `V={x,y}, L={a,b,c}, D1={a,b}, D2={b,c}`. Katalog `A: a=(x=y), b=(x≠y), c=(x=y)`; `B: a=(x=y), b=(x≠x), c=(x=y)`. Pełne konflikty `𝓜(A)={{a,b},{b,c}}`, `𝓜(B)={{b}}`. Obie projekcje do `D1` i `D2` dają `{{b}}`, więc zadania osobne są nierozróżnialne. Jednak sekwencja `(D1,-a)`, potem `(D2,-c)` pozostawia w `A` spójne `x≠y`, a w `B` sprzeczne `x≠x`.

**Bardziej wymagający warunek pamięci wspólnej:** nawet kod `ρ(A)=(𝓕_{D1}(A),𝓕_{D2}(A))`, wystarczający do odpowiedzi w każdym stałym reżimie osobno, **nie musi przyjmować jednoznacznej aktualizacji** `ρ(A\\{a})=U(ρ(A),D1,-a)`. W świadku po usunięciu `a` drugi składnik kodu wynosi `{{b,c}}` dla A i `{{b}}` dla B, mimo równego wejściowego kodu. Jest to wystawienie na próbę kongruencji aktualizacji z II.9 i MATH-76/T31-M3, **nie** nowa produkcyjna krawędź `DEPENDS_ON`.

**Wniosek redakcyjny:** rozdzielić zadania zewnętrznie wybierane raz na epizod od przełączania po interwencjach. Nie utożsamiać łącznej wystarczalności informacji w punkcie początkowym z aktualizowalną pamięcią wspólnego agenta. Status niniejszego argumentu `DERIVED/SELF_CHECKED/INDEPENDENT_REVIEW_NOT_REQUESTED`; bez nowych prób Node/LAB, obciążania Luny lub zamawiania Sola. Pakiet testów mapy `HOLD_BY_OWNER_BUDGET` ([#15](https://github.com/smoczynski-b/psi-model/issues/15#issuecomment-6383640277)). CORE5/IFX FREEZE, C1 HOLD.

### 6.14. Budżet przełączeń — dokładna pamięć i próg naprawy (24.10.2026)

**Status:** DERIVED / SELF_CHECKED, bez nowego numeru MATH. Podstawy: MATH-70 (Issue #13/6353258865), MATH-71 (6353300614), MATH-72 (6353389796), MATH-76/T31 (6377942281), II.7–II.9 oraz wcześniejszy §6.13.

**Kontrakt.** Porównujemy skończone katalogi oznaczonych równości i nierówności na wspólnym zbiorze aktywnych znaczników L. Wynikiem obserwacji jest tylko logiczna spójność Cons. Reżim i pozwala usuwać aktywne znaczniki ze zbioru D_i⊆L; żadne inne skutki ani dodawanie nie występują. Pierwszy reżim wybieramy dowolnie i bez kosztu; każda późniejsza zmiana reżimu to jedno przełączenie. W jednym reżimie wolno usunąć wiele znaczników. Niech H=unia zbiorów D_i, a κ(R) oznacza najmniejszą liczbę reżimów, których zbiory uprawnień pokrywają R⊆H; κ(∅)=0.

**T1 — osiągalność.** Zbiór R⊆H można wycofać przy najwyżej r przełączeniach wtedy i tylko wtedy, gdy κ(R)≤r+1. Konieczność: taka historia odwiedza najwyżej r+1 różnych reżimów. Dostateczność: przydzielamy każdy j∈R do jednego z κ(R) reżimów pokrywających R i wykonujemy ich wycofania blokami, przy najwyżej κ(R)−1 przełączeniach. Rodzina osiągalnych zbiorów Reach_r jest dziedziczna względem inkluzji.

**T2 — dokładna pamięć.** Niech T_r(A) będzie rodziną minimalnych inkluzyjnie zbiorów R∈Reach_r, dla których katalog A po usunięciu R jest spójny. Dla dowolnego R∈Reach_r:

\[
\operatorname{Cons}(A\setminus R)\iff
\exists T\in\mathcal T_r(A)\quad T\subseteq R.
\]

Dowód: spójność jest monotoniczna względem usuwania ograniczeń, a Reach_r zamknięta na podzbiory. Przy wspólnym L i identycznych D_i dwa katalogi mają izomorficzne drzewa przyszłych nazwanych działań i wyników Cons przy budżecie r wtedy i tylko wtedy, gdy ich rodziny T_r są równe. Każde R∈Reach_r ma legalną historię, więc równość drzew wyznacza wszystkie Cons i minimalne naprawy; odwrotnie wzór wyznacza odpowiedzi po każdej historii. T_r=∅ oznacza brak osiągalnej naprawy, natomiast T_r={∅} — spójność bez działań. Jest to iloraz zadaniowy II.7–II.8, nie minimum liczby bitów.

**T3 — dokładny próg przełączeń.** Z pełnej rodziny minimalnych konfliktów M(A) bierzemy F_H(A)=Min{C∩H:C∈M(A)}. Dla F∈F_H niech I(F)={i:D_i∩F≠∅}. Oznaczmy przez τ minimalną liczbę reżimów J, które łącznie trafiają każdy konflikt F, tj. dla każdego F istnieje i∈J z D_i∩F≠∅. Wówczas minimalna liczba przełączeń umożliwiająca spójność wynosi 0, jeżeli F_H=∅; τ−1, gdy 1≤τ<∞; oraz ∞, gdy F_H zawiera ∅. Dowód: każdy skuteczny zestaw wycofań wymaga odwiedzenia co najmniej τ reżimów; odwrotnie wystarczy usunąć wszystkie oznaczenia należące do unii dowolnych τ reżimów trafiających każdy konflikt. Jest to redukcja do problemu trafiania, bez twierdzenia o łatwej złożoności.

**T4 — ścisła hierarchia.** Dla każdego n≥2 wybierzmy D_i={j_i}, i=1,...,n, oraz rozłączne pary etykiet x_i,y_i, i=0,...,n. Oba katalogi zawierają niewycofywalne równości e_i:(x_i=y_i) i wycofywalne nierówności j_i:(x_i≠y_i), i=1,...,n, oraz niewycofywalne e_0:(x_0=y_0). Kolejny niewycofywalny znacznik d oznacza w katalogu A równość x_0=y_0, natomiast w B nierówność x_0≠y_0. Przy najwyżej n−2 przełączeniach pozostaje co najmniej jeden konflikt (e_i,j_i) w obu katalogach, więc ich przyszłe wyniki Cons są identyczne. Przy n−1 przełączeniach można wycofać wszystkie j_i: A staje się spójny, B pozostaje sprzeczny. Każdy szczebel budżetu może więc ściśle zwiększać zdolność rozróżniania. Przykład nie wykorzystuje samosprzecznych pętli.

**Granice:** przy ustalonym reżimie początkowym, ograniczonej kolejności przełączeń, zależnościach historycznych albo efektach fizycznych Reach trzeba wyznaczyć z rzeczywistego kontraktu; samo κ nie wystarcza. Bez nowych prób Node/LAB i bez dodatkowych zadań Luny/Sola; pakiet prób Mapy pozostaje HOLD_BY_OWNER_BUDGET. CORE5/IFX FREEZE; C1 HOLD.

### 6.15. Automat legalnych przełączeń — osiągalność, iloraz i aktualizacja (24.10.2026)

**Status:** DERIVED / SELF_CHECKED / INDEPENDENT_REVIEW_NOT_REQUESTED; NON-CORE. To doprecyzowanie zakresu §6.14, a nie nowy MATH. Źródła: [MATH-70](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353258865), [MATH-71](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353300614), [MATH-72](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353389796), [MATH-76/T31](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377942281). Starsze twierdzenia: [II.7](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-07-exact-history-memory-adequacy.md), [II.8](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-08-coarsest-exact-history-quotient.md), [II.9](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-09-recursive-history-quotient-update.md), źródła @b4c21748.

**Kontrakt.** Rozważamy skończone katalogi oznaczonych równości i nierówności na ustalonym zbiorze aktywnych identyfikatorów K i zbiorze etykiet V. Liczba grup spełniania jest nieograniczona; obserwujemy wyłącznie Cons. Wspólny obu katalogom skończony automat sterowania ma stany Q, aktualny stan q, skierowane przejścia G oraz uprawnienia wycofania D(q) w stanie q. Stan może uwzględniać licznik pozostałych przełączeń. Przełączenie q→q' nie modyfikuje treści katalogu; legalne usunięcie −j wymaga j∈K∩D(q), usuwa tylko j i nie zmienia q. Przełączenia nie zależą od treści deklaracji ani od wykonanych usunięć. Wycofanie jest dobrowolne, zatem można opuścić stan bez korzystania z jego praw. Etykiety przełączeń i usunięć są literalne.

**T1 — dokładna osiągalność.** Dla skierowanego spaceru p=(q=q_0,...,q_k) w G piszemy H_K(p)=K∩(⋃ D(q_l)), z unią po wszystkich odwiedzonych stanach. Rodzina możliwych usunięć ma postać

\[
\boxed{\mathscr R_{q,K}=\{R\subseteq K:\exists p\text{ legalny spacer od }q,\ R\subseteq H_K(p)\}.}
\]

Dowód konieczności: każde skreślenie następuje w stanie uprawnionym do tej nazwy. Dowód dostateczności: każdą nazwę ze zbioru R przydzielamy do pierwszej wizyty w stanie uprawnionym i wykonujemy skreślenie podczas tej wizyty. Rodzina jest zamknięta na podzbiory. Uwaga: unia praw stanów osobno osiągalnych nie musi być realizowalna w jednej historii — mogą leżeć na wykluczających się gałęziach.

**T2 — dokładny iloraz treści przy ustalonym sterowaniu.** Minimalne osiągalne naprawy dla katalogu A definiujemy jako

\[
\boxed{\mathcal T_{q,K}(A)=\operatorname{Min}_{\subseteq}
\{R\in\mathscr R_{q,K}:\operatorname{Cons}(A|_{K\setminus R})\}.}
\]

Dla dowolnego R∈𝓡_{q,K}:

\[
\operatorname{Cons}(A|_{K\setminus R})\iff
\exists T\in\mathcal T_{q,K}(A)\quad T\subseteq R.
\]

Dostateczność wynika z monotoniczności spójności przy usuwaniu. Konieczność wynika z wyboru minimalnej osiągalnej naprawy zawartej w R. Dla dwóch katalogów A,B o wspólnych K,Q,q,G,D drzewa wszystkich legalnych słów oznaczonych literalnymi etykietami oraz etykietami węzłów Cons są izomorficzne wtedy i tylko wtedy, gdy 𝓣_{q,K}(A)=𝓣_{q,K}(B). Istotnie każdą R∈𝓡_{q,K} osiąga legalne słowo; zgodność drzew daje wszystkie etykiety Cons i rodzinę jej minimalnych napraw. W przeciwnym kierunku wszystkie legalne słowa są wspólne, a wzór wyznacza ich etykiety. Rodzina pusta oznacza brak osiągalnej naprawy, rodzina zawierająca pusty zbiór — spójność bez działań. Jest to dokładnie najgrubszy iloraz **treści katalogów przy ustalonym q,K**, nie globalny iloraz stanów o różnych prawach lub aktywnych nazwach. Nie oznacza minimum bitowego (II.7–II.8).

**T3 — jawna aktualizacja na ilorazie (II.9).** Przechowujemy (q,K,𝓣) oraz wspólny automat. Legalne działanie e prowadzi do (q',K') i usuwa w tym jednym kroku Δ_e (pusty zbiór dla przełączenia, singleton dla nazwanej operacji −j). Wtedy

\[
\boxed{\mathcal T'=\operatorname{Min}_{\subseteq}
\{R'\in\mathscr R_{q',K'}:
\exists T\in\mathcal T,\ T\subseteq\Delta_e\cup R'\}.}
\]

Dowód: e wraz z dowolną legalną kontynuacją usuwającą R' stanowi legalne słowo bieżącego automatu usuwające Δ_e∪R'. Według T2 wynik spójności jest dokładnie warunkiem istnienia T zawartego w tym zbiorze. Minimalizacja po osiągalnych kontynuacjach wyznacza rodzinę następnego stanu bez odwoływania się do treści A. Jest to **częściowy**, reprezentantowo niezależny operator; bez q i K sama rodzina 𝓣 może nie rozpoznawać legalności następnego ruchu. Nie wynikają z tego gwarancje tanich obliczeń.

**T4 — minimalny koszt przełączeń.** Pełna rodzina minimalnych konfliktów katalogu A niech będzie 𝓜(A). Skierowany spacer p od q *pokrywa konflikty* wtedy i tylko wtedy, gdy dla każdego C∈𝓜(A) zachodzi C∩H_K(p)≠∅. Istnieje legalna naprawa po najwyżej k przełączeniach wtedy i tylko wtedy, gdy istnieje taki spacer o najwyżej k krawędziach. W stronę konieczną każde rzeczywiste skreślenie leży w H_K(p), a naprawa trafia wszystkie minimalne konflikty. W stronę dostateczną można podczas wizyt po p usunąć wszystkie nazwy z H_K(p), trafiając wszystkie konflikty. Najmniejszy koszt jest więc długością najkrótszego *skierowanego spaceru pokrywającego konflikty*, nie liczbą nieuporządkowanych wybranych reżimów. Dopuszczamy wielokrotne wizyty w tym samym stanie. Przy jawnie danej 𝓜(A) odpowiada temu skończony problem najkrótszej ścieżki w iloczynie Q × 2^{𝓜(A)}, gdzie drugi czynnik rejestruje już trafione konflikty. Nie twierdzimy, że konstrukcja jest ekonomiczna ani wielomianowa.

**Kontrprzykład przeciw zastosowaniu §6.14 poza jego dziedziną.** Stan początkowy q0 ma dwie rozłączne gałęzie q0→q1 i q0→q2, bez możliwości powrotu lub przejścia między q1 i q2; D(q0)=∅, D(q1)={a}, D(q2)={b}. Można osobno wycofać a lub b, lecz nie obie nazwy w jednym epizodzie, niezależnie od budżetu. Katalog ma cztery wpisy: niewycofywalne e_a:(x1=y1), e_b:(x2=y2) oraz wycofywalne a:(x1≠y1), b:(x2≠y2), na rozłącznych parach etykiet. Ma dwa minimalne konflikty {e_a,a} i {e_b,b}. Nieuporządkowany zbiór reżimów {q1,q2} trafiałby oba konflikty; żadna legalna historia ich nie trafia. W tym automacie katalog jest nienaprawialny. Wzór pokrycia κ(R)≤r+1 z §6.14 wymagał swobodnej kolejności reżimów i tutaj nie obowiązuje.

**Granice:** przełączenia zależne od wcześniejszych wycofań, zewnętrzne koszty, zmiany praw w odpowiedzi na obserwację, odtwarzanie wpisu, interwencje fizyczne lub dodatkowe zadania wymagają powiększenia kontraktu; H_K(p) nie musi wtedy wyznaczać pełnej legalności. Nie podnosimy powiązań redakcyjnych do produkcyjnych DEPENDS_ON.

**Tryb kosztowy:** badanie wyłącznie matematyczne, Node/LAB i Sol/E pozostają HOLD_BY_OWNER_BUDGET, Luna nie otrzymuje nowych zleceń. CORE5/IFX FREEZE, C1 HOLD.

### 6.16. Strażniki zależne od wycofań — dokładny iloraz bez dziedziczności osiągalności (24.10.2026)

**Status:** `DERIVED / SELF_CHECKED / INDEPENDENT_REVIEW_NOT_REQUESTED`. Matematyczne rozszerzenie §6.15, bez nowego MATH i bez zmian CORE5. Podstawa: [MATH-70](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353258865), [MATH-72](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353389796), [MATH-76/T31](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377942281), [II.7](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-07-exact-history-memory-adequacy.md) i [II.9](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-09-recursive-history-quotient-update.md).

**Kontrakt.** I to skończony zbiór nazw certyfikatów, K⊆I zbiór aktualnie aktywnych nazw. Katalog A przypisuje każdej nazwie deklarację równości/nierówności na ustalonym skończonym V. Liczba grup jest nieograniczona, a jedynym wynikiem zadania jest boolowska wartość Cons(A|_K). Sterowanie ma skończony stan q i częściową deterministyczną aktualizację δ((q,K),e)=(q',K'), gdzie e jest literalnie nazwanym przełączeniem bez usunięcia albo wycofaniem −j, j∈K, po którym K'=K\{j}. Reguły dozwolenia przełączeń mogą zależeć od aktualnego K; automat i δ **nie zależą od treści deklaracji A**. Cała historia sterowania istotna dla legalności musi już być zawarta w q (np. licznik przełączeń, ostatni ruch). Bez takiego warunku q,K nie są dobrze określonym stanem Markowa.

Niech s=(q,K), a ℛ_s będzie rodziną R⊆K takich, że istnieje legalne słowo sterowania od s pozostawiające aktywny zbiór K\R. Rodzina ℛ_s **nie musi być dziedziczna**. Definiujemy

\[
\boxed{\mathcal T_s(A)=\operatorname{Min}_{\subseteq}\{R\in\mathscr R_s:
\operatorname{Cons}(A|_{K\setminus R})\}.}
\]

**T1 — dokładny test na nie-dziedzicznej rodzinie osiągalnej.** Dla każdego R∈ℛ_s:

\[
\boxed{\operatorname{Cons}(A|_{K\setminus R})\iff
\exists T\in\mathcal T_s(A)\quad T\subseteq R.}
\]

Dowód kierunku „jeśli”: monotoniczność spełnialności przy skreślaniu ograniczeń; jeżeli K\T jest spójny i T⊆R, to K\R też jest spójny. W drugą stronę: jeśli osiągalne R przywraca spójność, rodzina osiągalnych i skutecznych S⊆R jest **niepusta** (zawiera R), skończona, więc ma element minimalny T. Element taki jest minimalny globalnie wśród wszystkich osiągalnych i skutecznych wycofań, bo każdy skuteczny właściwy podzbiór T także byłby zawarty w R; zatem T∈𝓣_s(A). Dowód **nie zakłada**, że każdy podzbiór osiągalnego R jest osiągalny. Poprzednie odwołanie do dziedziczności ℛ w §6.15 dotyczyło tamtego węższego kontraktu.

**T2 — jądro najgrubszego dokładnego ilorazu.** Dla dwóch katalogów A,B o tym samym I,K,V oraz wspólnym s i tym samym automacie treściowo niezależnym:

\[
\boxed{\operatorname{Beh}_s(A)\cong\operatorname{Beh}_s(B)
\iff \mathcal T_s(A)=\mathcal T_s(B).}
\]

Izomorfizm drzew zachowuje korzeń, dosłowne nazwy kroków i etykiety węzłów Cons. Konieczność: każda osiągalna R ma co najmniej jedno legalne słowo; wspólna gramatyka sterowania i zgodność drzew wyznaczają odpowiedź Cons dla każdego R, a stąd jego minimalne osiągalne naprawy. Dostateczność: T1 wyznacza odpowiedź Cons po każdym legalnym słowie, zaś legalność i literalne krawędzie zależą wyłącznie od s i δ, wspólnych obu katalogom. Stąd izomorfizm drzew po identycznych słowach. Jest to specjalizacja II.7–II.8; minimalność jest **ilorazowa**, nie bitowa.

**T3 — aktualizacja ilorazowa (II.9).** Dla legalnego e:s→s'=(q',K') niech Δ=K\K' (puste dla przełączenia, singleton dla wycofania). Przy znajomości s,s',e,δ i bieżącego 𝓣_s(A):

\[
\boxed{\mathcal T_{s'}(A)=\operatorname{Min}_{\subseteq}
\{R'\in\mathscr R_{s'}:
\exists T\in\mathcal T_s(A),\ T\subseteq\Delta\cup R'\}.}
\]

Każde przyszłe R' po s' daje legalne słowo s→s'→... i łączne usunięcia Δ∪R' osiągalne z s. Z T1 mamy więc równość jego Cons z warunkiem po prawej. Minimalizacja po osiągalnych R' wyznacza dokładnie następne 𝓣. Dziedziczność ℛ_s nie jest potrzebna. Aktualizacja jest dobrze określona na klasach; legalność kroku wymaga jawnej kontroli s,e,δ. Nie przesądza to kosztu konstrukcji ℛ.

**Kontrprzykład — konieczność usunięcia logicznie zbędnego znacznika.** K={a,b,λ}. Deklaracje a:(x=x), b:(x≠y), λ:(x=y). W q0 jedynie −a jest dopuszczone. Przejście q0→q1 jest legalne dopiero gdy a∉K. W q1 dopuszczamy −b, a −λ nie jest dopuszczone nigdzie. Z q0 rodzina wycofań wynosi dokładnie

\[
\mathscr R=\{\varnothing,\{a\},\{a,b\}\}.
\]

W szczególności osiągalność nie jest dziedziczna: {a,b}∈ℛ, ale {b}∉ℛ. Minimalny konflikt samego katalogu to {λ,b}, natomiast minimalna osiągalna naprawa to {a,b}. Redundantny logicznie certyfikat a musi być wycofany, aby uruchomić reżim umożliwiający usunięcie b. Formuły §6.14 o nieuporządkowanym pokryciu reżimami i §6.15 o ścieżkach sterowania niezależnych od usunięć nie wolno tu stosować bez zmiany kontraktu.

**Dwie granice typu.** (1) Jeżeli stan q nie rejestruje historycznej przesłanki legalności, mogą istnieć dwie historie kończące z tym samym (q,K), lecz o różnych dozwolonych ruchach; wtedy δ nie jest funkcją na (q,K) i wymaga wzbogacenia q. (2) Jeśli uprawnienie zależy od **treści** deklaracji, a nie wyłącznie od q,K, dwa katalogi o tym samym 𝓣 mogą mieć inne legalne krawędzie i T2 przestaje być bezwarunkowo prawdziwe. W takim przypadku potrzebny jest bogatszy kontrakt albo pełny iloraz przyszłych literalnie etykietowanych drzew z II.7.

**Granica wykonawcza:** brak prób Node, Sol/E, Luny i LAB, brak nowego modułu i nowego numeru MATH. Źródłowe wyniki MATH-70–74 zachowują swoje ograniczone statusy niezależnego odbioru; §6.16 nie dziedziczy tych statusów. CORE5/IFX FREEZE, C1 HOLD, próby mapy HOLD_BY_OWNER_BUDGET.

### 6.17. Legalność i obserwacje zależne od treści — poprawka zakresu oraz skończony iloraz dokładny (24.10.2026)

**Źródła:** MATH-70 ([#13/6353258865](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353258865)), MATH-72 ([#13/6353389796](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6353389796)), MATH-76/T31 ([#13/6377942281](https://github.com/smoczynski-b/psi-model/issues/13#issuecomment-6377942281)), oraz starsze [II.7](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-07-exact-history-memory-adequacy.md), [II.8](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-08-coarsest-exact-history-quotient.md), [II.9](https://github.com/smoczynski-b/PSI/blob/b4c21748fc855b01d8b89dfed36ca57842bad863/docs/principia-v2-09-recursive-history-quotient-update.md) @b4c21748. Status niniejszego wyprowadzenia: **DERIVED / SELF_CHECKED / INDEPENDENT_REVIEW_NOT_REQUESTED**, bez nowego MATH, NON-CORE.

**A. Kontrprzykład do przeniesienia §6.16 poza kontrakt.** Ustalmy V={x,y}, aktywne nazwy K={λ} i dwa katalogi: A(λ)=(x=x), B(λ)=(x=y). Oba są spójne i nie dopuszczają wycofań, więc dla obu minimalna osiągalna naprawa wynosi 𝓣={∅}. Niech legalność literalnego przełączenia σ zależy od tego, czy aktywny certyfikat λ głosi nietrywialną równość różnych etykiet. Wtedy σ jest legalne w B i nielegalne w A. Zatem drzewa legalnej przyszłości się różnią mimo równego (q,K,𝓣). W §6.16 wymagano niezależności legalności od treści; przykłady **nie przeczą** tamtemu twierdzeniu. Sama wartość Cons i minimalne naprawy nie wyznaczają prawa przełączenia zależnego od treści.

**B. Kontrakt skończonej pełnej przyszłości.** Niech S będzie skończonym, niepustym zbiorem stanów zawierających WSZYSTKIE zmienne istotne dla przyszłej legalności, danych źródłowych, aktywnych znaczników, sterowania i obserwacji. Niech E będzie zbiorem literalnie etykietowanych kroków; w razie raportów wynikowych etykietą może być para (czynność, raport). Zakładamy o:S→O jako aktualnie obserwowaną etykietę zadaniową, En(s)⊆E jako zbiór możliwych legalnych etykiet oraz **częściową deterministyczną** aktualizację δ(s,e)∈S dla e∈En(s). Przy każdym ustalonym s i e jest najwyżej JEDEN następnik. Drzewo Beh(s) rozwija wszystkie takie legalne etykiety, niosąc o(s) na każdym węźle; pętle stanu dają nieskończone rozwinięcie drzewa, mimo skończonego S. Nie orzekamy tu o rozkładach prawdopodobieństwa ani nierozróżnialnych wielu następnikach pod tą samą etykietą.

**T1 — skończona rafinacja dokładnego ilorazu.** Definiujemy relacje na S:

\[
R_0=\{(s,t):o(s)=o(t)\},
\]

\[
R_{n+1}=\{(s,t):o(s)=o(t),\quad
\operatorname{En}(s)=\operatorname{En}(t),\quad
\forall e\in\operatorname{En}(s)\ 
(\delta(s,e),\delta(t,e))\in R_n\}.
\]

Wówczas każda R_n jest relacją równoważności, R_{n+1}⊆R_n, a ciąg stabilizuje się w pewnym N≤|S|−1. Dla każdego s,t∈S:

\[
\boxed{(s,t)\in R_N\iff\operatorname{Beh}(s)\cong\operatorname{Beh}(t)}
\]

przy izomorfizmie zachowującym dosłowne etykiety kroków, etykiety obserwacji, korzeń i strukturę następców.

**Dowód.** R_0 jest równością obserwacji, zatem relacją równoważności. Jeżeli R_n jest równoważnością, warunek równości zbiorów En oraz punktowa zgodność następców według R_n również tworzą relację równoważności, więc R_{n+1} nią jest. Z indukcji R_{n+1}⊆R_n (dla n=0 bezpośrednio; dla n>0 wynik z indukcyjnej inkluzji następników). Każda ścisła zmiana rozbija co najmniej jedną klasę; z co najwyżej |S| klas wynika stabilizacja w N≤|S|−1. Po stabilizacji R_N jest zgodną z legalnością i następnikiem kongruencją: korzenie w relacji mają równe obserwacje, te same etykiety legalnych ruchów oraz następników w tej samej relacji. Indukcja po długości słowa dowodzi zgodności wszystkich skończonych prefiksów przyszłości, a więc izomorfizmu pełnych rozwinięć drzew. W przeciwnym kierunku izomorfizm literalnie oznaczonych drzew daje zgodność korzeni, dostępnych krawędzi i następników na dowolnej ustalonej głębokości, więc (s,t)∈R_n dla wszystkich n, w szczególności R_N. □

**T2 — najgrubszy dokładny iloraz i jego aktualizacja.** Oznaczmy ρ(s)=[s]_{R_N}. Wtedy ρ jest dokładnie adekwatną pamięcią z II.7 i najgrubszym dokładnym ilorazem w porządku relacji równoważności z II.8, względem powyższego kontraktu. Ponadto zbiór dozwolonych literalnych działań jest dobrze określony na klasie:

\[
\overline{\operatorname{En}}([s])=\operatorname{En}(s),
\]

a częściowa aktualizacja ma postać

\[
\boxed{\overline\delta([s],e)=[\delta(s,e)]_{R_N},
\quad e\in\overline{\operatorname{En}}([s]).}
\]

Obie definicje są niezależne od reprezentanta na mocy stabilnego warunku R_N; to dokładnie przesłanki II.9. **Granica:** N≤|S|−1 jest ograniczeniem liczby iteracji rafinacji *na jawnie skończonej przestrzeni S*, a nie zapewnieniem taniego algorytmu, małego S lub skończonej pamięci dla oryginalnego systemu z nieskończoną historią.

**T3 — warunek legalnej kompresji pośredniej.** Niech η:S→Z będzie proponowaną pamięcią (np. składowe kosztowe, projekcja konfliktów, fragment proweniencji). Aby η samodzielnie obsługiwała prawidłową aktualizację i raporty bez reprezentanta, wystarczy i — w tym deterministycznym kontrakcie — jest konieczne, by przy η(s)=η(t) zachodziły równocześnie:
(a) o(s)=o(t);
(b) En(s)=En(t);
(c) η(δ(s,e))=η(δ(t,e)) dla każdego wspólnego legalnego e.
Jest to kongruencja jądra η. Wtedy pamięć obsługuje wszystkie przyszłości oraz dobrze określony operator U:Z×E⇀Z na obrazie η. Sama dokładność obserwacyjna η bez (c) może pozwalać na wyznaczenie klasy zadaniowej jako funkcji η, ale nie musi wyznaczać **następnego kodu η**. Jeżeli wymagamy tylko dokładności zadaniowej bez aktualizacji samej η, właściwym i słabszym kryterium pozostaje ker_eq η⊆R_N (II.7).

**D. Ograniczenia.** Jeżeli system jest niedeterministyczny z wieloma następcami dla identycznej etykiety, probabilistyczny, historycznie nie-Markowowski albo ma nieprzeliczalne zbiory stanów, nie wolno bez dodatkowego kontraktu przenosić powyższej rafinacji i ograniczenia N. W takim przypadku punktem odniesienia jest nadal przyszłe drzewo II.7 lub odpowiedni jawnie zadany typ bisymulacji i obserwacji. Formalna spójność równań nie dowodzi empirycznej prawdziwości certyfikatów.

**Koszty:** Node/LAB i Sol/E pozostają HOLD_BY_OWNER_BUDGET; Luna nie otrzymuje nowych zadań, nie zamawiamy testów ani recenzji. CORE5/IFX FREEZE, C1 HOLD.
