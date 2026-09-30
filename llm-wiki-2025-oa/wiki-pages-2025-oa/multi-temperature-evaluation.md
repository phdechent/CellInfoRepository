---
type: concept
aliases:
  - "Multi-Temperature Evaluation"
tags:
  - synthesis
---

# Multi-Temperature Evaluation

**Summary:** Multi-temperature evaluation means repeating the same electrical, aging or model-validation protocol on commercial cells at several controlled ambient temperatures, typically from −20 °C to 45 °C in a climate chamber. In the 2025 papers it shows higher resistance, lower capacity and faster aging at low temperature, and it shows where models stop working in the cold.

## Synthesized Knowledge

**Protocols and boundary conditions.** Every study controlled the ambient temperature with an environmental chamber, but the papers report very different levels of detail. For the A123 ANR26650M1-B LiFePO4 cell, an ESPEC BTU-433 chamber was stabilized for one hour before each test at 21, 0, 40 and −10 °C, with 24 h rest between conditions. Surface temperature came from three Type K thermocouples (±1 °C) fixed with thermally conductive tape (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]). The Samsung INR21700-50G was tested at −10, 0, 10, 20, 30 and 45 °C in an ESPEC BTX-475 chamber. One thermocouple sat near the centre of the cell surface and a second one measured the ambient air (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]). The Sony US18650VTC6 study used a low-temperature chamber with ±2 °C accuracy. Cell surface temperature during cycling was not analysed; the authors list it as future work (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]). For the LG 18650HG2 and Panasonic 18650PF drive-cycle tests, the thermal chamber itself recorded battery temperature, and no sensor details are given (Source: [[a-combined-improved-dung-beetle-optimization-and-extreme-learning-mach]]). None of the four papers reports a mechanical constraint. Three papers are internally inconsistent about their own temperature or cycle matrix:
- LG 18650HG2 / Panasonic 18650PF: the tests are stated at −20, 0, 10 and 25 °C, but the training set is described as covering six temperatures from −20 to 40 °C (Source: [[a-combined-improved-dung-beetle-optimization-and-extreme-learning-mach]]).
- Sony US18650VTC6: Table 3 lists −20, −10, 0, 25 and 45 °C, while the capacity analysis names −20, −10, 0, 10 and 25 °C (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]).
- A123 ANR26650M1-B: the setup text gives 10 cycles at 0, 40 and −10 °C, but a figure caption states 100 cycles (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]).

**Temperature-dependent performance.** Low temperature consistently raised resistance and reduced available capacity.
- Sony US18650VTC6: fresh cells at −20 °C had ohmic, polarization and total resistances of 109.0, 44.2 and 153.3 mΩ, which is 5.6, 3.3 and 4.7 times the 25 °C values. OCV at low SOC rose markedly below 0 °C (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]).
- Samsung INR21700-50G: only 4434 mAh could be extracted at 0.2C and −10 °C (about 13% below the specification), with about 20% reduction at 1C. DCIR, R0 and R2 increased as temperature fell. Power capability peaked at 30–45 °C and was severely reduced at −10 °C. Surface temperature rise at 1C was larger at lower ambient temperature (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]).
- A123 ANR26650M1-B: the same number of cycles took longer at 0 and −10 °C. Discharge capacity was initially low at 0 and 40 °C and then increased over the following cycles (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]).

**Temperature-dependent aging.** Two papers report faster degradation in the cold. For the Sony US18650VTC6 under 3C/3C cycling, 83.3% capacity remained after 150 cycles at 25 °C versus 74.2% at −20 °C. Polarization resistance grew 28.9% at −20 °C versus 13.5% at 25 °C. Ohmic resistance growth did not follow temperature monotonically (15.4% at 25 °C, 19.7% at 0 °C, 12.4% at −20 °C), and total resistance growth peaked at −10 °C with 20.8% (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]). For the A123 LFP cell, the authors state that −10 °C accelerates capacity degradation while 21 and 40 °C stay relatively stable (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]). This last result rests on a single cell and an unclear cycle count.

**Model validation across temperature.** Model accuracy depends on temperature in different ways, depending on the model and the output checked.
- A123 ANR26650M1-B, electrochemical-thermal model (thermal parameters calibrated at room temperature): case-temperature RMSE was about 2 °C at 21, 0 and 40 °C but rose to 6.0 °C at −10 °C. Voltage RMSE moved the other way and was lowest at −10 °C (0.18 V versus 0.482 V at 21 °C). The authors attribute the cold-temperature thermal deviation to temperature-independent thermal parameters (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]).
- Samsung INR21700-50G, second-order RC ECM: fitting error grew as temperature fell. At 1C the RMSE was 0.038 V at −10 °C versus 0.009 V at 45 °C (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]).
- LG 18650HG2, IDBO-ELM SOC estimator: UDDS RMSE was 0.0135 at −20 °C, 0.0120 at 0 °C and 0.0128 at 25 °C. The error was therefore not lowest at room temperature (Source: [[a-combined-improved-dung-beetle-optimization-and-extreme-learning-mach]]).

## Literature Mentions

- [[a-combined-improved-dung-beetle-optimization-and-extreme-learning-mach]]: IDBO-ELM SOC estimator for LG 18650HG2 and Panasonic 18650PF, trained on multi-temperature drive-cycle data and tested at −20, 0 and 25 °C with RMSE around 1.2–1.4%; ageing is not considered.
- [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]: A123 ANR26650M1-B electrochemical-thermal model validated at 21, 0, 40 and −10 °C; case-temperature RMSE rises to 6.0 °C at −10 °C because thermal parameters are temperature-independent.
- [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]: Sony US18650VTC6 cycled at −20 to 45 °C; at −20 °C, resistance is 4.7× higher (total) and capacity retention after 150 cycles is lower (74.2% vs 83.3% at 25 °C).
- [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]: Samsung INR21700-50G capacity/HPPC/ECM characterization at six temperatures from −10 to 45 °C; capacity, power and ECM fit quality all fall at low temperature.

## Related Concepts

- [[state-of-charge-estimation|State-of-Charge Estimation]]
- [[capacity-degradation|Capacity Degradation]]
- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]
- [[electrochemical-thermal-model|Electrochemical-Thermal Model]]

*Last updated: 2026-09-27*
