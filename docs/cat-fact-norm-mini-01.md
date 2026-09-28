# PSI — CAT–FACT–NORM–MINI 01

**Status:** `BRIDGE / EXACT-NOISELESS MINI-THEOREM / FIRST DUAL-OPERATOR RUN`  
**Scope:** regular open-interval curves in `R^3`; exact observation; time parameter preserved.  
**Does not claim:** statistical stability, noisy-data recovery, closed-curve periodic normalization, or a new theorem of differential geometry.

This document is the first full run of the PSI dual-operator cycle

\[
\mathsf E\to\mathsf A\to\mathsf E_{\rm fals}\to\mathsf A_{\rm freeze}.
\]

The purpose is to turn the earlier proposal `CAT–FACT–NORM–MINI on Frenet/Bishop trajectories` into one typed, falsifiable, minimal construction.

---

## 1. Source motivation

Earlier PSI work proposed the following closure programme:

- finite catalogue grammar;
- explicit `SE(3)` gauge;
- reduction rules;
- termination;
- local confluence modulo gauge;
- a normal front;
- later adequacy/stability testing on data.

The same source explicitly proposed Frenet/Bishop trajectories as the preferred small laboratory. The present MINI executes only the **exact mathematical layer**. Statistical adequacy under sampling/noise remains outside this theorem.

---

## 2. Domain and protocol

Let

\[
\gamma:[0,T]\to\mathbb R^3
\]

be a `C^3` regular curve with

\[
v(t)=\|\dot\gamma(t)\|>0
\qquad\forall t\in[0,T].
\]

The protocol `P_0` observes the full trajectory with its time parameter:

\[
Y=\gamma(t),\qquad t\in[0,T].
\]

The observational gauge is the orientation-preserving Euclidean group

\[
G_{\rm ext}=SE(3).
\]

Thus the external object is the class

\[
[\gamma]_{SE(3)}.
\]

Time reparameterization is **not** part of the gauge in MINI-01. If it is admitted, the timing factor `v(t)` must be quotiented or reformulated separately.

Define arc length

\[
s(t)=\int_0^t v(u)\,du,
\qquad L=s(T),
\]

and write the curve by arc length when discussing frames.

---

## 3. Two classical local encodings

### 3.1 Frenet atom

On an interval `I` on which the curvature satisfies

\[
\kappa(s)>0,
\]

a Frenet atom is

\[
F_I=(v,\kappa,\tau)_I.
\]

The Frenet frame is defined only on the part of the curve where the required nondegeneracy holds.

### 3.2 Bishop atom

A Bishop / relatively-parallel atom is

