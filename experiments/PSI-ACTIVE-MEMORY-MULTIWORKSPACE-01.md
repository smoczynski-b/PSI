# PSI-ACTIVE-MEMORY-MULTIWORKSPACE-01

Status: EXPERIMENTAL / NON-CANONICAL  
Branch: `psi-memory-map-01`

## Object

Selective event routing and dependency invalidation across multiple simultaneously active workspaces backed by one shared memory environment.

This is an execution-layer experiment. It does not add a PSI primitive, does not create M20, does not change CORE5, and does not mutate the live PSI-FORUM gateway.

## Contract

Let active workspaces be

`W_1, ..., W_n`.

Each workspace has:

- an already compiled task contract;
- an active node set `V_i*`;
- declared dependency tokens `Dep(W_i)`;
- an `ActiveRuntime` maintaining stable local tensor indices and sparse delta patches.

The coordinator maintains two reverse indices:

`I_V(v) = { i : v in V_i* }`

for event delivery, and

`I_D(d) = { i : d in Dep(W_i) }`

for epistemic invalidation.

These operations are distinct.

### Event delivery

For an admitted edge event `u -r-> v`, only workspaces in

`I_V(u) union I_V(v)`

are offered the event. Each local `ActiveRuntime` still decides whether the event mutates its state.

An observed but non-admitted FORUM object (`FORUM_OBJECT_SEEN`) is delivered to no semantic workspace.

### Invalidation

A changed dependency token `d` marks only members of `I_D(d)` as `NEEDS_RECHECK`. A stale workspace emits the token

`workspace:<workspace_id>`

so another workspace that explicitly depends on that workspace can be invalidated transitively.

`NEEDS_RECHECK` means only that a declared dependency changed. It does not mean false.

## Frozen witness

Three workspaces are used:

- `proof`: contains node `A`;
- `chemistry`: disjoint from `A`;
- `downstream`: semantically disjoint from `A` but explicitly depends on `workspace:proof`.

An admitted FORUM relation

`A SUPPORTS P2`

must be routed only to `proof`.

Then changing the dependency token

`source:forum:OID-MW`

must invalidate exactly:

`proof -> downstream`

while `chemistry` remains `VALID` and bitwise/semantically unchanged.

A seen-but-not-admitted FORUM relation must mutate no workspace.

## Scaling witness

The experiment adds 128, 1024, 4096, and 16384 unrelated workspaces while keeping one target workspace fixed.

For a local admitted event touching only the target, the indexed **candidate-selection** requirement is:

`candidate_workspaces = examined_workspaces = 1`

independent of the number of unrelated workspaces.

Wall-clock timings are reported only as observations and are not CI proof obligations.

### F0.4 interpretation correction

`examined_workspaces=1` measures only routing across workspaces. It does **not** imply that the full mutation cost is constant or `O(|delta|)`.

`PSI-ACTIVE-MEMORY-COST-ACCOUNTING-01` later established that the present `_refresh_indices` scans every edge of the selected workspace twice (through `nodes` and `dependencies`) and that tuple-backed processed-event history append recopies the existing history.

Thus the preserved result is:

\[
\boxed{\text{workspace selection is selective across unrelated workspaces}}
\]

not:

\[
\boxed{\text{the entire selected-workspace update has constant cost}.}
\]

## Success / STOP

PASS_WITH_BOUNDARY requires:

1. admitted event reaches exactly the relevant workspace;
2. all unrelated workspace semantic digests remain unchanged;
3. a non-admitted FORUM observation reaches no semantic workspace;
4. a newly introduced FORUM source dependency becomes visible to the invalidation index;
5. source invalidation reaches the direct workspace and its declared downstream workspace, but no unrelated workspace;
6. the scaling witness examines exactly one candidate workspace at every tested population size;
7. all previous memory regressions still pass.

## Boundary

The reference coordinator is single-process and single-writer. It does not yet implement concurrent writers, transaction isolation, rollback, distributed event clocks, network transport, live FORUM mutation, GPU execution, or cross-process persistence. The experiment establishes indexed routing semantics and selective workspace invalidation only. Local index-refresh and history-maintenance costs are measured separately by `PSI-ACTIVE-MEMORY-COST-ACCOUNTING-01`.
