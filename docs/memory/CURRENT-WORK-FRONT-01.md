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
F3.2 NEXT
```

## F3.1 — wynik

Referencyjny runtime archiwum potwierdza:

```text
base snapshot
+ ordered deltas
+ version manifest
+ content digest
+ append-only CURRENT_POINTER
→ deterministic reconstruction
→ restart/replay
```

Zamrożone rozróżnienia:

\[
\boxed{CURRENT\neq TRUE\neq REUSABLE}
\]

\[
\boxed{RESTORE\_CANDIDATE\neq ADMIT}
\]

\[
\boxed{manifest\neq reconstructed\ state}
\]

Jedna baza może obsługiwać wiele wersji bez pełnej kopii snapshotu na każdą wersję. `NEEDS_RECHECK` przeżywa archiwizację i restart. Brak delty, mismatch digestu, kolizja `version_id`, błędny pointer i brak autoryzowanego runbooku działają fail-closed.

Workflow `PSI memory archive runtime`, run `36748602618`, zakończył się `success`; ponownie przeszedł także F3.0, regresja Sługi i konstytucja instytucji.

## F3.2 — następna jednostka

**L2 USAGE / MOVEMENT ARCHIVE INTEGRATION.**

Połączyć archiwum z istniejącym `ACCESS_STEWARD` tak, aby L2 przechowywało referencje do historii użycia bez omijania ograniczeń telemetrii.

Minimalny świadek:

1. sesja legalnie wchodzi do `map:alpha`, przechodzi do `map:beta` i wychodzi;
2. Nadzorca zapisuje koszt i typed movement telemetry;
3. Kustosz archiwizuje wersje obu map;
4. L2 zapisuje tylko identyfikatory/referencje do właściwych rekordów ruchu i kosztów;
5. `T1_SECURITY_RESTRICTED` / `T2_AUDIT_DURABLE` nie stają się publiczne przez L2;
6. po restarcie można wykazać: jaka wersja mapy była używana, przez jakie legalne przejście, przy jakim koszcie, bez kopiowania pełnej telemetrii;
7. brak `VIEW_TELEMETRY` blokuje materializację treści ograniczonej, ale nie niszczy audytowego odwołania;
8. L2 nie zmienia statusu epistemicznego mapy i nie stanowi dowodu prawdy.

Dopiero po F3.2 należy rozstrzygnąć, czy F3 wymaga jeszcze runtime planistycznego Kustosza przed przejściem do F4/PSI-VIZ.
