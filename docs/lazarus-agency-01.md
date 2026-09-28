# PSI — LAZARUS-AGENCY-01

**Status:** DERIVED / LAB / CORE-PRESSURE RESULT  
**Agent architecture:** `AGENT-PSI-ARCHITECTURE-02`  
**Canonical target:** `PSI-R3-CONSOLIDATED-CANON-03`  
**Historical basis:** POST-RUN3 / D2 / ERRATA-D2-01 / D3 / PSI-RED-1

This note re-runs the historical Lazarus agency witness against the current CORE5 architecture. It does not reconstruct RUN3 and does not introduce a new primitive unless the existing roles fail.

---

## 1. ROUTER

Primary level:

\[
\boxed{\mathrm{DERIVED}/\mathrm{LAB}}
\]

Secondary tag:

\[
\boxed{\mathrm{CORE\!-\!PRESSURE}}.
\]

The question is not whether execution/agency is operationally useful. It is whether the distinction requires a semantic role beyond

\[
(\Omega,\Psi,\mathcal K,\mathscr O_{\mathcal T},\delta)
\]

under an explicit contract.

---

## 2. CONTRACT SNAPSHOT

Freeze the exact task-relative contract

\[
C_A=(O,T,P,G,\varepsilon,D,S)
\]

as follows.

### Object

Histories and current operational state, minimally of the form

\[
H_t=(\varepsilon_0,y_1,\ldots,\varepsilon_{t-1},y_t)
\]

or an equivalent recoverable experiment/observation transcript, together with the active operational composition

\[
\Gamma_t\in\operatorname{Comp}(\mathcal R_t).
\]

The physical candidate quotient remains

\[
X_t=Q_t/G_t.
\]

### Task

Determine task-relevant legal/executable actions and their future consequences under the frozen mission/task contract.

### Protocol

Only executed experiments and observations that are recoverable from the transcript constrain the historical fibre.

### Gauge

The existing realization gauge `G_t`; no additional “agency gauge” is introduced.

### Tolerance

Exact (`ε=0`) for the logical witness.

### Domain

Finite-horizon relational/deterministic transition semantics sufficient to define future task behaviour and executable action sets.

### Source basis

Historical D2/D3 and the later PSI reduction audit are treated as inherited claims to be re-audited, not automatically accepted.

---

## 3. A0 — semantic/type audit

The current-state compatibility fibre

\[
F_t(H)\subseteq X_t
\]

and the task-relevant information state are not the same type.

Define

\[
\rho_F:\mathcal H_t\to\mathcal P(X_t),
\qquad
\rho_F(H)=F_t(H).
\]

A task equivalence on histories may be written schematically as

