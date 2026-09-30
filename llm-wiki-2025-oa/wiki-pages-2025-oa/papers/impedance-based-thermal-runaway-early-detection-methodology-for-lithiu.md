---
cell_target: "Samsung SDI INR21700-50E"
doi: "https://doi.org/10.1016/j.ijepes.2025.111053"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Thermal Runaway"
  - "Electrochemical Impedance Spectroscopy"
  - "Accelerating Rate Calorimetry"
---

# Impedance-based Thermal Runaway early detection methodology for Lithium-Ion batteries

## General Analysis

**Core Thesis:** The paper proposes an early thermal-runaway detection method for Samsung INR21700-50E cells based on single-frequency impedance (400.15 Hz) phase and magnitude tracking. The impedance behaviour is characterized in ARC tests at 10%, 50% and 100% SoC and validated in fast overtemperature tests at cell and 8s1p module level against an automotive VOC gas sensor, giving warnings about 15 h (slow) and 6–12 min (fast) before thermal runaway.

**Methodological Focus**
- Testing Mode: Accelerating rate calorimetry (Heat-Wait-Seek) with EIS, overtemperature abuse tests with continuous single-frequency EIS, module-level thermal runaway test, gas sensing
- Operating Conditions: ARC from 25 °C in 5 °C steps to TR at 10/50/100% SoC; overtemperature tests with 80 W heater at 100% and 50% SoC; EIS 1 Hz–1.6 kHz, 50 mA amplitude
- Degradation Markers: None (fresh cells after three C/2 activation cycles)

## Keyword Context

- [[thermal-runaway|Thermal Runaway]]: Thermal runaway is triggered by thermal abuse (ARC heat-wait-seek and 80 W overtemperature heating) and detected via impedance warnings before venting and explosion.
- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]: Single-frequency EIS at 400.15 Hz, selected by maximizing temperature variance over SoC variance, provides phase-shift and magnitude-decoupling warning criteria.
- Accelerating Rate Calorimetry: ARC tests with the Heat-Wait-Seek protocol were used to characterize cell impedance at SoC values of 10%, 50% and 100% and temperatures from 25 °C up to 120 °C.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To develop and validate an impedance-based (single-frequency EIS) early thermal-runaway detection methodology for Samsung INR21700-50E cells and compare it with gas-sensor detection; approach: Experimental

> Evidence: "In this work, a new impedance-based Thermal Runaway (TR) early detection methodology for Li-ion batteries is proposed."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: characterize impedance versus temperature and SoC and validate TR warning criteria; tests: three C/2 activation cycles, ARC Heat-Wait-Seek tests at 10%, 50% and 100% SoC with EIS (1 Hz–1.6 kHz), fast overtemperature abuse tests (80 W heater) at 100% and 50% SoC with continuous 400.15 Hz EIS and VOC gas sensor, 8s1p module TR test at 100% SoC; data origin: Own experiments

> Evidence: "Accelerating Rate Calorimetry (ARC) tests were carried out in a THT EV + ARC calorimeter."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C start (cells charged at 25 °C; ARC initialized at 25 °C) with THT EV+ ARC Heat-Wait-Seek steps of 5 °C, 30 min wait, 0.02 °C/min sensitivity up to TR; abuse-chamber ambient temperature not reported; stability/tolerance: not reported

> Evidence: "The tests were initialized at 25 °C and ended with the Thermal Runaway of the cells."

### Q4: Mechanical Boundary Conditions

**Answer:** None reported; magnitude: not reported; fixture: in overtemperature tests the heater dummy cell is attached with metallic cable ties and the cell is hung in the chamber center; module tests in 8s1p configuration

> Evidence: "The heater is attached to the cell with metallic cable ties, and the cell is hung in the center of the chamber"

### Q5: Cell Temperature Measurement

**Answer:** Thermocouple × 3 at positive tab, negative tab and cell center (overtemperature tests); attachment: not reported; sampling: not reported

> Evidence: "3 thermocouples were used for tracking the cell’s temperature, on the positive tab, on the negative tab and on the cell center."

### Q6: Temperature-Dependent Performance

**Answer:** At 25 °C to about 120 °C (ARC, 10/50/100% SoC), impedance decreased with rising temperature and then increased from approximately 90 °C; the 400.15 Hz phase shift changed strongly between 25 °C and 48 °C, fell below −0.5° above about 50 °C and converged thereafter; magnitude was more SoC-dependent, phase more temperature-dependent

> Evidence: "with the impedance initially decreasing as temperature increased, then reversing direction and increasing at approximately 90 °C"

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Not explicitly discussed.

### Q9: Model Parameterization and Validation

**Answer:** Not explicitly discussed.

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Not explicitly discussed.
