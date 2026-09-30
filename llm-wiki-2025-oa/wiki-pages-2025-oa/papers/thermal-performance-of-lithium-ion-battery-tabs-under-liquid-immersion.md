---
cell_target: "A123 Systems ANR26650M1-B"
doi: "https://doi.org/10.1016/j.fub.2025.100037"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "diamond"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Immersion Cooling"
  - "Battery Thermal Management"
  - "Two-Phase Heat Transfer"
---

# Thermal performance of lithium-ion battery tabs under liquid immersion cooling conditions

## General Analysis

**Core Thesis:** The paper experimentally investigates the thermal behaviour of the electrode terminals (tabs) of a 2.5 Ah LithiumWerks ANR26650M1B LFP cylindrical cell fully immersed in Novec 7000. It compares single-phase natural convection with preheated two-phase (subcooled boiling) immersion conditions during high-rate charging (up to 4C) and discharging (up to 10C), showing that boiling on the terminals limits terminal-to-fluid temperature differences and cell thermal non-uniformity.

**Methodological Focus**
- Testing Mode: CC-CV charging at 1C-4C and CC discharging at 4C-10C with terminal/surface thermocouple measurements and high-speed imaging of boiling
- Operating Conditions: Single-phase natural convection from ambient (initial 18.4-21.9 °C) vs. bulk fluid preheated to 33 °C ± 0.5 °C; chamber pressure 1 bar ± 0.02 bar; discharge to 2 V, charge CV taper to 0.125 A
- Degradation Markers: None

## Keyword Context

- [[immersion-cooling|Immersion Cooling]]: The cell is completely immersed in Novec 7000 dielectric fluid, and terminal and surface heat transfer are compared between single-phase natural convection and two-phase immersion conditions.
- [[battery-thermal-management|Battery Thermal Management]]: Thermal non-uniformity δT and terminal-to-bulk temperature differences are evaluated against BTMS criteria such as the 40 °C limit and the 2 °C degradation threshold.
- Two-Phase Heat Transfer: Subcooled nucleate boiling on the electrode terminals under preheated conditions gave ΔT values two to three times lower than single-phase natural convection.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To experimentally examine heat transfer of the ANR26650M1B LFP cell, particularly at the electrode terminals, and its effect on thermal homogeneity under single-phase and two-phase liquid immersion cooling at high charge/discharge rates; approach: Experimental

> Evidence: "this study aims to experimentally examine the heat transfer performance of a 26650 lithium iron phosphate (LiFePO 4 or LFP) cylindrical battery"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: quantify terminal and surface heat transfer and thermal non-uniformity under immersion cooling; tests: CC-CV charging at 1C, 2C, 3C and 4C (CV until 0.125 A), CC discharging at 4C, 6C, 8C and 10C to 2 V, 1 h OCV rest before each event, high-speed camera imaging (500 Hz) of boiling from 0.8 DOD; data origin: Own experiments

> Evidence: "The cell is deemed to be completely charged when the supplied current tapers to 0.125 A at the end of the CV stage."

### Q3: Ambient Boundary Conditions

**Answer:** Bulk fluid preheated to 33 °C ± 0.5 °C via a cartridge heater in the liquid pool (two-phase tests); single-phase tests started from ambient conditions (initial 18.7-19.9 °C for discharge, 18.4-21.9 °C for charge); vapour condensed by a copper coil fed with 15 °C chiller water, holding chamber pressure at 1 bar ± 0.02 bar; stability/tolerance: ± 0.5 °C (preheated fluid)

> Evidence: "the bulk fluid is preheated to a temperature of 33 ℃ ± 0.5 ℃ , with the single phase natural convection tests performed from ambient conditions"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Exposed-junction T-type thermocouples (0.2 mm) × 7: one on each electrode terminal (offset from the spot-welded nickel tabs) plus five along the cell major axis at 11 mm spacing; attachment: Loctite 315 high-thermal-conductivity adhesive; sampling: not reported (recorded with NI 9213 DAQ); 1.5 mm T-type probes measure bulk fluid and vapour temperature

> Evidence: "A further five thermocouples are positioned along the cell’s major axis at a fixed distance of 11 mm"

### Q6: Temperature-Dependent Performance

**Answer:** At preheated 33 °C vs. single-phase conditions starting at 18.7-19.9 °C, 10C discharge lasted 341 s (0.95 DOD) vs. 330 s (0.92 DOD) with an average 5 % greater electrical power output; at 4C charge, the CC stage extended from ~0.62 to 0.84 SOC and total charging time fell from 1777 s to 1233 s (31 % reduction)

> Evidence: "This amounts as a total charging time of 1233 s at the elevated temperature, a reduction of 31 % in comparison to the 1777 s required"

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
