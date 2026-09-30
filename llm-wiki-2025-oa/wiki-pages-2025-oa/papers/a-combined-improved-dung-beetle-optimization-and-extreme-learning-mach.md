---
cell_target: "LG Chem 18650HG2; Panasonic NCR18650PF"
doi: "https://doi.org/10.1038/s41598-025-00482-9"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Charge Estimation"
  - "Metaheuristic Optimization"
  - "Multi-Temperature Evaluation"
---

# A combined improved dung beetle optimization and extreme learning machine framework for precise SOC estimation

## General Analysis

**Core Thesis:** The paper proposes an Improved Dung Beetle Optimizer (Circle chaotic mapping, golden sine strategy, Levy flight) to set the input weights and hidden biases of an Extreme Learning Machine for SOC estimation. The IDBO-ELM is evaluated on drive-cycle data of LG 18650HG2 and Panasonic 18650PF cells across ambient temperatures, driving conditions, initial SOC values and running time, reaching MAE and RMSE around 1.4%.

**Methodological Focus**
- Testing Mode: Drive-cycle discharge tests (UDDS, US06, HWFET) on a battery test system in a thermal chamber; data-driven SOC estimation
- Operating Conditions: Tests at –20, 0, 10 and 25 °C (LG training set stated as –20, –10, 0, 10, 25 and 40 °C); initial SOC 100%, 80% and 50%
- Degradation Markers: None

## Keyword Context

- [[state-of-charge-estimation|State-of-Charge Estimation]]: SOC of the two 18650 cells is estimated by the IDBO-ELM and benchmarked against ELM, LSTM, CNN-LSTM and DBO-ELM using MAE, RMSE and R2.
- Metaheuristic Optimization: An improved dung beetle optimizer with Circle chaotic mapping, golden sine and Levy flight strategies tunes the ELM input weights and hidden biases.
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]: The model is trained on LG 18650HG2 data from six ambient temperatures and tested at –20 °C, 0 °C and 25 °C, and additionally on Pan18650 data at different temperatures.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To develop and validate an IDBO-optimized extreme learning machine for accurate SOC estimation of LG 18650HG2 and Panasonic 18650PF cells under different temperatures, driving cycles, battery materials and initial SOC values; approach: Hybrid

> Evidence: "The proposed IDBO-ELM method is validated in the context of five parameters, namely, different ambient temperatures, operating conditions, battery materials, initial SOC values, and running time."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: generate charge/discharge data under realistic EV driving profiles for training and testing the SOC estimator; tests: UDDS, US06 and HWFET drive-cycle tests on LG 18650HG2 (3.0 Ah) and Pan 18650PF (2.9 Ah) cells using a NEWARE battery test system and a thermal chamber; data origin: Own experiments

> Evidence: "three different test curves were used, including UDDS, US06, and HWFET curves"

### Q3: Ambient Boundary Conditions

**Answer:** –20, 0, 10 and 25 °C via thermal chamber (the LG training set is described as combining –20, –10, 0, 10, 25 and 40 °C); stability/tolerance: not reported

> Evidence: "Experiments were conducted at temperatures of –20 °C, 0 °C, 10 °C, and 25 °C."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Battery temperature was recorded by the thermal chamber; sensor type, count, placement, attachment and sampling rate not reported

> Evidence: "The thermal chamber played a dual role by modulating the temperature and concurrently recording the battery temperature."

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: prediction of SOC from measured battery data; type: data-driven single-hidden-layer extreme learning machine with IDBO hyperparameter (weights/biases) optimization; thermal component: No

> Evidence: "It is combined with the ELM model to optimize the input weights and hidden biases of the ELM network, forming the IDBO-ELM model."

### Q9: Model Parameterization and Validation

**Answer:** Parameters (ELM input weights and hidden biases) from IDBO numerical optimization; calibrated with own LG 18650HG2 data combining six ambient temperatures (normalized to 0–1); validated against UDDS, US06 and HWFET test sets with Coulomb-counting reference SOC using MAE, RMSE and R2 (e.g. UDDS RMSE 0.0135, 0.0120 and 0.0128 at –20, 0 and 25 °C)

> Evidence: "The training set combines data from six ambient temperatures: –20 °C, –10 °C, 0 °C, 10 °C, 25 °C and 40 °C."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: –20 °C to 40 °C, UDDS/US06/HWFET profiles, initial SOC 100%, 80% and 50%, two cell types (LG 18650HG2 and Pan 18650PF); explicitly reported limitations: aging conditions and SOH–SOC coupling not considered, larger errors below 0.1 SOC due to polarization, and longer running time than plain ELM

> Evidence: "However, varying aging conditions could influence SOC estimation, and the subsequent coupling characteristics of SOH and SOC should be taken into account"
