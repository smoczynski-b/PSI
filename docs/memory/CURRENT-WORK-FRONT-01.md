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
F4.2 NEXT
```

## F4.1 — wynik

Jeden zweryfikowany `VisualFrame` jest teraz źródłem dwóch reprezentacji wykonawczych bez dostępu renderera do autorytatywnego `Workspace`:

```text
VisualFrame
├─> PrintKeyframe
└─> AnimationTimeline
```

Zamrożone:

\[
\boxed{renderer\ input=checked\ VisualFrame,\ not\ authoritative\ memory}
\]

\[
\boxed{graphic\ identity\neq screen\ position}
\]

\[
\boxed{PROJECTION\ REDACTION\ survives\ rendering}
\]

`PrintKeyframe` jest neutralnym, wektorowo-bezpiecznym opisem sceny (`circle+text`, `line+text`, brak gradientów) z przypiętymi digestami źródła. Stabilny `asset_id` zależy od tożsamości obiektu/relacji, a nie od współrzędnych; dwa layouty tej samej sceny zachowują te same identyfikatory graficzne.

`AnimationTimeline` używa rygla F4.0. Dla `REPOSITION` emituje tylko `MOVE_NODE` przy identycznym `semantic_digest`. Dla rzeczywistego zdarzenia semantycznego emituje jedynie zadeklarowane `SEMANTIC_EVENT` wskazujące digest stanu przed/po; renderer nie rekonstruuje sam matematyki z geometrii.

W jednej animacji muszą pozostać stałe:

```text
task_id
visible_metadata
channel_meanings
```

Zmiana zadania albo widoczności metadanych nie może udawać zmiany pamięci. Renderer nie może odzyskać `provenance`, jeśli zostało ono usunięte na granicy F4.0.

Workflow `PSI-VIZ F4.1 outputs`, run `36759122579`, zakończył się `success`. W jednym jobie przeszły:

```text
F4.0 PSI-VIZ projection contract
F4.1 print/animation output contract
finite representation control
active memory regression
institutional constitution
```

Szczegóły: `docs/memory/PSI-VIZ-F4.1-01.md`.

## F4.2 — następna jednostka

**REAL VECTOR RENDERER + MINIMAL ANIMATION ADAPTER.**

Pierwszy rzeczywisty rendering ma zużywać wyłącznie formaty pośrednie F4.1:

```text
PrintKeyframe      -> deterministic SVG
AnimationTimeline -> minimal Manim adapter / executable scene description
```

Minimalny świadek F4.2:

1. wyrenderować scenę `Y,x1,x2,m` do prawdziwego SVG bez ponownego dostępu do `Workspace`;
2. SVG ma zawierać źródłowy `semantic_digest`, `layout_digest` i `profile_id` jako metadane;
3. wszystkie `asset_id` z `PrintKeyframe` muszą pojawić się w SVG i pozostać stabilne;
4. brak gradientów, filtrów, rastrów i ukrytych metadanych semantycznych;
5. sprawdzić deterministyczność: ten sam `PrintKeyframe` -> identyczny digest SVG;
6. przygotować minimalny adapter timeline, który mapuje `MOVE_NODE` na instrukcje Manim bez dopisywania relacji;
7. `SEMANTIC_EVENT` bez jawnego adaptera danego typu ma działać fail-closed, a nie być zgadywane;
8. klatka SVG ma być bezpiecznym źródłem dla późniejszego PDF/druku;
9. po F4.2 można wykonać rzeczywisty krótki film i dopiero potem wejść w F5 — pomiar skuteczności reprezentacji.
