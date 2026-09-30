# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Reviewed code:** `1f79a752c9f4c87f2e870fcc1fecdbe0c1e35f2f`  
**R1 result:** `docs/memory/PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md`  
**R2 result:** `docs/memory/PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md`  
**Scope:** current work selection for an explicitly selected memory task.
Supersedes older NEXT prose in AGENTS, memory README and WORK-FRONT.
The general project default remains in `docs/control-state.json`.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Current decision

**NEXT: R3 — verify visual digests and duplicated bindings at every PSI-VIZ consumer boundary.**
R1 and R2 are closed `PASS_WITH_BOUNDARY`. The mandated three-unit re-evaluation
(R0–R2) found no new evidence that changes the ordered front, so R3 remains the
highest unresolved blocker of F4.4. F0–F4.3 keep their recorded
PASS/CONTRACT_PASS scopes; those scopes do not certify stale-hash resistance.

R1 evidence is recorded in
[`PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md`](PSI-MEMORY-R1-JOURNAL-RECOVERY-01.md).
R2 evidence is recorded in
[`PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md`](PSI-MEMORY-R2-RESULT-RECONCILIATION-01.md):
the original crash witness was reproduced as a failure in run `36770611699`,
and the corrected cross-journal witness plus Servant, ACCESS_STEWARD and WAL
regressions passed in run `36771111707`.

Audit discipline inherited from **Semantica Rozmowy — 03** remains binding:
a local projection is not the project state (`P_i(S) !=> S`), and a successful
local transition does not certify the global transition. R2 applied this to
journal projections; R3 applies the same rule to representation bindings: a
stored digest field is not evidence that the payload currently consumed by the
renderer still has that digest.

