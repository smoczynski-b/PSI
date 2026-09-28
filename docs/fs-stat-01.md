# PSI — FS-STAT-01

**Status:** COMPLETED HARDENING REGRESSION / PARTIAL STATISTICAL BRIDGE / NO CORE CHANGE  
**Date:** 2026-09-28  
**Parent:** `CAT–FACT–NORM–MINI-01`  
**Agent:** PSI Agent Architecture v02

## 0. Purpose

`CAT–FACT–NORM–MINI-01` is exact and noiseless. It explicitly does **not** imply stable recovery from sampled noisy trajectories.

This run asks:

\[
\boxed{
\text{when do finite sampling and observation noise preserve enough differential information}
\text{ to recover the Frenet/Bishop task data stably?}
}
\]

This is a hardening/regression problem, not primitive discovery.

The historical closure program requested:

- regularized estimators of `v, κ, τ`;
- confidence intervals;
- Frenet/Bishop switching;
- a flatness test `H0: τ=0`;
- stability under sampling and noise.

The present run establishes the conditioning boundary and a legal statistical protocol. It does **not** claim a new general theorem of nonparametric statistics.

---

## 1. Contract snapshot

Let

\[
\gamma:[0,T]\to\mathbb R^3
\]

be a fixed time-parametrized curve.

For the deterministic layer assume

\[
\gamma\in C^5,
\qquad
\|\dot\gamma(t)\|\ge v_0>0.
\]

Samples are observed at a uniform grid

\[
t_j=j\Delta,
\]

through

\[
Y_j=\gamma(t_j)+\varepsilon_j.
\]

Two noise contracts are kept separate.

### D∞ — bounded deterministic noise

\[
\boxed{\|\varepsilon_j\|\le\delta.}
\]

No confidence statement is legal under D∞ alone.

### G — Gaussian sampling model

For the statistical layer only, assume

\[
\boxed{
\varepsilon_j\stackrel{iid}{\sim}N(0,\sigma^2I_3)
}
\]

or an explicitly declared replacement model with corresponding inference theory.

Time reparameterization remains outside the gauge, as in MINI-01.

---

## 2. Differential targets

Write

