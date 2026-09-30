---
cell_target: "Samsung SDI INR18650-25R"
doi: "https://doi.org/10.3390/batteries11020067"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Phase Change Material"
  - "Battery Thermal Management"
  - "Air Cooling"
---

# Experimental Investigation of Phase Change Material-Based Battery Pack Performance Under Elevated Ambient Temperature

## General Analysis

**Core Thesis:** The study experimentally evaluates a paraffin (40–42 °C) PCM-based battery pack of nine series-connected Samsung INR18650-25R cells with air-duct cooling, compared with an air-cooled baseline without PCM. Ambient (inlet air) temperatures of 22–42 °C, up to the PCM melting point, are applied at 1C and 3C discharge to quantify temperature reduction and local PCM melting.

**Methodological Focus**
- Testing Mode: Pack-level constant-current discharge (1C and 3C, CC-CV to 2.5 V per cell) with surface thermocouple measurements, with and without PCM; CC-CV charging at 4 A
- Operating Conditions: Ambient 22, 27, 32, 37 and 42 °C in a thermal chamber; initial pack temperature 22 °C; inlet air speed 2.1 ± 0.1 m/s
- Degradation Markers: None

## Keyword Context

- [[phase-change-material|Phase Change Material]]: Paraffin wax with a 40–42 °C melting range fills the pack, and its temperature reduction and local melting percentage are quantified versus ambient temperature and C-rate.
- [[battery-thermal-management|Battery Thermal Management]]: The paper assesses a hybrid PCM/air-pipe thermal management system for keeping 18650 cells below about 40–42 °C under elevated ambient temperatures.
- [[air-cooling|Air Cooling]]: A conventional air-cooled pack with aluminium air pipes and a fan-driven duct serves as the baseline, whose inlet air temperature is raised to emulate unfavourable cooling.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study experimentally assesses how well a PCM-based pack of INR18650-25R cells limits cell temperature when the ambient temperature rises up to the PCM melting point, at 1C and 3C discharge; approach: Experimental

> Evidence: "This study experimentally assesses the thermal performance of a proposed phase change material (PCM)-based battery pack under elevated ambient temperatures."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: evaluate PCM thermal performance and utilization under elevated ambient temperatures against an air-cooled baseline; tests: CC-CV charge at 4 A to 4.2 V per cell (cutoff 0.1 A), constant-current discharge at 1C (2.5 A) and 3C (7.5 A) to 2.5 V per cell followed by CV to 0.1 A, with and without PCM at five ambient temperatures, repeated for uncertainty analysis; PCM melting/solidification characterization; data origin: Own experiments

> Evidence: "The total discharge times for 1C and 3C discharge rates are approximately 66 min and 25 min, respectively."

### Q3: Ambient Boundary Conditions

**Answer:** 22–42 °C in 5 °C steps via a 227 L thermal chamber (SD-508) controlling the inlet air temperature, with the pack initially held at 22 ± 0.1 °C; stability/tolerance: ±0.5 °C chamber accuracy

> Evidence: "Five ambient temperatures were studied, ranging from 22◦C to 42◦C in increments of 5◦C."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** T-type thermocouples (Omega 5TC-TT-T-24-72, ±0.5 °C) × 9 at the cell surfaces at mid-height, oriented to capture all sides of the cells; attachment: not specified beyond being attached to the surface, read via Adafruit 3263 amplifiers and an Arduino Mega; sampling: not reported

> Evidence: "Nine thermocouples were attached to the surface of the batteries at the center of the total height, capturing temperature data from all sides of the batteries"

### Q6: Temperature-Dependent Performance

**Answer:** At ambient temperatures of 22–42 °C and 3C discharge, the maximum cell surface temperature of the baseline pack rose from 38 °C to 55 °C, whereas with PCM it remained below 42 °C; the PCM reduced the maximum temperature by 2.6–13.3 °C at 3C and 1.6–2.5 °C at 1C; electrical responses versus temperature were not reported

> Evidence: "the baseline system experienced a significant temperature increase from 38◦C to 55◦C"

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
