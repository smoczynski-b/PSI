# PSI — claim registry 10

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-09.md` as current public registry  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`

This version adds `FS-STAT-01`. CORE5 and Agent Architecture v02 remain unchanged.

## Retained claims C01–C47

Retain C01–C47 from `claim-registry-09.md` without semantic change.

---

## C48 — finite-difference derivative conditioning

For uniformly sampled noisy trajectory data with bounded deterministic observation error `||ε_j||≤δ`, the centered derivative stencils satisfy, at interior points,

\[
\|\widehat d_1-\gamma'\|
\le
\frac{M_3}{6}h^2+\frac{\delta}{h},
\]

\[
\|\widehat d_2-\gamma''\|
\le
\frac{M_4}{12}h^2+\frac{4\delta}{h^2},
\]

\[
\|\widehat d_3-\gamma'''\|
\le
\frac{M_5}{4}h^2+\frac{3\delta}{h^3}.
\]

**STATUS:** `CLASSICAL NUMERICAL-ANALYSIS FACT / EXACT REGRESSION`  
**ROLE:** `FS-STAT CONDITIONING`.

---

## C49 — low-curvature torsion instability

For

\[
\gamma_{\varepsilon,\omega}(s)
=
(s,\varepsilon\cos\omega s,\varepsilon\sin\omega s),
\]

\[
\kappa_{\varepsilon,\omega}
=
\frac{\varepsilon\omega^2}{1+\varepsilon^2\omega^2},
\qquad
\tau_{\varepsilon,\omega}
=
\frac{\omega}{1+\varepsilon^2\omega^2}.
\]

As `ε→0`, the curves converge in `C^3` on compact intervals to the same straight line and `κ→0`, while `τ→ω`.

Thus classical Frenet torsion has no continuous extension through the zero-curvature straight-line stratum and cannot be uniformly stably recovered over classes allowing `κ→0`.

**STATUS:** `EXACT COUNTEREXAMPLE / STABILITY BOUNDARY`.

---

## C50 — uncertainty-driven Frenet/Bishop gate

A Frenet/torsion representation is licensed only when the protocol certifies the cross-product denominator away from zero strongly enough for the task error tolerance.

If derivative errors satisfy

\[
\|\widehat d_1-\gamma'\|\le\eta_1,
\qquad
\|\widehat d_2-\gamma''\|\le\eta_2,
\]

a conservative lower bound can be formed from

\[
\widehat w=\|\widehat d_1\times\widehat d_2\|
\]

and a cross-product error radius. If the certified lower bound is inadequate for the requested torsion precision, the legal status is

\[
\boxed{\mathrm{FRENET\ UNRESOLVED}\to\mathrm{BISHOP}.}
\]

This is not evidence that true curvature is exactly zero.

**STATUS:** `POLICY / STABLE-IDENTIFIABILITY GATE`.

---

## C51 — exact/stable/confidence distinction

The project must distinguish

\[
\boxed{
\mathrm{ID}_{\rm exact}
\mid
\mathrm{ID}_{\rm stable}
\mid
\mathrm{CONF}_{1-\alpha}.
}
\]

Exact uniqueness does not imply perturbation stability, and perturbation stability does not by itself supply probabilistic confidence coverage.

**STATUS:** `CORE-ADJACENT POLICY / STATISTICAL DISCIPLINE`.

---

## C52 — confidence requires a probability contract

Under bounded deterministic noise alone, no frequentist confidence statement is licensed.

Under an explicit probabilistic model such as iid Gaussian coordinate noise, regularized derivative estimators may carry model-relative covariance/confidence statements after bias control.

**STATUS:** `CLASSICAL STATISTICAL DISCIPLINE / POLICY`.

---

## C53 — local polynomial derivative layer is imported classical machinery

Local polynomial regression provides regularized derivative estimates with classical bias/variance and asymptotic-normality theory under standard smoothness/design assumptions.

`FS-STAT-01` uses this machinery but does not claim it as new PSI mathematics.

**STATUS:** `CLASSICAL / ADAPTED`  
**ROLE:** `FS-STAT ESTIMATION LAYER`.

---

## C54 — flatness test boundary

A pointwise test `H0,t: τ(t)=0` is legal only in a certified Frenet sector after bias and variance control.

Failure of the Frenet gate is not evidence for `τ=0`.

A global interval claim

\[
H_0:\tau\equiv0
\]

requires simultaneous/global inference and remains OPEN in the current FS-STAT layer.

**STATUS:** `PARTIAL / OPEN`.

---

## C55 — quotient-level confidence remains open

A confidence set on Bishop normal classes modulo `SO(2)` is a legitimate PSI-STAT target, but coordinatewise intervals do not automatically induce valid quotient-level coverage.

Coverage on the quotient requires a separate asymptotic/bootstrap argument, especially near singular orbit strata.

**STATUS:** `OPEN / BRIDGE`.

---

## C56 — FS-STAT hardening verdict

`CAT–FACT–NORM–MINI-01` remains exact, but transport to sampled/noisy data requires additional conditioning/statistical hypotheses.

No CORE primitive or Agent control primitive is added.

**STATUS:** `HARDENING RESULT / NO CORE CHANGE`.

---

## Current phase

The first post-R4 hardening triad is complete:

\[
\boxed{
\mathrm{HCube}
+
\mathrm{Go}
+
\mathrm{FS\!-\!STAT}
\to
\mathrm{REGRESSION\ BANK\ 01}.
}
\]

`REGRESSION-BANK-01` is assembled. Current work moves to **Principia V1/V2 unit construction, source/proof/regression binding, and first V1/V2 freeze**.