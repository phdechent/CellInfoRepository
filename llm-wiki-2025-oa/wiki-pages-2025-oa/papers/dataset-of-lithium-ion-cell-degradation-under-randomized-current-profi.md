---
cell_target: "JGNE JGPFR26650; Samsung SDI ICR18650-26J; Samsung SDI INR21700-40T"
doi: "https://doi.org/10.1016/j.dib.2025.111531"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Battery Dataset"
  - "Capacity Degradation"
  - "Hybrid Pulse Power Characterization"
---

# Dataset of lithium-ion cell degradation under randomized current profiles for NMC, NCA, and LFP chemistries

## General Analysis

**Core Thesis:** The paper describes an experimental aging dataset of eight lithium-ion cells (four Samsung ICR18650-26J NCA, two Samsung INR21700-40T NMC, two JGNE JGPFR26650 LFP) cycled with randomized discharge current profiles for more than 600 cycles. Periodic HPPC, capacity and reference performance tests capture capacity fade and power loss to support model and BMS development.

**Methodological Focus**
- Testing Mode: Randomized-current (RC) discharge cycling with CC-CV charging; periodic HPPC and 1C constant-current reference performance tests; low-current (0.04 A) OCV discharges
- Operating Conditions: Room temperature (no value stated); 1C CC-CV charge; discharge 0.5C to 5C (up to 2C for NCA); HPPC at 0.5C, 1C, 2C every 20 cycles; 1 Hz sampling
- Degradation Markers: Capacity fade (SOH from capacity tests), power loss

## Keyword Context

- [[battery-dataset|Battery Dataset]]: The paper publishes raw (.xlsx) and processed (.mat) cycling and diagnostic data for eight cells in the FairData repository.
- [[capacity-degradation|Capacity Degradation]]: SOH is computed from the discharged capacity in periodic capacity tests normalized to nominal capacity to track aging over more than 600 cycles.
- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]: HPPC tests at 0.5C, 1C and 2C are performed after every 20 cycles to track changes in transient dynamics.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study provides a dataset characterizing degradation of NMC, NCA and LFP cells under randomized usage profiles with periodic diagnostic tests; approach: Experimental

> Evidence: "This paper describes an experimental dataset of lithium-ion cells subjected to a randomized usage profile and periodically characterized through diagnostic tests."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: capture cell aging (capacity fade and power loss) under randomized usage patterns for model and BMS development; tests: activation with two full cycles at 0.5C, low-current (0.04 A) OCV discharge, RC discharge cycling (one-minute random current steps, 0.5C to 5C, up to 2C for NCA) with 1C CC-CV recharge, HPPC at 0.5C/1C/2C every 20 cycles with 6 min pulses, 1C reference constant-current discharge; data origin: Own experiments

> Evidence: "After every set of 20 cycles, HPPC tests are performed at different current rates (0.5C, 1C, and 2C)."

### Q3: Ambient Boundary Conditions

**Answer:** Room temperature (no numerical value stated); control method not reported; stability/tolerance: not reported (ambient temperature was recorded)

> Evidence: "All cells are tested at room temperature."

### Q4: Mechanical Boundary Conditions

**Answer:** Cell tested inside a clamp; magnitude: not reported; fixture: clamp (no further description)

> Evidence: "Each cell was tested inside the clamp and instrumented with a T-type thermocouple"

### Q5: Cell Temperature Measurement

**Answer:** T-type thermocouple × 1 at the centre of the cell surface; attachment: not reported; sampling: 1 Hz

> Evidence: "instrumented with a T-type thermocouple to measure the surface temperature in the center location"

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Not explicitly discussed.

### Q9: Model Parameterization and Validation

**Answer:** Not explicitly discussed.

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Not explicitly discussed.
