---
cell_target: "Sony-Murata US18650VTC5"
doi: "https://doi.org/10.1016/j.rineng.2025.104136"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Phase Change Material"
  - "Air Cooling"
  - "Battery Thermal Management"
---

# A novel hybrid cooling system for a Lithium-ion battery pack based on forced air and fins integrated with phase change material

## General Analysis

**Core Thesis:** The paper experimentally compares a forced-air cooling model and a hybrid PCM-Air model (extended copper fins immersed in Rubitherm RT47) for a 9-cell pack (3S3P) of Sony US18650VTC5 cells discharged at 1C, 2C and 3C at 35 °C ambient and air velocities of 0-3 m/s. The hybrid PCM-Air model lowers maximum temperature and reduces the maximum temperature difference by about 39-62% relative to air cooling, keeping it within 5 °C.

**Methodological Focus**
- Testing Mode: Constant-current pack discharge at 1C, 2C and 3C with surface temperature logging; CC-CV pack charging; air-duct cooling tests with and without PCM/fins
- Operating Conditions: 35 °C ± 1 °C controlled room temperature; pack CC charge at 3.9 A (0.5C) to 12.6 V then CV; discharge at 7.8, 15.6 and 23.4 A to 7.5 V; air velocities 0, 1, 2 and 3 m/s
- Degradation Markers: None

## Keyword Context

- [[phase-change-material|Phase Change Material]]: Rubitherm RT47 (melting range 41-48 °C) surrounds the cells and copper fins to absorb peak heat, reducing Tmax to 55 °C at 3C and 3 m/s.
- [[air-cooling|Air Cooling]]: Natural and forced air cooling at 1-3 m/s in an air duct form the baseline Air model and the convective sink of the hybrid PCM-Air model.
- [[battery-thermal-management|Battery Thermal Management]]: The study evaluates pack-level cooling configurations to keep Tmax and ΔTmax of the VTC5 pack within safe limits at high ambient temperature.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To experimentally assess the thermal performance of forced-air and hybrid PCM-fin-air cooling of a Sony US18650VTC5 battery pack under 1C, 2C and 3C discharge at 35 °C ambient; approach: Experimental

> Evidence: "this study aims to experimentally assess the thermal performance of the LIB pack cooling system under various discharge rates (1C, 2C, and 3C) at an ambient temperature of 35 °C."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: evaluate Tmax and ΔTmax of the pack for two cooling models at different air velocities and C-rates; tests: CC-CV pack charging at 0.5C to 12.6 V, constant-current discharge at 1C, 2C and 3C to 7.5 V with an electronic load under natural convection and forced air at 1-3 m/s, with and without PCM and fins; PCM solidification test; data origin: Own experiments

> Evidence: "The discharge process was conducted using a DC Electronic Load of type UTL8200+ Series under a constant current for the 1C, 2C, and 3C discharge rates."

### Q3: Ambient Boundary Conditions

**Answer:** 35 °C via controlled room temperature; stability/tolerance: ±1 °C

> Evidence: "are conducted under a controlled room temperature of 35 °C with a variation of ±1 °C"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** K-type thermocouple × 5 at different locations in the battery pack measuring battery surface temperatures T1-T5; attachment: not reported; sampling: every 60 s (Applent AT4208 data logger)

> Evidence: "Five K-type thermocouples are installed at different locations in the battery pack to measure the batteries' surface temperatures T1, T2, T3, T4, and T5"

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: quantify battery heat generation and the pack heat balance (air convection, PCM storage, battery storage); type: analytical heat generation (irreversible Joule plus reversible entropic) and lumped energy balance equations; thermal component: Yes

> Evidence: "The total heat generation rate of the battery pack is determined in the present study as follows"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from own measured current, voltage, air, PCM and battery temperatures plus PCM thermophysical properties (Table 2); no calibration reported; experimental temperature rise at 3C compared with literature (Abd, Kavasogullari, Qin) with deviations of about 13-49%

> Evidence: "The comparison has demonstrated a similar trend in the results with average deviation in T max, rise by about 29 % lower than Kavasogullari"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (pack-level energy balance); represented inhomogeneities: none in the model (measured pack temperature difference ΔTmax between five thermocouple locations is reported experimentally)

> Evidence: "Q b is heat (W) stored in the battery due to the internal resistance and chemical reactions."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 35 °C ambient, 1C-3C discharge, air velocities 0-3 m/s; explicitly reported limitations: system complexity and added PCM weight, PCM thermal conductivity could be improved

> Evidence: "However, challenges may arise due to the system's complexity and the added weight of the PCM."
