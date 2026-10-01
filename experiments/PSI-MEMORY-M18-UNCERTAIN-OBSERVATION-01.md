# PSI-MEMORY-M18-UNCERTAIN-OBSERVATION-01

**Status:** EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 0. Question

Can the M16/M17 fibre discipline survive partial, noisy and conflicting observations without degrading into nearest-match ranking?

## 1. Set-valued observation

An observation is represented as

\[
O_i=(r_i,V_i),
\]

where `V_i` is a nonempty set of values admitted by the observation.

Its support is

\[
S_i=\bigcup_{v\in V_i}\operatorname{Supp}(r_i,v).
\]

A precise observation is the special case \(|V_i|=1\).

## 2. Explicit conflict budget

For lexical fibre \(F_0\) and integer tolerance \(b\ge0\), define

\[
\boxed{
F^{(b)}(O_1,\ldots,O_n)
=
\{x\in F_0:\#\{i:x\notin S_i\}\le b\}.
}
\]

For \(b=0\), this is the exact conjunctive law from M16/M17:

\[
F^{(0)}=F_0\cap\bigcap_i S_i.
\]

The tolerance is part of the contract. It is not inferred from the data and is not a confidence score.

## 3. Required semantics

M18 requires:

- fixed-\(b\) refinement is monotone under additional observations;
- set-valued observations preserve ambiguity when they do not separate candidates;
- exact inconsistency remains empty when \(b=0\);
- \(b>0\) returns every candidate satisfying the tolerance, not the closest candidate;
- increasing \(b\) may widen the admissible fibre and therefore is not additional evidence;
- final admissibility for a fixed observation multiset is order-independent;
- `NO_LEXICAL_FIBRE` remains distinct from `INCONSISTENT`;
- no probability, score or ranking is introduced.

## 4. Frozen witness

The experiment reuses the 24-object M17 relational world and its DE `Uhr` lexical fibre.

It contains five principal contracts:

- `E0`: exact clean identification, \(b=0\);
- `U0`: set-valued position observation, \(b=0\), deliberately unresolved;
- `A0`: one tolerated conflict across four observations, deliberately two-valued;
- `N0`: noisy five-observation contract, \(b=0\), inconsistent;
- `N1`: the same noisy observations, \(b=1\), singleton identified with tolerance;
- `N2`: the same noisy observations, \(b=2\), wider unresolved fibre.

The noisy witness intentionally contains `DISPLAY=ANALOG` against an otherwise quartz/battery target. The experiment does not silently decide which observation is wrong; only the explicit budget determines admissibility.

## 5. Success predicate

M18 passes iff all deterministic regressions in `scripts/test_m18_uncertain_observation.py` hold while M1–M17 remain green.

## 6. Boundary

M18 uses finite categorical observations and an integer conflict budget. It does not implement probabilities, likelihoods, weighted evidence, continuous measurement error, learned sensor models or Bayesian inference.

It tests whether PSI can represent uncertainty without collapsing candidate-set semantics into ranking.
