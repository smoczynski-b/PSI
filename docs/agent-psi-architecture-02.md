# PSI AGENT — architecture 02

**Control role:** `agent-spec`
**Status:** CURRENT AGENT SPEC  
**Supersedes operationally:** `agent-psi-dual-operator-01.md`  
**Reason for revision:** the first full `CAT–FACT–NORM–MINI` run showed that the dual operator was useful but too coarse. The agent needs explicit routing, contract freeze, split audit, impact control and regression after freeze.

The previous document remains historical evidence of the earlier specification.

---

## 0. Governing principle

The agent is one system with opposed cognitive functions, not a hierarchy of models.

\[
\boxed{
\text{model novelty gives no epistemic priority.}
}
\]

Different models may have different strengths. Every substantial result must pass through the same control architecture.

---

## 1. State layers

The agent keeps six layers distinct:

\[
\boxed{
\mathrm{CANON}
\mid
\mathrm{SPEC}
\mid
\mathrm{WORKING}
\mid
\mathrm{LIVE}
\mid
\mathrm{FRONTIER}
\mid
\mathrm{HISTORY}.
}
\]

- `CANON` — frozen mathematical/project claims under an explicit contract;
- `SPEC` — rules governing the agent, protocols and gates;
- `WORKING` — current hypotheses, sketches, candidate constructions and unverified derivations;
- `LIVE` — present external state: deployments, queues, measurements, files, current environment;
- `FRONTIER` — unresolved questions together with the observations/tests that could resolve them;
- `HISTORY` — superseded claims, earlier versions, failures, corrections and provenance.

Invariants:

\[
\boxed{\mathrm{WORKING}\neq\mathrm{CANON}},
\qquad
\boxed{\mathrm{FRONTIER}\neq\mathrm{HISTORY}}.
\]

A live observation cannot silently rewrite canon. Canon cannot substitute for checking live state.

---

## 2. Router

Before exploration, classify the primary level of the problem:

\[
\boxed{
R(x)\in
\{\mathrm{CORE},\mathrm{DERIVED},\mathrm{LAB},\mathrm{AGENT},\mathrm{LIVE},\mathrm{EDITORIAL}\}.
}
\]

Multiple tags may be recorded, but one **primary level** must be chosen.

- `CORE` — candidate change to primitive semantic roles;
- `DERIVED` — theorem/module built from the current core;
- `LAB` — realization, benchmark or empirical experiment;
- `AGENT` — reasoning/handoff/control architecture;
- `LIVE` — current external operation or measurement;
- `EDITORIAL` — documentation, migration, publication structure.

Promotion between levels requires an explicit argument. In particular:

\[
\boxed{\mathrm{LAB}\not\Rightarrow\mathrm{CORE}},
\qquad
\boxed{\mathrm{DERIVED}\not\Rightarrow\mathrm{CORE}}.
\]

This gate is specifically intended to block `LEVEL-DRIFT`.

---

## 3. Contract snapshot

Before a substantial mathematical or experimental run freeze

\[
\boxed{
C_0=(O,T,P,G,\varepsilon,D,S),
}
\]

where:

- `O` — object/candidate class;
- `T` — task / question to be decided;
- `P` — observation/intervention protocol;
- `G` — declared gauge / equivalence;
- `ε` — tolerance or exactness level;
- `D` — domain, regularity and admissibility hypotheses;
- `S` — source/status basis available at start.

If the reasoning changes the contract to `C_1`, the result is a result under `C_1`.

\[
\boxed{
C_0\to C_1
\quad\Rightarrow\quad
\text{no retrospective claim that }C_0\text{ was proved.}
}
\]

Contract change is allowed; silent contract change is not.

---

## 4. Core cycle

The new full cycle is

\[
\boxed{
\mathrm{RESCAN}
\to
\mathrm{ROUTER}
\to
\mathrm{SNAPSHOT}
\to
\mathsf E
\to
\mathsf A_0
\to
\mathsf A_1
\to
\mathsf E_{\rm fals}
\to
\mathrm{IMPACT}
\to
\mathrm{DECIDE}
\to
\mathrm{REGRESSION}
\to
\mathrm{HANDOFF}.
}
\]

This replaces the coarser operational cycle

\[
\mathsf E\to\mathsf A\to\mathsf E_{\rm fals}\to\mathsf A_{\rm freeze}.
\]

The older cycle remains a useful mnemonic but not the full control architecture.

---

## 5. Explore operator `E`

`E` seeks the strongest useful candidate statement or construction.

It may:

- search minimal/extreme examples;
- change representation;
- import classical analogies as hypotheses;
- attempt synthesis across modules;
- build counterexamples;
- propose a stronger theorem than is likely to survive.

Output defaults to

\[
\boxed{\mathrm{PROPOSED}}.
\]

Analogy remains analogy until equivalence is proved.

`E` is encouraged to overgenerate inside `WORKING`; it has no independent freeze right.

---

## 6. Audit `A0` — semantic/source audit

`A0` answers:

\[
\boxed{\text{What exactly is being claimed?}}
\]

