---
type: concept
aliases:
  - "Fast Charging"
tags:
  - synthesis
---

# Fast Charging

**Summary:** Fast charging in the 2025 open-access corpus covers four scales: cell-level charging-strategy design based on degradation modelling (Samsung INR21700-50E), module-level immersion cooling at up to 3C (Samsung INR21700-48X), tab immersion cooling of a pouch cell at 2C–4C (Melasta SLPBB042126), and vehicle-level 800 V DC charging (LG Chem E66A in the Porsche Taycan). The papers set different temperature limits and targets.

## Synthesized Knowledge

**Cell-level strategy and degradation.** For Samsung INR21700-50E NCA cells, an advanced single-particle model was built with a polynomial electrolyte approximation, SEI growth, lithium plating and a lumped heat balance (1D through-thickness electrolyte with radial particle approximation). It was validated against the authors' own CC charging at 0.6–3C (voltage accuracy 96.63 %, maximum error 5.47 % at 3C), the charging temperature (about 96.7 %) and SOH over repeated cycles (error around 9 %). The model's plating map over C-rate, SOC and temperature was used to design a Thermal-Boost Fast Charging (TBFC) profile that starts at 3C and steps down with SOC to charge from SOC 0.05 to 0.75 within 20 min. Experimentally, TBFC extended cycle life by 170 % compared with 2.1C CCCV, and plating caused about 72 % of the capacity loss at 2.1C (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]). In the model, raising temperature from 25 °C to 55 °C cut the lithium plating rate by a factor of nine and lowered the charging voltage from 4.18 V to 4.04 V at 1.8C. No experimental comparison of aging across temperatures was reported, and the experimental ambient temperature was not stated; current was cut off when the thermocouple-measured cell temperature exceeded 55 °C (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]). Reported limitations are a larger error at 3C and a growing SOH error because SEI decomposition and plating dissolution are not modelled (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]).

**Thermal management during fast charging.** A 5S7P module of 35 Samsung INR21700-48X cells, immersed in Therminol D-12 oil at 0.8 LPM (25 °C ambient chamber, chiller-controlled coolant), reached Tmax/ΔT of 38.6 °C/4.3 °C at 3.0C charging and 43.0 °C/5.5 °C at 3.0C discharging. This was measured by nine T-type thermocouples at mid-height on cells from inlet to outlet, against a target window of 25–40 °C and ΔT below 5 °C. The cells were held in an aluminium box with 2 mm spacing and no reported mechanical pressure (Source: [[experimental-study-on-thermal-management-of-5s7p-battery-module-with-i]]). For the Melasta SLPBB042126 LCO pouch cell, a 3D transient ANSYS Fluent model was used, with Bernardi heat generation, anisotropic conduction, tab Joule heating and a two-phase laminar nanofluid model, parameterised from the authors' own HPPC resistance and entropic-coefficient measurements. It was validated at 2C charging and 25 °C ambient (natural convection and 1 % SiO2 tab cooling at 15 ml/min; seven surface thermocouples) with a maximum RMSE of 1.33 °C. At 4C (simulation only), tab cooling reduced the cell temperature difference by 82.8 % versus surface cooling. 2C is the manufacturer's maximum charge rate for this cell. Limitations include uniform internal heat generation, and tab-only cooling can over-cool so that the lower cell surface ends up warmer than the upper section (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]).

**Vehicle-level charging and differing thermal limits.** The Porsche Taycan pack, which uses LG Chem E66A cells per literature, reached a 262.2 kW peak during 800 V DC charging from 5 % to 100 % SOC, starting at a battery system temperature of 35 °C, and the charge took 57.22 min. Power was reduced after about 9 min to keep the onboard battery system temperature at or below 54 °C. The ohmic-loss split relies on one lumped cell resistance, measured at 1.243 mΩ (50 % SOC, 20 °C, 1C, 10 s pulse) (Source: [[quantifying-the-state-of-the-art-of-electric-powertrains-in-battery-el]]). **The papers' temperature targets conflict.** The INR21700-50E study deliberately raises cell temperature ("Thermal-Boost") because its model predicts less plating at higher temperature, with a 55 °C cut-off (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]). The INR21700-48X immersion-cooling study aims to keep module Tmax within 25–40 °C (Source: [[experimental-study-on-thermal-management-of-5s7p-battery-module-with-i]]). The Taycan charging control holds the battery system at 54 °C (Source: [[quantifying-the-state-of-the-art-of-electric-powertrains-in-battery-el]]). These limits refer to different quantities (a cell thermocouple, module surface Tmax, and the vehicle's system temperature signal) and to different cells, so they cannot be compared directly. The charging windows also differ: 5–75 % SOC in 20 min for INR21700-50E versus 5–100 % SOC in 57.22 min at vehicle level.

## Literature Mentions

- [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]: A plating-map-based Thermal-Boost Fast Charging profile (20 min, SOC 0.05–0.75) extended cycle life of Samsung INR21700-50E cells by 170 % vs 2.1C CCCV.
- [[experimental-study-on-thermal-management-of-5s7p-battery-module-with-i]]: Oil immersion cooling kept a 5S7P module of Samsung INR21700-48X cells at 38.6 °C Tmax / 4.3 °C ΔT during 3.0C charging.
- [[quantifying-the-state-of-the-art-of-electric-powertrains-in-battery-el]]: 800 V DC charging of the Porsche Taycan (LG Chem E66A cells) peaked at 262.2 kW and took 57.22 min (5–100 % SOC), derated to hold 54 °C.
- [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]: Validated 3D CFD shows nanofluid tab cooling of the Melasta SLPBB042126 pouch cell cuts the in-cell ΔT by 82.8 % vs surface cooling at 4C.

## Related Concepts

- [[lithium-plating|Lithium Plating]]
- [[immersion-cooling|Immersion Cooling]]
- [[electrochemical-thermal-model|Electrochemical-Thermal Model]]
- [[battery-thermal-management|Battery Thermal Management]]

*Last updated: 2026-09-27*
