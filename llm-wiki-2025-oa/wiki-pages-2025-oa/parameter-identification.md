---
type: concept
aliases:
  - "Parameter Identification"
tags:
  - synthesis
---

# Parameter Identification

**Summary:** Parameter identification extracts the values of equivalent-circuit model elements (OCV, R0, RC branches) from measured pulse or relaxation responses of a commercial cell. In the 2025 corpus it is performed offline on pulse data for the LG Chem INR21700 M50T and Samsung INR21700-50G, with the characterization C-rate and temperature strongly affecting the resulting parameters.

## Synthesized Knowledge

For the LG Chem INR21700 M50T (NMC-811), a 3-RC Thevenin model with SOC-dependent parameters was parameterized from own pulse-discharge tests (2% and 5% SOC steps, 1 h rests, Chroma 63204 DC load, 0.25 s logging) at 0.5C, 0.8C and 1C: OCV from the second relaxation point, R0 from the instantaneous voltage drop, and RC branches from a trust-region nonlinear least-squares triple-exponential fit with time constants bounded by impedance-spectrum regions; two direct methods, without (Method 1) and with (Method 2) capacitive compensation, were compared on PD, WLTC and high-current profiles (e.g. 1C PD RMSE 15.78 mV for Method 1 vs. 9.99 mV for Method 2) (Source: [[optimal-direct-parameter-extraction-of-a-lithium-ion-equivalent-circui]]). Increasing the parameterization C-rate introduced overshoot on lower-current profiles, Method 1 struggled on profiles well below its parameterization C-rate, and a second optimization on the PD curve led to overfitting; only discharge was parameterized and ambient temperature was not reported (Source: [[optimal-direct-parameter-extraction-of-a-lithium-ion-equivalent-circui]]).

For the Samsung INR21700-50G, a 2-RC model was parameterized from multi-duration HPPC tests (2, 10, 30 and 180 s pulses at every 5% SOC, 0.2C and 1C) at −10, 0, 10, 20, 30 and 45 °C in an ESPEC BTX-475 chamber, with one thermocouple near the centre of the cell surface and one in ambient air: OCV from the rested voltage before each pulse, R0 from the instantaneous drop, and R1, R2, C1, C2 fitted with MATLAB fminsearch and averaged over the four pulse durations for each SOC and temperature (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]). DCIR, R0, R2 and τ2 increased at low temperature, and fit accuracy degraded at low temperature (1C: RMSE 0.038 V at −10 °C vs. 0.009 V at 45 °C); the ECM is weakly coupled to a two-node core/surface lumped thermal network whose parameters and validation are not reported (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]).

The two studies differ in protocol choices that affect comparability. Both take R0 from the instantaneous voltage drop, but the M50T study fits RC branches to rest relaxations and keeps separate parameter sets per C-rate, finding that the characterization C-rate matters (Source: [[optimal-direct-parameter-extraction-of-a-lithium-ion-equivalent-circui]]), whereas the 50G study averages parameters across pulse durations (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]). There is also a tension on rest duration: the M50T study uses 1 h rests to derive OCV and relaxation parameters (Source: [[optimal-direct-parameter-extraction-of-a-lithium-ion-equivalent-circui]]), while the 50G study states that a 1 h rest may not reach full OCV equilibrium, especially at low temperature (Source: [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]). Neither study reports mechanical constraints, both models are lumped, and both are validated only on fresh cells.

## Literature Mentions

- [[optimal-direct-parameter-extraction-of-a-lithium-ion-equivalent-circui]]: 3-RC Thevenin parameters of LG Chem INR21700 M50T from 0.5C/0.8C/1C pulse discharge; capacitive-compensation Method 2 more accurate (1C PD RMSE 9.99 vs. 15.78 mV).
- [[systematic-characterization-of-lithium-ion-cells-for-electric-mobility]]: 2-RC parameters of Samsung INR21700-50G from multi-duration HPPC at −10 to 45 °C; resistances rise and fit accuracy falls at low temperature.

## Related Concepts

- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]
- [[open-circuit-voltage|Open-Circuit Voltage]]
- [[internal-resistance|Internal Resistance]]
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]

*Last updated: 2026-09-27*