Read the [latest audit](AUDIT-ROZMOWY-04.md#memory-and-agent-review-2026-09-30)
for source locations, separating witnesses and acceptance conditions for R3–R8.

## Ordered repair plan

| Unit | Priority / dependency | Deliverable and stop condition |
|---|---|---|
| R0: current instructions | DONE | Entry points select this front; old F0 failures are no longer presented as current; Curator's implemented proposal engine is distinguished from unimplemented restructuring |
| R1: journal continuation | DONE / PASS_WITH_BOUNDARY | Shared JSONLWAL repairs only incomplete final tails at the verified byte boundary; complete corruption fails closed; interrupted repair and short writes are tested; wrapper and shared-runtime restart witnesses pass |
| R2: result reconciliation | DONE / PASS_WITH_BOUNDARY | Memory COMMIT, SERVANT_RESULT, ACCESS_MOVEMENT and ACCESS_RESULT reconcile after interruption boundaries; exact replay does not duplicate mutation or metering; later independent movement does not corrupt historical outcome; ID collision remains rejected |
| R3: visual digest verification | P1 / NEXT | Nested changes to frame/keyframe/timeline/plan cannot render or classify under old hashes; verify binding consistency at each consumer |
| R4: complete status redaction | P1 / after R3 | Hidden node and edge status is absent from emitted payloads and visual channels; allowed metadata remains usable |
| R5: directed visual relations | P1 / after R4 | Reversing a directed edge is visibly distinguishable in SVG and rendered animation; task-required metadata has a declared output channel or checked accompanying packet |
| R6: cost semantics | P1 / before cost-benefit claims | Over-budget meter evidence is retained; quote/actual/unknown are separate; units and scalarization are explicit; per-request check is not called a cumulative budget |
| R7: consumed version receipt | P2 / before claiming observed version use | Distinguish a movement association from verified consumption; two versions of one map cannot silently substitute for each other |
| R8: no-proposal observation identity | P2 / before general collision guarantee | Define ID scope and test below-threshold observations with changed-payload replay, including restart |

R7/R8 do not block unrelated visualization repair; they block their respective
stronger claims. Do not convert this table into an automatic instruction to run
all units indefinitely. Select one primary unit per authorized work scope.
For R3, test the actual payload against its declared digest at every consumer;
do not repair only the producer or trust frozen dataclass wrappers around
mutable nested objects.

## Handoff and proportional verification

1. Freeze R3 input HEAD, payload type, digest invariant and separating cases.
   First execute stale-hash cases against that revision; record reproduced/not
   reproduced.
2. Mutate nested frame/keyframe/timeline/plan payloads while retaining old
   stored digests. Rendering or semantic transition classification must reject
   the inconsistent object before output is produced.
3. Implement the smallest shared verifier or boundary checks that recompute the
   relevant digest from the payload actually consumed. Verify duplicated
   bindings (frame/keyframe/timeline/plan) agree rather than checking fields in
   isolation.
4. Run the separating witness and affected F4.0–F4.3 source/render regressions.
   Broaden only for an identified dependency.
5. A valid hash proves binding/integrity only. Do not describe it as semantic
   truth, authorization, admission or provenance authority.
6. Update code, necessary tests, result and this pointer as one coherent unit.
   Recheck remote HEAD; preserve concurrent changes; never force-push routinely.
7. Stop when stale payloads fail closed and unchanged valid F4 witnesses still
   pass. Re-evaluate the frontier after R3 if a material new dependency appears.

For F4.4, R1 and R2 are satisfied; require R3–R5 and the affected integration
regressions first. R6 must precede an end-to-end cost claim or F5 cost
comparison. Keep F4.4 restricted to one typed SPLIT with an admitted source
transition and verified before/after diff. A richer event without an adapter
still fails closed. After that, F5 tests a fixed task set and simple retrieval
baseline; model benefit remains NOT_RUN. GPU and live FORUM work remain outside
this selected front.

## Recorded implementation state

```text
F0   PASS_WITH_BOUNDARY
F1   PASS_WITH_BOUNDARY
F2.0 CONTRACT_PASS
R1   PASS_WITH_BOUNDARY
R2   PASS_WITH_BOUNDARY
F2.1 PASS_WITH_BOUNDARY; R6 OPEN
F3.0 CONTRACT_PASS
F3.1 PASS_WITH_BOUNDARY
F3.2 PASS_WITH_BOUNDARY; R7 OPEN
F3.3 PASS_WITH_BOUNDARY; R8 OPEN
F3   REFERENCE_CASES_PASS; HARDENING_OPEN
F4.0 CONTRACT_PASS; R3/R4 OPEN
F4.1 PASS_WITH_BOUNDARY; R3/R4 OPEN
F4.2 PASS_WITH_BOUNDARY; R3/R4/R5 OPEN
F4.3 PASS_WITH_BOUNDARY; R3/R4/R5 OPEN
F4.4 DEFERRED_AFTER_R3_R4_R5
F5   NOT_RUN
```

## F4.3 — recorded witness before this review

Poniższy zapis zachowuje wynik wcześniejszego wykonania; otwarte warunki R3–R5 są opisane wyżej.

Pierwszy rzeczywisty film PSI-VIZ został wyrenderowany w Manimie z wcześniej sprawdzonego łańcucha:

```text
VisualFrame
-> PrintKeyframe + AnimationTimeline
-> ManimPlan
-> executable Manim scene
-> real MP4
```

Świadek pozostaje czysto reprezentacyjny:

```text
FIBRE_LAYOUT -> REPOSITION -> QUOTIENT_LAYOUT
```

przy:

\[
\boxed{semantic\_digest_{before}=semantic\_digest_{after}}
\]

oraz różnych `layout_digest`.

Zamrożone:

\[
\boxed{REPOSITION\ does\ not\ mutate\ semantics}
\]

\[
\boxed{typed\ edges\ follow\ moving\ nodes}
\]

\[
\boxed{shared\ timeline\ interval\Rightarrow parallel\ execution}
\]

\[
\boxed{unsupported\ richer\ schedule\Rightarrow FAIL\ CLOSED}
\]

Rzeczywiste wykonanie ujawniło dwie granice wcześniejszego prototypu: brak relacyjnych krawędzi w filmie oraz sekwencyjne wykonywanie ruchów mających ten sam przedział czasu. F4.3 naprawił oba problemy bez zmiany semantyki: krawędzie/etykiety śledzą węzły przez `always_redraw`, a cztery `MOVE_NODE` są wykonywane równolegle w jednym `self.play(..., run_time=1.25)`.

Pierwszy realny render przeszedł technicznie, lecz autoweryfikacja klatek ujawniła niewidoczną etykietę czarnego węzła oraz kolizje etykiet relacji. Nie zamrożono tego renderu. Poprawka dodała deterministyczny kontrast tekstu oraz prostopadłe odsunięcie etykiet z tłem planszy. Najnowszy render po poprawce jest autorytatywnym świadkiem F4.3.

```text
workflow: PSI-VIZ F4.3 real Manim execution
run:      36763500447
head:     9e764cbbd728eeeffa2c9ca7a943c13e996a8b41
Manim:    0.19.0
codec:    h264
size:     854 x 480
fps:      15
frames:   25
duration: 1.666667 s
MP4 size: 44273 bytes
MP4 sha256: 1c2747cf0a56dd39a2e8a7dcaf2d16487c2e3513f093bd61a3e65864238f5ec1
```

Najnowszy job przeszedł F4.0, F4.1, F4.2, F4.3 source, rzeczywisty render Manim/FFmpeg, `ffprobe`, kontrolę pierwszej/ostatniej klatki, test reprezentacji, aktywną pamięć i konstytucję instytucji.

Artefakt:

```text
name:       psi-viz-f4.3-real-manim
artifact:   11120225172
zip sha256: 21706750037952a5987bd02a7c7bfc7f96f0513834e2ffdad2703dec8b2608bd
```

Granice pozostające po PASS:

- typografia jest prototypowa; etykiety `COMPATIBLE_WITH` w pierwszym układzie są nadal zbyt blisko siebie dla wydawniczo finalnej planszy;
- F4.3 obsługuje tylko jeden wspólny przedział ruchu;
- brak jeszcze zdarzenia semantycznego;
- cold CI Manima jest ciężkie (około 116 MB pobieranych pakietów systemowych i około 275 MB dodatkowej zajętości przed zależnościami Pythona).

Szczegóły: `docs/memory/PSI-VIZ-F4.3-01.md`.

## F4.4 — zachowana specyfikacja odroczonej jednostki

**FIRST TYPED SEMANTIC ADAPTER — SPLIT.**

Pierwszy adapter semantyczny ma materializować źródłową regułę PSI-VIZ:

```text
rozszczepienie = obserwacja rozdzielająca
```

Minimalny świadek:

1. zacząć od stanu F4.0 z kompatybilnymi `x1,x2`;
2. wprowadzić rzeczywiste, admitted zdarzenie pamięci rozdzielające jeden przypadek;
3. utworzyć nowy `VisualFrame` związany z nową rewizją i innym `semantic_digest`;
4. `AnimationTimeline` deklaruje `SPLIT`, nie `REPOSITION`;
5. adapter `SPLIT` musi otrzymać typowany diff przed/po i wykazać dokładnie, które obiekty/relacje pojawiły się, zniknęły lub zmieniły status;
6. renderer nie może wywnioskować splitu z odległości ekranowej;
7. brak zgodnego diffu albo nieoczekiwany typ zmiany => fail-closed;
8. wyrenderować krótki realny film i sprawdzić, że `semantic_digest` rzeczywiście zmienia się zgodnie ze źródłem;
9. nie uogólniać jeszcze adaptera na arbitralne `SEMANTIC_EVENT`.

Po spełnieniu powyższych bramek i F4.4 można zamknąć pierwszy pionowy przekrój PSI-VIZ: stan -> widok -> druk -> ruch reprezentacyjny -> ruch semantyczny, a następnie przejść do F5 — pomiaru skuteczności reprezentacji.