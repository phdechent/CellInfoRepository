---
cell_target: "Sony-Murata US18650VTC6"
doi: "https://doi.org/10.3390/batteries11110396"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Capacity Degradation"
  - "Thermal Runaway"
  - "Multi-Temperature Evaluation"
---

# Research on Aging Evolution and Safety Characteristics of Lithium-Ion Batteries Cycling at Low Temperature

## General Analysis

**Core Thesis:** The study experimentally characterizes how low-temperature (−20 °C) cycling of Sony US18650VTC6 NCM cells affects OCV, ohmic and polarization resistance and capacity under varying temperatures, charge/discharge rates and voltage windows. Thermal runaway tests in an accelerating rate calorimeter on cells aged at low temperature show that aged cells still release large energy during thermal runaway.

**Methodological Focus**
- Testing Mode: Galvanostatic CC-CV aging cycling, HPPC resistance tests every 25 cycles, capacity tests, accelerating rate calorimetry (Heat-Wait-Search)
- Operating Conditions: Primarily −20 °C (also −10, 0, 25 °C and 45/10 °C in the temperature series); 3C/3C accelerated aging; charge 0.33–3C with 3C discharge and vice versa; 1C cycling with voltage windows 2.50–3.80 V to 3.40–4.20 V; up to 150 cycles
- Degradation Markers: Capacity fade, ohmic/polarization/total resistance growth, OCV shift at low SOC, change in thermal runaway indices

## Keyword Context

- [[capacity-degradation|Capacity Degradation]]: Charge/discharge capacity retention is tracked every 25 cycles up to 150 cycles as a function of temperature, C-rate and DOD/DOC at low temperature.
- [[thermal-runaway|Thermal Runaway]]: ARC Heat-Wait-Search tests on fully charged cells after 0, 15, 25, 75 and 150 low-temperature cycles give T1, T2, T3 and maximum self-heating rates.
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]: OCV, HPPC resistance and capacity fade are compared across ambient temperatures from −20 °C to 45 °C to quantify the effect of low temperature.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To reveal capacity and internal-resistance degradation laws and the thermal runaway safety evolution of Sony US18650VTC6 cells cycled at low temperature (−20 °C) under different temperatures, C-rates and DOD/DOC; approach: Experimental

> Evidence: "Cycling and charging/discharging experiments under low temperatures were conducted to collect realistic battery data."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: collect degradation and safety data for LIBs aged at low temperature; tests: 3C CC-CV/3C CC accelerated aging at −20 °C (groups aged to 0–150 cycles), C-rate matrix (0.33–3C charge/discharge) at −20 °C, 3C/3C aging at −20 to 45 °C with HPPC every 25 cycles, DOD/DOC voltage-window cycling at 1C and −20 °C, HPPC (1C 10 s discharge, 40 s rest, 0.75C 10 s charge every 10% SOC), ARC Heat-Wait-Search thermal runaway tests; data origin: Own experiments

> Evidence: "Thermal runaway tests were conducted for cells under different aging cycles, that is, fresh, 15th, 25th, 75th, and 150 th cycles."

### Q3: Ambient Boundary Conditions

**Answer:** −20 °C primary (temperature series at −20, −10, 0, 25 and 45 °C per Table 3; the capacity analysis names −20, −10, 0, 10 and 25 °C) via a low-temperature chamber rated to −40 °C; stability/tolerance: ±2 °C chamber accuracy

> Evidence: "low-temperature chamber to −40 °C, providing ±2 °C accuracy"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Cell temperature during cycling is not reported as analyzed (the authors list cell surface temperature monitoring as future work; the data acquisition unit offers ±0.1 °C temperature accuracy); during ARC tests the cell temperature was tracked to obtain T1–T3; sensor type, count, placement, attachment and sampling not reported

> Evidence: "thermal monitoring analysis of cell surface temperature may also be conducted"

### Q6: Temperature-Dependent Performance

**Answer:** At −20 °C, fresh cells had ohmic, polarization and total resistances of 109.0, 44.2 and 153.3 mΩ, i.e. 5.6, 3.3 and 4.7 times the 25 °C values; OCV at low SOC rises markedly below 0 °C (at 0% SOC >3.2 V at −10 °C and >3.6 V at −20 °C for cells aged 125–150 cycles)

> Evidence: "At −20 °C, fresh batteries have ohmic, polarization, and total resistances of 109.0 m Ω, 44.2 mΩ, and 153.3 m Ω, respectively"

### Q7: Temperature-Dependent Aging

**Answer:** Across −20 °C to 25 °C with 3C/3C cycling, lower temperature accelerated degradation: after 150 cycles 83.3% capacity retained at 25 °C versus 74.2% at −20 °C; polarization resistance grew 28.9% at −20 °C vs 13.5% at 25 °C; ohmic resistance grew 15.4% at 25 °C, 19.7% at 0 °C and 12.4% at −20 °C; total resistance growth peaked at −10 °C (20.8%)

> Evidence: "capacity re- tained at 25 °C versus 74.2% retained at −20 °C"

### Q8: Model Purpose and Type

**Answer:** Not explicitly discussed.

### Q9: Model Parameterization and Validation

**Answer:** Not explicitly discussed.

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Not explicitly discussed.
