# PSI — DECISION / EPISTEMIC LEDGER 01 — ADDENDUM 02

**Status:** `CURRENT ADDENDUM / READ WITH psi-ledger-01.md`  
**Date:** 2026-09-29  
**Agent spec:** `agent-psi-architecture-02.md`

This addendum preserves the base ledger and records material changes after E027 / D011. It introduces no new control primitive.

---

# A. Epistemic Ledger continuation

## E028 — CAT/FACT/NORM normal-form/factorization correction

- **Prior claim:** C19-v2 asserted singleton gauge-only factorization fibre for the exact Frenet/Bishop MINI.
- **New observation:** confluence/unique normal form identifies all legal grammar terms only after normalization equivalence; different segmentations need not be gauge-equivalent.
- **Minimal witness:**
  \[
  B_{[0,L]}
  \quad\text{vs}\quad
  B_{[0,a]}\oplus B_{[a,L]}.
  \]
  They can normalize to the same Bishop normal class without being identified by the declared constant normal-plane gauge alone.
- **Correction:** C19-v2 withdrawn; C19-v3 and C67 added.
- **Current exact result:**
  \[
  \boxed{|\operatorname{im}NF|=1}
  \]
  and
  \[
  \boxed{|\mathfrak F^{0}_{FB,P}(Y)/\!\equiv_{NF}|=1.}
  \]
  No singleton claim for \(\mathfrak F^{0}_{FB,P}(Y)=\operatorname{RawFact}/G_P\).
- **Regression:** F62.
- **Impact:** Freeze 01 Errata 01 required; CORE5 unchanged; Agent v02 unchanged.

## E029 — FRAME closure

C22–C24 expanded as II.15 and globally checked.

Primary datum:

\[
H_\gamma\in SO(2).
\]

Periodic transported Bishop/RMF frame iff

\[
H_\gamma=I.
\]

On the stronger globally Frenet-legal domain,

\[
H_\gamma=R_{-\int\tau ds}\pmod{2\pi}
\]

up to sign convention.

Holonomy is primary; total torsion is a coordinate on the stronger sector. No interval-to-loop inflation and no CORE change.

## E030 — HIGHER closure

C29–C33 expanded as II.16 and globally checked.

Minimal witness:

\[
*\to B\mathbb Z_2\leftarrow *
\]

with

\[
|\pi_0(*\times^h_{B\mathbb Z_2}*)|=2
\neq
1=|*\times_{\pi_0(B\mathbb Z_2)}*|.
\]

Result: task-relevant witness/stabilizer data may require richer representation; coarse truncation must pass ordinary task-adequacy testing. No sixth CORE role is forced.

## E031 — whole-V2 cross-check

`principia-v2-whole-crosscheck-01.md` checks II.1–II.16 as one theorem volume.

Result:

\[
\boxed{
\mathrm{PRINCIPIA\ V2\ II.1:II.16}
=\mathrm{MATHEMATICAL\ GLOBAL\ PASS}.
}
\]

No new mathematical errata after Freeze Errata 01.

Cross-volume locks confirmed:

- candidate/factorization fibre != task quotient != normal-form quotient;
- static task adequacy != deterministic/stochastic dynamic autonomy;
- quotient-order minimality != implementation minimality;
- interval normal form != periodic loop frame;
- coarse truncation may erase task-relevant higher data;
- classical results remain classically attributed.

## E032 — V2 control normalization

Whole-V2 audit found one control drift: Skeleton 02 still advertised stale registry pointers while carrying status `CURRENT`.

Repair:

- `principia-volume-skeleton-03.md` becomes current editorial skeleton;
- `principia-v2-theorem-map-04.md` becomes current V2 control map;
- Work Map and README updated;
- Skeleton 02, Theorem Maps 01–03 and addenda remain genealogy.

No mathematical change.

---

# B. Decision Ledger continuation

## D012 — stop FRAME/HIGHER transition until MINI factorization error repaired

- **Observation:** unique normal form did not imply singleton gauge-only factorization fibre.
- **Alternatives:** continue FRAME/HIGHER with known defect / stop and repair freeze claim.
- **Action:** stop derived-layer progression; create Freeze Errata 01, C19-v3/C67 and F62; rewrite II.14; rerun CAT/FACT/NORM cross-check.
- **Result:** `II.13–II.14 GLOBAL PASS AFTER ERRATA 01`; CORE5 unchanged.

## D013 — require FRAME and HIGHER layer gates before whole-V2 closure

- **Observation:** both layers were previously pressure results but had not yet been integrated as current V2 theorem prose after the MINI errata.
- **Action:** construct II.15 and II.16, run `principia-v2-frame-crosscheck-01.md` and `principia-v2-higher-crosscheck-01.md`.
- **Result:** both layers global PASS; no new errata.

## D014 — close V2 only after whole-volume cross-check and control normalization

- **Observation:** all local/layer units passed, but project history shows local PASS sequences do not certify the whole layer.
- **Action:** run `principia-v2-whole-crosscheck-01.md`; then normalize control pointers.
- **Result:** V2 II.1–II.16 mathematical global PASS; Skeleton 03 and Theorem Map 04 become current; next major phase released.

## D015 — release Volume III / PHISICA–LOGOS migration

- **Gate:** V1 normalized PASS + V2 mathematical global PASS + V2 control normalization.
- **Action:** move primary mathematical work to Volume III / PHISICA–LOGOS migration while keeping OPEN-PSI at WAIT and PSI-FORUM at WATCH.
- **Scope lock:** no primitive discovery unless a new typed semantic-role counterexample appears.

---

# C. Current state

\[
\boxed{
\mathrm{V1}=\mathrm{NORMALIZED\ PASS},
\qquad
\mathrm{V2}=\mathrm{MATHEMATICAL\ GLOBAL\ PASS},
}
\]

\[
\boxed{
\mathrm{CONTROL}=\mathrm{NORMALIZED\ THROUGH\ SKELETON\ 03/MAP\ 04},
}
\]

\[
\boxed{
\mathrm{NEXT}=\mathrm{VOLUME\ III/PHISICA\!\!-\!LOGOS\ MIGRATION}.
}
\]
