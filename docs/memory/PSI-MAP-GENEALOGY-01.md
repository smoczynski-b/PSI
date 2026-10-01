# PSI-MAP-GENEALOGY-01

**Status:** EXPERIMENTAL GENEALOGY / NON-CANONICAL / NOVELTY UNRESOLVED  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30

## 1. Purpose

This registry maps external architectural precedents onto the current PSI memory architecture without rewriting historical systems in PSI vocabulary.

It answers a narrow question:

> Which earlier systems already instantiate roles now appearing in PSI active memory, and which parts of the present synthesis are not yet matched by a verified predecessor?

The registry is genealogical. It does not establish originality, priority, patentability, theorem dependence, or historical influence.

## 2. Genealogical invariants

The following are mandatory:

\[
\boxed{\text{historical resemblance}\neq\text{proof dependency}}
\]

\[
\boxed{\text{shared role}\neq\text{shared formalism}}
\]

\[
\boxed{\text{later PSI vocabulary must not be projected backward}}
\]

Therefore HEARSAY-II did not contain `PSI-SERVANT`, Artificial Immune Systems were not `PSI-IMMUNE`, and the 2003 Knowledge Market did not trade PSI maps. The registry records only source-supported role correspondences.

## 3. Verified predecessor families

### 3.1 Blackboard systems — shared state

HEARSAY-II provides a genuine predecessor for a common mutable problem state with data-directed activation of knowledge sources. Its blackboard handler maintained auxiliary state and updated it as knowledge sources changed the blackboard.

Barbara Hayes-Roth's 1985 blackboard control architecture goes further by separating domain and control problems and allowing a system to reason about its own knowledge and behavior.

Current mapping:

```text
HEARSAY-II -> PSI-SHARED-MEMORY
BB1/control-blackboard -> role precursor for PSI-SERVANT
```

Boundary: PSI active memory additionally has typed provenance, task-local workspaces, selective invalidation, MVCC and WAL; none of these is attributed to the historical blackboard systems by this registry.

### 3.2 Electronic institutions — guardians and institutional mediation

AMELI executes electronic institutions by mediating external agents through governors and managers while enforcing institutional rules.

Current mapping:

```text
AMELI governor/manager -> role precursor for PSI-GUARDIAN
```

Boundary: an AMELI governor mediates an external agent's institutional participation. `PSI-GUARDIAN` is only a current candidate role for admission/control at the shared-memory boundary; the two are not identified.

### 3.3 Autonomic computing and artificial immune systems — homeostasis

MAPE-K supplies the control-loop pattern:

```text
MONITOR -> ANALYZE -> PLAN -> EXECUTE
                 \-> KNOWLEDGE <-/
```

Artificial Immune Systems supply a distinct line: anomaly/fault detection, diagnosis, isolation and recovery inspired by biological immunity.

Current mapping:

```text
MAPE-K -> homeostatic/control contribution to SERVANT and IMMUNE
AIS/FDDR -> direct role analogy for IMMUNE
```

Boundary: `PSI-IMMUNE` is not a selected AIS algorithm and has no domain-truth authority. Its proposed object is pathology of memory/execution dynamics.

### 3.4 Knowledge markets and shareable experience objects — exchange

Dignum & Dignum (2003) provide a direct knowledge-market predecessor: agent-mediated organizational knowledge sharing.

Decisional DNA / SOEKS (2012) is especially close to the proposed object layer: a structured, shareable representation of decisional experience. Its future-work section explicitly proposes a knowledge market using SOEKS and Decisional DNA.

Current mapping:

```text
Knowledge Market -> PSI-MAP-EXCHANGE
Decisional DNA/SOEKS -> PSI-MAP-OBJECT + PSI-MAP-EXCHANGE
```

Boundary: the traded object in those systems is not a PSI task-relative map and is not licensed by the PSI representation-adequacy criterion.

### 3.5 Nanopublications and provenance — curatorship

Nanopublications make a small assertion plus provenance/publication information into a referencable knowledge object. Recent provenance-driven extensions represent supporting and conflicting evidence and trust relations among agents/facts.

