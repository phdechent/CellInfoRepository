---
type: concept
aliases:
  - "Post-Mortem Analysis"
tags:
  - synthesis
---

# Post-Mortem Analysis

**Summary:** In the two 2025 open-access studies referencing this concept, post-mortem work means disassembling pristine (un-aged) commercial cells to harvest cathodes for ex situ materials characterization, NMR cryoporometry on an LG Chem INR21700 M50 NMC811 cathode and Raman spectroscopy on an A123 ANR26650M1-B LFP cathode. Both show that the opening atmosphere is a controlled boundary condition of the method.

## Synthesized Knowledge

**Harvesting protocols.** The LG Chem INR21700 M50 cell was disassembled in a nitrogen-filled glove box to avoid contact with moisture and oxygen; its NMC811 electrode was rinsed with dimethyl carbonate, vacuum-dried and stacked (about 20 segments) for saturation with OMCTS (Source: [[cryoporometry-for-short-t2-samples-a-t1-filter-method-applied-to-batte]]). The A123 ANR26650M1-B cells were discharged to the minimum safe cut-off voltage and opened either in an argon glove-box (reference cathode, R-LFP) or deliberately in laboratory air at about 25 °C and about 50% humidity (humidity-exposed cathode, H-LFP); Sony US18650V3 NMC-LMO cathodes were treated the same way (Source: [[raman-spectroscopy-of-practical-lib-cathodes-a-study-of-humidity-induc]]). Neither study aged the cells electrochemically before opening; the M50 is explicitly un-aged (Source: [[cryoporometry-for-short-t2-samples-a-t1-filter-method-applied-to-batte]]) and the A123 cells were pristine (Source: [[raman-spectroscopy-of-practical-lib-cathodes-a-study-of-humidity-induc]]).

**Characterization techniques and findings.** For the INR21700 M50 cathode, a T1-filter NMR cryoporometry method was developed because the T2 of OMCTS in paramagnetic NMC and LFP cathodes (0.02–0.2 ms) is too short for the standard T2 filter; the melting curve converted via the Gibbs-Thomson relation gave a bimodal pore size distribution, covering about 8 nm to 1 μm (Source: [[cryoporometry-for-short-t2-samples-a-t1-filter-method-applied-to-batte]]). The sample temperature (not a cell temperature) was controlled by a Peltier system inside the NMR probe with 0.05 °C accuracy, ramped from -10 °C to the OMCTS melting point (17.25 °C) as slowly as 0.002 °C/min, and measured with two 4-wire platinum sensors in the copper pieces near the sample (Source: [[cryoporometry-for-short-t2-samples-a-t1-filter-method-applied-to-batte]]). For the A123 ANR26650M1-B cathode, confocal Raman spectroscopy (632.8 nm), SEM/EDS and CR2032 coin-cell cycling at C/10 (2.5–3.65 V) linked humidity exposure to a blue shift of carbon D and G bands, a 957 cm−1 shoulder of delithiated LFP, etched/spheroidized particle morphology and capacity fade, with LFP fading more slowly than NCM-LMO (Source: [[raman-spectroscopy-of-practical-lib-cathodes-a-study-of-humidity-induc]]).

**Limitations relevant to cell-level review questions.** Neither study reports ambient temperature control of an operating cell, mechanical constraint, or operating-cell temperature sensing, and neither builds a battery cell model (Source: [[cryoporometry-for-short-t2-samples-a-t1-filter-method-applied-to-batte]]; Source: [[raman-spectroscopy-of-practical-lib-cathodes-a-study-of-humidity-induc]]). The cryoporometry method has not been validated quantitatively against another pore-characterization technique, the ~10 nm LFP pore class sits at the instrument's resolution limit, and spline-smoothing artefacts appear above 1 μm for NMC (Source: [[cryoporometry-for-short-t2-samples-a-t1-filter-method-applied-to-batte]]). The two studies differ in inert gas (nitrogen vs. argon) but no contradiction in findings arises; the Raman study's observation that air opening damages the cathode (Source: [[raman-spectroscopy-of-practical-lib-cathodes-a-study-of-humidity-induc]]) is consistent with the moisture-exclusion rationale of the cryoporometry harvesting (Source: [[cryoporometry-for-short-t2-samples-a-t1-filter-method-applied-to-batte]]).

## Literature Mentions

- [[cryoporometry-for-short-t2-samples-a-t1-filter-method-applied-to-batte]]: NMC811 cathode from an un-aged LG Chem INR21700 M50, harvested in N2 glove box, yields a bimodal pore size distribution (~8 nm–1 μm) by T1-filter NMR cryoporometry.
- [[raman-spectroscopy-of-practical-lib-cathodes-a-study-of-humidity-induc]]: LFP cathodes from pristine A123 ANR26650M1-B cells opened in argon vs. humid air show Raman, morphological and coin-cell capacity signatures of humidity damage.

## Related Concepts

- [[cell-teardown-analysis|Cell Teardown Analysis]]
- [[capacity-degradation|Capacity Degradation]]
- [[x-ray-computed-tomography|X-Ray Computed Tomography]]

*Last updated: 2026-09-27*
