# PSI — claim registry 13

**Status:** ACTIVE / PUBLIC DERIVATIVE  
**Supersedes:** `claim-registry-12.md` as current public registry  
**Canonical source:** physical `PSI-R3-CONSOLIDATED-CANON-03` v1.0.0  
**Errata source:** `principia-v1-v2-freeze-01-errata-01.md`

Retain C01–C18 and C20–C66 from `claim-registry-12.md` without semantic change.

C19-v2 is withdrawn and replaced by C19-v3.

---

## C19-v3 — CAT–FACT–NORM–MINI corrected normal-form theorem

Let

\[
\gamma:[0,T]\to\mathbb R^3
\]

be `C^3` and regular with fixed time parameter. Use the finite grammar `{F,B}` and constant Bishop normal-plane gauge `SO(2)`.

Two exact observation contracts remain legal:

### Absolute-coordinate contract

\[
P_0^{abs}:Y_{abs}=\gamma(t),
\qquad
G_{abs}=SO(2)_{normal}.
\]

### Shape contract

\[
P_0^{shape}:Y_{shape}=[\gamma]_{SE(3)},
\qquad
G_{shape}=SE(3)\times SO(2)_{normal}.
\]

For either correctly typed contract:

1. the rewrite `F→B` plus Bishop merge is well-defined on legal gauge classes;
2. it terminates;
3. it is locally confluent and hence confluent by Newman's lemma;
4. every legal finite Frenet/Bishop grammar factorization has the same Bishop normal class;
5. the normalization map
   \[
   \operatorname{NF}:\mathfrak F^{0}_{FB,P}(Y)\to\mathcal N_{FB,P}(Y)
   \]
   has singleton image:
   \[
   \boxed{|\operatorname{im}\operatorname{NF}|=1};
   \]
6. equivalently, the task quotient by equality of normal form has one class:
   \[
   \boxed{
   |\mathfrak F^{0}_{FB,P}(Y)/\!\equiv_{NF}|=1.
   }
   \]

Here

\[
\mathfrak F^{0}_{FB,P}(Y)
=
\operatorname{RawFact}^{0}_{FB,P}(Y)/G_P
\]

is the **gauge-only factorization candidate space**.

No singleton claim is made for this candidate space itself.

**STATUS:** `BRIDGE / EXACT MINI / PASS AFTER FREEZE ERRATA 01`  
**ROLE:** `CAT/FACT/NORM NORMAL-FORM BENCHMARK`  
**SOURCE:** `cat-fact-norm-mini-02.md`  
**FALSIFIER:** F62.

---

## C67 — normal-form identifiability is weaker than literal factorization uniqueness

For a rewrite-normalization problem, distinguish:

\[
\boxed{
\text{gauge-only factorization candidate space}
\mid
\text{normalization map}
\mid
\text{task quotient by normal form}.
}
\]

A unique normal form does not imply that distinct pre-normal factorizations are gauge-equivalent.

Therefore:

\[
\boxed{
|\operatorname{im}\operatorname{NF}|=1
\not\Rightarrow
|\operatorname{RawFact}/G|=1.
}
\]

This is a permanent representation/factorization discipline and the abstract content of F62.

**STATUS:** `SCOPE CORRECTION / FACT DISCIPLINE`.

---

## C20 retained

C20 is unchanged: if `kappa=0` invalidates the Frenet frame while the curve remains regular and Bishop representation remains legal, the event is a representation/domain repair (`recode`), not automatic catalog birth.

---

## Current control state

- physical CANON-03 remains unchanged;
- CORE5 remains frozen;
- Freeze 01 remains active subject to Errata 01;
- current falsifier registry is v12;
- Agent Architecture v02 remains current.
