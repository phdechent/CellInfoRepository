---
cell_target: "Sony-Murata US18650VTC6"
doi: "https://doi.org/10.1016/j.csite.2025.106580"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Battery Thermal Management"
  - "Air Cooling"
  - "Metal Foam"
---

# Comparative analysis of innovative cooling systems for Li-ion cells using carbon-graphene coatings, metal foams, and 3D printing

## General Analysis

**Core Thesis:** The paper experimentally compares unconventional cooling solutions for Li-ion cells: carbon/graphene coatings and a 3D-printed liquid-cooling channel plate on a Li-polymer flat cell, and an Al 6082 metal-foam frame (with and without a Peltier cold point) for a two-cell series pack of US18650VTC6 cells. For the VTC6 pack, the metal-foam frame reduced the stabilized temperature increment by 20 % and the frame plus Peltier cell by 46 % relative to plastic support, and a Bernardi-based temperature-rise-per-heat metric shows cylindrical cells heat more than flat cells.

**Methodological Focus**
- Testing Mode: Pulsed current test on a two-cell series 18650 pack with infrared thermography (heating to 4500 s, cool-down to 5050 s)
- Operating Conditions: Test box with monitored dry-bulb temperature and relative humidity, dehumidifier, no active air-velocity control (natural convection); ambient values not reported
- Degradation Markers: None

## Keyword Context

- [[battery-thermal-management|Battery Thermal Management]]: Thermal management options for the VTC6 pack (plastic support, metal-foam frame, metal-foam frame with Peltier cell) are compared by the surface-averaged temperature increment.
- [[air-cooling|Air Cooling]]: The metal-foam frame dissipates heat to surrounding air by natural convection in the passive configuration, giving a 20 % lower temperature increment than the plastic-supported reference.
- Metal Foam: A high-porosity Al 6082 alloy foam frame produced by lost-PLA casting acts as both mechanical support and heat dissipator for the 18650 cells.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To experimentally compare unconventional cooling configurations, including a metal-foam frame with and without a Peltier cold point for US18650VTC6 cells, in terms of temperature increment versus internal heat generation; approach: Experimental (with Bernardi-equation heat-generation analysis)

> Evidence: "A comparison between the three configurations has been performed in terms of the cell increment of temperature versus cell internal heat generation."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: evaluate heat-dissipation performance of support/cooling configurations; tests: pulsed current test of two VTC6 cells in series in three configurations (A plastic support, B metal-foam frame, C metal-foam frame with Peltier cell) with infrared imaging, heating to 4500 s and cool-down to 5050 s (details referred to an earlier work); data origin: Own experiments

> Evidence: "Three configurations are tested as shown in Fig. 5 : A) cells with plastic support (reference case); B) cells mounted on the metal foam-based frame"

### Q3: Ambient Boundary Conditions

**Answer:** Not reported numerically; ambient dry-bulb temperature and relative humidity monitored in a black-painted test box with a dehumidifier and no active air-velocity control; stability/tolerance: not reported

> Evidence: "The environmental conditions are monitored at dry-bulb temperature and relative humidity."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Infrared camera × 1 (320 × 256 pixels, 3.0-5.5 μm) viewing the cell surface from 1 m, plus a K-type thermocouple on the battery surface to validate the camera reading; attachment: not reported; sampling: 0.1 Hz (camera, 260 μs exposure)

> Evidence: "The acquisition frequency is 0.1 Hz, and the exposure time is 260 μs. The camera is at 1 m from the battery."

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: quantify internal heat generation to normalize the temperature rise for comparing cooling solutions; type: Bernardi heat-generation equation (irreversible polarization plus reversible entropic term); a 0-D electro-thermal model was calibrated with flat-cell (non-target) channel-plate tests; thermal component: Yes

> Evidence: "This is mathematically derived from the well-established Bernardi equation [ 34 ]"

### Q9: Model Parameterization and Validation

**Answer:** Heat generation computed from measured current and voltage via the Bernardi equation; the 0-D electro-thermal model was calibrated with the 3D-printed channel-plate tests on the flat cell (not the target cell); validation metrics: not reported

> Evidence: "Tailored 3D-printed channel plates for liquid cooling have allowed adequate control of the cell temperature and have also been used to calibrate a 0-D electro-thermal model."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (0-D) for the electro-thermal model; represented inhomogeneities: none in the model (2D surface temperature fields were only measured by infrared imaging and then surface-averaged)

> Evidence: "have also been used to calibrate a 0-D electro-thermal model"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: not reported; explicitly reported limitations: constant-current loading far from real operation, single-cell/small-pack tests not representative of heat flow in a full battery pack, prismatic cells not addressed

> Evidence: "the application of a constant current load to a cell is very far from the real operation"
