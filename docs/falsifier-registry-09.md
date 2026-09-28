# PSI — falsifier registry 09

**Status:** ACTIVE / TEST GOVERNANCE  
**Supersedes:** `falsifier-registry-08.md` as current public registry.

Retain F01–F45 from v08 without semantic change.

---

## F46 — exact-to-stable inflation

**TARGET:** any inference

\[
\mathrm{ID}_{\rm exact}
\Rightarrow
\mathrm{ID}_{\rm stable}.
\]

**FALSIFIER:** a perturbation family for which exact parameters remain mathematically defined away from the boundary but their recovery condition number diverges.

**FIXED WITNESS:** the low-curvature helix family in `FS-STAT-01`.

**VERDICT:** exact uniqueness alone does not license finite-sample stability.

---

## F47 — low-curvature torsion stability

**TARGET:** any claim of uniform torsion stability over a class allowing `κ→0`.

**FIXED WITNESS:**

\[
\gamma_{\varepsilon,\omega}(s)
=(s,\varepsilon\cos\omega s,\varepsilon\sin\omega s).
\]

As `ε→0`, `γ_{ε,ω}` converges in `C^3` to a line while `τ_{ε,ω}→ω`.

**VERDICT:** no continuous torsion extension / no uniform stable recovery through the zero-curvature stratum.

**REGRESSION:** YES.

---

## F48 — dense-sampling finite-difference inflation

**TARGET:** any inference

\[
\Delta\downarrow0
\Rightarrow
\text{raw derivative estimation improves at fixed observation noise}.
\]

**ORACLE:** finite-difference noise amplification.

For derivative order `r`, the raw noise term scales like a negative power of the stencil step; in the explicit stencils used by FS-STAT:

\[
\operatorname{Var}(\widehat d_1)\propto h^{-2},
\quad
\operatorname{Var}(\widehat d_2)\propto h^{-4},
\quad
\operatorname{Var}(\widehat d_3)\propto h^{-6}.
\]

**VERDICT:** smoothing/bandwidth selection is required.

---

## F49 — universal curvature threshold

**TARGET:** any hard-coded universal rule such as

`if κ < constant then switch to Bishop`

without reference to sampling, noise, derivative uncertainty or task tolerance.

**ORACLE:** require a certified denominator/error budget.

**VERDICT:** universal threshold prohibited; switch must be protocol-relative.

---

## F50 — confidence-without-probability-model

**TARGET:** a claimed confidence level under only deterministic bounded noise.

**FALSIFIER:** no declared sampling distribution / probability law from which coverage is defined.

**VERDICT:** confidence claim invalid. Use deterministic uncertainty bounds instead.

---

## F51 — torsion-test outside Frenet gate

**TARGET:** pointwise or global `H0: τ=0` inference when `||γ'×γ''||` is not certified away from zero.

**VERDICT:** blocked. Failure to identify torsion is not evidence of zero torsion.

---

## F52 — pointwise-to-global flatness inflation

**TARGET:** inference

\[
\text{pointwise non-rejection/rejection pattern}
\Rightarrow
\tau\equiv0\text{ or }\tau\not\equiv0\text{ globally}
\]

without simultaneous/global error control.

**VERDICT:** prohibited. Global planarity needs a simultaneous band or global statistic.

---

## F53 — Bishop-is-noiseless inflation

**TARGET:** any inference

\[
\text{Bishop avoids Frenet singularity}
\Rightarrow
\text{Bishop estimation is immune to sampling/noise}.
\]

**VERDICT:** prohibited. Bishop removes the singular division by curvature but still depends on estimated tangent/transport data.

---

## F54 — quotient-confidence inflation

**TARGET:** coordinatewise confidence intervals claimed to imply valid coverage of the quotient class `[k]_{SO(2)}`.

**ORACLE:** require an explicit quotient metric/alignment plus bootstrap/asymptotic coverage proof.

**CURRENT VERDICT:** OPEN; not supplied by FS-STAT-01.

---

## PASS inflation rule

Every run report must contain both:

`WHAT FAILED / PASSED`

and

`WHAT THIS RESULT DOES NOT TEST`.

## Promotion gate

A non-classical claim may move toward stable theorem status only after

\[
\boxed{\text{typed hypotheses}+\text{proof/test}+\text{real falsifier}+\text{oracle}+\text{scope}.}
\]

For classical theorems, proof and provenance take precedence over manufactured pseudo-falsification.