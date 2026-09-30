---
cell_target: "A123 Systems AMP20M1HD-A"
doi: "https://doi.org/10.1016/j.rineng.2025.104509"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "State-of-Charge Estimation"
  - "Unscented Kalman Filter"
  - "Online Parameter Identification"
---

# Hardware-in-the-Loop simulation for online identification of lithium-ion battery model parameters and state of charge estimation

## General Analysis

**Core Thesis:** The paper proposes a modified adaptive unscented Kalman filter (mAUKF) with exponentially weighted process-noise covariance, combined with FFRLS online identification of a second-order Thevenin model, to estimate SOC under large initial SOC errors. The method is validated on an A123 AMP20M1HD cell (19.5 Ah) through Simulink simulation, a laboratory discharge experiment, and a hardware-in-the-loop (HIL) test bench with a Raspberry Pi 4.

**Methodological Focus**
- Testing Mode: HPPC test for the OCV-SOC relationship; constant-current discharge for SOC estimator validation; HIL emulation of charge/discharge scenarios
- Operating Conditions: 0.5C (9.75 A) discharge; 20 % initial SOC error; 1 s measurement sampling (reference device 0.1 s); ambient temperature not reported
- Degradation Markers: None

## Keyword Context

- [[state-of-charge-estimation|State-of-Charge Estimation]]: SOC of the A123 cell is estimated with UKF, AUKF and the proposed mAUKF and compared by RMSE, MAE and convergence time.
- [[unscented-kalman-filter|Unscented Kalman Filter]]: The proposed mAUKF extends the adaptive UKF by exponentially weighting the process-noise covariance estimate to speed convergence under large initial SOC errors.
- [[online-parameter-identification|Online Parameter Identification]]: A forgetting-factor recursive least squares (FFRLS) algorithm identifies the second-order RC model parameters online, alternating with the SOC estimator.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study aims to estimate SOC robustly under large initial SOC errors using an mAUKF with FFRLS online parameter identification and to validate it in simulation, experiment and a HIL bench; approach: Hybrid

> Evidence: "The effectiveness of the method is validated using both simulation and experimental results."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: determine the OCV-SOC relationship and validate the SOC estimation algorithms on a real cell; tests: HPPC test for the SOC-OCV relationship, continuous constant-current discharge at 0.5C (9.75 A) of a single A123 cell with reference measurement by a PCS-1000 instrument, plus HIL tests with a battery emulator; data origin: Own experiments

> Evidence: "first, determining the SOC OCV relationship using the HPPC method"

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

**Answer:** Purpose: real-time SOC estimation robust to large initial SOC errors; type: second-order RC (Thevenin) equivalent circuit model with FFRLS parameter identification and UKF/AUKF/mAUKF state estimation, plus a Simscape battery model of the A123 AMP20M1HD cell used for simulation and HIL emulation; thermal component: Not stated

> Evidence: "The modified AUKF (mAUKF) begins by constructing a second-order Thevenin model of the batteries through the forgetting factor recursive least squares (FFRLS) method"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from online FFRLS identification (forgetting factor 0.9985), initialized from prior knowledge; OCV-SOC relationship from the authors' own HPPC test fitted with an 8th-order polynomial; validated against Simulink simulation, the authors' own 0.5C discharge experiment with PCS-1000 reference coulomb counting, and HIL tests, using RMSE, MAE and convergence time

> Evidence: "Based on the experimental results, the SOC OCV relationship was determined to be represented by an 8th-order polynomial function"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped; represented inhomogeneities: none (a preliminary 29-cell pack simulation is reported, but no spatial or cell-to-cell inhomogeneity is modelled)

> Evidence: "To confirm its feasibility, a preliminary simulation on a 29-cell battery pack was conducted in scenario 11."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: single-cell 0.5C (9.75 A) discharge experiment, simulated and HIL charge/discharge scenarios with 20 % initial SOC error and different initial covariances; explicitly reported limitations: HIL results show larger errors than simulation due to sensor and ADC noise, discrepancies between actual and simulated battery models make initialization difficult, and transfer to large packs requires balancing, monitoring/protection and higher computational efficiency

> Evidence: "However, the HIL results exhibit larger errors, as indicated in Table 8 compared to Table 6 , highlighting the impact of real-world noise and hardware limitations."
