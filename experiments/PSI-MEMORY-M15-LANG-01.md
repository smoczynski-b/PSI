# PSI-MEMORY-M15-LANG-01 — language invariance over a relational memory

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can different human-language surfaces compile to the same retrieval contract and the same relational task view without forcing lexical categories themselves to be identical?

The target distinction is:

\[
\boxed{\text{language surface}\neq\text{memory relation structure}.}
\]

For equivalent task formulations in Polish, English and German, M15 requires:

\[
\operatorname{Sig}(\operatorname{Compile}_{PL}(u_{PL}))
=
\operatorname{Sig}(\operatorname{Compile}_{EN}(u_{EN}))
=
\operatorname{Sig}(\operatorname{Compile}_{DE}(u_{DE})),
\]

and then:

\[
\mathfrak R_{\mathcal T_{PL}}(\mathcal M)
=
\mathfrak R_{\mathcal T_{EN}}(\mathcal M)
=
\mathfrak R_{\mathcal T_{DE}}(\mathcal M).
\]

The equality is over executable contract structure and selected graph edges, not over strings.

## 1. Task-language witnesses

Broad task:

- PL: `sprawdź przesłanki dowodu II.9 i jego granice`;
- EN: `check the proof prerequisites of II.9 and its boundaries`;
- DE: `prüfe die Beweisvoraussetzungen von II.9 und seine Grenzen`.

Strict boundary task:

- PL: `dla II.9 pokaż granice, tylko pełne certyfikaty`;
- EN: `for II.9 show boundaries, only full certificates`;
- DE: `für II.9 zeige Grenzen, nur vollständige Zertifikate`.

A language without an installed adapter is a fail-closed control and must return `NEEDS_LANGUAGE_ADAPTER / NO_RETRIEVAL`.

## 2. Denotation witness

M15 deliberately refuses the stronger and generally false assumption

\[
\text{lexical scope}_{PL}=\text{lexical scope}_{EN}=\text{lexical scope}_{DE}.
\]

The frozen toy lexicon uses:

- PL `zegarek` -> `OBJ-WRIST`;
- EN `watch` -> `OBJ-WRIST`;
- DE `Uhr` -> `{OBJ-WRIST, OBJ-WALL}`;
- DE `Armbanduhr` -> `OBJ-WRIST`.

The world-relation fixture contains, independently of those lexical labels:

\[
OBJ\!\!-
WRIST\xrightarrow{MEASURES}TIME,
\qquad
OBJ\!\!-
WALL\xrightarrow{MEASURES}TIME,
\]

and

\[
OBJ\!\!-
WRIST\xrightarrow{ATTACHED\_TO}WRIST,
\qquad
OBJ\!\!-
WALL\xrightarrow{ATTACHED\_TO}WALL.
\]

Therefore the relation `MEASURES TIME` does not distinguish the two German candidates, while `ATTACHED_TO WRIST` does.

This expresses the intended architecture:

\[
\boxed{\text{lexical fibre}\xrightarrow{\text{world relations}}\text{task-relevant identification}.}
\]

## 3. Success conditions

M15 passes iff:

1. PL/EN/DE broad tasks compile to identical executable signatures;
2. they retrieve the same 12-edge graph;
3. PL/EN/DE strict-boundary tasks retrieve the same 4 fragment-certified edges;
4. an unsupported language adapter fails closed;
5. German `Uhr` remains lexically ambiguous before relational grounding;
6. the shared relation `MEASURES TIME` does not falsely collapse that ambiguity;
7. the discriminating relation `ATTACHED_TO WRIST` reduces the German candidate set to `OBJ-WRIST`, matching PL `zegarek` and EN `watch`.

## 4. Boundary

M15 does not claim general multilingual language understanding, universal ontology, or language-independent perception of the world. The three adapters and the denotation fixture are frozen test harnesses.

The experiment tests an architectural invariant: **memory identity and retrieval need not be tied to one natural-language partition of concepts**. Human language may provide different lexical fibres over a shared relational substrate; unresolved lexical differences must remain unresolved until task-relevant relations actually distinguish them.
