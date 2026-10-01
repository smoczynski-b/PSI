# PSI-VIZ-F4.0-01 — sprawdzalna projekcja rewizji pamięci

**Status:** EXPERIMENTAL / NON-CANONICAL / CONTRACT TEST  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Source lineage:** `PSI-VIZ-LINEAGE-01` / rozmowa `Konstruowanie litery a`.  
**Does not modify:** CORE5, CANON-03, authoritative memory state.

## 1. Cel

F4.0 wprowadza minimalny kompilator widoku PSI-VIZ nad konkretnym `Workspace`.
Nie renderuje jeszcze filmu ani planszy Manim. Rozdziela najpierw to, co ma znaczenie
semantyczne, od tego, co jest wyłącznie geometrią prezentacji.

```text
Workspace revision
+ VisualContract
+ LayoutSpec
→ VisualFrame
```

`VisualFrame` zawiera dwa niezależne skróty:

```text
semantic_digest
layout_digest
```

Zatem:

\[
\boxed{\text{visual projection}\neq\text{authoritative memory}}
\]

oraz

\[
\boxed{\text{semantic layer}\neq\text{layout layer}}.
\]

## 2. Wiązanie ze źródłem

Kontrakt wizualny wskazuje dokładnie:

```text
source_contract_id
source_contract_digest
source_revision
source_state_digest
task_id
```

Stary kontrakt wizualny nie może po cichu renderować nowej rewizji pamięci.
Zmiana `revision` albo `state_digest` wymaga nowego wiązania.

## 3. Kanały wizualne

F4.0 wymaga jawnego znaczenia kanałów, np.:

```text
color      -> trwała identyfikacja obiektu/typu
symbol     -> typowana rola matematyczna
position   -> wyłącznie layout w F4.0
motion     -> jawnie zadeklarowany typ przejścia
line_style -> klasa relacji
```

Brak jawnego znaczenia nie daje prawa do inferencji z wyglądu.

W szczególności w F4.0:

\[
\boxed{\text{screen distance has no metric meaning}.}
\]

Jeśli później położenie ma kodować koszt, czas, tolerancję lub wielkość fizyczną,
kontrakt musi jawnie dodać jednostkę i regułę odwzorowania.

## 4. Dwa layouty — jeden stan

Świadek używa struktury:

```text
Y --COMPATIBLE_WITH--> x1
Y --COMPATIBLE_WITH--> x2
x1 --TASK_EQUIV--> m
x2 --TASK_EQUIV--> m
```

czyli wizualnej postaci sytuacji zgodnej z intuicją:

\[
|F(Y)|>1,\qquad |q_{\mathcal T}(F(Y))|=1.
\]

Dwa układy (`FIBRE_LAYOUT`, `QUOTIENT_LAYOUT`) mają różne współrzędne, lecz zachowują
te same obiekty, typowane relacje, provenance/status oraz wiązanie z rewizją pamięci.

Warunek:

\[
\boxed{
semantic\_digest(L_1)=semantic\_digest(L_2),\quad
layout\_digest(L_1)\neq layout\_digest(L_2)
}
\]

## 5. Ruch

F4.0 rozróżnia co najmniej dwa przypadki:

### `REPOSITION`

Zmiana wyłącznie layoutu:

```text
semantic_changed = false
layout_changed   = true
```

Jest legalna i nie może być przedstawiana jako zmiana wiedzy.

### zdarzenie semantyczne (`EDGE_ADD`, `EDGE_REMOVE`, `STATUS_CHANGE`, ...)

Musi mieć:

```text
semantic_changed = true
```

Próba animowania `EDGE_ADD` przy niezmienionym stanie jest błędem kontraktu.

## 6. Ograniczenie ujawnienia

`visible_metadata` jest częścią kontraktu wizualnego. F4.0 dopuszcza jawne pola:

```text
provenance
status
```

Jeżeli odbiorca/widok nie ma prawa do `provenance`, kompilator usuwa to pole z
warstwy semantycznej. Nie wolno kodować ukrytej wartości kolorem, położeniem,
tooltipem ani innym kanałem bocznym.

\[
\boxed{\text{redaction}\neq\text{visual hiding only}.}
\]

## 7. Kontrole negatywne

Regresja wymusza:

1. dokładne wiązanie do rewizji i digestu pamięci;
2. pełną zgodność zbioru węzłów layoutu z widokiem;
3. brak zmiany `semantic_digest` przy samym przesunięciu;
4. brak fałszywego zdarzenia semantycznego przy samym przesunięciu;
5. zmianę `semantic_digest` po rzeczywistym `EDGE_UPSERT`;
6. usunięcie `provenance` w kontrakcie ograniczonym.

## 8. Granica F4.0

To jeszcze nie dowodzi, że grafika poprawia rozumowanie agenta ani człowieka.
Nie ma też eksportu SVG/PDF/MP4 ani silnika Manim.

F4.0 daje wyłącznie sprawdzalny **scene contract** nad pamięcią.

Następny krok F4.1 powinien użyć tego samego `VisualFrame` do dwóch wyjść:

```text
print keyframe (SVG/PDF-safe scene description)
animation timeline (Manim adapter)
```

bez ponownego definiowania semantyki w rendererze.
