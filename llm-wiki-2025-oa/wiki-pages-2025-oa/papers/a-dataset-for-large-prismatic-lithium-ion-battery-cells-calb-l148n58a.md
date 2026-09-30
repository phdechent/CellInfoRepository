---
cell_target: "CALB L148N58A"
doi: "https://doi.org/10.1016/j.dib.2025.111301"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Battery Dataset"
  - "Cell-to-Cell Variation"
  - "Electrochemical Impedance Spectroscopy"
---

# A dataset for large prismatic lithium-ion battery cells (CALB L148N58A): Comprehensive characterization and real-world driving cycles

## General Analysis

**Core Thesis:** The paper publishes an experimental dataset for a batch of eleven fresh B-grade CALB L148N58A prismatic NMC/graphite cells (58 Ah), characterized with C/20 capacity tests, HPPC, EIS and scaled WLTP/UDDS/US06 driving cycles at 10, 25 and 40 °C. The data are intended to reveal post-manufacturing cell-to-cell variation in capacity and impedance and to support battery model development and BMS algorithm validation.

**Methodological Focus**
- Testing Mode: C/4 CCCV conditioning, C/20 CC discharge/CCCV charge capacity test, HPPC with 1C and C/3 discharge pulses (10 s pulses, 10 min rest), concatenated WLTP/UDDS/US06 driving cycles scaled to 1C peak current, EIS from 0.01 Hz to 3 kHz at 20/40/60/80% SOC
- Operating Conditions: Ambient temperatures of 10, 25 and 40 °C in an ESPEC LU-114 thermal chamber; voltage window 2.5-4.2 V
- Degradation Markers: None (fresh cells; capacity and ohmic resistance spread across the batch reported)

## Keyword Context

- [[battery-dataset|Battery Dataset]]: The paper's main output is a public Mendeley dataset of raw (.xlsx) and processed (.mat) test data for eleven CALB L148N58A cells at three temperatures.
- [[cell-to-cell-variation|Cell-to-Cell Variation]]: The campaign aims to identify the distribution of post-manufacturing capacity and impedance variations within the batch of fresh prismatic cells.
- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]: EIS was measured with a Gamry 3000AE integrated with the Arbin cycler at four SOC levels for each cell and temperature.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To provide a comprehensive characterization and driving-cycle dataset for eleven fresh CALB L148N58A cells that captures cell-to-cell variation and supports model development and BMS validation; approach: Experimental

> Evidence: "The comprehensive experimental campaign aims to identify the distribution of post-manufacturing cell-to-cell variations in terms of capacity and impedance within a batch of fresh prismatic cells."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: assess capacity and impedance spread of a fresh batch and generate data for model development and validation of estimation/control strategies; tests: C/4 CCCV conditioning, C/20 CC discharge and CCCV charge, HPPC with 1C and C/3 discharge pulses at 10 SOC steps, concatenated WLTP, UDDS and US06 driving cycles (peak current scaled to 1C; initial SOC ~100%, 80%, 60%), EIS (0.01 Hz-3 kHz) at 20/40/60/80% SOC, all repeated at 10, 25 and 40 °C on eleven cells; data origin: Own experiments

> Evidence: "The experimental process for the 11 cells is divided into four main sections, namely C/20, HPPC, driving cycles and EIS"

### Q3: Ambient Boundary Conditions

**Answer:** 10, 25 and 40 °C via an ESPEC LU-114 thermal chamber (chamber ambient temperature logged by a T-type thermocouple); stability/tolerance: not reported

> Evidence: "The ESPEC LU-114 thermal chamber maintains the experimental ambient temperature at the designated target."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** T-type thermocouple(s) on the cell surface (count per cell not stated; an additional thermocouple measures chamber ambient temperature), logged by the Arbin cycler/DAQ as Aux_Temperature_1; attachment: not reported; sampling: not reported

> Evidence: "is equipped with T-type thermocouples to measure the ambient temperature as well as the surface temperature of each cell"

### Q6: Temperature-Dependent Performance

**Answer:** At 10, 25 and 40 °C, the median C/20 discharge capacity of the batch increased with rising temperature while the capacity spread was larger at low temperature; HPPC-derived discharge ohmic resistance was higher at lower temperatures, with a slight decrease and then slight increase with rising SOC at all temperatures

> Evidence: "As expected, the median capacity value increases as the temperature rises, while the range is larger at low temperatures"

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