\[
H\equiv_{\mathcal T,t}H'
\iff
\operatorname{Beh}_{\mathcal T}(H)
\cong
\operatorname{Beh}_{\mathcal T}(H'),
\]

where `Beh_T` includes exactly the future distinctions required by the task: legal/executable actions, reachable task outcomes, costs or other declared task observables.

Hence the correct distinction is

\[
\boxed{
F_t(H)=F_t(H')
\not\Rightarrow
H\equiv_{\mathcal T,t}H'.
}
\]

The slogan

\[
\text{“same information, different agency”}
\]

is therefore too strong unless “information” is explicitly restricted to the current world-state fibre. The precise claim is:

\[
\boxed{
\text{same current-state uncertainty}
\not\Rightarrow
\text{same task agency}.}
\]

If two cases are equal in the full task quotient `M_T,t`, task-relevant agency cannot differ by definition of that quotient.

---

## 4. Operational composition is typed, not mystical

Historical POST-RUN3 introduced

\[
\Gamma_t\in\operatorname{Comp}(\mathcal R_t)
\]

as the active composition of operational regimes.

Executability is a predicate such as

\[
Exec_t(r;\mathcal T,\Gamma_t,\mathcal P_t)\in\{0,1\}.
\]

Thus two histories can have the same compatible physical-state fibre and still induce different action sets when their operational compositions differ:

\[
F_t(H)=F_t(H'),
\qquad
\mathcal A_t^{dop}(H,\Gamma)
\neq
\mathcal A_t^{dop}(H',\Gamma').
\]

This does not show that `agency` is a new ontological coordinate. It shows that `ρ_F` forgot variables needed by the decision task.

---

## 5. A1 — representation theorem for the D2 witness

### Proposition — D2 representation inadequacy

Let

\[
\rho_F(H)=F_t(H).
\]

If there exist histories `H,H'` such that

\[
F_t(H)=F_t(H')
\]

but

\[
\operatorname{Beh}_{\mathcal T}(H)
\not\cong
\operatorname{Beh}_{\mathcal T}(H'),
\]

then

\[
\boxed{
\ker_{eq}\rho_F
\not\subseteq
\equiv_{\mathcal T,t}.
}
\]

Therefore the current-state fibre alone is not a task-sufficient representation.

### Proof

The hypotheses give a pair `(H,H')` lying in `ker_eq ρ_F` but not in `≡_{T,t}`. Hence the kernel inclusion required for exact task factorization fails. ∎

This is an immediate application of the classical/PSI factorization criterion already present in CORE5.

---

## 6. Repair without a new primitive

There are at least two legal repairs inside the existing architecture.

### Repair A — richer candidate/state object

Use a candidate carrying the task-relevant operational information, for example

\[
\widetilde\Omega_t
\subseteq
\mathcal H_t\times\operatorname{Comp}(\mathcal R_t)
\]

or another equivalent typed state from which the same task observables can be recovered.

Then legal/executable action structure is represented by observables/functions on that candidate.

### Repair B — task quotient on histories

Keep the full history space and define

\[
M_{\mathcal T,t}
=
\mathcal H_t/\equiv_{\mathcal T,t}.
\]

A representation

\[
\rho:\mathcal H_t\to Z
\]

is task-sufficient exactly when

\[
\boxed{
\ker_{eq}\rho
\subseteq
\equiv_{\mathcal T,t}.
}
\]

This is the same adequacy criterion already used elsewhere in PSI.

---

## 7. D3 — correlation warning

D3 strengthens the lesson.

After an experiment, world state and operational composition may be jointly uncertain:

\[
(x_{t+1},\Gamma_{t+1}).
\]

Separate marginals

\[
F^X_{t+1},
\qquad
F^\Gamma_{t+1}
\]

need not determine the joint admissible set

\[
J_{t+1}\subseteq X_{t+1}\times\operatorname{Comp}(\mathcal R_{t+1}).
\]

Two histories can therefore have the same marginals but different correlations and different future task trees.

Again this is a representation defect:

\[
\boxed{
\text{marginals} \neq \text{joint task-relevant state}.}
\]

CORE5 already permits the candidate space to be the joint object, and `δ`/the transition relation can propagate the joint pair. No sixth semantic role is forced.

---

## 8. CORE5 reduction table

| Proposed agency datum | Existing role | Reduction |
|---|---|---|
| history `H_t` | candidate / protocol-relative state | choose `Ω_c` as histories or an equivalent sufficient state |
| active composition `Γ_t` | candidate component / contract state | include in `Ω_c` or in a recoverable operational state used by task observables |
| executable action set | task observable | `R_A(ω)=A_t^{dop}(ω)` |
| execution predicate | task observable / compatibility predicate | `Exec_t(r;T,Γ,P)` |
| future action/outcome tree | task closure under dynamics | generated through `δ_c` / admitted transports |
| experiment update of world + agency | dynamics | joint transition on `(x,Γ)` |
| same world fibre, different agency | representation inadequacy | `ker ρ_F \not\subseteq E_T` |
| task-minimal information state | task quotient | `M_T=Ω/E_T` or history quotient equivalent |

No row requires a new semantic role after the candidate/contract is typed correctly.

---

## 9. E_fals — attacks

### Attack 1 — same full task information, different agency

If one could exhibit

\[
H\equiv_{\mathcal T,t}H'
\]

while a task-relevant executable-action observable differs, then the chosen definition of `≡_T` would be internally inconsistent. This would attack the task closure/specification, not prove a new primitive.

### Attack 2 — candidate enrichment fails

To trigger R4 one would need a typed witness showing that no candidate enrichment or contract-relative state can carry the agency datum without destroying another required distinction.

No such witness is present in D2/D3.

### Attack 3 — joint uncertainty cannot be propagated

D3 would pressure the dynamics role only if a joint `(x,Γ)` transition could not be represented as an admissible relation/kernel on the chosen candidate. The historical formalism explicitly provides such a joint transition relation.

### Attack 4 — Γ is irreducibly external to every candidate

This would require a proof that `Γ` is neither candidate data, nor protocol/contract state, nor a derived task observable input. The historical typing shows the opposite.

All four attacks fail to produce an R4 witness.

---

## 10. IMPACT / R4 verdict

The historical slogan is corrected, but the mathematical lesson survives.

Old loose formulation:

\[
\text{same information}\not\Rightarrow\text{same agency}.
\]

Current precise formulation:

\[
\boxed{
F_t(H)=F_t(H')
\not\Rightarrow
H\equiv_{\mathcal T,t}H'.
}
\]

Therefore

\[
\boxed{
\mathrm{LAZARUS\!-\!AGENCY\!-\!01}:
\mathrm{CORE5\ SURVIVES}.}
\]

The witness is a permanent regression against identifying the current physical-state fibre with the full task information state.

---

## 11. WHAT THIS RESULT DOES NOT TEST

This result does **not** establish:

- an ontology or philosophy of free will / agency;
- that every decision problem requires an explicit `Γ_t` coordinate;
- that histories are always the computationally minimal representation;
- statistical stability under uncertain/noisy execution models;
- universal optimal-control or POMDP results;
- that `F_t` is never sufficient — it can be sufficient under a task/contract for which `ker ρ_F ⊆ ≡_T`.

---

## 12. Regression set

Permanent regressions:

1. **WORLD-FIBRE ≠ TASK-STATE** — do not identify `F_t` with `M_T,t` by definition.
2. **MARGINALS ≠ JOINT** — state and agency marginals can lose their correlation.
3. **Γ typing** — `Γ_t` is an operational composition, not a resource or generic scalar.
4. **Exec typing** — action/régime executability must include the relevant task/protocol/operational state unless already encoded in the candidate.
5. **D* ≠ π** — oracle decision on a known hidden state is not the same map as an information policy.
6. **SLOGAN correction** — say “same current-state fibre” rather than “same information” unless full task information is genuinely equal.

---

## 13. Decision

\[
\boxed{
\mathrm{FREEZE\ as\ DERIVED\ PRESSURE\ RESULT};
\quad
R4=NO.
}
\]

The next unresolved independent CORE5 pressure branch is `HIGHER-FIBRE`.