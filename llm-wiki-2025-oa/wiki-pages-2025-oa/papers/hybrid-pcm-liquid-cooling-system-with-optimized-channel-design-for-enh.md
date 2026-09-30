---
cell_target: "Samsung SDI INR18650-30Q"
doi: "https://doi.org/10.3390/en18184996"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Phase Change Material"
  - "Liquid Cooling"
  - "Computational Fluid Dynamics"
---

# Hybrid PCM–Liquid Cooling System with Optimized Channel Design for Enhanced Thermal Management of Lithium–Ion Batteries

## General Analysis

**Core Thesis:** The study experimentally compares PCM (paraffin/1-tetradecanol), silicone oil, thermally conductive adhesive and air as cooling media for a 3p pack of Samsung INR18650-30Q cells during 2C discharge, then uses a validated STAR-CCM+ model to design a hybrid PCM-indirect liquid cooling system. PCM reduced peak surface temperature by 47 % versus air, and the best channel layout (D) lowered surface temperature by a further 9 °C (17.8 %) relative to PCM alone, with 0.108 L/min identified as the optimal flow rate.

**Methodological Focus**
- Testing Mode: Constant-current 2C discharge from 4.2 V to 2.5 V with multi-point thermocouple measurements, repeated three times; CFD parametric study of channel designs, flow rates and 1C-5C discharge
- Operating Conditions: 20 °C ambient in a temperature-controlled chamber; 2C discharge (experiments); simulated 1C-5C and coolant flow 0.005-1.08 L/min
- Degradation Markers: None

## Keyword Context

- [[phase-change-material|Phase Change Material]]: PCM filling the pack (described as paraffin wax with a 40 °C melting point; Table 2 lists 1-tetradecanol properties) gave the lowest maximum surface temperature (52.7 °C vs. 126.1 °C air-cooled) and the longest isothermal maintenance time (56 min), but only about 37 % of the PCM had melted after 30 min.
- [[liquid-cooling|Liquid Cooling]]: Four indirect water-cooling channel configurations (A-D) beneath the PCM-filled pack were compared numerically, with configuration D achieving the lowest surface temperature and highest heat transfer coefficient (209.2 W/m2·K).
- [[computational-fluid-dynamics|Computational Fluid Dynamics]]: STAR-CCM+ simulations with the NTGK battery model, enthalpy-porosity PCM phase change and a 1 mm tetrahedral mesh reproduced the measured maximum surface temperature within 1 %.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To evaluate PCM and other media as cooling materials for an INR18650-30Q pack and to design a hybrid PCM-liquid cooling system with optimized channel geometry and flow rate; approach: Hybrid

> Evidence: "Numerical simulations were conducted to systematically assess the thermal performance of the proposed design."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: compare cooling media and validate the numerical model; tests: 2C constant-current discharge of a 3p INR18650-30Q pack (4.2 V to 2.5 V) with PCM, silicone oil (KF-96), thermally conductive adhesive (PK-404DM) and air (no medium), each repeated three times, plus post-discharge natural cooling; data origin: Own experiments

> Evidence: "The batteries were discharged at a 2 C -rate, beginning from an initial voltage of 4.2 V and continuing until the cell voltage decreased to 2.5 V."

### Q3: Ambient Boundary Conditions

**Answer:** 20 °C via a temperature- and humidity-controlled chamber (JEIO TECH TH3-KE-025); stability/tolerance: chamber resolution/error listed as ±0.3 °C

> Evidence: "All testing was carried out within a temperature -controlled ch amber set to 20 °C ambient conditions."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** K-type thermocouples × 3 per cell (top, middle, bottom; three cells) plus thermocouples on the external enclosure wall and at the PCM center; attachment: affixed to each cell (method not specified); sampling: 1 s intervals via a Graphtec GL840 data logger

> Evidence: "three K -type thermocouples were affixed to each cell at the top, middle, and bottom positions."

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: predict battery surface temperature, temperature distribution and PCM melting for different cooling media, channel designs, flow rates and C-rates; type: 3D CFD (STAR-CCM+) with the NTGK semi-empirical electro-thermal battery model and enthalpy-porosity PCM phase-change model; thermal component: Yes

> Evidence: "the Newman –Tiedemann – Geske–Kim (NTGK) semi -empirical model was utilized to numerically investigate both thermal and electrical responses within a lithium–ion battery cell"

### Q9: Model Parameterization and Validation

**Answer:** Parameters: NTGK coefficients described as experimentally determined, PCM properties from Table 2 (literature), constant battery thermal conductivity and specific heat, external h = 5 W/m2·K; mesh and time-step independence studies (1 mm, 2 s); validated against own measured surface temperature of the PCM pack during 2C discharge (predicted 50.6 °C vs. measured 51.2 °C, error below 1 %)

> Evidence: "The predicted maximum battery surface temperature was 50.6 °C, while the measured value was 51.2 °C, yielding a relative error under 1%."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** 3D; represented inhomogeneities: temperature distribution within the pack and PCM (top and side views), PCM liquid-fraction distribution around the cells, and effects of cooling-channel layout on battery surface temperature

> Evidence: "A tetrahedral unstructured mesh was constructed throughout the domain, ap- plying a grid size of 1 mm in both the battery and PCM zones."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 2C discharge of the PCM-filled pack at 20 °C ambient (channel, flow-rate and 1C-5C cases are purely numerical); explicitly reported limitations: battery thermal conductivity and specific heat assumed constant; at ≥4C the hybrid system cannot keep temperatures within limits and operation ≤2C is advised; long-term durability at the optimal flow rate requires further research

> Evidence: "During the simulation, the battery ’s thermal conductivity and specific heat were taken to be constant through discharge"
