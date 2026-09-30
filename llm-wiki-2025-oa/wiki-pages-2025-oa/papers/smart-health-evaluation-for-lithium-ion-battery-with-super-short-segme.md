---
cell_target: "CATL CB2W0; Lishen LP27148134"
doi: "https://doi.org/10.1002/advs.202503583"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Both"
tags:
  - literature_extraction
  - "State-of-Health Estimation"
  - "Incremental Capacity Analysis"
  - "Machine Learning"
---

# Smart Health Evaluation for Lithium‐Ion Battery With Super‐Short‐Segment Charging

## General Analysis

**Core Thesis:** The paper proposes a degradation-mechanism-guided Scale-Invariant Feature Transform (DoG-TVA) method that automatically extracts health features from incremental capacity curves of very short charging segments, fused with an ANN for SOH estimation. Own long-term cycling data of 40 Ah LISHEN LP27148134 and 280 Ah CATL CB2W0 LFP cells (plus EVE cells and public CALCE, Oxford and MST datasets) are used, with SOH RMSE down to 1.97% even for 10% DOD charging segments.

**Methodological Focus**
- Testing Mode: Long-term galvanostatic CCCV cycle-life testing with periodic capacity calibration (every 10 cycles); partial-DOD cycling
- Operating Conditions: 25 °C ambient (±0.2 °C); LISHEN at 2C, 1C, 0.3C with 100% and 60% DOD (2.0–3.65 V), plus 10 h 45 °C stress for 2C cells; CATL at 0.5C (140 A) with 100%, 60%, 40% and 10% DOD
- Degradation Markers: Capacity fade (SOH), IC peak shift/diminishing attributed to LLI and LAM

## Keyword Context

- [[state-of-health-estimation|State-of-Health Estimation]]: SOH, defined as the ratio of remaining to initial capacity, is the target estimated from charging-curve features for LISHEN, CATL, EVE and public-dataset cells.
- [[incremental-capacity-analysis|Incremental Capacity Analysis]]: IC curves are the input from which the DoG-TVA algorithm automatically extracts peak, valley and inflection features even when conventional IC peaks disappear at 10% DOD.
- [[machine-learning|Machine Learning]]: An ANN maps the automatically extracted DoG-TVA features to SOH, trained on one cell and tested on other cells of the same condition.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To estimate SOH accurately from super-short charging segments by automatic, degradation-mechanism-guided feature extraction from IC curves combined with an ANN, validated on multiple cell types including LISHEN 40 Ah and CATL 280 Ah LFP cells; approach: Hybrid

> Evidence: "Asmartmethodisproposedfor accuratebatteryhealthestimationusingsuper-shortchargingsegments."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: generate long-term degradation data under different charging currents and DODs to train and validate the SOH estimator; tests: LISHEN CCCV cycle-life tests at 2C, 1C, 0.3C and 100%/60% DOD until 70% capacity with 0.3C capacity calibration every ten cycles and a 10 h 45 °C temperature stress; CATL CCCV cycling at 140 A (3.65 V, CV cut-off 14 A, discharge to 2.0 V) with 0.5C calibration every 10 cycles and 40%/10% DOD cycling; data origin: Both (own LISHEN/CATL/EVE data plus public CALCE, Oxford and MST datasets)

> Evidence: "ForLISHENbatteries,cycle-lifetestswereconducteduntilthe cell capacity deteriorated to 70% of the nominal capacity."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via temperature-controlled chamber (45 °C applied for 10 h as a temperature stress for LISHEN 2C cells); stability/tolerance: ±0.2 °C

> Evidence: "Allbatteryagingcycleswereconductedatacontrolledtemperature( ±0.2°C)."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Across 25 °C cycling and a 10 h 45 °C temperature stress (simulating thermal-management failure) applied to LISHEN 2C 100% and 60% DOD cells, a downward capacity trend was attributed to the increased ambient temperature; no further multi-temperature aging comparison was made

> Evidence: "Thedownwardtrend(bluecurve)in(D)isattributedtothe increaseofambienttemperature,whichissetto45 °Cforadurationof10hourstosimulatethecaseofthermalmanagementfailure."

### Q8: Model Purpose and Type

**Answer:** Purpose: estimate battery SOH from automatically extracted IC-curve features; type: data-driven (DoG-TVA feature extraction plus artificial neural network); thermal component: No

> Evidence: "AnANNmodelisusedhereintoestimatethebatterySOHwith the extracted health features"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from ANN training on one cell per condition (Cell 1) with features extracted automatically without parameter tuning; calibrated with own LISHEN/CATL/EVE cycling data and public datasets; validated against the remaining cells (Cells 2 and 3) using RMSE (e.g., LISHEN test RMSE 0.93–1.87%, CATL 40% DOD 2.33%, 10% DOD 1.97%)

> Evidence: "one battery (Cell 1) is selected as the training dataset, while the others (Cell 2 & 3) serve as the testing dataset."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 25 °C for LISHEN, CATL, EVE and CALCE cells (40 °C Oxford, 30 °C MST), C-rates 0.3–2C for LISHEN and 0.5C for CATL, DOD 100%, 60%, 40% and 10%, with added measurement noise; explicitly reported limitations: dynamic temperature systems and pack-level analyses were not investigated and are left for future research

> Evidence: "such as dynamic tempera- ture systems and battery pack-level analyses, remains challeng- ing due to the signiﬁcantly higher costs"
