---
cell_target: "Molicel INR-21700-P42A"
doi: "https://doi.org/10.1038/s41597-025-05725-y"
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

# High-power lithium-ion battery characterization dataset for stochastic battery modeling

## General Analysis

**Core Thesis:** The paper presents an open-source characterization dataset of high-power Molicel INR-21700-P42A NMC/Si-graphite cells to support stochastic battery modelling. 45 cells are screened at 25 °C and 12 selected cells undergo capacity tests, high C-rate pulse tests with GITT (up to 8C) and EIS at 5, 25 and 40 °C, revealing temperature effects on capacity and resistance and cell-to-cell variability.

**Methodological Focus**
- Testing Mode: Capacity tests (CC discharge / CCCV charge at C/3, C/10, C/20), HPPC-inspired high C-rate pulse with GITT test (C/2 to 8C), EIS (10 mHz-10 kHz), cell screening with 1C pulses
- Operating Conditions: Screening at 25 °C; characterization at 5 °C, 25 °C and 40 °C in a thermal chamber; voltage window 2.5-4.2 V; pulses at 15-95% SoC; EIS at 20%, 50%, 80% SoC
- Degradation Markers: None (no aging cycling); C/3 capacity change between screening and CDT of -4.25% to +0.66%

## Keyword Context

- [[battery-dataset|Battery Dataset]]: The paper is a data descriptor releasing raw CSV/XLSX screening, capacity, pulse and EIS data of Molicel P42A cells on OSF.
- [[cell-to-cell-variation|Cell-to-Cell Variation]]: Ten near-mean and two outlier cells were selected from 45 screened cells, and capacity and resistance spreads across cells are analysed to enable stochastic modelling.
- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]: EIS at three temperatures and three SoCs shows impedance curves shrinking with increasing temperature and a distribution of high-frequency resistance R0 across cells.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To provide a characterization dataset of 12 high-power Molicel INR-21700-P42A cells (capacity, high C-rate pulse and impedance tests at three temperatures) capturing cell-to-cell variation for stochastic battery modelling; approach: Experimental

> Evidence: "we present a characterization dataset of 12 high-power NMC cells which includes capacity tests, high C-rate pulse tests, and impedance tests"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: generate a public high-power characterization dataset with cell-to-cell variation; tests: Phase 1 screening of 45 cells at 25 °C (C/3 discharge with 1C pulses at 80/50/20% SoC); Phase 2 on 12 cells: constant discharging test (C/3, C/10, C/20), high C-rate pulse with GITT test (C/2, 1C, 2C, 3C, 6C, 8C), and EIS at 20/50/80% SoC, each at 5, 25 and 40 °C; data origin: Own experiments

> Evidence: "For characterization, three tests are performed namely Constant discharging test (CDT), High C-rate pulse with GITT test (HCGT) and Electrochemical Impedance Spectroscopy (EIS)."

### Q3: Ambient Boundary Conditions

**Answer:** 5, 25 and 40 °C via Amerex IC500R thermal chamber (Phase 1 screening at 25 °C in an AES thermal chamber); stability/tolerance: during 5 °C EIS about 20% of tests recorded 8-10 °C, afterwards chamber stabilized between 5-7 °C

> Evidence: "inadequate regulation led to recorded temperatures in the range of 8-10 °C. After the issue was addressed, temperature control was significantly improved"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Cell surface temperature recorded (Aux_Temperature column in CDT and HCGT files); sensor type, count, location and attachment not reported; sampling: not reported for temperature (0.01 s for pulse voltage/current)

> Evidence: "and ’ Aux_Temperature(°C)’ columns representing the test time, voltage, current, and cell surface temperature, respectively."

### Q6: Temperature-Dependent Performance

**Answer:** At 25 °C cells show higher average discharge capacity (about 3.9 Ah) than at 5 °C and 40 °C (about 3.8 Ah); EIS curves shrink as temperature increases (largest semicircles at 5 °C); 5 °C pulse resistances are consistently higher and more spread than at 25 °C and 40 °C

> Evidence: "5 °C resistance box plots are consistently higher than at other two temperatures, but the spread and resistance value decreases as C-rate increases."

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
