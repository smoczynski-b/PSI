# PRINCIPIA SEMANTICA — current Volume 3 theorem map

**Control role:** `theorem-map-v3`

**Status:** `CURRENT / III.1:III.14 RECORDED / III.7:III.14 COMPOSITION PASS / P9 GENERAL OPEN`  
**Date:** 2026-10-01  
**Current historical snapshot:** [principia-v3-theorem-map-12.md](principia-v3-theorem-map-12.md)

---

# 1. Current closure

The recorded Volume III stack now includes:

\[
\boxed{\mathrm{III.1:III.6\ PHISICA}=GLOBAL\ PASS}
\]

\[
\boxed{\mathrm{III.7:III.8\ MOST/HCube}=GLOBAL\ PASS}
\]

\[
\boxed{\mathrm{III.9\ DOM\!-\!LOGOS}=PASS}
\]

\[
\boxed{\mathrm{III.10\ SOP\!-\!11E}=SECTOR\ PASS}
\]

\[
\boxed{\mathrm{III.11\ P9\!-\!G}=PASS}
\]

\[
\boxed{\mathrm{III.12\ P9\!-\!H}=CONDITIONAL\ PASS}
\]

\[
\boxed{\mathrm{III.13\ P9\!-\!I}=PASS}
\]

\[
\boxed{\mathrm{III.14\ P9\!-\!POLY}=PASS}
\]

with

\[
\boxed{P2_{\rm general}=PARTIAL},
\qquad
\boxed{P9_{\rm general}=OPEN/CENTRAL}.
\]

---

# 2. III.14 — polynomial resolvent / regularized-decay bridge

For a bounded linear \(C_0\)-semigroup \(T(t)\) on a complex Hilbert space, with generator \(A\),

\[
i\mathbb R\subset\rho(A),
\qquad
\alpha>0,
\]

III.14 records the Borichev–Tomilov equivalence, in particular

\[
\boxed{
\|R(is,A)\|=O(|s|^\alpha)
\Longleftrightarrow
\|T(t)A^{-1}\|=O(t^{-1/\alpha})
}
\]

under the precise asymptotic convention and equivalent formulations in the theorem unit.

The target quantity is regularized dynamics, not the raw semigroup norm. The theorem is `CLASSICAL / ADAPTED`, not `PSI-NEW`.

Primary unit: [III.14](principia-v3-14-p9-poly-resolvent-regularized-decay.md).  
Typed source review: [P9-POLY review](source-review-v3-14-p9-poly-01.json).  
Typed source gate: [P9-POLY gate](source-gate-v3-14-p9-poly-01.json).

---

# 3. Composition status

The typed composition record is now

\[
\boxed{\mathrm{III.7:III.14}=\mathrm{COMPOSITION\ PASS}.}
\]

Permanent distinctions include

\[
\boxed{
\text{full resolvent profile}\neq\text{full semigroup profile},
}
\]

\[
\boxed{
\omega_0=s_0\neq\text{polynomial regularized-decay data},
}
\]

and

\[
\boxed{T(t)A^{-1}\neq T(t).}
\]

F63 and F64 remain active boundaries. III.14 also retains boundedness of the semigroup, \(i\mathbb R\subset\rho(A)\), the Hilbert/Banach boundary and the distinction between operator-norm \(O\) and pointwise \(o\).

---

# 4. Current front

III.14 is closed under its typed bounded Hilbert linear \(C_0\)-semigroup contract. The unrestricted P9 problem remains `OPEN/CENTRAL`; no automatic III.15 is licensed.

Scheduling is governed by [work-map.md](work-map.md), not by theorem adjacency alone.

No CORE5 change and no Agent v03 witness.


## Recorded unit status (control view)

<!-- BEGIN CONTROL STATUS -->
| Unit | Recorded status | Evidence |
|---|---|---|
| III.1 | PASS_AFTER_ERRATA | [unit](principia-v3-01-lambda-operator-projectability.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.2 | PASS_AFTER_ERRATA | [unit](principia-v3-02-weight-sturm-liouville.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.3 | PASS_AFTER_ERRATA | [unit](principia-v3-03-domain-selfadjoint.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.4 | PASS_AFTER_ERRATA | [unit](principia-v3-04-compact-resolvent-spectrum.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.5 | PASS_AFTER_ERRATA | [unit](principia-v3-05-liouville-normal-form.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.6 | PASS_AFTER_ERRATA | [unit](principia-v3-06-perturbation-hellmann-feynman.md) / [audit](principia-v3-phisica-whole-crosscheck-01.md) |
| III.7 | PASS | [unit](principia-v3-07-spectral-information-hierarchy-most.md) / [audit](principia-v3-most-hcube-whole-crosscheck-01.md) |
| III.8 | PASS | [unit](principia-v3-08-hcube-nonnormal-resolvent-lab.md) / [audit](principia-v3-most-hcube-whole-crosscheck-01.md) |
| III.9 | PASS | [unit](principia-v3-09-semigroup-projectability-dom-logos.md) / [audit](principia-v3-dom-logos-crosscheck-01.md) |
| III.10 | SECTOR_PASS | [unit](principia-v3-10-sop11e-wellposedness-sectors.md) / [audit](principia-v3-sop11e-dom-logos-crosscheck-01.md) |
| III.11 | PASS | [unit](principia-v3-11-p9-metric-gradient-bridge.md) / [audit](principia-v3-p9-composition-crosscheck-01.md) |
| III.12 | CONDITIONAL_PASS | [unit](principia-v3-12-hypocoercive-modified-energy-bridge.md) / [audit](principia-v3-p9h-composition-crosscheck-01.md) |
| III.13 | PASS | [unit](principia-v3-13-p9i-hilbert-resolvent-growth-bridge.md) / [audit](source-review-v3-13-p9i-01.json) |
| III.14 | PASS | [unit](principia-v3-14-p9-poly-resolvent-regularized-decay.md) / [audit](source-review-v3-14-p9-poly-01.json) |
<!-- END CONTROL STATUS -->
