# PRINCIPIA SEMANTICA — FOUR-VOLUME SKELETON 03

**Status:** `CURRENT EDITORIAL SKELETON / POST-V2-WHOLE-CROSSCHECK`  
**Date:** 2026-09-29  
**Canonical source:** physical `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Current claim source:** `docs/claim-registry-13.md`  
**Current falsifier source:** `docs/falsifier-registry-12.md`  
**Regression source:** `docs/regression-bank-01.md`  
**Freeze source:** `docs/principia-v1-v2-freeze-01.md` **subject to** `docs/principia-v1-v2-freeze-01-errata-01.md`  
**V1 status:** `NORMALIZED PASS`  
**V2 status:** `II.1–II.16 MATHEMATICAL GLOBAL PASS`  
**Whole-V2 audit:** `docs/principia-v2-whole-crosscheck-01.md`

This supersedes `principia-volume-skeleton-02.md` as the **current editorial pointer**. Skeleton 02 and its addendum remain genealogy.

---

# 0. Redaction rule

\[
\boxed{
\text{PHYSICAL CANON}
\to
\text{CURRENT CLAIM/FALSIFIER REGISTRIES}
\to
\text{FREEZE + ERRATA}
\to
\text{UNIT PROSE}
\to
\text{LOCAL CROSSCHECK}
\to
\text{LAYER CROSSCHECK}
\to
\text{WHOLE-VOLUME CROSSCHECK}.
}
\]

Permanent process rule:

\[
\boxed{
\text{sequence of local PASSes}
\not\Rightarrow
\text{whole-layer PASS}.
}
\]

---

# Volume I — Fundamenty

**Status:** `FIRST PROSE PASS / NORMALIZED PASS`.

## I.1 Kontrakt i role semantyczne

CORE5:

\[
\mathfrak P_c=(\Omega_c,\Psi_c,\mathcal K_c,\mathscr O_{\mathcal T,c},\delta_c).
\]

Role must remain semantically distinct. Candidate stuffing is prohibited.

## I.2 Obserwacja, włókno i adekwatność katalogu

\[
F_c(Y)=\Psi_c^{-1}(\mathcal K_c^Y).
\]

Catalog adequacy precedes fibre identification; no universal scalar `D_ADEQ^cat` is a CORE primitive.

## I.3 Rozróżnienie zadaniowe i legalna redukcja

\[
\mathscr R_{\mathcal T,c},
\qquad
E_{\mathcal T,c},
\qquad
M_{\mathcal T,c}.
\]

Task-information adequacy:

\[
\ker_{eq}\rho\subseteq E_{\mathcal T,c}.
\]

This is not the whole contract-legality test.

## I.4 Historia i pamięć

\[
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H').
\]

\[
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
\]

## I.5 Dokładność, stabilność, licencja statystyczna

\[
\mathrm{ID}_{exact}\not\Rightarrow\mathrm{ID}_{stable},
\qquad
\mathrm{ID}_{stable}\not\Rightarrow\mathrm{CONF}_{1-\alpha}.
\]

## I.6 Granice metodologiczne

Permanent distinctions include:

- representation != world;
- unobserved != zero;
- PSI-ID != PSI-CAT;
- symmetry != automatically legal gauge;
- realization equivalence != behavioural recoding;
- no primitive growth without a new typed semantic-role counterexample.

---

# Volume II — Twierdzenia i mosty strukturalne

**Status:** `II.1–II.16 MATHEMATICAL GLOBAL PASS` after `principia-v2-whole-crosscheck-01.md`.

## A. Własny kręgosłup ilorazowy — II.1–II.9

### II.1 Dokładna rozstrzygalność zadaniowa

\[
|q_{\mathcal T,c}(F_c(Y))|=1
\iff
F_c(Y)\neq\varnothing
\land
F_c(Y)^2\subseteq E_{\mathcal T,c}.
\]

### II.2 Kryterium faktoryzacji

\[
\ker_{eq}\rho\subseteq\ker_{eq}R
\iff
\exists!g:\operatorname{im}\rho\to W,
\quad R=g\circ\rho.
\]

Uniqueness only on `im rho` (F60).

### II.3 Globalna wystarczalność obserwatora

\[
\ker_{eq}\Psi_c\subseteq E_{\mathcal T,c}
\iff
q_{\mathcal T,c}\text{ factors through }\Psi_c.
\]

### II.4 Adekwatność reprezentacji

\[
\ker_{eq}\rho\subseteq E_{\mathcal T,c}.
\]

### II.5 Legalność informacyjna redukcji

\[
\ker_{eq}q\subseteq E_{\mathcal T,c}.
\]

F55/F57 remain mandatory scope locks.

### II.6 Deterministyczna dynamika ilorazowa

\[
xEy\Rightarrow\delta(x)E\delta(y)
\]

iff deterministic dynamics descends to the quotient.

### II.7 Dokładna adekwatność pamięci

\[
\ker_{eq}\rho_t\subseteq\equiv_{\mathcal T,t}.
\]

### II.8 Najgrubszy dokładny iloraz historii

\[
M_{\mathcal T,t}=\mathcal H_t/\!\equiv_{\mathcal T,t}.
\]

Coarsest in quotient order, not bit/storage/compute minimality.

### II.9 Rekurencyjna aktualizacja ilorazu historii

\[
U_{\mathcal T,t}([H],\varepsilon,y)
=
[\delta_t(H,\varepsilon,y)]_{\mathcal T,t+1}.
\]

Source/result IDs: C45+C59. Proof dependency: II.7 / C57-C58 + typed extension definitions. II.6 is structural analogy; II.8 is not a proof prerequisite.

---

## B. Klasyczne mosty — II.10–II.12

### II.10 Silna lumpowalność Markowa

\[
xEy\Rightarrow P(x,C)=P(y,C)
\quad\forall C\in S/E.
\]

F61:

\[
\text{task quotient}\not\Rightarrow\text{Markov lumpability}.
\]

### II.11 Myhill–Nerode

For full right-continuation tests:

\[
E_{\mathcal T,L}
=
\bigcap_w\ker R_w
=
\equiv_L.
\]

### II.12 Paige–Tarjan

Classical finite relational coarsest-partition algorithm, applicable only after an explicit PT1–PT4 reduction proof.

Standard refinement bound: `O(m log n)`; explicit-input accounting must include initialization/storage.

---

## C. CAT / FACT / NORM — II.13–II.14

### II.13 Kanoniczny zakres PSI-CAT i PSI-FACT

Current canonical definitions are C62/C63. Older ISO/HOR/REF/CRS and groupoid/homotopy FACT structures are derived extensions C66, not universal definitions.

### II.14 CAT–FACT–NORM–MINI after Errata 01

Gauge-only factorization candidate space:

\[
\mathfrak F^{0}_{FB,P}(Y)=\operatorname{RawFact}^{0}_{FB,P}(Y)/G_P
\]

may be non-singleton.

Correct exact result:

\[
\boxed{|\operatorname{im}NF|=1}
\]

and equivalently

\[
\boxed{|\mathfrak F^{0}_{FB,P}(Y)/\!\equiv_{NF}|=1.}
\]

C19-v3/C67/F62 are current. C19-v2 is withdrawn.

---

## D. FRAME — II.15

Normal/Bishop holonomy:

\[
H_\gamma\in SO(2).
\]

Periodic transported RMF iff

\[
H_\gamma=I.
\]

On the stronger global Frenet domain:

\[
H_\gamma
=R_{-\int\tau ds}
\pmod{2\pi}
\]

up to sign convention.

Holonomy is primary; total torsion is a coordinate in the stronger sector.

---

## E. HIGHER — II.16

Minimal witness:

\[
*\to B\mathbb Z_2\leftarrow *.
\]

\[
\left|\pi_0(*\times^h_{B\mathbb Z_2}*)\right|=2
\neq
1=
\left|*\times_{\pi_0(B\mathbb Z_2)}*\right|.
\]

Task-relevant witness/stabilizer data must survive representation/truncation. Richer representation does not imply a new CORE role.

---

# Volume III — Realizacje / Modele / Laboratoria

**Status:** `NEXT MAJOR CONTENT PHASE after V2 closure and editorial normalization`.

Planned retained laboratories:

1. PHISICA / operator reductions;
2. HCube — R01;
3. LAZARUS;
4. Go — R02;
5. Frenet/Bishop + FS-STAT — R03;
6. Agent / handoff / regression governance;
7. PSI-FORUM;
8. SOP / genomic and other domain adapters;
9. OPEN-PSI.

Rule:

\[
\boxed{
\text{laboratory PASS}\not\Rightarrow\text{theorem promotion}.
}
\]

---

# Volume IV — Genealogia

Preserve:

- superseded claims;
- old CAT/FACT calculi;
- Integrata / Universalia / LOGOS genealogy;
- model and agent genealogy;
- correction history including Freeze Errata 01;
- historical maps/skeletons.

\[
\boxed{\text{superseded}\neq\text{erased}.}
\]

---

# Current editorial gates

Any new or revised theorem unit must carry:

`ID | TYPE | HYPOTHESES | STATUS | SOURCE | PROOF/DERIVATION | BOUNDARY/FALSIFIER | REGRESSION | PROOF DEPENDENCY | STRUCTURAL ANALOGY | DOWNSTREAM USE`.

Any semantic change after Freeze 01 requires:

\[
\boxed{
\text{ERRATA}\to\text{IMPACT}\to\text{REGRESSION}\to\text{HANDOFF}.
}
\]

Current permanent no-go set includes F55–F62.

---

# Current execution order

\[
\boxed{
\mathrm{V1\ NORMALIZED\ PASS}
\to
\mathrm{V2\ II.1:II.16\ MATHEMATICAL\ GLOBAL\ PASS}
\to
\mathrm{V2\ CONTROL\ NORMALIZATION}
\to
\mathrm{VOLUME\ III/PHISICA\!\!-\!LOGOS\ MIGRATION}.
}
\]

CORE5 remains frozen. Agent Architecture v02 remains current.
