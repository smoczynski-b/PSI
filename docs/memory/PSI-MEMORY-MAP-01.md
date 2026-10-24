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
