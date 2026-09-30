# PSI-VIZ-F4.3-01 — pierwszy rzeczywisty film Manim

**Status:** EXPERIMENTAL / NON-CANONICAL / PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Depends on:** F4.0 scene contract, F4.1 output contract, F4.2 SVG/Manim renderer.  
**Does not modify:** CORE5, CANON-03, authoritative memory state, live FORUM gateway.

## 1. Cel

F4.3 wykonuje po raz pierwszy rzeczywistą animację PSI-VIZ w Manimie, zamiast jedynie generować plan lub skrypt.

Świadek pozostaje celowo czysto reprezentacyjny:

```text
FIBRE_LAYOUT
    -> REPOSITION
QUOTIENT_LAYOUT
```

przy niezmienionym stanie semantycznym.

\[
\boxed{semantic\_digest_{before}=semantic\_digest_{after}}
\]

oraz

\[
\boxed{layout\_digest_{before}\neq layout\_digest_{after}}.
\]

Nie występuje jeszcze żadne zdarzenie semantyczne.

## 2. Scena

Widoczny graf ma cztery obiekty i cztery relacje:

```text
Y  --COMPATIBLE_WITH--> x1
Y  --COMPATIBLE_WITH--> x2
x1 --TASK_EQUIV-------> m
x2 --TASK_EQUIV-------> m
```

co odpowiada wizualnemu świadkowi intuicji:

\[
|F(Y)|>1,\qquad |q_{\mathcal T}(F(Y))|=1.
\]

Film nie odczytuje `Workspace`. Jego źródłem pozostaje sprawdzony łańcuch:

```text
VisualFrame
-> PrintKeyframe + AnimationTimeline
-> ManimPlan
-> executable Manim scene
-> MP4
```

## 3. Korekta wykonawcza ujawniona przez F4.3

Przejście od planu do rzeczywistego filmu ujawniło dwie granice wcześniejszego prototypu.

### 3.1 Krawędzie muszą uczestniczyć w ruchu

Pierwotny skrypt F4.2 przesuwał węzły, ale nie materializował relacyjnych krawędzi w filmie. F4.3 dodaje więc typowane krawędzie i etykiety jako obiekty prezentacyjne śledzące końce przez `always_redraw`.

Nie tworzy to nowych relacji:

\[
\boxed{edge\ display\ follows\ relation;\ display\ does\ not\ create\ relation}.
\]

### 3.2 Wspólny przedział czasu oznacza ruch równoległy

`AnimationTimeline` F4.1 zapisywał cztery `MOVE_NODE` z tym samym przedziałem czasu. Generyczny skrypt F4.2 wykonywał je kolejno, co zmieniało czasową realizację widoku.

F4.3 wykonuje wszystkie cztery ruchy w jednym:

```text
self.play(move_1, move_2, move_3, move_4, run_time=1.25)
```

Richer schedule nie jest zgadywany. Jeżeli akcje nie mają jednego wspólnego przedziału, F4.3 działa fail-closed przez `UnsupportedTimelineSchedule`.

## 4. Autoweryfikacja wizualna i poprawka czytelności

Pierwszy realny render przeszedł test techniczny, lecz kontrola klatek ujawniła:

1. niewidoczną etykietę czarnego węzła `x1`;
2. nakładające się etykiety relacji.

Nie uznano więc pierwszego renderu za końcowe świadectwo F4.3.

Poprawka wykonawcza, bez zmiany semantyki:

- kolor tekstu węzła jest wybierany deterministycznie z kontrastu luminancji wypełnienia;
- ciemne wypełnienie otrzymuje jasny tekst;
- etykieta relacji jest odsuwana prostopadle od krawędzi;
- strona odsunięcia jest deterministyczna;
- etykieta ma tło koloru planszy (`BackgroundRectangle`), aby zachować czytelność podczas ruchu.

Regresja zamraża te własności jako `legibility_guards`.

Po poprawce kontrola pierwszej i ostatniej klatki potwierdziła widoczność wszystkich czterech węzłów i czytelność typowanych relacji. Pozostaje granica typograficzna: w `FIBRE_LAYOUT` dwie etykiety `COMPATIBLE_WITH` są nadal zbyt blisko siebie, aby uznać planszę za finalny materiał wydawniczy. Jest to wada składu, nie błąd semantyczny.

