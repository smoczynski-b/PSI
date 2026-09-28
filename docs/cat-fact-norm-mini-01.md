# PSI — CAT–FACT–NORM–MINI 01

**Status:** `BRIDGE / EXACT-NOISELESS MINI / FIRST DUAL-OPERATOR RUN`  
**Scope:** `C^3` regular curves on the compact interval `[0,T]`; exact observation; time parameter preserved.  
**Does not claim:** statistical stability, noisy-data recovery, closed-curve periodic normalization, or a new theorem of differential geometry.

This document records the first full PSI dual-operator run

\[
\mathsf E\to\mathsf A\to\mathsf E_{\rm fals}\to\mathsf A_{\rm freeze}.
\]

The result is intentionally small. Its role is to test whether PSI can distinguish catalogue change, representation repair, factorization gauge and normal form without promoting classical Frenet/Bishop geometry into a new core primitive.

---

## 1. Contract snapshot

Let

\[
\gamma:[0,T]\to\mathbb R^3
\]

be `C^3` and regular:

\[
v(t)=\|\dot\gamma(t)\|>0\qquad\forall t\in[0,T].
\]

The exact protocol `P_0` observes the full time-parametrized trajectory

\[
Y=\gamma(t),\qquad t\in[0,T].
\]

Time reparameterization is **not** part of the gauge in MINI-01.

The external geometric gauge acts on the curve:

\[
G_{\rm ext}=SE(3),
\qquad
\gamma\sim g\gamma.
\]

Define arc length

\[
s(t)=\int_0^t v(u)\,du,
\qquad L=s(T).
\]

The internal frame gauge acts on an oriented Bishop normal pair by one constant rotation

\[
G_{\rm normal}=SO(2).
\]

These two actions must not be confused: `SE(3)` acts on the embedded curve/frame, while `SO(2)` acts on the choice of oriented basis in the normal plane.

---

## 2. Classical local encodings

### Frenet atom

On an interval `I` where

\[
\kappa(s)>0,
\]

a legal Frenet atom is represented by

\[
F_I=(v,\kappa,\tau)_I.
\]

### Bishop atom

A Bishop / relatively-parallel atom is represented by

\[
B_I=(v,k_1,k_2)_I
\]

with frame `(T,N_1,N_2)` satisfying

\[
T'=k_1N_1+k_2N_2,
\]

\[
N_1'=-k_1T,
\qquad
N_2'=-k_2T.
\]

For a regular curve on an interval, specifying one oriented orthonormal normal pair at one point determines the Bishop frame. Changing this initial pair by a constant

\[
R_\alpha\in SO(2)
\]

rotates the curvature vector

\[
k=(k_1,k_2)
\]

by the same constant normal-plane gauge. Thus the invariant Bishop shape datum in this MINI is

\[
[k]_{SO(2)},
\]

not a preferred ordered pair `(k_1,k_2)`.

---

## 3. Finite grammar

Let

\[
\mathcal L_{FB}=\{F,B\}.
\]

A grammar term is a finite ordered concatenation

\[
X=X_1\oplus\cdots\oplus X_n
\]

of legal Frenet or Bishop atoms on consecutive subintervals covering `[0,L]` and reconstructing one regular curve with matching position and tangent at shared boundaries.

Gauge is an isomorphism relation on realizations; it is not a catalogue-changing rewrite.

---

## 4. Frenet-to-Bishop recode

On every Frenet-valid interval choose `theta` with

\[
\theta'=-\tau
\]

in a fixed convention and rotate the Frenet normal/binormal pair into a relatively-parallel normal pair. Then, in the same convention,

\[
k_1=\kappa\cos\theta,
\qquad
k_2=-\kappa\sin\theta.
\]

Changing the integration constant in `theta` changes only the constant `SO(2)` normal gauge.

Hence

\[
\boxed{R_F:F_I\longrightarrow B_I}
\]

