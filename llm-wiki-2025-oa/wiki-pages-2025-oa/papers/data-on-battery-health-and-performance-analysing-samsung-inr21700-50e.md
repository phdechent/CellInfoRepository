---
cell_target: "Samsung SDI INR21700-50E"
doi: "https://doi.org/10.1016/j.dib.2025.111346"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Battery Dataset"
  - "Hybrid Pulse Power Characterization"
  - "Machine Learning"
---

# Data on battery health and performance: Analysing Samsung INR21700-50E cells with advanced feature engineering

## General Analysis

**Core Thesis:** The data article publishes raw time-series and engineered features from charge-discharge and HPPC tests on 256 Samsung INR21700-50E cells in 32 batches, measured at 25 °C at the University of Wuppertal. Engineered features such as SoH, internal and dynamic resistance, capacity fade rate and temperature metrics are provided, and their benefit is illustrated with Linear Regression and Random Forest models.

**Methodological Focus**
- Testing Mode: CC/CV charge at C/2 (98 mA cutoff), C/5 discharge to 2.5 V, HPPC with micro-HPPC at every 10 % SOC step from 100 % to 10 % plus 0 % SOC
- Operating Conditions: 25 °C in a climate chamber; recording at 100 Hz (charge/discharge) and 1 kHz (HPPC)
- Degradation Markers: Capacity fade rate, SoH, internal resistance, dynamic resistance (engineered features)

## Keyword Context

- [[battery-dataset|Battery Dataset]]: The paper releases a Zenodo dataset (10.5281/zenodo.13730404) of voltage, current, power and temperature time series from 256 INR21700-50E cells organised by batch and cell in CSV format.
- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]: HPPC tests integrated into the discharge process, recorded at 1 kHz, are the primary source for the resistance and power features in the dataset.
- [[machine-learning|Machine Learning]]: Linear Regression and Random Forest models trained on original versus engineered features show reduced MAE, MSE and MAPE with engineered features at stable R² scores.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To provide a public dataset of measured charge-discharge and HPPC data with engineered health features for INR21700-50E cells to support degradation analysis and predictive modelling; approach: Experimental (with supporting machine-learning demonstration)

> Evidence: "The primary motivation for compiling this dataset is to study the degradation patterns and performance characteristics of lithium-ion batteries, particularly the Samsung INR21700-50E model."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: characterize performance and health of 256 INR21700-50E cells for a public dataset; tests: CC/CV charge at C/2 with 98 mA cutoff, rest, C/5 discharge to 2.5 V, rest to thermal equilibrium, HPPC at multiple stages with micro-HPPC every 10 % SOC from 100 % to 10 % and a final HPPC at 0 % SOC; data origin: Own experiments

> Evidence: "The data were collected using standardized charge–discharge protocols and HPPC tests on Samsung INR21700-50E cells."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via a climate/thermal chamber, with cells equilibrated before testing; stability/tolerance: not reported

> Evidence: "These tests were performed in a climate chamber maintained at a consistent temperature of 25 °C to ensure thermal equilibrium."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Cell temperature (Temp_Cell, described as internal cell temperature) and ambient temperature were recorded; sensor type, count, placement and attachment: not reported; sampling: 100 Hz for charge/discharge cycles and 1 kHz for HPPC tests

> Evidence: "All cycles were recorded at 100 Hz for standard charge/discharge cycles and 1 kHz for the HPPC tests"

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: demonstrate the predictive value of engineered features for SOH and capacity degradation; type: data-driven (Linear Regression and Random Forest); thermal component: No

> Evidence: "two models—Linear Regression and Random Forest—were trained using both the original and engineered feature sets."

### Q9: Model Parameterization and Validation

**Answer:** Parameters learned from the own INR21700-50E dataset (original vs. engineered features) with cross-validation; validated with MAE, MSE, MAPE and R² on charging and discharging cycles and additionally on an external forklift operation profile dataset

> Evidence: "To guard against this, cross-validation techniques were employed, and consistent R² scores across folds were observed."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 25 °C charge-discharge and HPPC data plus a forklift operation profile dataset; explicitly reported limitations: scalability and adaptation to other chemistries or varying operating conditions may require further validation; harsh-temperature tests are planned

> Evidence: "Nonetheless, scalability and adaptation to other battery chemistries or varying operating conditions might require further validation and improvement of these designed features."
