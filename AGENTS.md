# PSI repository working rules

Read `docs/work-map.md`, `docs/work-routine.md` and the current pointers in
`docs/control-state.json` at entry. Read only the sources needed for the selected
unit. The stable control files supersede numbered snapshots for work selection;
historical mathematical sources keep their provenance and contract limits.

- User instructions take precedence. Keep CORE5 and CANON-03 frozen.
- Select one primary unit; check all sector blockers before continuing a branch.
- Before freezing a substantial contract, apply the [contract interview gate](docs/contract-interview.md). Treat punctuation, spelling, shorthand and sentence fragments as surface noise unless they change working meaning. If two materially plausible interpretations would change the object, data/source type, action, inferential target or success criterion, ask one short discriminating question before execution. Do not ask the user to decide routine implementation details. Do not silently normalize semantic uncertainty away.
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

- For an explicitly selected memory task, read `docs/memory/README.md` and
  select the unit in `docs/memory/CURRENT-WORK-FRONT-01.md`. This is the
  memory-specific application of user-task precedence; the general project
  default in `docs/control-state.json` remains unchanged. Read the latest
  `Memory and agent review 2026-09-30` section of the audit for acceptance cases.
  Current next unit: R1 journal-tail recovery. Earlier F0 collision/domain/view
  repairs are complete at their stated scope; do not select them again from
  historical NEXT paragraphs. F4.4 waits for the front's listed prerequisites.
- Keep the four-role constitution. ACCESS_STEWARD executes Guardian policy;
  Curator may propose infrastructure changes but cannot self-authorize them.
  For persistent side effects, test interruptions between journals as well as
  clean restart. For derived visual packets, verify the actual payload binding
  at each consumer; check redaction and task-required relation direction.
- Keep same-data representation tests separate from acquiring or classifying
  different photographs. Preserve chemistry's intended role: physically
  constrained processes represented through formulas, quantities, conditions
  and typed relations, with natural language as an interface rather than a
  mandatory internal record. Keep this design aim separate from measured LLM ability.
- Distinguish arbitrary drawing coordinates from process-derived geometry
  (states, reaction directions, conservation constraints and trajectories).
  The nearness-only negative control does not refute such geometry. A finite
  elemental vocabulary does not make molecular or dynamical state space finite.
  Report source binding separately from mathematical validity. M4b A/B/C tests
  text-context selection, not the benefit of formal inter-agent communication.
- Read active memory as authoritative records plus derived task workspaces.
  COO relation planes and drawings omit some record metadata; preserve source,
  contract, version and status alongside them whenever the task needs these.
  A procedural ACK or a health label is not an epistemic verdict. Existing
  single-process regression success is not complete recovery/integration proof.
- Reproduce M4 inputs with `scripts/prepare_memory_evaluation.py`. Do not use
  the evaluator rubric to select lexical results, tune on observed answers,
  substitute one context for independent model runs, or call preparation/model
  regression success a measured quality gain. A known calibration task is not
  held-out evidence. Unknown costs remain unknown.
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
