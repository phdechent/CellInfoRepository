---
cell_target: "Panasonic-Sanyo NCR18650GA"
doi: "https://doi.org/10.3390/ma18010213"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Phase Change Material"
  - "Battery Thermal Management"
  - "Electrodeposited Coating"
---

# Electrolytic Ni-P and Ni-P-Cu Coatings on PCM-Loaded Expanded Graphite for Enhanced Battery Thermal Management with Mechanical Properties

## General Analysis

**Core Thesis:** The paper develops electrolytic Ni-P and Ni-P-Cu coatings on RT42 paraffin-loaded expanded graphite (PCM/EG) blocks to raise their thermal conductivity and mechanical strength for passive battery cooling. A 3s2p pack of Panasonic/Sanyo NCR18650GA cells embedded in the blocks is discharged at 1.25C and 2.5C to show that the Ni-P-Cu coating (27.1 W/m·K) yields the lowest cell temperatures and longest discharge durations.

**Methodological Focus**
- Testing Mode: Constant-current pack discharge with multi-point thermocouple temperature measurement; material characterization (SEM/EDS, XRD, DSC, TGA, transient hot bridge thermal conductivity, tensile/compression tests)
- Operating Conditions: 25 °C ambient in a conditioned chamber; 3s2p pack discharged at 1.25C and 2.5C (8.1 A and 10.2 A stated in methods) to 7.8 V or 60 °C
- Degradation Markers: None

## Keyword Context

- [[phase-change-material|Phase Change Material]]: RT42 paraffin (phase transition approx. 38–43 °C) impregnated into expanded graphite at about 90% PCM absorbs cell heat as latent heat and creates a temperature plateau during discharge.
- [[battery-thermal-management|Battery Thermal Management]]: Uncoated, Ni-P-coated and Ni-P-Cu-coated PCM/EG packs are compared by peak cell surface temperature, discharge duration, capacity and energy of a six-cell NCR18650GA pack.
- Electrodeposited Coating: Ni-P and Ni-P-Cu layers deposited electrolytically (Cu supplied from a scrap copper anode) raise the composite thermal conductivity from 5.67 to 16.5 and 27.1 W/m·K and increase compressive strength up to 39.4 MPa.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To determine whether electrolytic Ni-P and Ni-P-Cu coatings on PCM/EG cooling packs improve thermal conductivity, mechanical strength and the thermal management of an NCR18650GA battery pack under 1.25C and 2.5C discharge; approach: Experimental

> Evidence: "the proposed project aims to coat PCM/EG thermal control systems/cooling packs with both Ni"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: evaluate the thermal management performance of uncoated, Ni-P-coated and Ni-P-Cu-coated PCM/EG packs; tests: 3s2p pack (six NCR18650GA cells, 11.7 V, 6700 mAh) constant-current discharges at 1.25C and 2.5C with termination at 7.8 V or 60 °C, recording local temperatures, voltage/current, capacity and energy (three repeats per configuration); data origin: Own experiments

> Evidence: "Performance tests were conducted in a conditioned chamber/incubator (Nucleon brand)"

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via conditioned chamber/incubator (Nucleon), with initial temperatures set to 25 °C to reach thermal equilibrium before loading; stability/tolerance: not reported

> Evidence: "with the initial temperatures at time t = 0 set to 25 °C to achieve thermal equilibrium"

### Q4: Mechanical Boundary Conditions

**Answer:** No pressure constraint reported; cells were inserted in 18 mm-diameter cell spaces of the PCM/EG block, connected by nickel strip, and supported top and bottom by 5 mm thick 3D-printed parts; magnitude: not reported

> Evidence: "printed s upport parts (5 mm thick, dark blue color)"

### Q5: Cell Temperature Measurement

**Answer:** T-type thermocouples × 6 on cell number 1: T1–T3 on the outer surface and T4–T6 on the inner surface (bottom, middle, top); attachment: described only as attached, method not specified; sampling: not reported (Keithley 2701 data acquisition and PCE-1200 device)

> Evidence: "T4, T5, and T6 represent the three thermocouples on the inner surface of cell number 1"

### Q6: Temperature-Dependent Performance

**Answer:** At 25 °C ambient only (no ambient-temperature variation): at 2.5C the uncoated PCM/EG pack peaked at approx. 61 °C with approx. 900 s discharge, whereas the Ni-P-Cu-coated pack stabilized at approx. 53 °C with approx. 1400 s discharge; at 1.25C peaks were approx. 43 °C (PCM/EG), 45 °C (Ni-P) and 42 °C (Ni-P-Cu), with discharge durations of about 2400, 2600 and 2800 s

> Evidence: "coated PCM/EG stabilized at approximately 53 °C after ~1300 s"

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
