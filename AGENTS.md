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

## Experimental memory — conversation 04 correction

- Read `docs/memory/AUDIT-ROZMOWY-04.md` before using the experimental memory.
  Execute compiled M13–M15 contracts through `scripts/memory_retrieval.py`;
  the declared anchor, evidence mode and budget are binding.
- Recheck fragment and whole-source hashes at use time. A stored VALID label
  is not current verification. Stale certificates cannot fall back silently
  to routing attestations; routing hints are not proof dependencies certified
  by this retrieval run.
- Unknown relation/schema means NO_RELATION_CONTRACT, not an empty compatible
  fibre. Count conflicts only for well-typed observations and an integer budget.
- Preserve multiple candidates and task-relative quotients. Equal observed
  material attributes do not identify a unique object/history.
- For chat audits, distinguish full transcripts, primary archived fragments,
  retrieved summaries and repository artifacts. Search-query echoes are not
  user statements. Never report a complete-chat audit from summaries alone.
- After the declared counterexample passes and affected regressions remain
  valid, finish the repair unit. Do not automatically open another numbered
  experiment. M4b's actual model comparison remains NOT_RUN.
