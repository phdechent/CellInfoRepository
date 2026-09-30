---
type: concept
aliases:
  - "Hybrid Pulse Power Characterization"
tags:
  - synthesis
---

# Hybrid Pulse Power Characterization

**Summary:** Hybrid Pulse Power Characterization (HPPC) applies current pulses separated by rests at a series of SOC levels. In the 2025 open-access papers it is used to obtain resistance, power capability and OCV data, to parameterize and validate equivalent circuit models, and to track power loss during aging. The pulse durations, SOC steps, C-rates and thermal boundary conditions differ considerably from paper to paper.

## Synthesized Knowledge

**Protocols differ between papers.** On the Samsung INR21700-50E, HPPC is built into the discharge: a micro-HPPC at every 10 % SOC step from 100 % to 10 %, a final HPPC at 0 % SOC, and recording at 1 kHz. It is the main source of the dataset's internal- and dynamic-resistance features (Source: [[data-on-battery-health-and-performance-analysing-samsung-inr21700-50e]]). On the Samsung INR21700-50G, the pulses are 2 s, 10 s, 30 s and 180 s long, applied at every 5 % SOC with 1–2 h rests, at 0.2C and 1C. Only one iteration was run per condition (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]). On the Samsung INR18650-20R, the sequence is 1C discharge steps of 10 % DOD, a 40 min rest, a 5C or 2C 10 s discharge pulse, a 30 s rest and a 10 s charge pulse (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]). The aging dataset on JGNE JGPFR26650 (LFP), Samsung ICR18650-26J (NCA) and Samsung INR21700-40T (NMC) runs HPPC at 0.5C, 1C and 2C with 6 min pulses after every 20 randomized-current cycles, sampled at 1 Hz (Source: [[dataset-of-lithium-ion-cell-degradation-under-randomized-current-profi]]). Pulse length therefore ranges from 10 s to 6 min, and sampling from 1 Hz to 1 kHz. These are different protocol choices rather than one standardized procedure. A low-cost electronic DC load also offers a dedicated HPPC mode, demonstrated down to 2.5 V on an A123 AMP20M1HD-A LFP cell. The note gives no pulse parameters or temperature for it (Source: [[low-cost-electronic-dc-load-module-design-for-battery-capacity-evaluat]]).

**Boundary conditions.** The papers control and report ambient conditions very differently:
- The INR21700-50E tests ran in a climate chamber at 25 °C, with cells equilibrated first. A cell temperature signal was recorded, but its sensor and placement are not reported (Source: [[data-on-battery-health-and-performance-analysing-samsung-inr21700-50e]]).
- The INR21700-50G was characterized at −10, 0, 10, 20, 30 and 45 °C in an ESPEC BTX-475 chamber. One thermocouple sat near the centre of the cell surface and a second measured ambient air (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]).
- The randomized-current aging dataset was recorded at unspecified room temperature. Each cell sat in a clamp (magnitude not reported) with one T-type thermocouple at the centre of the surface (Source: [[dataset-of-lithium-ion-cell-degradation-under-randomized-current-profi]]).
- The INR18650-20R HPPC data were taken at 25 °C ambient; the note reports no control method and no cell temperature sensing (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]).

**Temperature dependence of HPPC-derived quantities.** Only the INR21700-50G study reports how HPPC results change with temperature. DCIR, R0 and R2 rose at low temperature, and τ2 grew as temperature fell. Discharge and regenerative power capability were highest at 30 °C and 45 °C and severely reduced at −10 °C. At −10 °C, OCV deviated from the 30 °C value by −0.21 % to −0.73 % above 30 % SOC and by up to −4.80 % at low SOC. The −10 °C tests ended early, before about 15–20 % SOC. The authors also note that the 1 h rest may not reach full OCV equilibrium, especially at low temperature (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]).

**Use for model parameterization and validation.** On the INR21700-50G, R0 comes from the instantaneous voltage drop. R1, R2, C1 and C2 are fitted with MATLAB fminsearch and averaged over the four pulse durations, feeding a second-order RC model weakly coupled to a two-node lumped thermal network. Fit quality was lower at low temperature: at 1C, MAPE was 0.876 % at −10 °C against 0.198 % at 45 °C. The thermal model was not validated (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]). On the INR18650-20R, 25 °C HPPC data calibrate a state-observer identification of a fractional-order first-order RC model. Its mean relative voltage error was 0.27 %, against 1.68 % for FFRLS and 3.37 % for a Kalman filter. The authors state that reaching the required chaotic state depends on manual tuning of memristor parameters (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]). On the INR21700-50E, HPPC-derived engineered features lowered MAE, MSE and MAPE of Linear Regression and Random Forest models, with R² stable, at 25 °C. The authors say other operating conditions would need further validation (Source: [[data-on-battery-health-and-performance-analysing-samsung-inr21700-50e]]).

## Literature Mentions

- [[data-on-battery-health-and-performance-analysing-samsung-inr21700-50e]]: 1 kHz micro-HPPC every 10 % SOC on 256 Samsung INR21700-50E cells at 25 °C supplies resistance features for an ML dataset.
- [[dataset-of-lithium-ion-cell-degradation-under-randomized-current-profi]]: HPPC at 0.5C/1C/2C (6 min pulses) every 20 randomized-current cycles tracks power loss in JGNE JGPFR26650, Samsung ICR18650-26J and INR21700-40T cells at room temperature.
- [[low-cost-electronic-dc-load-module-design-for-battery-capacity-evaluat]]: An open-source electronic DC load's HPPC mode is demonstrated to 2.5 V on an A123 AMP20M1HD-A cell; no temperature data.
- [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]: 25 °C HPPC data (SOC 0.9–0.1) on a Samsung INR18650-20R calibrate a state-observer fractional-order RC identification (MRE 0.27 %).
- [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]: Multi-duration (2–180 s) HPPC on the Samsung INR21700-50G from −10 to 45 °C yields OCV, DCIR, power maps and second-order RC parameters.

## Related Concepts

- [[parameter-identification|Parameter Identification]]
- [[internal-resistance|Internal Resistance]]
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]
- [[open-circuit-voltage|Open-Circuit Voltage]]

*Last updated: 2026-09-27*
