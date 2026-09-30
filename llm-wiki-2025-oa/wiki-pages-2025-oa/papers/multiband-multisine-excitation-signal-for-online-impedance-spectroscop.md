---
cell_target: "Samsung SDI ICR18650-26J"
doi: "https://doi.org/10.3390/batteries11050188"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Electrochemical Impedance Spectroscopy"
  - "Multisine Excitation"
  - "Fractional-Order Equivalent Circuit Model"
---

# Multiband Multisine Excitation Signal for Online Impedance Spectroscopy of Battery Cells

## General Analysis

**Core Thesis:** The paper proposes a multiband multisine excitation for online EIS, in which the spectrum is split into sequentially excited sub-bands to raise per-tone SNR at nearly the same measurement time as single-band multisine. The Samsung ICR18650-26J enters as the device-under-test model: its fractional-order ECM, extracted from the authors' Hioki IM3590 impedance measurement of a fully charged cell, is embedded in a hardware/software co-simulation framework, where the multiband approach reduces impedance magnitude RMSE from 7.30 mΩ to 0.40 mΩ.

**Methodological Focus**
- Testing Mode: Laboratory EIS (Hioki IM3590 chemical impedance analyzer) on a fully charged cell for ECM extraction; co-simulation of multisine EIS in [1–100] Hz
- Operating Conditions: Fully charged cell (SOC 100%); temperature not reported
- Degradation Markers: None

## Keyword Context

- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]: Online broadband EIS is the application target, and a lab EIS measurement of the target cell provides the reference impedance for the simulated measurement system.
- Multisine Excitation: The core contribution divides the multisine spectrum into K sub-bands (e.g., K = 4 sub-bands of 5 tones in [1–100] Hz) with crest-factor optimization per sub-band.
- [[fractional-order-equivalent-circuit-model|Fractional-Order Equivalent Circuit Model]]: The target cell is represented in the circuit co-simulation by a fractional-order ECM whose parameters were experimentally extracted.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study demonstrates that a multiband multisine excitation improves online EIS accuracy at short measurement time, using a fractional-order ECM of the fully charged Samsung ICR18650-26J as the simulated cell under test; approach: Hybrid

> Evidence: "A commercial battery cell was modeled with a fractional-order ECM whose parameters were experimentally extracted"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: extract fractional-order ECM parameters of the target cell for the co-simulation framework; tests: impedance measurement of a fully charged ICR18650-26J with a Hioki IM3590 Chemical Impedance Analyzer (a separate online multiband EIS demonstration with the hardware prototype during a C/3 capacity check was performed on an unnamed 2.9 Ah 18650 cell, not the target cell); data origin: Own experiments

> Evidence: "Values of the parameters were experimentally extracted using a Hioki IM3590 Chemical Impedance Analyzer."

### Q3: Ambient Boundary Conditions

**Answer:** Not explicitly discussed.

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: provide the reference impedance of the cell under test in a co-simulation (digital twin) of an EIS sensing system to compare excitation strategies; type: fractional-order equivalent circuit model embedded in a CAD circuit simulator with Verilog-A ADC models; thermal component: No

> Evidence: "it consists of an actual digital twin of the overall sensing system, being an excellent and flexible environment to compare, in particular, different excitation techniques"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from the authors' own Hioki IM3590 impedance measurement of the fully charged cell; the simulated EIS estimates are compared against the analytical ECM spectrum: magnitude RMSE 7.30 mΩ (single-band) vs. 0.40 mΩ (multiband with CF optimization) and 0.47 mΩ (without CF optimization); phase RMSE 67.8, 4.9 and 11.2 mrad, respectively

> Evidence: "The RMSE of the impedance magnitude improved from 7.30 m Ωfor the single-band multisine to 0.40 m Ωfor the multiband multisine approach"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped; represented inhomogeneities: none

> Evidence: "Equivalent circuit model of the fully-charged battery cell Samsung ICR18650-26J used in the simulation framework."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: fully charged cell only, excitation band [1–100] Hz in simulation; explicitly reported limitations: linear frequency spacing chosen for crest-factor reasons although logarithmic spacing is usual, sub-band switching time Tw treated as a hardware-dependent parameter, and nonlinear/time-varying impedance estimation not covered

> Evidence: "Alternative solutions have been developed during the last decade to estimate nonlinear and time-varying impedances, which make use of advanced algorithms [ 28,29] but are not covered in this work."
