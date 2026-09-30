---
cell_target: "EVE EVE-INR18650 33V"
doi: "https://doi.org/10.3390/modelling6030100"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Charge Estimation"
  - "State-of-Health Estimation"
  - "Unscented Kalman Filter"
---

# Joint Estimation of SOC and SOH Based on Kalman Filter Under Multi-Time Scale

## General Analysis

**Core Thesis:** The paper develops a multi-time-scale joint SOC and SOH estimator for the EVE INR18650/33V cell, using an SVD-based Unscented Kalman Filter on the micro-time scale for SOC and an EKF on the macro-time scale for impedance parameters and capacity. The method is parameterized with the authors' own capacity, aging and HPPC tests and verified under DST and FUDS conditions.

**Methodological Focus**
- Testing Mode: Static capacity test, full-SOC-range aging cycle test, HPPC tests at different aging stages, DST and FUDS dynamic profiles
- Operating Conditions: Static capacity test at 25 °C with 0.5C discharge; aging cycling from 100% to 0% SOC (temperature not stated); CT-4008Tn-5V12A tester
- Degradation Markers: Capacity fade (initial 3.1 Ah) and aging-dependent SOC–OCV shift (up to 248 mV between SOH 100% and 80%)

## Keyword Context

- [[state-of-charge-estimation|State-of-Charge Estimation]]: The SVDUKF estimates SOC on the micro-time scale and achieved an SOC RMSE of 1.0531% under DST.
- [[state-of-health-estimation|State-of-Health Estimation]]: Capacity estimated by the macro-scale EKF is divided by initial capacity to give SOH, with errors within 2% (DST) and 1% (FUDS).
- [[unscented-kalman-filter|Unscented Kalman Filter]]: The UKF is modified by replacing Cholesky decomposition with singular value decomposition (SVDUKF) to improve accuracy and stability of SOC estimation.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To establish a joint SOC and SOH estimation method (SVDUKF-EKF under a multi-time scale) for the EVE INR18650/33V cell, parameterized from own tests and verified under DST and FUDS; approach: Hybrid

> Evidence: "This paper uses the ternary EVE-INR-18650/33V vehicle ba ttery cell as the research object"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: build a battery test database for OCV–SOC–SOH relationships, parameter identification and state estimation; tests: static capacity test (0.5C discharge, average of three capacities, 3.1 Ah initial), aging cycle test over 100%–0% SOC, HPPC tests at different aging stages, DST and FUDS profiles for verification; data origin: Own experiments

> Evidence: "static capacity tests, aging tests, and Hybrid Pulse Power Characte ristic (HPPC) tests were conducted on the batteries under di ﬀerent aging degrees"

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C (static capacity test) via constant-temperature condition, control method not reported; stability/tolerance: not reported. Temperatures of aging, HPPC and DST/FUDS tests not stated.

> Evidence: "Under a constant temperature of 25 °C, the ba ttery was discharged at a 0.5 C rate until it reached the cut-o ﬀ voltage."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: estimate SOC (micro-time scale) and ohmic resistance, dual polarization RC parameters and maximum available capacity/SOH (macro-time scale); type: second-order RC equivalent circuit model with SVDUKF-EKF joint estimator and OCV–SOC–SOH surface; thermal component: Not stated

> Evidence: "the Extended Kalman Filter (EKF) is used on the macro-time scale to estimate ba ttery parameters that change slowly, including internal resistance, dual polarization impedance parameters"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from own HPPC tests: OCV–SOC–SOH 6th-order polynomial surface fit (RMSE 0.0146 V), impedance parameters identified with AFFRLS as initial values; calibrated with own HPPC data at different aging stages; validated against measured terminal voltage, SOC and SOH under DST (SOC RMSE 1.0531%, SOH error within 2%) and FUDS (SOC RMSE 1.5611%, SOH error within 1%)

> Evidence: "The impedance parameters are obtained through the AFFRLS method, with the initial value of the maximum available capacity set to 2.9 Ah (actual value: 2.9588 Ah)."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (second-order RC equivalent circuit model); represented inhomogeneities: none

> Evidence: "Figure 3 shows the second-order RC equivalent circuit model of lithium-ion ba tteries."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: DST and FUDS profiles with initial SOC error (80% vs. 100% true), true capacities 2.9588 Ah (DST) and 3.0993 Ah (FUDS), and robustness tests with different initial SOC values; test temperature not stated; explicitly reported limitations: terminal voltage and SOH errors increase after 12,000 s when SOC falls below 20% due to model deviation at low SOC

> Evidence: "due to the large deviation of the battery model caused by the low SOC, the SOH estimation error increases."
