# PRINCIPIA SEMANTICA — current Volume 3 theorem map

**Control role:** `theorem-map-v3`

**Status:** `CURRENT / PHISICA GLOBAL PASS / MOST-HCUBE GLOBAL PASS / III.9 DOM-LOGOS PASS / III.10 SOP-11E PASS / III.11 P9-G PASS / III.12 P9-H PASS / P9-INFINITE-DIMENSIONAL GATE NEXT`  
**Date:** 2026-09-29  
**Historical source:** [principia-v3-theorem-map-08.md](principia-v3-theorem-map-08.md)

---

# 1. Closed blocks

\[
\boxed{\mathrm{III.1:III.6\ PHISICA}=GLOBAL\ PASS}
\]

\[
\boxed{\mathrm{III.7:III.8\ MOST/HCube}=GLOBAL\ PASS}
\]

\[
\boxed{\mathrm{III.9\ DOM\!-
LOGOS}=PASS/COMPOSITION\ PASS}
\]

\[
\boxed{\mathrm{III.10\ SOP\!-
11E}=SECTOR\ PASS}
\]

\[
\boxed{\mathrm{III.11\ P9\!-
G}=PASS}
\]

\[
\boxed{\mathrm{III.12\ P9\!-
H}=PASS}
\]

with

\[
\boxed{P2_{\rm general}=PARTIAL},
\qquad
\boxed{P9_{\rm general}=OPEN/CENTRAL}.
\]

---

# 2. III.12 — modified-energy / hypocoercive bridge

Contract:

\[
A:D(A)\subset\mathcal H\to\mathcal H
\]

generates a \(C_0\)-semigroup, and there exists bounded coercive

\[
Q=Q^*,
\qquad
mI\le Q\le MI,
\]

such that

\[
A^*Q+QA\le-2\lambda Q.
\]

Then

\[
\boxed{\|e^{tA}\|_Q\le e^{-\lambda t}},
\]

\[
\boxed{\|e^{tA}\|\le\sqrt{\kappa(Q)}e^{-\lambda t}},
\]

\[
\boxed{
\|(zI-A)^{-1}\|_Q
\le
(\Re z+\lambda)^{-1}
\quad(\Re z>-\lambda),
}
\]

\[
\boxed{
\|(zI-A)^{-1}\|
\le
\frac{\sqrt{\kappa(Q)}}{\Re z+\lambda},
}
\]

and

\[
\boxed{
\mathcal K_Q(A)=1,
\qquad
1\le\mathcal K(A)\le\sqrt{\kappa(Q)}.
}
\]

The ambient pseudospectral right edge satisfies

\[
\boxed{
\sup\Re\sigma_\varepsilon(A)
\le
-\lambda+\sqrt{\kappa(Q)}\,\varepsilon.
}
\]

---

# 3. Hypocoercivity correction

For

\[
A=S+N,
\quad S=S^*\le0,
\quad N^*=-N,
\]

the ambient norm is non-increasing. Thus hypocoercivity is not a theorem of unavoidable transient amplification.

Its role is to recover strict exponential decay from degenerate direct dissipation by constructing an adapted equivalent metric.

DMS provides such a construction only under typed kinetic hypotheses H1–H4.

---

# 4. III.11–III.12 relation

III.11 is a special case of III.12:

\[
Q=G,
\qquad
A=-G^{-1}H,
\qquad
A^*G+GA=-2H\le-2\mu_GG.
\]

III.11 is stronger within its subclass because the metric transport yields a self-adjoint normal form. III.12 requires only strict dissipativity in an equivalent metric.

---

# 5. Composition status

`principia-v3-p9h-composition-crosscheck-01.md` establishes

\[
\boxed{
\mathrm{III.7:III.12}=\mathrm{COMPOSITION\ PASS}.
}
\]

Permanent distinctions now include:

\[
\boxed{
\text{hypocoercive decay}\neq\text{transient growth}},
\]

\[
\boxed{
\text{Kreiss amplification index}\neq\text{decay/growth margin}},
\]

\[
\boxed{
\text{modified metric}\Rightarrow\text{new norm-sensitive operator representation}.
}
\]

---

# 6. Current open front

The next unresolved P9 class is genuinely infinite-dimensional:

- unbounded generators;
- continuous spectrum;
- resolvent-to-growth equivalence beyond finite-dimensional Kreiss;
- Gearhart–Prüss type conditions;
- failure modes outside Hilbert or outside uniform resolvent control.

No III.13 theorem is authorized yet.

The next admissible mathematical gate, subject to [global work selection](work-map.md), is

\[
\boxed{
\mathrm{P9\!-
I\ INFINITE\!-
DIMENSIONAL\ RESOLVENT/GROWTH\ SOURCE\ GATE\ NEXT}.
}
\]

No CORE5 change and no Agent v03 witness.
Scheduling is governed by [work-map.md](work-map.md), not by mathematical adjacency alone.


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
<!-- END CONTROL STATUS -->
