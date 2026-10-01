# PSI-MEMORY-M5-RESULT-01

**Status:** PASS / GRANULARITY WITNESS FOUND  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-29

## 1. Result

GitHub Actions run `36620619085` executed M1-M5 successfully.

Automatic traversal from `GO-G4` at radius 3 reproduced the seven-node M3 view and generated five source files without hand-selecting the task pack.

Measured automatic pack:

- view nodes: `7`;
- source files: `5`;
- broad baseline: `201696` bytes;
- generated source files: `82325` bytes;
- generated manifest: `342` bytes;
- generated total / broad baseline: `0.4099`;
- reduction: `59.01%`.

Therefore M5 passes the frozen 50% engineering gate.

## 2. Comparison with M4a

M4a hand-guided pack:

\[
39560\text{ bytes}
\]

M5 automatically generated source pack plus manifest:

\[
82667\text{ bytes}.
\]

The automatic graph traversal is therefore source-complete and still substantially smaller than the broad baseline, but materially larger than the hand-guided pack.

## 3. Granularity witness

The cause is explicit:

```text
C57 -> docs/claim-registry.md
C58 -> docs/claim-registry.md
```

The two small semantic atoms share a coarse file-level source pointer. Automatic source resolution therefore loads the whole stable claim registry.

This yields the architectural witness:

\[
\boxed{\text{correct graph granularity} + \text{coarse source addressing} \Rightarrow \text{avoidable context inflation}.}
\]

The next problem is not a graph-database problem. It is a source-address problem.

## 4. Next construction target

Introduce fragment-addressable provenance while keeping the file as the durable source object, for example:

\[
\operatorname{SourceRef}(v)
=(\text{path},\text{anchor/range},\text{content hash},\text{version}).
\]

Then repeat M5 with `C57` and `C58` resolving only their certified fragments. The test should compare:

\[
B_{fragment-generated}
\quad\text{against}\quad
B_{file-generated}=82667.
\]

The durable storage remains ordinary Git/text; only the semantic address becomes finer.

## 5. Scope

M5 does not establish globally minimal context and does not execute an LLM. It establishes that the graph can autonomously generate a bounded source pack and identifies file-level source addressing as the next measurable inefficiency.