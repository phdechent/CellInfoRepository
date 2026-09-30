---
cell_target: "LG Chem INR21700 M50T"
doi: "https://doi.org/10.3390/en18215645"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Parameter Identification"
  - "Thevenin Equivalent Circuit"
  - "Pulse Discharge Test"
---

# Optimal Direct Parameter Extraction of a Lithium-Ion Equivalent Circuit Cell Model for Electric Vehicle Application

## General Analysis

**Core Thesis:** The paper compares the two dominant direct methods for extracting 3-RC Thevenin equivalent-circuit parameters from pulse-discharge relaxation curves, one without (Method 1) and one with (Method 2) capacitive compensation, using pulse discharge tests on the LG M50T NMC-811 cell at 0.5C, 0.8C and 1C. Model accuracy is assessed on pulse-discharge, WLTC and high-current transient profiles to recommend the preferable method for EV applications.

**Methodological Focus**
- Testing Mode: Pulse discharge (2% and 5% SOC steps with 1 h rests) using a Chroma 63204 programmable DC load; transient WLTC and high-current (HC) discharge profiles
- Operating Conditions: Pulse discharge at 0.5C, 0.8C and 1C; discharge only; ambient temperature not reported
- Degradation Markers: None

## Keyword Context

- [[parameter-identification|Parameter Identification]]: SOC-dependent ECM parameters are extracted from relaxation curves by bounded nonlinear least-squares fitting, and two direct extraction formulas are compared across three C-rates.
- Thevenin Equivalent Circuit: A Thevenin model with three parallel RC branches, implemented in Simulink with Coulomb counting, is the model being parameterized.
- Pulse Discharge Test: The pulse discharge protocol on the target cell provides the relaxation data for parameterization and is repeated at 0.5C, 0.8C and 1C to quantify the effect of characterization C-rate.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study aims to extract the optimal 3-RC ECM parameter set for the LG M50T cell with the two dominant direct methods and to compare their accuracy over transient load profiles at multiple C-rates; approach: Hybrid

> Evidence: "this paper aims to extract the optimal parameter set regarding the two dominant direct methods with an electrochemically based logic"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: obtain parameterization and validation data for the ECM and quantify the influence of characterization C-rate; tests: pulse discharge test (full charge and rest, then pulses removing 2% SOC ×10, 5% SOC ×12, and 2% steps for the last 20% SOC, each followed by 1 h rest) at 0.5C, 0.8C and 1C, plus WLTC and HC transient discharge profiles; current and voltage logged at 0.25 s with a redundant Hall-sensor/voltage-divider measurement; data origin: Own experiments

> Evidence: "the pulse discharge test was performed at 3 different C-rates: 0.5C, 0.8C, and 1C."

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

**Answer:** Purpose: predict the terminal voltage of the cell under EV transient loads as the basis for BMS algorithms; type: 3-RC Thevenin equivalent circuit model with SOC-dependent parameters and Coulomb-counting SOC, implemented in Simulink; thermal component: Not stated

> Evidence: "the chosen model is an ECM with three parallel branches"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from the authors' own pulse discharge data: OCV from the second relaxing point, R0 from the instantaneous voltage drop divided by pulse current, and RC branches from a trust-region nonlinear least-squares fit of a triple-exponential to each relaxation with time constants bounded by impedance-spectrum regions; RC values then computed via Method 1 (unscaled) or Method 2 (capacitive compensation); calibrated with pulse discharge data at 0.5C, 0.8C and 1C; validated against measured PD, WLTC and HC voltage responses using RMSE, maximum error, MAE and RSQ (e.g., 1C PD RMSE 15.78 mV for Method 1 vs. 9.99 mV for Method 2)

> Evidence: "(14) was fit to the curve using a nonlinear least squares optimization (15) and (16)"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (single-cell equivalent circuit); represented inhomogeneities: none

> Evidence: "Figure 1. 3-RC-equivalent circuit cell model."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: discharge only; parameter sets from 0.5C, 0.8C and 1C pulse discharge tested on PD, WLTC (average 1.014 A, 100% to 8.83% SOC) and HC (average 1.9742 A, 100% to 1.34% SOC) profiles; explicitly reported limitations: only discharge parameterization is considered; time-constant bounds are rough NMC impedance-spectrum bounds; increasing the parameterization C-rate introduces overshoot on lower-current profiles; Method 1 struggles on profiles well below its parameterization C-rate; a second optimization on the PD curve led to overfitting and worse transient performance

> Evidence: "The scope of this paper focuses only on the discharge parameterization of the cell"
