# PSI-MEMORY-M13-TASK-CONTRACT-01 — natural task to retrieval contract

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can a plain Polish task instruction be compiled into the typed retrieval contract used by M12, without a hand-written per-task TSV and without silently broadening ambiguous requests?

The target form is:

\[
\boxed{
\text{TASK}
\longrightarrow
\mathcal T=(a,I,R,\pi,B,S)
}
\]

where:

- \(a\) — anchor;
- \(I\) — recognized task intents;
- \(R\) — allowed relation policy;
- \(\pi\) — expansion/terminal semantics and priorities;
- \(B\) — context edge budget;
- \(S\) — stop condition.

## 1. Frozen witness

Primary natural task:

> `sprawdź przesłanki dowodu II.9 i jego granice`

A paraphrase is also frozen:

> `dla II.9 pokaż zależności dowodowe oraz czego twierdzenie nie implikuje`

Both must compile to the same contract previously written manually for M12:

- `HARD_DEPENDS_ON` — expand;
- `USES_DEFINITION` — expand;
- `USES_LEMMA` — expand;
- `NOT_DEPENDS_ON` — terminal;
- `DOES_NOT_IMPLY` — terminal;
- anchor `II.9`;
- local radius `2`;
- edge budget `12`.

The resulting selected relation set must equal the manually contracted M12 selection.

## 2. Narrowing witness

Task:

> `pokaż tylko przesłanki dowodowe II.9`

must compile only the proof-prerequisite family. It must not inherit boundary relations merely because they are nearby and validly mapped.

## 3. Negative controls

Two failure modes are deliberate:

### Ambiguous intent

> `opisz II.9`

must yield:

\[
\boxed{\mathrm{NEEDS\_CONTRACT}}
\]

and `NO_RETRIEVAL`.

### Missing anchor

> `sprawdź przesłanki dowodu`

must yield:

\[
\boxed{\mathrm{NEEDS\_ANCHOR}}
\]

and `NO_RETRIEVAL`.

Thus uncertainty causes a stop, not broad context expansion.

## 4. Compiler boundary

`M13-LEXICAL-01` is deliberately deterministic and narrow. It uses a frozen Polish lexical map for two task intents:

- `PROOF_PREREQUISITE`;
- `BOUNDARY`.

It is not presented as general natural-language understanding, semantic parsing, or an optimal task compiler.

The experiment tests architecture:

\[
\boxed{\text{recognized task semantics}\to\text{explicit executable retrieval contract}.}
\]

## 5. Success predicates

M13 passes iff:

1. the two paraphrases compile identically;
2. the compiled combined contract reproduces the manual M12 policy and selected 12-edge view;
3. the proof-only request yields a strict subset with no boundary relations;
4. ambiguous intent yields no retrieval;
5. missing anchor yields no retrieval.
