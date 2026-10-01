# PSI-MEMORY-M15-LANG-RESULT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36632409346` executed M1–M15 successfully.

M15 tests whether human-language variation can be kept outside the identity of the relational memory object.

For the frozen broad task, Polish, English and German formulations compiled to the same executable contract and selected exactly the same 12-edge task graph:

\[
\boxed{
\operatorname{Sig}(\operatorname{Compile}_{PL}(u_{PL}))
=
\operatorname{Sig}(\operatorname{Compile}_{EN}(u_{EN}))
=
\operatorname{Sig}(\operatorname{Compile}_{DE}(u_{DE}))
}
\]

and

\[
\boxed{
\mathfrak R_{\mathcal T_{PL}}(\mathcal M)
=
\mathfrak R_{\mathcal T_{EN}}(\mathcal M)
=
\mathfrak R_{\mathcal T_{DE}}(\mathcal M).
}
\]

The same invariant held in strict evidence mode: all three languages selected the same four fragment-certified boundary edges.

## 2. Fail-closed language boundary

A French fixture was intentionally supplied without an installed M15 adapter.

The compiler returned:

\[
\boxed{\mathrm{NEEDS\_LANGUAGE\_ADAPTER}\to\mathrm{NO\_RETRIEVAL}.}
\]

The system does not guess a contract from an unsupported language surface.

## 3. Lexical scopes are not forced to coincide

M15 deliberately rejects the stronger claim that corresponding words in different languages must have the same extension.

Frozen denotation fixture:

- PL `zegarek` -> `{OBJ-WRIST}`;
- EN `watch` -> `{OBJ-WRIST}`;
- DE `Uhr` -> `{OBJ-WRIST, OBJ-WALL}`;
- DE `Armbanduhr` -> `{OBJ-WRIST}`.

Thus:

\[
\boxed{
\operatorname{Lex}_{DE}(\text{Uhr})
\neq
\operatorname{Lex}_{PL}(\text{zegarek}).
}
\]

This mismatch is preserved rather than normalized away.

## 4. Relational grounding

The world fixture is independent of lexical labels:

\[
OBJ\!\!-
WRIST\xrightarrow{MEASURES}TIME,
\qquad
OBJ\!\!-
WALL\xrightarrow{MEASURES}TIME,
\]

\[
OBJ\!\!-
WRIST\xrightarrow{ATTACHED\_TO}WRIST,
\qquad
OBJ\!\!-
WALL\xrightarrow{ATTACHED\_TO}WALL.
\]

Because both objects satisfy `MEASURES TIME`, that relation does not resolve the wider German lexical fibre:

\[
\operatorname{Lex}_{DE}(\text{Uhr})\cap\{x:x\xrightarrow{MEASURES}TIME\}
=
\{OBJ\!\!-
WRIST,OBJ\!\!-
WALL\}.
\]

The discriminating relation does:

\[
\operatorname{Lex}_{DE}(\text{Uhr})\cap\{x:x\xrightarrow{ATTACHED\_TO}WRIST\}
=
\{OBJ\!\!-
WRIST\}.
\]

After relational grounding:

\[
\boxed{
PL(\text{zegarek})
=
EN(\text{watch})
=
DE(\text{Uhr}\mid ATTACHED\_TO=WRIST)
=
OBJ\!\!-
WRIST.
}
\]

The equality is therefore not imposed at the lexical layer. It emerges only where the relational evidence actually identifies the same world object.

## 5. Architectural interpretation

M15 supports the working separation:

\[
\boxed{
L_i\xrightarrow{\lambda_i}\text{lexical fibre}\xrightarrow{\text{relational constraints}}\mathcal M_{world}.
}
\]

Human languages may partition the world differently. The memory does not require one language's lexical partition to become canonical.

For task retrieval, what should be invariant is the task-relevant relational projection, not the natural-language phrase:

\[
\boxed{
\Pi_{\mathcal T}\mathcal D(x)
}
\]

rather than a supposedly universal word label.

This makes language adapters observers/interfaces over the relational memory, not owners of memory identity.

## 6. Relation to PSI

M15 does not add a new PSI primitive. It is an experimental realization of the existing PSI discipline:

- different language surfaces act as different observation maps;
- their compatible fibres need not have the same width;
- identification is legal only when task-relevant relations actually collapse the fibre;
- unresolved lexical ambiguity remains unresolved.

In compact form:

\[
\boxed{
\text{change of language}\neq\text{change of world relation}
}
\]

but also:

\[
\boxed{
\text{same apparent word role}\not\Rightarrow\text{same lexical fibre}.
}
\]

## 7. Boundary

M15 uses three frozen deterministic adapters and a toy denotation/world fixture. It does not establish general multilingual understanding, universal language-independent ontology, or ontology-independent perception.

The demonstrated invariant is narrower and stronger operationally: **where independently specified language adapters successfully compile the same task, retrieval is language-invariant; where lexical scopes differ, the system preserves that difference until relational evidence resolves it.**

The next useful extension is not another language synonym list. It is to make language adapters themselves produce explicit candidate fibres and test cross-language agreement/disagreement against a larger relational domain, while keeping the underlying memory graph language-neutral.
