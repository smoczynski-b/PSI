# PSI — CAT–FACT–NORM–MINI 01

**Status:** `BRIDGE / EXACT-NOISELESS MINI / AUDITED WITH CONTRACT ERRATA`  
**Scope:** `C^3` regular curves on the compact interval `[0,T]`; exact observation; time parameter preserved.  
**Audit:** `PROOF-SOURCE-MIGRATION-AUDIT-01`  
**Does not claim:** statistical stability, noisy-data recovery, closed-curve periodic normalization, general PSI-FACT equivalence, or a new theorem of differential geometry.

This document records the first full PSI dual-operator run and its later proof/source audit.

The result is intentionally small. Its role is to test whether PSI can distinguish catalogue change, representation repair, factorization gauge and normal form without promoting classical Frenet/Bishop geometry into a new core primitive.

---

## 1. Contract snapshot — corrected observation/gauge typing

Let

\[
\gamma:[0,T]\to\mathbb R^3
\]

be `C^3` and regular:

\[
v(t)=\|\dot\gamma(t)\|>0\qquad\forall t\in[0,T].
\]

Time reparameterization is **not** part of either MINI gauge.

Define arc length

\[
s(t)=\int_0^t v(u)\,du,
\qquad L=s(T).
\]

The internal Bishop-frame presentation gauge acts on an oriented normal pair by one constant rotation:

\[
G_{\rm normal}=SO(2).
\]

This gauge leaves the embedded curve unchanged and therefore preserves both exact protocols below.

The earlier MINI text mixed fixed-coordinate observation with an external `SE(3)` quotient. That is not automatically legal: a nontrivial Euclidean motion generally changes the observed coordinate curve. The corrected theorem therefore has two separately typed variants.

### 1.1. Absolute-coordinate protocol

\[
\boxed{P_0^{\rm abs}:\quad Y_{\rm abs}=\gamma(t),\quad t\in[0,T].}
\]

The observation is the full time-parametrized curve in the declared Euclidean coordinate system.

For this protocol, a nontrivial

\[
g\in SE(3)
\]

generally satisfies

\[
g\gamma(t)\neq\gamma(t),
\]

so external `SE(3)` is **not** a gauge acting inside the compatible fibre over the same `Y_abs`.

The relevant presentation gauge for the Frenet/Bishop factorization is only

\[
SO(2)_{\rm normal}.
\]

### 1.2. Shape protocol

\[
\boxed{P_0^{\rm shape}:\quad Y_{\rm shape}=[\gamma]_{SE(3)}}
\]

or, equivalently, an explicitly `SE(3)`-invariant observation carrying the same exact shape information and time parameter.

Under this protocol the observation descends through external Euclidean gauge, so the legal realization gauge is

\[
\boxed{G_{\rm shape}=SE(3)\times SO(2)_{\rm normal}.}
\]

This is the variant in which Euclidean realization classes are quotiented inside the compatible factorization fibre.

### 1.3. Standing distinction

`SE(3)` acts on the embedded realization. `SO(2)_{normal}` acts on the choice of oriented basis in the normal plane. They are different actions and must not be compressed into one untyped notion of gauge.

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

## 3. Finite grammar and quotient domain

Let

\[
\mathcal L_{FB}=\{F,B\}.
\]

A grammar term is a finite ordered concatenation

\[
X=X_1\oplus\cdots\oplus X_n
\]

of legal Frenet or Bishop atoms on consecutive subintervals covering `[0,L]` and reconstructing one regular curve with matching position and tangent at shared boundaries.

The rewrite theorem is formulated on **normal-frame gauge classes** of such grammar terms. Equivalently, one may first prove equivariance of the raw rewrite under constant normal `SO(2)` and then pass to the quotient.

Gauge is an isomorphism/presentation relation; it is not a catalogue-changing rewrite.

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
- every legal `R_M` leaves `n_F` unchanged and strictly decreases `n_seg`.

Thus **every** rewrite step strictly decreases `mu`; it is not necessary to postpone the termination argument for `R_M` until all Frenet atoms have disappeared.

Therefore there is no infinite rewrite chain.

---

## 7. Local confluence and confluence modulo gauge

Work with the induced rewrite on constant-normal-`SO(2)` gauge classes.

The relevant overlap analysis is:

1. **disjoint Frenet recodes** — disjoint unary steps commute modulo their local presentation choices;
2. **triple Bishop merge** — for
   \[
   B_1\oplus B_2\oplus B_3,
   \]
   the two adjacent merge orders produce the same globally transported Bishop-frame class after gauge alignment;
3. **Frenet recode versus Bishop merge** — the unary `F→B` redex and the binary `B⊕B→B` redex do not overlap at the same initial location; disjoint redexes commute.

Hence the quotient rewrite is locally confluent.

Together with termination, Newman's lemma yields confluence of the induced rewrite system on gauge classes.

The conclusion is a unique **normal class**, not a canonical frame representative.

---

## 8. Normal datum

For either corrected exact interval protocol define

\[
\boxed{
N_{FB}(\gamma)=\bigl(v(t),[k_1(s),k_2(s)]_{SO(2)}\bigr).
}
\]

These scalar data determine the curve after supplying one initial Euclidean position/frame; changing that initial Euclidean frame changes the embedded representative by an element of `SE(3)`.

Thus:

- under `P_0^{abs}`, the actual observed coordinates fix the Euclidean placement;
- under `P_0^{shape}`, only the Euclidean realization class is observed/identified.

In either variant every legal finite Frenet/Bishop segmentation reduces to the same Bishop normal datum modulo one constant normal-plane rotation.

---

## 9. Factorization fibres — restricted MINI objects

