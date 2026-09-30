---
cell_target: "LG Chem E66A"
doi: "https://doi.org/10.3390/wevj16060296"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Fast Charging"
  - "Electric Vehicle Energy Consumption"
  - "800 V Architecture"
---

# Quantifying the State of the Art of Electric Powertrains in Battery Electric Vehicles: Comprehensive Analysis of the Two-Speed Transmission and 800 V Technology of the Porsche Taycan

## General Analysis

**Core Thesis:** The paper characterizes a 2022 Porsche Taycan Performance Battery Plus (93.4 kWh gross, 198s2p LG Chem E66A NMC721 pouch cells per literature) at vehicle level, covering driving resistances, two-speed powertrain efficiency, range at different ambient temperatures and the 800 V battery system in charging and discharging. For the battery, a measured cell internal resistance is used to quantify ohmic losses, and DC fast charging is compared with a 400 V Volkswagen ID.3.

**Methodological Focus**
- Testing Mode: Vehicle coast-down tests, chassis dynamometer driving cycles (WLTC, FTP-75, HWFET, Urban, Interurban, Highway), climate-chamber warm-up and constant-velocity tests, 22 kW AC and 800 V DC charging with onboard OBD-II logging; cell internal resistance pulse test (1C, 10 s discharge pulse at 50% SOC) in a thermal chamber
- Operating Conditions: Vehicle tests at 23 ± 2 °C reference, −7 °C and 35 °C ambient; DC charging from 5% to 100% SOC starting at 35 °C battery system temperature; cell resistance at 20 °C
- Degradation Markers: None

## Keyword Context

- [[fast-charging|Fast Charging]]: 800 V DC charging from 5% to 100% SOC reached a peak of 262.2 kW and took 57.22 min, with power reduced to keep the battery system temperature at or below 54 °C.
- Electric Vehicle Energy Consumption: Range and energy consumption were measured in official and real-world cycles and at −7, 23 and 35 °C, e.g. 17.94 kWh/100 km and 519.3 km in the WLTC.
- 800 V Architecture: The 800 V battery system is compared with the 400 V ID.3, showing lower ohmic battery losses during discharge and a lower share of ohmic losses during charging.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To quantify vehicle dynamics, powertrain efficiency, range and the two-speed transmission and 800 V battery system of the Porsche Taycan (whose battery uses the LG Chem E66A cell), using a measured cell resistance to split battery ohmic losses; approach: Hybrid (vehicle and cell measurements with an analytical energy-loss breakdown)

> Evidence: "This study details vehicle dynamics, electric powertrain efficiencies, their impact on vehicle level, and the two technological advancements."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: obtain vehicle-level data on range, efficiency and charging, and the cell internal resistance for battery loss calculation; tests: cell internal resistance with a 1C, 10 s discharge pulse at 50% SOC and 20 °C (thermal chamber, BaSyTec MRS 6 V cycler with two parallel channels); vehicle coast-down, dynamometer range tests, climate-chamber warm-up and constant-velocity tests, 22 kW AC charging and 800 V DC charging (5-100% SOC); data origin: Own experiments

> Evidence: "Ri = 1.243 mΩ was measured in reference conditions of 50% SOC, 20 ◦C, 1 C, and a 10 s discharge pulse"

### Q3: Ambient Boundary Conditions

**Answer:** Cell resistance test: 20 °C via a Vötsch VC3 4100 thermal chamber; vehicle tests: 23 ± 2 °C reference plus −7 °C and 35 °C via a climate chamber; stability/tolerance: ± 2 °C for the reference vehicle tests, not reported for the cell test

> Evidence: "The internal resistance of the cells was measured in aVC3 4100 thermal camber"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** No cell-mounted sensor reported; battery system temperature was read from the vehicle's onboard signals via the OBD-II data logger during DC charging (rising to and held at 54 °C); attachment: not applicable; sampling: not reported

> Evidence: "after 14 min, it is maintained at a temperature of 54 ◦C for 4 min"

### Q6: Temperature-Dependent Performance

**Answer:** At vehicle level only: at −7 °C ambient, energy consumption was highest over the entire constant-velocity range (largest relative deviation at 10 km/h), and after warm-up in the WLTC it was still 35.3% higher (22.6 vs 16.7 kWh/100 km) than at 23 °C; 35 °C gave a near-constant 4.2% higher consumption than 23 °C; during DC charging, power reduction after ~9 min coincided with the battery system temperature limit of 54 °C. Cell-level temperature dependence was not reported.

> Evidence: "After 9 min, the charging control reduces the power to ensure that the battery system temperature does not exceed the 54 ◦C."

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: split energy losses along the powertrain and quantify internal battery (ohmic) losses; type: analytical energy-loss balance with a lumped ohmic battery loss term based on cell resistance, current per parallel string and number of cells; thermal component: No

> Evidence: "The internal battery losses or, rather, ohmic losses, represent the final group"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from the authors' own cell pulse-resistance measurement (Ri = 1.243 mΩ) and vehicle-measured battery currents; calibrated with onboard vehicle data from the driving cycles and DC charging; validated against: not reported (results compared with the Volkswagen ID.3 study)

> Evidence: "Ri = 1.243 mΩ was measured in reference conditions of 50% SOC, 20 ◦C, 1 C, and a 10 s discharge pulse"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (single resistance value applied to all cells); represented inhomogeneities: none

> Evidence: "According to Equation (9), the ohmic losses depend on cell resistances and currents."

### Q11: Model Applicability and Limitations

**Answer:** Not explicitly discussed.
