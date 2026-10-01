# PSI-VIZ-F4.2-01 — rzeczywisty SVG i minimalny adapter Manim

**Status:** EXPERIMENTAL / NON-CANONICAL / RENDERER TEST  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Depends on:** `PSI-VIZ-F4.0-01`, `PSI-VIZ-F4.1-01`.  
**Does not modify:** CORE5, CANON-03, authoritative memory state.

## 1. Cel

F4.2 materializuje pierwsze rzeczywiste wyjścia PSI-VIZ bez przywracania rendererowi dostępu do `Workspace`:

```text
PrintKeyframe      -> deterministic SVG
PrintKeyframe
+ AnimationTimeline -> ManimPlan -> executable Manim Python (REPOSITION only)
```

Renderer przyjmuje wyłącznie sprawdzone formaty pośrednie F4.1.

\[
\boxed{renderer\not\to Workspace}
\]

## 2. SVG

`render_svg(PrintKeyframe)` generuje zwykły SVG 1.1/2-compatible XML z prymitywów:

```text
rect
line
circle
text
g
metadata
```

Nie występują:

```text
image
filter
linearGradient
radialGradient
data:image/*
```

Klatka zawiera jako binding metadata wyłącznie identyfikatory kontrolne:

```text
semantic_digest
layout_digest
profile_id
print_payload_digest
visual_contract_id
task_id
source_revision
source_state_digest
```

Relacje, status i provenance nie są kopiowane do ukrytego bloku metadata. Jeśli były legalnie widoczne już w `PrintKeyframe`, mogą wystąpić wyłącznie jako jawne elementy sceny. Jeśli zostały usunięte na granicy F4.0, renderer ich nie odtwarza.

Każdy obiekt zachowuje dokładny `asset_id` jako `data-asset-id`.

## 3. Determinizm

Dla identycznego `PrintKeyframe`:

\[
SVG(K)=SVG(K)
\]

bajt w bajt, a więc także:

\[
SHA256(SVG_1)=SHA256(SVG_2).
\]

Nie jest to twierdzenie o równoważności wszystkich rendererów SVG; dotyczy referencyjnego renderera F4.2.

## 4. Manim

F4.2 rozdziela:

```text
AnimationTimeline -> ManimPlan
ManimPlan          -> Python scene
```

`MOVE_NODE` ma mechaniczne tłumaczenie:

```text
MOVE_NODE(asset, from, to, t0, t1)
-> ANIMATE_MOVE_TO(asset, to, duration)
```

Skrypt Manim zachowuje stabilne `asset_id`, etykiety i kolory z `PrintKeyframe`; nie importuje ani nie rekonstruuje `Workspace`.

## 5. Rygiel zdarzeń semantycznych

Ogólny renderer F4.2 **nie interpretuje** `SEMANTIC_EVENT`.

\[
\boxed{unknown\ semantic\ event\Rightarrow FAIL\ CLOSED}
\]

`compile_manim_plan` może zaakceptować wyłącznie jawnie przekazany identyfikator typowanego adaptera, np. `EDGE_ADD -> psi_edge_add_v1`, ale generyczny `render_manim_python` nadal odmawia wykonania takiego planu. Rzeczywista implementacja `EDGE_ADD`, `COLLAPSE`, `SPLIT` itd. wymaga osobnego adaptera z własną regresją.

## 6. Świadek

Regresja używa tej samej sceny:

```text
Y --COMPATIBLE_WITH--> x1
Y --COMPATIBLE_WITH--> x2
x1 --TASK_EQUIV--> m
x2 --TASK_EQUIV--> m
```

i przejścia `FIBRE_LAYOUT -> QUOTIENT_LAYOUT`.

Wszystkie cztery węzły mają jawne `from/to`, więc referencyjny skrypt Manim nie musi zgadywać pozycji początkowej żadnego obiektu.

Kontrola źródła jest ograniczona do `status`; `provenance` (`source:fibre`, `source:quotient`) nie może pojawić się ani w SVG, ani w skrypcie Manim.

## 7. Artefakty CI

Test zapisuje:

```text
build/psi-viz-f4.2/fibre-keyframe.svg
build/psi-viz-f4.2/reposition-plan.json
build/psi-viz-f4.2/reposition-scene.py
build/psi-viz-f4.2/manifest.json
```

Workflow publikuje ten katalog jako artefakt `psi-viz-f4.2-render`.

## 8. Granica F4.2

F4.2 daje rzeczywisty SVG oraz syntaktycznie wykonywalny skrypt Manim dla `REPOSITION`, ale CI nie renderuje jeszcze MP4 przez zainstalowany silnik Manim. Nie istnieje jeszcze adapter semantyczny dla `EDGE_ADD/SPLIT/COLLAPSE`.

Następna jednostka powinna być mała: uruchomić Manim na artefakcie `REPOSITION` i uzyskać pierwszy krótki film, a następnie przygotować pierwszy jawny adapter semantyczny (najlepiej `SPLIT` lub `EDGE_ADD`) z kontrolą przed/po.
