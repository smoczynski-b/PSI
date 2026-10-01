# PRINCIPIA SEMANTICA — VOLUME III THEOREM MAP 12

**Status:** `CURRENT / III.1:III.14 CLOSED AS TYPED / III.7:III.14 COMPOSITION PASS / P9 GENERAL OPEN`  
**Date:** 2026-10-01  
**Supersedes for control:** `principia-v3-theorem-map-11.md`

---

# 1. Closed blocks

\[
\boxed{\mathrm{III.1:III.6\ PHISICA}=GLOBAL\ PASS}
\]
\[
\boxed{\mathrm{III.7:III.8\ MOST/HCube}=GLOBAL\ PASS}
\]
\[
\boxed{\mathrm{III.9\ DOM\!-\!LOGOS}=PASS/COMPOSITION\ PASS}
\]
\[
\boxed{\mathrm{III.10\ SOP\!-\!11E}=SECTOR\ PASS}
\]
\[
\boxed{\mathrm{III.11\ P9\!-\!G}=PASS}
\]
\[
\boxed{\mathrm{III.12\ P9\!-\!H}=PASS}
\]
\[
\boxed{\mathrm{III.13\ P9\!-\!I}=PASS/COMPOSITION\ PASS}
\]
\[
\boxed{\mathrm{III.14\ P9\!-\!POLY}=PASS/COMPOSITION\ PASS}
\]

with
\[
\boxed{P2_{\rm general}=PARTIAL},
\qquad
\boxed{P9_{\rm general}=OPEN/CENTRAL}.
\]

---

# 2. III.14 contract

Let \(A\) generate a bounded linear \(C_0\)-semigroup \(T(t)\) on a complex Hilbert space, with
\[
i\mathbb R\subset\rho(A),
\qquad
\alpha>0.
\]
Then the Borichev–Tomilov theorem identifies polynomial high-frequency resolvent growth with polynomial decay of regularized dynamics, in particular
\[
\boxed{
\|R(is,A)\|=O(|s|^\alpha)
\Longleftrightarrow
\|T(t)A^{-1}\|=O(t^{-1/\alpha})
}
\]
under the precise asymptotic conventions and equivalent formulations stated in III.14.

**Classification:** `CLASSICAL / ADAPTED`; not `PSI-NEW`.

Primary unit:

`principia-v3-14-p9-poly-resolvent-regularized-decay.md`.

---

# 3. Composition result

The combined operator layer now satisfies
\[
\boxed{\mathrm{III.7:III.14}=\mathrm{COMPOSITION\ PASS}.}
\]

Permanent distinctions include
\[
\boxed{
\text{full resolvent profile}
\neq
\text{full semigroup profile},
}
\]
\[
\boxed{
\omega_0=s_0
\neq
\text{polynomial regularized decay data},
}
\]
and
\[
\boxed{
T(t)A^{-1}
\neq
T(t).
}
\]

III.14 is therefore a restricted structural bridge compatible with MOST/HCube, not a universal inversion theorem.

---

# 4. Falsifier locks

F63 and F64 remain active. III.14 additionally freezes:

1. boundedness of the semigroup as an input hypothesis;
2. \(i\mathbb R\subset\rho(A)\);
3. the distinction between raw and regularized dynamics;
4. operator-norm \(O\) versus pointwise \(o\);
5. the Hilbert/Banach boundary.

No CORE5 extension is introduced.

---

# 5. Current front

The selected P9-POLY front is closed as a typed theorem unit. The unrestricted P9 problem remains open, but no further theorem candidate has yet passed a fresh selection gate.

Therefore
\[
\boxed{\mathrm{NEXT\ AUTOMATIC}=NONE.}
\]

A future III.15 requires a new explicit problem selection and source/contract gate.
