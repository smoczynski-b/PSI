# PSI-MEMORY-M8-RESULT-01

**Status:** PASS  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36625024317` executed M1–M8 successfully.

For anchor `GO-G4` and certified radius `3`, the end-to-end builder produced:

- nodes: `11`;
- certified edges: `11`;
- unique evidence fragments: `6`;
- unique evidence bytes: `2111`;
- complete serialized context artifact: `6414` bytes.

The frozen M4 broad baseline is `201696` bytes. Therefore:

\[
\frac{6414}{201696}=0.0318,
\]

and the complete M8 context is smaller by

\[
\boxed{96.82\%}.
\]

## 2. End-to-end path

M8 now materializes the full retrieval chain:

\[
\boxed{
\text{task anchor}
\to
\text{certified relation traversal}
\to
\text{VALID edge set}
\to
\text{deduplicated evidence fragments}
\to
\text{agent context artifact}.
}
\]

The distant M3 bridge is no longer an uncertified navigation convenience. Its Go→II.7 and Go→II.9 meanings are independently fragment-certified.

## 3. Local degradation test

The regression changes the state of `EV-GO-II9` in simulation.

For `STALE`:

- `E-GOREG-II9` is excluded;
- `II.9` is unreachable and is absent from the context;
- all II.9-only descendants disappear;
- the independently certified Go→II.7 path remains.

For `SOURCE_DRIFT`, strict M8 retrieval also excludes the edge pending recheck, but does not classify II.9 as false.

Thus the retrieval layer degrades locally rather than forcing a global memory reset.

## 4. Architectural conclusion

M8 combines the prior results:

- M3: sparse distant bridge increases reach;
- M5: graph traversal can generate a task pack automatically;
- M6: typed relations carry structural description;
- M7: relations can carry fragment-addressable provenance and validity;
- M8: the pieces compose into a bounded executable retrieval path.

The current experimental memory object is therefore usefully represented as

\[
\mathcal M=(V,E,P,S),
\]

with task retrieval operator

\[
\mathfrak R_{a,r}^{VALID}(\mathcal M)
\]

that starts at anchor `a`, traverses certified `VALID` relations to radius `r`, deduplicates evidence objects, and serializes only the resulting local context.

## 5. Boundary

M8 is an engineering result about structural retrieval and context size. It does not establish:

- equal or better LLM answer quality;
- actual token reduction inside a model;
- optimality/minimality of the selected subgraph;
- universal applicability outside the current PSI memory sample.

Those require M4b or later independent model runs.

## 6. Next architectural question

The next useful test is no longer another local compression ratio. It is whether the same retrieval operator remains stable when the memory graph grows materially and when two agents add competing/candidate relations. That requires introducing write-side deltas and epistemic admission (`CANDIDATE -> VERIFIED`) rather than only read-side retrieval.