## 5. Wynik rzeczywistego renderu

Autorytatywny dla F4.3 jest **najnowszy** workflow po poprawce czytelności:

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
```

MP4:

```text
sha256 = 1c2747cf0a56dd39a2e8a7dcaf2d16487c2e3513f093bd61a3e65864238f5ec1
```

Klatki kontrolne:

```text
first-frame.png sha256 = 1fe594ebce6c3d48156df1bbdde80164311157ea20cfdf5084affb151d728ff5
last-frame.png  sha256 = 31ac3235e2eb5b893955afddbc516ab2fd32e81f6b3f90426d1d5b8ffc1a0be8
```

Skróty są różne, więc klatka początkowa i końcowa nie są identyczne.

Źródło wykonawcze:

```text
scene_source_digest = 3bc309b7e6fe92d897ef4450f901e585e3d45ac854ab376c93579bc14ad20ccf
semantic_digest     = eda5671f52a14874efec95808fb8e286551ff9a307036bc2f4eff8406f2316af
```

Manifest potwierdza:

```text
semantic_change = false
motion          = REPOSITION
visible_nodes   = 4
visible_edges   = 4
```

## 6. Regresje

Najnowszy run przeszedł w jednym jobie:

```text
F4.0 projection contract
F4.1 output contract
F4.2 renderer contract
F4.3 executable scene source
Manim runtime installation
real MP4 rendering
ffprobe / frame verification
finite representation control
active memory regression
institutional constitution
artifact upload
```

W szczególności:

```text
semantic_digest_invariant=PASS
parallel_timeline_execution=PASS
typed_edges_follow_nodes=PASS
renderer_has_no_workspace_access=PASS
projection_redaction_survives_scene_source=PASS
unsupported_schedule_fail_closed=PASS
legibility_guards=PASS
real_mp4=PASS
```

## 7. Artefakt CI

Najnowszy artefakt:

```text
name:      psi-viz-f4.3-real-manim
artifact:  11120225172
zip size:  204648 bytes
zip sha256: 21706750037952a5987bd02a7c7bfc7f96f0513834e2ffdad2703dec8b2608bd
```

Zawiera m.in.:

```text
psi-viz-reposition.mp4
first-frame.png
last-frame.png
fibre-keyframe.svg
quotient-keyframe.svg
reposition-plan.json
reposition-scene.py
manifest.json
video-probe.json
render-digests.txt
```

## 8. Granica kosztu wykonawczego

Cold CI dla Manima jest obecnie ciężkie: instalacja systemowa pobiera około 116 MB pakietów i zwiększa zajętość środowiska o około 275 MB, następnie instalowany jest `manim==0.19.0` wraz z zależnościami Pythona.

To jest koszt infrastruktury renderującej, nie koszt semantycznego `REPOSITION`.

\[
\boxed{render\ environment\ cost\neq semantic\ operation\ cost}.
\]

Cache/kontener mogą być późniejszą optymalizacją. Nie należy mieszać jej z implementacją pierwszego zdarzenia semantycznego.

## 9. Status

\[
\boxed{F4.3=PASS\_WITH\_BOUNDARY}
\]

PASS oznacza: istnieje realny, zweryfikowany MP4 zachowujący semantyczną niezmienniczość podczas zmiany layoutu.

Boundary oznacza:

- renderer obsługuje tylko prosty wspólny przedział `MOVE_NODE`;
- brak jeszcze typowanego adaptera zdarzenia semantycznego;
- typografia etykiet jest prototypowa, nie wydawniczo finalna;
- cold CI jest kosztowne.

Następny krok F4.4: pierwszy **typowany adapter semantyczny**. Naturalnym kandydatem jest `SPLIT`, ponieważ w rodowodzie PSI-VIZ rozszczepienie odpowiada obserwacji rozdzielającej; jego implementacja musi być związana z rzeczywistą zmianą stanu/digestu, a nie z samą geometrią.