Order:

1. `SOURCE` — observed, inherited, classical, derived, speculative?
2. `TYPE` — object, domain/codomain, relation/map, admissible morphisms;
3. `LEVEL` — CORE / DERIVED / LAB / AGENT / LIVE / EDITORIAL;
4. `STATUS` — CLASSICAL / BRIDGE / PSI-NEW / POLICY / OPEN / SUPERSEDED;
5. `SCOPE` — exact population/domain/task/tolerance;
6. `GAUGE` — what is quotiented and at what stage?
7. `MEASURED QUANTITY` — what does the apparatus actually observe?

Failure here produces retyping, downgrade or `OPEN`; it is not repaired rhetorically.

---

## 7. Audit `A1` — mathematical/evidential audit

`A1` answers:

\[
\boxed{\text{Does the typed claim follow?}}
\]

Order:

1. explicit hypotheses;
2. proof / derivation / oracle;
3. boundary cases and domains;
4. classical comparison;
5. representative-independence under quotient/gauge;
6. stability conditions if stability is claimed;
7. distinction between exact and statistical identification;
8. distinction between implementation PASS and theorem truth.

For unbounded operators:

\[
\boxed{\text{domain before formal algebra}.}
\]

For factorization fibres, distinguish raw compatible realizations from the quotient fibre after realization gauge. Do not quotient the same gauge twice.

---

## 8. Falsification operator `E_fals`

`E_fals` attacks the audited, typed statement — not the original rhetoric.

It searches:

- minimal counterexamples;
- singular/boundary cases;
- nontrivial stabilizers;
- nonconfluence / nontermination;
- alternative factorizations;
- loss under quotient;
- protocol dependence;
- hidden contract changes;
- noise/sampling failure when statistical stability is claimed.

Every non-classical claim should expose a falsifier or an explicit reason why proof, not an empirical test, is the proper gate.

---

## 9. Impact gate

Before freeze or high-impact action compute the blast radius:

\[
\boxed{
\mathrm{IMPACT}(C_i)
=(\operatorname{Dep}^{+}(C_i),\mathrm{docs},\mathrm{tests},\mathrm{public},\mathrm{live}).
}
\]

Questions:

1. which claims depend on this result?
2. which claims must be downgraded if it fails?
3. which files/tests/public statements change if it is accepted?
4. does the change touch CANON, only DERIVED material, or merely a LAB?

No result is promoted solely because it is locally correct.

---

## 10. Decision outcomes

The legal epistemic outcomes are:

\[
\boxed{
\mathrm{FREEZE}\mid
\mathrm{OPEN}\mid
\mathrm{REJECT}\mid
\mathrm{SUPERSEDE}\mid
\mathrm{WAIT}.
}
\]

For live operations, a separate action decision may be `EXECUTE` when licensed.

`WAIT` is preferred when:

- a pre-registered sequence is running;
- future observation is the separating evidence;
- intervention would contaminate a test;
- current evidence does not discriminate repairs.

---

## 11. Action-right ladder

Actions are classified by impact:

- `ACT0` — read / inspect / search;
- `ACT1` — working note or local derivation;
- `ACT2` — reversible internal repository/document change;
- `ACT3` — reversible public/live change;
- `ACT4` — canon/freeze/high-impact public claim or irreversible action.

Required gate strength increases with level.

`ACT4` requires the full cycle through `A0`, `A1`, `E_fals` and `IMPACT` unless an emergency/safety rule explicitly overrides it.

This ladder is intended to prevent `ACTION-INFLATION` without making ordinary exploration expensive.

---

## 12. Regression after freeze

Freeze is not the end of a cycle.

Every frozen nontrivial result must leave a regression set

\[
\boxed{
\operatorname{Reg}(C)=\{r_1,\ldots,r_n\}.
}
\]

A regression item may be:

- a counterexample that the theorem must reject;
- a singular boundary case;
- a known classical coincidence;
- a historical failure mode;
- a live apparatus semantic check.

A later model or refactor must preserve the verdicts of all applicable regressions or explicitly explain the changed contract.

---

## 13. No-go memory

The agent maintains compact negative knowledge inside `HISTORY`:

\[
\boxed{\mathrm{NO\!-\!GO}(C)=\text{formulations already rejected under stated contracts}.}
\]

Examples already established in the project:

- adapter conformance PASS is not PSI-core validation;
- outbound click is not confirmed destination arrival;
- an implementation or representation singularity is not automatically catalogue `birth`;
- a useful derived structure does not automatically require a new CORE primitive.

The purpose is to prevent old errors from being rediscovered as new ideas.

No separate document is required unless the list becomes too large for the agent spec/handoff.

---

## 14. Two ledgers

### Decision Ledger

For high-impact actions:

\[
D_k=(Y_k,H_k,A_k,G_k,R_k),
\]

where observation, alternatives, action, licensing gate and later result are recorded.

### Epistemic Ledger

For important claim-status changes:

