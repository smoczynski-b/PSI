# PSI — claim registry 08

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-07.md` as current public registry  
**Canonical source:** `PSI-R3-CONSOLIDATED-CANON-03`

This version adds `HCUBE-REGRESSION-01`. CORE5 and Agent Architecture v02 remain unchanged.

## Retained claims C01–C37

Retain C01–C37 from `claim-registry-07.md` without semantic change.

---

## C38 — exact HCube paired witness

Let

\[
A=\operatorname{diag}(2,1,0),
\qquad
B=\begin{pmatrix}2&0&0\\0&1&1\\0&0&0\end{pmatrix}.
\]

Then

\[
\chi_A=\chi_B=\lambda(\lambda-1)(\lambda-2)
\]

and

\[
\|A\|_2=\|B\|_2=2.
\]

At `z=1/2`, however,

\[
\left\|\left(\tfrac12I-A\right)^{-1}\right\|_2=2,
\]

while

\[
\left\|\left(\tfrac12I-B\right)^{-1}\right\|_2
=2(1+\sqrt2).
\]

**STATUS:** `CLASSICAL MATRIX FACT / EXACT BENCHMARK`  
**ROLE:** `HCUBE / REPRESENTATION REGRESSION`.

---

## C39 — coarse spectral-summary insufficiency

For

\[
\rho_0(X)=\left(\chi_X,\|X\|_2\right)
\]

and

\[
R_{1/2}(X)=\left\|\left(\tfrac12I-X\right)^{-1}\right\|_2,
\]

C38 gives

\[
\rho_0(A)=\rho_0(B)
\]

but

\[
R_{1/2}(A)\neq R_{1/2}(B).
\]

Therefore

\[
\boxed{
\ker_{eq}\rho_0
\not\subseteq
\ker_{eq}R_{1/2}.
}
\]

Thus `rho_0` is task-insufficient for the declared resolvent-sensitive task.

**STATUS:** `BRIDGE / REPRESENTATION-ADEQUACY REGRESSION`.

---

## C40 — HCube separator status

For the same pair, the classical bridge

\[
\|e^{t\operatorname{ad}_X}\|_{HS}
=\kappa_2(e^{tX})
\]

also separates the matrices. At `t=1`:

\[
\kappa_2(e^A)=e^2\approx7.38905610,
\]

while

\[
\kappa_2(e^B)\approx8.86992603.
\]

This establishes HCube as a valid diagnostic separator for this benchmark, not as a unique/minimal representation and not as a CORE primitive.

**STATUS:** `CLASSICAL BRIDGE + LAB BENCHMARK`.

---

## C41 — P9/HCube separation retained

The project must preserve the distinction between:

\[
x\mapsto e^{tA}x
\]

and

\[
X\mapsto e^{tA}Xe^{-tA}.
\]

The exact bridge between the similarity-action norm and `kappa(e^{tA})` does not imply that pseudospectra of `ad_A` predict state transient growth.

**STATUS:** `POLICY / CLASSICAL-SCOPE DISCIPLINE`.

---

## Current phase

Primitive search remains stopped. Current work is regression hardening:

\[
\boxed{
\mathrm{HCube\ DONE}
\to
\mathrm{Go\ memory}
\to
\mathrm{FS\!-\!STAT}
\to
\mathrm{Principia\ migration}.
}
\]