---
cell_target: "A123 Systems AMP20M1HD-A"
doi: "https://doi.org/10.1016/j.ohx.2025.e00679"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Electronic DC Load"
  - "Hybrid Pulse Power Characterization"
  - "Open-Source Hardware"
---

# Low-cost electronic DC load module design for battery capacity evaluation

## General Analysis

**Core Thesis:** The paper presents an open-source, modular master-slave electronic DC load (MSEL, up to 50 W and 20 A per module) for battery and power-supply testing. The A123 AMP20M1HD LiFePO4 cell (3.3 V, 19.5 Ah) serves as the device under test to validate the load's constant-current, constant-resistance, constant-power, battery-capacity and HPPC modes against a high-accuracy reference meter.

**Methodological Focus**
- Testing Mode: Constant-current (20 A), constant-resistance (0.1 Ω) and constant-power (100 W) discharge for 30 min; 1C capacity discharge to 2.5 V; HPPC pulse discharge to 2.5 V
- Operating Conditions: 1C discharge to 2.5 V cut-off; ambient temperature not reported
- Degradation Markers: None

## Keyword Context

- Electronic DC Load: The paper's contribution is a low-cost, scalable electronic DC load whose control accuracy is validated by discharging the target cell.
- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]: A dedicated Battery HPPC mode automatically generates discharge pulses and rest periods, demonstrated on the target cell down to 2.5 V.
- Open-Source Hardware: Schematics, PCB layouts, firmware and bill of materials (total $282.108) are released under CC BY 4.0 as an alternative to commercial loads.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study designs a low-cost, modular electronic DC load and uses the A123 AMP20M1HD cell as the test object to validate its stability and accuracy in five operating modes, including battery capacity and HPPC testing; approach: Experimental

> Evidence: "The 123-AMP20M1HD lithium-ion battery, with a nominal voltage of 3.3 V and a capacity of 19.5 A h , was used as the test object."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: validate the stability, accuracy and adaptability of the electronic load under real conditions; tests: 30-min CC (20 A), CR (0.1 Ω) and CP (100 W) discharges; 1C battery-capacity discharge to 2.5 V (18.918 Ah from the device vs. 18.928 Ah from the PCS-1000 reference); HPPC pulse test to 2.5 V; an additional 30-min 20 A test on a 3.3 V LiFePO4 battery to assess MOSFET thermal balancing; data origin: Own experiments

> Evidence: "For the battery capacity and HPPC modes, the test was executed until the cut-off voltage of 2.5 V was reached to verify the testing device’s functionality in battery applications."

### Q3: Ambient Boundary Conditions

**Answer:** Not explicitly discussed.

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

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
