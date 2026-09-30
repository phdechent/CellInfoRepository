---
cell_target: "Samsung SDI INR21700-50G"
doi: "https://doi.org/10.3390/batteries11080313"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Hybrid Pulse Power Characterization"
  - "Parameter Identification"
  - "Multi-Temperature Evaluation"
---

# Systematic Characterization of Lithium-Ion Cells for Electric Mobility and Grid Storage: A Case Study on Samsung INR21700-50G

## General Analysis

**Core Thesis:** The paper characterizes the Samsung INR21700-50G cell with static capacity and multi-duration HPPC tests from −10 °C to 45 °C at 0.2C and 1C, deriving OCV, DCIR, pulse power capability maps (fish charts) and second-order RC equivalent-circuit parameters as functions of SOC and temperature. A weakly coupled electro-thermal model with a two-node lumped thermal network is presented to support real-time BMS use.

**Methodological Focus**
- Testing Mode: Static capacity tests; HPPC with 1C (and 0.2C) discharge/charge pulses of 2 s, 10 s, 30 s and 180 s at 5% SOC steps; CC-CV charging at C/2 to 4.2 V
- Operating Conditions: −10, 0, 10, 20, 30 and 45 °C in a temperature chamber; 0.2C and 1C
- Degradation Markers: None

## Keyword Context

- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]: Multi-duration HPPC tests provide OCV, DCIR, discharge and regenerative power capability and the voltage responses used for ECM fitting.
- [[parameter-identification|Parameter Identification]]: R0 is taken from the instantaneous voltage drop and R1, R2, C1, C2 are fitted to HPPC voltage responses with MATLAB fminsearch at every SOC and temperature.
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]: All capacity, OCV, resistance, power and parameter results are compared across six test temperatures from −10 °C to 45 °C.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study provides a systematic electrical and thermal characterization of the Samsung INR21700-50G cell and a second-order ECM with a weakly coupled lumped thermal model parameterized from HPPC data across temperature and SOC; approach: Hybrid

> Evidence: "This work presents a detailed characterization of the Samsung INR21700-50G lithium-ion cell for electric mobility and grid storage applications."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: obtain capacity, OCV, DCIR, power capability and ECM parameter data over temperature and SOC for BMS design; tests: preconditioning soak at 30 °C, CC-CV charge at C/2 to 4.2 V with 50 mA cutoff and at least 1 h rest; static capacity discharge at 0.2C and 1C; HPPC with discharge, charge and SOC-reset pulses of 2 s, 10 s, 30 s and 180 s at every 5% SOC with 1–2 h rests, one iteration per condition; data origin: Own experiments

> Evidence: "Each pulse duration starts at 2 s, with subsequent sequences using 10, 30, and 180 s pulses."

### Q3: Ambient Boundary Conditions

**Answer:** −10, 0, 10, 20, 30 and 45 °C via ESPEC BTX-475 temperature-controlled chamber, with ambient air temperature monitored by a second thermocouple; stability/tolerance: not reported

> Evidence: "Both static capacity and HPPC tests are performed at temperatures T∈ {− 10, 0, 10, 20, 30, 45}◦Cfor two C-rates: 0.2 C and 1 C."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Thermocouple × 1 on the cell near the center of the surface (approximately 35 mm from the top or bottom), plus one thermocouple in ambient air; attachment: attached/affixed to the surface (method not specified); sampling: not reported

> Evidence: "Thermocouple 1 is attached near the center of the cell surface to measure the cell temperature, and Thermocouple 2 is placed in the ambient air."

### Q6: Temperature-Dependent Performance

**Answer:** Between −10 °C and 45 °C: discharge voltage was highest at 30 °C and lowest at −10 °C; capacity and energy fell with lower temperature and higher rate (at −10 °C only 4434 mAh at 0.2C, about 13% below the 25 °C specification, and about 20% reduction at 1C); surface temperature rise at 1C was larger at lower ambient temperature; OCV deviated −0.21% to −0.73% (SOC > 30%) and up to −4.80% at low SOC at −10 °C versus 30 °C; DCIR, R0 and R2 increased at low temperature and τ2 increased as temperature decreased; discharge and regenerative power capability were highest at 30 °C and 45 °C and severely reduced at −10 °C

> Evidence: "For the extreme case of −10◦C, only 4434 mAh could be extracted at 0.2 C."

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: predict terminal voltage, temperature and heat generation for real-time BMS state estimation, thermal control and power prediction; type: second-order RC equivalent circuit model weakly (sequentially) coupled to a two-node core/surface lumped thermal network, with a 3D lookup table in SOC and mean temperature; thermal component: Yes

> Evidence: "A weakly coupled electro-thermal model is presented to support real-time BMS applications"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from the authors' own HPPC data: OCV from the rested voltage before each pulse, R0 from the instantaneous voltage drop, and R1, R2, C1, C2 from least-squares fitting of the pulse voltage response with MATLAB fminsearch, averaged over the four pulse durations for each SOC and temperature; calibrated with 0.2C and 1C HPPC data at −10 to 45 °C; validated against the measured HPPC voltage via curve-fitting metrics (e.g., 1C: MAE 0.032 V, RMSE 0.038 V, MAPE 0.876% at −10 °C; MAE 0.007 V, RMSE 0.009 V, MAPE 0.198% at 45 °C); thermal-model parameter values and thermal validation are not reported

> Evidence: "MATLAB 2024a’s fminsearch function was used to solve this optimization problem for the parameters."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (electrical ECM plus two-node thermal network); represented inhomogeneities: core versus surface temperature only

> Evidence: "The lumped capacitance model used in this work represents the cell with two thermal nodes-core and surface, each associated with a distinct temperature."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: −10 °C to 45 °C, 0.2C and 1C HPPC pulses of 2–180 s, SOC from 100% down to the 2.5 V cutoff (tests at −10 °C terminated early before about 15–20% SOC), fresh cell; explicitly reported limitations: the two-node lumped thermal model neglects finer internal temperature gradients during high-rate operation and localized degradation effects; only one HPPC iteration was performed; the 1 h rest may not reach full OCV equilibrium, especially at low temperature; fitting accuracy decreases at lower temperatures; aged cells and high-power cycling are left for future work

> Evidence: "neglecting finer internal temperature gradients that may develop during a high charge/discharge scenario"
