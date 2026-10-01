# PSI-VIZ-R4-STATUS-REDACTION-01

**Status:** `PASS_WITH_BOUNDARY`  
**Date:** 2026-09-30  
**Branch:** `psi-memory-map-01`  
**Corrected implementation:** `7d76308bf7ae63f43606f58c50d7948c89f2860b`  
**Scope:** PSI-VIZ status visibility at the checked projection boundary and its downstream consumers.  
**Does not modify:** CORE5, CANON-03, Guardian admission, live FORUM gateway, R5 relation-direction semantics.

## 1. Defect

The visual contract already gated edge status on

```text
"status" in visible_metadata
```

but `compile_visual_frame` copied `workspace.node_status` unconditionally.
Therefore a contract with `visible_metadata=()` could still expose node status,
and downstream `PrintKeyframe` / SVG could render it.

This violated the audit rule

\[
P_i(S)\not\Rightarrow S:
\]

redaction of one projection component (edge status) did not establish complete
status redaction of the visual packet.

## 2. Separating witness — FAIL before correction

Executable witness: `scripts/test_psi_viz_status_redaction_r4.py`.

Source state contains:

```text
X.status = NEEDS_RECHECK
edge(Y, COMPATIBLE_WITH, X).status = ADMITTED
```

Two contracts are compiled over the same state:

```text
C_hidden.visible_metadata = ()
C_visible.visible_metadata = ("status",)
```

Before correction, workflow run `36773765562`, job `110086411840`, failed at:

```python
assert hidden_a.semantic_payload.get("node_status", {}) == {}
```

Thus the hidden contract still carried node status. This is the executable
FAIL-before witness required by R4.

## 3. Correction

`compile_visual_frame` now projects node status only when status is explicitly
allowed by the visual contract:

```python
"node_status": (
    dict(sorted(workspace.node_status.items()))
    if "status" in contract.visible_metadata
    else {}
),
```

No renderer-side policy filter was added. Guardian/admission logic was not
changed. Downstream consumers remain restricted to the checked projection.

## 4. Acceptance evidence

The R4 gate `36773865796` completed successfully and includes:

1. R4 separating witness;
2. R3 digest/binding regression;
3. F4.0 projection regression;
4. F4.1 output regression;
5. F4.2 renderer regression;
6. F4.3 executable-source regression.

The witness establishes for `C_hidden`:

- no node status in `VisualFrame`;
- no edge status in `VisualFrame`;
- forbidden status absent from `PrintKeyframe`;
- forbidden status absent from SVG text/metadata;
- forbidden status absent from `ManimPlan`;
- forbidden status absent from executable Manim source.

For `C_visible` it establishes that node and edge status remain explicitly
available in `VisualFrame` and `PrintKeyframe` and renderable in SVG.

The hidden and visible semantic digests differ, so R3 packet-integrity checking
remains operative after the projection change.

Independent gates for corrected commit `7d76308...` also passed:

- F4.0 contract: run `36773865836` — `success`;
- R3 digest integrity: run `36773865827` — `success`;
- F4.2 renderer: run `36773865817` — `success`;
- F4.3 real Manim execution: run `36773865882` — `success`.

The real-Manim job `110086752607` independently passed source re-verification,
Manim runtime installation, real MP4 rendering, rendered-video verification,
finite-representation control, active-memory regression and institutional
constitution regression, then uploaded the render products.

## 5. Result

\[
\boxed{R4=PASS\_WITH\_BOUNDARY}
\]

Operationally:

```text
status hidden by projection contract
    -> absent from checked downstream visual channels

status explicitly allowed
    -> preserved in declared status-bearing frame/print/SVG channels
```

The result is a projection guarantee, not a global authorization theorem.

## 6. Boundary

R4 does **not** claim that animation exposes every allowed status/provenance
field. The current `ManimPlan` intentionally does not preserve those metadata
fields as visual assets. Declaring animation metadata exposure belongs to the
R5 visual-relation/exposure unit or a later typed channel contract.

R4 also does not establish visible direction of directed relations. That is R5.

Therefore the next repair unit is:

\[
\boxed{R5\;\text{— directed visual relations}.}
\]
