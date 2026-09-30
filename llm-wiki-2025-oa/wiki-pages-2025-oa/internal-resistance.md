---
type: concept
aliases:
  - "Internal Resistance"
tags:
  - synthesis
---

# Internal Resistance

**Summary:** Two 2025 open-access studies measure or model internal resistance of commercial 18650 cells: as a directly measured input that improves data-driven SOC estimation of the Panasonic NCR18650BD, and as a fitted voltage-drop term in an empirical OCV ± IR model of a Sony-Murata US18650VTC6 string. Both treat resistance at fixed temperature and without aging.

## Synthesized Knowledge

**Measurement approaches.** For the Panasonic NCR18650BD, internal resistance was measured simultaneously with current, voltage and temperature on a purpose-built test bench using a HIOKI BT3562 during NYCC, UDDS, HWFET and LA92 drive-cycle discharges, after full charge at 2 A and a 2 h thermal soak in an ESPEC chamber at 0, 25 or 45 °C, with 1 Hz sampling; cell temperature came from a TI TMP1117 sensor whose placement is not reported (Source: [[cnn-lstm-optimized-with-swats-for-accurate-state-of-charge-estimation]]). For the Sony-Murata US18650VTC6, resistance was not measured directly but derived as the IR drop (OCV − CCV) from intermittent tests on a five-cell series string (10 min current at 1, 3 or 5 A, then 5 min rest), at unspecified room temperature, with 25 °C stated only for the IEC 62660-1 validation run and no reported temperature control method or cell temperature sensing (Source: [[experimental-testing-and-modeling-of-li-ion-battery-performance-based]]). Neither study reports mechanical boundary conditions.

**Dependence on state and use in models.** On the NCR18650BD, measured internal resistance showed a Pearson correlation of -0.960 with SOC, and adding it as an input to a SWATS-optimized CNN-LSTM reduced LA92 test error at 25 °C from MAE 0.036/RMSE 0.042 (max error 13%) to MAE 0.017/RMSE 0.022 (max error 9%), i.e. by 52.8% (MAE) and 47.6% (RMSE) (Source: [[cnn-lstm-optimized-with-swats-for-accurate-state-of-charge-estimation]]). On the VTC6 string, the discharge IR drop was fitted as an exponential function of capacity and the charge IR drop as a linear function of current (0.22985 + 0.19837·I); the resulting lumped OCV ± IR model reproduced continuous 1–5 A curves and the IEC 62660-1 profile with errors mostly below 2.5% (up to 3.5% during rests, because relaxation is not captured) (Source: [[experimental-testing-and-modeling-of-li-ion-battery-performance-based]]).

**Temperature and limitations.** Neither study quantifies resistance as a function of temperature. The NCR18650BD own-data model was validated only at 25 °C, while benchmarking on public CALCE Samsung INR18650-20R data at 0 °C gave maximum errors above 10% (Source: [[cnn-lstm-optimized-with-swats-for-accurate-state-of-charge-estimation]]). The VTC6 model is lumped (the string treated as one voltage source), limited to one cell type, fixed ambient temperature, currents up to 5 A and fresh cells, and its end-of-discharge deviations are attributed to temperature differences between pause and non-pause experiments (Source: [[experimental-testing-and-modeling-of-li-ion-battery-performance-based]]). The two papers parameterize resistance against different variables (SOC correlation for the NCR18650BD vs. capacity and current for the VTC6), so their resistance behaviour cannot be directly compared; no numerical contradiction between them is reported.

## Literature Mentions

- [[cnn-lstm-optimized-with-swats-for-accurate-state-of-charge-estimation]]: Measured internal resistance of the Panasonic NCR18650BD correlates at -0.960 with SOC and roughly halves CNN-LSTM SOC error on LA92 at 25 °C.
- [[experimental-testing-and-modeling-of-li-ion-battery-performance-based]]: IR drop of a five-cell Sony-Murata US18650VTC6 string fitted as exponential in capacity (discharge) and linear in current (charge) in an OCV ± IR model with errors below 2.5%.

## Related Concepts

- [[open-circuit-voltage|Open-Circuit Voltage]]
- [[state-of-charge-estimation|State-of-Charge Estimation]]
- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]]
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]

*Last updated: 2026-09-27*
