---
type: concept
aliases:
  - "Electrochemical-Thermal Model"
tags:
  - synthesis
---

# Electrochemical-Thermal Model

**Summary:** Electrochemical-thermal models couple an electrochemical or electrochemically derived voltage/heat model to a thermal model. In the 2025 papers the electrochemical part ranges from single-particle models through semi-empirical NTGK to EIS-parameterized equivalent circuits, and the thermal part ranges from lumped balances to 3D fields; all are validated against surface-temperature measurements on commercial cells.

## Synthesized Knowledge

**Model types and spatial resolution.** Four studies cover a wide range of model types:
- **Samsung INR21700-50E:** an advanced single-particle model with a polynomial through-thickness electrolyte approximation, SEI-growth and lithium-plating side reactions, and a lumped heat balance. It predicts charging voltage, temperature and SOH (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]).
- **A123 ANR26650M1-B:** a Single Particle Model feeds heat generation, computed as S(t) = V(t)|I(t)|, into a radially layer-resolved lumped thermal network. The network resolves 38 spiral-wound layers (counted by disassembly) with 306 thermal states and assumes adiabatic ends, so axial and tab effects are absent. It predicts internal temperatures up to 15 °C above the surface at 21 °C (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]).
- **Kokam SLPB120216216G1H 57 Ah pouch cell:** a 3D MSMD NTGK model in Ansys Fluent. Its volumetric heat source includes ohmic, reaction and entropic terms, and it places the highest temperature at the junction between tabs and cell body (Source: [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]).
- **LG INR21700 M50T:** the literature-based electrochemical sub-model was replaced by an ECM (Rs, RC elements, Warburg element, separate charge and discharge OCV maps). The ECM is coupled to a symmetry-based 2D disc thermal network that drives a heatable replacement cell in hardware-in-the-loop thermal-management tests (Source: [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]).

**Parameterization and validation.** Parameter sources and validation metrics differ by study:

| Cell | Parameter source | Validation result |
|---|---|---|
| A123 ANR26650M1-B | Literature thermal and electrochemical values; thermal resistances calibrated at room temperature | Case-temperature RMSE 1.99 °C for the multi-layer model vs 2.39 °C for a single-layer model at 21 °C (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]) |
| Samsung INR21700-50E | Parameter tables; source not explicitly stated | 96.63% voltage accuracy for 0.6–3C CC charging (5.47% maximum error at 3C), about 96.7% temperature accuracy, about 9% SOH error (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]) |
| Kokam SLPB120216216G1H | NTGK functions fitted to voltage/current curves | Maximum temperature within about 4.54% on average at 0.5–2C discharge; 4C and 5C simulated only (Source: [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]) |
| LG INR21700 M50T | Own EIS (averaged over four cells, 0.1 Hz–10 kHz at five SOC points) and OCV measurements; linear temperature coefficient referenced to 20 °C | Mean discharge-voltage deviation about 1.5% (<50 mV), pulse deviations <0.1 V (Source: [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]) |

**Boundary conditions of the validation experiments.** The experimental boundary conditions are often weakly documented:
- Samsung INR21700-50E: the ambient temperature is not reported, and current was cut when the cell exceeded 55 °C (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]).
- Kokam SLPB120216216G1H: the ambient temperature is not reported and tests ran without active cooling. The instrumentation used eight heat-flux sensors with thermocouples at tab, top, middle and bottom positions plus a FLIR thermal imager. The measured top-to-bottom face gradient reached about 4 °C (Source: [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]).
- A123 ANR26650M1-B: the only multi-temperature validation (21, 0, 40, −10 °C, chamber-controlled). Only three surface thermocouples were used, so the predicted internal temperatures could not be checked (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]).
- LG INR21700 M50T: validation at 40, 25, 0 and −20 °C ambient; the chamber control method and the sensor details are not reported (Source: [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]).
None of the studies reports mechanical constraint beyond a holding mandrel during EIS for the M50T (Source: [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]).

**Limitations.** A recurring weakness is the thermal parameter set:
- A123 ANR26650M1-B: temperature-independent thermal parameters caused a cooling delay at 0 and 40 °C and a 6.0 °C case-temperature RMSE at −10 °C. The model also assumes constant solid diffusion coefficients and neglects electrolyte dynamics (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]).
- LG INR21700 M50T: thermal parameters are not yet evaluated, and heat conduction through the layers is underestimated, so temperatures are overestimated at points (Source: [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]).
- Samsung INR21700-50E: SOH error grows over cycling because SEI decomposition and plating dissolution are not modelled (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]).
- Kokam SLPB120216216G1H: no explicit limitations are stated, although its 4C and 5C predictions (48.51 °C and 54.02 °C maximum) have no experimental counterpart (Source: [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]).

**Voltage and temperature accuracy can diverge.** For the A123 cell, voltage RMSE was lowest at −10 °C (0.18 V) while temperature RMSE was highest there (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]). The papers do not compare heat-generation formulations directly. The A123 study uses S = V|I|, whereas the Kokam NTGK model uses ohmic, reaction and entropic terms (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]; [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]).

## Literature Mentions

- [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]: Advanced SPM with SEI/plating and a lumped heat balance for the Samsung INR21700-50E, validated on 0.6–3C charging (96.63%) and used to design a 20-min fast-charging profile.
- [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]: 3D NTGK model of the Kokam SLPB120216216G1H 57 Ah pouch cell in Ansys Fluent; maximum temperature within about 4.5% at 0.5–2C; the tab region is hottest.
- [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]: SPM plus a 306-state multi-layer thermal network for the A123 ANR26650M1-B, validated at four ambient temperatures; fails at −10 °C (case-temperature RMSE 6.0 °C).
- [[utilization-of-battery-analysis-methodologies-for-parametrization-and]]: EIS/OCV-parameterized ECM coupled to a 2D thermal network for the LG INR21700 M50T, used for HiL replacement-cell operation; thermal parameters not yet evaluated.

## Related Concepts

- [[heat-generation|Heat Generation]]
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]
- [[lithium-plating|Lithium Plating]]
- [[battery-thermal-management|Battery Thermal Management]]

*Last updated: 2026-09-27*
