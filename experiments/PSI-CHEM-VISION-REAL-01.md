# PSI-CHEM-VISION-REAL-01

**Status:** EXPERIMENTAL / REAL-IMAGE WITNESS  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30

## 1. Purpose

Replace the synthetic `visual_trace` surrogate from `PSI-CHEM-VISION-LAB-01` with a first set of real chemistry photographs while preserving the same epistemic contract:

\[
\boxed{\text{image evidence}\neq\text{chemical identity}.}
\]

The visual layer remains a reviewed attestation, not an automated pixel classifier.

## 2. Sources

Three Wikimedia Commons witnesses are frozen in `chem-vision-real-images-01.tsv`:

1. methyl-red colour transition under acidic/neutral/alkaline conditions;
2. red-cabbage pH-indicator colour series;
3. iron(II) carbonate formation/colour-state witness.

Each record retains its source page and licence.

## 3. Visual partition

The first two photographs are assigned the same coarse visual class:

\[
\mathrm{MULTI\_SAMPLE\_COLOR\_SERIES}.
\]

Thus the visual fibre is

\[
F_{\rm vis}=\{\mathrm{METHYL\_RED},\mathrm{RED\_CABBAGE}\}.
\]

The concrete chemical systems are distinct, so

\[
|F_{\rm vis}|=2
\]

for the chemical-identity task.

For the coarser reaction-motif task, both instantiate

\[
\mathrm{PH\_INDICATOR\_CHROMATIC\_RESPONSE},
\]

hence

\[
\boxed{|q_{\mathcal T_{\rm motif}}(F_{\rm vis})|=1.}
\]

This is the real-image analogue of the synthetic object-vs-task witness.

## 4. Third witness

The iron(II)-carbonate photograph is placed in the distinct visual class

\[
\mathrm{SOLID\_FORMATION\_COLOR\_STATE}
\]

and the source description records a white solid, carbon-dioxide evolution in the preparation, and a dark green-gray change upon oxygen exposure. Its reaction motif is therefore recorded, conservatively, as

\[
\mathrm{PRECIPITATION\_GAS\_OXIDATION\_COUPLED}.
\]

This witness is not used to claim that a solid-looking image uniquely determines that chemistry.

## 5. Structural recurrence

The experiment distinguishes three levels:

\[
\boxed{
\text{visual class}
\neq
\text{reaction motif}
\neq
\text{chemical identity}.
}
\]

A repeated visual geometry can contain multiple chemical realizations. A repeated reaction motif can likewise have multiple chemical realizations. The task contract decides which quotient matters.

## 6. Information architecture

The intended record is now

\[
I=(\text{image source},\text{visual attestation},\text{reaction motif},\text{chemical identity},\text{provenance}).
\]

The image is not discarded after feature extraction. It remains part of the evidence chain.

Future machine vision should therefore produce only a candidate observation:

\[
\Psi_{\rm image}(I)=Y_{\rm vis},
\]

which enters a compatible fibre. It must not write a chemical identity directly.

## 7. Regression

`scripts/test_chem_vision_real_images.py` checks:

1. two distinct chemical systems share the same coarse visual class;
2. their chemical identity remains unresolved from that class;
3. their coarse pH-indicator reaction motif is task-singleton;
4. the iron(II)-carbonate witness occupies a different visual/reaction class;
5. every record retains a source page and provenance status.

## 8. Boundary

The visual classes were manually reviewed from the source photographs and descriptions. This experiment does **not** measure segmentation accuracy, image embeddings, visual similarity metrics or general chemical-image recognition.

The next meaningful step is not a larger image collection. It is a controlled **representation test**: take the same image set and deliberately vary crop, colour balance, projection and feature granularity to see which apparent clusters survive changes in the visual contract.
