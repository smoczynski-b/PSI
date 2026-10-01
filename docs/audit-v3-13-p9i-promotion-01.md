# PRINCIPIA SEMANTICA — III.13 / P9-I PROMOTION AUDIT 01

**Status:** `PROMOTION VERIFIED / COMPOSITION VERIFIED / CONTROL-REGISTRY DRIFT REPAIRED`  
**Date:** 2026-10-01  
**Scope:** bounded audit of the already-promoted `III.13` unit and its control-state closure.  
**Does not modify:** theorem content, CORE5, CANON-03, general P9 status.

---

## 1. Promoted theorem

The numbered unit

`principia-v3-13-p9i-hilbert-resolvent-growth-bridge.md`

is present and records, for a densely defined closed generator

\[
A:D(A)\subset\mathcal H\to\mathcal H
\]

of a strongly continuous **linear** semigroup on a complex Hilbert space,

\[
\boxed{\omega_0(T)=s_0(A)}.
\]

Classification remains `CLASSICAL / ADAPTED` via Gearhart–Prüss–Huang. No PSI novelty claim is attached to the classical equality.

The proof source is

`principia-v3-p9i-theorem-selection-proof-gate-01.md`.

---

## 2. Composition closure

`principia-v3-p9i-composition-crosscheck-01.md` records

\[
\boxed{\mathrm{III.7:III.13}=\mathrm{COMPOSITION\ PASS}}.
\]

The cross-check preserves the required distinctions:

- scalar exponential abscissa != full resolvent/semigroup profile;
- projectability != stability;
- well-posedness/generation != the III.13 bridge;
- linear C0-semigroup != nonlinear semigroup or nonautonomous evolution family;
- III.13 != construction of a coercive Lyapunov metric;
- \(\omega_0=s_0=0\) != uniform boundedness;
- Hilbert theorem != arbitrary Banach theorem.

The frozen HCube pair remains an exact composition witness: equal coarse abscissae coexist with different full resolvent-norm profiles.

---

## 3. Control drift found during promotion audit

The theorem/composition layer was already complete when this audit began. A separate control-layer drift remained:

```text
falsifier-registry-13.md contained F63-F64
but
stable docs/falsifier-registry.md was still materialized only through F62
and control-state.json still recorded F = 62.
```

This did not falsify III.13, but it contradicted the repository rule that the stable current registry is the materialized public C/F layer.

The drift was repaired by:

1. materializing F63 and F64 into `docs/falsifier-registry.md`;
2. updating its header to materialization through registry 13 and 64 entries;
3. changing `control-state.json` registry count to `F = 64` and binding the stable registry to `falsifier-registry-13.md` in the supersedes graph;
4. adding a control-validator guard requiring the latest numbered claim/falsifier snapshot to be represented by the stable materialization;
5. adding a mutation regression showing that a new numbered falsifier snapshot without materialization is rejected.

The one-shot repair workflow used to perform the deterministic concatenation was removed after successful execution.

---

## 4. Permanent locks

F63 and F64 are now present in both the numbered registry 13 and the stable materialized registry.

- **F63:** imaginary-axis resolvent boundedness alone does not imply exponential stability for an arbitrary Hilbert-space C0-semigroup.
- **F64:** finite/infinite-dimensional Kreiss export does not give a dimension-free uniform-boundedness theorem.

They remain falsifier/regression locks, not CORE5 primitives.

---

## 5. Verdict

\[
\boxed{
\mathrm{III.13}=\mathrm{PASS/COMPOSITION\ PASS}
\]

and

\[
\boxed{
P9_{\rm general}=\mathrm{OPEN/CENTRAL}.
\]

The promotion audit introduces no automatic `III.14` candidate.

`NEXT_AUTOMATIC = NONE` remains correct; a new mathematical theorem front requires explicit selection and a fresh typed source/contract gate.
