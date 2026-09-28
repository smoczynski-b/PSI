# PSI — HIGHER-FIBRE-01

**Status:** COMPLETED PRESSURE TEST / BRIDGE / CORE5 SURVIVES  
**Agent:** PSI Agent Architecture v02  
**Date:** 2026-09-28

## 0. Router

Primary level:

\[
\boxed{\mathrm{DERIVED}}
\]

Secondary tag:

\[
\mathrm{CORE\!-\!PRESSURE}.
\]

The question is not whether homotopy/groupoid structure exists. The question is whether task-relevant witness/stabilizer data force a semantic role not representable by the current CORE5 contract.

---

## 1. Contract snapshot

Use the exact 1-groupoid witness

\[
*\longrightarrow B\mathbb Z_2\longleftarrow *
\]

where `B Z_2` is the one-object groupoid with automorphism group `Z_2={e,s}` and both maps select its unique object.

Freeze:

- object class: small groupoids / explicit groupoid presentations;
- task: distinguish compatibility witnesses / isotropy when declared task-relevant;
- protocol: exact, no noise/tolerance;
- gauge: equivalences that preserve the declared task semantics;
- domain: 1-groupoids are sufficient for the witness; no universal infinity-categorical theorem is claimed;
- source status: classical groupoid/homotopy pullback construction + PSI representation/pressure interpretation.

---

## 2. Strict object-set pullback versus weak pullback

If one first forgets all morphisms and keeps only object sets, then

\[
\operatorname{Ob}(*)=\{*\},
\qquad
\operatorname{Ob}(B\mathbb Z_2)=\{*\}.
\]

Hence the strict set pullback is

\[
\boxed{
\{*\}\times_{\{*\}}\{*\}=\{*\}.
}
\]

Now form the weak/2-pullback of groupoids.

An object is a triple

\[
(*,*,\alpha)
\]

where

\[
\alpha:*\to *
\]

is an isomorphism in `B Z_2`.

Therefore

\[
\alpha\in\{e,s\}.
\]

Because the two terminal source groupoids have only identity arrows, distinct `alpha` values are not identified by source-side morphisms. Thus the weak pullback is equivalent here to the discrete two-element groupoid:

\[
\boxed{
*\times^h_{B\mathbb Z_2}*
\simeq
\mathbb Z_2^{\rm disc}.
}
\]

Consequently

\[
\boxed{
\left|\pi_0\!\left(*\times^h_{B\mathbb Z_2}*\right)\right|=2,
}
\]

while

\[
\boxed{
\left|*\times_{\pi_0(B\mathbb Z_2)}*\right|=1.
}
\]

Hence coarse truncation before forming the compatibility fibre can destroy witness multiplicity:

\[
\boxed{
\pi_0(A\times_C^h B)
\not\cong
\pi_0(A)\times_{\pi_0(C)}\pi_0(B)
}
\]

in this witness.

This is classical higher/groupoid structure. PSI claims no novelty for the categorical fact.

---

## 3. Task-sensitive interpretation

Let the task observable on the weak fibre be

\[
R_\alpha(*,*,\alpha)=\alpha\in\mathbb Z_2.
\]

Then

\[
R_\alpha(e)\neq R_\alpha(s).
\]

The coarse strict set fibre contains only one point and therefore cannot represent this distinction.

If

\[
\rho_{\rm coarse}:\{e,s\}\to\{*\}
\]

is the coarse representation, then

\[
\ker_{\rm eq}\rho_{\rm coarse}
\not\subseteq
\ker_{\rm eq}R_\alpha.
\]

Thus, by the ordinary PSI factorization criterion,

\[
\boxed{
\rho_{\rm coarse}\text{ is task-insufficient whenever the witness }\alpha\text{ matters}.}
\]

If the task is invariant under `alpha`, then the same coarse representation may be adequate.

Therefore higher data are not automatically relevant; relevance is contract/task-relative.

---

## 4. Stabilizer witness

A separate but related regression is

\[
B1
\qquad\text{versus}\qquad
B\mathbb Z_2.
\]

Both have one connected component:

\[
\pi_0(B1)=\pi_0(B\mathbb Z_2)=\{*\},
\]

but their stabilizers differ:

\[
\operatorname{Aut}_{B1}(*)=1,
\qquad
\operatorname{Aut}_{B\mathbb Z_2}(*)\cong\mathbb Z_2.
\]

