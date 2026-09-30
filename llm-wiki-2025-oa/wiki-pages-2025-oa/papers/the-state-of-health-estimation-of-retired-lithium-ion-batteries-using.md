---
cell_target: "Panasonic NCR18650BD; Samsung SDI ICR18650-26F"
doi: "https://doi.org/10.3390/en18051035"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Health Estimation"
  - "Second-Life Batteries"
  - "Machine Learning"
---

# The State of Health Estimation of Retired Lithium-Ion Batteries Using a Multi-Input Metabolic Gated Recurrent Unit

## General Analysis

**Core Thesis:** The paper proposes a multi-input metabolic gated recurrent unit (MM-GRU) that estimates the SoH of retired lithium-ion cells and packs from constant-current charging time, charging current area and the 1800 s discharge voltage drop, using a sliding window of four cycles. It is validated on retired Samsung ICR18650-26F cells, six-cell Samsung packs and retired Panasonic NCR18650BD cells aged under constant-current and dynamic energy-storage discharge scenarios.

**Methodological Focus**
- Testing Mode: Galvanostatic cycle aging with CC-CV charging and scenario-based discharge (constant 0.5C or dynamic 0.2C–1C steps), with 0.2C capacity measurement each cycle
- Operating Conditions: 24 °C in an environmental test chamber; 0.5C CC-CV charge to 4.2 V; Condition 1: 0.5C constant-current discharge; Condition 2: 0.2C/0.5C/1C/0.75C/0.2C steps of 5 min; about 100 cycles
- Degradation Markers: Capacity fade (SoH), constant-current charging time, charging current area, discharge voltage drop

## Keyword Context

- [[state-of-health-estimation|State-of-Health Estimation]]: SoH, defined as estimated capacity over nominal capacity, is estimated with the MM-GRU and compared with SVM, BPNN and GRU using Max AE, MAE and RMSE.
- [[second-life-batteries|Second-Life Batteries]]: The tested cells are retired batteries (131 Samsung and 34 Panasonic cells deemed suitable after screening) intended for secondary use in household energy storage.
- [[machine-learning|Machine Learning]]: A GRU network with a metabolic mechanism that replaces the oldest health-indicator set with the newest one is trained on data from a single battery and applied to others.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study aims to accurately estimate the SoH of retired lithium-ion cells and packs under different energy-storage operating conditions with minimal historical data using an MM-GRU model trained on own aging data; approach: Hybrid

> Evidence: "It requires only four cycles of historical data to reliably predict the SoH of subsequent cycles."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: obtain aging data of retired cells and packs under typical household energy-storage discharge scenarios for SoH model training and validation; tests: initial 0.2C discharge, 0.5C CC-CV charging, discharge by Scenario 1 (0.5C constant current) or Scenario 2 (dynamic 0.2C/0.5C/1C/0.75C/0.2C, 5 min each), 0.2C capacity measurement, repeated for 101 cycles, on selected Samsung cells, four six-cell series Samsung packs and selected Panasonic cells after a clustering experiment; data origin: Own experiments

> Evidence: "Repeat steps (1) to (3) until 101 cycles of energy storage scenario tests are completed."

### Q3: Ambient Boundary Conditions

**Answer:** 24 °C via an environmental test chamber; stability/tolerance: not reported

> Evidence: "Set the temperature in the environmental test chamber to 24 °C."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: estimate capacity and SoH of retired cells and packs for subsequent cycles; type: data-driven multi-input metabolic gated recurrent unit (MM-GRU) with a metabolic window of four cycles; thermal component: No

> Evidence: "this paper presents a highly eﬃcient estimation model based on the multi-input metabolic gated recurrent unit (MM-GRU)"

### Q9: Model Parameterization and Validation

**Answer:** Parameters (network weights) learned offline from the authors' own aging data of a single training battery or pack (e.g., D23, D22, pack2, pack3, R18, R23) using constant-current charging time, charging current area and 1800 s voltage drop as inputs (voltage drop omitted for packs); validated on other own-tested cells/packs under the same and different operating conditions using Max AE, MAE and RMSE (Max AE below 3.8 %, RMSE up to about 1.2 %, MAE not exceeding 1 %) and compared with SVM, BPNN and GRU

> Evidence: "The model is trained using data from a single battery and applied to other batteries"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: retired Samsung ICR18650-26F cells, six-cell series Samsung packs and retired Panasonic NCR18650BD cells at 24 °C over about 100 cycles under Condition 1 (0.5C constant-current discharge) and Condition 2 (dynamic discharge), with 0.5C CC-CV charging; explicitly reported limitations: larger errors during sudden SoH changes or rapid capacity decline, the voltage-drop feature was not suitable for the Samsung packs, and future work is needed on larger systems with inter-cell dependencies and reduced data reliance

> Evidence: "it was found that the voltage drop feature was not suitable for the Samsung retired battery packs"
