---
type: concept
aliases:
  - "Heat Generation"
tags:
  - synthesis
---

# Heat Generation

**Summary:** Heat generation in commercial cells is studied through measured surface temperature rise, heat flux and thermography, and through model heat-source terms. The four 2025 papers use different heat-source formulations and thermal boundary conditions. They also report hotspots in different places, depending on cell format and whether the model is spatially resolved.

## Synthesized Knowledge

**Heat-source formulations differ.** The papers compute heat generation in different ways, and their predicted temperatures come from these different inputs:
- The Sony-Murata US18650VTC6 study names Joule and entropic heat as the sources of chemistry-specific surface-temperature profiles. The entropic contribution is what distinguishes the chemistries (Source: [[accurate-chemistry-identification-of-lithium-ion-batteries-based-on-te]]).
- The 3D NTGK (MSMD) model of the Kokam SLPB120216216G1H pouch cell in Ansys Fluent uses a volumetric heat source with ohmic, reaction and entropic terms (Source: [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]).
- The cascaded model of the A123 ANR26650M1-B computes heat as S(t) = V(t)|I(t)| from the Single Particle Model terminal voltage (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]).

**Thermal boundary conditions and sensing differ.** The VTC6 cells were insulated with 1.5 cm styrofoam in a 25 °C Memmert ICP110 chamber. One PT100 sat mid-way on the curved surface. The authors state that ambient temperature effects were ignored because of the insulation (Source: [[accurate-chemistry-identification-of-lithium-ion-batteries-based-on-te]]). The Samsung ICR18650-26J (and an EVE 40PL 21700) were tested at 25 ± 2 °C laboratory ambient with no chamber specified. Two LM35 sensors (geometric centre and near the cathode terminal) were combined with a FLIR E5 infrared camera. Cells rested until the surface was within ±0.5 °C of ambient (Source: [[analysis-of-the-relationship-between-discharge-cutoff-voltage-and-ther]]). The Kokam pouch cell had no active cooling and no reported ambient temperature; its face was at 22.3 °C at the start of the 2 C discharge. It carried eight heat flux sensors with thermocouples (tabs, top, middle, bottom) plus FLIR T335 thermography (Source: [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]). The ANR26650M1-B was cycled in an ESPEC BTU-433 chamber at 21, 0, 40 and −10 °C, stabilized for 1 h. Three Type K thermocouples were fixed with thermally conductive tape, and there were no internal sensors (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]).

**Measured heating magnitudes and C-rate effects.** Each study reports the magnitude of heating in its own terms:
- **ICR18650-26J:** the maximum surface temperature rise exceeded 30 °C at 2C discharge to 2.5 V, more than double that of the 21700 cell. The authors propose load-adaptive cutoff voltages: about 2.9–3.0 V at ≤1C and 3.1–3.2 V at 1.5–2C (Source: [[analysis-of-the-relationship-between-discharge-cutoff-voltage-and-ther]]).
- **Kokam 57 Ah pouch cell:** the face exceeded 35 °C from about 1.35 C without cooling, and the top-to-bottom face gradient reached about 4 °C (Source: [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]).
- **VTC6 (insulated):** the first 1C charge raised the surface to 39 °C. In later cycles the internal resistance is lower at the elevated cell temperature, so entropic cooling shows up as a mid-way temperature drop (Source: [[accurate-chemistry-identification-of-lithium-ion-batteries-based-on-te]]).
- **ANR26650M1-B:** at 40 °C ambient the measured peak surface temperature was 48.7 °C, against 47.5 °C from the model (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]).

**Where the heat concentrates, and model limitations.** The papers disagree on the dominant inhomogeneity. The pouch-cell study finds the tab/body junction hottest and locates heat near the tabs at higher C-rates. Its 3D model matched measured maximum temperatures with about 4.54 % average deviation (1.41–6.22 % per C-rate). The 4 C and 5 C cases were simulated only (Source: [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]). The cylindrical ANR26650M1-B model resolves 38 radial layers with adiabatic ends and no tab effects. It predicts internal temperatures up to 15 °C above the surface at 21 °C, but these internal predictions could not be checked because there were no internal sensors. Case-temperature RMSE was about 2 °C at 21, 0 and 40 °C and rose to 6.0 °C at −10 °C, which the authors attribute to temperature-independent thermal parameters calibrated at room temperature (Source: [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]). These are different cell formats and modelling choices (axial/tab vs. radial resolution), not directly comparable results. The VTC6 study adds that below about 75 % SOH, irreversible heat may become so large that the temperature response is less distinctive for chemistry classification (Source: [[accurate-chemistry-identification-of-lithium-ion-batteries-based-on-te]]).

## Literature Mentions

- [[accurate-chemistry-identification-of-lithium-ion-batteries-based-on-te]]: Joule and entropic heat produce chemistry-specific surface-temperature profiles of insulated Sony-Murata US18650VTC6 cells at 25 °C, classified by a GRU network.
- [[analysis-of-the-relationship-between-discharge-cutoff-voltage-and-ther]]: Surface temperature rise of the Samsung ICR18650-26J exceeded 30 °C at 2C to 2.5 V, motivating load-adaptive cutoff voltages.
- [[experimental-study-of-pouch-type-battery-cell-thermal-characteristics]]: The uncooled Kokam SLPB120216216G1H pouch cell is hottest at the tabs, with a face gradient of about 4 °C; a 3D NTGK model matches maximum temperatures within about 4.5 %.
- [[investigating-thermal-dynamics-in-cylindrical-li-ion-batteries-across]]: An SPM-driven 306-state layer-resolved thermal model of the A123 ANR26650M1-B is validated at 21/0/40 °C but deviates at −10 °C (RMSE 6.0 °C).

## Related Concepts

- [[battery-thermal-management|Battery Thermal Management]]
- [[electrochemical-thermal-model|Electrochemical-Thermal Model]]
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]
- [[internal-resistance|Internal Resistance]]

*Last updated: 2026-09-27*
