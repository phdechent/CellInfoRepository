---
cell_target: "Samsung SDI INR18650-25R"
doi: "https://doi.org/10.3390/batteries11020077"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Active Cell Balancing"
  - "Battery Management System"
  - "Cell-to-Cell Variation"
---

# Inductor-Based Active Balancing Topology with Wide Voltage Range Capability

## General Analysis

**Core Thesis:** The paper proposes an inductor-based cell-to-pack active balancing topology that operates over a wide cell voltage range, supports simultaneous multicell balancing with a balancing current independent of the imbalance level, and uses low-cost low-side gate drivers. The topology is verified experimentally on a five-cell series-connected pack of Li-ion INR18650-25R cells.

**Methodological Focus**
- Testing Mode: Balancer circuit verification (oscilloscope gate voltages and inductor current) and cell-voltage balancing tests (cell-by-cell, multicell, during charging and during discharging)
- Operating Conditions: Five-cell series pack charged to 20.532 V (top cell 4.2062 V); 175 kHz PWM at 70 % duty; 10 mV balancing threshold; ambient temperature not reported
- Degradation Markers: None

## Keyword Context

- Active Cell Balancing: The proposed topology transfers energy from individual high-voltage cells to the whole pack via inductors, reducing the cell voltage difference below 10 mV in 47 to 170 min depending on the test.
- [[battery-management-system|Battery Management System]]: The balancer is designed as a low-cost BMS solution compatible with a wide range of cell voltages without isolated power modules or high-side gate drivers.
- [[cell-to-cell-variation|Cell-to-Cell Variation]]: Cell capacity inconsistency and resulting voltage imbalance between the five series cells are the problem the balancer addresses.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study proposes and experimentally verifies a low-cost inductor-based active balancing topology with wide voltage range capability on an INR18650-25R lithium-ion pack; approach: Hybrid

> Evidence: "The presented experimental results verify the operation of the proposed balancer on a lithium-ion battery pack."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: validate the balancing topology and its low-cost driving circuit; tests: oscilloscope verification of MOSFET gate voltages and inductor current on the top cell, cell-by-cell balancing, multicell balancing, multicell balancing during charging with an external power supply and during discharging with a load, on a five-cell series pack of INR18650-25R cells; data origin: Own experiments

> Evidence: "To validate the proposed balancing topology and its low-cost driving circuit, a series of experiments were conducted."

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

**Answer:** Purpose: estimate the cell-to-pack energy-transfer efficiency and inductor current of the balancer and illustrate the balancing algorithm; type: analytical circuit equations of the balancer with simulated inductor current and simulated cell-voltage balancing (no electrochemical or equivalent-circuit cell model is described); thermal component: No

> Evidence: "The efficiency calculation does not consider eddy current losses in the inductor and copper plane below it, MOSFET reverse recovery, diode recovery, or energy consumed by the driving circuit."

### Q9: Model Parameterization and Validation

**Answer:** Parameters from component datasheets (diode forward voltage, MOSFET on-resistances, inductor resistance); the simulated inductor current waveform was compared with the measured oscilloscope waveform on the experimental board (qualitative agreement, no error metric reported)

> Evidence: "The measured result matches the simulation result shown in Figure 4."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: five-cell series INR18650-25R pack with the top cell at 4.2062 V, 175 kHz PWM with 70 % duty ratio; explicitly reported limitations: efficiency calculation neglects eddy current losses, reverse recovery and driving-circuit energy; peak inductor current differs slightly from simulation due to cell voltage difference and inductor tolerance; validation on larger modules and real-world applications is future work

> Evidence: "caused by the difference in cell voltage between the simulation and the actual test, as well as the tolerance of the inductor"