is a recode between two legal representations of the same curve on that interval.

---

## 5. Bishop gluing

For adjacent Bishop atoms reconstructing the same curve,

\[
B_{I_1}\oplus B_{I_2},
\]

their oriented normal pairs at the common endpoint differ by one `SO(2)` rotation. Align the second segment by that constant gauge. Relative parallel transport then produces one Bishop frame on the union:

\[
\boxed{R_M:B_{I_1}\oplus B_{I_2}\longrightarrow B_{I_1\cup I_2}.}
\]

After gluing a connected interval, only one global constant `SO(2)` presentation gauge remains.

---

## 6. Termination

Define

\[
\mu(X)=\bigl(n_F(X),n_{\rm seg}(X)\bigr)\in\mathbb N^2
\]

with lexicographic order.

- `R_F` strictly decreases `n_F`;
- once no Frenet atoms remain, `R_M` strictly decreases `n_seg`.

Therefore there is no infinite rewrite chain.

---

## 7. Confluence modulo gauge

The rewrite rules respect the declared gauge, so they induce a rewrite relation on gauge classes.

The relevant critical configurations are:

1. independent Frenet recodes — they commute modulo local `SO(2)` choices;
2. triple Bishop merge — either merge order gives the same transported frame class after fixing the first segment presentation;
3. recode/merge — the redex types are distinct; after the required recodes only Bishop merges remain.

Thus the induced quotient rewrite is locally confluent. Together with termination, Newman's lemma gives confluence of the induced rewrite system on gauge classes.

The conclusion is a unique **normal class**, not a canonical frame representative.

---

## 8. Normal datum

For the exact interval contract define

\[
\boxed{
N_{FB}(\gamma)=\bigl(v(t),[k_1(s),k_2(s)]_{SO(2)}\bigr).
}
\]

`SE(3)` does not act on these scalar functions; it acts on the reconstructed embedded curve and initial Euclidean frame. The relation is:

\[
N_{FB}(\gamma)
+\text{one initial Euclidean frame}
\Longrightarrow
\gamma,
\]

and changing that initial Euclidean frame changes only the reconstructed representative in `[\gamma]_{SE(3)}`.

Therefore every legal finite Frenet/Bishop segmentation of one exact regular interval curve reduces to the same datum `N_FB(γ)` modulo the one constant normal-plane rotation.

---

## 9. Factorization fibre: raw versus quotiented

To avoid double quotienting, distinguish the raw realization set

\[
\operatorname{RawFact}^{0}_{FB,P_0}(Y)
\]

from the factorization fibre after the declared realization gauge:

\[
\boxed{
\operatorname{Fact}^{0}_{FB,P_0}(Y)
:=
\operatorname{RawFact}^{0}_{FB,P_0}(Y)
/\bigl(SE(3)\times SO(2)_{\rm normal}\bigr).
}
\]

Here `SE(3)` refers to the external Euclidean realization and `SO(2)` to the Bishop normal presentation. With this convention **no further quotient is applied to `Fact`**.

Exact observation determines

\[
v(t)=\|\dot\gamma(t)\|,
\]

then arc length and the tangent. A Bishop frame is determined by one initial oriented normal pair, and any two such choices differ by one constant `SO(2)` rotation. Conversely, `v`, the Bishop curvature vector modulo that rotation, and one initial Euclidean frame reconstruct the trajectory.

Hence

\[
\boxed{
\left|\operatorname{Fact}^{0}_{FB,P_0}(Y)\right|=1.
}
\]

This is the MINI factorization-identifiability result.

Its geometric ingredients are classical. The PSI content is the explicit separation

\[
\text{catalogue}
\mid
\text{raw realization}
\mid
\text{gauge}
\mid
\text{recode}
\mid
\text{normal class}
\mid
\text{protocol}.
\]

---

## 10. CAT verdict: Frenet failure is not birth

Suppose

