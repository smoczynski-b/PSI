# ARCH-LANG-CERT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30

## Purpose

This is a provenance-hardening unit requested after `AUDIT-ROZMOWY-04.md`. It does not open M20 and does not change PSI core, theorem validity, or ordinary memory retrieval.

The target is narrow: bind selected historical language/representation claims to exact substrings of the two raw MHTML archives whose whole-file SHA-256 values were already recorded.

## Certificate contract

Each record in `arch-lang-fragment-cert-01.tsv` contains:

- historical archive node;
- SHA-256 of the complete MHTML source;
- selector type `exact_utf8_html_substring`;
- exact UTF-8 substring;
- SHA-256 and byte length of that substring;
- expected occurrence count.

Two verification levels are deliberately separated:

1. `CERT_REGISTRY_PASS` — repository-only check. It verifies certificate structure, selector hashes and binding of each source hash to `arch-lang-source-recovery-01.tsv`. It **does not claim the raw archive was read**.
2. `SOURCE_REVALIDATION_PASS` — requires the raw `.mhtml` files through `--source-dir`. The verifier hashes the whole sources, decodes MIME `text/html` payloads as UTF-8 and checks exact occurrence counts.

This distinction implements the Conversation-04 rule that a stored label is not current source verification.

## Frozen evidence

### 2026-04-27/28 — language invariance

Source SHA-256:

`0e69aa1b4b0004edb7a2a40f0d9703e15da5eca38eaa2f8e03e4026c2efebee5`

Certified exact substrings:

- `EV-ARCH-0427-INVARIANT` — `inwariant semantyczny przy zmianie reprezentacji`
- `EV-ARCH-0427-LANGUAGE-LOCAL` — `język = reprezentacja lokalna`

These fragments certify that the phrases occur in the identified raw archive. They do not certify the later M15/M16 formalism and do not by themselves prove the interpretive genealogy edge `PRECURSOR_OF`.

### 2026-05-20/21 — local/global semantic atlas

Source SHA-256:

`b93e3a406b6dccd9884d6036121c149e5f928feeed1f34a1156dd9190a467493`

Certified exact substrings:

- `EV-ARCH-0520-LOCAL-GLOBAL` — `tekst lokalnie znaczy, ale globalnie nie posiada jednej reprezentacji znaczenia.`
- `EV-ARCH-0520-ATLAS` — `lokalnie reprezentowalny atlas sensu bez globalnej trywializacji`

Again, this certifies archived wording, not the truth of the old mathematical metaphor or the later M17 interpretation.

## Current execution

The raw files supplied in the current sandbox were re-hashed and all four selectors occurred exactly once. Therefore this work unit obtained:

`ARCH-LANG-CERT-01 SOURCE_REVALIDATION_PASS`

for these two sources.

The repository CI can reproduce only `CERT_REGISTRY_PASS` because the private/raw ZIP is intentionally not committed.

## Non-upgrades

The following remain weaker and are **not** promoted by this unit:

- `ARCH-2025-11-25-DENOTATION-LAYERS` — `CONVERSATION_RECOVERED`;
- `ARCH-2026-06-01-OBJECT-RELATIONAL-IDENTITY` — `CONVERSATION_RECOVERED`;
- `ARCH-2026-09-06-PSI-LANG` — `CONVERSATION_RECOVERED`;
- `ARCH-2026-07-12-EDGE-TRANSPORT` — `LIBRARY_RECOVERED`;
- `ARCH-2026-05-16-REPRESENTATION-LINEARIZATION` — raw archive recovered, fragment selector not frozen here.

No raw-export bytes means no M7/M8-style fragment certificate by assertion alone.

## Boundary

`RAW_FRAGMENT_CERTIFIED` means: whole-source identity plus exact archived substring has been revalidated against the raw source. It does **not** establish speaker attribution beyond what the source itself encodes, historical priority, mathematical truth, or the correctness of a genealogy relation.

The active genealogy remains interpretive and separate from proof dependency.
