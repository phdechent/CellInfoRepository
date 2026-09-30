---
cell_target: "Samsung SDI INR21700-50E"
doi: "https://doi.org/10.1016/j.csite.2025.107013"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Fast Charging"
  - "Lithium Plating"
  - "Electrochemical-Thermal Model"
---

# Development of a fast-charging strategy considering degradation in lithium-ion batteries

## General Analysis

**Core Thesis:** The paper develops an advanced single-particle model with SEI growth, lithium plating and a lumped thermal balance to analyse how C-rate and temperature drive degradation of Samsung SDI INR21700-50E NCA cells during fast charging. A lithium plating generation map over C-rate, SOC and temperature is used to design a Thermal-Boost Fast Charging (TBFC) profile that charges within 20 min, and own experiments show it extends cycle life by 170% compared with 2.1C CCCV charging.

**Methodological Focus**
- Testing Mode: Constant-current charging at 0.6-3C for model validation; repeated fast-charge cycling (CCCV at 2.1C vs. TBFC multi-step profile) with SOH tracking; cell temperature by thermocouple
- Operating Conditions: Charging from SOC 0.05 to 0.75 within 20 min (CCCV at 2.1C with 4.2 V cut-off, TBFC starting at 3C); cut-off 4.2 V/2.5 V; current stopped above 55 °C cell temperature; simulated parametric range 25-55 °C
- Degradation Markers: SOH/capacity fade, charging voltage rise, modelled SEI thickness and lithium plating

## Keyword Context

- [[fast-charging|Fast Charging]]: A Thermal-Boost Fast Charging profile that starts at 3C and steps down with SOC is proposed to charge within 20 min and is compared experimentally with 2.1C CCCV charging.
- [[lithium-plating|Lithium Plating]]: Lithium plating overpotential is modelled to map plating rate versus C-rate, SOC and temperature, and plating is found to cause about 72% of capacity loss at 2.1C.
- [[electrochemical-thermal-model|Electrochemical-Thermal Model]]: A single-particle model with polynomial electrolyte approximation, SEI/plating side reactions and a lumped heat balance predicts voltage, temperature and SOH of the cell.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To analyse the effects of C-rate and temperature on degradation (SEI growth and lithium plating) of the INR21700-50E during fast charging with an advanced single-particle model and to derive and experimentally verify a cycle-life-extending fast-charging strategy; approach: Hybrid

> Evidence: "This study develops an advanced single-particle model to analyze the effects of C-rate and temperature on lithium-ion battery degradation during fast charging."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: validate the advanced SPM (voltage, temperature, SOH) and demonstrate the fast-charging strategy; tests: CC charging from 0.6C to 3C in 0.6C steps, temperature during charging, repeated charge-discharge cycling for SOH, and cycling with TBFC versus CCCV at 2.1C (SOC 0.05-0.75 within 20 min); data origin: Own experiments

> Evidence: "SOH of the battery was compared between the proposed fast-charging strategy and conventional constant current–constant voltage (CCCV) charging through experimentation."

### Q3: Ambient Boundary Conditions

**Answer:** Experimental ambient temperature not reported; current automatically stopped when cell temperature exceeded 55 °C (model assumes initial cell temperature of 25 °C); stability/tolerance: not reported

> Evidence: "To prevent overheating, the supplied current was automatically stopped by the electric contactor when the battery temperature exceeded 55 °C."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Thermocouple × count not reported at location not reported; attachment: not reported; sampling: not reported (indicator NX-9, measurement uncertainty about ±0.5%)

> Evidence: "The battery temperature was measured using a thermocouple connected to an indicator (NX-9, HANYOUNG NUX, Korea)."

### Q6: Temperature-Dependent Performance

**Answer:** At 25 °C to 55 °C (model-based parametric study at 1.8C), charging voltage decreases from 4.18 V to 4.04 V and activation overpotential from 0.175 V to 0.104 V with increasing temperature

> Evidence: "When the temperature increases from 25 °C to 55 °C, the charging voltage decreases from 4.18 V to 4.04 V."

### Q7: Temperature-Dependent Aging

**Answer:** Across 25 °C to 55 °C (model-based), increasing temperature improves lithium-ion diffusivity and reduces the lithium plating rate by a factor of nine; no experimental aging comparison across temperatures was reported

> Evidence: "increasing the temperature from 25 °C to 55 °C improves lithium-ion diffusivity, reducing lithium plating by a factor of nine."

### Q8: Model Purpose and Type

**Answer:** Purpose: predict charging voltage, temperature and degradation (SEI growth and lithium plating) to map lithium plating and design a fast-charging strategy; type: advanced single-particle electrochemical model with polynomial electrolyte approximation and degradation side reactions, plus lumped heat balance; thermal component: Yes

> Evidence: "Moreover, the model also considered the effect of temperature during charging conditions."

### Q9: Model Parameterization and Validation

**Answer:** Parameters listed in Tables 1 and 2 (source not explicitly stated in text); validated against own measured CC charging voltages at 0.6-3C (accuracy 96.63%, maximum error 5.47% at 3C), charging temperature (accuracy about 96.7%) and SOH over repeated cycles (error around 9%)

> Evidence: "The model closely matched the experimental data, achieving an accuracy of 96.63 %."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** 1D through-thickness electrolyte concentration (polynomial approximation across negative electrode, separator, positive electrode) with single-particle radial approximation; lumped thermal; represented inhomogeneities: electrolyte concentration across the cell sandwich and particle surface-to-average concentration difference

> Evidence: "we employed a polynomial approximation as shown in Fig. 1 (b)"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: CC charging 0.6C-3C, charging temperature rise, SOH over repeated charging cycles (about 120-170 cycles in fast-charging tests); parametric study limited to 25-55 °C; explicitly reported limitations: larger error at 3C due to large electrode-electrolyte concentration differences, SOH error increasing with cycles because SEI decomposition, plating dissolution and SEI-plating interaction are not modelled

> Evidence: "This discrepancy arises because the model does not account for the decomposition of the SEI layer and the dissolution of lithium plating over extended cycles"