A task sensitive to isotropy/stabilizer structure must therefore not use `pi_0` alone as its candidate representation.

Again the defect is exactly representation inadequacy:

\[
\ker\rho_{\pi_0}\not\subseteq E_{\mathcal T}
\]

for a stabilizer-sensitive task.

---

## 5. CORE5 reduction

The witness-bearing problem can be represented without a sixth semantic role.

### Candidate

Use witness-decorated / structured candidates, e.g.

\[
\widetilde\Omega
=
\{(*,*,e),(*,*,s)\}
\]

for the minimal witness, or more generally a declared coding/presentation of the task-relevant groupoid/homotopy object.

### Observation

The observation may remain coarse:

\[
\Psi(e)=\Psi(s)=Y,
\]

so the compatible fibre is

\[
F(Y)=\{e,s\}.
\]

### Task observables

If the task sees the witness, include

\[
R_\alpha(e)=e,
\qquad
R_\alpha(s)=s.
\]

Then the task equivalence separates the two candidates.

If the task is witness-invariant, omit that distinction and the task quotient may identify them.

### Compatibility

A bare yes/no compatibility relation need not itself carry witness multiplicity if the witness is retained in the candidate representation. Equivalently, the observation space may be witness-decorated under another legal contract.

### Dynamics / transport

If morphisms/coherences evolve, the structured candidate representation and declared transition/transport can retain them. No distinct sixth role is forced by this witness.

---

## 6. Gauge correction

The phrase

`candidate space after gauge quotient`

must not be read as

`coarse orbit set regardless of task`.

A coarse quotient is legal only if it preserves all distinctions required by the contract.

For a proposed reduction

\[
q_G:\Omega\to\Omega/G,
\]

task legality requires

\[
\boxed{
\ker_{\rm eq}q_G\subseteq E_{\mathcal T}.
}
\]

If stabilizers, isotropy or compatibility witnesses are task-relevant, replacing a quotient groupoid/stack-like object by its orbit set can violate this condition.

Thus:

\[
\boxed{
\text{gauge reduction must itself pass the representation-adequacy test}.}
\]

This is a clarification of CORE5 usage, not an added primitive.

---

## 7. Order-of-operations regression

The permanent higher-fibre regression is:

\[
\boxed{
\text{preserve higher compatibility data first}
\to
\text{take only task-legal truncation afterward}.
}
\]

Do not assume

\[
\text{truncate inputs}
\to
\text{strict fibre}
\]

is equivalent.

The `B Z_2` witness proves that the two orders can differ.

---

## 8. R4 pressure table

| Gate | Test | Result |
|---|---|---|
| candidate | can witness/stabilizer data be represented in `Omega`? | YES — structured/witness-decorated candidates |
| observation | can coarse/enriched readout be declared explicitly? | YES |
| compatibility | can witness data be retained by candidate or observation instead of erased? | YES |
| task | can task observables distinguish witness/stabilizer data when relevant? | YES |
| dynamics/transport | can structured transitions preserve the relevant data? | YES under declared contract |
| contract | can legal truncation/gauge be constrained by task adequacy? | YES |
| task-relevant loss after reduction | unavoidable? | NO |
| minimal sixth role | demonstrated? | NO |

Therefore

\[
\boxed{
\mathrm{HIGHER\!-\!FIBRE\!-01}:
\mathrm{CORE5\ SURVIVES}.}
\]

---

## 9. What this result does not test

This run does **not** claim:

- that every infinity-categorical problem admits a convenient finite set encoding;
- that all coherence information can always be replaced by finitely many invariants;
- that homotopy fibres are unnecessary mathematics;
- that `pi_0` is always inadequate;
- that stabilizers are always task-relevant;
- that arbitrary higher dynamics have already been formalized in the current public core.

It establishes only that the canonical minimal witness does not force a sixth semantic role once candidate representation and gauge legality are made task-relative.

---

## 10. Freeze verdict

Freeze the following bridge statements:

\[
\boxed{
\text{higher/groupoid data may be necessary for an adequate representation,}
}
\]

but

\[
\boxed{
\text{necessity of richer representation}\neq\text{necessity of a new CORE role}.
}
\]

The decisive adequacy condition remains

\[
\boxed{
\ker_{\rm eq}\rho\subseteq E_{\mathcal T}.
}
\]

The next legal step is the cross-branch `R4 PRESSURE COURT`, not another higher-fibre extension.