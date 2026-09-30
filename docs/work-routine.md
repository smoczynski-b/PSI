# PSI — proportional work routine

**Control role:** `work-routine`  
**Status:** ACTIVE / AGENT POLICY  
**Effective:** 2026-09-29; applies during active work.  
**Basis:** [Agent Architecture 02](agent-psi-architecture-02.md),
[source governance](source-governance-01.md), [current work map](work-map.md).

## Selection and limits

At entry: read current state, check STOP/WAIT and select one executable unit.
An observed failure or a newly available separating observation takes priority
over automatically continuing the previous branch. An explicit user task takes
precedence over this default queue.

`WAIT` blocks only its declared intervention. It does not block read-only
observation or other independent work. An unavailable observation is `UNVERIFIED`
or `BLOCKED`, never zero, FAIL, or proof that nobody used PSI.

The current traffic protocol already stops instrumentation at G0A/G0D.
Its unobserved G0B/G0C/G0E do not invalidate the narrower measurement contract.
No global G0 PASS or global G0 FAIL may replace these component statuses.

## Contract interview before snapshot

Before a substantial unit, apply [contract-interview.md](contract-interview.md).
First reconstruct the draft object, task, protocol/source basis and success/stop
condition from the conversation and project state. Ordinary language noise —
missing punctuation, spelling, shorthand or unfinished surface form — should be
repaired silently when doing so does not select between different working meanings.

If more than one materially plausible interpretation remains and the alternatives
would change the primary object, data/source type, inferential target, public or
irreversible action, result type or success criterion, ask the user one short
question that separates those contracts. Ask about working meaning, not writing
quality. Do not ask the user to choose routine implementation details that remain
execution-equivalent.

In compact form:

\[
\boxed{
\text{surface noise}\to\text{repair};\qquad
\text{material contract fork}\to\text{ASK};\qquad
\text{execution-only fork}\to\text{EXECUTE}.
}
\]

`go` still means execute when the contract is already sufficiently determined.
It does not license invention of a missing material contract field.

## Regular actions during activity

| Trigger | Action | Limit / recorded result |
|---|---|---|
| Session start or context handoff | Read current pointers, delta since previous handoff, blockers and priorities | One bounded inspection; reuse unchanged verified context |
| Before a substantial unit | Reconstruct intent; apply contract-interview gate; then state object, task, contract, source, success/stop condition | Ask only for material ambiguity; one short record in the working unit, not a new control document |
| On changed hypothesis/domain/gauge/metric or newly exposed meaning fork | Relabel contract; check whether clarification is required; then check affected claims and regressions | Immediate, before using the changed result |
| At unit completion | Verify result at its actual scope; update affected current records together | One coherent commit normally; 2–3 only if independently reviewable |
| After 3 completed units, or immediately after significant external delta | Review all sectors; check whether the next selected unit still has priority | One short frontier review; no full source reread without cause |
| First active session of a Warsaw calendar day | One bounded traffic summary read for the completed window, if an authorized endpoint is available; reuse latest FORUM monitor result | Record window, source, counts/unknowns and censoring; no synthetic visit/click; do not repeat an unchanged read |
| Before repository publication | Check control consistency, affected regressions, diff and current remote HEAD | No force-push; no unrelated full regression suite |
| Session end | Record result, evidence, open blocker and next admissible action | Brief delta; use commit plus current work record, avoid parallel chronicles |

Existing hourly FORUM monitoring remains the background watcher. Do not create
another hourly/daily automation merely to enforce this active-session routine.
An inactive session does not execute these checks. The first-day read is an
agent procedure, not a claim that a new scheduler has been installed.

## Effort allocation

Working target over several substantive units: **75% execution, 15% targeted
verification, 10% coordination and recording**. These are operating budgets,
not measured performance and not a reason to truncate a necessary proof.
If coordination repeatedly exceeds 10%, consolidate pointers and reports before
adding more process. A broken invariant may temporarily exceed the budget;
state the defect and stop the repair when its check passes.

## Git and evidence

Use stable current filenames. Do not append numbered registry/work-map versions.
Historical snapshots remain immutable provenance; `control-state.json` and the
README identify the current roles. A ledger records changed reasoning or a
high-impact decision, not every file save. A commit count alone is not a quality
metric; review coherence, recoverability and test coverage instead.

No recurring commit is required. No notification is required without a meaningful
delta. Test failure blocks only the dependent operation; preserve independent work.

## Repair record — 2026-09-29

- `work-map-09` lost the reason for traffic WAIT; the reason exists in
  [PSI-TRAFFIC-EST-01, section 12](../experiments/PSI-TRAFFIC-EST-01.md).
  Restored it in the stable work map. Prior blanket G0 FAIL and the resulting
  obligatory instrumentation restart are withdrawn.
- Materialized C01–C67 and F01–F62 into complete current registries; applied the
  already adopted C19-v3/F62 correction to the stale F12 wording and the C22/C23 resolution to the stale C21 OPEN label.
- Stable maps separate mathematical readiness from global work selection.
  P9-I remains an admissible source gate during observational WAIT, conditional
  on the routine sector check. III.13 remains unauthorized without its gate.
- Added executable pointer, registry and status consistency checks plus negative
  controls. Their PASS is organizational verification, not a mathematical reaudit
  or live telemetry test. Operational effectiveness over later sessions remains
  to be observed.

## Repair record — 2026-09-30

- Added the contract-interview gate after an observed object drift in the chemistry/
  representation discussion: `obraz` was silently specialized from data representation
  to laboratory photograph.
- Surface-language noise is now explicitly separated from semantic and material
  contract ambiguity. Only the latter licenses an interrupting clarification question.
- `go` remains direct execution when the current contract is unambiguous.
