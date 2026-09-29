# PRINCIPIA SEMANTICA — VOLUME III THEOREM MAP 07

**Status:** `CURRENT / PHISICA GLOBAL PASS / MOST-HCUBE GLOBAL PASS / III.9 DOM-LOGOS PASS / III.10 SOP-11E SECTOR PASS / III.11 P9-G PASS / P9-U SOURCE GATE NEXT`  
**Date:** 2026-09-29  
**Supersedes for control:** `principia-v3-theorem-map-06.md`

---

# 1. Closed blocks

## PHISICA III.1–III.6

\[
\boxed{\mathrm{GLOBAL\ PASS\ AFTER\ LOCAL\ ERRATA\ 01}}.
\]

## MOST / HCube III.7–III.8

\[
\boxed{\mathrm{MATHEMATICAL\ GLOBAL\ PASS}}.
\]

## DOM-LOGOS III.9

\[
\boxed{\mathrm{PASS / COMPOSITION\ PASS}}.
\]

## SOP-11E III.10

\[
\boxed{\mathrm{SECTOR\ PASS}},
\qquad
\boxed{P2_{\rm general}=PARTIAL}.
\]

---

# 2. P9 migration result

The P9 migration gate found that older working material conflated:

1. the energy Hessian \(H_L=D^2L\);
2. the dissipative Hermitian part \(-\operatorname{Re}A\);
3. raw resolvent sensitivity;
4. the continuous-time Kreiss constant.

These are now separated.

Invalid working claims withdrawn include:

- nonnormality with \([H,N]=0\) in a decomposition \(A=-H+N\), \(H^*=H\), \(N^*=-N\);
- \(\mathcal K(-\mu I)\to\infty\) as \(\mu\to0\);
- treating the transient Jordan block as having \(H=\mu I>0\) plus a skew-adjoint remainder in the same norm;
- universal no-bridge conclusions whose proofs relied on these claims.

`p9-hessian-transient-migration-01.md` is the current repair source.

---

# 3. III.11 — P9-G metric-gradient bridge

For

\[
A=-G^{-1}H,
\qquad
G=G^*>0,
\quad
H=H^*>0,
\]

define

\[
B=G^{-1/2}HG^{-1/2},
\qquad
\mu_G=\lambda_{\min}(B).
\]

Then in the energy metric:

\[
\boxed{
\|e^{tA}\|_G=e^{-\mu_Gt}
}
\]

and

\[
\boxed{
\|(zI-A)^{-1}\|_G
=
\frac{1}{\operatorname{dist}(z,-\sigma(B))}.
}
\]

Hence

\[
\boxed{\mathcal K_G(A)=1}.
\]

In Euclidean norm:

\[
\boxed{
\|e^{tA}\|_2
\le
\sqrt{\kappa_2(G)}e^{-\mu_Gt},
}
\]

\[
\boxed{
\|(zI-A)^{-1}\|_2
\le
\frac{\sqrt{\kappa_2(G)}}{\operatorname{Re}z+\mu_G},
}
\]

so

\[
\boxed{
1\le\mathcal K_2(A)\le\sqrt{\kappa_2(G)}.
}
\]

III.11 also supplies an explicit \(2\times2\) witness with positive \(G,H\) for which the energy norm is strictly contractive but the Euclidean numerical abscissa is positive, proving that transient growth is metric-relative.

**III.11 STATUS:** `THEOREM PROSE PASS / PROOF PASS / LOCAL CROSS-CHECK PASS`.

---

# 4. P9 composition result

`principia-v3-p9-composition-crosscheck-01.md` establishes

\[
\boxed{
\mathrm{III.7:III.11}=\mathrm{COMPOSITION\ PASS}.
}
\]

The combined taxonomy is now:

- `P9-G` — metric-gradient sector: CLOSED as III.11;
- `P9-J` — Jordan/defective local laboratory: CLOSED locally;
- `P9-U` — unrestricted nonnormal generators: OPEN / CENTRAL.

MOST/HCube general non-factorization and the P9-G restricted bridge are compatible because the latter assumes an additional common normal form \(B\).

---

# 5. Permanent P9 distinctions

\[
\boxed{
H_L=D^2L
\neq
H_{\rm diss}:=-\frac{A+A^*}{2}
\text{ in general}.
}
\]

\[
\boxed{
\sup_{\operatorname{Re}z\ge0}\|(zI-A)^{-1}\|
\neq
\mathcal K(A).
}
\]

For \(A=-\mu I\):

\[
\boxed{
\mathcal R_0(A)=1/\mu,
\qquad
\mathcal K(A)=1.
}
\]

And for a dissipative decomposition in one fixed norm:

\[
A=-H+N,
\quad H\ge\mu I,
\quad N^*=-N
\]

implies

\[
\boxed{
\|e^{tA}\|\le e^{-\mu t},
\qquad
\mathcal K(A)=1.
}
\]

---

# 6. Current open front

The general P9 problem remains

\[
\boxed{P9_{\rm general}=OPEN/CENTRAL}.
\]

The unresolved subclass `P9-U` contains, among other things:

- degenerate/hypocoercive symmetric parts;
- unbounded nonnormal generators;
- continuous spectrum;
- quantitative resolvent-to-growth bounds in infinite dimension;
- minimal sufficient commutator/structural data.

No III.12 theorem is authorized yet.

The next legal state is

\[
\boxed{
\mathrm{P9\!-
U\ SOURCE/CONTRACT\ GATE\ NEXT}.
}
\]

No CORE5 change and no Agent v03 witness.