The objects below are **grammar-specific set-level MINI models**. They are not definitions of the general PSI-FACT groupoid/homotopy fibre and do not erase stabilizers or compatibility witnesses in other contracts.

### 9.1. Absolute-coordinate factorization fibre

Let

\[
\operatorname{RawFact}^{0,\rm abs}_{FB,P_0}(Y_{\rm abs})
\]

be the raw set of legal finite `{F,B}` segmentations/realizations reconstructing the exactly observed coordinate trajectory.

Define

\[
\boxed{
\operatorname{Fact}^{0,\rm abs}_{FB,P_0}(Y_{\rm abs})
:=
\operatorname{RawFact}^{0,\rm abs}_{FB,P_0}(Y_{\rm abs})
/SO(2)_{\rm normal}.
}
\]

Then

\[
\boxed{
\left|\operatorname{Fact}^{0,\rm abs}_{FB,P_0}(Y_{\rm abs})\right|=1.
}
\]

No external Euclidean quotient is taken inside this fixed-coordinate compatible fibre.

### 9.2. Shape factorization fibre

Let

\[
\operatorname{RawFact}^{0,\rm shape}_{FB,P_0}(Y_{\rm shape})
\]

be the corresponding raw family for the exact shape observation modulo Euclidean realization.

Define

\[
\boxed{
\operatorname{Fact}^{0,\rm shape}_{FB,P_0}(Y_{\rm shape})
:=
\operatorname{RawFact}^{0,\rm shape}_{FB,P_0}(Y_{\rm shape})
/\bigl(SE(3)\times SO(2)_{\rm normal}\bigr).
}
\]

Then

\[
\boxed{
\left|\operatorname{Fact}^{0,\rm shape}_{FB,P_0}(Y_{\rm shape})\right|=1.
}
\]

### 9.3. Reconstruction logic

Exact observation determines the speed, arc length and tangent in the corresponding observation class. A Bishop frame is determined by one initial oriented normal pair, and any two such choices differ by one constant `SO(2)` rotation. Conversely, the Bishop normal datum plus the appropriately typed Euclidean initial data reconstructs the realization.

The PSI content is the explicit separation

\[
\text{catalogue}
\mid
\text{raw grammar realization}
\mid
\text{observation-compatible gauge}
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

The Frenet representation ceases to be legal at the singular point, whereas a Bishop representation remains legal for the same regular curve/shape observation. No new external behavioural sector is introduced; the compatible object admits a legal representation repair.

Therefore, under either corrected MINI contract,

\[
\boxed{
F\to B\text{ at a Frenet singularity is recode/domain repair, not catalogue birth.}
}
\]

This is contract-relative and is not a universal statement about representation failures.

---

## 11. Falsification boundary

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

`SE(3)` distinguishes mirror images. If the intended shape gauge is `E(3)` or `O(3)`, the contract must state this separately.

### X6 — gauge/observation mismatch

A transformation cannot be quotiented inside a fixed observation fibre merely because it is geometrically natural. The observation/compatibility contract must be invariant/equivariant so that the action descends.

---

## 12. What MINI-01 establishes after errata

Under either of the two corrected exact contracts:

1. the grammar `{F,B}` is finite;
2. the induced rewrite on normal-frame gauge classes terminates;
3. it is locally confluent and therefore confluent;
4. every legal finite Frenet/Bishop segmentation reduces to one Bishop normal class;
5. the corresponding restricted MINI factorization set has one class after the **observation-compatible** declared gauge;
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
- equivalence of the restricted set-level MINI object with the full PSI-FACT groupoid/homotopy fibre in arbitrary contracts;
- a new Frenet/Bishop theorem;
- universal sufficiency of CORE5.

---

## 14. Audit record

### Initial exploration

Strong proposal: every admissible Frenet/Bishop realization of a regular trajectory normalizes to one canonical decomposition.

### First semantic audit

Downgrade `canonical decomposition` to a normal equivalence class; separate external Euclidean geometry from internal normal-frame presentation; distinguish raw realizations from their quotient.

### Proof/source audit 01

The later audit found an additional typing defect: fixed-coordinate exact observation and external `SE(3)` quotient had been combined without showing that `SE(3)` preserves the same observation fibre.

Correction:

\[
P_0^{abs}\quad\text{or}\quad P_0^{shape},
\]

with different legal quotient groups as specified above.

It also strengthened the confluence proof by placing the rewrite explicitly on gauge classes and corrected the termination wording.

---

## 15. Freeze statement after errata

### Absolute-coordinate form

For an exactly observed, time-parametrized `C^3` regular coordinate curve on a compact interval, every finite legal Frenet/Bishop segmentation reduces to one Bishop normal class modulo constant normal-plane rotation, and

\[
\left|\operatorname{Fact}^{0,\rm abs}_{FB,P_0}(Y_{\rm abs})\right|=1.
\]

### Shape form

For an exactly observed, time-parametrized regular curve **modulo `SE(3)`**, every finite legal Frenet/Bishop segmentation reduces to one Bishop normal class, and

\[
\left|\operatorname{Fact}^{0,\rm shape}_{FB,P_0}(Y_{\rm shape})\right|=1.
\]

In either contract, vanishing curvature that only invalidates the Frenet frame is a recode/domain event rather than evidence for catalogue birth.

**Freeze level:** `BRIDGE / MINI`, not CORE theorem.

---

## 16. Subsequent attacks already completed

- `CLOSED-FRAME-01` — global return holonomy / periodicity;
- `FS-STAT-01` — finite sampling, noise and low-curvature conditioning;
- `PROOF-SOURCE-MIGRATION-AUDIT-01` — observation/gauge typing, proof placement and source migration.

General CAT/FACT migration remains a separate freeze gate.