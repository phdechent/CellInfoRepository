---
cell_target: "Samsung SDI INR18650-25R"
doi: "https://doi.org/10.3390/en18164364"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Charge Estimation"
  - "Adaptive Extended Kalman Filter"
  - "Online Parameter Identification"
---

# SOC Estimation for Lithium-Ion Batteries Based on Weighted Multi-Innovation Sage–Husa Adaptive EKF

## General Analysis

**Core Thesis:** The paper proposes an improved adaptive forgetting factor recursive least squares (IAFFRLS) algorithm for online identification of a second-order RC model and a weighted multi-innovation improved Sage–Husa adaptive EKF (WMISAEKF) for SOC estimation. The methods are developed on UDDS data of an ATL 33 Ah cell, and their applicability is checked with FTP-75 data of the INR18650-25R (2500 mAh) cell at 25 °C, where WMISAEKF reduced MAE, RMSE and MAXE by 75.61%, 72.92% and 55.74% compared with EKF.

**Methodological Focus**
- Testing Mode: Dynamic drive-cycle discharge (FTP-75 for the INR18650-25R; UDDS and intermittent discharge-rest OCV test for the ATL 33 Ah cell)
- Operating Conditions: Constant 25 °C; INR18650-25R rated capacity 2500 mAh
- Degradation Markers: None

## Keyword Context

- [[state-of-charge-estimation|State-of-Charge Estimation]]: SOC estimation accuracy of EKF, ISAEKF and WMISAEKF is compared on the UDDS (ATL cell) and FTP-75 (INR18650-25R) profiles.
- Adaptive Extended Kalman Filter: The WMISAEKF combines an improved Sage–Husa noise covariance update with weighted multi-innovation to prevent filter divergence and improve accuracy.
- [[online-parameter-identification|Online Parameter Identification]]: The IAFFRLS algorithm identifies the second-order RC parameters online using an arccot-based adaptive forgetting factor regulation.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To improve SOC estimation by combining a new online parameter identification algorithm (IAFFRLS) with a weighted multi-innovation Sage–Husa adaptive EKF, with the INR18650-25R FTP-75 data used to verify applicability under a different working condition; approach: Hybrid

> Evidence: "To verify the applicability of the algorithm proposed in this paper under different working conditions"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: provide validation data for parameter identification and SOC estimation; tests: FTP-75 drive-cycle test of the INR18650-25R at 25 °C (measured condition data used for SOC verification); main development data from an ATL 33 Ah ternary cell (UDDS for 300 min, ~11 cycles, at 100% SOH, and intermittent discharge-rest OCV test) on a Neware CE6008a tester; data origin: Own experiments (the 25R data are described as measured, without an external source cited)

> Evidence: "The measured condition data were used to verify the SOC estimation in the algorithm proposed in this paper."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C (constant temperature; control method not reported for the INR18650-25R test); stability/tolerance: not reported (tester temperature error ±1 °C stated for the ATL test system)

> Evidence: "Under a constant temperature of 25◦C, the rated capacity of the test object was 2500 mAh."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: prediction of terminal voltage and SOC estimation; type: second-order RC equivalent circuit model with IAFFRLS online parameter identification and WMISAEKF state estimator; thermal component: No

> Evidence: "this study adopts the second-order RC equivalent circuit model for investigation"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from online IAFFRLS identification (λmax = 1, λmin = 0.985) with a 7th-order polynomial OCV–SOC fit from intermittent discharge-rest tests (ATL cell); calibrated with UDDS data of the ATL 33 Ah cell; validated against UDDS (WMISAEKF SOC RMSE 0.0021) and the INR18650-25R FTP-75 data (WMISAEKF SOC MAE 0.0030, RMSE 0.0039, MAXE 0.0135)

> Evidence: "compared with the EKF algorithm, the MAE, RMSE, and MAXE of WMISAEKF are decreased by 75.61%, 72.92%, and 55.74%, respectively"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped; represented inhomogeneities: none

> Evidence: "this study adopts the second-order RC equivalent circuit model for investigation"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: UDDS and FTP-75 profiles at constant 25 °C, fresh cells (ATL at 100% SOH), with added noise and incorrect initial SOC; explicitly reported limitations: validation only under laboratory conditions with simulated profiles at constant temperature; generalization to real operation, extreme thermal cycling and nonlinear degradation states remains unverified; SOH effects not considered

> Evidence: "validation was exclusively conducted under laboratory conditions using simulated UDDS and FTP-75 profiles at a constant temperature"
