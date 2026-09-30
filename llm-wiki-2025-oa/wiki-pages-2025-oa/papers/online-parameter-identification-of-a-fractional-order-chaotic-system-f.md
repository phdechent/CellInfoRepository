---
cell_target: "Samsung SDI INR18650-20R"
doi: "https://doi.org/10.3390/batteries11100377"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Online Parameter Identification"
  - "Fractional-Order Equivalent Circuit Model"
  - "Hybrid Pulse Power Characterization"
---

# Online Parameter Identification of a Fractional-Order Chaotic System for Lithium-Ion Battery RC Equivalent Circuit Using a State Observer

## General Analysis

**Core Thesis:** The paper builds a fractional-order hyperchaotic system by connecting a charge-controlled (asymmetric diode bridge) memristor emulator and inductors as a load to a first-order RC equivalent circuit, and designs a state observer to identify R0, R1 and C1 online. The identification is validated on a Samsung INR18650-20R cell under HPPC and DST at 25 °C and UDDS at 40 °C, where the observer predicts terminal voltage more accurately than FFRLS and a Kalman filter.

**Methodological Focus**
- Testing Mode: HPPC pulse test (1C discharge steps of 10 % DOD, 5C/2C 10 s pulses), DST and UDDS dynamic profiles on an Arbin BT200
- Operating Conditions: HPPC and DST at 25 °C, UDDS at 40 °C ambient; 2.5-4.2 V; CC-CV charge at 0.2C with 0.02C cutoff
- Degradation Markers: None

## Keyword Context

- [[online-parameter-identification|Online Parameter Identification]]: A state observer identifies the unknown chaotic-system parameters A, B and D online, from which R0, R1 and C1 of the first-order RC-ECM are computed from measured voltage, current and charge.
- [[fractional-order-equivalent-circuit-model|Fractional-Order Equivalent Circuit Model]]: The first-order RC-ECM is formulated with a Caputo fractional derivative of the polarization capacitor voltage (order α between 0 and 1) and embedded in a fourth-order hyperchaotic system.
- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]: HPPC data from SOC 0.9 to 0.1 at 25 °C are used for identification, where the observer gives a mean relative voltage error of 0.27 % versus 1.68 % (FFRLS) and 3.37 % (KF).

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To achieve accurate real-time online identification of first-order RC-ECM parameters of the INR18650-20R cell using a memristor-based fractional-order chaotic system and a state observer; approach: Hybrid

> Evidence: "an identification observer is designed for each unknown parameter of the first-order RC-ECM, achieving online identification of these unknown parameters of the first-order RC-ECM of LIB"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: validate the state-observer parameter identification and compare it with FFRLS and KF via terminal-voltage prediction; tests: HPPC (0.2C CC-CV charge to 4.2 V, 2 h rest, 1C discharge to successive 10 % DOD steps, 40 min rest, 5C or 2C 10 s discharge pulse, 30 s rest, 10 s charge), DST at 25 °C, UDDS at 40 °C; data origin: Own experiments

> Evidence: "Real-time tests were carried out using the Arbin BT200 system (ARBIN Instrument Company, College Station, TX, USA)."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C (HPPC, DST) and 40 °C (UDDS) ambient; control method: not reported; stability/tolerance: not reported

> Evidence: "tests were conducted across multiple drive cycles (HPPC, DST, and UDDS) at two ambient temperatures: 25◦C and 40◦C."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: online identification of R0, R1 and C1 and real-time terminal-voltage prediction; type: fractional-order (Caputo) first-order RC equivalent circuit embedded in a memristor-based fourth-order hyperchaotic system with a state observer for parameter identification; thermal component: No

> Evidence: "This paper establishes a fractional-order chaotic system for first-order RC-ECM based on a charge-controlled memristor."

### Q9: Model Parameterization and Validation

**Answer:** Parameters identified online by the state observer from own measured voltage, current and charge; calibrated with the HPPC data at 25 °C; validated against measured terminal voltage under HPPC 25 °C (MRE 0.27 %, MAE 1.36 mV, RMSE 0.34 %), DST 25 °C (MRE 0.21 %, MAE 2.36 mV, RMSE 0.22 %) and UDDS 40 °C (MRE 0.17 %, MAE 1.62 mV, RMSE 0.19 %), outperforming FFRLS and KF

> Evidence: "The battery terminal voltage was predicted in real-time online by substituting the identified parameters ( R0,R1, and C1) into the first-order RC-ECM"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: HPPC (SOC 0.9 to 0.1) and DST at 25 °C, UDDS at 40 °C on a single INR18650-20R cell; explicitly reported limitations: reaching the chaotic state relies on manual tuning of memristor parameters, identification fails when the system is non-chaotic, and extending to second- or third-order RC-ECMs increases observer-design difficulty

> Evidence: "Currently, achieving a chaotic state relies on the manual tuning of memristor parameters."
