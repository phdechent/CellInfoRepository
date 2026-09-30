---
cell_target: "EVE EVE-INR18650 33V"
doi: "https://doi.org/10.3390/batteries11020073"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "X-Ray Computed Tomography"
  - "Capacity Degradation"
  - "X-Ray Beam Damage"
---

# Lab-Scale X-Ray Exposure Has No Measurable Impact on Lithium-Ion Battery Performance and Lifetime

## General Analysis

**Core Thesis:** The study evaluates whether lab-scale X-ray exposure (2 min and 60 min scans with a 225 kV rotating-anode source) affects the performance and lifetime of EVE INR18650-33V NMC/graphite cells. Fifteen cells in three groups (control, 2 min, 60 min) were characterized by reference performance tests, aggressively cycled for 300 cycles and CT-scanned; no statistically significant differences in energy, rate, lifetime or swelling were found.

**Methodological Focus**
- Testing Mode: Reference performance tests (C/20, C/5, C/2 charge/discharge), CC-CV galvanostatic cycling (C/2 charge, 1C discharge) for 300 cycles, X-ray exposure and CT scanning
- Operating Conditions: RPTs at 33 °C and cycling at 45 °C in convection-based temperature chambers; 2.5-4.2 V; X-ray at 210 kV and 190 µA
- Degradation Markers: Discharge capacity retention at C/20, C/5 and C/2, capacity vs. cycle number, and jellyroll core area (swelling proxy)

## Keyword Context

- [[x-ray-computed-tomography|X-Ray Computed Tomography]]: CT scans (2 min and 60 min exposures, Nikon XT H 225 ST) are the X-ray exposure studied, and post-cycling CT scans quantify core area as a swelling proxy.
- [[capacity-degradation|Capacity Degradation]]: Discharge capacity over 300 cycles at 45 °C and across three RPTs showed no statistically significant difference between exposed and control groups.
- X-Ray Beam Damage: Exposed doses of ~10 Gy (2 min) and ~300 Gy (60 min) were estimated and found to have no measurable impact on performance or lifetime.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To determine whether lab-scale X-ray exposure affects the performance and lifetime of EVE INR18650-33V cells; approach: Hybrid (experiments with supporting dose and 1D X-ray absorption calculations)

> Evidence: "In this work, we evaluate the impact of lab-scale X-rays on battery performance and lifetime."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: compare performance and lifetime of X-ray-exposed and unexposed cells; tests: initial RPT (C/20, C/5, C/2 CC charge to 4.2 V and discharge to 2.5 V), X-ray exposure (2 min or 60 min), second RPT, 300 cycles (C/2 CC-CV charge to 4.2 V with 62 mA cutoff, 1C discharge to 2.5 V), final RPT, 2-min CT scan; five cells per group; temperature monitoring during X-ray exposure (Figure S5); data origin: Own experiments

> Evidence: "Fifteen cells were placed into one of three experimental groups for a total of five cells per group."

### Q3: Ambient Boundary Conditions

**Answer:** 33 °C for RPTs and 45 °C for cycling via convection-based temperature chambers; stability/tolerance: not reported

> Evidence: "Cycling tests were performed in convection -based temperature chambers set to 45 °C to accelerate cell aging."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Cell temperature was measured during X-ray exposure (Figure S5), confirming negligible heating; sensor type, count, placement, attachment and sampling: not reported

> Evidence: "Our measurements of cell temperature during X -ray exposure confirm ed this result (Figure S5)."

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: estimate the fraction of X-rays absorbed by the cell and the worst-case X-ray-induced temperature rise; type: simplified 1D X-ray absorption model (SpekPy spectrum simulation through can and 40 electrode stacks) plus a lumped heat-capacity estimate (ΔT = Q/mc); thermal component: Yes (simple heat-capacity calculation giving 0.3 K worst case)

> Evidence: "We then use d the SpekPy Python package to simulate X -ray absorption in this system [58]."

### Q9: Model Parameterization and Validation

**Answer:** Parameters from component thicknesses estimated from a CT radial slice, assumed 50 % porosity, beam settings (210 kV, 40°, 2.5 mm Al filter) and a literature-based heat capacity of 1000 J kg−1 K−1; calibrated with: not reported; validated against own cell-temperature measurement during X-ray exposure (Figure S5), which confirmed negligible heating

> Evidence: "We estimated the thickness of each major component via measurements of a “radial slice” (Supplementa ry Figure S4)."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** 1D; represented inhomogeneities: layered can/current collector/electrode stack along the X-ray path; the authors approximated cylindrical geometry by scaling with the average chord length (π/4)

> Evidence: "In other words, our 1D model overestimate d X-ray absorption through a cylindrical battery."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 2 min and 60 min exposures at 210 kV/190 µA on EVE INR18650-33V cells; explicitly reported limitations: 1D model overestimates absorption; conclusions may not hold for other cell formats (e.g., prismatic), chemistries (e.g., sodium-ion), cycling conditions, or beyond 300 cycles due to latent degradation

> Evidence: "we cannot guarantee that these conclusions woul d hold for other test conditions."
