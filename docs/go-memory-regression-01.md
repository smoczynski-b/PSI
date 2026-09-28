# PSI — GO-MEMORY-REGRESSION-01

**Status:** COMPLETED REGRESSION / MEMORY-REPRESENTATION BENCHMARK / NO CORE CHANGE  
**Date:** 2026-09-28  
**Agent:** PSI Agent Architecture v02

## 0. Purpose

This run belongs to the post-R4 hardening phase.

It does not study Go strategy. It uses frozen Go legality tests as a benchmark for the question:

\[
\boxed{
\text{when does a compressed memory }\rho_t(H_t)
\text{ preserve all future distinctions required by the task?}
}
\]

Primary level:

\[
\boxed{\mathrm{LAB/BENCHMARK}\to\mathrm{REPRESENTATION\ ADEQUACY}.}
\]

No new PSI primitive is under consideration.

---

## 1. Source boundary

The recovered RED-1 source explicitly freezes four Go results:

- `G0` — no-ko rules;
- `G2` — simple ko;
- `G3` — positional superko;
- `G4` — situational superko.

The same recovered artifact does **not** state a separate `G1` result.

Therefore this benchmark preserves the historical series label `G0–G4`, but does not invent a missing `G1` theorem, board witness or memory representation.

\[
\boxed{G1=\mathrm{SOURCE\ GAP}\quad\text{in the presently recovered source set}.}
\]

This is a provenance limitation, not a mathematical contradiction.

---

## 2. General memory criterion

Let

\[
\mathcal H_t
\]

be the history space at time `t` and let

\[
H\equiv_{\mathcal T,t}H'
\]

mean that the two histories have the same future task semantics.

For a memory representation

\[
\rho_t:\mathcal H_t\to R_t,
\]

exact task sufficiency is