\[
\kappa(s_0)=0
\]

while the curve remains regular.

The Frenet representation ceases to be legal at the singular point, whereas a Bishop representation remains legal for the regular curve. No new external behavioural sector is introduced; the same observed curve admits a legal representation repair.

Therefore, under MINI-01,

\[
\boxed{
F\to B\text{ at a Frenet singularity is recode/domain repair, not catalogue birth.}
}
\]

This is contract-relative and is not a universal statement about representation failures.

---

## 11. Falsification boundary

The stronger exploratory proposal fails outside the frozen contract.

### X1 — loss of regularity

If

\[
\dot\gamma(t_0)=0,
\]

the present tangent/arc-length construction is outside scope.

### X2 — reparameterization admitted as gauge

If arbitrary orientation-preserving reparameterizations are admitted, `v(t)` is not invariant. Timing must then be quotiented or removed from the factorization target.

### X3 — closed curves

For a closed parameter domain, normal-plane parallel transport may return the normal pair rotated. A periodic representative therefore requires explicit treatment of return rotation / holonomy rather than silent extension of the interval result.

### X4 — sampled/noisy data

Exact identifiability does not imply stable derivative, curvature or frame recovery from finite noisy samples, especially in low-curvature regions.

### X5 — reflections

`SE(3)` distinguishes mirror images. If the intended gauge is `E(3)` or `O(3)`, the contract must state this separately.

---

## 12. What MINI-01 establishes

Under the frozen exact contract:

1. the grammar `{F,B}` is finite;
2. the induced rewrite on gauge classes terminates;
3. it is locally confluent and therefore confluent;
4. every legal finite Frenet/Bishop segmentation reduces to one Bishop normal class;
5. the raw compatible realization family has one class after the declared realization gauge;
6. a zero-curvature Frenet failure of an otherwise regular curve is a representation/domain event, not evidence for catalogue birth.

---

## 13. What MINI-01 does not establish

It does not establish:

- noisy-data consistency;
- robustness under finite sampling;
- a canonical global frame representative;
- periodic normalization for closed curves;
- uniqueness modulo arbitrary time reparameterization;
- general confluence of PSI-CAT;
- general identifiability of arbitrary system factorizations;
- a new Frenet/Bishop theorem;
- universal sufficiency of CORE5.

---

## 14. Dual-operator audit record

### `E`

Strong proposal: every admissible Frenet/Bishop realization of a regular trajectory normalizes to one canonical decomposition.

### `A0` — semantic/source audit

Downgrade `canonical decomposition` to a normal equivalence class; separate external Euclidean gauge from internal normal-frame gauge; distinguish raw factorization realizations from their quotient.

### `A1` — mathematical audit

Freeze the domain `C^3`, regular interval curve, fixed time parameter and exact observation. Establish termination and confluence only for the finite `{F,B}` rewrite under these hypotheses.

### `E_fals`

Regularity failure, reparameterization, closed-loop return rotation, reflections and noisy derivative recovery defeat the unrestricted proposal.

### freeze

\[
\boxed{
\begin{minipage}{0.88\linewidth}
For an exactly observed, time-parametrized `C^3` regular curve on a compact interval, every finite legal Frenet/Bishop segmentation reduces to one Bishop normal class modulo constant normal-plane rotation; the corresponding raw realization family has one factorization class after the declared Euclidean and normal-frame gauge. In this contract, vanishing curvature that only invalidates the Frenet frame is a recode/domain event, not evidence for catalogue birth.
\end{minipage}
}
\]

**Freeze level:** `BRIDGE / MINI`, not CORE theorem.

---

## 15. Next legal attacks

1. `CLOSED-FRAME-01` — closed-loop return rotation / holonomy and its correct role in FRAME/CORE5;
2. `FS-STAT-01` — finite sampling, noise and low-curvature conditioning.

Only after those attacks may CAT–FACT–NORM be generalized beyond MINI-01.