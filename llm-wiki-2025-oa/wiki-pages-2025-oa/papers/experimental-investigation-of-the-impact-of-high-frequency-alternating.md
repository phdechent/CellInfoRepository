---
cell_target: "Panasonic-Sanyo NCR18650GA"
doi: "https://doi.org/10.1016/j.fub.2025.100036"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "diamond"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Alternating Current Heating"
  - "Capacity Degradation"
  - "Electrochemical Impedance Spectroscopy"
---

# Experimental investigation of the impact of high-frequency alternating current on heating a Li-ion cell at subzero temperatures and its effect on lifetime

## General Analysis

**Core Thesis:** The study experimentally examines whether internal heating of a 3.5 Ah Panasonic/Sanyo NCR18650GA cell with a high-frequency (up to 250 kHz) boost-converter-based AC heater accelerates ageing. Heated cells are compared with current-mirrored reference cells over 100 measurement cycles, either with ~1800 periodic heating cycles from about −9 °C to 10 °C or with continuous heating at 25 °C ambient, attributing the ~7 % extra capacity fade of periodically heated cells mainly to mechanical stress from rapid temperature changes rather than to the alternating current.

**Methodological Focus**
- Testing Mode: High-frequency AC self-heating with superimposed DC discharge, current-mirrored reference discharge, C/20 capacity checks, EIS (250 kHz-10 mHz) at five cell voltages, waveform measurements
- Operating Conditions: Periodic heating at T_amb = −10 °C (cell heated to 10 °C, cooled below −9 °C) with charge/discharge at 25 °C; continuous fan-cooled heating at T_amb = 25 °C; characterization at 25 °C ± 2 °C; 3.15-4.15 V cycling window, 750 mA charge/discharge
- Degradation Markers: Capacity fade (C/20 Coulomb counting), ohmic resistance increase ΔR_AC and ΔR_DC from EIS

## Keyword Context

- Alternating Current Heating: A boost-converter heater generates a triangular alternating current (I_AC ≈ 10 A RMS, up to 250 kHz) superimposed on a discharge current to heat the cell internally from subzero temperatures, with an initial heating rate of 15.6 K/min.
- [[capacity-degradation|Capacity Degradation]]: Periodically heated cells retained 86.3-86.9 % capacity versus 92.8-93.4 % for reference cells after 100 measurement cycles, while continuously heated cells showed about 94.1 % versus 94.8 %.
- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]: EIS at 4.2, 4.0, 3.6, 3.2 and 2.8 V showed that the ageing difference between periodically heated and reference cells lies mainly in the ohmic region (ΔR_AC).

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To determine how high-frequency alternating-current self-heating at subzero temperatures, and the current ripples themselves, affect ageing of the NCR18650GA cell; approach: Experimental (with supporting equivalent-circuit and analytical heater equations)

> Evidence: "This study seeks to integrate the effects of current ripples and the heating process in relation to the ageing of the cell."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: separate ageing caused by the heating process and by AC ripples from that of a normal discharge; tests: 100 measurement cycles on heated cells and current-mirrored reference cells (couples 1-3: periodic heating at −10 °C ambient, ~1800 heating cycles; couples 4-7: continuous fan-cooled heating at 25 °C with external inductances of 0-1000 nH, 250-35.71 kHz), C/10 discharge and C/20 charge capacity checks, EIS at five voltages before and after cycling, current/voltage waveform measurements every 350 mAh; data origin: Own experiments

> Evidence: "In this work, 3 cells and 3 reference cells were measured, mostly referred to as cell couple 1 to 3 consisting of the matched cells"

### Q3: Ambient Boundary Conditions

**Answer:** −10 °C ambient for periodic heating steps and 25 °C for charge/discharge and continuous-heating tests via a climate chamber; characterization at 25 °C ± 2 °C; stability/tolerance: ± 2 °C (characterization); minor heat-cycle variations were attributed to air-flow differences in the climate chamber

> Evidence: "The entire process was conducted at an ambient temperature of T amb = 25 °C ± 2 °C."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Cell surface temperature of heated (T_Cell,heat) and reference (T_Cell,ref) cells was measured and used as the control variable for heating (stop at 10 °C, restart below −9 °C); sensor type, count, placement, attachment and sampling: not reported

> Evidence: "Heat up the cell with the HF-Heater to T Cell = 10 °C, wait 30 min to reach a cell surface temperature of below T Cell = −9 °C"

### Q6: Temperature-Dependent Performance

**Answer:** From about −10 °C, the heated cell reached 10 °C within 74 s (initial heating rate 15.6 K/min; average ~11 K/min over all cycles); rising cell temperature lowered R_DC, increasing cell voltage and discharge current, and at 25 °C ambient the lower R_DC led to higher I_DC during heating (maximum cell temperature 44 °C)

> Evidence: "Due to a lower cell resistance R DC at higher cell temperatures, the current I DC will be higher"

### Q7: Temperature-Dependent Aging

**Answer:** Across reference cells, those discharged at lower temperature (T_Cell,ref ≈ −9.6 °C) aged faster than those at ≈ 25 °C despite lower current (Q_ref 92.8-93.4 % vs. ~94.8 %); periodically heated cells (average ~0 °C) retained < 87 %, which the authors attribute to mechanical stress from rapid temperature changes; in continuous-heating tests, cells with higher average temperature showed higher capacity fade

> Evidence: "By comparing the reference cells, we observed faster ageing ( Q ref ) for the cell at a lower temperature during discharge ( T Cell,ref ), despite the lower current"

### Q8: Model Purpose and Type

**Answer:** Purpose: describe the frequency-dependent cell impedance and estimate the heater currents I_DC and I_AC from cell- and heater-specific values; type: equivalent circuit model (series inductance, R_L1||L1, R0, two RC elements with Warburg impedance) plus analytical power-loss balance of the heater; thermal component: No (power losses only, no thermal model)

> Evidence: "Now it is possible to estimate I DC and I AC using cell-specific and heater-specific values"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from own measurements (system inductance measured at L ≈ 170 nH; EIS used to characterize the cell), with R_DC, R_AC and L_Cell treated as constant; calibrated with: not reported; validated against: not explicitly reported (measured I_DC and I_AC reported, no quantitative model-error metric)

> Evidence: "The inductance of the system was measured to be approximately L ≈ 170 nH."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: not explicitly reported; explicitly reported limitations: the high-frequency R_L1||L1 term is excluded in later calculations, resistances and inductance are assumed constant, the Warburg expression is valid only for an infinite diffusion layer; the ageing test covers one cell type only

> Evidence: "For further calculations, we will simplify the high-frequency path by excluding the term R L1 in parallel with L 1 ."
