# PSI-VIZ-F4.1-01 — jedno źródło sceny, klatka drukowa i oś animacji

**Status:** EXPERIMENTAL / NON-CANONICAL / OUTPUT CONTRACT TEST  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Depends on:** `PSI-VIZ-F4.0-01`  
**Does not modify:** CORE5, CANON-03, authoritative memory state.

## 1. Cel

F4.1 sprawdza, czy jeden już zweryfikowany `VisualFrame` może być źródłem dwóch
wyjść wykonawczych bez ponownego definiowania matematyki w rendererze:

```text
VisualFrame
├─> PrintKeyframe      (wektorowo-bezpieczny opis planszy)
└─> AnimationTimeline (deklaratywne polecenia dla przyszłego adaptera Manim)
```

Renderer nie otrzymuje `Workspace`. Otrzymuje wyłącznie `VisualFrame`, a więc już
przefiltrowany stan F4.0.

\[
\boxed{renderer\ input = checked\ visual\ projection,\ not\ authoritative\ memory}
\]

## 2. Klatka drukowa

`compile_print_keyframe(frame, profile)` tworzy neutralny opis wektorowy:

```text
canvas
nodes: circle + text
edges: line + text
stable asset ids
source digests
```

W F4.1 nie generujemy jeszcze binarnego SVG/PDF. Pole `vector_safe=true` oznacza,
że scena używa wyłącznie prymitywów możliwych do bezpośredniego odwzorowania na
SVG/PDF; gradienty są zakazane.

Profil roboczy odpowiada rodowodowi Byrne/PSI:

```text
ivory background
black foreground
red / blue / gold / black identity palette
serif typography
large margins
```

Kolor jest stabilnym identyfikatorem obiektu w obrębie profilu. Nie jest
wnioskowany z położenia.

## 3. Stabilna tożsamość graficzna

Każdy węzeł i krawędź dostaje deterministyczny `asset_id` zależny od identyfikatora
obiektu/relacji, nie od współrzędnych ekranu.

Dla dwóch layoutów tego samego stanu:

\[
asset\_id_{L_1}(x)=asset\_id_{L_2}(x),
\]

podczas gdy współrzędne i `payload_digest` planszy mogą się zmienić.

To realizuje zasadę z `Konstruowanie litery a`:

\[
\boxed{symbol\ matematyczny = ten\ sam\ obiekt\ graficzny\ w\ całym\ wywodzie}.
\]

## 4. Oś animacji

`compile_animation_timeline(before, after, motion)` nie interpretuje matematyki
na podstawie geometrii. Najpierw używa rygla F4.0 `classify_transition(...)`.

Dla `REPOSITION`:

```text
semantic_digest before == semantic_digest after
layout_digest before   != layout_digest after
```

powstają wyłącznie polecenia:

```text
MOVE_NODE(asset_id, from, to, t0, t1)
```

Dla zdarzenia semantycznego (`EDGE_ADD`, `EDGE_REMOVE`, ...), F4.1 nie próbuje
samodzielnie rekonstruować znaczenia zmiany. Emituje tylko zatwierdzone:

```text
SEMANTIC_EVENT(
  declared_motion,
  from_semantic_digest,
  to_semantic_digest,
  t0,
  t1
)
```

Szczegółowy sposób animowania takiego zdarzenia należy do późniejszego adaptera,
ale adapter nie może dopisać nowej semantyki.

## 5. Niezmienność kontraktu podczas animacji

Zmiana `semantic_digest` może wynikać również ze zmiany samego kontraktu widoku.
Dlatego F4.1 wymaga podczas jednej animacji stałości:

```text
task_id
visible_metadata
channel_meanings
```

Zmiana zadania albo nagłe ujawnienie provenance nie może udawać `EDGE_ADD`.

## 6. Redakcja

F4.1 nie ma dostępu do `Workspace`, więc nie może odzyskać metadanych usuniętych
przez F4.0. Jeśli `VisualFrame` nie zawiera `provenance`, nie pojawi się ono ani w
planszy drukowej, ani w osi animacji.

\[
\boxed{redaction\ at\ projection\ boundary\ survives\ rendering.}
\]

## 7. Świadek

Używamy tej samej struktury co F4.0:

```text
Y --COMPATIBLE_WITH--> x1
Y --COMPATIBLE_WITH--> x2
x1 --TASK_EQUIV--> m
x2 --TASK_EQUIV--> m
```

Dwa layouty (`FIBRE_LAYOUT`, `QUOTIENT_LAYOUT`) generują:

1. dwie różne klatki drukowe o tych samych `asset_id`;
2. legalną oś `REPOSITION`;
3. po rzeczywistym `EDGE_UPSERT` — legalne `SEMANTIC_EVENT(EDGE_ADD)` dopiero z
   nowego, poprawnie związanego `VisualFrame`.

## 8. Granica F4.1

F4.1 nie generuje jeszcze pliku SVG/PDF ani filmu MP4. Nie uruchamia Manima.
Potwierdza format pośredni, na którym można oprzeć oba renderery bez powielania
semantyki.

Następny krok F4.2 powinien wykonać **pierwszy rzeczywisty renderer wektorowy**
(SVG jako źródło drukowe/PDF-safe) i prosty adapter Manim lub równoważny odczyt
timeline, przy zachowaniu digestów F4.0/F4.1.
