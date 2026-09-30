---
cell_target: "Samsung SDI ICR18650-26F"
doi: "https://doi.org/10.3390/en18051037"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Health Estimation"
  - "Machine Learning"
  - "Online Parameter Identification"
---

# A Novel Online State-of-Health Estimation Method for Lithium-Ion Batteries with Multi-Input Metabolic Long Short-Term Memory Framework

## General Analysis

**Core Thesis:** The paper proposes a multi-input metabolic LSTM (MM-LSTM) framework for online SoH estimation that uses capacity degradation, discharge-voltage sample entropy and ohmic-resistance increment as inputs. It is trained and validated on the authors’ own aging data from four Samsung ICR18650-26F (LCO) cells and one Panasonic NCR18650B cell under different temperatures and dynamic profiles, achieving a maximum SoH error within 1.98 %, including transfer between cell chemistries.

**Methodological Focus**
- Testing Mode: Capacity tests and dynamic drive-profile tests (NEDC, UDDS, JP1015) as characteristic tests, plus aging cycles with dynamic profiles (mixed dynamic current, NEDC with 2C pulses, UDDS)
- Operating Conditions: Characteristic tests at 10, 25 and 40 °C (S42/S43), 35 °C (S30) and 25 °C (S17, P01); aging at 45 °C (S42/S43, S17, P01) and 35 °C (S30); 1 Hz data sampling; environmental chamber
- Degradation Markers: Capacity degradation (SoH), ohmic internal resistance increment ΔR, discharge-voltage sample entropy

## Keyword Context

- [[state-of-health-estimation|State-of-Health Estimation]]: SoH (current capacity relative to rated capacity) of the ICR18650-26F cells is estimated until capacity loss reaches the 20 % cut-off criterion, with Max AE below 1.66 % for same-type training.
- [[machine-learning|Machine Learning]]: An LSTM-based degradation state model with metabolic input updating, initialized with four cycles of history, is compared with plain LSTM, GPR and SVM.
- [[online-parameter-identification|Online Parameter Identification]]: The ohmic resistance R0 of a Thevenin model is identified in real time under dynamic loading by FFRLS (forgetting factor 0.95) and smoothed by variational mode decomposition to form the ΔR indicator.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To develop and validate an online SoH estimation framework (MM-LSTM) that transfers across operating conditions and cell types using own aging data from ICR18650-26F cells; approach: Hybrid

> Evidence: "To solve the issue, in this article, a novel multi-input metabolic long short-term memory (MM-LSTM) framework is developed."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: generate degradation data for training and validating the SoH estimator; tests: repeated test cycles of characteristic tests (capacity test and NEDC/UDDS/JP1015 dynamic tests) and aging tests (S42/S43: mixed dynamic current at 45 °C; S30: NEDC with 2C-rate pulses at 35 °C; S17 and P01: UDDS at 45 °C, with aging procedures repeated 10 times per test cycle for S30, S17 and P01); data origin: Own experiments

> Evidence: "A capacity test and three dynamic condition tests were among the characteristic tests."

### Q3: Ambient Boundary Conditions

**Answer:** Characteristic tests at 10, 25 and 40 °C (S42/S43), 35 °C (S30), 25 °C (S17); aging tests at 45 °C (S42, S43, S17) and 35 °C (S30), via a temperature-controlled environmental chamber; stability/tolerance: not reported

> Evidence: "the testing procedures in each test cycle included the characteristic tests at three temperatures (10◦C, 25◦C, and 40◦C) and the aging cycle tests"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** The authors state qualitatively that ohmic internal resistance is significantly influenced by ambient temperature, motivating the use of the resistance increment ΔR rather than absolute resistance; no quantitative temperature comparison is reported

> Evidence: "Meanwhile, the ohmic internal resistance is sig- nificantly influenced by ambient temperature."

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: online SoH estimation via capacity-degradation prediction; type: data-driven LSTM-based degradation state model with metabolic input updating, plus a first-order Thevenin ECM whose R0 is identified by FFRLS for the ΔR indicator; thermal component: No

> Evidence: "a battery degradation state model is developed using the capacity degradation as the estimated state variable and the extracted degradation indicators as input observation variables"

### Q9: Model Parameterization and Validation

**Answer:** R0 identified in real time from own measured voltage/current under dynamic profiles by FFRLS (forgetting factor 0.95) and filtered by VMD; LSTM trained offline on own reference-cell data (S43_25 °C_NEDC, S43_25 °C_UDDS or P01_25 °C_UDDS) and initialized with four cycles of test-cell history; validated against measured SoH of S17, S30, S42 and S43 (same-type Max AE ≤ 1.66 %, MAE ≤ 0.52 %; cross-type Max AE ≤ 1.98 %, RMSE ≤ 0.64)

> Evidence: "The forgetting factor was set as 0.95."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: ICR18650-26F test data at 10, 25, 35 and 40 °C with NEDC, UDDS and JP1015 profiles, over the life until the 20 % capacity-loss cut-off; explicitly reported limitations: largest errors occur at SoH fluctuations caused by capacity recovery during experimental pauses; hardware integration and additional indicators left for future work

> Evidence: "This occurrence results in a maximum error in the estimation of SoH that corresponds to the fluctuation"
