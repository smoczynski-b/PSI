# PSI — REGRESSION-BANK-01

**Status:** ACTIVE / HARDENING BANK  
**Date:** 2026-09-28  
**Inputs:** `HCUBE-REGRESSION-01`, `GO-MEMORY-REGRESSION-01`, `FS-STAT-01`

## 0. Purpose

This bank collects permanent counterexamples and boundary tests that every later redaction, model handoff and theorem extension should survive.

It is not a new module of PSI.

The common form is:

\[
\boxed{
\text{representation / inference claim}
\to
\text{fixed witness}
\to
\text{oracle}
\to
\text{scope-limited verdict}.
}
\]

---

## R01 — operator representation inadequacy / HCube

### Target

Any claim that

\[
\rho_0(X)=(\chi_X,\|X\|_2)
\]

is sufficient for resolvent-sensitive tasks.

### Fixed witness

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=\begin{pmatrix}2&0&0\\0&1&1\\0&0&0\end{pmatrix}.
\]

They satisfy

\[
\chi_A=\chi_B,
\qquad
\|A\|_2=\|B\|_2=2,
\]

but

\[
\left\|\left(\tfrac12I-A\right)^{-1}\right\|_2=2,
\]

\[
\left\|\left(\tfrac12I-B\right)^{-1}\right\|_2=2(1+\sqrt2).
\]

### Oracle

\[
R_{1/2}(X)=\left\|\left(\tfrac12I-X\right)^{-1}\right\|_2.
\]

### Verdict

\[
\boxed{\ker\rho_0\not\subseteq\ker R_{1/2}.}
\]

### Permanent boundary

HCube may be used as a separator/diagnostic but must not be promoted to a necessary or universal representation merely because it separates this pair.

---

## R02 — task-relative memory inadequacy / Go

### Target

Any claim that one fixed compressed present is sufficient across rule systems.

### Frozen ladder

\[
\rho_0=(B_t,\sigma_t)
\]

suffices under no-ko, but fails under simple ko.

\[
\rho_K=(B_t,\sigma_t,B_{t-1})
\]

repairs the frozen simple-ko witness, but fails under positional superko.

\[
\rho_{PSK}=(B_t,\sigma_t,V_t)
\]

repairs positional superko, but fails under situational superko.

\[
\rho_{SSK}=(B_t,\sigma_t,U_t)
\]

is sufficient under the frozen situational-superko contract.

### Oracle

Future move legality under the declared rule/task contract.

### Verdict

\[
\boxed{
\mathrm{ADEQ}_{mem}(\rho,\mathcal T)=1
\iff
\ker\rho_t\subseteq\equiv_{\mathcal T,t}.
}
\]

### Permanent boundaries

- task quotient minimality is quotient-order minimality, not bit/compute minimality;
- mathematical recursive update does not imply finite/efficient memory;
- currently recovered sources do not supply separate G1 content.

---

## R03 — exact versus stable differential identification / FS-STAT

### Target

Any inference

\[
\mathrm{ID}_{exact}
\Rightarrow
\mathrm{ID}_{stable}
\Rightarrow
\mathrm{CONF}_{1-\alpha}.
\]

### Fixed conditioning layer

For bounded sample noise `||ε_j||≤δ`, the centered derivative stencils satisfy

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

### Fixed low-curvature witness

\[
\gamma_{\varepsilon,\omega}(s)
=
(s,\varepsilon\cos\omega s,\varepsilon\sin\omega s)
\]

has

\[
\kappa_{\varepsilon,\omega}
=
\frac{\varepsilon\omega^2}{1+\varepsilon^2\omega^2},
\]

\[
\tau_{\varepsilon,\omega}
=
\frac{\omega}{1+\varepsilon^2\omega^2}.
\]

As `ε→0`, the curves converge in `C^3` to a line while torsion tends to the arbitrary fixed frequency `ω`.

### Oracle

Continuity/stability of the declared differential invariant plus explicit sampling/noise contract.

### Verdict

\[
\boxed{
\kappa\downarrow0
\Rightarrow
\text{no uniform stable Frenet torsion recovery}.
}
\]

The legal response is an uncertainty-driven Frenet/Bishop gate, not an arbitrary universal curvature threshold.

### Permanent boundaries

- bounded noise does not license confidence levels;
- raw dense differencing at fixed noise is unstable;
- pointwise torsion tests do not imply global planarity;
- Bishop removes the Frenet singular coordinate but not all estimation noise;
- quotient-level confidence coverage remains open.

---

## 1. Cross-bank invariant

The three regressions instantiate the same abstract PSI pattern in different domains:

\[
\boxed{
\text{a representation is legal only if it preserves every distinction required by the task}.}
\]

HCube:

\[
\text{spectrum+norm}
\not\Rightarrow
\text{resolvent adequacy}.
\]

Go:

\[
\text{compressed present}
\not\Rightarrow
\text{future legality adequacy}.
\]

FS-STAT:

\[
\text{exact coordinate}
\not\Rightarrow
\text{stable/statistically licensed coordinate}.
\]

---

## 2. Mandatory use

Before promoting a theorem, representation or agent compression touching the corresponding domain, rerun the relevant bank entry.

A later result fails regression if it silently reintroduces any of:

1. spectral-summary sufficiency for nonnormal/resolvent tasks;
2. task-independent memory sufficiency;
3. quotient-order minimality as bit/compute minimality;
4. exact-identifiability-to-stability inflation;
5. confidence without a probability contract;
6. low-curvature torsion as a uniformly stable coordinate.

---

## 3. Relation to CORE5

The bank does not add a sixth primitive.

All three cases are absorbed by the existing adequacy logic:

\[
\boxed{
\ker_{eq}\rho\subseteq E_{\mathcal T}
}
\]

or, for histories,

\[
\boxed{
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
}
\]

FS-STAT adds a distinct **stability/statistical licensing layer** around an exact representation claim; this is a condition on inference quality, not a new semantic role in CORE5.

---

## 4. Regression-bank status

\[
\boxed{
\mathrm{REGRESSION\ BANK\ 01}
=
\{R01\text{ HCube},R02\text{ Go},R03\text{ FS-STAT}\}.
}
\]

The first post-R4 hardening cycle is complete.

Next priority:

\[
\boxed{
\text{Principia V1/V2 migration and theorem freezing from claim-registry v10}.
}
\]
