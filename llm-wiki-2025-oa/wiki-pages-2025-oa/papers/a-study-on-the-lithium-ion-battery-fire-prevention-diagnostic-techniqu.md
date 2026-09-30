---
cell_target: "Samsung SDI INR18650-30Q"
doi: "https://doi.org/10.3390/en18246510"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Internal Short Circuit"
  - "Partial Discharge Detection"
  - "Thermal Runaway"
---

# A Study on the Lithium-Ion Battery Fire Prevention Diagnostic Technique Based on Time-Resolved Partial Discharge Algorithm

## General Analysis

**Core Thesis:** The paper proposes a time-resolved partial discharge (TRPD) and FFT-based diagnostic method to detect micro internal short circuits as early electrical precursors of thermal runaway. Using Samsung INR18650-30Q cells in accelerated-degradation cycling (in situ) and probe-induced mechanical deformation (ex situ) tests, it identifies characteristic defect-signal peaks at 3.9, 11.9 and 19 MHz.

**Methodological Focus**
- Testing Mode: CCCV/CC accelerated degradation cycling with HFCT and electromagnetic-antenna signal acquisition; mechanical deformation (abuse) tests with needle, spherical and semi-elliptical probes
- Operating Conditions: 25 °C and 60 °C; 1C and 2C, CCCV charge to 4.2 V, CC discharge to 2.5 V; oscilloscope sampling 80 MS/s
- Degradation Markers: Capacity fade; high-frequency defect discharge signals

## Keyword Context

- Internal Short Circuit: Micro internal short circuits are detected via high-frequency transient discharge signals whose FFT spectra show peaks near 3.9 MHz, 11.9 MHz and 19 MHz.
- Partial Discharge Detection: Time-resolved partial discharge analysis, adapted from high-voltage insulation diagnostics, treats the separator as the dielectric layer and uses amplitude thresholds of 250 mV (HFCT) and 2 V (antenna).
- [[thermal-runaway|Thermal Runaway]]: The diagnostic method aims at early recognition of latent insulation degradation and internal short circuits before thermal runaway occurs.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To develop and demonstrate a TRPD–FFT diagnostic technique that detects micro internal short circuits in Samsung INR18650-30Q cells as early fire-hazard precursors; approach: Experimental

> Evidence: "This study proposes a time-resolved partial discharge (TRPD)-based diagnos- tic method for identifying early electrical precursors of fire hazards in lithium-ion batteries."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: collect defect signal data under accelerated degradation and physical deformation; tests: in situ accelerated degradation cycling at 1C and 2C (CCCV to 4.2 V, CC to 2.5 V) at 25 °C and 60 °C with HFCT and electromagnetic antenna measurements, ex situ probe-induced deformation in 1 mm steps with EMW, TEV and HFCT sensors, three repetitions per condition; data origin: Own experiments

> Evidence: "Cylindrical LIBs were subjected to accelerated degradation tests under two temperature conditions: room temperature (25◦C) and high temperature (60◦C)."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C and 60 °C (cycling) via controlled environment, control method not specified; stability/tolerance: not reported

> Evidence: "Environmental factors such as temperature and humidity were carefully controlled."

### Q4: Mechanical Boundary Conditions

**Answer:** Controlled mechanical deformation (abuse) with sharp needle, spherical and semi-elliptical probes applied in 1 mm incremental steps (ex situ tests only); magnitude: force not reported; fixture: deformation unit with battery holder in safety enclosure

> Evidence: "The deformation was applied in 1 mm incremental steps"

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Across 25 °C and 60 °C at 1C and 2C, capacity decreased progressively with cycling, with the most rapid decline at 60 °C and 2C, attributed to accelerated side reactions and SEI decomposition

> Evidence: "the capacity reduction rate was most pronounced in the high-temperature 2C-rate test"

### Q8: Model Purpose and Type

**Answer:** Not explicitly discussed.

### Q9: Model Parameterization and Validation

**Answer:** Not explicitly discussed.

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Not explicitly discussed.
