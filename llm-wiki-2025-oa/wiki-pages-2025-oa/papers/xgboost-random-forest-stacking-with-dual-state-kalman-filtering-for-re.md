---
cell_target: "Samsung SDI INR18650-25R"
doi: "https://doi.org/10.1016/j.rineng.2025.106428"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Charge Estimation"
  - "Machine Learning"
  - "Battery Management System"
---

# XGBoost–random forest stacking with dual-state Kalman filtering for real-time battery SOC estimation

## General Analysis

**Core Thesis:** The paper proposes HEAD-KF, which fuses XGBoost and random-forest SOC predictions by non-negative ridge stacking and smooths them with an adaptively tuned dual-state Kalman filter, for real-time SOC estimation on low-cost e-bike BMS hardware. It is trained and validated on own charge-discharge and field data from a 20S1P pack of Samsung INR18650-25R (NCA) cells and runs on a Raspberry Pi 4 in about 6 ms per update.

**Methodological Focus**
- Testing Mode: Charge-discharge cycling of a 20S1P pack and e-bike field testing with BMS/Raspberry Pi data logging
- Operating Conditions: Standardized charge-discharge cycles at varying temperatures simulating urban e-bike profiles (numeric temperature values not recoverable from the text); data logged at 1 Hz
- Degradation Markers: None

## Keyword Context

- [[state-of-charge-estimation|State-of-Charge Estimation]]: Pack SOC is estimated from voltage, filtered current and voltage derivative, with reference labels reconstructed by coulomb counting with OCV resets.
- [[machine-learning|Machine Learning]]: XGBoost and random forest regressors (200 trees each) are stacked by constrained ridge regression and benchmarked against SVR, LightGBM and LSTM.
- [[battery-management-system|Battery Management System]]: The estimator is deployed on a Raspberry Pi 4 interfaced with an ANT BMS 24S, targeting the latency and power budgets of embedded e-bike BMS hardware.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To develop and validate a low-latency hybrid ensemble plus adaptive Kalman filter SOC estimator for embedded e-bike BMS using a Samsung INR18650-25R pack; approach: Hybrid

> Evidence: "This novel approach also validates the performance of HEAD-KF on a commercial e-bike"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: acquire training and validation data for SOC estimators and benchmark accuracy, latency and power on hardware; tests: standardized charge-discharge cycles at varying temperatures, e-bike field riding on varied routes, charge and discharge segments, synthetic noise/drift injection and covariance-perturbation replays on the recorded data; data origin: Own experiments

> Evidence: "The battery pack underwent standardized charge-discharge cycles at varying temperatures of"

### Q3: Ambient Boundary Conditions

**Answer:** Multiple temperatures (numeric values not recoverable from the text) via not reported control method; field tests at varying ambient temperatures; stability/tolerance: not reported

> Evidence: "This unseen slice contains complete voltage–current traces gathered on varied routes and in ambient temperatures from"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** BMS temperature sensors (type and count not stated) on the pack; attachment: not reported; sampling: 1 Hz

> Evidence: "It begins with raw voltage, current, and temperature data acquisition at 1 Hz from the battery management system"

### Q6: Temperature-Dependent Performance

**Answer:** Across the tested temperature range (values not recoverable from the text), the authors attribute RC-EKF mid-plateau drift to temperature-dependent impedance changes; HEAD-KF MAE increased only modestly at the lower temperature bound while LSTM error grew more strongly

> Evidence: "Temperature-dependent impedance changes further violate the constant-parameter assumption of the RC model"

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: real-time prediction of SOC; type: data-driven ensemble (XGBoost and random forest fused by non-negative ridge stacking) with a dual-state linear Kalman filter with adaptive covariances; baselines coulomb counting, fourth-order RC EKF, SVR, LightGBM, LSTM; thermal component: No

> Evidence: "fuses Extreme Gradient Boosting and Random-Forest regressors through non-negative ridge stacking and smooths the fused output with a dual-state Kalman filter"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from training on the authors' own 141,872-sample pack dataset with reference SOC from coulomb counting with temperature-compensated capacity-fade correction and OCV resets; hyperparameters by nested time-series cross-validation (Bayesian optimization for SVR, PSO for XGBoost); Kalman covariances adapted online from residual variance; calibrated with chronological 70%/15% training/validation splits; validated against the last 15% of field data using MAE, RMSE and SMAPE (global MAE stated as 4 × 10−4 % SOC; worst-case discharge error 2.8 × 10−3 SOC)

> Evidence: "Temporal partitioning preserved causality through chronological splits (70%/15%/15%) within each temperature slice"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: fresh NCA 20S1P pack under charge, discharge and a temperature sweep, field e-bike data, noise/bias-drift injections and ±20% covariance perturbations; explicitly reported limitations: applicability to other chemistries such as LFP and to aged cells remains to be confirmed

> Evidence: "its applicability to other chemistries, such as lithium iron phosphate (LFP), and aged cells remains to be confirmed"
