# PSI repository working rules

Read `docs/work-map.md`, `docs/work-routine.md` and the current pointers in
`docs/control-state.json` at entry. Read only the sources needed for the selected
unit. The stable control files supersede numbered snapshots for work selection;
historical mathematical sources keep their provenance and contract limits.

- User instructions take precedence. Keep CORE5 and CANON-03 frozen.
- Select one primary unit; check all sector blockers before continuing a branch.
- A WAIT needs a reason, source, release condition, next check and allowed work.
- Distinguish experimental observation from intervention. Do not manufacture traffic.
- Use the Bronsztejn gate for substantive mathematics: object, type/domain,
  conditions, measured quantity, proof/test. Preserve SOP11/P9/P10/P13 scope;
  do not claim a named audit was run without its applicable specification.
- Scale audit to impact. A link fix needs a link check; a theorem needs the full
  agent cycle and affected regressions. Do not rerun unrelated laboratories.
- Update stable current files in place. Keep old snapshots as history.
- One coherent, reviewable change should normally be one commit; split only for
  independently testable changes. Do not rewrite published history to meet a quota.
- Run `python scripts/check_control.py` for control changes. Run its mutation
  tests when changing the checker. It checks control consistency, not theorem truth.
- Before publishing, recheck remote HEAD, inspect the diff and preserve concurrent
  changes. Never force-push as a routine repair.
- End with changed state, verification scope, remaining blocker and next action.
  No delta means no new report, ledger entry or commit is needed.
