# PSI-ACTIVE-MEMORY-COST-ACCOUNTING-01

**Status:** PASS_WITH_BOUNDARY / EXPERIMENTAL / NON-CANONICAL  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30

## 1. Purpose

Correct the interpretation of earlier active-memory scaling results by separating:

1. global workspace selection cost;
2. local event handling;
3. local reverse-index refresh work;
4. processed-event history maintenance;
5. dependency invalidation work.

The experiment measures deterministic logical work in the current reference implementation. It is not a CPU-cycle, cache, memory-bandwidth or asymptotic theorem for a future implementation.

## 2. Why the correction was required

Earlier regressions correctly established that indexed routing can select one relevant workspace while thousands of unrelated workspaces remain untouched:

\[
N_{W}=16385,\qquad N_{\rm examined\ workspaces}=1.
\]

That result concerns **workspace selection** only.

The current implementation performs additional work after selection:

- `_refresh_indices` materializes both `Workspace.nodes` and `Workspace.dependencies`;
- both properties iterate over every edge in the selected workspace;
- `processed_events` is a tuple, so appending accepted event ids recopies the existing tuple.

Therefore the complete current local update path is not proven \(|\Delta|\)-local.

## 3. Explicit counters

`ActiveRuntime.apply()` now reports:

- `examined_events`;
- `mutations`;
- `history_items_copied`;
- `history_items_appended`.

`MultiWorkspaceRuntime.dispatch()` additionally reports:

- `examined_workspaces`;
- `index_refresh_edge_visits`;
- `index_node_membership_updates`;
- `index_dependency_membership_updates`.

The same counters are propagated through `SharedCommitResult` and the durable WAL-backed runtime so later end-to-end experiments can report the whole execution path rather than only candidate selection.

## 4. Edge-size witness

One target workspace is selected and receives one admitted edge delta.

For an initial workspace with `N` edges, after the delta it has `N+1` edges. The current `_refresh_indices` calls two full edge-scanning properties, hence:

\[
C_{\rm refresh}=2(N+1)\ \text{edge visits}.
\]

Regression witnesses:

| initial edges | examined workspaces | index refresh edge visits |
|---:|---:|---:|
| 8 | 1 | 18 |
| 1024 | 1 | 2050 |

Thus:

\[
\boxed{
\text{selective routing across workspaces}\not\Rightarrow
\text{constant local refresh cost}
}
\]

## 5. History-size witness

With graph size fixed, one accepted event is appended to a pre-existing processed-event history.

Current tuple semantics give:

\[
C_{\rm history}=|H_t|
\]

existing event identifiers recopied into the new tuple.

Regression witnesses:

| existing history | copied history items |
|---:|---:|
| 8 | 8 |
| 1024 | 1024 |

This cost is independent of the graph-size witness and must be accounted separately.

## 6. Global-routing witness

With 2049 registered workspaces, one event touching only the target workspace yields:

\[
N_{\rm examined\ workspaces}=1,
\]

while the local refresh for the 8-edge target still reports 18 edge visits.

Therefore the corrected structural result is:

\[
\boxed{
\text{global workspace routing is selective, but the current full local update path contains }O(|E_W|)+O(|H_W|)\text{ components.}
}
\]

No claim is made that these terms are unavoidable. They are properties of the present reference implementation and are candidates for later incremental-index/history optimization.

## 7. Consequence for earlier claims

Earlier statements such as `examined_workspaces=1` remain valid **as routing claims**.

The stronger statement

\[
C_{t\to t+1}=O(|\Delta_t|)
\]

for the whole integrated update path is **not established** by the current implementation.

The legal formulation is:

\[
\boxed{
\text{candidate selection is local in the tested routing index; total local mutation cost is separately measured and presently size-dependent.}
}
\]

## 8. Boundary and next use

F0.4 is a measurement/claim-correction gate, not a performance optimization task. The discovered costs are preserved for F1 so the first full end-to-end reuse experiment reports them honestly.

Potential later repairs include incremental maintenance of workspace node/dependency indices and a non-copying append-only processed-event structure, but those changes require their own semantic-equivalence regressions and are not silently folded into this experiment.
