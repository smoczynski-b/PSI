# PSI — current work map

**Control role:** `work-map`
**Record date:** 2026-09-29

Generated from [control-state.json](control-state.json); edit that source,
then run `python scripts/check_control.py --write`.
Mathematical statuses are inherited records, not fresh proof audits.

## Selection

First check external deltas and blockers. A repair or newly available separating observation preempts continuation. User instructions take precedence.

Default substantive unit: **P9-I**, after the external delta/STOP check.
One active primary unit. [Regular checks and effort budget](work-routine.md).

## Operational tasks

### TRAFFIC-INSTRUMENTATION — WAIT

**Reason:** The current aggregate experiment intentionally stops instrumentation at G0A/G0D; no session/person identifier is collected.

**Release:** Observed censoring, a supported breakout, actual instrumentation failure, or an explicitly revised measurement contract.

**Next check:** First active session of each Warsaw calendar day, or after an observed failure/censoring/breakout.

**Allowed:** Read existing summaries; accumulate prospective pageview and outbound-click counts; preserve publication sequence.

**Source:** [experiments/PSI-TRAFFIC-EST-01.md](../experiments/PSI-TRAFFIC-EST-01.md).

### TRAFFIC-OBSERVATION — READY

**Action:** At the first active session of the day obtain one bounded summary for a completed window using an authorized endpoint; otherwise record access BLOCKED without inventing counts.

**Evidence:** Protocol inspected; no live counts collected in this control repair. G0A/G0D PASS is inherited instrumentation status, not a fresh deployment check.

**Source:** [experiments/PSI-TRAFFIC-EST-01.md](../experiments/PSI-TRAFFIC-EST-01.md).

### FORUM — WATCH

**Action:** Reuse the existing hourly monitor. Inspect only changed OIDs or anomalies, dereferencing the exact objects before semantic claims.

**Evidence:** Automation enabled at inspection on 2026-09-29. No fresh T3/T4 evidence retrieved; neither confirmed nor disproved by this repair.

**Source:** [docs/work-map-09.md](../docs/work-map-09.md).

### P9-I — READY

**Action:** Run the source/contract gate for infinite-dimensional resolvent/growth. No III.13 theorem or numbering before a passed gate.

**Evidence:** Next mathematical gate inherited; selected only after the bounded external delta/STOP check.

**Source:** [docs/theorem-map-v3.md](../docs/theorem-map-v3.md).

### MODEL-ADAPTER — BLOCKED

**Reason:** The supplied session handoff reports RUN-01 blocked by missing TYPESAFE_API_KEY. This is inherited operational status; current secret availability was not verified here.

**Release:** Verify authorized secret configuration without exposing its value, then apply the pre-registered run gate.

**Next check:** When integration configuration changes or this task is explicitly selected.

**Allowed:** Inspect adapter and contract; do not represent a missing credential as a falsification of PSI.

**Source:** [.github/workflows/psi-jev-run-01.yml](../.github/workflows/psi-jev-run-01.yml).

### PSI-VIZ — BACKLOG

**Action:** LAB realization: test identifiability of the fibre after selection against current priorities.

**Evidence:** Design inherited from supplied conversation; no implementation verified in this repository.

**Source:** [docs/work-routine.md](../docs/work-routine.md).

### AGENT-COMPARISON — BACKLOG

**Action:** Prepare a controlled comparison only when selected; do not report conceptual abilities as measured improvements.

**Evidence:** Architecture is procedural; comparative efficacy remains unverified.

**Source:** [docs/agent-psi-architecture-02.md](../docs/agent-psi-architecture-02.md).

## Recorded mathematical state

| Unit | Recorded status | Evidence |
|---|---|---|
| II.1 | PASS | [unit](principia-v2-01-exact-task-decidability.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.2 | PASS | [unit](principia-v2-02-kernel-factorization.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.3 | PASS | [unit](principia-v2-03-global-observer-sufficiency.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.4 | PASS | [unit](principia-v2-04-representation-adequacy.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.5 | PASS | [unit](principia-v2-05-task-information-legality-of-reduction.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.6 | PASS | [unit](principia-v2-06-deterministic-quotient-dynamics.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.7 | PASS | [unit](principia-v2-07-exact-history-memory-adequacy.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.8 | PASS | [unit](principia-v2-08-coarsest-exact-history-quotient.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.9 | PASS | [unit](principia-v2-09-recursive-history-quotient-update.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.10 | PASS | [unit](principia-v2-10-strong-lumpability-bridge.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.11 | PASS | [unit](principia-v2-11-myhill-nerode-bridge.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.12 | PASS | [unit](principia-v2-12-paige-tarjan-benchmark.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.13 | PASS_AFTER_ERRATA | [unit](principia-v2-13-cat-fact-canonical-scope.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.14 | PASS_AFTER_ERRATA | [unit](principia-v2-14-cat-fact-norm-mini.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.15 | PASS | [unit](principia-v2-15-closed-frame-holonomy.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| II.16 | PASS | [unit](principia-v2-16-higher-compatibility-truncation.md) / [audit](principia-v2-whole-crosscheck-01.md) |
| III.1 | PASS_AFTER_ERRATA | [unit](principia-v3-01-lambda-operator-projectability.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.2 | PASS_AFTER_ERRATA | [unit](principia-v3-02-weight-sturm-liouville.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.3 | PASS_AFTER_ERRATA | [unit](principia-v3-03-domain-selfadjoint.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.4 | PASS_AFTER_ERRATA | [unit](principia-v3-04-compact-resolvent-spectrum.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.5 | PASS_AFTER_ERRATA | [unit](principia-v3-05-liouville-normal-form.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.6 | PASS_AFTER_ERRATA | [unit](principia-v3-06-perturbation-hellmann-feynman.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.7 | PASS | [unit](principia-v3-07-spectral-information-hierarchy-most.md) / [audit](principia-v3-most-hcube-whole-crosscheck-01.md) |
| III.8 | PASS | [unit](principia-v3-08-hcube-nonnormal-resolvent-lab.md) / [audit](principia-v3-most-hcube-whole-crosscheck-01.md) |
| III.9 | PASS | [unit](principia-v3-09-semigroup-projectability-dom-logos.md) / [audit](principia-v3-dom-logos-crosscheck-01.md) |
| III.10 | SECTOR_PASS | [unit](principia-v3-10-sop11e-wellposedness-sectors.md) / [audit](principia-v3-sop11e-dom-logos-crosscheck-01.md) |
| III.11 | PASS | [unit](principia-v3-11-p9-metric-gradient-bridge.md) / [audit](principia-v3-p9-composition-crosscheck-01.md) |
| III.12 | CONDITIONAL_PASS | [unit](principia-v3-12-hypocoercive-modified-energy-bridge.md) / [audit](principia-v3-p9h-composition-crosscheck-01.md) |

CORE5 remains FROZEN. P2 general remains PARTIAL; P9 general remains OPEN/CENTRAL.
III.13 requires a completed P9-I source/contract gate.

## Interpretation

Traffic: G0A/G0D instrumentation PASS is inherited from the protocol;
G0B/G0C/G0E remain UNOBSERVED. No fresh live counts are asserted here.
WWW visual grammar remains frozen; FB publication sequence is unchanged.
PSI theory/control lives here; the experimental implementation lives in psi-model.
Stable pointers supersede numbered control snapshots. Unchanged history is not reread
at every session. No new status, ledger or commit is required without a meaningful delta.
