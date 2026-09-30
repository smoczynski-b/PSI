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
F4.1 NEXT
```

## F4.0 — wynik

Powstał minimalny kompilator `Workspace + VisualContract + LayoutSpec -> VisualFrame`, który jawnie rozdziela:

```text
semantic_layer / semantic_digest
layout_layer   / layout_digest
```

Zamrożone:

\[
\boxed{visual\ projection\neq authoritative\ memory}
\]

\[
\boxed{semantic\ layer\neq layout\ layer}
\]

\[
\boxed{screen\ distance\ has\ no\ metric\ meaning\ in\ F4.0}
\]

Świadek wykorzystuje strukturę odpowiadającą intuicji `|F(Y)|>1` przy `|q_T(F(Y))|=1`: dwa kompatybilne obiekty `x1,x2` schodzą do tego samego obiektu zadaniowego `m`. Dwa różne layouty (`FIBRE_LAYOUT`, `QUOTIENT_LAYOUT`) zachowują identyczny `semantic_digest`, a mają różne `layout_digest`.

`REPOSITION` jest legalne tylko wtedy, gdy zmienia się layout bez zmiany semantycznej. Zdarzenie takie jak `EDGE_ADD` wymaga rzeczywistej zmiany `semantic_digest`. Stary kontrakt wizualny nie może po cichu renderować nowej rewizji pamięci.

`visible_metadata` jest częścią kontraktu: ograniczony widok usuwa `provenance` z payloadu zamiast ukrywać je jedynie graficznie. Layout musi zawierać dokładnie zbiór widocznych węzłów — ciche zniknięcie obiektu jest błędem.

Workflow `PSI-VIZ F4.0 contract`, run `36758342287`, zakończył się `success`. W tym samym jobie przeszły:

```text
F4.0 PSI-VIZ projection contract
finite representation control
active memory regression
institutional constitution
```

Pierwszy run F4.0 ujawnił wyłącznie błąd konfiguracji CI (`fetch-depth: 1`) dla historycznie przypiętego testu reprezentacji; po ustawieniu `fetch-depth: 0` ten sam test przeszedł bez zmiany kodu F4.0.

Szczegóły: `docs/memory/PSI-VIZ-F4.0-01.md`.

## F4.1 — następna jednostka

**PRINT KEYFRAME + ANIMATION TIMELINE FROM THE SAME VISUALFRAME.**

Nie wolno ponownie definiować semantyki w rendererze. Jeden `VisualFrame` ma kompilować się do dwóch reprezentacji wykonawczych:

```text
VisualFrame
├─> print scene description (SVG/PDF-safe geometry + labels)
└─> animation timeline (Manim-ready declarative events)
```

Minimalny świadek F4.1:

1. wykorzystać dokładnie scenę F4.0 `Y,x1,x2,m`;
2. wygenerować statyczną klatkę kluczową w stylu PSI/Byrne bez gradientów i poświaty;
3. wygenerować deklaratywną sekwencję `REPOSITION`, a następnie rzeczywiste zdarzenie semantyczne;
4. ten sam `semantic_digest` ma być zapisany w klatce drukowej i osi animacji;
5. identyfikatory obiektów, kolory/symbole i typy relacji mają być stabilne między klatkami;
6. renderer nie może dodawać relacji ani metadanych nieobecnych w `VisualFrame`;
7. klatka statyczna ma być wektorowo eksportowalna, a timeline możliwy do podania do Manima bez ręcznego przepisywania matematyki;
8. kontrola ujemna: zmiana współrzędnych nie może stworzyć semantycznego eventu, a ukryte `provenance` nie może pojawić się w eksporcie.

Po F4.1 można przejść do rzeczywistego renderera/filmu i następnie do F5 — pomiaru skuteczności reprezentacji.