\[
B_I=(v,k_1,k_2)_I,
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

For a regular curve on an interval such a frame exists after choosing an oriented orthonormal normal pair at one point.

Changing that initial normal pair by a constant rotation

\[
R_\alpha\in SO(2)
\]

rotates the curvature vector

\[
k=(k_1,k_2)
\]

by the same constant normal-plane gauge. Therefore the intrinsic Bishop datum for this MINI is

\[
[k]_{SO(2)},
\]

not a preferred pair `(k_1,k_2)`.

---

## 4. Finite grammar

A term in the grammar `L_FB` is a finite ordered concatenation

\[
X=X_1\oplus\cdots\oplus X_n,
\]

where every atom `X_j` is either a legal Frenet atom `F_{I_j}` or a legal Bishop atom `B_{I_j}` on consecutive subintervals covering `[0,L]`.

Admissible concatenation requires that adjacent atoms reconstruct the same position and tangent at the shared endpoint. Frame variables may differ by their declared gauge.

The grammar therefore has only two atom types:

\[
\boxed{\mathcal L_{FB}=\{F,B\}.}
\]

This is deliberately smaller than the general PSI-CAT calculus. `birth`, `death`, `split`, `merge`, and `recode` remain general catalogue operations; MINI-01 tests whether the apparent Frenet→Bishop change actually requires `birth`.

---

## 5. Gauge

The complete MINI gauge is

\[
\boxed{G=SE(3)\times SO(2)_{\rm normal}.}
\]

- `SE(3)` changes global position and orientation of the curve;
- `SO(2)_normal` changes the initial oriented Bishop normal pair.

For a segmented Bishop representation, each local segment may initially carry its own `SO(2)` presentation. Boundary matching removes the relative rotations; after gluing a connected interval, only one global constant `SO(2)` gauge remains.

Gauge is an isomorphism relation, **not** a catalogue-changing rewrite.

---

## 6. Recode `F -> B`

On every Frenet-valid interval there is a Bishop recoding.

Let `(T,N,B)` be the Frenet frame. Choose an angle `theta` satisfying the convention-dependent relation

\[
\theta'=-\tau
\]

for the rotation

\[
\begin{pmatrix}N_1\\N_2\end{pmatrix}
=
R_{\theta}
\begin{pmatrix}N\\B\end{pmatrix}.
\]

Then the corresponding Bishop curvature vector is obtained by the same rotation of the normal curvature vector. In one fixed convention,

\[
k_1=\kappa\cos\theta,
\qquad
k_2=-\kappa\sin\theta.
\]

Changing the integration constant in `theta` changes only the constant `SO(2)` normal gauge.

Hence the first rewrite is

\[
\boxed{R_F:\quad F_I\longrightarrow B_I.}
\]

It is a **recode**, not a birth of a new geometric behaviour.

---

## 7. Bishop gluing and merge

Let two adjacent Bishop atoms reconstruct the same regular curve and share the same tangent at their common endpoint:

\[
B_{I_1}\oplus B_{I_2}.
\]

Their oriented normal pairs at the shared point differ by one element of `SO(2)`. Rotate the second local frame by that constant gauge so that the frames agree at the boundary. Relative parallel transport then gives one Bishop frame on the union.

Thus the second rewrite is

\[
\boxed{R_M:\quad B_{I_1}\oplus B_{I_2}\longrightarrow B_{I_1\cup I_2}.}
\]

The alignment choice is unique modulo the remaining global constant `SO(2)` gauge.

---

## 8. Termination

For a grammar term `X`, define

\[
\mu(X)=\bigl(n_F(X),n_{\rm seg}(X)\bigr)\in\mathbb N^2
\]

with lexicographic order.

- `R_F` strictly decreases `n_F`;
- `R_M` leaves `n_F=0` on its redex and strictly decreases the number of segments.

No rule increases either component before a decrease in the earlier component.

Therefore there is no infinite rewrite chain:

\[
\boxed{\mathcal L_{FB}/G\text{ is terminating under }\{R_F,R_M\}.}
\]

---

## 9. Local confluence modulo gauge

The possible critical configurations are elementary.

### 9.1 Two independent Frenet recodes

Recoding disjoint Frenet atoms commutes. Different integration constants for `theta` differ only by local `SO(2)` gauge and are removed at gluing.

### 9.2 Triple Bishop merge

For

\[
B_1\oplus B_2\oplus B_3,
\]

merging `(B_1,B_2)` first or `(B_2,B_3)` first yields the same relatively-parallel frame on the full union once the first segment frame is fixed. Any two initial choices differ by one global `SO(2)` rotation.

Therefore the two reduction paths meet in the same quotient class.

### 9.3 Recode / merge interaction

`R_M` has only Bishop–Bishop redexes, whereas `R_F` has Frenet redexes. Hence there is no nontrivial same-redex overlap. After all necessary recodes, the merge rules reduce the resulting Bishop segmentation.

Thus the rewrite system is locally confluent **modulo `G`**.

Since it is also terminating, Newman's lemma applied on the quotient gives confluence.

---

## 10. Normal form

Every legal finite Frenet/Bishop segmentation of the same regular curve on `[0,T]` reduces to one Bishop class

\[
\boxed{
\operatorname{NF}_{FB}(\gamma)
=
\bigl[v(t),k_1(s),k_2(s)\bigr]_{SE(3)\times SO(2)}.
}
\]

More precisely, the curve itself is quotiented by `SE(3)`, while `(k_1,k_2)` is quotiented by the constant normal-plane `SO(2)` gauge.

The normal object is therefore a **class**, not a preferred frame.

---

## 11. Exact identifiability of the MINI factorization

From the exact time-parametrized observation:

\[
v(t)=\|\dot\gamma(t)\|
\]

is determined uniquely. Arc length `s(t)` and unit tangent `T(s)` are therefore determined.

A Bishop frame is determined by the choice of one initial oriented normal pair. Any two such choices differ by a constant `SO(2)` rotation, and the corresponding Bishop curvature vectors differ by that same gauge.

Conversely, given

\[
(v,[k]_{SO(2)})
\]

and one initial Euclidean frame, the Bishop ODE together with

\[
\dot\gamma(t)=v(t)T(s(t))
\]

reconstructs the trajectory. Different initial Euclidean frames differ by `SE(3)`.

Hence, for this exact protocol,

\[
\boxed{
\left|
\operatorname{Fact}^{0}_{FB,P_0}(Y)
/\bigl(SE(3)\times SO(2)\bigr)
\right|=1.
}
\]

This is the MINI factorization-identifiability result.

Its geometric ingredients are classical; the PSI content is the explicit separation

\[
\text{catalogue}\mid\text{factorization}\mid\text{gauge}\mid\text{recode}\mid\text{normal class}\mid\text{protocol}.
\]

---

## 12. CAT verdict: Frenet singularity is not `birth`

Suppose `kappa` approaches or reaches zero at a point at which the curve remains regular.

The Frenet encoding ceases to be legal there, but the Bishop encoding remains a legal representation of the same regular curve. Because legal Frenet pieces recode into the Bishop representation without adding a new external behavioural sector,

\[
\boxed{
F\to B\text{ at a Frenet singularity is a recode/domain repair, not catalog birth, under MINI-01.}
}
\]

This is a **contract-relative verdict**. It does not assert that every representation failure in every domain is merely a recode.

---

## 13. Falsification pass

The exploratory strong version does **not** survive unchanged. The following cases block a universal statement.

### X1 — loss of regularity

If

\[
\dot\gamma(t_0)=0,
\]

then the present construction of arc length, tangent and Bishop data may fail. MINI-01 makes no claim there.

### X2 — time reparameterization admitted as gauge

If arbitrary orientation-preserving reparameterizations are included in the gauge, `v(t)` is not invariant. The factorization must then quotient timing separately or use arc-length-only shape data.

Therefore the present uniqueness statement requires the observed time parameter to remain part of the protocol.

### X3 — closed curves / periodic frame requirement

On a closed parameter domain, parallel transport of the normal plane may have nontrivial holonomy. A Bishop frame transported once around the loop need not satisfy the same periodic frame condition without an additional holonomy datum.

Therefore the interval normal-form theorem is **not** silently extended to `S^1`.

### X4 — sampled or noisy observations

Derivative estimation, curvature estimation and frame switching may be unstable near low-curvature regions. Exact identifiability does not imply statistical stability.

This is delegated to a later `FS-STAT` experiment.

### X5 — reflections

`SE(3)` does not identify mirror images. If the intended observational gauge is `E(3)` or `O(3)` rather than orientation-preserving rigid motions, the contract must state that explicitly.

---

## 14. What the result establishes

`PASS` for MINI-01 means:

1. the grammar `{F,B}` is finite;
2. the declared rewrite system terminates;
3. it is locally confluent modulo the declared gauge;
4. every legal finite Frenet/Bishop segmentation on an open interval has one Bishop normal **class**;
5. under exact time-parametrized observation the `(timing, Bishop-shape)` factorization is identifiable modulo `SE(3) x SO(2)`;
6. Frenet failure at zero curvature does not force a PSI-CAT `birth` in this contract.

---

## 15. What the result does NOT test

MINI-01 does **not** establish:

- noisy-data consistency;
- robustness under finite sampling;
- a canonical global frame representative;
- periodic normalization for closed curves;
- uniqueness under arbitrary time reparameterization;
- general confluence of PSI-CAT;
- general identifiability of arbitrary system factorizations;
- a new differential-geometric Frenet/Bishop theorem;
- universal sufficiency of CORE5.

---

## 16. Dual-operator verdict

### `E` — exploratory proposal

Strong proposal: every admissible Frenet/Bishop realization of a regular trajectory normalizes to one canonical decomposition.

### `A` — audit reduction

Replace `canonical decomposition` by a **normal equivalence class** and add exact hypotheses: regular `C^3` interval curve, fixed time parameter, exact observation, `SE(3) x SO(2)` gauge.

### `E_fals` — attacks

Regularity failure, reparameterization gauge, closed-loop holonomy and noisy derivative recovery defeat the unrestricted proposal.

### `A_freeze` — surviving claim

\[
\boxed{
\begin{minipage}{0.88\linewidth}
For an exactly observed, time-parametrized `C^3` regular curve on an interval, every finite legal Frenet/Bishop segmentation reduces, under Frenet-to-Bishop recoding and Bishop gluing, to a unique global Bishop factorization class modulo orientation-preserving rigid motion and constant normal-plane rotation. In this contract, a Frenet singularity caused by vanishing curvature is a representation/domain event, not evidence for catalog birth.
\end{minipage}
}
\]

**Freeze level:** `BRIDGE / MINI`, not CORE theorem.

---

## 17. Next legal step

The next step is **not** to generalize the theorem immediately.

Run two attacks in parallel:

1. `FS-STAT-01` — finite sampling/noise/low-curvature stability and held-out adequacy;
2. `CLOSED-FRAME-01` — add loop holonomy and test whether it remains derived data or creates genuine pressure on the current candidate/gauge/frame architecture.

Only after those tests should CAT–FACT–NORM be generalized beyond this MINI.