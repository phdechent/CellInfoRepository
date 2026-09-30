---
cell_target: "Samsung SDI ICR18650-26J"
doi: "https://doi.org/10.3390/batteries11100351"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Electrochemical Impedance Spectroscopy"
  - "Fractional-Order Equivalent Circuit Model"
  - "Hardware-Software Co-Simulation"
---

# An Integrated Co-Simulation Framework for the Design, Analysis, and Performance Assessment of EIS-Based Measurement Systems for the Online Monitoring of Battery Cells

## General Analysis

**Core Thesis:** The paper proposes a Cadence–Matlab co-simulation framework that models the hardware and software of an online EIS measurement system together with a battery cell ECM, to debug, refine and validate EIS sensor designs. Impedance measured on a fully charged Samsung ICR18650-26J cell with a benchtop Hioki IM3590 parameterizes the cell models, and the framework predictions are compared with the refined EIS prototype and the Hioki reference.

**Methodological Focus**
- Testing Mode: Electrochemical impedance spectroscopy (benchtop Hioki IM3590 and in-house multisine EIS sensor-node prototype)
- Operating Conditions: Fully charged cell; 1 mA nominal excitation current; test frequencies 4.64–120.54 Hz (prototype range 1–200 Hz); temperature not reported
- Degradation Markers: None

## Keyword Context

- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]: Online EIS with a multisine delta-sigma excitation prototype and benchtop Hioki EIS on the target cell provide the impedance data the framework is designed and validated against.
- [[fractional-order-equivalent-circuit-model|Fractional-Order Equivalent Circuit Model]]: A modified Randles ECM with a CPE, approximated by a Cauer I RC ladder within 1% over 4–120 Hz, represents the cell in the circuit simulator.
- Hardware-Software Co-Simulation: Cadence ic 6.17 circuit simulation is linked with Matlab impedance-estimation algorithms to reveal how hardware non-idealities, such as common-mode noise, affect the final impedance estimate.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To develop and validate an integrated hardware–software co-simulation framework for EIS-based online battery monitoring systems, using impedance measured on a Samsung ICR18650-26J cell to parameterize the cell model and to compare predictions with prototype and benchtop measurements; approach: Hybrid

> Evidence: "This study aims to develop an integrated co-simulation framework to support the design, debugging, and validation of EIS measurement systems devoted to the online monitoring of battery cells"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: extract cell ECM parameters and experimentally validate the co-simulation framework; tests: benchtop EIS with Hioki IM3590 on a fully charged ICR18650-26J cell; online EIS with the refined sensor-node prototype on a real fully charged lithium-ion cell and on an RC reference DUT, compared with Hioki data; data origin: Own experiments

> Evidence: "experimentally extracted from a real fully charged cylindrical battery cell Samsung ICR18650-26J 2600 mAh"

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

**Answer:** Purpose: prediction of the impedance spectrum estimated by the complete EIS hardware/software chain including non-idealities; type: circuit-level co-simulation with a battery ECM (first a simplified RCL ECM, then a fractional-order modified Randles ECM with CPE); thermal component: No

> Evidence: "the simple battery cell model of Figure 3 is substituted with a more accurate version that incorporates a CPE"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from own Hioki IM3590 measurements on a fully charged cell (resistors and CPE parameters), with the CPE approximated by continued fraction expansion and a Cauer I ladder (max. deviation <1% over 4–120 Hz); validated against ECM analytical values, the refined prototype and Hioki data: RMS deviation versus ECM 18.5 mΩ (real) and 17.8 mΩ (imaginary) before hardware refinement and 0.59 mΩ and 0.86 mΩ after

> Evidence: "the values of the two resistors and the parameters characterizing the CPE were experimentally extracted by means of measurements carried out with the Hioki Chemical Impedance Analyzer"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (resistor in series with a resistor parallel to a CPE); represented inhomogeneities: none

> Evidence: "Even a simple modified Randles model consisting of a resistor in series to the parallel connection of another resistor with a CPE"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: fully charged cell, test frequencies 4.64–120.54 Hz with 1 mA nominal excitation; explicitly reported limitations: connection impedances and the ASIC-to-cell fixture not modeled, parameter dispersion of components requires calibration, residual low-frequency discrepancies, and about one hour per simulation restricting use to offline analysis

> Evidence: "connection impedances are not modeled in the simulation"
