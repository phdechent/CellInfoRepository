---
type: concept
aliases:
  - "Immersion Cooling"
tags:
  - synthesis
---

# Immersion Cooling

**Summary:** Three 2025 open-access studies experimentally tested direct liquid immersion of commercial cells in dielectric fluids: full-module single-phase oil immersion of Samsung SDI INR21700-48X cells, nanofluid tab versus surface immersion of a Melasta SLPBB042126 pouch cell (with a validated 3D CFD model), and single- versus two-phase Novec 7000 immersion of an A123 ANR26650M1-B cell. Tabs/terminals emerge as a key heat path, and fluid temperature doubles as the ambient boundary condition.

## Synthesized Knowledge

**Configurations and protocols.** A 5S7P module of 35 INR21700-48X cells in an aluminum box (2 mm spacing, bottom-to-top flow, 3 inlets/3 outlets) was cooled by forced single-phase dielectric oil; Therminol D-12 was selected over Pitherm 150B and BOT 2100 at 1.0C discharge, and 0.8 LPM was selected from 0.4–1.0 LPM by trading heat transfer coefficient against pressure drop (Source: [[experimental-study-on-thermal-management-of-5s7p-battery-module-with-i]]). For the Melasta SLPBB042126 (6600 mAh LCO pouch), only the tabs or only the surface were submerged in circulating silicone-oil nanofluid (SiO2, Al2O3, CuO; 15–75 ml/min), tested experimentally at 2C CC-CV with 1% SiO2 at 15 ml/min (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]). The A123 ANR26650M1-B (2.5 Ah LFP) was fully immersed in Novec 7000 and charged at 1C–4C CC-CV and discharged at 4C–10C, comparing single-phase natural convection with preheated subcooled boiling at 1 bar ± 0.02 bar, with 500 Hz high-speed imaging of boiling (Source: [[thermal-performance-of-lithium-ion-battery-tabs-under-liquid-immersion]]).

**Boundary conditions and temperature sensing.** Ambient/fluid control differs strongly: 25 °C in a temperature/humidity chamber with coolant inlet held by a 5 kW chiller (Source: [[experimental-study-on-thermal-management-of-5s7p-battery-module-with-i]]); 25 °C chamber with 1 h stabilization (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]); bulk fluid preheated to 33 °C ± 0.5 °C for two-phase tests versus single-phase tests starting from uncontrolled ambient (initial 18.4–21.9 °C) (Source: [[thermal-performance-of-lithium-ion-battery-tabs-under-liquid-immersion]]). All three use T-type thermocouples: nine at mid-height on nine module cells (Source: [[experimental-study-on-thermal-management-of-5s7p-battery-module-with-i]]); seven on the pouch cell including positive and negative tab regions (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]); seven 0.2 mm exposed-junction sensors, one per terminal plus five along the axis at 11 mm spacing, bonded with Loctite 315 (Source: [[thermal-performance-of-lithium-ion-battery-tabs-under-liquid-immersion]]). None reports a mechanical boundary condition or sampling rate.

**Performance findings and differing criteria.** Therminol D-12 at 0.8 LPM held Tmax/ΔT at 38.6 °C/4.3 °C for 3.0C charging and 43.0 °C/5.5 °C for 3.0C discharging, against targets of 25–40 °C and ΔT below 5 °C (Source: [[experimental-study-on-thermal-management-of-5s7p-battery-module-with-i]]). Tab cooling reduced the cell temperature difference by 82.8% versus surface cooling at 4C (simulated) (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]). Subcooled boiling on the terminals gave terminal-to-fluid ΔT two to three times lower than single-phase natural convection, evaluated against a 40 °C limit and a 2 °C non-uniformity threshold (Source: [[thermal-performance-of-lithium-ion-battery-tabs-under-liquid-immersion]]). The acceptable cell-to-cell/in-cell ΔT criterion therefore differs between studies (below 5 °C vs. 2 °C), and the module results at 3.0C (4.3–5.5 °C) would not satisfy the stricter criterion; the papers do not reconcile these. The higher fluid temperature also improved electrical performance of the ANR26650M1-B: at 33 °C, 4C charging time fell from 1777 s to 1233 s (31%) and 10C discharge delivered about 5% more average power (Source: [[thermal-performance-of-lithium-ion-battery-tabs-under-liquid-immersion]]). Tab cooling is not unambiguously beneficial: excessive tab-only cooling can make the lower cell surface warmer than the upper section, increasing the temperature differential (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]).

**Modelling.** Only the pouch-cell study models immersion cooling: a 3D transient ANSYS Fluent model with Bernardi heat generation, anisotropic conduction, tab Joule heating and a two-phase mixture laminar nanofluid model, parameterized from the authors' own HPPC resistance and entropic-coefficient tests and validated against their 2C experiments and literature data (max RMSE 1.33 °C, max error 3.50%); limitations are uniform internal heat generation, neglected radiation, and validation only at 2C/25 °C with 1% SiO2 at 15 ml/min, while 4C, other nanofluids and a seven-cell pack are extrapolated (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]). No immersion study addresses aging.

## Literature Mentions

- [[experimental-study-on-thermal-management-of-5s7p-battery-module-with-i]]: Single-phase Therminol D-12 immersion of a 5S7P Samsung SDI INR21700-48X module keeps Tmax 38.6 °C/ΔT 4.3 °C at 3.0C charging.
- [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]: Nanofluid tab immersion of Melasta SLPBB042126 pouch cell, CFD-validated (RMSE ≤1.33 °C); 82.8% lower ΔT than surface cooling at 4C.
- [[thermal-performance-of-lithium-ion-battery-tabs-under-liquid-immersion]]: Novec 7000 two-phase immersion of A123 ANR26650M1-B cuts terminal ΔT 2–3× and 4C charge time by 31% at 33 °C fluid.

## Related Concepts

- [[battery-thermal-management|Battery Thermal Management]]
- [[fast-charging|Fast Charging]]
- [[computational-fluid-dynamics|Computational Fluid Dynamics]]
- [[liquid-cooling|Liquid Cooling]]

*Last updated: 2026-09-27*
