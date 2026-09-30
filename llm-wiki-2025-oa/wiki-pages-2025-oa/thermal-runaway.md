---
type: concept
aliases:
  - "Thermal Runaway"
tags:
  - synthesis
---

# Thermal Runaway

**Summary:** In the 2025 open-access corpus, thermal runaway (TR) of commercial 18650/21700 cells is addressed through heating-triggered abuse tests (accelerating rate calorimetry, heater-induced overtemperature, heated pressure vessel) and through early-warning diagnostics based on impedance or high-frequency partial-discharge signals. Temperature boundary conditions are mostly defined by the abuse protocol (heating rate, Heat-Wait-Seek steps) rather than by a controlled ambient, and no study builds a TR model.

## Synthesized Knowledge

**Triggering protocols and measured TR characteristics.** For Samsung SDI INR18650-30Q (NMC622/graphite) cells at 100% SOC, TR was triggered by heating at 5 °C/min inside a self-developed threaded canister placed in an 8 L nitrogen-filled (>99% N2) vessel at atmospheric pressure; replacing the original safety vent with 4, 8 or 12 layers of aluminium foil set bursting pressures of 1, 2 and 3 MPa, and higher bursting pressure delayed venting, increased vented gas volume from 5.3 to 6.5 L and raised H2 content from 23.92% to 28.81%, while also changing solid-residue composition (XRD, SEM-EDS) (Source: [[effects-of-different-safety-vent-bursting-pressures-on-lithium-ion-bat]]). For Samsung SDI INR21700-50E cells, ARC Heat-Wait-Seek tests (start 25 °C, 5 °C steps, 30 min wait, 0.02 °C/min sensitivity) at 10%, 50% and 100% SoC were combined with EIS, and fast overtemperature tests used an 80 W heater dummy cell fixed with metallic cable ties at cell and 8s1p module level (Source: [[impedance-based-thermal-runaway-early-detection-methodology-for-lithiu]]). For Sony-Murata US18650VTC6 cells aged at −20 °C, ARC Heat-Wait-Search tests on fully charged cells after 0, 15, 25, 75 and 150 cycles yielded characteristic temperatures T1–T3 and maximum self-heating rates, and aged cells still released large energy during TR (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]).

**Early detection.** A single-frequency impedance method at 400.15 Hz (chosen by maximising temperature variance over SoC variance) on the INR21700-50E gave warnings about 15 h before TR in slow (ARC) tests and 6–12 min before TR in fast overtemperature tests, benchmarked against an automotive VOC gas sensor; impedance first decreased with rising temperature and then increased from about 90 °C, the phase shift changed strongly between 25 °C and 48 °C and fell below −0.5° above about 50 °C, with magnitude more SoC-dependent and phase more temperature-dependent (Source: [[impedance-based-thermal-runaway-early-detection-methodology-for-lithiu]]). A time-resolved partial discharge (TRPD) and FFT method on INR18650-30Q cells detected micro internal short circuits, as precursors of TR, via defect-signal peaks at 3.9, 11.9 and 19 MHz using HFCT (250 mV threshold) and antenna (2 V threshold) sensors, during accelerated cycling at 25 °C and 60 °C and during probe-induced deformation in 1 mm steps (force not reported) (Source: [[a-study-on-the-lithium-ion-battery-fire-prevention-diagnostic-techniqu]]).

**Boundary conditions, temperature sensing and temperature-dependent aging.** Cell temperature sensing is sparse: three thermocouples on positive tab, negative tab and cell centre in the INR21700-50E overtemperature tests (attachment and sampling not reported) (Source: [[impedance-based-thermal-runaway-early-detection-methodology-for-lithiu]]); no explicit cell sensor but vessel temperature and a 2 kHz piezoelectric pressure signal in the vent study (Source: [[effects-of-different-safety-vent-bursting-pressures-on-lithium-ion-bat]]); cell temperature tracked only in ARC, not during cycling, in the VTC6 study (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]); and none reported in the TRPD study (Source: [[a-study-on-the-lithium-ion-battery-fire-prevention-diagnostic-techniqu]]). Regarding aging preceding TR tests, INR18650-30Q capacity declined fastest at 60 °C and 2C, attributed to side reactions and SEI decomposition (Source: [[a-study-on-the-lithium-ion-battery-fire-prevention-diagnostic-techniqu]]), while for the VTC6 lower temperature accelerated degradation: after 150 3C/3C cycles 83.3% capacity was retained at 25 °C versus 74.2% at −20 °C, and at −20 °C fresh-cell ohmic, polarization and total resistances were 109.0, 44.2 and 153.3 mΩ (5.6, 3.3 and 4.7 times the 25 °C values) (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]). The VTC6 chamber accuracy was ±2 °C (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]), whereas the TRPD study only states that temperature and humidity were "carefully controlled" (Source: [[a-study-on-the-lithium-ion-battery-fire-prevention-diagnostic-techniqu]]).

**Contradictions and inconsistencies.** The two aging-related studies point to opposite temperature extremes as degradation accelerators relative to 25 °C — high temperature (60 °C) for the INR18650-30Q (Source: [[a-study-on-the-lithium-ion-battery-fire-prevention-diagnostic-techniqu]]) and low temperature (−20 °C) for the VTC6 (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]); these were obtained on different cells and protocols and are not directly comparable. Within the VTC6 study, resistance growth is not monotonic in temperature (ohmic growth 15.4% at 25 °C, 19.7% at 0 °C, 12.4% at −20 °C; total growth peaking at −10 °C with 20.8%), and the temperature series is listed as −20/−10/0/25/45 °C in one place but −20/−10/0/10/25 °C in the capacity analysis (Source: [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]). Warning lead times depend strongly on the heating scenario (about 15 h slow vs. 6–12 min fast) (Source: [[impedance-based-thermal-runaway-early-detection-methodology-for-lithiu]]).

## Literature Mentions

- [[a-study-on-the-lithium-ion-battery-fire-prevention-diagnostic-techniqu]]: Samsung SDI INR18650-30Q; TRPD–FFT detects micro internal shorts (peaks at 3.9, 11.9, 19 MHz) as TR precursors, with fastest capacity fade at 60 °C and 2C.
- [[effects-of-different-safety-vent-bursting-pressures-on-lithium-ion-bat]]: Samsung SDI INR18650-30Q at 100% SOC heated at 5 °C/min in N2; higher vent bursting pressure (1–3 MPa) delayed venting and raised gas volume (5.3–6.5 L) and H2 share.
- [[impedance-based-thermal-runaway-early-detection-methodology-for-lithiu]]: Samsung SDI INR21700-50E; 400.15 Hz impedance phase/magnitude criteria warned about 15 h (ARC) and 6–12 min (overtemperature) before TR at cell and 8s1p module level.
- [[research-on-aging-evolution-and-safety-characteristics-of-lithium-ion]]: Sony-Murata US18650VTC6 cycled at −20 °C; ARC after up to 150 cycles shows aged cells still release large TR energy, with faster fade at −20 °C than 25 °C.

## Related Concepts

- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]
- [[capacity-degradation|Capacity Degradation]]
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]
- [[internal-resistance|Internal Resistance]]

*Last updated: 2026-09-27*
