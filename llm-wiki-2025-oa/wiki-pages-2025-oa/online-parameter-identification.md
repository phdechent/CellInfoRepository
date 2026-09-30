---
type: concept
aliases:
  - "Online Parameter Identification"
tags:
  - synthesis
---

# Online Parameter Identification

**Summary:** Online parameter identification in the 2025 corpus means recursively estimating equivalent-circuit-model (ECM) parameters (R0, RC pairs) from measured current and voltage during operation, to feed SOC or SOH estimators. Forgetting-factor recursive least squares (FFRLS) and its variants dominate, with one study proposing a chaotic-system state observer; all models are lumped, non-thermal and validated at one or two fixed ambient temperatures.

## Synthesized Knowledge

**Methods and model structures.** FFRLS identifies a first-order Thevenin model's ohmic resistance R0 in real time under dynamic loading (forgetting factor 0.95), smoothed by variational mode decomposition to form a resistance-increment indicator ΔR for an LSTM-based SOH estimator on Samsung SDI ICR18650-26F cells (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]). FFRLS with forgetting factor 0.9985 identifies a second-order Thevenin model alternating with a modified adaptive unscented Kalman filter for SOC estimation on an A123 Systems AMP20M1HD-A cell (Source: [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]). An improved adaptive FFRLS (IAFFRLS) with an arccot-based forgetting factor regulated between 0.985 and 1 identifies a second-order RC model for a weighted multi-innovation Sage–Husa adaptive EKF, checked on Samsung SDI INR18650-25R FTP-75 data (Source: [[soc-estimation-for-lithium-ion-batteries-based-on-weighted-multi-innov]]). A different route embeds a fractional-order (Caputo) first-order RC-ECM in a memristor-based fourth-order hyperchaotic system and uses a state observer to identify R0, R1 and C1 of a Samsung SDI INR18650-20R cell (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]). The forgetting-factor choice thus differs across studies (0.95, 0.9985, adaptive 0.985–1); no note compares these settings on a common cell.

**Contradicting assessments of FFRLS.** Three studies adopt FFRLS (or a variant) as their identification basis (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]; Source: [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]; Source: [[soc-estimation-for-lithium-ion-batteries-based-on-weighted-multi-innov]]), whereas the INR18650-20R study reports FFRLS as clearly inferior to its state observer, with a mean relative HPPC voltage error of 1.68 % vs. 0.27 % (Kalman filter 3.37 %) (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]). These comparisons are on different cells and protocols, so the corpus does not settle which identifier is preferable.

**Experimental boundary conditions.** Ambient temperature control ranges from explicit to absent: environmental-chamber characteristic tests at 10, 25 and 40 °C (also 35 °C) and aging at 45 °C/35 °C for the ICR18650-26F, with no tolerance or cell temperature sensing reported (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]); HPPC and DST at 25 °C and UDDS at 40 °C for the INR18650-20R, control method not reported (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]); constant 25 °C for the INR18650-25R (Source: [[soc-estimation-for-lithium-ion-batteries-based-on-weighted-multi-innov]]); and no ambient temperature reported for the A123 0.5C discharge and HIL tests (Source: [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]). None of the four notes reports mechanical constraint or cell temperature measurement. The only temperature-related statement is qualitative: ohmic resistance is strongly influenced by ambient temperature, which is why the resistance increment rather than absolute R0 is used (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]).

**Validation and limitations.** Validation is via terminal-voltage or state-estimation error: MRE 0.27 %/0.21 %/0.17 % for HPPC 25 °C/DST 25 °C/UDDS 40 °C (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]); SOC MAE 0.0030 and RMSE 0.0039 on FTP-75 (Source: [[soc-estimation-for-lithium-ion-batteries-based-on-weighted-multi-innov]]); SOH Max AE ≤ 1.98 % including cross-chemistry transfer to a Panasonic NCR18650B (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]); and RMSE/MAE/convergence time against PCS-1000 reference coulomb counting, where HIL errors exceed simulation errors due to sensor and ADC noise (Source: [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]). Reported limitations include manual tuning of memristor parameters and failure when non-chaotic (Source: [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]), constant-temperature laboratory validation only with SOH effects ignored (Source: [[soc-estimation-for-lithium-ion-batteries-based-on-weighted-multi-innov]]), and SOH errors peaking at capacity-recovery fluctuations after test pauses (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]). All identified models are lumped; the A123 study's 29-cell pack simulation models no cell-to-cell inhomogeneity (Source: [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]).

## Literature Mentions

- [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]: FFRLS (λ = 0.95) identifies Thevenin R0 online for a ΔR health indicator feeding MM-LSTM SOH estimation of Samsung SDI ICR18650-26F cells (Max AE ≤ 1.98 %).
- [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]: FFRLS (λ = 0.9985) second-order Thevenin identification with mAUKF SOC estimation on an A123 AMP20M1HD-A cell, validated in simulation, 0.5C experiment and HIL.
- [[online-parameter-identification-of-a-fractional-order-chaotic-system-f]]: Chaotic-system state observer identifies fractional first-order RC-ECM parameters of a Samsung SDI INR18650-20R at 25/40 °C, outperforming FFRLS and KF.
- [[soc-estimation-for-lithium-ion-batteries-based-on-weighted-multi-innov]]: Adaptive-forgetting IAFFRLS for a second-order RC model with WMISAEKF SOC estimation, verified on Samsung SDI INR18650-25R FTP-75 data at 25 °C.

## Related Concepts

- [[parameter-identification|Parameter Identification]]
- [[state-of-charge-estimation|State-of-Charge Estimation]]
- [[unscented-kalman-filter|Unscented Kalman Filter]]
- [[fractional-order-equivalent-circuit-model|Fractional-Order Equivalent Circuit Model]]

*Last updated: 2026-09-27*
