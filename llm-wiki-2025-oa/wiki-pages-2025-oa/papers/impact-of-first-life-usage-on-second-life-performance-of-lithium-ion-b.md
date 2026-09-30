---
cell_target: "Samsung SDI INR18650-35E"
doi: "https://doi.org/10.1016/j.nxener.2025.100385"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Second-Life Batteries"
  - "Capacity Degradation"
  - "Electrochemical Impedance Spectroscopy"
---

# Impact of first-life usage on second-life performance of lithium-ion batteries

## General Analysis

**Core Thesis:** The study experimentally examines whether high- or low-current first-life cycling of retired Samsung INR18650-35E NCA cells (taken from e-bike packs) affects their subsequent second-life aging under 30% DoD cycling at 0.5C or 0.25C. Capacity, DC and AC internal resistance are tracked over 600 second-life cycles, and the measured degradation rates feed a payback analysis of four second-life BESS business cases.

**Methodological Focus**
- Testing Mode: Galvanostatic cycling (100% DoD first-life, 30% DoD second-life around 50% SoC) with periodic capacity, DCIR pulse and EIS/ACIR characterization
- Operating Conditions: Room temperature setpoint 20 °C; first life HC 1.18C discharge/0.58C charge vs LC 0.58C/0.29C at 100% DoD; second life 0.5C (1.7 A) or 0.25C (0.85 A) at 30% DoD; capacity check CC-CV 0.5C charge to 4.2 V, 0.2C discharge to 2.65 V
- Degradation Markers: Capacity fade (approx. 2% per 1,000 cycles at HC second life; 0.6% per 1,000 cycles HC-LC; capacity increase in LC-LC), ACIR and DCIR evolution, EIS spectra

## Keyword Context

- [[second-life-batteries|Second-Life Batteries]]: Retired e-bike NCA cells aged to approx. 80% SoH are cycled under stationary-storage-like partial DoD profiles to estimate remaining cycles and business-case payback.
- [[capacity-degradation|Capacity Degradation]]: Second-life capacity fade is quantified per 1,000 cycles for the HC-HC, LC-HC, HC-LC and LC-LC groups, showing no significant influence of the first-life current level under identical second-life conditions.
- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]: EIS (1 A amplitude, 45 points up to 2000 Hz) provides ACIR at 1000 Hz and spectra at first-life start, EOL and after 600 second-life cycles, compared with DCIR.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To determine how first-life cycling current (high vs low) affects second-life capacity degradation and internal resistance evolution of retired Samsung INR18650-35E NCA cells under 30% DoD cycling at two currents, and to use the results for second-life business-case estimates; approach: Experimental

> Evidence: "Specifically, we examine how first-life usage profiles influence second-life performance and longevity"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: quantify aging of NCA cells across four first-life/second-life usage patterns; tests: first-life 100% DoD cycling (HC or LC) to approx. 80% SoH, second-life 600 cycles at 30% DoD centred at 50% SoC at 0.5C or 0.25C, capacity tests, DCIR (1 A, 60 ms pulses across SoC) and ACIR/EIS characterization every 50 or 100 cycles on 12 cells in 4 groups; data origin: Own experiments

> Evidence: "The setup includes a control PC, a cell cycle tester (Arbin BT2000), and an auxiliary electrochemical impedance spectroscopy (EIS) tester (Camry)"

### Q3: Ambient Boundary Conditions

**Answer:** 20 °C (room temperature setpoint) in a temperature-controlled and insulated steel container; stability/tolerance: not quantified, some variation was observed

> Evidence: "The temperature setpoint for both cycling and characterization was room temperature (20°C), although some variation was observed during testing."

### Q4: Mechanical Boundary Conditions

**Answer:** No pressure constraint reported; magnitude: not reported; fixture: custom-designed 18650 cell holders with welded joints and 4-probe contacts

> Evidence: "The cells are securely housed in custom-designed holders for 18,650 cylindrical cells, featuring welded joints and 4-probe contacts"

### Q5: Cell Temperature Measurement

**Answer:** Thermocouple × 1 per cell at the centre of each cell; attachment: attached (method not specified); sampling: not reported

> Evidence: "A thermocouple is attached to the center of each cell to enable continuous temperature monitoring."

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
