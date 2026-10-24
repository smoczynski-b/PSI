# M013 combined finite acceptance

Disclosure: PUBLIC for oracle.py, INPUTS.json, RECEIPT.json, MAP_COVERAGE.json,
SOURCES.json and this README. Source snapshots contain previously published
project comments. No book text, account data, host identifiers, private session
exports or credentials are included.

## Reproduce

From the repository root:

```text
python -B experiments/m013-combined-20261024/oracle.py
```

Python standard library only. The script writes its receipt beside the input.
A rerun changes the completion timestamp and duration; compare mathematical
results and source/code/input hashes rather than the complete receipt hash.

## Method and erratum

All set partitions of the explicitly supplied nonterminal states are examined
(n=1,2,3,4: 1,2,5,15 partitions). Terminal codes preserve the exact answer and
are separate from ACT codes. For each proposed nonterminal code, the program
constructs the actual partial code-update function and rejects conflicting
coded successors. It also checks the required report-presence signature.

This directly checks the chosen code's update. It does not substitute
kernel inclusion in R_infinity for congruence. The accepted C3+ erratum and
the subsequent dependency audit are snapshotted in SOURCES.json. Initial
states use one fixed action and every actual transition is terminal.

Only after the direct partition minimum is computed does the program compare
it with expected values. The selective-contract cases are additionally compared
with an independent enumeration of graph color assignments and a sum across
report-presence layers.

## Observed result

PASS_SCOPED for the single process, in packet order M013-01 then M013-02.

| Case | C3 before / result | C3+ before / result |
|---|---|---|
| B0 | 4 | 5 |
| B1 | 3 | 4 |
| B2 | 3 -> 4 | 4 -> 4 |
| B3 | 3 -> 3 | 4 -> 3 |
| B4 | 3 -> 4 | 3 -> 5 |
| K1 | 4 -> 3 | 4 -> 4 |
| K2 | 3 -> 3 | 3 -> 6 |
| K1, n=4 | 6 -> 3 | 6 -> 6 |

The receipt includes optimal partitions, counts of admissible partitions by
number of classes, explicit update witnesses, and factorization checks on
every microstate (4,8,12 states respectively for K1,K2,K1 n=4). B2/B3/B4
satisfy the extension bounds and the exact strong-code change formula; B4
introduces one new terminal value.

Packet02: six S1 settings and two S2 settings match the predicted minima.
The broken S3 oracle gives 4 instead of 6 and is rejected. S4 invalid models
are rejected: resolved initial state, ambiguous report and a synthetic report
outside the declared physical alphabet. Additional scope controls reject
different actions, declared nonterminal successors, invalid factorization,
changed q and changed initial beliefs (eight negative controls in total).

S5 checks all 32 subsets for S1 and all 8 for S2: 230 strict subset comparisons
satisfy monotonicity; all 92 one-report extensions satisfy the factor-two bound.
Every one of these 40 cases also matches both graph calculations.

## Map boundary

MAP_COVERAGE.json records NOT_INDEXED for the exact M013 originals
6387176219,6387296277,6387364404 in the existing runtime's pinned overlay.
Data commit 38adb94c7f1f99374621017c33fbe4048602d922; runtime commit
447b0df1c76eb9dead8266aeeda6ca6c74c295c2. The historical MATH76 source-index
record is not a locator of these new originals. The CLI was not called after
this precheck; the map, pins and index were not changed.

## Scope

Finite falsification and acceptance of the specified cases only. This is not
a proof of the general theorems, certification of arbitrary multi-step
encodings, a RAM/bit-cost measurement, deployment or an independent-model
review. No additional model calls, services, workers or core changes.
Previous map and OCR tests were not rerun.