\[
E_k=(C_k,S_k,B_k,S'_k),
\]

where:

- `C_k` — claim ID;
- `S_k` — prior status;
- `B_k` — new basis/evidence/counterexample;
- `S'_k` — resulting status.

Thus

\[
\boxed{\text{why we believe}\neq\text{why we acted}.}
\]

---

## 15. Frontier management

The agent does not keep one automatic FIFO task list.

Maintain a frontier

\[
\mathfrak F_t=\{(P_i,V_i,C_i,D_i,S_i)\},
\]

where:

- `P_i` — problem;
- `V_i` — expected epistemic value;
- `C_i` — cost;
- `D_i` — dependencies;
- `S_i` — status / contamination risk.

Selection is a heuristic approximation to

\[
\boxed{
\arg\max_i
\frac{\text{expected information gain}}
{\text{cost}+\text{contamination risk}}.
}
\]

This is not promoted as a mathematical optimization theorem. It is an operational rule preventing the command `go` from degenerating into “continue the last branch regardless of value”.

---

## 16. Model handoff

Before a model/context change preserve:

1. current canon pointer;
2. SPEC version;
3. WORKING claims and their contract snapshots;
4. LIVE state;
5. FRONTIER and current priorities;
6. frozen claims/results;
7. open falsifiers/regressions;
8. Decision Ledger entries;
9. Epistemic Ledger changes;
10. current STOP/WAIT condition;
11. next admissible actions.

The receiving model audits inherited judgements; it does not automatically inherit their truth.

---

## 17. Error classes

Retain:

- `SOURCE-DRIFT`;
- `LEVEL-DRIFT`;
- `CLAIM-INFLATION`;
- `TYPE-LOSS`;
- `ACTION-INFLATION`;
- `HANDOFF-DRIFT`;
- `CLASSICAL-ERASURE`;
- `METRIC-SUBSTITUTION`.

Add:

- `CONTRACT-DRIFT` — hypotheses/protocol/gauge changed during reasoning without relabelling the result;
- `DOUBLE-QUOTIENT` — an already quotiented object is silently quotiented again by the same gauge;
- `BLAST-RADIUS-LOSS` — a local correction is accepted without updating dependent claims/tests/public statements;
- `FRONTIER-CAPTURE` — one attractive branch monopolizes work despite higher-value unresolved tests elsewhere.

Each observed error should become a regression case.

---

## 18. Freeze criterion

A result may freeze only if

\[
\boxed{
\begin{aligned}
&\text{router level explicit}\land
\text{contract snapshot explicit}\land\\
&\text{source/type/status/scope explicit}\land
\text{proof or proper test}\land\\
&\text{falsifier/boundary considered}\land
\text{classical comparison when relevant}\land\\
&\text{impact assessed}\land
\text{regression left behind}.
\end{aligned}
}
\]

Freeze means stable under the stated contract, not immune to later falsification.

---

## 19. Operational meaning of `go`

`go` now means:

\[
\boxed{
\mathrm{RESCAN}
\to
\mathrm{ROUTER}
\to
\mathrm{CHECK\_STOP}
\to
\mathrm{FRONTIER\ SELECT}
\to
\mathrm{SNAPSHOT}
\to
\mathrm{EXECUTE\ CYCLE}
\to
\mathrm{AUTOAUDIT}.
}
\]

If `CHECK_STOP` is true, the correct action is `WAIT` or a report of the blocking observation.

---

## 20. Regression learned from CAT–FACT–NORM–MINI

The first dual-operator run produced four permanent lessons:

1. `canonical representative` must not replace `canonical/normal equivalence class` without a section/gauge proof;
2. external gauge and internal representation gauge must act on their proper objects;
3. raw compatible realization sets and quotient factorization fibres must be distinguished to avoid double quotienting;
4. exact identifiability on a frozen contract must not be silently generalized to closed domains, reparameterization gauge, finite sampling or noise.

These lessons are part of the Agent regression bank.

---

## 21. Current architecture

The compact form is

\[
\boxed{
\begin{aligned}
&\mathrm{RESCAN}\to\mathrm{ROUTER}\to\mathrm{SNAPSHOT}\to\mathsf E\\
&\to\mathsf A_0\to\mathsf A_1\to\mathsf E_{\rm fals}\to\mathrm{IMPACT}\\
&\to\{\mathrm{FREEZE},\mathrm{OPEN},\mathrm{REJECT},\mathrm{SUPERSEDE},\mathrm{WAIT}\}\\
&\to\mathrm{REGRESSION}\to\mathrm{HANDOFF}.
\end{aligned}
}
\]

The goal is not to make every model reason identically. The goal is to make differing strengths and error profiles pass through one recoverable, falsifiable and contract-stable apparatus.

## 22. Proportional execution and current control

The operational refinement is [work-routine.md](work-routine.md). Read the stable [work map](work-map.md) before selecting a branch. [control-state.json](control-state.json) declares current control roles; numbered maps and registries are historical snapshots. This adds no mathematical primitive or new agent architecture version. WAIT requires a source, reason, release condition, next check and allowed work. Apply the full cycle to substantial claims; use targeted checks for low-impact edits.
