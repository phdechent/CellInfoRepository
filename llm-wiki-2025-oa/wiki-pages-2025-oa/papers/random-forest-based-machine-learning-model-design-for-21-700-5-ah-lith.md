---
cell_target: "Samsung SDI INR-21700-50S"
doi: "https://doi.org/10.3390/physchem5010012"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Health Estimation"
  - "Machine Learning"
  - "Capacity Degradation"
---

# Random Forest-Based Machine Learning Model Design for 21,700/5 Ah Lithium Cell Health Prediction Using Experimental Data

## General Analysis

**Core Thesis:** The paper develops random forest and support vector regression models to predict the SoH of a 5 Ah Samsung INR21700-50S cell from voltage, current and surface temperature recorded during a 300-cycle 1C aging test at 25 °C. Random forest outperformed SVR (R² 0.94 vs. 0.909; RMSE 0.0570 vs. 0.0638 in the discussion section) and current was the most important feature.

**Methodological Focus**
- Testing Mode: Galvanostatic full charge-discharge aging cycling
- Operating Conditions: 25 °C in a climatic chamber; repeated full charge and full discharge at 1C (written as 1◦C in the text); 300 cycles
- Degradation Markers: Capacity fade expressed as SoH (remaining capacity divided by initial capacity)

## Keyword Context

- [[state-of-health-estimation|State-of-Health Estimation]]: SoH, defined as the capacity after each cycle relative to the initial capacity, is the target predicted by the models.
- [[machine-learning|Machine Learning]]: Random forest, SVR, linear regression, XGBoost and KNN regressors are trained on current, voltage and temperature features and compared by R² and RMSE.
- [[capacity-degradation|Capacity Degradation]]: The cell was monitored over 300 charge-discharge cycles to record its aging behaviour under 1C cycling.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To develop and compare random forest and SVR models for SoH prediction of 5 Ah 21700 cells using data from an own aging test; approach: Hybrid

> Evidence: "data from an experimental aging test were used to build the prediction model"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: generate aging data for training SoH prediction models; tests: 300 full charge-discharge cycles at 1C with recording of terminal voltage, current, surface temperature and capacity per cycle; data origin: Own experiments

> Evidence: "The cell was monitored over the course of 300 charge–discharge cycles"

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via Weiss Technik climatic chamber; stability/tolerance: not reported

> Evidence: "The testing procedure was carried out in a climatic chamber to maintain a consistent temperature of 25◦C"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Sensor type not reported × count not reported at cell surface; attachment: not reported; sampling: not reported

> Evidence: "Temperature (T): Surface cell temperature."

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: prediction of SoH; type: data-driven regression (random forest, SVR with RBF kernel; linear regression, XGBoost and KNN for comparison); thermal component: No (temperature used only as an input feature)

> Evidence: "Two machine learning models: support vector regression (SVR) and random forest (RF) were designed and evaluated."

### Q9: Model Parameterization and Validation

**Answer:** Parameters from training on the author's own aging data (features: current, voltage, temperature, voltage rate of change) after Z-score outlier removal and min-max normalization; hyperparameters tuned by grid search with k-fold cross-validation (100 trees optimal; SVR C = 1, ε = 0.1); validated against measured SoH using R², RMSE and MAE (RF R² 0.94, RMSE 0.0570; 10-fold CV average RMSE 0.058)

> Evidence: "By tuning the number of trees (Ntrees) using grid search, we found that the optimal number of trees was 100"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: one cell type cycled at 1C and 25 °C over 300 cycles; explicitly reported limitations: model accuracy is greater for SoH values above 50%; random forest is often viewed as a black-box model, interpretability to be explored in future work

> Evidence: "The developed model demonstrates greater accuracy for higher state of health (SOH) values, specifically those above 50%"
