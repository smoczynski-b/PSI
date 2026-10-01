# PSI-MEMORY-M9-WRITE-01 — multi-agent write-side admission

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can two agents submit memory deltas without either agent obtaining direct authority to mutate verified memory, while the system preserves duplicates, conflicts, provenance and deterministic admission?

The write-side contract is:

\[
\boxed{\text{agent output}\to\mathrm{CANDIDATE}\to\text{admission gate}\to\{\mathrm{VERIFIED},\mathrm{UNVERIFIED},\mathrm{CONFLICT}\}.}
\]

No M9 path promotes an object to `CANON`.

## 1. Witness

Both agents inspect the existing II.9 / Go-memory sector.

Agent A proposes:

1. thin node `BIT-MINIMALITY`;
2. `II.9 --DOES_NOT_IMPLY--> BIT-MINIMALITY`;
3. an already-known `GO-G4 --SUPPORTS--> SSK-MEMORY` edge.

Agent B proposes:

1. the same thin node `BIT-MINIMALITY`;
2. the competing edge `II.9 --IMPLIES--> BIT-MINIMALITY`;
3. the same already-known Go edge.

The bounded II.9 source section states that II.9 *does not establish bit minimality*. Therefore the negative relation can be admitted under this experiment's explicit verifier, whereas the competing positive direction cannot.

## 2. Admission requirements

The gate must satisfy all of the following:

- agent identity grants no epistemic authority;
- arrival order does not change the canonical admission result;
- identical thin-node proposals coalesce instead of duplicating memory;
- an already verified relation is returned as `DUPLICATE_VERIFIED`, not written again;
- a supported relation may become `VERIFIED`;
- a competing unsupported relation remains auditable as `CONFLICT_UNVERIFIED`;
- no candidate becomes `CANON`;
- source evidence is bounded by an explicit selector, not a full-file reread.

## 3. Scope boundary

M9 is not a general natural-language theorem prover. The verifier is deliberately narrow and contract-specific. It tests write-side governance, deterministic coalescence and conflict retention.

The experiment does **not** claim that arbitrary proposed relations can be semantically verified from text without a domain-specific verifier or human/mathematical proof procedure.

## 4. Success predicate

M9 passes iff:

\[
\boxed{\operatorname{Admit}(\Delta_A,\Delta_B)=\operatorname{Admit}(\Delta_B,\Delta_A)}
\]

and the admitted delta contains exactly:

- one canonical thin node `BIT-MINIMALITY`;
- one new verified relation `II.9 DOES_NOT_IMPLY BIT-MINIMALITY`;

while the opposite relation remains `CONFLICT_UNVERIFIED` and the repeated Go relation produces no graph growth.
