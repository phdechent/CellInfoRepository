---
type: concept
aliases:
  - "Battery Dataset"
tags:
  - synthesis
---

# Battery Dataset

**Summary:** Four 2025 data descriptors publish their own measurements of commercial cells (CALB L148N58A, Samsung INR21700-50E, Molicel INR-21700-P42A, and a mixed NMC/NCA/LFP set) for model development, BMS validation and machine learning. They vary widely in sample size, temperature coverage, cell-temperature instrumentation and whether aging is included.

## Synthesized Knowledge

**Scope and purpose.** Two datasets characterize *fresh* cells to capture cell-to-cell variation. One covers eleven B-grade CALB L148N58A prismatic NMC/graphite cells (58 Ah), measured with C/20 capacity, HPPC (1C and C/3 pulses), EIS (0.01 Hz–3 kHz) and scaled WLTP/UDDS/US06 cycles (Source: [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]]). The other covers 12 of 45 screened Molicel INR-21700-P42A high-power cells, measured with capacity tests, high C-rate pulse/GITT tests up to 8C and EIS (10 mHz–10 kHz) for stochastic modelling (Source: [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]]). A third dataset is the largest by sample size: 256 Samsung INR21700-50E cells in 32 batches, with charge–discharge and HPPC data plus engineered features (SoH, internal/dynamic resistance, capacity fade rate, temperature metrics) (Source: [[data-on-battery-health-and-performance-analysing-samsung-inr21700-50e]]). Only one dataset contains aging. It covers eight cells (Samsung ICR18650-26J NCA, Samsung INR21700-40T NMC, JGNE JGPFR26650 LFP) cycled for more than 600 cycles under randomized discharge currents (0.5C–5C, up to 2C for NCA), with HPPC every 20 cycles (Source: [[dataset-of-lithium-ion-cell-degradation-under-randomized-current-profi]]).

**Ambient and mechanical boundary conditions.** The datasets cover different temperatures:
- 10, 25 and 40 °C in an ESPEC LU-114 chamber for the CALB cells (Source: [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]])
- 5, 25 and 40 °C for the Molicel cells (Source: [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]]). This is the only dataset that reports a control deviation: about 20 % of the 5 °C EIS tests recorded 8–10 °C before the chamber was fixed, after which it held 5–7 °C.
- 25 °C only for the INR21700-50E cells (Source: [[data-on-battery-health-and-performance-analysing-samsung-inr21700-50e]])
- Unquantified room temperature for the randomized-profile aging set (Source: [[dataset-of-lithium-ion-cell-degradation-under-randomized-current-profi]])

Only the randomized-profile dataset mentions a mechanical constraint: each cell was tested inside a clamp, with no magnitude given (Source: [[dataset-of-lithium-ion-cell-degradation-under-randomized-current-profi]]).

**Cell temperature sensing and sampling.** Instrumentation varies:
- T-type thermocouples on each CALB cell surface plus one for the chamber ambient; count per cell and attachment not reported (Source: [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]])
- A single T-type thermocouple at the surface centre, sampled at 1 Hz (Source: [[dataset-of-lithium-ion-cell-degradation-under-randomized-current-profi]])
- A "Temp_Cell" channel described as *internal* cell temperature with no sensor details, sampled at 100 Hz (cycles) and 1 kHz (HPPC) (Source: [[data-on-battery-health-and-performance-analysing-samsung-inr21700-50e]])
- A surface-temperature column with unspecified sensor and sampling (pulse voltage/current at 0.01 s) (Source: [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]])

**Temperature-dependent performance: a contradiction.** The two multi-temperature datasets disagree on how capacity changes with temperature. For the CALB L148N58A, the median C/20 discharge capacity *increases* with temperature from 10 to 40 °C, and the capacity spread is largest at low temperature (Source: [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]]). For the Molicel P42A, average discharge capacity is *highest at 25 °C* (about 3.9 Ah) and *lower at both 5 °C and 40 °C* (about 3.8 Ah) (Source: [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]]). The two datasets agree on resistance. The CALB HPPC ohmic resistance is higher at low temperature, with a slight dip and then a slight rise across SOC (Source: [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]]). The Molicel 5 °C pulse resistances are consistently higher and more spread, and its EIS curves shrink as temperature rises (Source: [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]]). The INR21700-50E data are used to show that engineered features lower MAE/MSE/MAPE of linear regression and random forest models. The authors note that other chemistries and operating conditions (harsh temperatures) still need validation (Source: [[data-on-battery-health-and-performance-analysing-samsung-inr21700-50e]]).

## Literature Mentions

- [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]]: Public dataset of 11 fresh CALB L148N58A prismatic cells (C/20, HPPC, EIS, drive cycles) at 10/25/40 °C; capacity rises with temperature and its spread is larger at low temperature.
- [[data-on-battery-health-and-performance-analysing-samsung-inr21700-50e]]: Zenodo dataset of charge–discharge and 1 kHz HPPC data for 256 Samsung INR21700-50E cells at 25 °C, with engineered features for ML.
- [[dataset-of-lithium-ion-cell-degradation-under-randomized-current-profi]]: Aging dataset of Samsung ICR18650-26J, Samsung INR21700-40T and JGNE JGPFR26650 cells under randomized currents for over 600 cycles, clamped, with one centre surface thermocouple.
- [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]]: Open dataset of 12 Molicel INR-21700-P42A cells (capacity, up-to-8C pulse/GITT, EIS) at 5/25/40 °C; capacity peaks at 25 °C and resistance is highest at 5 °C.

## Related Concepts

- [[cell-to-cell-variation|Cell-to-Cell Variation]]
- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]
- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]

*Last updated: 2026-09-27*
