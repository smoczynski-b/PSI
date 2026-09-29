# PSI-MEMORY-M10-RESULT-01

**Status:** PASS  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36626907424` completed the M1–M10 memory regression suite successfully. The M10 step passed.

M10 closes the first executable memory cycle:

\[
\boxed{
\text{READ}
\to
\text{WORK / candidate delta}
\to
\text{ADMIT}
\to
\mathcal M'
\to
\text{READ}'.
}
\]

## 2. Locality witness

Anchor: `GO-G4`.

M9 admitted the verified relation

\[
\mathrm{II.9}\xrightarrow{\mathrm{DOES\_NOT\_IMPLY}}\mathrm{BIT\!\!-
MINIMALITY}.
\]

Since `II.9` is reached from `GO-G4` at distance 2, `BIT-MINIMALITY` is reached at distance 3.

The regression confirms:

### Radius 2

\[
\Delta V=0,\qquad \Delta E=0.
\]

The pre-M9 and post-M9 usable views are identical.

### Radius 3

\[
\Delta V=\{\mathrm{BIT\!\!-
MINIMALITY}\},
\]

\[
\Delta E=
\left\{
\mathrm{II.9}\xrightarrow{\mathrm{DOES\_NOT\_IMPLY}}\mathrm{BIT\!\!-
MINIMALITY}
\right\}.
\]

No other node or relation is introduced by the M9 admission.

## 3. Audit isolation

The competing M9 proposal

\[
\mathrm{II.9}\xrightarrow{\mathrm{IMPLIES}}\mathrm{BIT\!\!-
MINIMALITY}
\]

has status `CONFLICT_UNVERIFIED` in the admission ledger.

M10 verifies that it is absent from ordinary retrieval. Thus:

\[
\boxed{\mathcal M_{audit}\not\subseteq\mathcal M_{usable}.}
\]

Auditability is retained without contaminating task context.

## 4. Provenance completion discovered by M10

Before the cycle test, M10 exposed a missing field in the M9 materialized delta: it had fragment SHA-256 but not the frozen Git blob SHA of the source version.

The M9 verified delta was therefore completed with both:

- `verified_git_blob_sha`;
- `fragment_sha256`.

This restores the M7/M8 distinction:

- fragment changed -> `STALE`;
- file version changed but fragment unchanged -> `SOURCE_DRIFT`;
- both match -> `VALID`.

## 5. Reversibility test

For the newly admitted M9 evidence, M10 simulates both:

\[
\mathrm{STALE}
\]

and

\[
\mathrm{SOURCE\_DRIFT}.
\]

In either strict-retrieval case, the radius-3 view returns exactly to the pre-M9 graph state: `BIT-MINIMALITY` and its newly admitted edge disappear, while the prior verified memory remains intact.

Thus admission is not an irreversible mutation of epistemic truth; later validity state still gates use.

## 6. Architectural conclusion

After M10 the experimental memory supports a complete bounded loop with distinct roles:

\[
\boxed{
\mathcal M
\xrightarrow{\mathfrak R^{VALID}_{a,r}}
C_{task}
\xrightarrow{A_i}
\Delta_i
\xrightarrow{\mathfrak A_c}
\mathcal M'
\xrightarrow{\mathfrak R^{VALID}_{a,r}}
C'_{task}.
}
\]

The observed invariant is locality:

\[
\boxed{
\Delta C_{task}
=
\text{only the newly admitted verified structure reachable under the task budget}.
}
\]

## 7. Boundary

M10 remains an engineering/regression result on the present PSI memory sample. It does not establish independent multi-model quality gains, a general semantic verifier, or optimal graph selection.

The next architectural test should concern **growth under repeated admission** rather than another single-delta example: multiple sequential deltas, supersession/revocation, and bounded context stability as the verified graph becomes materially larger.
