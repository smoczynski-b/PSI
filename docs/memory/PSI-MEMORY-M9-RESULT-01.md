# PSI-MEMORY-M9-RESULT-01

**Status:** PASS  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36625841303` executed M1–M9 successfully.

M9 used two synthetic agent delta fixtures (`AGENT-A`, `AGENT-B`) to test write-side governance. These are not claimed to be independent LLM executions.

The write contract was:

\[
\boxed{\text{agent output}\to\mathrm{CANDIDATE}\to\text{evidence-gated admission}.}
\]

The regression verified:

- arrival-order invariance: PASS;
- author identity grants no authority: PASS;
- identical thin-node proposals coalesce: PASS;
- duplicate verified relations do not grow the graph: PASS;
- a bounded source-supported relation can become `VERIFIED`: PASS;
- a competing unsupported relation remains `CONFLICT_UNVERIFIED`: PASS;
- no M9 candidate becomes `CANON`: PASS.

## 2. Admitted delta

Exactly two new verified memory objects were admitted:

1. thin node `BIT-MINIMALITY`;
2. relation

\[
\boxed{\mathrm{II.9}\xrightarrow{\mathrm{DOES\_NOT\_IMPLY}}\mathrm{BIT\!\!-
MINIMALITY}.}
\]

Both are licensed by the bounded source section `## 12. Granice II.9`, with fragment SHA-256

`910b450abde13f721fd5429494a873b116f3ca0e959a416aac3583bf028497ca`

and fragment size `399` bytes.

The verified delta is materialized separately from the admission ledger in `psi-memory-m9-verified-delta-01.tsv`.

## 3. Conflict retention

Agent B proposed the competing relation

\[
\mathrm{II.9}\xrightarrow{\mathrm{IMPLIES}}\mathrm{BIT\!\!-
MINIMALITY}.
\]

It was not silently deleted and not admitted to the verified layer. Its status is:

\[
\boxed{\mathrm{CONFLICT\_UNVERIFIED}}.
\]

The source fragment used by the candidate does not license that direction.

Thus the architecture separates:

\[
\boxed{\text{audit memory}\neq\text{usable verified memory}.}
\]

## 4. Duplicate suppression

Both agents also proposed the already verified relation

\[
\mathrm{GO\!\!-
G4}\xrightarrow{\mathrm{SUPPORTS}}\mathrm{SSK\!\!-
MEMORY}.
\]

Both submissions were classified `DUPLICATE_VERIFIED`; no duplicate edge was added.

## 5. Multi-agent invariant

M9 explicitly checks

\[
\boxed{
\operatorname{Admit}(\Delta_A,\Delta_B)
=
\operatorname{Admit}(\Delta_B,\Delta_A).
}
\]

This is the first concurrency-relevant invariant of PSI-MEMORY: the epistemic result may not depend on which agent's packet arrived first.

## 6. Architectural conclusion

After M9 the experimental memory has distinct read and write operators:

\[
\mathfrak R^{VALID}_{a,r}(\mathcal M)
\]

for bounded retrieval, and

\[
\mathfrak A_c(\mathcal M,\Delta_1,\ldots,\Delta_n)
\]

for contract-relative admission of candidate deltas.

The important separation is:

\[
\boxed{\text{agent may propose}\neq\text{agent may certify}\neq\text{agent may canonize}.}
\]

## 7. Boundary

M9 does not establish a general semantic verifier for arbitrary natural-language relations. Its verifier is deliberately narrow and contract-specific. It validates the governance architecture: candidate isolation, provenance, coalescence, duplicate suppression, conflict retention and deterministic admission.

A real multi-model experiment still requires independent model executions rather than synthetic delta fixtures.

## 8. Next target

The next useful test is M10: integrate the M9 verified delta into a task retrieval view while leaving the conflict only in the audit layer, then verify that retrieval changes exactly where the newly admitted relation makes it relevant and nowhere else.
