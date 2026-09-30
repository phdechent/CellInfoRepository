---
cell_target: "Samsung SDI INR21700-50G"
doi: "https://doi.org/10.3390/wevj16050255"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Capacity Degradation"
  - "Lithium Plating"
  - "Reversible Capacity Loss"
---

# The Overlooked Role of Battery Cell Relaxation: How Reversible Effects Manipulate Accelerated Aging Characterization

## General Analysis

**Core Thesis:** Using Samsung SDI INR21700-50G (NCA/silicon-graphite) cells extracted from a Lucid Air, the study shows that continuous cycling in accelerated aging tests builds up lithiation and conducting-salt inhomogeneities that cause partly reversible capacity loss, which recovers during check-ups and rest. Shorter cycling interruptions, larger DOD and higher C-rates intensify inhomogenization, which precedes lithium plating and cell failure, whereas static or dynamic recovery cycles roughly double cycle life.

**Methodological Focus**
- Testing Mode: Galvanostatic cycle aging with pre-rest and post-rest check-ups every 100 cycles (C/3 discharge capacity, C/15 pOCV, HPPC DC resistance), 10 h rest phases, capacity difference analysis, end-of-discharge voltage tracking and lithium stripping (differential voltage) analysis
- Operating Conditions: 25 °C ambient in climate chambers; substudies on cycling interruption (1C/1C, 20-100% SOC), DOD (0-100% to 70-80% SOC at 1C/1C), C-rate (0.5C/0.5C, 1C/0.37C, 1C/1C, 2C/2C at 0-100% SOC) and static/dynamic recovery cycles
- Degradation Markers: Capacity fade (to 70-80% of initial), DC resistance increase, capacity differences CD C-rate and CD resting, end-of-discharge voltage shift, lithium stripping plateaus, knee point and cell failure

## Keyword Context

- [[capacity-degradation|Capacity Degradation]]: Relative capacity fade measured before and after 10 h rest reveals that shorter cycling interruptions produce up to four times fewer cycles before reaching 80% capacity.
- [[lithium-plating|Lithium Plating]]: Lithium stripping plateaus in the rest-phase differential voltage confirm lithium plating shortly before the knee point and cell failure in highly inhomogenized cells.
- Reversible Capacity Loss: Capacity recovered during check-ups and rest (CD resting) is used to quantify the reversible share of capacity loss caused by inhomogeneous lithium distribution.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To investigate how the test procedure and stress factors (DOD, C-rate) affect the formation and rehomogenization of cell inhomogeneities in the INR21700-50G and how relaxation methods can counteract them in accelerated aging tests; approach: Experimental

> Evidence: "This work investigates the impact of the test procedure and several stress factors, namely depth of discharge and C- rate, on the formation and rehomogenization of cell inhomogeneities."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: quantify reversible versus apparent aging under different test designs and stress factors; tests: initial characterization (mean 4.83 Ah, 26 mΩ); cycle aging with pre-rest CU (C/3 capacity, C/15 pOCV), 10 h rest and post-rest CU (C/3, C/15 discharge/charge, HPPC) every 100 cycles; Substudy 1 stepwise removal of CU elements and rest (1C/1C, 20-100% SOC); Substudy 2 DOD variation at 1C/1C; Substudy 3 C-rate variation at 0-100% SOC; Substudy 4 static rest at 6/23/56% SOC or dynamic C/15 charge relaxation; one cell per condition (three cells for 1C/1C at 100% DOD); data origin: Own experiments

> Evidence: "CUs are performed on a regular basis every 100 cycles directly after cycling (pre-rest) and after the subsequent ten-hour rest (post-rest)."

### Q3: Ambient Boundary Conditions

**Answer:** 25 °C via a Memmert IPP110eco and a BINDER KB115 E4 climate chamber without additional active temperature control; stability/tolerance: not reported (small temperature fluctuations between cells due to location in the chamber could not be precluded)

> Evidence: "E4 climate chamber (BINDER GmbH, Tuttlingen, Germany) at a constant ambient tempera- ture of 25◦Cwithout additional active temperature control"

### Q4: Mechanical Boundary Conditions

**Answer:** None reported; magnitude: not reported; fixture: Arbin single-cell battery holders with 4-wire sensing, horizontal orientation

> Evidence: "The cells were electrically connected with Arbin single-cell battery holders"

### Q5: Cell Temperature Measurement

**Answer:** NTC thermistor on the cell surface (count per cell not stated), measured throughout the entire experiment; end-of-charge and end-of-discharge surface temperatures reported in Appendix B; attachment: not reported; sampling: not reported

> Evidence: "The cells’ surface temperatures were measured throughout the entire experiment using a negative temperature coefficient thermistor."

### Q6: Temperature-Dependent Performance

**Answer:** At 25 °C ambient, cell self-heating during the first cycles after check-up and rest raised the surface temperature and increased the end-of-discharge voltage as polarization decreased; in the 2C/2C case, stronger self-heating was assumed to reduce inhomogenization initially and raised pre-rest check-up capacities, distorting the capacity difference calculation. No controlled variation of ambient temperature was performed.

> Evidence: "This temperature rise is accompanied by an increase in end-of-discharge voltage, as cell polarization decreases."

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
