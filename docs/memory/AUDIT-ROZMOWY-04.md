# Semantica Rozmowy — 04: audyt i korekta wykonania

Current work selection: [CURRENT-WORK-FRONT-01](CURRENT-WORK-FRONT-01.md).
Latest assessment: [memory and agent review](#memory-and-agent-review-2026-09-30).
The older sections below describe their own frozen commits. Their three F0
runtime defects have since been repaired; they are not the current repair queue.
The new review distinguishes source-derived findings from executed CI evidence.

Data: 2026-09-30, Europe/Warsaw.
Podstawa: gałąź `psi-memory-map-01`, stan
`db230e498c7f2808164ab4e0ac462b5b7da24751`; dokumenty i wykonania M1–M19,
odzyskane streszczenia ustaleń rozmowy oraz dwa źródłowe archiwa MHTML
z dostarczonego ZIP-u. Pełnego eksportu rozmowy 04 nie odnaleziono.
Nie jest to deklaracja przeczytania wszystkich jej wypowiedzi.

## Ocena wyniku rozmowy

Rozmowa doprowadziła do użytecznego, skończonego laboratorium pamięci:
typowanego grafu, kontroli proweniencji, kontraktów odczytu i jawnych włókien
kandydatów. Rozdzielenie zależności dowodowej, analogii, genealogii i planu
pracy jest poprawne i pozostaje zachowane. M15–M19 zachowują niejednoznaczność
językową zamiast wybierać najbliższą odpowiedź.

Dokumentowane granice są zasadniczo trafne: M4a mierzy bajty przygotowanych
pakietów, M8 rozmiar wybranych fragmentów; żaden z tych pomiarów nie dowodzi
poprawy rozumowania modelu. M4b ma status NOT_RUN. Próby M9 są syntetycznymi
zmianami dwóch uczestników, nie niezależnym badaniem dwóch modeli.

Gałąź ma 117 commitów po bazowym `7f4aecd`; część rozdziela jedną jednostkę
na zapisy pojedynczych plików. Liczba commitów nie mierzy jakości. Historii
nie przepisano; bieżąca naprawa jest jednym spójnym pakietem z testami.

Główna usterka leży między kontraktem a wykonaniem: wybrane przykłady
przechodziły testy, chociaż zmiana węzła, źródła lub typu danych naruszała
deklarowane warunki. Poniższe świadki sprawdzono przez wykonanie kodu.

## Potwierdzone błędy → jednostki → konsekwencje

| Błąd | Jednostka i świadek sprzed poprawki | Wdrożona korekta |
|---|---|---|
| Inny punkt startowy niż w kontrakcie | M12–M15: zadanie o II.7 zwracało także krawędzie wychodzące z II.9; selektor miał stałe `ANCHOR=II.9` | Wspólny wykonawca otrzymuje węzeł z kontraktu; test porównuje zadania o II.7 i II.9. |
| Dowolny wybór jednego z kilku węzłów | M13: „II.9 i II.7” wybierało II.7 według porządku identyfikatorów | NEEDS_ANCHOR_POLICY i brak odczytu. |
| Zakaz odczytany jako dodatnia intencja | M13–M15: „Pomiń zależności dowodowe II.9; pokaż granice” wybierało także przesłanki | Niewspierany zakres wyłączenia daje NEEDS_CONTRACT; obsługiwane „czego nie implikuje” nadal działa. |
| Etykieta zastępowała bieżącą kontrolę źródła | M14/M15 i ścieżka M9: `VALID`/`VERIFIED` wystarczało bez ponownego skrótu | Porównanie fragmentu i całego pliku w chwili użycia; nieaktualny certyfikat nie wraca jako słabsza wskazówka. |
| Tryb certyfikowany wymagał drugiego przełącznika | Pomocnicze wykonanie M14 wymagało `strict=True` niezależnie od kontraktu | Tryb odczytu wykonuje się bez dodatkowej decyzji wywołującego. |
| Ucięcie budżetem nie było oznaczone | M14: budżet 4 wybierał 4 z 5 dostępnych certyfikowanych granic II.9 | Jawne `budget_truncated`; nie utożsamia się limitu ze zbadaniem całego lokalnego zbioru. |
| Nieznany predykat stawał się sprzecznością | M16/M18: literówka `MAESURES` dawała INCONSISTENT | NO_RELATION_CONTRACT, bez pozornego pustego włókna. |
| Nieustalona dziedzina tolerancji | M18 dopuszczało ułamki, NaN i wartości logiczne jako liczbę konfliktów | Wymagane `b∈N₀`; wartości obserwacji są skończonym zbiorem napisów, nie pojedynczym napisem. |
| Pusty wybór omijał kontrolę schematu | M19: błędna relacja z pustym wyborem obiektów przechodziła jako wynik zerowy | Najpierw kontrola relacji i identyfikatorów, potem projekcja. |

Wykonanie kontraktu przeniesiono z pomocniczych procedur testowych do
`scripts/memory_retrieval.py`. Dotychczasowe testy M12–M15 korzystają teraz
z tej samej ścieżki, którą ma stosować agent. Widok M19 nad grafem deklaruje,
że pokazuje zapisane relacje bez ponownej certyfikacji; nie podszywa się pod
odczyt dowodowy.

## Warunek matematyczny

Dla ustalonej dziedziny `W`, poprawnie określonego predykatu `r` i obserwacji `a`:

\[
F_{k+1}=F_k\cap\{x\in W:r(x)=a\}.
\]

Brak definicji `r` oznacza brak legalnego kroku. Nie oznacza, że zbiór po prawej
stronie jest pusty. Dopiero sprzeczne dane dotyczące zdefiniowanego predykatu
mogą legalnie dać `F=∅`.

Dla M18:

\[
F_b=\left\{x\in F_0:
\sum_i\mathbf1\{r_i(x)\notin A_i\}\le b\right\},
\qquad b\in\mathbb N_0.
\]

Przy stałym `b` dodanie poprawnej obserwacji nie powiększa włókna. Zmiana `b`
zmienia kontrakt tolerancji; nie jest nowym świadectwem o świecie. Naprawa
dotyczy dziedziny tych działań, nie ustanawia nowego prymitywu PSI.

## Zegarek: tożsamość i zadanie

Dodany świadek obejmuje dwa zegarki `A,B` o tych samych obserwowanych cechach
materialnych, lecz różnych historiach. Po obserwacji położenia i mierzonej
wielkości pozostaje `F={A,B}`. Dopiero zadeklarowana obserwacja historii
wyodrębnia jeden egzemplarz. Jest to skończony model rozróżnienia zgłoszonego
przez użytkownika; nie twierdzenie o naturalnej ontologii.

Należy rozdzielać:

\[
|q_{\mathrm{cechy}}(F)|=1,
\qquad |q_{\mathrm{historia}}(F)|=2.
\]

Jednoznaczność odpowiedzi na zadanie nie wymaga jednoznaczności całego
obiektu. Nazwa językowa i zgodność kilku cech nie kasują różnicy historii.

## Genealogia źródeł

Skróty całych plików `Principia Semantica Uzupełnienie.mhtml` i
`Kontynuacja projektu PSI.mhtml` zgadzają się z rejestrem:

- `0e69aa1b4b0004edb7a2a40f0d9703e15da5eca38eaa2f8e03e4026c2efebee5`;
- `b93e3a406b6dccd9884d6036121c149e5f928feeed1f34a1156dd9190a467493`.

To weryfikacja tożsamości archiwów. Nie poświadcza automatycznie cytatu,
autorstwa wypowiedzi ani relacji PRECURSOR_OF. Trzy wpisy
CONVERSATION_RECOVERED mają odtworzone lokalizacje/streszczenia, lecz bez
utrwalonego certyfikatu surowego eksportu. Test genealogii nazwano zgodnie
z wykonaniem: REGISTRY_CONSISTENCY_PASS. Nie wykonuje on odzyskiwania archiwów.

## Reguła pracy dla kolejnych modeli

1. Ustal obiekt zadania, kontrakt, źródło i warunek zakończenia.
2. Wykonaj jeden ograniczony odczyt ze wskazanego węzła; zachowaj kierunki i typy relacji.
3. Sprawdź aktualne źródła użytych certyfikatów. Wskazówka wyszukiwawcza nie zastępuje dowodu.
4. Zachowaj wielość kandydatów, brak kontraktu i ucięcie odczytu jako różne stany.
5. Zakończ jednostkę po kontrprzykładzie naprawczym i testach dotkniętych ścieżek.
   Kolejny numer eksperymentu wymaga nowego wybranego zadania.

Przykład właściwego wejścia:

```bash
python scripts/memory_retrieval.py 'dla II.9 pokaż granice, tylko pełne certyfikaty'
```

Pozostają otwarte: niezależny pomiar jakości modeli (M4b), ogólna semantyka
języka i wyłączeń, kompozycja wielu węzłów, certyfikacja historycznych
fragmentów rozmów oraz zastosowanie poza zadanymi skończonymi dziedzinami.
Nie uruchomiono płatnych badań ani nie scalono laboratorium z `main`.

## Active memory review 2026-09-30

Reviewed commit: `fce89bde2d8bb6e95292d435bed84e1702c6b26c`.
Scope: all 46 changed files in the 51 commits after `cf9d91a`, including three
memory specifications, nine experiment protocols, seven TSV registries, ten
runtime modules, twelve regression programs and five workflows. The twelve
new regression programs passed locally. This is a source/code/test inspection,
not a complete transcript review, model-quality trial or fresh literature audit.
Additional boundary witnesses below remain OPEN in the inspected runtime.

### Obiekt → warunki → wielkość → test

Obiekt: lokalna pamięć współdzielona z widokami zadaniowymi, MVCC, dziennikiem
WAL, Sługą i Immunologią. Warunki: jeden proces, jawne zbiory odczytów i
zależności, dostarczona baza odtworzenia oraz jawnie dopuszczone zdarzenia.
Mierzone: równość decyzji po restarcie, legalność reakcji na dane liczbowe,
kompletność wskazania zależnych widoków i rzeczywista liczba odwiedzonych
krawędzi. Źródłem oceny są wykonane kontrprzykłady, nie nazwy ról.

Przejście 12 programów dotyczy ich zapisanych przypadków. Grupy:
aktywna pamięć, skalowanie, unieważnianie, wiele widoków, współbieżne propozycje,
MVCC, integracja współdzielona, WAL, Sługa, Immunologia, instytucja i genealogia.
Test genealogii kontroluje rejestr; etykiet `SOURCE_VERIFIED` nie zweryfikowano
ponownie przez lekturę wszystkich publikacji. Oryginalność pozostaje OPEN.

### Potwierdzone świadki i kierunek napraw

| Jednostka | Odtworzone zachowanie | Warunek odbioru naprawy przez GPT-5 |
|---|---|---|
| Sługa: decyzja po kolizji i restarcie | `C/SEMANTIC_VERDICT` daje BLOCK. `C/RECOVER` daje kolizję. Po ponownym utworzeniu `ServantRuntime` oryginalne `C/SEMANTIC_VERDICT` daje kolizję zamiast powtórzenia BLOCK. | Pierwszy ukończony zapis identyfikatora pozostaje rozstrzygający przed i po restarcie; kolizja jest kronikowana oddzielnie. Powtórzenie nie wykonuje drugiej transakcji. |
| Immunologia: dziedzina liczbowa | `value=NaN` dla `IMM-CONFLICT-BURST` zmienia `NORMAL` na `POST_QUARANTINED` i emituje NOTICE oraz POST_QUARANTINE. | Niepoprawna wartość nie może uruchomić reakcji. Jawnie ustalić dziedzinę progów, obserwacji i całkowitych budżetów; sprawdzić NaN, nieskończoności, wartości logiczne i granice. |
| Immunologia po `RECOVER` | `durable.shared.views` zostaje zastąpione, lecz istniejące `immune.views` wskazuje poprzedni obiekt. Nowy zależny widok `late` nie trafia do REQUEST_RECHECK. | Po odtworzeniu używany jest bieżący indeks albo stara instancja zostaje jawnie wyłączona do ponownego związania. Brak cichego odczytu dawnego indeksu. |
| Koszt rozsyłania | Przy jednej delcie licznik wskazuje jeden widok, lecz `_refresh_indices` odwiedza 18 krawędzi dla początkowego N=8 i 2050 dla N=1024. | Rozdzielić liczbę wybranych widoków od pracy w nich; uwzględnić przebudowę indeksów i narastającą historię zdarzeń. To granica obecnego pomiaru, nie utrata poprawności wyniku. |
| Rzadkie macierze relacji | Zmiana tylko pochodzenia krawędzi z `doc:one` na `doc:two` daje identyczne COO, lecz inny skrót semantycznego stanu. | Przy zadaniu wymagającym pochodzenia zachować metadane obok macierzy. Samo COO sprawdza strukturę relacji, nie cały zapis pamięci. |

Przyczyna pierwszej luki: `_load_completed_commands` bierze ostatni
`SERVANT_RESULT`, również wynik kolizji zapisany przez `_stop(..., remember=False)`.
Wyłączenie zapamiętania działa w żywym słowniku, ale nie w odtwarzaniu kroniki.
Przyczyna drugiej: warunek `value < min_value` nie odrzuca NaN.
Trzecia powstaje na styku poprawnie działających osobno warstw; sam test
odtworzenia dziennika nie obejmuje związania istniejącej Immunologii.

Odtworzenie trzech usterek na wskazanym commicie, bez usług zewnętrznych:

```bash
PYTHONPATH=scripts python - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
from test_servant_runtime import make_durable
from servant_runtime import ServantRuntime, ServantCommand
from test_immune_runtime import make_stack, workspace, obs
from immune_runtime import ReactionBudget

with TemporaryDirectory() as td:
    root = Path(td)
    durable = make_durable(root / 'memory.wal')
    servant = ServantRuntime(durable, root / 'servant.wal')
    original = ServantCommand('C', 'SEMANTIC_VERDICT')
    print(servant.handle(original).disposition)
    servant.handle(ServantCommand('C', 'RECOVER'))
    restarted = ServantRuntime(durable, root / 'servant.wal')
    print(restarted.handle(original).disposition)

with TemporaryDirectory() as td:
    durable, servant, immune = make_stack(td, budget=ReactionBudget())
    result = immune.observe(obs('NAN', 'IMM-CONFLICT-BURST',
        'PROTOCOL_CONFLICT_COUNT', 'proof', float('nan')))
    print(result.status)

with TemporaryDirectory() as td:
    durable, servant, immune = make_stack(td, budget=ReactionBudget())
    servant.handle(ServantCommand('R', 'RECOVER'))
    durable.shared.register('late', workspace('L', 'LROOT', 'L'),
        extra_dependencies=('workspace:proof',))
    result = immune.observe(obs('RECOVERED', 'IMM-INVALIDATION-FANOUT',
        'INVALIDATION_FANOUT', 'proof', 8))
    print(durable.shared.views.direct_dependents('workspace:proof'))
    print(result.requested_rechecks)
PY
```

Zaobserwowane wyniki: `BLOCK_ILLEGAL_TRANSITION`, następnie
`STOP_ESCALATE_CHRONICLE`; `POST_QUARANTINED` dla NaN; bieżący indeks ma
bezpośrednich zależnych `down1, late`, natomiast żądania obejmują `down1, down2`
i pomijają `late`. Program jest historycznym odtworzeniem błędów, nie wzorcem
oczekiwanych poprawnych wyników.

### Co wynika dla projektu

Nowy dział realizuje większą część infrastruktury, niż obejmowała wcześniejsza
ocena M4b. Utrzymywanie widoków przez delty jest już implementacją referencyjną,
a nie samą metaforą. Mierzone przyspieszenia dotyczą skończonych prób
syntetycznych; 12 PASS nie ustanawia jeszcze niezawodności całej integracji
ani poprawy wyników modeli.

Pierwsza jednostka dla GPT-5: naprawa odtwarzania decyzji Sługi i regresja
`oryginał → kolizja → restart → oryginał`. STOP po zachowaniu pierwotnej decyzji,
braku dodatkowego COMMIT i przejściu testów Sługi oraz dotkniętych wywołań
Immunologii. Pozostałe naprawy są kolejnymi, odrębnymi jednostkami.
Nie potrzeba nowego prymitywu, kolejnej roli ani nowej numeracji architektury.

Po naprawach: jeden pełny przebieg z rzeczywistymi rekordami PSI, a następnie
oddzielne badanie jakości modeli i pełnego kosztu. M4b pozostaje NOT_RUN.
Wskazana kolejność jest decyzją wykonawczą tego przeglądu, nie twierdzeniem
o optymalności ani odzyskanym dosłownym poleceniem z rozmowy 04.

### Zakres odzyskania rozmowy i grafiki

Ponowne wyszukiwanie nie dostarczyło pełnego eksportu rozmowy 04. Streszczenia
odtworzyły chmurę punktów z odległymi istotnymi połączeniami, różne obrazy tych
samych danych oraz wymóg ustalania intencji przed zamrożeniem kontraktu.
Zwrócone parafrazy nie są tu traktowane jako dosłowne cytaty, nawet gdy opis
wyniku wyszukiwania nazywał je pełnym cytatem.

W osobnym wątku wizualnym istnieje `PSI-VIZ-TEST-01_factorization.mp4`
(14 s, 1080×1920) i `PSI-VIZ-TEST-01_final-frame.png`. Obejrzano klatki filmu
w 3 s i 8 s oraz planszę końcową; nie deklaruje się obejrzenia każdej klatki.
Świadek rozróżnia `rho(u,v)=u, R(u,v)=u²` od `rho(u,v)=u, R(u,v)=v`.
To prezentacja faktoryzacji i jej niepowodzenia, nie pomiar pamięci modelu.
Pliki nie są częścią tego commitu; ich skróty wiążą oglądane artefakty:

- film: `118b86f5b1e07f6ace014d7dd174ae3d80b0a2a8503cbe0eb93def951b8681bf`;
- plansza: `b3121ba24e6483cba75ccd12ed107af79cc951e5daa20845018a7a81c12791ba`.

Cel użytkownika obejmuje wizualizację wzorów, przekształceń i zależności oraz
możliwość filmu. Zapis formalny dla wykonania, geometria procesu i plansza
dla człowieka mają odrębne zadania. Zasady ich zgodności są w
[kontrakcie reprezentacji](representation-check.md).

## Memory and agent review 2026-09-30

**Reviewed HEAD:** `53bdc36c44c0b2d6d2621339ec65dc0f00de9b80`.
**Delta:** 88 commits / 67 changed files after
`5937291ce4bf85c729fca1269c2c400f202a4250`.
**Decision:** retain the implemented F0–F4.3 reference results; repair durability
and projection boundaries before F4.4. This review changes instructions and
work selection, not runtime behavior or canonical mathematics.

The delta and selected unchanged dependencies were retrieved. Inspection focused
on contracts, persistence and replay paths, movement/usage integration, Curator
decisions, visual transformations, corresponding tests and workflow records.
The local execution environment was unavailable. New witnesses below are
**SOURCE_DERIVED / RUNTIME_NOT_RUN in this review**. Their first implementation
step is an executable regression that fails on the reviewed revision. Existing
CI successes are evidence for their recorded cases, not fresh execution here.
No full conversation-04 transcript was recovered; available conversation
summaries cannot establish the complete instruction/approval history.

### Value demonstrated and remaining measurement

| Layer | Demonstrated progress | Remaining boundary |
|---|---|---|
| F0 | First SERVANT result survives ID collision/restart; IMMUNE rejects invalid numeric domains; recovered shared/view handles retain identity | These fixes do not settle other crash windows |
| F0 cost accounting | Index scans and event-history work are explicitly counted | Operation counts are not total latency, token or infrastructure cost |
| F1 | Source read once; derived result survives clean restart; changed premise produces persistent NEEDS_RECHECK | A/B are deterministic fixtures, not live model agents |
| F2.1 | ACCESS_STEWARD executes Guardian policy, tracks session location, separates capabilities and telemetry classes | New cross-journal recovery gap R2 |
| F3.1–F3.3 | Snapshot/delta reconstruction, version manifests, CURRENT, usage references and proposal-only Curator | R1/R7/R8 limit durability, observed-use attribution and observation identity |
| F4.0–F4.3 | Source-bound scene pipeline, SVG and a real Manim MP4; parallel motion and moving edges were corrected | R3–R5 limit integrity, redaction and visible relation direction |

ACCESS_STEWARD is subordinate Guardian machinery, not a fifth constitutional
role. Curator observes explicit administrative metrics and proposes changes;
the reference planner does not execute restructuring or allocate its own budget.
Recursive archive references are implemented within this bounded model.

This is useful engineering progress: later work can reuse a derived result and
its declared dependency status. Improvement in a lower model's answers, total
cost, generality and novelty remains unmeasured. A drawing's successful render
does not establish a benefit from communicating through that drawing.

### Object, invariant and measurement

Object: the existing single-process memory/role journals and their derived
visual packets, with an explicit seed, contract, version and request identity.
No distributed-execution guarantee is added.

For each committed movement request `r`, after recovery completes, require
one state transition, one canonical movement and one canonical outcome.
Repeated audit attempts are allowed; repeated mutation or charging is not.
Measure lost acknowledged records, duplicate effects and outcome mismatches;
the acceptance target for each declared interruption case is zero.

For every consumed visual packet `p`, verify
`H(canonical_payload(p)) == declared_payload_digest(p)` and its source
bindings before use. Test a changed payload with the old digest. Hash equality
does not replace task-relative adequacy: directedness, visibility and required
metadata need their own separating cases.

### Retrieved execution evidence

| Evidence | Commit / run | Verified scope |
|---|---|---|
| F1 | `a1606ca9e358b9064bbad48ae98b0c56b2864213`; [run 36742791245](https://github.com/smoczynski-b/PSI/actions/runs/36742791245) | Job steps succeeded for reuse, SERVANT/collision, WAL and cost accounting |
| F3.3 integration | [run 36756411723](https://github.com/smoczynski-b/PSI/actions/runs/36756411723) | Logs report archive contract/runtime/usage, Curator, ACCESS_STEWARD, SERVANT and institution PASS at their stated scope |
| F4.3 real render | `d32f6b547715be28638b125e3570a172a1b35cc2`; [run 36764149914](https://github.com/smoczynski-b/PSI/actions/runs/36764149914) | Logs verify h264 MP4, 1.666667 s, 44273 bytes, artifact 11119624136; F4.0–F4.3 and affected regressions passed |
| Reviewed HEAD | [control 36764211193](https://github.com/smoczynski-b/PSI/actions/runs/36764211193), [memory-map 36764211280](https://github.com/smoczynski-b/PSI/actions/runs/36764211280) | Both jobs succeeded at reviewed HEAD; path-filtered component runs above have their own commits |

The later render run supplements the original F4.3 witness; do not mix their
artifact IDs or ZIP digests. This reviewer inspected code, job steps and logs,
not the downloaded video frames. A nonempty MP4 and unequal endpoint PNG files
are technical checks, not a general semantic or legibility test.

### Source-derived findings and bounded acceptance cases

**R1 / P0 — safe journal continuation and tail repair.**
In [JSONLWAL](../../scripts/durable_shared_memory.py), initialization reads a
valid prefix but does not resolve `tail_truncated`; `append`
writes to the existing bytes. Main DurableSharedMemoryRuntime explicitly repairs
the tail; AccessChronicle, ArchiveChronicle, UsageChronicle, Curator's WAL,
ServantChronicle and ImmuneMemory do not.

Separating witness: valid record → append an incomplete `{"seq":`
tail → restart a journal → append a new record. The new JSON is concatenated
to the old fragment; append returns, but the reader discards that invalid final
line. Another append moves it into the interior and raises corruption.
Additionally, `repair_truncated_tail` opens the entire file with `wb`;
interruption while rewriting can destroy previously valid history.

Acceptance: every journal either repairs an explicitly uncommitted tail safely
before writing or blocks writes with a recovery reason. Preserve the verified
prefix through an interruption during repair; never treat interior/hash-chain
corruption as a disposable tail. Exercise interrupted append, restart, repair,
two subsequent appends and another restart. Check representative journal wrappers
and the shared writer; include short-write handling before claiming durable ACK.
A validated byte-boundary truncation or an atomic replacement is a candidate
implementation, subject to the declared filesystem durability contract.

**R2 / P0 — reconcile committed state with institutional results.**
In [SERVANT](../../scripts/servant_runtime.py), durable commit precedes
`SERVANT_RESULT`. If the process stops between them, restart restores the
transaction but not a completed command. Repeating the exact command reaches
`DurableSharedMemoryRuntime.commit`, which rejects the already known txid,
and SERVANT records BLOCK despite the committed mutation.

[ACCESS_STEWARD](../../scripts/access_steward_runtime.py) adds another boundary:
SERVANT commit → ACCESS_MOVEMENT → ACCESS_RESULT. Restart between these writes
can recover location M1 without the completed ENTER result. Repeating the same
OUTSIDE→M1 request then returns SESSION_ALREADY_PRESENT. Telemetry can be absent,
or report MOVED beside a later DENY result.

Acceptance: persist/bind request and command fingerprints to transaction
identity, then reconcile unfinished outcomes from verified durable evidence.
Crash after memory COMMIT, before SERVANT_RESULT, before ACCESS_MOVEMENT and
before ACCESS_RESULT. On restart, exact replay preserves the committed outcome,
records one canonical movement/result, performs no second mutation or charge,
and still rejects a different payload with the same ID. Include a later
independent movement so reconciliation cannot rely only on current location.
Do not reconstruct an original proposal using a newer base revision.
Audit attempts may remain multiple; the committed operation is unique.

**R3 / P1 — verify visual payloads at every consumption boundary.**
[VisualFrame](../../scripts/psi_viz_projection.py) and subsequent packets use
frozen dataclasses containing mutable dictionaries. `compile_print_keyframe`
reads their contents without recomputing frame digests; transition classification
compares stored digest fields. `render_svg`, `compile_manim_plan` and
`compile_executable_manim_scene` do not verify the actual input payload hash.

Witness: compile a valid keyframe, change a nested label/relation/coordinate,
keep its old digest, then render it. The image follows the modified payload
while binding metadata still carries the old digest. Similarly, mutate a frame's
semantic payload without changing its stored digest and classify a transition.

Acceptance: reject stale hashes and inconsistent duplicated bindings before
rendering/classification; test nested mutation at frame, keyframe, timeline and
plan boundaries. Deep immutability or defensive copies reduce accidental edits
but do not replace verification when deserializing a packet. A matching hash
checks payload identity, not authorization or truth.

**R4 / P1 — apply status redaction to nodes as well as edges.**
`compile_visual_frame` gates edge status on `visible_metadata` but always
copies `workspace.node_status`. `compile_print_keyframe` copies it into node
status and SVG renders it. Existing redaction fixtures principally exercise
edge provenance.

Witness: node X has NEEDS_RECHECK, contract uses `visible_metadata=()`.
Acceptance: no forbidden node/edge status in frame, output packets, SVG,
executable scene or a visual channel derived from that hidden value; explicitly
allowed status remains available. This is a projection-contract defect; the
current renderer does not itself implement Guardian admission.

**R5 / P1 — retain task-required direction in visible relations.**
[SVG](../../scripts/psi_viz_renderer.py) emits undirected `<line>` primitives
and [Manim](../../scripts/psi_viz_manim_exec.py) emits `Line`, with no declared
visible direction encoding. For fixed node positions, SVG depictions of
A DEPENDS_ON B and B DEPENDS_ON A have the same visible line and relation label;
different opaque asset IDs do not supply the missing distinction to a viewer.

Acceptance: declare direction encoding for directed relation types and test
the reversed-edge pair in SVG and an actual rendered animation frame.
Symmetric relations may use undirected marks only under their relation contract.
Separately declare which status/provenance fields an animation exposes:
ManimPlan currently drops those fields when constructing node/edge assets.
Retain a checked accompanying packet when a task requires them.

**R6 / P1 — distinguish tariff, measured work and budget accounting.**
ACCESS_STEWARD calls `cost_meter` before the durable movement. If its returned
cost exceeds budget, the DENY path discards that value and `_finish` records
a zero vector. The fixtures use supplied costs; they do not measure the whole
commit/fsync/telemetry path. `CostVector.l1` sums seven components whose units
or normalization are not defined in that type.

Witness: estimated compute=1, budget=2, meter returns compute=3. Acceptance:
DENY leaves location unchanged and preserves the returned cost evidence with its
meaning. Define whether this is a quote or already incurred cost; measure actual
work after execution where applicable. Keep unknown separate from zero.
Declare units and, before scalar totals, a normalization/weighting contract.
Current per-request budget checks do not establish a cumulative allocation/debit
system; add one only when a selected task needs it.

**R7 / P2 — movement association is not proof of version consumption.**
[Usage validation](../../scripts/memory_archive_usage_runtime.py) checks that an
archive manifest names the movement's destination map. Movement has no consumed
archive-version/revision field. A caller can associate that movement with either
of two historical versions of the same map. Existing checks establish the
reference association, not which version the agent actually read.

Acceptance: either label the record as an association only, or require a
verified read/use receipt containing version/revision and content digest.
Test two versions of the same map: reject attribution to the unconsumed version;
restart preserves the binding and telemetry access restrictions.

**R8 / P2 — define identity for observations that produce no proposal.**
[Curator.evaluate](../../scripts/curator_planner_runtime.py) remembers an
observation fingerprint only when a proposal is written. A below-threshold
observation leaves no identity record; the same ID with changed metrics is later
accepted if it now crosses a threshold. The general collision claim therefore
exceeds the tested observation-with-proposal case.

Acceptance: define ID scope explicitly. If IDs identify all observations, persist
a bounded no-proposal outcome and reject changed-payload reuse before/after
restart. Otherwise narrow the contract and name the input accordingly.
The test must include below-threshold → same ID/different metrics → restart,
not only two conflicting observations that both produce proposals.

### Agent workflow assessment and proportional correction

The agent repaired the earlier F0 findings, built executable reference modules,
and corrected edge motion and label problems exposed by real rendering.
It generally labels deterministic/reference results and unrun model evaluation.
Those are useful habits worth preserving.

The main weakness is extending local PASS results across untested boundaries.
Clean restart is not interruption between journals; a stored hash is not a
verification at its next consumer; an emitted edge is not necessarily a readable
directed relation. New tests should target these distinctions.

Entry instructions also drifted: AGENTS and memory README still selected the
already repaired SERVANT collision; WORK-FRONT selected an earlier phase;
CURRENT selected F4.4; Curator's planning amendment still said NOT IMPLEMENTED.
This review synchronizes those pointers. The general project default P9-I is
unchanged; an explicit memory task selects the memory front under the existing
user-task precedence rule.

The 88 commits include repeated runtime → test → workflow → report → pointer
sequences. Commit count is not quality or a measure of active work time.
Prefer one coherent unit containing implementation, its necessary tests and
the current-pointer update. Keep published history. No inference about ignored
STOP messages or unapproved work is justified by the incomplete chat record.

Use the existing 75/15/10 execution/verification/coordination target as a working
budget, not a measured result. On entry inspect the delta once; after three
units or a material external change review priorities; at each durable side
effect inspect interruption boundaries; before publication check fresh HEAD
and affected gates. Stop a unit when its acceptance case and affected
regressions pass. Do not add a parallel audit registry or a timer-driven
stream of reports. The detailed order and stop conditions live in
[CURRENT-WORK-FRONT-01](CURRENT-WORK-FRONT-01.md).

### Decision after stabilization

Resume the bounded F4.4 SPLIT adapter only after its listed prerequisites.
Then choose one small F5 comparison with fixed tasks, source revision, model
settings and evaluator. Compare ordinary context, a simple retrieval baseline
and PSI memory; separate calibration from held-out cases. Measure correct reuse,
correct refusal of stale results, incorrect accepted answers, source rereads,
tokens/tool calls and end-to-end latency. Include interruption and changed-premise
cases. A cheaper incorrect answer is not a successful memory optimization.
M4b remains a separate text-context preparation experiment with model efficacy
NOT_RUN. No model run, paid evaluation, deployment or main-branch merge is part
of this review.
