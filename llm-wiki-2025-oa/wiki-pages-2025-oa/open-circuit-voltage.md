---
type: concept
aliases:
  - "Open-Circuit Voltage"
tags:
  - synthesis
---

# Open-Circuit Voltage

**Summary:** Two 2025 papers measure open-circuit voltage (OCV) on commercial cylindrical cells with rest-interrupted (pseudo-OCV) procedures and use separate charge and discharge OCV curves as model inputs. Rest durations, SOC resolution and how the OCV is represented in the model differ between them.

## Synthesized Knowledge

**The measurement procedures differ.** On a five-cell series string of Sony-Murata US18650VTC6 cells, OCV was measured in intermittent tests. After a 20 min rest following full discharge, 10 min of current at 1, 3 or 5 A alternated with 5 min rests, and OCV was read during each rest. The note reports only room temperature for this characterization; the IEC 62660-1 validation ran at 25 °C (Source: [[experimental-testing-and-modeling-of-li-ion-battery-performance-based]]). On LG Chem INR21700 M50T cells, separate charge and discharge pseudo-OCV curves were measured on three cells at eleven SOC points, each with a 30 min rest (Source: [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]). The rest periods (5 min vs 30 min) and SOC resolution differ. The notes do not say whether either reaches equilibrium.

**Both treat charge and discharge separately, but represent OCV differently.** For the VTC6, the OCV–capacity relation was fitted with a 4th-order polynomial for discharge and a linear equation for charge. It enters an empirical V = OCV ± IR model whose IR term is exponential in capacity for discharge and linear in current (0.22985 + 0.19837·I) for charge (Source: [[experimental-testing-and-modeling-of-li-ion-battery-performance-based]]). For the M50T, the charge and discharge OCV curves were transferred directly into the model as characteristic maps. The model is an equivalent circuit (Rs, two RC elements, an RC sub-element and a Warburg element, parameterized from EIS at 20 °C) coupled to a 2D thermal network. It drives a heatable replacement cell for hardware-in-the-loop thermal-management tests (Source: [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]).

**Validation, temperature and limitations.** The VTC6 model was validated against continuous CC curves at 1, 3 and 5 A and the IEC 62660-1 dynamic profile at 25 °C. Errors were below 2.5 %, rising to 3.5 % during rests because relaxation is not captured. Deviations at the end of discharge are attributed to temperature differences between the pause and non-pause experiments. The authors list the fixed ambient temperature, a single cell type, currents no higher than 5 A and no aging as limitations. The note reports no cell temperature sensing (Source: [[experimental-testing-and-modeling-of-li-ion-battery-performance-based]]). The M50T model was validated at 40, 25, 0 and −20 °C ambient on fresh cells. It reproduced the voltage dip and relaxation at the start of a −20 °C, 5 A discharge. Mean discharge voltage deviation was about 1.5 % (<50 mV) and pulse deviations were below 0.1 V. At higher currents, the 55 °C surface-temperature limit was reached before the 2.5 V cutoff. The authors state that thermal conduction through the layers is underestimated and that thermal parameters have not yet been evaluated (Source: [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]). Neither note gives OCV at more than one temperature, so the temperature dependence of OCV itself is not covered for these cells.

## Literature Mentions

- [[experimental-testing-and-modeling-of-li-ion-battery-performance-based]]: OCV from 5-min rest pauses on a Sony-Murata US18650VTC6 string, fitted per direction (4th-order polynomial for discharge, linear for charge), feeds an OCV ± IR model validated with IEC 62660-1 at 25 °C (errors below 2.5 %).
- [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]: Charge/discharge pseudo-OCV maps (11 SOC points, 30-min rests) of the LG INR21700 M50T parameterize an EIS-based ECM-thermal model validated from −20 to 40 °C.

## Related Concepts

- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]
- [[internal-resistance|Internal Resistance]]
- [[electrochemical-thermal-model|Electrochemical-Thermal Model]]
- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]

*Last updated: 2026-09-27*
