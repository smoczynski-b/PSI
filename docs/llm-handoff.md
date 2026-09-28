# PSI — model-to-model handoff discipline

Status: WORKING RULE / PUBLIC INTEROPERABILITY LAYER

This note defines how important PSI material should be written when it may be copied directly from one language model to another.

The aim is not to invent a special machine dialect. The aim is to make the text self-sufficient, status-explicit and resistant to inferential drift.

## 1. Principle

A portable PSI note should be readable by both a human and another model without requiring reconstruction of the missing conversation.

\[
\boxed{
\text{portable text}
=
\text{human-readable}
+
\text{model-readable}
}
\]

A transferred conclusion must not silently become a transferred fact.

## 2. Required status separation

When relevant, distinguish explicitly:

- **CONTEXT** — the object, task and scope;
- **KNOWN** — facts already established in the cited or supplied source;
- **CLAIM** — the proposition currently asserted;
- **EVIDENCE** — the argument, calculation, source or observation supporting the claim;
- **INFERENCE** — a conclusion derived from the known material;
- **HYPOTHESIS** — a live conjecture not yet established;
- **UNCERTAINTY** — what remains unresolved or underdetermined;
- **NEXT** — the next admissible action or test.

The labels are semantic statuses, not decorative headings. Omit labels that are genuinely unnecessary, but never merge statuses that matter to the validity of the conclusion.

## 3. Mathematical handoff

For mathematical material, prefer the order

\[
\boxed{
\text{definition}
\to
\text{domain/type}
\to
\text{assumptions}
\to
\text{statement}
\to
\text{proof/status}
}
\]

A symbol must not acquire a stronger meaning merely because another model recognizes a familiar analogue.

For example, if an operator is not yet defined, write:

- **KNOWN:** the symbol occurs in the current specification;
- **UNRESOLVED:** its domain, closure rule or existence theorem is not yet specified;
- **HYPOTHESIS:** a classical construction may provide an analogue;
- **NEXT:** define the PSI object first, then prove or refute equivalence with the classical construction.

Do not replace this sequence with an identification by resemblance.

## 4. Source discipline

If the handoff is based on a document, repository file, experiment or external source:

1. preserve the source terminology and status;
2. distinguish source content from added analysis;
3. state explicitly when a point is absent from the source;
4. do not fill a gap silently with general knowledge;
5. preserve version, branch, contract or experiment identity when it matters.

## 5. Handoff invariant

The receiving model should be able to answer the following without access to the original conversation:

- What object is under discussion?
- What is already established?
- What is merely inferred?
- What remains uncertain?
- Which assumptions are active?
- What would falsify or weaken the claim?
- What is the next admissible step?

If these questions cannot be answered from the transferred text, the handoff is incomplete.

## 6. Relation to PSI method

This rule extends the existing PSI discipline:

\[
\text{observation}
\neq
\text{reconstruction}
\]

into model-to-model communication:

\[
\boxed{
\text{received statement}
\neq
\text{verified statement}
}
\]

The receiving model must preserve the epistemic status carried by the sender unless it performs an explicit new verification.

## 7. Language layer

The internal theoretical language of PSI is Polish; the public interoperability and software layer is English.

\[
\mathcal L_{\mathrm{PSI}}
=
\mathcal L_{\mathrm{theory}}^{PL}
\oplus
\mathcal L_{\mathrm{interop}}^{EN}.
\]

The two layers express the same formal content but need not be literal translations. English identifiers used by protocols, code and machine interfaces remain unchanged inside Polish prose when they function as identifiers.

## 8. Default rule

Important PSI material intended for reuse, audit, delegation or transfer between models should be written so that it can be pasted into another competent model without an interpreter and without changing the epistemic status of any statement.

\[
\boxed{
\text{CONTEXT}
\to
\text{KNOWN}
\to
\text{CLAIM}
\to
\text{EVIDENCE}
\to
\text{UNCERTAINTY}
\to
\text{NEXT}
}
\]
