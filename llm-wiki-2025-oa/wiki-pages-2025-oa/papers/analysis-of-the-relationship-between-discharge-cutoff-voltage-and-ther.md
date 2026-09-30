---
cell_target: "Samsung SDI ICR18650-26J"
doi: "https://doi.org/10.3390/app16010079"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Heat Generation"
  - "Discharge Cutoff Voltage"
  - "Battery Management System"
---

# Analysis of the Relationship Between Discharge Cutoff Voltage and Thermal Behavior in Different Lithium-Ion Cell Types

## General Analysis

**Core Thesis:** The study experimentally analyses how the discharge cutoff voltage affects usable energy and surface temperature rise of Samsung ICR18650-26J (18650) and EVE 40PL (21700) cells at 0.5C–2C. It introduces a Thermal Efficiency Ratio (TER) and finds that the 26J cell needs load-adaptive cutoff limits (about 2.9–3.0 V at ≤1C and 3.1–3.2 V at 1.5–2C).

**Methodological Focus**
- Testing Mode: CC–CV charging to 4.20 V followed by constant-current discharges to seven cutoff voltages (3.60–2.50 V) with surface temperature and IR thermography
- Operating Conditions: 25 ± 2 °C ambient; 0.5C CC–CV charge (0.05C cutoff); 0.5C, 1C, 1.5C, 2C discharge; three repetitions per condition, five cells per format
- Degradation Markers: None

## Keyword Context

- [[heat-generation|Heat Generation]]: The maximum surface temperature rise of the ICR18650-26J exceeded 30 °C at 2C discharge to 2.5 V, more than double that of the 21700 cell.
- Discharge Cutoff Voltage: Seven discharge cutoff voltages between 3.60 V and 2.50 V were tested to find the compromise between usable energy and thermal stress.
- [[battery-management-system|Battery Management System]]: The authors propose TER-based, load-adaptive lower cutoff limits as a practical framework for BMS control.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To determine the optimal lower discharge cutoff voltage for the Samsung ICR18650-26J (compared with a 21700 cell) considering usable energy and thermal development, using the Thermal Efficiency Ratio; approach: Experimental

> Evidence: "The present research aims to define and analyze the optimal value of the lower voltage threshold more precisely, considering both thermal development and usable capacity aspects."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: quantify usable energy and temperature rise versus cutoff voltage and C-rate; tests: three preconditioning cycles at 0.5C, CC–CV charge to 4.20 V (0.5C, 0.05C cutoff), discharges at 0.5C, 1C, 1.5C and 2C to cutoffs of 3.60–2.50 V, three repetitions per condition on five cells; data origin: Own experiments

> Evidence: "Controlled discharge cycles were then performed at four different load levels: 0.5C, 1C, 1.5C, and 2C, defined relative to nominal capacity."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via controlled laboratory conditions (no chamber specified); stability/tolerance: ±2 °C; cells rested until surface temperature returned to within ±0.5 °C of ambient between cycles

> Evidence: "All experiments were carried out under controlled laboratory conditions at an ambient temperature of 25± 2◦C."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** LM35 CAZ precision temperature sensor × 2 at the cell's geometric center and near the cathode terminal, plus FLIR E5 infrared camera for spatial uniformity; attachment: surface-mounted (method not specified); sampling: recorded continuously, rate not reported

> Evidence: "one sensor attached near the cell’s geometric center and another positioned close to the cathode terminal"

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

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
