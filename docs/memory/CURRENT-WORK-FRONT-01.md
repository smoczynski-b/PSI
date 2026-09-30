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
F4.3 PASS_WITH_BOUNDARY
F4.4 NEXT
```

## F4.3 — wynik

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

## F4.4 — następna jednostka

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

Po F4.4 można zamknąć pierwszy pionowy przekrój PSI-VIZ: stan -> widok -> druk -> ruch reprezentacyjny -> ruch semantyczny, a następnie przejść do F5 — pomiaru skuteczności reprezentacji.
