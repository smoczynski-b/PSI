# PSI — public repository routine

**Control role:** `work-routine`  
**Status:** PUBLIC RELEASE / GOVERNANCE ROUTINE

This file governs changes that are intended to appear on the public PSI repository. Internal research selection is maintained separately in a protected workspace.

## Public change sequence

```text
SOURCE / CHANGE
    -> VALIDATE
    -> DISCLOSURE GATE
    -> PUBLISH
    -> VERIFY PUBLIC PROJECTION
```

`VALIDATE` checks the declared technical or mathematical contract. `DISCLOSURE GATE` assigns `PUBLIC | REVIEW | WITHHOLD` to an explicit file/fragment scope. `PUBLISH` is a separate action; no PASS automatically authorizes it.

## Mathematical discipline

Use:

\[
\text{object}\to\text{type/domain}\to\text{conditions}\to\text{quantity}\to\text{proof/test}.
\]

For unbounded operators, domain precedes formal algebra. Classical results must remain labeled classical/adapted when used as PSI bridges.

## Repository discipline

- Recheck remote HEAD before a write.
- Preserve concurrent changes; no routine force-push.
- Keep stable public pointers coherent.
- Run `python scripts/check_control.py` and `python scripts/check_public_projection.py` for affected public-control changes.
- Run only affected mathematical/runtime regressions.
- Public release prose and metadata are English; symbols, quotations and identifiers retain source form.
- Historical internal files, if still present for provenance, do not select current private work.

A component PASS, publication PASS and system PASS are distinct claims.
