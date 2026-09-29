# PSI-MEMORY-M4-RESULT-01

**Status:** M4a PASS / M4b NOT_RUN  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Frozen criterion

`PSI-MEMORY-M4-01` froze M4a before measurement:

\[
B_{guided}/B_{broad}\le 0.5,
\]

while retaining all declared task-critical mathematical source anchors.

No guessed token conversion is used.

## 2. Measured result

GitHub Actions run `36620226279` executed both the existing M1-M3 regressions and `scripts/test_memory_economy.py`.

Observed context-pack sizes:

| condition | files | UTF-8 bytes | lines |
|---|---:|---:|---:|
| broad reconstruction | 16 | 201696 | 7639 |
| memory-guided | 7 | 39560 | 1784 |

Therefore

\[
\frac{B_{guided}}{B_{broad}}=0.1961,
\]

and the measured byte reduction is

\[
\boxed{80.39\%}.
\]

M4a therefore passes the predeclared 50% reduction gate.

## 3. Retained source anchors

Both packs contain the four task-critical mathematical sources:

- `docs/go-memory-regression-01.md`;
- `docs/principia-v2-04-representation-adequacy.md`;
- `docs/principia-v2-07-exact-history-memory-adequacy.md`;
- `docs/principia-v2-09-recursive-history-quotient-update.md`.

The memory-guided condition additionally carries the small M3 navigation/provenance layer instead of the broad project-control, registry and theorem-map bootstrap.

## 4. What M4a establishes

M4a establishes only this bounded engineering fact:

\[
\boxed{\text{the current PSI memory map can prepare a source-complete task pack with much less raw material than the declared broad baseline.}}
\]

It does not establish lower LLM token use, lower latency, better reasoning, or equal answer quality. Those require actual model telemetry and independent executions.

## 5. M4b status

M4b requires two isolated runs of the same model/configuration under the frozen task and separate input conditions, followed by blind scoring against the seven-point gold rubric in `experiments/PSI-MEMORY-M4-01.md`.

No independent zero-cost execution harness is currently attached to this experiment. Starting managed Brainbase tasks would be billable, so under the current zero-cost constraint they were not started.

Status:

\[
\boxed{\mathrm{M4b}=\mathrm{NOT\_RUN}\;/\;\mathrm{ZERO\!\!-\!COST\ HARNESS\ REQUIRED}.}
\]

## 6. Regression safety

The same CI run retained:

- M1 PASS;
- M2 PASS;
- M3 PASS;
- M4a PASS.

Thus the economy measurement did not replace the dependency, invalidation, or distant-bridge regressions.
