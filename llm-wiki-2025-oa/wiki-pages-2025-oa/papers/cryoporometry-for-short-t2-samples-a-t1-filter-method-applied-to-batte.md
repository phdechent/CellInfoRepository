---
cell_target: "LG Chem INR21700 M50"
doi: "https://doi.org/10.1016/j.mrl.2025.200180"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "NMR Cryoporometry"
  - "Pore Size Distribution"
  - "Post-Mortem Analysis"
---

# Cryoporometry for short T2 samples: A T1 filter method applied to battery electrode characterization

## General Analysis

**Core Thesis:** The paper introduces a T1-filter NMR cryoporometry method, using a Peltier-controlled probe and OMCTS as saturating liquid, to measure pore size distributions (about 8 nm to 1 μm) in paramagnetic Li-ion cathodes where liquid and frozen phases cannot be separated by T2. The NMC811 cathode harvested from an un-aged LG Chem 21700 M50 cell (plus a Saft LFP electrode) serves as a demonstration sample, yielding a bimodal pore size distribution.

**Methodological Focus**
- Testing Mode: Cell disassembly and electrode harvesting; low-field (20.9 MHz) NMR relaxometry (FID, CPMG, saturation recovery, T1–T2 maps); NMR cryoporometry with T1 filter
- Operating Conditions: Sample temperature ramp from -10 °C up to the OMCTS melting point (17.25 °C), ramp as slow as 0.002 °C/min near melting; no electrochemical operation
- Degradation Markers: None (un-aged cell)

## Keyword Context

- NMR Cryoporometry: A T1-filter variant of NMR cryoporometry is developed because the T2 of OMCTS in LFP and NMC cathodes is too short (0.02–0.2 ms) for the standard T2-filter method.
- Pore Size Distribution: The melting curve of OMCTS in the stacked NMC electrode segments is converted via the Gibbs-Thomson relation into a pore size distribution, which is bimodal for the NMC electrode.
- [[post-mortem-analysis|Post-Mortem Analysis]]: The NMC electrode was obtained by disassembling an un-aged LG Chem 21700 M50 cell in a nitrogen glove box, rinsing with dimethyl carbonate and vacuum drying.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study establishes a T1-filter NMR cryoporometry method to obtain pore size distributions of paramagnetic battery cathodes, demonstrated on the NMC811 cathode from an LG Chem 21700 M50 cell; approach: Experimental

> Evidence: "Instead, we propose to use the T 1 contrast to separate these phases."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: characterize the pore structure of the cathode harvested from the target cell and demonstrate the T1-filter method; tests: cell disassembly in N2 glove box, DMC rinsing and vacuum drying of the NMC electrode, saturation with OMCTS (about 20 stacked electrode segments or pellet), T2 (CPMG) and T1 (saturation recovery) relaxation measurements and T1–T2 maps, and NMR cryoporometry melting-curve measurements (RD = 500 ms, 64 scans, ~31 s per point for NMC, melt volume 87 μL); data origin: Own experiments

> Evidence: "After disassembling the cell in a nitrogen-filled glove box to avoid contact with moisture and oxygen, the electrodes were rinsed with dimethyl carbonate solvent"

### Q3: Ambient Boundary Conditions

**Answer:** Sample (not cell) temperature scanned from -10 °C up to the OMCTS bulk melting temperature via a Peltier system inside the NMR probe, with the hot side held by a cooling bath; stability/tolerance: accuracy 0.05 °C, sensitivity 0.001 °C; ramps as slow as 0.002 °C/min near melting

> Evidence: "providing a very precise and convenient control of the temperature (accuracy of 0.05 °C and sensitivity of 0.001 °C)"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** No operating-cell temperature measurement (electrode sample only); 4-wire platinum sensors × 2 placed inside the copper pieces near the sample; attachment: embedded in copper pieces; sampling: data points every 60 s during the melting ramp

> Evidence: "two 4 wire platinum sensors (accuracy ±0.03 °C, sensitivity and resolution of 0.001 °C) are placed inside the copper pieces and near the sample"

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: explain the NMR signal under a T1 filter so that the liquid fraction derivative (and hence pore size distribution via the Gibbs-Thomson equation) can be extracted; type: analytical two-component NMR relaxation signal model (no battery cell model); thermal component: No (only the temperature dependence of frozen-OMCTS T1 is considered)

> Evidence: "The measured amplitude S m can be modeled by the following equation, assuming two single components T 1L and T 1S for the liquid and solid relaxation time"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from the authors' own relaxation measurements (T1 of liquid vs. frozen OMCTS, linear T1S–temperature relation of bulk frozen OMCTS) and literature Gibbs-Thomson constants (kGT = 113 K·nm, τ = 2 nm); melting curve calibrated using the fluid volume from dry/wet mass difference; no quantitative validation against another pore-characterization technique

> Evidence: "the melting curve is calibrated using the volume of fluid determined from the mass difference between the dry and wet states"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: pore sizes from about 8 nm (lowest temperature -10 °C) up to about 1 μm; explicitly reported limitations: small LFP pore class around 10 nm is at the instrument's resolution limit, spline-smoothing artefacts above 1 μm for NMC, and comparison with other characterization techniques is outside the scope

> Evidence: "For the LFP case, there is clearly a small class of pores around 10 nm, at the limit of resolution of the present instrument"
