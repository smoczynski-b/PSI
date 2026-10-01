# PSI-MEMORY-M14-COMPOSITION-01 — typed contract composition

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can several task intents and evidence constraints be composed into one executable retrieval contract without treating composition as a blind union?

Working rule:

\[
\boxed{\operatorname{Compose}(c_1,\ldots,c_n)\neq c_1\cup\cdots\cup c_n}
\]

unless typing, anchor policy and evidence requirements are mutually compatible.

## 1. Added contract dimensions

M14 adds:

- intent `ANALOGY` mapped to terminal relation `ANALOGY_TO`;
- evidence mode `VALID_FRAGMENT_CERT_ONLY`;
- explicit detection of several anchors in one task;
- contract-conflict output rather than silent weakening.

## 2. Frozen witnesses

### C1 — compatible composition

`dla II.9 pokaż przesłanki dowodu, granice i analogie`

Expected: one anchor, three compatible intent families, ordinary attestation mode, executable retrieval.

### C2 — evidence/intention conflict

`dla II.9 pokaż przesłanki dowodu i analogie, tylko pełne certyfikaty`

The local map contains an `ANALOGY_TO` relation for II.9, but no fragment-certified analogy edge. The strict evidence gate therefore removes the entire requested analogy family.

Expected:

\[
\boxed{\mathrm{CONTRACT\_CONFLICT}\to\mathrm{NO\_RETRIEVAL}}.
\]

### C3 — anchor conflict

`sprawdź przesłanki dowodu II.9 i II.11.PSI-BRIDGE`

Expected: `NEEDS_ANCHOR_POLICY`; the compiler must not choose one anchor implicitly.

### C4 — legal strict mode

`dla II.9 pokaż granice, tylko pełne certyfikaty`

Expected: strict mode is executable because the requested boundary family has fragment-certified support.

## 3. Success predicates

M14 passes iff:

1. C1 includes proof, boundary and analogy relations;
2. C2 is fail-closed because analogy has zero strict-certificate coverage;
3. C3 is fail-closed because multiple anchors lack a composition policy;
4. C4 selects only fragment-certified boundary edges with zero routing-attested leakage;
5. M1–M13 remain green.

## 4. Boundary

M14 does not implement general multi-anchor execution or general natural-language understanding. It tests typed composition, evidence-mode compatibility and explicit conflict detection for frozen relation families.
