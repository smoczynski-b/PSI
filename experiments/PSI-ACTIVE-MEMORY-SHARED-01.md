# PSI-ACTIVE-MEMORY-SHARED-01

Status: EXPERIMENT / NON-CANONICAL

## Goal

Integrate the already tested active-memory layers without changing PSI CORE5:

1. one authoritative MVCC memory;
2. multiple task-local active workspaces;
3. selective event routing after commit;
4. downstream invalidation only through declared workspace dependencies;
5. no global workspace scan after a local accepted delta.

The experiment tests the execution architecture, not consciousness and not a new PSI primitive.

## Architecture

\[
A_i\to P_i\to \mathcal M_t^{\rm MVCC}\to \Delta_t\to \{W_j\}_{\rm delivered}\to \{W_k\}_{\rm NEEDS\_RECHECK}.
\]

The admission boundary remains the authoritative MVCC commit. Rejected or no-op proposals do not enter local workspaces.

For local routing, `MultiWorkspaceRuntime` uses indexed active-node membership. A workspace that actually changes emits a dependency token

\[
\texttt{workspace:<id>}
\]

which selectively invalidates downstream workspaces that explicitly declared that dependency.

## Frozen witnesses

### W1 — atomic two-agent commit

Two proposals against the same authoritative revision modify disjoint semantic slots. The global transaction commits once and produces one new authoritative revision.

Expected:

- proof event delivered only to `proof`;
- chemistry event delivered only to `chem`;
- `downstream` receives no semantic event;
- `downstream`, which declares `workspace:proof`, becomes `NEEDS_RECHECK`;
- unrelated local state remains unchanged.

### W2 — FORUM observation boundary

`FORUM_OBJECT_SEEN` is not transaction-admissible. It must be rejected before local routing and invalidation.

### W3 — indexed scaling witness

Register 4096 unrelated workspaces plus one relevant direct workspace and one downstream dependent workspace. A single local committed event must examine:

- one MVCC version slot;
- one routed workspace;
- one dependency link.

This is operational accounting, not an asymptotic timing proof.

## Pass condition

`PASS_WITH_BOUNDARY` requires:

- authoritative MVCC commit succeeds for legal proposals;
- only committed proposals are routed;
- direct workspaces receive only relevant deltas;
- downstream invalidation follows declared workspace dependencies;
- unrelated workspaces remain semantically unchanged;
- rejected FORUM observations produce zero local delivery/invalidation;
- scaling witness remains `1/1/1` for version checks / routed workspaces / dependency links.

## Boundary

This is a deterministic, crash-free, single-process reference integration. The authoritative commit happens before local propagation. There is not yet a durable WAL or two-phase recovery guaranteeing recovery from a process crash between those phases. There are no real threads/processes, distributed clocks, consensus, live FORUM writes, or GPU execution.
