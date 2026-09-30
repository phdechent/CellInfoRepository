---
cell_target: "Samsung SDI INR21700-40T"
doi: "https://doi.org/10.3390/en18236300"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Electrochemical Impedance Spectroscopy"
  - "Bus Plate Impedance Correction"
  - "Battery Module Design"
---

# Development of a Correction Algorithm for Structural Elements to Enhance EIS Measurement Reliability in Battery Modules

## General Analysis

**Core Thesis:** The paper analyzes how nickel bus plates distort EIS measurements of parallel-connected battery modules and develops a geometry-based correction algorithm with current-distribution and frequency-dependent correction factors to extract the pure module impedance. The algorithm is parameterized with EIS data of Samsung INR21700-40T single cells and 2P–4P modules and cross-validated on an LFP 3P module.

**Methodological Focus**
- Testing Mode: Electrochemical impedance spectroscopy (Hioki BT4560-50, 41 points from 0.1 Hz to 1 kHz) on standalone bus plates, single cells and 2P/3P/4P parallel modules
- Operating Conditions: 25 °C in a temperature chamber; 50 % SOC; 100 % SOH (fresh cells)
- Degradation Markers: None

## Keyword Context

- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]: EIS of individual INR21700-40T cells provides the ideal parallel-module reference impedance against which measured and corrected module spectra are compared.
- Bus Plate Impedance Correction: Bus plate impedance is predicted from geometry (resistance with an experimental correction coefficient and 3.7 nH/mm inductance) and subtracted with configuration- and frequency-dependent factors, reducing RMSE by 88–95 % for NCA modules.
- [[battery-module-design|Battery Module Design]]: Structural elements of parallel modules (nickel bus plates connecting 21700 cells) are identified as the source of impedance artifacts whose relative share grows with the number of parallel cells.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study aims to quantify and correct bus plate impedance artifacts in EIS measurements of parallel battery modules to extract the pure module impedance; approach: Hybrid

> Evidence: "This study presents a systematic analysis of bus plate effects on EIS meas- urements of parallel battery modules and develops a correction algorithm to extract pure module impedance."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: establish bus plate impedance equations, derive correction factors and validate the correction algorithm; tests: standalone EIS of six nickel bus plate samples (30/52/75 mm length, 0.15/0.2 mm thickness), EIS of individual INR21700-40T cells followed by EIS of the same cells in 2P, 3P and 4P configurations (41 log-spaced points, 0.1 Hz–1 kHz); data origin: Own experiments

> Evidence: "First, EIS measurements of each individual cell were conducted before configuring parallel modules to obtain reference data."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via a temperature chamber; stability/tolerance: not reported

> Evidence: "to elim- inate impedance changes due to temperature, measurements were conducted while maintaining 25 °C in a temperature chamber."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: predict bus plate impedance from geometric parameters and correct measured module EIS spectra; type: geometry-based resistance-inductance impedance model of the bus plate combined with a correction-coefficient model for current distribution (number of parallel cells) and frequency dependence; thermal component: No

> Evidence: "Through this equation, bus plate im pedance can be predicted using only the geometric parameters of the bus plate."

### Q9: Model Parameterization and Validation

**Answer:** Parameters from nickel resistivity, an experimentally derived resistance correction coefficient and an inductance per unit length of about 3.7 nH/mm from the authors' own standalone bus plate EIS; current-distribution coefficient β and frequency coefficients c determined by exhaustive grid search on the authors' own INR21700-40T 2P–4P data; validated against the ideal parallel impedance calculated from own single-cell EIS using RMSE and MAE (NCA RMSE reduced from 1.18–2.65 mΩ to 0.10–0.14 mΩ) and cross-validated on an independent SLC26700 LFP 3P module (RMSE 2.44 to 0.17 mΩ)

> Evidence: "An exhaustive search method was employed, with search ranges established based on measurement da ta analysis."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (module-level impedance correction); represented inhomogeneities: configuration-dependent current distribution through shared bus plates between parallel cells (mutual inductance neglected)

> Evidence: "in actual parallel modules, bus plates are located between each cell, and current is distributed to the cells at each branch point."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 25 °C, 50 % SOC, fresh cells (100 % SOH), 0.1 Hz–1 kHz, 2P–4P NCA modules and an LFP 3P module, with bus plate impedance of about 15–25 % of total impedance; explicitly reported limitations: not validated at very low temperatures, extremely low SOC or with excessive numbers of parallel cells; theoretical assumptions may need revision beyond 10 kHz, for high-current pulses, above 60 °C or for different cell geometries

> Evidence: "did not validate the method under extreme conditions such as very low temp eratures, extremely low SOC, or configura- tions with excessive numbers of parallel cells."
