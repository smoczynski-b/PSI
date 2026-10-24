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
