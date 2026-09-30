---
cell_target: "Samsung SDI ICR18650-22P"
doi: "https://doi.org/10.1109/access.2025.3564072"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Charge Estimation"
  - "Second-Life Batteries"
  - "Machine Learning"
---

# Self SOC Estimation for Second-Life Lithium-Ion Batteries

## General Analysis

**Core Thesis:** The paper proposes a two-layer random forest system that first identifies the capacity curve of a second-life Samsung ICR18650-22P cell and then estimates its SOC with a capacity-specific model, without prior knowledge of cell history. Trained on 18 and tested on 82 own discharge experiments (1450-2300 mAh cells), it reaches about 45 mAh capacity RMSE and below 0.87% SOC RMSE offline, and is deployed on a Raspberry Pi for 15 real-time experiments.

**Methodological Focus**
- Testing Mode: CC-CV charging and constant-current (resistive load) full discharge of second-life cells with 1 s data logging; offline and real-time SOC inference
- Operating Conditions: CC-CV charge at 0.7C to 4210 mV; discharge through a constant load; cell capacities 1400-2300 mAh; ambient temperature not stated
- Degradation Markers: Reduced capacity of second-life cells (1450-2300 mAh range) used as input, no aging tracked

## Keyword Context

- [[state-of-charge-estimation|State-of-Charge Estimation]]: SOC of each discharged cell is estimated by capacity-specific random forest models and compared against Coulomb-counting reference SOC.
- [[second-life-batteries|Second-Life Batteries]]: The method targets second-life 18650 cells with different capacities and ages where traditional hard-programmed BMS thresholds fail.
- [[machine-learning|Machine Learning]]: A first random forest predicts cell capacity from voltage, current and accumulated capacity, and ten second-layer random forests (35 estimators each) estimate SOC.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To estimate the SOC of second-life lithium-ion cells independent of capacity or age using two random forest layers (capacity identification, then SOC estimation), implemented in real time on a Raspberry Pi; approach: Hybrid

> Evidence: "This work presents a system consisting of two Machine Learning (ML) layers to automatically estimate the state of charge (SOC) of SLB independent of the battery’s capacity or age."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: collect discharge data of second-life cells with different capacities to train/test the ML models and to validate real-time inference; tests: CC-CV charging (0.7C to 4210 mV) followed by constant-current discharge through a load for 100 cells (offline dataset) and 15 cells (online Raspberry Pi tests), logging voltage, current and accumulated capacity every second; data origin: Own experiments

> Evidence: "In the Raspberry, fifteen experiments with 18650 cells (see the configuration in Table 2) have been carried out"

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

**Answer:** Purpose: predict the cell capacity curve and instantaneous SOC of second-life cells; type: data-driven two-layer random forest (one capacity model, ten capacity-specific SOC models); thermal component: No

> Evidence: "A single Random Forest (RF) model was created in Phase I, and ten RF models were built and trained in Phase II."

### Q9: Model Parameterization and Validation

**Answer:** Parameters from random forest training (35 estimators) on 18 own discharge experiments (two cells per capacity class); validated on 82 own offline experiments (capacity RMSE about 45.08 mAh; SOC RMSE mean 0.85%) against Coulomb-counting reference SOC, and on 15 real-time experiments (capacity RMSE 79.94 mAh, SOC RMSE 1.8%)

> Evidence: "A Coulomb counting was used to calculate the real SOC of the cells to compare and evaluate the ML models."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: discharge of Samsung ICR18650-22P second-life cells with capacities between about 1400/1450 and 2300 mAh, discharging process only; explicitly reported limitations: real-time errors higher than offline (attributed to training-set size and input noise), and the method was built and tested for a specific type of SLB

> Evidence: "The proposed idea has been built, trained, and tested for a specific type of SLB."
