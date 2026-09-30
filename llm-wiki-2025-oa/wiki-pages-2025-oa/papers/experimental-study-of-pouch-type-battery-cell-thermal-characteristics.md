---
cell_target: "Kokam SLPB120216216G1H"
doi: "https://doi.org/10.3390/batteries12010014"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Battery Thermal Management"
  - "Electrochemical-Thermal Model"
  - "Heat Generation"
---

# Experimental Study of Pouch-Type Battery Cell Thermal Characteristics Operated at High C-Rates

## General Analysis

**Core Thesis:** The paper experimentally characterises the surface temperature distribution of a 57 Ah SolarEdge (formerly Kokam) SLPB120216216G1H NMC pouch cell during charging and discharging at 0.5-2 C using heat flux sensors, thermocouples and thermal imaging, and validates a 3D NTGK (MSMD) model in Ansys Fluent against the measured maximum temperatures (average deviation about 4.5%). It finds the tab region hottest, a top-to-bottom face gradient up to about 4 °C, and that the face exceeds 35 °C from about 1.35 C without cooling.

**Methodological Focus**
- Testing Mode: Constant-current discharge and CCCV charging with surface temperature/heat flux sensing and infrared thermography; 3D NTGK electrochemical-thermal simulation
- Operating Conditions: Charge up to 4.2 V and discharge to 2.7 V at 0.5, 1, 1.5 and 2 C (1 C = 57 A), without active cooling; simulations additionally at 4 C and 5 C
- Degradation Markers: None

## Keyword Context

- [[battery-thermal-management|Battery Thermal Management]]: The measured face temperature gradients and tab heating are used to argue for additional cooling, especially of the upper cell face, above about 1.5 C.
- [[electrochemical-thermal-model|Electrochemical-Thermal Model]]: A 3D multi-scale multi-domain NTGK model in Ansys Fluent predicts cell voltage and temperature at 0.5-5 C and matches measured maximum temperatures with about 4.5% average deviation.
- [[heat-generation|Heat Generation]]: The NTGK volumetric heat source comprises ohmic, reaction and entropic terms, and experiments show heat concentrating near the tabs at higher C-rates.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To develop and validate a numerical model predicting the thermal behaviour of the 57 Ah pouch cell under various charge/discharge conditions and to experimentally quantify face temperature distribution, gradients and the effect of C-rate on heating; approach: Hybrid

> Evidence: "The aim of this research is to develop and validate a numerical model of pouch-type lithium-ion battery cells that accurately predicts thermal behavior"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: assess cell temperatures and face temperature gradients during charging/discharging at different intensities and validate the NTGK model; tests: full charge to 4.2 V (CC-CV via bench supply up to 60 A) and discharge to 2.7 V (CBA Amplifier 10X) at 0.5, 1, 1.5 and 2 C with heat flux/thermocouple and thermal imaging measurements; data origin: Own experiments

> Evidence: "At the start of this study, the battery cell was fully charged and discharged, charging up to 4.2 V and discharging until the battery cell voltage dropped to 2.7 V"

### Q3: Ambient Boundary Conditions

**Answer:** Ambient temperature not reported; tests performed without active cooling (cell face at 22.3 °C at the start of 2 C discharge); stability/tolerance: not reported

> Evidence: "Since this study was performed without active cooling"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Heat flux sensors with thermocouples × 8 on the cell face at tabs (C-1, C-2), top (T-1, T-2), middle (M-1, M-2) and bottom (B-1, B-2), plus FLIR T335 thermal imager over the whole face (matt adhesive tape, emissivity 0.95); attachment: not reported for sensors; sampling: thermal images at 10 min intervals, sensor rate not reported

> Evidence: "8 heat flux sensors with thermocouples were installed on the cell face"

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: predict electrochemical and thermal behaviour (voltage and temperature distribution) of the cell at different discharge C-rates; type: MSMD NTGK semi-empirical electrochemical-thermal model in Ansys Fluent; thermal component: Yes

> Evidence: "The NTGK model is used in this numerical study."

### Q9: Model Parameterization and Validation

**Answer:** Parameters from NTGK Y and U functions obtained by fitting experimental voltage/current curves (dataset used for fitting not explicitly specified); validated against own measured maximum cell temperatures at 0.5-2 C discharge with an average deviation of about 4.54% (1.41-6.22% per C-rate)

> Evidence: "the average difference between the simulation and the experimental data is about 4.54%"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** 3D; represented inhomogeneities: temperature distribution over the cell with highest temperature at the junction between tabs (contacts) and cell body

> Evidence: "The highest temperature was recorded in the cell body at the junction between the contacts and the body."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: discharge at 0.5, 1, 1.5 and 2 C (maximum temperature comparison); 4 C and 5 C were only simulated without experimental comparison; explicitly reported limitations: none stated

> Evidence: "0.5 29.7 27.85 6.22 1 30.3 28.55 5.77 1.5 37.6 35.81 4.76 2 39.4 38.85 1.41 4 - 48.51 - 5 - 54.02 -"