\[
a=\gamma',
\qquad
b=\gamma'',
\qquad
c=\gamma'''.
\]

Then

\[
v=\|a\|,
\]

\[
\kappa=\frac{\|a\times b\|}{\|a\|^3},
\]

and wherever

\[
w:=\|a\times b\|>0,
\]

\[
\tau
=
\frac{\det(a,b,c)}{\|a\times b\|^2}.
\]

The denominator of torsion is therefore exactly the object that becomes singular as curvature tends to zero.

---

## 3. Explicit finite-difference noise amplification

Let `h=mΔ` be an effective stencil step at an interior point. Use

\[
\widehat d_1
=
\frac{Y(t+h)-Y(t-h)}{2h},
\]

\[
\widehat d_2
=
\frac{Y(t+h)-2Y(t)+Y(t-h)}{h^2},
\]

and

\[
\widehat d_3
=
\frac{Y(t+2h)-2Y(t+h)+2Y(t-h)-Y(t-2h)}{2h^3}.
\]

Let

\[
M_r=\sup_{u\in[t-2h,t+2h]}\|\gamma^{(r)}(u)\|.
\]

Under D∞, Taylor expansion plus the stencil coefficient norms give

\[
\boxed{
\|\widehat d_1-a\|
\le
\eta_1(h)
:=
\frac{M_3}{6}h^2+\frac{\delta}{h}.
}
\]

Similarly,

\[
\boxed{
\|\widehat d_2-b\|
\le
\eta_2(h)
:=
\frac{M_4}{12}h^2+\frac{4\delta}{h^2}.
}
\]

and

\[
\boxed{
\|\widehat d_3-c\|
\le
\eta_3(h)
:=
\frac{M_5}{4}h^2+\frac{3\delta}{h^3}.
}
\]

Thus decreasing the stencil step reduces truncation bias but amplifies observation error increasingly strongly with derivative order.

At the level of scaling, balancing the two terms gives

\[
h_1\asymp\delta^{1/3},
\qquad
\eta_1\asymp\delta^{2/3},
\]

\[
h_2\asymp\delta^{1/4},
\qquad
\eta_2\asymp\delta^{1/2},
\]

\[
h_3\asymp\delta^{1/5},
\qquad
\eta_3\asymp\delta^{2/5}.
\]

These are conditioning statements for the fixed stencils, not minimax statistical theorems.

---

## 4. Exact Gaussian variance of the same raw stencils

Under contract G, before bias correction,

\[
\operatorname{Cov}(\widehat d_1\mid t_j)
=
\frac{\sigma^2}{2h^2}I_3,
\]

\[
\operatorname{Cov}(\widehat d_2\mid t_j)
=
\frac{6\sigma^2}{h^4}I_3,
\]

\[
\operatorname{Cov}(\widehat d_3\mid t_j)
=
\frac{5\sigma^2}{2h^6}I_3.
\]

Therefore raw finite differences are not a consistent small-step procedure at fixed noise variance: variance diverges as `h→0`.

This is the reason FS-STAT requires smoothing/regularization rather than simply denser differencing.

---

## 5. Propagation to geometric invariants

Define plug-in estimates

\[
\widehat v=\|\widehat d_1\|,
\]

\[
\widehat\kappa
=
\frac{\|\widehat d_1\times\widehat d_2\|}
{\|\widehat d_1\|^3},
\]

and, when the denominator is certified away from zero,

\[
\widehat\tau
=
\frac{\det(\widehat d_1,\widehat d_2,\widehat d_3)}
{\|\widehat d_1\times\widehat d_2\|^2}.
\]

Immediately,

\[
\boxed{|\widehat v-v|\le\eta_1.}
\]

On any class with

\[
\|a\|\ge v_0>0
\]

and bounded second derivative, curvature is locally Lipschitz in `(a,b)`:

\[
|\widehat\kappa-\kappa|
\le
C_\kappa(v_0,M_2)(\eta_1+\eta_2)
\]

for sufficiently small derivative errors.

For torsion an additional lower bound is essential:

\[
\boxed{\|a\times b\|\ge w_0>0.}
\]

Then, with bounded derivatives,

\[
|\widehat\tau-\tau|
\le
C_\tau(v_0,w_0,M_2,M_3)
(\eta_1+\eta_2+\eta_3).
\]

The crucial point is not the exact constant but its conditioning:

\[
\boxed{
C_\tau\to\infty
\quad\text{as}\quad
w_0\downarrow0.
}
\]

Hence torsion recovery cannot be uniformly stable on a class that allows curvature to approach zero.

---

## 6. Exact low-curvature instability witness

For `ε>0`, `ω>0`, define

\[
\boxed{
\gamma_{\varepsilon,\omega}(s)
=
\bigl(s,\varepsilon\cos(\omega s),\varepsilon\sin(\omega s)\bigr).
}
\]

Direct calculation gives

\[
\|\gamma'\|^2
=1+\varepsilon^2\omega^2,
\]

\[
\boxed{
\kappa_{\varepsilon,\omega}
=
\frac{\varepsilon\omega^2}
{1+\varepsilon^2\omega^2},
}
\]

and

\[
\boxed{
\tau_{\varepsilon,\omega}
=
\frac{\omega}
{1+\varepsilon^2\omega^2}.
}
\]

For fixed `ω`,

\[
\gamma_{\varepsilon,\omega}
\to
\ell(s)=(s,0,0)
\]

in `C^3` on compact intervals as `ε→0`, while

\[
\kappa_{\varepsilon,\omega}\to0
\]

but

\[
\tau_{\varepsilon,\omega}\to\omega.
\]

Take two distinct frequencies `ω_1≠ω_2`. Then both curve families converge to the same straight line in `C^3`, but

\[
\left|
\tau_{\varepsilon,\omega_1}
-
\tau_{\varepsilon,\omega_2}
\right|
\to
|\omega_1-\omega_2|>0.
\]

Therefore:

\[
\boxed{
\text{torsion has no continuous extension through the straight-line / zero-curvature stratum.}
}
\]

This is a deterministic impossibility witness. No estimator can be uniformly stable for Frenet torsion over a class containing this boundary while still agreeing with classical torsion away from it.

---

## 7. Frenet/Bishop switching must be uncertainty-driven

The switch must not use a universal arbitrary threshold such as `κ<0.01`.

Let

\[
\widehat w
=
\|\widehat d_1\times\widehat d_2\|.
\]

If

\[
\|\widehat d_1-a\|\le\eta_1,
\qquad
\|\widehat d_2-b\|\le\eta_2,
\]

a conservative cross-product uncertainty radius is

\[
r_w
=
\eta_1\|\widehat d_2\|
+
\|\widehat d_1\|\eta_2
+
3\eta_1\eta_2.
\]

Define

\[
L_w=\max(0,\widehat w-r_w).
\]

### Certified Frenet sector

Use Frenet/torsion only when the lower bound is strong enough to meet the declared torsion-error tolerance:

\[
\boxed{
L_w>0
\quad\text{and}\quad
C_\tau(L_w)\,(\eta_1+\eta_2+\eta_3)
\le\varepsilon_\tau^{\rm task}.
}
\]

### Unresolved / Bishop sector

If this certification fails, the legal output is

\[
\boxed{\mathrm{FRENET\ UNRESOLVED}\to\mathrm{BISHOP}.}
\]

This does **not** assert that the true curvature is exactly zero. It asserts only that the protocol cannot stably license Frenet torsion at the requested precision.

The Bishop switch removes the division by `κ` inherent in the Frenet normal/torsion representation. It does not magically remove derivative-estimation error.

---

## 8. Statistical regularization layer

Raw finite differences are diagnostic, not the recommended estimator.

For contract G use local polynomial regression separately on the three coordinates of the curve. A local polynomial estimator of a derivative is linear in the observations:

\[
\widehat\gamma^{(r)}(t)
=
\sum_i w_{ir}(t;b)Y_i,
\]

where `b` is the smoothing bandwidth.

Under Gaussian isotropic noise,

\[
\boxed{
\operatorname{Cov}
(\widehat\gamma^{(r)}(t)\mid\{t_i\})
=
\sigma^2
\left(\sum_iw_{ir}^2\right)I_3.
}
\]

Bias remains and must be controlled by polynomial order, bandwidth choice, undersmoothing or explicit bias correction.

Classical local-polynomial theory supplies bias/variance expansions and asymptotic normality for derivative estimators under standard smoothness/design assumptions. `FS-STAT-01` imports that machinery; it does not claim it as new PSI mathematics.

For one common fit estimating through the third derivative, a local polynomial of sufficiently high degree (for example degree at least four under the present `C^5` smoothness target) provides a legal regularized derivative layer. The precise optimal order/bandwidth is part of the statistical protocol, not a CORE primitive.

---

## 9. Confidence statements

A confidence interval is legal only under an explicit probability model.

### Derivatives

Under contract G, joint covariance of the linear derivative estimates is available from the smoothing weights. Bias-corrected or undersmoothed Gaussian intervals may then be constructed for derivative components.

### Speed and curvature

On a certified regular set

\[
v\ge v_0>0,
\]

the delta method may be applied to `v` and `κ` after bias control.

### Torsion

For torsion require the stronger gate

\[
w\ge w_0>0.
\]

Only there is the torsion functional locally smooth enough for ordinary delta-method inference.

Near the low-curvature boundary, a nominal torsion confidence interval is not to be reported. The correct status is

\[
\boxed{\mathrm{UNRESOLVED/BISHOP}.}
\]

---

## 10. Flatness test `H0: τ=0`

The historical FS-STAT program requested a flatness test.

A pointwise test

\[
H_{0,t}:\tau(t)=0
\]

is legal only in the certified Frenet sector after bias control and variance estimation.

For example, under a valid asymptotic Gaussian approximation one may use

\[
Z(t)=\frac{\widehat\tau(t)}{\widehat{\operatorname{se}}(\widehat\tau(t))}.
\]

However:

1. this is only a **pointwise** test;
2. testing planarity over an interval requires simultaneous inference / a global statistic;
3. failure of the Frenet gate is not evidence for `τ=0`;
4. at `κ≈0`, torsion is the wrong coordinate for a stable flatness decision.

Therefore

\[
\boxed{
H_0:\tau\equiv0\text{ on an interval}
}
\]

remains an **OPEN statistical subproblem** unless a simultaneous-band/global test is explicitly supplied.

A Bishop-frame formulation of planarity is a natural future alternative because it need not divide by curvature.

---

## 11. Quotient-level uncertainty

The historical PSI-STAT idea of uncertainty on structural equivalence classes remains legitimate but is not automatically solved by coordinatewise intervals.

For the Bishop normal datum define a task metric such as

\[
d_G((v,k),(\tilde v,\tilde k))
=
\inf_{R\in SO(2)}
\left(
\|v-\tilde v\|^2
+
\|k-R\tilde k\|^2
\right)^{1/2}.
\]

A candidate structural confidence set could then be

\[
\mathcal C_{1-\alpha}(Y)
\subset
\{(v,[k]_{SO(2)})\}.
\]

But valid coverage

\[
\mathbb P
\bigl(
N_{FB}(\gamma)\in\mathcal C_{1-\alpha}(Y)
\bigr)
\ge1-\alpha
\]

requires a separate bootstrap/asymptotic proof, especially near singular orbit strata.

Thus quotient-level coverage is retained as

\[
\boxed{\mathrm{OPEN/BRIDGE},}
\]

not claimed as completed by FS-STAT-01.

---

## 12. Main hardening verdict

The exact MINI result survives finite sampling only after adding a statistical/conditioning contract.

The key distinctions are:

\[
\boxed{
\text{exact identifiability}
\neq
\text{stable identifiability}
\neq
\text{statistical confidence}.
}
\]

More specifically:

1. `v` is a first-derivative quantity and is comparatively well conditioned under the regularity gate;
2. `κ` requires second-derivative recovery and a speed lower bound;
3. `τ` requires third derivatives and division by `||γ'×γ''||^2`;
4. torsion is not uniformly stable as curvature approaches zero;
5. the Frenet/Bishop switch is therefore an inference gate, not merely an implementation convenience;
6. confidence statements require an explicit probabilistic noise model;
7. Bishop representation removes the Frenet singular coordinate but not all finite-sample uncertainty.

---

## 13. What passed

### PASS-FS1 — derivative conditioning is explicit

The finite-difference layer gives exact bias/noise amplification bounds and derivative-order scaling.

### PASS-FS2 — low-curvature impossibility witness

The family `γ_{ε,ω}` proves non-uniform torsion stability at the zero-curvature boundary.

### PASS-FS3 — switch policy is typed

Frenet usage is conditioned on a certified lower bound / task error budget rather than a universal curvature threshold.

### PASS-FS4 — statistical confidence is model-relative

No confidence interval is asserted under bounded deterministic noise alone.

### PASS-FS5 — exact MINI status is preserved

FS-STAT does not weaken the exact theorem. It specifies the extra hypotheses needed to transport it into a noisy finite-sample setting.

---

## 14. What remains open

1. rigorous simultaneous/global planarity test;
2. optimal bandwidth/order selection for the complete `(v,κ,τ)` pipeline;
3. finite-sample nonasymptotic confidence bounds for nonlinear invariants;
4. quotient-level confidence-set coverage modulo `SO(2)`;
5. statistically optimal Bishop-frame estimator through repeated curvature zeros;
6. minimax rates for the task-relative normal class;
7. irregular/nonuniform sampling and correlated/heteroscedastic noise.

---

## 15. Classical provenance

The geometric ingredients are classical Frenet/Bishop geometry.

Local polynomial regression and derivative estimation are also classical statistical machinery. Relevant classical references include:

- R. L. Bishop, *There Is More than One Way to Frame a Curve* (1975), DOI `10.1080/00029890.1975.11993807`;
- D. Ruppert and M. P. Wand, *Multivariate Locally Weighted Least Squares Regression*, Annals of Statistics 22 (1994), DOI `10.1214/aos/1176325632`;
- J. Fan and I. Gijbels, *Data-Driven Bandwidth Selection in Local Polynomial Fitting*, JRSS B 57 (1995), DOI `10.1111/j.2517-6161.1995.tb02034.x`.

The PSI contribution in this run is architectural: placing conditioning, representation choice, gauge, exact identifiability and statistical licensing in one explicit contract and regression sequence.

---

## 16. Freeze verdict

Freeze:

\[
\boxed{
\text{MINI exact uniqueness does not imply finite-sample stability.}
}
\]

Freeze:

\[
\boxed{
\kappa\downarrow0
\Rightarrow
\text{Frenet torsion becomes non-uniformly unstable};
\quad
\text{switch to Bishop/UNRESOLVED unless certified otherwise}.
}
\]

Freeze the three-level distinction:

\[
\boxed{
\mathrm{ID}_{\rm exact}
\mid
\mathrm{ID}_{\rm stable}
\mid
\mathrm{CONF}_{1-\alpha}.
}
\]

No CORE change and no Agent architecture change are justified.

`FS-STAT-01` completes the first post-R4 hardening triad together with HCube and Go.
