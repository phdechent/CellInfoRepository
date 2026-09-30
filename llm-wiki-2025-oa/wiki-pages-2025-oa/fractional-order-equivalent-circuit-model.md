---
type: concept
aliases:
  - "Fractional-Order Equivalent Circuit Model"
tags:
  - synthesis
---

# Fractional-Order Equivalent Circuit Model

**Summary:** Fractional-order equivalent circuit models replace ideal capacitors with constant phase elements (CPEs) or fractional derivatives to capture dispersive (e.g. diffusion) dynamics in a lumped cell model. In the 2025 corpus they are used for SOC/SOH co-estimation, online RC parameter identification and as the cell model inside EIS measurement-system co-simulations, all without a thermal component.

## Synthesized Knowledge

For state estimation, a fractional-order second-order RC model (Grünwald–Letnikov discretization, CPE orders m = 0.9674, n = 0.9554) of the Samsung INR18650-30Q was identified offline from own 1C pulse-discharge data using the whale optimization algorithm and updated online by an EKF; it reduced the mean terminal-voltage error to 0.0047 V (max 0.0363 V) versus 0.0051 V for the integer-order model, and a strong-tracking SVD-UKF gave mean SOC errors of 0.45% (UDDS), 0.51% (NEDC) and 0.35% (HWFET) with SOH error within 0.25% (Source: [[cooperative-estimation-method-for-soc-and-soh-of-lithium-ion-batteries]]). The authors motivate the fractional order by fractional diffusion dynamics, but temperature and aging were not varied and the ambient temperature was not reported (Source: [[cooperative-estimation-method-for-soc-and-soh-of-lithium-ion-batteries]]).

For online parameter identification, a Caputo fractional-order first-order RC model of the Samsung INR18650-20R was embedded in a memristor-based fourth-order hyperchaotic system, and a state observer identified R0, R1 and C1 online; on own Arbin BT200 data the voltage MRE was 0.27% (HPPC, 25 °C), 0.21% (DST, 25 °C) and 0.17% (UDDS, 40 °C), outperforming FFRLS (1.68% on HPPC) and a Kalman filter (3.37%) (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]). Ambient temperatures of 25 and 40 °C are stated but the control method, stability and cell temperature sensing are not reported; limitations are that reaching the chaotic state requires manual memristor tuning, identification fails in the non-chaotic regime, and higher-order RC extensions complicate observer design (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]).

For EIS instrumentation design, two papers use the same fractional-order modified Randles model (series resistor plus a resistor parallel to a CPE) of a fully charged Samsung ICR18650-26J, parameterized from own Hioki IM3590 measurements. In a Cadence–Matlab co-simulation, the CPE was approximated by a Cauer I RC ladder within 1% over 4–120 Hz; RMS deviation from the ECM dropped from 18.5/17.8 mΩ (real/imaginary) to 0.59/0.86 mΩ after hardware refinement, with limitations including unmodelled connection impedances and about one hour per simulation (Source: [[an-integrated-co-simulation-framework-for-the-design-analysis-and-perf]]). Using that framework as a digital twin, a multiband multisine excitation reduced impedance-magnitude RMSE from 7.30 mΩ to 0.40 mΩ in [1–100] Hz; nonlinear and time-varying impedance was not covered (Source: [[multiband-multisine-excitation-signal-for-online-impedance-spectroscop]]). Both are validated only at 100% SOC, and temperature is not reported in either (Source: [[an-integrated-co-simulation-framework-for-the-design-analysis-and-perf]]; Source: [[multiband-multisine-excitation-signal-for-online-impedance-spectroscop]]).

Across all four papers the models are lumped, have no thermal coupling and represent no spatial inhomogeneity, and none reports mechanical constraint or cell temperature measurement. The validated ranges are narrow: single cells, one or two ambient temperatures at most, and fixed SOC in the EIS studies. No contradictions between papers were identified; the studies differ in model order (first-order, second-order, Randles-CPE) and in whether parameters are identified offline (Source: [[cooperative-estimation-method-for-soc-and-soh-of-lithium-ion-batteries]]), online (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]) or from impedance spectra (Source: [[an-integrated-co-simulation-framework-for-the-design-analysis-and-perf]]).

## Literature Mentions

- [[an-integrated-co-simulation-framework-for-the-design-analysis-and-perf]]: Randles-CPE model of a fully charged Samsung ICR18650-26J from Hioki EIS, used in a Cadence–Matlab EIS co-simulation (RMS deviation down to 0.59/0.86 mΩ).
- [[cooperative-estimation-method-for-soc-and-soh-of-lithium-ion-batteries]]: Fractional-order 2-RC model of Samsung INR18650-30Q (WOA + EKF) with SVD-UKF gives mean SOC errors 0.35–0.51% and SOH error within 0.25%.
- [[multiband-multisine-excitation-signal-for-online-impedance-spectroscop]]: Fractional-order ECM of a fully charged Samsung ICR18650-26J as digital twin; multiband multisine cuts magnitude RMSE from 7.30 to 0.40 mΩ.
- [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]: Caputo fractional first-order RC model of Samsung INR18650-20R identified online by a state observer (MRE 0.17–0.27% at 25/40 °C).

## Related Concepts

- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]]
- [[online-parameter-identification|Online Parameter Identification]]
- [[state-of-charge-estimation|State-of-Charge Estimation]]
- [[unscented-kalman-filter|Unscented Kalman Filter]]

*Last updated: 2026-09-27*
