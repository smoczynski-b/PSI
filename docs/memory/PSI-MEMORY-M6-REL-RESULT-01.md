# PSI-MEMORY-M6-REL-RESULT-01

**Status:** PASS_WITH_BOUNDARY  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Measured result

GitHub Actions run `36621808624` executed M1–M6 successfully.

M6 reconstructed structural relation profiles without using node prose labels or edge notes:

- `II.9`: 14 relational facets;
- `GO-G4`: 4 relational facets;
- `II.11.PSI-BRIDGE`: 9 relational facets.

The same run retained M1, M2, M3, M4a and M5 PASS.

## 2. What the relations recover

For `II.9`, the profile recovers:

- strict dependency on II.7;
- use of C57/C58;
- analogy to II.6;
- explicit non-dependency on II.8;
- outputs C45/C59;
- regression link from the Go memory bank;
- the Myhill–Nerode exemplification;
- negative scope boundaries: no implication of finite memory, computability or efficiency.

For `GO-G4`, the profile recovers its regression-bank membership, SSK contract, falsification of the PSK memory representation and support for the SSK memory representation.

For `II.11.PSI-BRIDGE`, the profile recovers the II.7/II.8 bridge dependencies, II.9 exemplification, C18 evidence role, language contract and exact identification with Nerode equivalence, while keeping the classical theorem aspect separate.

## 3. Architectural conclusion

The experiment supports the decomposition

\[
\boxed{\text{POINT}=\text{thin identity/content anchor}}
\]

\[
\boxed{\text{RELATIONS}=\text{structural description}}
\]

\[
\boxed{\text{PROVENANCE}=\text{license for each relation}}
\]

The important correction is that negative/modal relations are part of description. `DOES_NOT_IMPLY`, `NOT_DEPENDS_ON`, contract requirements and falsification/support edges are not secondary metadata; without them the object profile is materially incomplete.

## 4. Boundary

M6-REL does **not** establish that a theorem can be reduced to its graph neighborhood. The relation profile reconstructs external role, context, dependencies and limits; the internal mathematical proposition/proof remains a content atom referenced by the node.

Thus:

\[
\boxed{\operatorname{Desc}_{struct}(v)\approx\operatorname{Star}(v),\qquad \operatorname{Content}(v)\not\equiv\operatorname{Star}(v).}
\]

## 5. Next target

The next architectural test should attach provenance at the **edge level** and make selected relations fragment-addressable:

\[
\operatorname{Prov}(e)=(\text{path},\text{fragment},\text{hash},\text{version}).
\]

This directly joins the M5 granularity witness with the M6 result that relations themselves carry descriptive content.
