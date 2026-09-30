---
cell_target: "Samsung SDI INR21700-48X"
doi: "https://doi.org/10.3390/batteries11020059"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Immersion Cooling"
  - "Battery Thermal Management"
  - "Fast Charging"
---

# Experimental Study on Thermal Management of 5S7P Battery Module with Immersion Cooling Under High Charging/Discharging C-Rates

## General Analysis

**Core Thesis:** The study experimentally evaluates single-phase oil immersion cooling for a 5S7P module of 35 Samsung SDI INR21700-48X cells (4.8 Ah), selecting the best of three coolant oils and an optimal volume flow rate and then testing charge and discharge rates up to 3.0C. Therminol D-12 at 0.8 LPM kept Tmax/ΔT at 38.6 °C/4.3 °C at 3.0C charging and 43.0 °C/5.5 °C at 3.0C discharging.

**Methodological Focus**
- Testing Mode: Module-level CC-CV charging (21 V, 0.84 A cut-off) and CC discharging (12.5 V cut-off) at 1.0C-3.0C under forced immersion cooling with surface temperature, coolant temperature and pressure measurement
- Operating Conditions: 25 °C ambient in a constant temperature and humidity chamber; coolant oils Therminol D-12, Pitherm 150B, BOT 2100; VFR 0.4-1.0 LPM; bottom-to-top flow with 3 inlets and 3 outlets
- Degradation Markers: None

## Keyword Context

- [[immersion-cooling|Immersion Cooling]]: The 35 cells are submerged in dielectric oil in an aluminum box, with coolant type and volume flow rate varied to maximize heat transfer coefficient and limit pressure drop.
- [[battery-thermal-management|Battery Thermal Management]]: Module Tmax and cell-to-cell ΔT from nine surface thermocouples are the main performance criteria, targeted at 25-40 °C and below 5 °C.
- [[fast-charging|Fast Charging]]: The selected cooling configuration is tested at charging rates of 1.5C to 3.0C, reaching a Tmax of 38.6 °C at 3.0C.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To experimentally evaluate the effectiveness of immersion cooling for a 5S7P module of INR21700-48X cells by selecting an optimal coolant oil and volume flow rate and assessing thermal performance at high charge/discharge C-rates; approach: Experimental

> Evidence: "the efficiency of an immersion cooling system for controlling the temperature of 5S7P battery modules at high charge and discharge C-rates was experimen- tally evaluated"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: identify optimal coolant oil and flow rate and evaluate thermal management under harsh C-rates; tests: 1.0C discharge with three coolant oils at 0.6 LPM; 1.0C discharge with Therminol D-12 at 0.4, 0.6, 0.8 and 1.0 LPM; CC-CV charging at 1.5C-3.0C and CC discharging at 1.5C-3.0C with Therminol D-12 at 0.8 LPM, measuring Tmax, ΔT, HTC and pressure drop; data origin: Own experiments

> Evidence: "The charge/discharge rates conducted in the present study included 1.0C (33.6 A), 1.5C (50.4 A), 2.0C (67.2 A), 2.5C (84 A), and 3.0C (100.8 A)."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via a constant temperature and humidity chamber, with coolant inlet temperature controlled by a 5 kW JWT-30 chiller and heat exchanger (coolant held at 25 °C in the flow-rate tests); stability/tolerance: not reported (temperature measurement uncertainty ±1.31%)

> Evidence: "All experiments were carried out with an ambient temperature setting of 25◦C in a constant temperature and humidity chamber."

### Q4: Mechanical Boundary Conditions

**Answer:** None reported; magnitude: not reported; fixture: cells arranged in an aligned configuration in a 163.0 × 117.0 × 90 mm aluminum box with 2 mm spacing between cells and between cells and box

> Evidence: "The battery cells were arranged in an aligned configuration in an aluminum box with 163.0 ×117.0×90 mm dimensions."

### Q5: Cell Temperature Measurement

**Answer:** T-type thermocouples × 9 on the surface of nine cells at different module locations (T1-T9, from coolant inlet to outlet region), at the middle height of each cell; attachment: affixed to the cell surface (method not detailed); sampling: not reported (logged with a GL820 data logger)

> Evidence: "nine T-type thermocouples (T1–T9) were affixed to the surface of nine battery cells at various locations"

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
