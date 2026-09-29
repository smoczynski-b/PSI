# Targeted repair audit — 2026-09-29

Basis: PSI `f9026cbc7d3f475058747082230fb504439db91f`, current file contents,
their introducing commits, and the recovered conversation decisions.
This is a targeted follow-up, not a claim to have read complete exports of
every project conversation. The earlier C19-v3/F62 correction remains binding;
CORE5 and CANON-03 remain frozen. The user's current instruction selects repair
ahead of the default P9-I continuation.

## Mathematical repairs

| Finding | Evidence before repair | Correction and verification |
|---|---|---|
| D05, III.12 metric constant | `e7f8be106f11685e6f194f612839c7353a2ded9c`: arbitrary `m,M` identified with sharp condition number | Define sharp `m*,M*`; keep certificate ratio separate. `Q=I,m=1,M=4` refutes old equality. Decay/resolvent/Kreiss/pseudospectral deductions still follow; nonzero Hilbert space is explicit for the lower bound 1. |
| D06, II.14 cross-start inference | `0a9ccf6a3b9870f9826d2731d586756acc968583`: confluence used to infer one normal form across the whole fibre | Prove global Bishop uniqueness by the linear frame ODE, compare all starting terms, and exhibit a global atom for nonemptiness. Two irreducible symbols refute the old inference from confluence alone. |
| D07, gluing type | Local segment rotation described as if it were global gauge | Give raw atoms their realization/frame data; keep one diagonal `SO(2)` as gauge; right-segment alignment is normalization. ODE uniqueness proves gluing and confluence without assuming that independent local choices are global gauge. |
| D08, MINI-02 polarity | Formula said `!=1 need not hold` | Correct to `=1 need not hold`; F62's one-piece/two-piece witness remains valid. |

The proof cycle is scoped to those claims: object and domain in III.12 §1 and
II.14 §§1–2; quantities `c_Q` and `|im NF|`; derivations above/in the repaired
units; adversarial counterexamples in `scripts/test_math_regressions.py`;
affected composition statement updated in place. The old MINI-01 and numbered
control snapshots remain historical sources, not current replacements.

The test suite checks exact witness algebra and logical countermodels. It does
not mechanically verify a Hilbert-space theorem or all differential geometry.
The ODE proof and the semigroup proof were checked as mathematical prose at the
declared scope. III.12 stays CONDITIONAL_PASS; general P9 stays OPEN/CENTRAL.

## Control repairs and next source gate

D03/D04: control schema 2 validates task, unit and gate state enums. For a new
III.n beyond III.12, a `PASS` plus an existing arbitrary file is insufficient.
The typed JSON gate binds the target task/unit, the exact theorem and review
bytes (SHA-256), six contract fields and precise source locators.

To prepare III.13:

1. Complete P9-I's source/contract review before publishing a numbered unit.
   State `object`, `type_domain`, `conditions`, `quantity`, `claim`, `limits`.
2. Prepare a `SOURCE_CONTRACT_GATE` JSON record, schema 1, with `unit_id`,
   `task_id`, `contract`, `sources`, `unit:{path,sha256}` and
   `evidence:{path,sha256}`. Each source needs HTTPS `url`, exact `locator`,
   and `supports`, a nonempty subset of the six contract-field names.
3. Its separate `SOURCE_CONTRACT_REVIEW` JSON evidence, schema 1, must identify
   the same unit/task, `unit_sha256`, `contract_sha256`, `sources_sha256`,
   reviewer, scope, PASS verdict and all six explicit boolean `checks`.
   Structured digests use `digest_json` in the checker. State the actual review
   performed; do not copy the synthetic format fixture as evidence.
4. Publish the reviewed unit, evidence and gate together. In control state,
   the gate entry supplies `state`, `task_id`, `path`; the unit's `evidence`
   points to that exact review. Regenerate views and run the targeted checks.

This catches accidental mismatch, stale evidence and the reproduced README /
unrelated-III.12 bypass. A self-authored review is not a trusted signature;
hashes do not establish truth or reviewer independence. CI validates record
consistency, not the mathematical content of a supplied PASS. III.13's actual
gate remains OPEN; no synthetic fixture is published as a passed gate.

## Experimental implementation and remaining work

The finite controller experiment is separately recorded in psi-model commit
`d74f6c4f50f4578cc56df97508748945083c0f96`, draft PR #4 against
`psi-agent-state-01`. Its 65 passing tests concern the declared finite
laboratory; the experiment is not yet merged into that active branch and does
not measure improvement of arbitrary LLM agents.

FORUM discovery and bounded-read repairs belong to `psi-forum-seed-01` and its
deployment, with their own tests. Concurrent admission/caps, atomic
object-plus-ledger storage and authoritative global ordering remain separate
OPEN design issues. Existing SDK operations do not provide the transaction or
unique-key primitive needed to claim those guarantees.
