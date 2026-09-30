---
cell_target: "Sony-Murata US18650VTC6"
doi: "https://doi.org/10.3390/batteries11060208"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Machine Learning"
  - "Chemistry Identification"
  - "Heat Generation"
---

# Accurate Chemistry Identification of Lithium-Ion Batteries Based on Temperature Dynamics with Machine Learning

## General Analysis

**Core Thesis:** The paper proposes a GRU-network approach that identifies lithium-ion cell chemistry (NCA-GS: Sony US18650VTC6; NCA-G; NMC-G) solely from normalized surface-temperature profiles during constant-current charge or discharge. Own ageing tests to about 75% SOH provide the data, and classification accuracies of 97.5–100% are reached, outperforming voltage-based identification at 0.2C charge.

**Methodological Focus**
- Testing Mode: 1C CC charge/discharge ageing, 0.2C CCCV/CC check-ups, GITT, surface temperature measurement under insulation
- Operating Conditions: 25 °C chamber, cells insulated with 1.5 cm styrofoam; 1C CC ageing without rest; 0.2C CCCV to 4.2 V (0.05C cutoff) and 0.2C CC discharge to 2.5 V every 25 cycles; GITT every 50 cycles
- Degradation Markers: Capacity fade (SOH down to about 75%) and internal resistance increase with age

## Keyword Context

- [[machine-learning|Machine Learning]]: A GRU network with one GRU layer and two fully connected layers classifies the three chemistry types from normalized temperature time series with 97.5–100% accuracy.
- Chemistry Identification: The approach targets identification of NCA-GS (US18650VTC6), NCA-G and NMC-G electrode chemistries without opening the cell, to support recycling and second-life use.
- [[heat-generation|Heat Generation]]: Joule and entropic heat generation produce chemistry-specific surface-temperature profiles, with the entropic contribution identified as the distinguishing factor.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To identify the electrode chemistry of lithium-ion cells, including the Sony US18650VTC6 (NCA-GS), from surface temperature dynamics under constant-current cycling using GRU networks; approach: Hybrid

> Evidence: "we propose a novel machine learning-based approach for accurate chemistry identification of the electrode materials in LIBs based on their temperature dynamics under constant current cycling"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: generate ageing temperature data for classifier training and track SOH and internal resistance; tests: 1C CC charge/discharge ageing without rest, 0.2C CCCV charge and 0.2C CC discharge check-ups every 25 cycles with 5 h rests, GITT (0.2C pulses of 2.4 min, 6 min rest) every 50 cycles, repeated until about 75% SOH on three cells per chemistry; data origin: Own experiments

> Evidence: "The ageing cycles at 1 C and the checkup cycles at 0.2 C were repeated until the cell reached about 75% SOH."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via Memmert ICP110 temperature chamber, with cells insulated by 1.5 cm styrofoam; stability/tolerance: not reported

> Evidence: "This set-up was placed inside the Memmert ICP110 temperature chamber, which provided the constant ambient temperature of 25◦C for the insulated cells"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** PT100 × 1 mid-way on the curved cell surface; attachment: placed directly on the surface and covered by 1.5 cm styrofoam insulation; sampling: not reported

> Evidence: "A PT100 temperature sensor was placed directly mid-way on the curved surface of the cylindrical cells"

### Q6: Temperature-Dependent Performance

**Answer:** At 25 °C ambient, the first 1C charge raised the NCA-GS surface temperature to 39 °C; in subsequent 1C cycles at elevated cell temperature the internal resistance is lower than at room temperature, so entropic cooling causes a mid-way temperature drop

> Evidence: "at elevated temperatures in the subsequent cycles, the cell’s internal resistance is lower than its value at room temperature"

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: classify cell chemistry type (NCA-GS, NCA-G, NMC-G) from normalized temperature-difference time series; type: data-driven GRU network (one GRU layer, two fully connected layers, softmax); thermal component: No explicit thermal model (measured temperature is the sole input)

> Evidence: "This time series of temperature differences after normalisation is the only input of the GRU models."

### Q9: Model Parameterization and Validation

**Answer:** Parameters trained on own measured temperature profiles (random 60:20:20 train/validation/test split, learning rate tuned with Optuna); validated on the test set with accuracy/precision/recall/F1: separately trained 100%, 97.5%, 100%, 100% and jointly trained 100%, 97.5%, 99.9%, 100% for 0.2C charge, 0.2C discharge, 1C charge, 1C discharge

> Evidence: "the most important hyperparameter, the learning rate, is fine-tuned using the automatic hyperparameter fine-tuning framework Optuna"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not spatially resolved (data-driven classifier using a single mid-surface temperature signal per cell); represented inhomogeneities: none

> Evidence: "A PT100 temperature sensor was placed directly mid-way on the curved surface of the cylindrical cells"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 25 °C insulated cells, 0.2C and 1C charge/discharge, SOH from 100% to about 75%, three cell types; explicitly reported limitations: training data from more manufacturers, capacities and formats needed, ambient temperature effects were ignored due to insulation, and classification may become difficult below 75% SOH

> Evidence: "The classification may also become a challenge for cells with a significant age of SOH below 75% where the irreversible heat can be so high that the temperature response may become less distinctive."
