---
cell_target: "A123 Systems ANR26650M1-B"
doi: "https://doi.org/10.1038/s41598-025-16329-2"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Electrochemical-Thermal Model"
  - "Multi-Temperature Evaluation"
  - "Heat Generation"
---

# Investigating thermal dynamics in cylindrical Li-ion batteries across varied temperatures based on electrochemical principles

## General Analysis

**Core Thesis:** The paper experimentally validates a cascaded multi-layer electrochemical-thermal model (Single Particle Model driving a 306-state layer-resolved thermal network) for the ANR26650M1B (Lithium Werks/A123) 26650 LiFePO4 cell at four ambient temperatures. It shows good agreement at 21, 0 and 40 °C but significant deviations at -10 °C, which the authors attribute to temperature-independent thermal parameters calibrated at room temperature.

**Methodological Focus**
- Testing Mode: Repeated CCCV charge (10 A to 3.45 V, CV until 0.125 A) / CC discharge (10 A to 2.0 V) with 60 s rests; surface temperature measurement with Type K thermocouples
- Operating Conditions: Environmental chamber at 21 °C (100 cycles), 0 °C, 40 °C and -10 °C (10 cycles each per the text); ±10 A
- Degradation Markers: Discharge capacity evolution over cycles at four ambient temperatures

## Keyword Context

- [[electrochemical-thermal-model|Electrochemical-Thermal Model]]: A cascaded SPM-plus-multi-layer thermal model resolving 38 spiral-wound layers (306 thermal states) is the core object validated against measurements on the target cell.
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]: The model is validated at 21 °C, 0 °C, 40 °C and -10 °C ambient, with case-temperature RMSE rising to 6.0 °C at -10 °C.
- [[heat-generation|Heat Generation]]: Electrochemical heat generation is computed as S(t) = V(t)|I(t)| from the SPM terminal voltage and fed into the thermal network.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study experimentally validates a multi-layer electrochemical-thermal model of the ANR26650M1B cell across sub-zero, room and elevated ambient temperatures to resolve internal temperature gradients; approach: Hybrid

> Evidence: "this study focuses exclusively on experimentally validating the multi-layer formulation under a broader range of ambient temperatures"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: provide voltage and surface-temperature data for model validation (per ASME V&V 10 principles); tests: repeated cycles of CCCV charge at 10 A to 3.45 V (CV until 0.125 A), 60 s rest, CC discharge at 10 A to 2.0 V, 60 s rest, performed with a Neware BTS-4000 tester at 21 °C (100 cycles), 0 °C, 40 °C and -10 °C (10 cycles each according to the text) with 24 h rest between conditions; a single cell was used throughout; cell also disassembled to identify 38 layers; data origin: Own experiments

> Evidence: "constant current-constant voltage (CCCV) charging at 10 A until reaching a cutoff voltage of 3.45 V"

### Q3: Ambient Boundary Conditions

**Answer:** 21, 0, 40 and -10 °C via an ESPEC BTU-433 benchtop environmental chamber, stabilized for one hour before each test; stability/tolerance: not reported

> Evidence: "Prior to each test, the environmental chamber was set to the target ambient temperature and allowed to stabilize for one hour"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Type K thermocouples (accuracy ±1 °C) × 3 along the external surface; attachment: thermally conductive tape; no internal sensors; sampling: not reported

> Evidence: "Three sensors were mounted along the external surface using thermally conductive tape to ensure good thermal contact and reliable surface readings."

### Q6: Temperature-Dependent Performance

**Answer:** At 0 °C and -10 °C the time to complete the same number of cycles increased relative to 21 °C and 40 °C (slower kinetics); at 40 °C the measured surface peak temperature was 48.7 °C (model 47.5 °C); discharge capacity was initially low at 0 °C and 40 °C and increased in subsequent cycles

> Evidence: "the total duration of the test increases as the ambient temperature decreases"

### Q7: Temperature-Dependent Aging

**Answer:** Across 21, 0, 40 and -10 °C, the authors state that their discharge-capacity trends mirror the literature, with -10 °C accelerating capacity degradation while 21 °C and 40 °C maintain relatively stable performance; early capacity jumps are attributed to transient kinetic limitations rather than degradation reversal. (Note: the Fig. 8 caption lists 100 cycles for all temperatures, whereas the setup text states 10 cycles for 0, 40 and -10 °C.)

> Evidence: "sub-zero ( −10◦C ) ambient temperatures accelerate capacity degradation, while moderate temperatures (e.g., 21◦C and 40◦C) maintain relatively stable performance"

### Q8: Model Purpose and Type

**Answer:** Purpose: predict terminal voltage and resolve internal component temperatures (electrolyte, separators, electrodes, collectors, casing) and hotspots; type: cascaded electrochemical-thermal model (Single Particle Model + multi-layer lumped thermal resistance network with 306 states), compared to a single-layer formulation; thermal component: Yes

> Evidence: "Together with the electrolyte and outer casing, this configuration results in a total of 306 thermal states."

### Q9: Model Parameterization and Validation

**Answer:** Parameters from literature (Table 1 thermal and electrochemical parameters from ref. 46) with layer count from cell disassembly; thermal parameters and resistances calibrated at room temperature (stated as 20 °C/21 °C); validated against own voltage and case-temperature measurements: voltage RMSE 0.482 V (21 °C), 0.24 V (0 °C), 0.46 V (40 °C), 0.18 V (-10 °C); case-temperature RMSE 1.99 °C (multi-layer) vs 2.39 °C (single-layer) at 21 °C, 2.0 °C (0 °C), 2.1 °C (40 °C), 6.0 °C (-10 °C)

> Evidence: "Table  1 presents the thermal and electrochemical parameters used in the simulation, which were obtained from46."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Radially layer-resolved lumped network (38 spiral-wound layers × 8 components plus electrolyte and case; axial heat exchange neglected via adiabatic ends); represented inhomogeneities: radial core-to-surface/component-level temperature differences (internal temperatures predicted up to 15 °C above surface at 21 °C); no axial or tab effects

> Evidence: "It is assumed that the battery ends are adiabatic, with minimal axial heat exchange42"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: ambient 21, 0, 40 and -10 °C under ±10 A CCCV/CC cycling of a single cell; explicitly reported limitations: temperature-independent thermal parameters cause a cooling delay at 0 °C and 40 °C and large deviations at -10 °C; constant, temperature-independent solid diffusion coefficients; SPM neglects electrolyte dynamics; no internal temperature sensors for validation of internal predictions

> Evidence: "These discrepancies highlight the model’s limitations under extreme cold and motivate the incorporation of temperature-dependent thermal properties"
