# PSI — Decision / Epistemic Ledger 01 — ADDENDUM 01

**Status:** `ACTIVE ADDENDUM / 2026-09-29`

## E023 — MINI normal-form / factorization-fibre correction

- **Prior status:** C19-v2 treated the restricted gauge-only MINI factorization fibre as singleton after proving rewrite confluence.
- **New observation:** two grammar terms such as
  \[
  B_{[0,L]}
  \quad\text{and}\quad
  B_{[0,a]}\oplus B_{[a,L]}
  \]
  need not be gauge-equivalent although they normalize to the same Bishop class.
- **Diagnosis:** unique normal form was conflated with literal factorization uniqueness modulo gauge.
- **Result:** C19-v2 withdrawn; C19-v3 + C67 registered; F62 added; `cat-fact-norm-mini-02.md` becomes current corrected MINI source.
- **Freeze impact:** Freeze 01 Errata 01 required; CORE5 unchanged.

## D011 — stop FRAME until MINI correction closed

- **Observation:** whole CAT/FACT/NORM cross-check exposed a mathematical defect in the frozen MINI statement.
- **Alternatives:** continue to FRAME / halt and repair frozen theorem.
- **Action:** halt downstream prose, create corrected MINI-02, Claim Registry v13, Falsifier Registry v12, Freeze 01 Errata 01, corrected II.14 and global CAT/FACT/NORM cross-check.
- **Gate:** Agent v02 `IMPACT → REGRESSION → HANDOFF` discipline.
- **Result:**
  \[
  \boxed{
  \mathrm{II.13:II.14}
  =\mathrm{GLOBAL\ PASS\ AFTER\ ERRATA\ 01}.
  }
  \]
- **Release:** FRAME C22–C24 is legal only after this correction stack is current.

## Permanent lesson

\[
\boxed{
\text{confluence/unique normal form}
\not\Rightarrow
\text{singleton pre-normal candidate fibre}.
}
\]

Gauge equivalence, rewrite/recode equivalence and task equivalence must remain separately typed.