Current mapping:

```text
nanopublication/provenance -> PSI-CURATOR + PSI-MAP-OBJECT
```

Boundary: nanopublication provenance does not by itself provide PSI task-relative representation adequacy or the active-memory execution architecture.

### 3.6 Contemporary shared-world LLM systems

Two contemporary lines are recorded as parallels, not historical precursors:

- 2025 LLM blackboard MAS: multiple LLM agents coordinate through shared blackboard content;
- 2026 world-centered MAS: shared explicit world representation is placed above isolated agent-local representations.

They strengthen the claim that the design space is active, but they do not establish equivalence with PSI shared memory.

## 4. Current PSI synthesis

The current project already implements, experimentally:

```text
authoritative relational memory
-> task-local Workspace
-> local typed delta
-> selective routing
-> selective invalidation
-> MVCC transaction boundary
-> durable WAL/recovery
```

The proposed next institutional layer is:

```text
GUARDIAN  : admission / boundary legality
SERVANT   : procedural legality of state transitions; chronicler; local corrective agency
IMMUNE    : anomaly/pathology detection, quarantine, recovery and immune memory
CURATOR   : genealogy, provenance, versioning, supersession, archival and reuse scope
```

None of these candidate roles is granted domain epistemic authority merely by role.

## 5. FORUM as map exchange

Candidate object:

\[
M=(c,\Omega_M,\Pi_M,D_M,S_M,P_M,\tau_M),
\]

where the exact schema remains open, but a map must at least bind its contract/scope, representation, dependencies, sources/provenance and version/status.

Candidate operations include:

```text
IMPORT(M)
FORK(M)
REFINE(M)
SUPERSEDE(M)
CHALLENGE(M)
COMPOSE(M1,M2)
```

This is intentionally not reduced to popularity, ranking or one scalar reputation score.

## 6. PSI-specific gate

The strongest currently identified differentiator is not "shared memory" or "knowledge market" by itself. Those have clear precedents.

For a representation/map

\[
\rho:\Omega_c\to Z,
\]

PSI already has the task-relative adequacy condition

\[
\boxed{\ker_{\rm eq}\rho\subseteq E_{\mathcal T,c}}
\]

or equivalently

\[
\boxed{q_{\mathcal T,c}=g\circ\rho.}
\]

Thus a map offered for reuse may be compressed, but it may not merge distinctions required by its declared task.

This yields the architectural guardrail:

\[
\boxed{\text{exchange/reuse value}\neq\text{epistemic licence}.}
\]

Popularity, number of imports, producer identity and computational convenience cannot replace task-relative adequacy and contract/source checks.

## 7. Novelty status

The external scan verifies predecessors for almost every component role. It does **not** verify an earlier system combining all of the following in one architecture:

1. maps/representations as durable first-class exchange objects;
2. genealogy/provenance/versioning of maps inside the same memory;
3. separated guardian/servant/immune/curator roles without automatic epistemic authority;
4. delta-routed task-local agent workspaces over authoritative shared memory;
5. task-relative map legality governed by PSI representation adequacy.

This absence is not proof of novelty. The correct status is:

\[
\boxed{\texttt{UNRESOLVED\_NOVELTY}}
\]

A publication-quality novelty claim would require a broader systematic literature review and explicit nearest-neighbour comparison.

## 8. Machine-readable files

- `docs/memory/psi-map-genealogy-sources-01.tsv`
- `docs/memory/psi-map-genealogy-nodes-01.tsv`
- `docs/memory/psi-map-genealogy-edges-01.tsv`
- `scripts/test_map_genealogy.py`

The machine-readable graph is deliberately separate from the ordinary PSI theorem/proof dependency graph.

## 9. Boundary

This artifact does not modify CORE5, CANON-03, theorem status, FORUM gateway behavior or the live shared-memory runtime. `PSI-GUARDIAN`, `PSI-SERVANT`, `PSI-IMMUNE`, `PSI-CURATOR` and `PSI-MAP-EXCHANGE` remain candidate architectural roles/concepts until separately contracted and tested.
