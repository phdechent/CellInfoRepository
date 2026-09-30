---
cell_target: "Sony-Murata US18650VTC6"
doi: "https://doi.org/10.3390/batteries11080314"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Open-Circuit Voltage"
  - "Internal Resistance"
  - "Standardized Battery Testing"
---

# Experimental Testing and Modeling of Li-Ion Battery Performance Based on IEC 62660-1 Standard

## General Analysis

**Core Thesis:** The paper builds a simple empirical voltage model (OCV ± IR, with current-dependent polynomial/exponential fits) from charge/discharge and intermittent OCV tests on a series string of five Sony/Murata VTC6 cells. The model, derived from pause experiments, is validated against continuous CC charge/discharge at 1, 3 and 5 A and against an IEC 62660-1 dynamic discharge profile at 25 °C, with errors mostly below 2.5%.

**Methodological Focus**
- Testing Mode: CC/CV charge and full discharge at 1 A, 3 A, 5 A (12.5–21 V string limits); intermittent 10-min current / 5-min rest OCV–CCV tests; IEC 62660-1 dynamic discharge profile (BEV)
- Operating Conditions: Room temperature for CC/CV tests; 25 °C for IEC test; sampling 10 s (1 A, 3 A) and 1 s (5 A, IEC)
- Degradation Markers: None

## Keyword Context

- [[open-circuit-voltage|Open-Circuit Voltage]]: OCV–capacity relations were measured during 5-min rests and fitted with a 4th-order polynomial for discharge and a linear equation for charge.
- [[internal-resistance|Internal Resistance]]: The IR drop (OCV − CCV) was fitted as an exponential function of capacity for discharge and as a linear function of current (0.22985 + 0.19837·I) for charge.
- Standardized Battery Testing: The IEC 62660-1 dynamic discharge profile was applied to the five-cell string at 25 °C to validate the model over about 3 h (27.3 cycles, 19.58 Wh delivered).

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study develops and experimentally validates a simple OCV/IR-based voltage model for VTC6 cells under various currents and the IEC 62660-1 dynamic profile; approach: Hybrid

> Evidence: "This paper presents a combined experimental and modeling approach to evaluate the performance of lithium-ion batteries used in electric vehicles"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: characterize voltage behavior, extract OCV and IR for model parameterization, and validate the model; tests: CC/CV charge and full discharge of a five-cell series string at 1, 3 and 5 A (21 V to 12.5 V); intermittent OCV tests (20 min rest after full discharge, then 10 min current at 1/3/5 A and 5 min rest, repeated); IEC 62660-1 dynamic discharge profile from 100% SoC at 25 °C, all with an ITECH IT-M3900C bidirectional DC supply; data origin: Own experiments

> Evidence: "Then, a charging current of 1A, 3A and 5A was applied for 10 min, followed by a 5-min rest period, during which the OCV was measured."

### Q3: Ambient Boundary Conditions

**Answer:** Room temperature (value not stated) for CC/CV characterization; 25 °C for the IEC 62660-1 test; control method: not reported; stability/tolerance: not reported

> Evidence: "The test temperature was 25◦C, with SoC initialized at 100%, and the data were recorded every second."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: predict terminal voltage during charge and discharge at different currents and under dynamic profiles; type: empirical/mathematical model V = OCV ± IR with polynomial OCV–capacity fits and current-dependent exponential (discharge) or linear (charge) IR terms; thermal component: No

> Evidence: "The simulation model assumes that the cell voltage can be expressed as a combination of the open-circuit voltage and a current dependent term representing internal resistance or voltage drop"

### Q9: Model Parameterization and Validation

**Answer:** Parameters fitted to the authors' own OCV/CCV pause experiments at 1, 3 and 5 A (polynomial coefficients B0–B4, exponential coefficients y0, A, w, linear charge coefficients); validated against own continuous CC charge/discharge curves at 1, 3 and 5 A and the IEC 62660-1 dynamic profile, with errors below 2.5% (up to 3.5% during rest periods) and a cumulative energy deviation of about 0.143 Wh (36.3% measured vs. 36% modeled energy discharge)

> Evidence: "The proposed model exhibits significantly improved accuracy under the IEC 62660-1 protocol, achieving prediction errors below 2.5%."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (five-cell series string treated as a single voltage source); represented inhomogeneities: none

> Evidence: "providing additional insight into the behavior of the battery pack"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 1–5 A constant currents (charge and discharge) and the IEC 62660-1 BEV dynamic profile at 25 °C, fresh cells; explicitly reported limitations: deviations at the end of discharge (attributed to temperature differences between pause and non-pause experiments), errors up to 3.5% during rest periods (relaxation not captured), single battery type, fixed ambient temperature, currents not above 5 A, aging not included

> Evidence: "limitations arising from the use of a single battery type and fixed ambient temperature conditions are recognized"
