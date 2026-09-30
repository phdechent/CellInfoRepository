---
cell_target: "Samsung SDI INR18650-30Q"
doi: "https://doi.org/10.3390/wevj16090533"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Fractional-Order Equivalent Circuit Model"
  - "State-of-Charge Estimation"
  - "State-of-Health Estimation"
---

# Cooperative Estimation Method for SOC and SOH of Lithium-Ion Batteries Based on Fractional-Order Model

## General Analysis

**Core Thesis:** The paper proposes a multi-time-scale SOC/SOH co-estimation framework for the Samsung INR18650-30Q cell, combining a fractional-order second-order RC model identified offline with the whale optimization algorithm, a strong-tracking SVD-based UKF for SOC, and an EKF for online parameter/capacity updates. Using the authors' own pulse and drive-cycle data, it reports mean SOC errors of 0.45–0.51% and SOH errors within 0.25%.

**Methodological Focus**
- Testing Mode: Pulse discharge test (1C, 3 min pulses with 2 h rests) for OCV–SOC and parameter identification; UDDS, NEDC and HWFET drive-cycle tests for validation
- Operating Conditions: CC 0.5C / CV to 0.05C charge to 4.2 V, discharge to 2.5 V; 100 ms sampling; temperature not reported
- Degradation Markers: None measured (SOH tracked as maximum available capacity estimate)

## Keyword Context

- [[fractional-order-equivalent-circuit-model|Fractional-Order Equivalent Circuit Model]]: A fractional-order second-order RC model with CPEs (orders m = 0.9674, n = 0.9554) reduced the mean terminal-voltage error to 0.0047 V versus 0.0051 V for the integer-order model.
- [[state-of-charge-estimation|State-of-Charge Estimation]]: A strong-tracking SVD-UKF on the fractional-order model estimates SOC every 100 ms, reaching mean errors of 0.45% (UDDS), 0.51% (NEDC) and 0.35% (HWFET).
- [[state-of-health-estimation|State-of-Health Estimation]]: An EKF updates model parameters and maximum available capacity every 60 SOC steps, keeping SOH error within 0.25%.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study develops and validates a fractional-order-model-based cooperative SOC/SOH estimation method for the INR18650-30Q using its own pulse and drive-cycle measurements; approach: Hybrid

> Evidence: "Experimental results under three dynamic operating conditions driving cycles demonstrate that the proposed method effectively solves the SOC/SOH collaborative estimation problem"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: obtain OCV–SOC relation and data for offline parameter identification, and dynamic data for validating state estimation; tests: pulse discharge (CC 0.5C to 4.2 V, CV to 0.05C, 2 h rest, then repeated 1C 3-min discharge pulses with 2 h rest to 2.5 V) and UDDS, NEDC and HWFET current profiles from full charge to 2.5 V, using a YouNeng UPC-5V6A-8C tester (±0.05% accuracy, 100 ms sampling); data origin: Own experiments

> Evidence: "Pulse discharge tests and urban dynamometer driving schedule (UDDS) tests were conducted on the battery pack under investigation."

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

**Answer:** Purpose: predict terminal voltage for model-based SOC and SOH (maximum available capacity) estimation; type: fractional-order second-order RC equivalent circuit model (Grünwald–Letnikov discretization) with strong-tracking SVD-UKF for SOC and EKF for parameters; thermal component: No

> Evidence: "the diffusion of lithium ions within the electrolyte exhibits fractional-order dynamics, which cannot be fully captured by integer-order models"

### Q9: Model Parameterization and Validation

**Answer:** Parameters identified offline from own pulse-discharge data by the whale optimization algorithm (fitness: terminal-voltage error variance, 500 iterations) and updated online by EKF; validated against own pulse data (mean/max voltage error 0.0047/0.0363 V) and own UDDS, NEDC, HWFET data with Ah-integration reference SOC: mean SOC error 0.45%, 0.51%, 0.35% and max 1.03%, 1.39%, 1.17%; SOH error within 0.25%

> Evidence: "The average error of the fractional-order model is 0.0047 V and the maximum error is 0.0363 V ."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped; represented inhomogeneities: none

> Evidence: "A fractional-order second-order RC equivalent circuit model is established"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: single INR18650-30Q cell, full charge to 2.5 V under UDDS, NEDC and HWFET profiles, initial SOC errors (40/60/80%) and initial SOH values (90/95%); explicitly reported limitations: none stated beyond noting that ECM parameters change with temperature, aging, SOC and C-rate (motivating online updates); temperature and aging conditions were not varied

> Evidence: "the previously established model parameters may result in larger errors compared to the current state, which leads to increased SOC estimation errors"
