---
type: concept
aliases:
  - "X-Ray Computed Tomography"
tags:
  - synthesis
---

# X-Ray Computed Tomography

**Summary:** In the 2025 open-access corpus, X-ray computed tomography (CT) is used on commercial cylindrical cells as a nondestructive tool for production-quality inspection, for extracting internal design data to build geometric (CAD) models, and as a swelling proxy after cycling — and one study shows that lab-scale X-ray exposure itself has no measurable effect on cell performance or lifetime. Electrochemical and thermal boundary conditions are largely outside the scope of these studies.

## Synthesized Knowledge

**Inspection and internal design.** On a BYD FC4680 cylindrical cell, CT (73 s acquisition) was compared with ultrasound imaging (three hours) and 2D X-ray imaging (125 ms per image); CT slices resolved individual electrode layers, overhangs, tabs and the electrolyte meniscus and were presented as offering exceptionally rich insight into battery quality, within a perspective that links nonconformance to cell-to-cell variability (Source: [[challenges-and-opportunities-for-high-quality-battery-production-at-sc]]). For five high-power and low-temperature LFP cells including the A123 Systems ANR26650M1-B, pristine cells were micro-CT scanned (Comet YXLON FF85, approximately 10.588 µm voxel size; helical scan at 250 kV/160 µA for the ANR26650M1-B) at room temperature (value not stated) and then torn down, revealing a four-tab design and that the 26650 cell is not a scaled-up version of the same manufacturer's 18650 cell (Source: [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]).

**CT-derived models.** The LFP study converted CT and tear-down data into parameterised 3D CAD models (e.g. simplified 26650 thicknesses of 55 µm anode current collector, 30 µm anode coating, 20 µm separator, 55 µm cathode current collector, 45 µm cathode coating, 0.30 mm can) intended for virtual experiments such as finite element analysis, checked only against the number of jelly-roll windings; limitations include homogeneous layer thicknesses, no inter-layer spacing or tab-induced deformation, unmodelled tab connections, and thickness data that are only indicative due to measurement limitations (Source: [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]). A 1D X-ray absorption model (SpekPy spectrum through can and 40 electrode stacks, thicknesses estimated from a CT radial slice, 50% porosity assumed) plus a lumped heat-capacity estimate gave a worst-case X-ray-induced temperature rise of 0.3 K for the EVE INR18650-33V; the authors note the 1D model overestimates absorption through a cylindrical cell (Source: [[lab-scale-x-ray-exposure-has-no-measurable-impact-on-lithium-ion-batte]]).

**Effect of X-ray exposure on cells.** Fifteen EVE INR18650-33V NMC/graphite cells (control, 2 min and 60 min exposure at 210 kV/190 µA, estimated doses ~10 Gy and ~300 Gy) were characterised by reference performance tests at 33 °C (C/20, C/5, C/2), cycled 300 times at 45 °C (C/2 CC-CV charge, 1C discharge, 2.5–4.2 V) in convection-based chambers (stability not reported), and CT-scanned afterwards to measure jelly-roll core area as a swelling proxy; no statistically significant differences in energy, rate capability, lifetime or swelling were found, and cell temperature measured during exposure confirmed negligible heating (sensor details not reported) (Source: [[lab-scale-x-ray-exposure-has-no-measurable-impact-on-lithium-ion-batte]]). The authors caution that the conclusions may not hold for other formats (e.g. prismatic), chemistries (e.g. sodium-ion), cycling conditions or beyond 300 cycles (Source: [[lab-scale-x-ray-exposure-has-no-measurable-impact-on-lithium-ion-batte]]).

**Gaps and differences.** None of the three studies reports mechanical constraint or cell temperature sensing during electrochemical testing beyond the X-ray-heating check, and only the EVE study controls ambient temperature numerically (33 °C and 45 °C) (Source: [[lab-scale-x-ray-exposure-has-no-measurable-impact-on-lithium-ion-batte]]; [[challenges-and-opportunities-for-high-quality-battery-production-at-sc]]; [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]). Scan durations differ by more than an order of magnitude — 73 s on the FC4680 (Source: [[challenges-and-opportunities-for-high-quality-battery-production-at-sc]]) versus 2 min and 60 min exposures on the INR18650-33V (Source: [[lab-scale-x-ray-exposure-has-no-measurable-impact-on-lithium-ion-batte]]) — so the no-impact finding was tested for exposures at and well above the FC4680 scan duration, but on a different cell. No direct contradictions between the papers were found.

## Literature Mentions

- [[challenges-and-opportunities-for-high-quality-battery-production-at-sc]]: BYD FC4680; CT (73 s) compared with ultrasound and 2D X-ray resolves electrode layers, overhangs, tabs and electrolyte meniscus for quality inspection.
- [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]: A123 Systems ANR26650M1-B (and four other LFP cells); micro-CT at ~10.6 µm voxel plus tear-down yields component thicknesses, a four-tab design and simplified CAD models.
- [[lab-scale-x-ray-exposure-has-no-measurable-impact-on-lithium-ion-batte]]: EVE INR18650-33V; 2 min and 60 min X-ray exposures caused no significant change in capacity, rate, 300-cycle lifetime at 45 °C or CT-measured swelling.

## Related Concepts

- [[cell-teardown-analysis|Cell Teardown Analysis]]
- [[cell-to-cell-variation|Cell-to-Cell Variation]]
- [[capacity-degradation|Capacity Degradation]]
- [[post-mortem-analysis|Post-Mortem Analysis]]

*Last updated: 2026-09-27*
