---
cell_target: "Samsung SDI INR21700-40T"
doi: "https://doi.org/10.3390/en18051272"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Computational Fluid Dynamics"
  - "Battery Module Design"
  - "Cell-to-Cell Variation"
---

# A Modeling Technique for High-Efficiency Battery Packs in Battery-Powered Railway System

## General Analysis

**Core Thesis:** The paper uses 3D thermal-flow simulation (Ansys Fluent 2024 R2) to study how temperature gradients and terminal connection methods jointly cause cell-to-cell SOC/DOD deviation in a 4S3P railway battery module of Samsung INR21700-40T cells. The simulation is validated against the authors' own single-cell surface-temperature and voltage measurements under a railway driving profile at 25 °C, and a new terminal/cell connection configuration is proposed that reduces SOC deviation.

**Methodological Focus**
- Testing Mode: Single-cell railway vehicle driving profile (repeated 10 times) on a battery cycler with surface thermocouple and voltage measurement; 3D CFD simulation of a 4S3P module
- Operating Conditions: 25 °C chamber; railway station-to-station driving profile
- Degradation Markers: None

## Keyword Context

- [[computational-fluid-dynamics|Computational Fluid Dynamics]]: 3D thermal-flow analysis in Ansys Fluent 2024 R2, validated on a single cell, is used to incorporate temperature effects into the module analysis.
- [[battery-module-design|Battery Module Design]]: Single, center, diagonal and a proposed terminal connection method are compared for a 4S3P module with nickel interconnection plates.
- [[cell-to-cell-variation|Cell-to-Cell Variation]]: The maximum SOC deviation between cells at the end of a driving cycle is the evaluation metric, reduced to 0.00004 with the proposed connection method.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study aims to analyze how temperature distribution and terminal connection affect SOC/DOD deviation between INR21700-40T cells in a 4S3P module and to propose a connection method minimizing it, using a simulation validated on single-cell experiments; approach: Hybrid

> Evidence: "validated the simulation environment by comparing actual experimental and simulation results for a single cell"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: provide reference data to validate the single-cell simulation environment; tests: railway vehicle station-to-station driving profile applied with a battery cycler (Neware CT-4008T) and repeated 10 times, with measurement of cell surface temperature and voltage; data origin: Own experiments

> Evidence: "The measured surface temperature and voltage of the battery were collected as reference data for simulation validation."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via temperature chamber (Jeio-TECH LCH-11G-2C); stability/tolerance: not reported

> Evidence: "The experimental setup maintained a constant cell ambient temperature of 25◦C through a chamber"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Thermocouple (Neware CA-4008n, 16-bit resolution, ±1 °C measurement deviation) × count not reported at the cell surface; attachment: not reported; sampling: not reported

> Evidence: "Thermocouple (CA-4008n, Neware, Shenzhen, China)Resolution 16 Bit"

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: predict cell and module temperature distribution and the resulting cell-to-cell current and SOC deviation for different terminal connection methods; type: 3D thermal-flow (CFD) model in Ansys Fluent 2024 R2 with a Joule heat source based on SOC-dependent internal resistance, and Coulomb-counting SOC per cell; thermal component: Yes

> Evidence: "temperature effects were incorporated using Ansys Fluent 2024 R2, a three-dimensional heat flow simulation tool"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from literature (density 2887 kg/m3, specific heat 952 J/kg·K, thermal conductivity 0.87 W/m·K), Joule heating from current and SOC-dependent internal resistance, a single heat transfer coefficient and constant nickel-plate resistance; calibrated with not reported; validated against the authors' own single-cell voltage and surface temperature under the repeated railway profile at 25 °C, with maximum differences of 0.17 V (5%) and 0.74 °C (3%)

> Evidence: "The physical properties of this battery, referenced from previous research, are summarized in Table 1"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** 3D; represented inhomogeneities: module-level temperature gradient between central and peripheral cells, position-dependent internal resistance and current distribution from interconnection plate resistances, cell-to-cell SOC deviation in a 4S3P module

> Evidence: "The validated single-cell simulation model from Section 3.1 was expanded to a 4S-3P configuration"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: single cell at 25 °C under the railway vehicle driving profile; module results are simulation-only for one driving cycle; explicitly reported limitations: the proposed configuration is optimized only for the 4S3P structure and other configurations (e.g., 12S2P) require reanalysis; simulation differs from experiment by up to 5% in voltage and 3% in temperature

> Evidence: "the proposed module configuration exhibits certain limitations, as it is specifically optimized for the 4S-3P structure."
