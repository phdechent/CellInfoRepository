---
cell_target: "Samsung SDI INR21700-40T"
doi: "https://doi.org/10.3390/batteries11070236"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Health Estimation"
  - "Machine Learning"
  - "Incremental Capacity Analysis"
---

# Machine Learning-Based Methodology for Fast Assessment of Battery Health Status

## General Analysis

**Core Thesis:** The study proposes an RNN-based method to estimate the static capacity of aged Samsung INR21700-40T cells from only 6 min of 1C constant-current partial discharge data, to speed up health assessment for battery reuse and recycling. Using data from five cells aged over up to 1000 cycles, the model reached an average RMSE of 28.439 mAh and R² of 0.9993.

**Methodological Focus**
- Testing Mode: Accelerated aging by 2C CC charge/discharge with periodic segmented 1C partial discharges, DCIR and capacity measurements
- Operating Conditions: Room temperature (no numeric value); 2C CC aging cycles; 6-min 1C partial discharges at every 10% SOC decrement with 1 h rests; 0-1000 cycles; cut-off 4.2 V / 2.5 V
- Degradation Markers: Capacity fade (SOH decline), DCIR measured

## Keyword Context

- [[state-of-health-estimation|State-of-Health Estimation]]: The static capacity (SOH) of aged cells is the quantity estimated from short partial discharge data.
- [[machine-learning|Machine Learning]]: A recurrent neural network built in MATLAB 2024a is trained on time-series features from 6-min partial discharges.
- [[incremental-capacity-analysis|Incremental Capacity Analysis]]: Features are derived from ICA and DVA concepts, using voltage change and capacity change over the partial discharge period.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To enable rapid and reliable static capacity estimation of used Samsung INR21700-40T cells from 6-min 1C partial discharge data using an RNN; approach: Hybrid

> Evidence: "accurate static capacity estimation is possible using only short-term partial discharge data (6 min under 1C-rate CC conditions)"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: acquire training/validation data covering various aging degrees; tests: segmented discharge with DCIR and partial voltage measurement at every 10% SOC decrement (1 h rests), discharge/charge capacity measurement, accelerated aging with 2C CC charge/discharge up to 100 cycles per loop until SOH < 80% (0-1000 cycles); data origin: Own experiments

> Evidence: "the DCIR and partial voltage values are measured at every 10% decrement in SOC"

### Q3: Ambient Boundary Conditions

**Answer:** Room temperature (no numeric value stated) via not reported control method; stability/tolerance: not reported

> Evidence: "the experimental data were collected and aged only under room temperature (RT) conditions"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: prediction of static capacity (SOH); type: data-driven recurrent neural network (RNN); thermal component: No

> Evidence: "This study employed recurrent neural networks (RNNs) for processing time-series data derived from partial discharge measurements."

### Q9: Model Parameterization and Validation

**Answer:** Parameters from training on the author's own partial-discharge data (min-max normalized ICA/DVA-derived features); calibrated with data from three cells for training and one for validation; validated against one held-out test cell over 50 iterations using RMSE, MSE, MAE and R² (average RMSE 28.439 mAh, R² 0.9993)

> Evidence: "Data from three samples were used for training, one sample was used for validation, and one sample was reserved for testing."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 6-min 1C partial discharges from all SOC intervals over 0-1000 aging cycles at room temperature on five cells; explicitly reported limitations: data collected and aged only at room temperature, limiting applicability; imbalanced data distribution during aging can cause overestimation in certain aging cycles

> Evidence: "the imbalanced data distribution during the battery aging process can increase estimation errors in certain aging cycles, leading to overestimation"
