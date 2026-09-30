# CURRENT-WORK-FRONT-01

**Status:** EXPERIMENTAL / NON-CANONICAL / CURRENT POINTER  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Supersedes only:** historical `NEXT` prose in `WORK-FRONT-GPT5-01.md`.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## Stan

```text
F0   PASS_WITH_BOUNDARY
F1   PASS_WITH_BOUNDARY
F2.0 CONTRACT_PASS
F2.1 PASS_WITH_BOUNDARY
F3.0 CONTRACT_PASS
F3.1 PASS_WITH_BOUNDARY
F3.2 PASS_WITH_BOUNDARY
F3.3 PASS_WITH_BOUNDARY
F3   FUNCTIONALLY_CLOSED_REFERENCE_LEVEL
F4.0 CONTRACT_PASS
F4.1 PASS_WITH_BOUNDARY
F4.2 PASS_WITH_BOUNDARY
F4.3 NEXT
```

## F4.2 — wynik

Pierwszy rzeczywisty renderer PSI-VIZ działa wyłącznie nad formatami pośrednimi F4.1:

```text
PrintKeyframe -> deterministic SVG
PrintKeyframe + AnimationTimeline -> ManimPlan -> executable Python (REPOSITION)
```

Zamrożone:

\[
\boxed{renderer\not\to Workspace}
\]

\[
\boxed{same\ PrintKeyframe\Rightarrow same\ SVG\ bytes\ and\ digest}
\]

\[
\boxed{unknown\ semantic\ event\Rightarrow FAIL\ CLOSED}
\]

SVG używa wyłącznie prymitywów wektorowych `rect/line/circle/text/g/metadata`; bez rastrów, filtrów i gradientów. Binding metadata zawiera wyłącznie identyfikatory kontrolne (`semantic_digest`, `layout_digest`, `profile_id`, `print_payload_digest`, kontrakt/zadanie/rewizję/digest źródła), a nie ukrytą kopię relacji, provenance ani statusu.

W regresji kontrakt F4.0 celowo ukrywa `provenance`; ciągi `source:fibre` i `source:quotient` nie pojawiają się ani w SVG, ani w skrypcie Manim. Jawny `status` pozostaje widoczny, bo był dopuszczony w `VisualFrame`.

Adapter Manim mapuje wyłącznie `MOVE_NODE -> ANIMATE_MOVE_TO`. `SEMANTIC_EVENT` bez jawnego adaptera jest odrzucany. Nawet po podaniu identyfikatora adaptera generyczny renderer F4.2 nie wykonuje zdarzenia semantycznego: jego implementacja wymaga osobnej regresji.

Workflow `PSI-VIZ F4.2 renderer`, run `36760676294`, zakończył się `success`; w jednym jobie przeszły:

```text
F4.0 projection contract
F4.1 output contract
F4.2 SVG + Manim renderer
finite representation control
active memory regression
institutional constitution
```

Workflow opublikował realny artefakt `psi-viz-f4.2-render` zawierający:

```text
fibre-keyframe.svg
reposition-plan.json
reposition-scene.py
manifest.json
```

Szczegóły: `docs/memory/PSI-VIZ-F4.2-01.md`.

## F4.3 — następna jednostka

**EXECUTE THE FIRST MANIM REPOSITION FILM.**

Minimalny świadek:

1. użyć dokładnie `reposition-scene.py` wygenerowanego przez F4.2;
2. zainstalować/uruchomić Manim w izolowanym jobie CI i wyrenderować krótki MP4 dla `FIBRE_LAYOUT -> QUOTIENT_LAYOUT`;
3. film nie może czytać `Workspace` ani modyfikować planu;
4. zachować manifest z digestem planu i pliku źródłowego;
5. klatka początkowa/końcowa ma zachować te same `asset_id`/etykiety/kolory;
6. F4.3 nadal dotyczy wyłącznie `REPOSITION` — bez zdarzenia semantycznego;
7. dopiero po PASS filmu przygotować pierwszy jawny adapter semantyczny (`SPLIT` albo `EDGE_ADD`), a później wejść w F5 — pomiar skuteczności reprezentacji.