\[
\boxed{
\rho_t(H)=\rho_t(H')
\Rightarrow
H\equiv_{\mathcal T,t}H'.
}
\]

Equivalently,

\[
\boxed{
\ker_{eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

A single pair

\[
\rho_t(H)=\rho_t(H'),
\qquad
H\not\equiv_{\mathcal T,t}H'
\]

is therefore a complete falsifier of the proposed memory representation.

This is the same factorization/adequacy logic used throughout PSI; Go contributes concrete finite witnesses.

---

## 3. Recovered Go ladder

Write

\[
B_t=\text{current board},
\qquad
\sigma_t=\text{player to move}.
\]

### G0 — no ko

Frozen sufficient representation:

\[
\boxed{
\rho_0(H_t)=(B_t,\sigma_t).
}
\]

For next-move legality under the frozen no-ko rules,

\[
\boxed{
\ker\rho_0
\subseteq
\equiv_{\mathcal T_{\rm no\,ko}}.
}
\]

Thus the current situation is sufficient; no historical memory is required for this task.

---

### G2 — simple ko

The recovered witness contains histories `H_A,H_B` with

\[
(B_t,\sigma_t)_A=(B_t,\sigma_t)_B
\]

but different legality of the same next move.

Therefore

\[
\boxed{
\ker\rho_0
\not\subseteq
\equiv_{\mathcal T_{\rm ko}}.
}
\]

The frozen sufficient repair is

\[
\boxed{
\rho_K(H_t)=(B_t,\sigma_t,B_{t-1}).
}
\]

and

\[
\boxed{
\ker\rho_K
\subseteq
\equiv_{\mathcal T_{\rm ko}}.
}
\]

The rule change makes one-step board history task-relevant.

---

### G3 — positional superko

The simple-ko representation is insufficient:

\[
\boxed{
\ker\rho_K
\not\subseteq
\equiv_{\mathcal T_{\rm PSK}}.
}
\]

Define the set of boards previously visited:

\[
V_t=\{B_0,\ldots,B_t\}.
\]

The frozen sufficient representation is

\[
\boxed{
\rho_{\rm PSK}(H_t)
=(B_t,\sigma_t,V_t).
}
\]

with

\[
\boxed{
\ker\rho_{\rm PSK}
\subseteq
\equiv_{\mathcal T_{\rm PSK}}.
}
\]

Thus positional superko requires history only up to the set of previously visited **boards**.

---

### G4 — situational superko

The positional-superko memory is insufficient:

\[
\boxed{
\ker\rho_{\rm PSK}
\not\subseteq
\equiv_{\mathcal T_{\rm SSK}}.
}
\]

Define the set of previously visited situations:

\[
U_t=\{(B_i,\sigma_i):i\le t\}.
\]

The frozen sufficient representation is

\[
\boxed{
\rho_{\rm SSK}(H_t)
=(B_t,\sigma_t,U_t).
}
\]

and

\[
\boxed{
\ker\rho_{\rm SSK}
\subseteq
\equiv_{\mathcal T_{\rm SSK}}.
}
\]

Hence forgetting the player-to-move component of historical situations can identify histories whose next-move legality differs.

---

## 4. What the ladder means

The recovered progression is

\[
(B_t,\sigma_t)
\to
(B_t,\sigma_t,B_{t-1})
\to
(B_t,\sigma_t,V_t)
\to
(B_t,\sigma_t,U_t).
\]

This must **not** be read as the discovery of four new PSI state primitives.

It is a sequence of candidate representations for different tasks/rule systems:

\[
\boxed{
\rho\text{ changes because }\mathcal T\text{ changes}.}
\]

Each failure has the same form:

\[
\boxed{
\rho(H)=\rho(H')
\quad\text{while}\quad
H\not\equiv_{\mathcal T}H'.
}
\]

Therefore the series is a finite regression bank for representation adequacy.

---

## 5. Canonical history quotient

Let

\[
M_{\mathcal T,t}
=\mathcal H_t/\!\equiv_{\mathcal T,t},
\qquad
q_{\mathcal T,t}:\mathcal H_t\to M_{\mathcal T,t}.
\]

For every exact task-sufficient representation

\[
\rho_t:\mathcal H_t\to R_t,
\]

there exists a unique map

\[
f_t:\operatorname{im}\rho_t\to M_{\mathcal T,t}
\]

such that

\[
\boxed{
q_{\mathcal T,t}=f_t\circ\rho_t.
}
\]

Thus

\[
\ker\rho_t
\subseteq
\ker q_{\mathcal T,t}
=\equiv_{\mathcal T,t}.
\]

Therefore:

\[
\boxed{
M_{\mathcal T,t}
\text{ is the coarsest exact quotient of histories for task }\mathcal T.
}
\]

This is a minimality statement in the **order of quotients**.

It is not a theorem that `M_T,t` minimizes:

- dimension;
- number of coordinates;
- number of bits;
- storage cost;
- computational complexity.

---

## 6. Recursive update

The recovered RED-1 result also gives a mathematically well-defined partial update

\[
U_{\mathcal T,t}
\]

on task classes:

\[
\boxed{
U_{\mathcal T,t}
([H_t],\varepsilon_t,y_{t+1})
=
[\delta_t(H_t,\varepsilon_t,y_{t+1})]_{\mathcal T,t+1}.
}
\]

Equivalently,

\[
q_{\mathcal T,t+1}
(H_t\oplus(\varepsilon_t,y_{t+1}))
=
U_{\mathcal T,t}
(q_{\mathcal T,t}(H_t),\varepsilon_t,y_{t+1}).
\]

This says that the exact task state is recursively updateable **mathematically** once the quotient congruence condition holds.

It does not establish:

\[
\boxed{
\text{finite memory, effective computability or an efficient algorithm}.}
\]

Those are separate questions.

---

## 7. Representation order is task-relative

The ladder must not be interpreted as a universal absolute order

\[
\rho_0<\rho_K<\rho_{\rm PSK}<\rho_{\rm SSK}
\]

independent of task.

For the no-ko legality task, the extra memory is unnecessary.

For simple ko, one previous board is enough under the frozen rules.

For positional superko, the set of prior boards is the relevant summary.

For situational superko, the historical player-to-move information must also survive.

Therefore:

\[
\boxed{
\text{memory adequacy is relative to the future distinctions encoded by }\mathcal T.
}
\]

---

## 8. Relation to LAZARUS

Go and LAZARUS instantiate the same abstract failure mode:

\[
\boxed{
\text{a compressed present can identify histories whose future task semantics differ}.}
\]

But they test different concrete structures:

- Go: rule-dependent legality and historical exclusion;
- LAZARUS: executable actions, branch structure and world/operational correlation.

Neither requires a new primitive; both test candidate/history representation adequacy.

---

## 9. Permanent regressions

A future memory/state representation must pass all relevant tests:

1. **no-ko:** current board + player suffices;
2. **simple ko:** current situation alone must fail on the frozen witness; one previous board repairs it;
3. **PSK:** one-step history must fail; visited-board set repairs it;
4. **SSK:** visited-board set must fail; visited-situation set repairs it;
5. **minimality discipline:** do not call the canonical quotient bit-minimal or computationally minimal;
6. **recursion discipline:** mathematical recursive update does not imply bounded/finite memory or efficient computation;
7. **source discipline:** do not reconstruct `G1` without its actual source.

---

## 10. What this result does not test

This run does not establish:

- optimal Go strategy;
- equivalence of different real-world Go rule sets beyond the frozen contracts;
- computational complexity of maintaining `V_t` or `U_t`;
- bit-minimal encodings of superko memory;
- probabilistic or approximate memory sufficiency;
- finite-state realizability of the general quotient `M_T,t`;
- the missing historical content of `G1`.

---

## 11. Freeze verdict

Freeze the common schema:

\[
\boxed{
\mathrm{ADEQ}_{\rm mem}(\rho,\mathcal T)=1
\iff
\ker_{eq}\rho_t
\subseteq
\equiv_{\mathcal T,t}.
}
\]

and the interpretation:

\[
\boxed{
\text{Go G0/G2/G3/G4 are representation regressions, not primitive growth}.}
\]

No CORE change and no Agent architecture change are justified.

Next hardening target:

\[
\boxed{\mathrm{FS\!-\!STAT\!-01}.}
\]