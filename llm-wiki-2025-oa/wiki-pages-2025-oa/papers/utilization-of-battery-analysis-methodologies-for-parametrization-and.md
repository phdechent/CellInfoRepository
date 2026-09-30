---
cell_target: "LG Chem INR21700 M50T"
doi: "https://doi.org/10.1007/s41104-025-00150-0"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Both"
tags:
  - literature_extraction
  - "Electrochemical Impedance Spectroscopy"
  - "Open-Circuit Voltage"
  - "Electrochemical-Thermal Model"
---

# Utilization of battery analysis methodologies for parametrization and enhancement of an electrochemically approximated simulation model approach for thermal management battery system tests

## General Analysis

**Core Thesis:** The paper replaces a literature-based electrochemical sub-model of a real-time electrochemical-thermal cell model (used to drive a heatable replacement cell for thermal-management test benches) with an equivalent circuit parameterized from own EIS and OCV measurements on LG INR21700 M50T cells. The updated model is validated against discharge, pulse, energy-characteristic and SOC-determination cycles and shows improved voltage and transient prediction versus the previous model.

**Methodological Focus**
- Testing Mode: EIS (0.1 Hz–10 kHz, 500 mA amplitude) at five SOC points; pseudo-OCV measurements on charge and discharge; constant-current discharge, pulse and energy/performance characteristic cycles for validation
- Operating Conditions: EIS reference temperature 20 °C; 5 A (1.05C) discharges at 40, 25, 0 and −20 °C ambient; pulses of 15, 10 and 5 A; constant discharges 0.5–15 A to 2.5 V or 55 °C surface temperature
- Degradation Markers: None (cells measured at SOH 100%)

## Keyword Context

- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]: EIS spectra of four M50T cells at 100, 80, 50, 20 and 0% SOC were averaged and fitted in Zahner Thales to obtain SOC-dependent ECM elements.
- [[open-circuit-voltage|Open-Circuit Voltage]]: Separate charge and discharge OCV curves were measured on three cells at eleven SOC points with 30-min rests and transferred directly to the model as characteristic maps.
- [[electrochemical-thermal-model|Electrochemical-Thermal Model]]: The re-parameterized ECM is coupled to a thermal network model that computes heat transport through the cell layers to the surface for HiL replacement-cell operation.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To obtain a more precise, measurement-based parameterization of the ECM within an electrochemical-thermal simulation model of the LG INR21700 M50T cell and validate it against measured cycles and the previous literature-based model; approach: Hybrid

> Evidence: "The improved parametrization includes the measurement of several cells in terms of electrochemical impedance spectroscopy and open-circuit voltage"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: parameterize the ECM and OCV maps and validate the updated simulation; tests: EIS on four cells at 100/80/50/20/0% SOC (0.1 Hz–10 kHz, 500 mA), pseudo-OCV charge/discharge curves on three cells at 11 SOC points with 30-min rest, 0.5C discharge / 0.33C CCCV charge for SOC setting, 5 A discharges at four ambient temperatures, 15/10/5 A pulse discharges, constant-current energy characteristics at 0.5–15 A; data origin: Both (own EIS/OCV; validation cycles in-house or from BATEMO)

> Evidence: "were conducted for each cell at the specified SOC interpolation points, namely 100%, 80%, 50%, 20%, and 0%."

### Q3: Ambient Boundary Conditions

**Answer:** EIS parameters referenced to a measurement temperature of 20 °C; discharge validation at 40, 25, 0 and −20 °C ambient; control method and stability/tolerance: not reported

> Evidence: "The measurements were conducted at four ambient temperatures ( 40 ◦ C, 25 ◦ C, 0 ◦ C, and − 20 ◦ C)"

### Q4: Mechanical Boundary Conditions

**Answer:** No pressure constraint reported; magnitude: not reported; fixture: during EIS the cell was secured in a holding and contacting mandrel

> Evidence: "which was secured in the holding and contacting mandrel"

### Q5: Cell Temperature Measurement

**Answer:** Cell surface temperature recorded during discharge tests (also used as a 55 °C termination criterion); sensor type, count, placement, attachment and sampling rate not reported

> Evidence: "and surface temperature of the cell were recorded"

### Q6: Temperature-Dependent Performance

**Answer:** At −20 °C, the measured 5 A discharge showed a voltage dip at the beginning of discharge followed by relaxation, which the new temperature-dependent ECM predicted; at higher constant discharge currents the 55 °C surface-temperature limit was reached before the 2.5 V cut-off. No further quantitative temperature comparison of cell response is reported

> Evidence: "The voltage dip at the beginning of the measurement, along with its position"

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: real-time prediction of cell voltage, losses and temperature to operate a heatable thermal replacement cell in HiL thermal-management tests; type: equivalent circuit model (Rs, two RC elements, RC sub-element, Warburg element, charge/discharge OCV maps) coupled to a point-mass thermal network model; thermal component: Yes

> Evidence: "simulates the thermal processes through the cell layers to the surface by means of a thermal network model"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from own EIS spectra averaged over four cells and fitted per SOC point with Zahner Thales software (polynomial SOC dependence), own measured OCV maps, a linear temperature coefficient referenced to 20 °C, and empirically incorporated current dependence; validated against measured discharge, pulse, energy-characteristic and SOC-determination cycles (in-house and BATEMO) versus the previous model: mean discharge voltage deviation approx. 1.5% (<50 mV), pulse deviations below 0.1 V, median temperature error reduced from 0.14% to 0.05%

> Evidence: "the individual measurements of the four cells were averaged at each SOC interpolation point"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** 2D (symmetry-based 2D disc thermal network; the electrical ECM is lumped); represented inhomogeneities: temperature distribution through the cell layers to the surface; a 3D network of the entire cell is planned

> Evidence: "an increase in resolution from a symmetry-based 2D disc model to a 3D network of the entire cell"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: −20 to 40 °C ambient, 0.5–15 A constant discharge, 5–15 A pulses, fresh cells (SOH 100%); explicitly reported limitations: aging not measured (represented only by a simple RC element), current dependencies captured empirically rather than by EIS, thermal conduction through the layers underestimated and temperatures overestimated at points, thermal parameters not yet evaluated

> Evidence: "The evaluation was limited to parameters influenced by electrochemical processes; thermal parameters will be evaluated at a later stage."
