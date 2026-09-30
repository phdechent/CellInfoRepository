---
cell_target: "Melasta SLPBB042126"
doi: "https://doi.org/10.1016/j.csite.2025.106474"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Both"
tags:
  - literature_extraction
  - "Immersion Cooling"
  - "Computational Fluid Dynamics"
  - "Fast Charging"
---

# Thermal analysis of nanofluid submerged battery tab under fast charging conditions

## General Analysis

**Core Thesis:** The study investigates immersion cooling of the tabs of a Melasta SLPBB042126 6600 mAh LCO pouch cell with silicone-oil-based nanofluids during fast charging, using experimentally extracted cell parameters and a test bed to validate a 3D CFD model. Tab cooling is compared with surface cooling, and the effects of nanoparticle type (SiO2, Al2O3, CuO), concentration, flow rate and two serpentine channel structures for a seven-cell parallel pack are evaluated numerically.

**Methodological Focus**
- Testing Mode: HPPC internal resistance test, entropic coefficient measurement, CC-CV charging with surface temperature measurement under natural convection and nanofluid tab cooling; CFD simulation
- Operating Conditions: 25 °C ambient in a temperature/humidity chamber; 2C CC charge to 4.2 V then CV to 0.05C (experiment); 2C and 4C charging (simulation); nanofluid flow 15–75 ml/min
- Degradation Markers: None

## Keyword Context

- [[immersion-cooling|Immersion Cooling]]: Only the cell tabs (tab cooling) or only the cell surface (surface cooling) are submerged in circulating silicone-oil-based nanofluid to remove heat during charging.
- [[computational-fluid-dynamics|Computational Fluid Dynamics]]: A 3D transient ANSYS Fluent model with a two-phase mixture nanofluid model and laminar flow predicts cell and pack temperature fields.
- [[fast-charging|Fast Charging]]: Cooling performance is evaluated at 2C (the manufacturer's maximum charge rate) and 4C charging, where tab cooling reduced the cell temperature difference by 82.8 % compared with surface cooling at 4C.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study evaluates silicone-oil-based nanofluid immersion cooling of battery tabs versus surface cooling for a pouch cell and a seven-cell pack under fast charging; approach: Hybrid

> Evidence: "developing a test bed for the validation of a Computational Fluid Dynamics nanofluid immersion cooling model"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: extract cell parameters (internal resistance, entropic coefficient) and provide temperature data to validate the CFD model; tests: HPPC pulse test for internal resistance versus SOC, entropic coefficient measurement with temperature steps of 30/25/20/30 °C at SOC intervals, 2C CC-CV charging (discharged to 3 V, charged to 4.2 V, CV to 0.05C) under natural convection and under tab cooling with 1 % SiO2 nanofluid at 15 ml/min, each trial repeated three times; SEM of nanoparticles; data origin: Both (own experiments plus comparison with experimental results of Spitthoff et al. for natural convection)

> Evidence: "Fig. 10 illustrates a comparative analysis of the numerical simulation and experimental data under two conditions: natural convection and battery tab cooling under 2C charging."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via a temperature and humidity test chamber (GD-JS4005, Shanghai Haixiang) in a controlled temperature and humidity room, with 1 h stabilization before testing; stability/tolerance: not reported

> Evidence: "The battery was charged at a constant current rate of 2C to a voltage of 4.2 V at an ambient temperature of 25 °C"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** T-type thermocouples × 7 on the cell surface (T1 positive electrode/tab region, T2 negative electrode region, T3–T7 along the casing), read by a UNI-T UT3216 multi-channel temperature tester; attachment: not reported; sampling: not reported

> Evidence: "Thermocouples at T1 and T2 were used to monitor temperature changes at the positive (T1) and negative (T2) electrode regions, while T3 through T7 measured temperatures along the battery casing."

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: predict cell and pack temperature distributions under nanofluid tab and surface immersion cooling during 2C/4C charging; type: 3D transient CFD model (ANSYS Fluent) with Bernardi heat generation, anisotropic heat conduction, tab Joule heating and a two-phase mixture laminar nanofluid model; thermal component: Yes

> Evidence: "A three-dimensional simulation model incorporating gravity, transient conditions and laminar model was developed to study lithium-ion pouch cells and batteries with an immersion cooling design."

### Q9: Model Parameterization and Validation

**Answer:** Parameters from the authors' own HPPC internal resistance test and entropic coefficient measurement, specific heat and anisotropic thermal conductivity calculated from cell material parameters, tab heat from current collector resistivity and nanofluid thermophysical properties from tabulated values; validated against the authors' own 2C charging experiments (natural convection and 1 % SiO2 tab cooling) and literature data of Spitthoff et al., with a maximum RMSE of 1.33 °C and maximum %Error of 3.50 %

> Evidence: "From the figure, it can be seen that the max RMSE is 1.33 °C and max %Error is 3.50 %."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** 3D; represented inhomogeneities: tab-region heat generation and temperatures, in-cell surface temperature differences, anisotropic in-plane/through-plane conduction, and cell-to-cell temperature differences in a seven-cell parallel module (internal heat generation in the active region assumed uniform)

> Evidence: "The simulation model considers only the active material region and assumes uniform internal heat generation, ignoring radiation effects."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 2C charging at 25 °C ambient under natural convection and tab cooling with 1 % SiO2 nanofluid at 15 ml/min (simulations extended to 4C, other nanofluids, concentrations, flow rates and a seven-cell pack); explicitly reported limitations: uniform internal heat generation and neglected radiation assumed; tab-only cooling can over-cool so that the lower cell surface becomes warmer than the upper section; effects on thermal runaway, lifetime and coolant compatibility left for future work

> Evidence: "Excessive cooling can cause the temperature of the lower section of the lithium battery surface to exceed that of the upper section, leading to an increased temperature differential."
