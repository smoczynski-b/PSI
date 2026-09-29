# PSI-MEMORY-M4-01 — context economy pilot

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Purpose

M3 showed that one source-attested distant bridge can make the Go G4 regression reach the abstract history-memory cluster through a seven-node local view. M4 asks the next question:

\[
\boxed{\text{does that structural view reduce the material an agent must load for the same task?}}
\]

This experiment is split deliberately:

- **M4a — context preparation cost:** deterministic and measurable now;
- **M4b — model work quality/cost:** requires two independent agent runs and must not be simulated by a deterministic script.

No result from M4a alone licenses a claim that an LLM reasons better.

## 1. Frozen task

Both conditions receive exactly this task:

> Starting from the frozen Go G4 situational-superko regression, state the exact PSI memory-adequacy criterion; explain why visited-board memory `V_t` fails and what repairs it; identify the relation of the regression to II.7 and II.9 without turning a regression witness into a proof premise; preserve the G1 provenance gap; state what the canonical history quotient is minimal with respect to; and state what recursive update does **not** imply.

## 2. Two input conditions

### A — broad reconstruction

The agent is given `experiments/m4-broad-manifest.txt`: current project bootstrap/control material plus the obvious memory/history sources and registries that a repository-oriented agent would normally inspect when it does not have the task graph.

This is **not** claimed to be the whole repository. It is a declared broad baseline pack.

### B — memory-guided view

The agent is given `experiments/m4-guided-manifest.txt`: the M3 bridge/view material and only the mathematical source files reached by that view that are needed to answer the frozen task.

The guided pack is not allowed to omit any source anchor required by the gold rubric merely to improve compression.

## 3. Gold source anchors for M4b

An independent evaluator should require all seven points:

1. exact adequacy criterion
   \[
   \ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t};
   \]
2. under G4/SSK, `V_t={B_0,...,B_t}` is insufficient and `U_t={(B_i,\sigma_i):i\le t}` repairs the lost player-to-move history;
3. Go G4 is a regression witness/benchmark for the abstract memory and recursive-update criteria, not a proof premise for II.7 or II.9;
4. the currently recovered source set has `G1=SOURCE GAP`; no missing theorem/witness may be invented;
5. the canonical history quotient is coarsest/minimal in the **order of quotients**, not proven bit-, coordinate-, storage-, or complexity-minimal;
6. mathematical recursive update requires the declared congruence/well-definedness conditions and does not establish finite memory, effective computability, or efficient computation;
7. the whole ladder is task-relative: changing the rule/task changes the adequate representation; it is not a universal absolute ordering of memories.

## 4. M4a success condition — frozen before measurement

Let `B_A` be the total UTF-8 byte size of the broad manifest files and `B_B` the corresponding size for the guided manifest.

M4a passes iff:

\[
\boxed{B_B/B_A\le 0.5}
\]

and all declared task-critical mathematical sources occur in the guided pack.

The script also reports file count and line count. It does **not** convert bytes into guessed token counts.

## 5. M4b protocol

Two independent runs of the same model/configuration are required.

- Run A may read only the broad manifest files.
- Run B may read only the guided manifest files.
- Neither run sees the other run's answer.
- Same frozen task, same answer-length ceiling, same temperature/reasoning configuration where controllable.
- Record actual source reads, tool calls, elapsed wall-clock if exposed, provider-reported input/output tokens if exposed, and final answer.
- Blind-score each answer on the seven gold anchors above; score unsupported extra claims separately.

Primary M4b comparison:

\[
(\text{quality},\text{source reads},\text{input tokens if exposed},\text{unsupported claims}).
\]

A result is economically interesting only if the guided condition preserves answer quality while reducing observed work.

## 6. Scope discipline

M4a tests **context-pack compression**, not LLM intelligence.

M4b will test one bounded task and one model configuration; even a positive result will not establish universal superiority of graph memory.

The experiment must remain reproducible from the pinned manifests and repository commit.