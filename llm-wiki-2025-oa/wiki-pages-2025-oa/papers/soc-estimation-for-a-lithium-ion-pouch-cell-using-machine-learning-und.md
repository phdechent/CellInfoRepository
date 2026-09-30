---
cell_target: "A123 Systems 26AH"
doi: "https://doi.org/10.1038/s41598-025-02709-1"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Charge Estimation"
  - "Machine Learning"
  - "Extended Kalman Filter"
---

# SOC estimation for a lithium-ion pouch cell using machine learning under different load profiles

## General Analysis

**Core Thesis:** The paper compares Coulomb counting and an extended Kalman filter with linear regression, support vector regression and random forest regression for SOC estimation of a 26 Ah A123 NMC pouch cell. Data from four own load profiles (full cycle, partial cycle, WLTP-based dynamic and HPPC) are used, and random forest yields the lowest errors (RMSE 0.0229).

**Methodological Focus**
- Testing Mode: Galvanostatic CCCV full cycling, partial (20-90% SOC) shallow cycling, WLTP dynamic profile, HPPC pulse test
- Operating Conditions: 1C CCCV between 3 V and 4.2 V with C/10 cut-off; partial cycling at 1C between 20% and 90% SOC; HPPC from 100% to 10% SOC; ambient temperature not stated
- Degradation Markers: None (capacity fade not quantified)

## Keyword Context

- [[state-of-charge-estimation|State-of-Charge Estimation]]: SOC of the 26 Ah pouch cell is the target quantity estimated by all compared classical and data-driven methods.
- [[machine-learning|Machine Learning]]: Linear regression, SVR and random forest are trained on 262,469 measured data points with an 80/10/10 split, random forest achieving the lowest errors.
- Extended Kalman Filter: An EKF using an equivalent circuit model is one of the classical baselines, reaching an RMSE of 0.0925.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To compare classical (Coulomb counting, EKF) and machine-learning (linear regression, SVR, random forest) SOC estimation methods for a 26 Ah A123 NMC pouch cell under four different load profiles; approach: Hybrid

> Evidence: "we compare the accuracy and robustness of conventional approaches with those of ML models"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: generate a diverse dataset for training and evaluating SOC estimators; tests: six full CCCV cycles at 1C (3-4.2 V), 24 partial cycles at 1C between 20% and 90% SOC, WLTP-based dynamic load profile, HPPC (10 s pulses, 100% to 10% SOC in 10% steps); data origin: Own experiments

> Evidence: "subjecting a lithium-ion battery to four different load profiles utilizing a battery testing equipment"

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

**Answer:** Purpose: prediction of SOC; type: Coulomb counting, EKF with an equivalent circuit model, and data-driven linear regression, support vector regression and random forest regression; thermal component: Not stated

> Evidence: "The measurement equation h(x, u) relates SOC to terminal voltage using an equivalent circuit model (ECM)"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from ML training on the authors' 262,469 measured data points (voltage, current, SOC and derivative features), with grid search/randomized search cross-validation for hyperparameters; calibrated with 80% training / 10% validation data; validated against the 10% test set using RMSE, MSE and MAE (random forest RMSE 0.0229, MSE 0.0005, MAE 0.0139)

> Evidence: "The dataset was then divided into 80% training, 10% validation, and 10% test sets for estimation."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: full-cycle, partial-cycle (20-90% SOC), WLTP dynamic and HPPC (100-10% SOC) profiles of one pouch cell; explicitly reported limitations: ML techniques need significant computing resources and training data, posing obstacles for real-time deployment; Coulomb counting suffers from cumulative errors

> Evidence: "they need significant computing resources and training data, posing obstacles for real-time deployment"
