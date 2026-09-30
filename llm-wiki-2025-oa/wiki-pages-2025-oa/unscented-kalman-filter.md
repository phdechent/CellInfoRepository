---
type: concept
aliases:
  - "Unscented Kalman Filter"
tags:
  - synthesis
---

# Unscented Kalman Filter

**Summary:** Two 2025 papers use modified Unscented Kalman Filters (UKF) on lumped second-order RC equivalent circuit models to estimate SOC in commercial cells. Both combine the filter with recursive-least-squares parameter identification and HPPC-derived OCV–SOC relations. Neither reports the test temperature or any temperature dependence.

## Synthesized Knowledge

**The two papers modify the filter in different ways.** On the A123 AMP20M1HD-A LFP cell (19.5 Ah), the modified adaptive UKF (mAUKF) weights the process-noise covariance estimate exponentially, to converge faster under large initial SOC errors. It alternates with forgetting-factor RLS (FFRLS, forgetting factor 0.9985) identification of a second-order Thevenin model (Source: [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]). On the EVE INR18650/33V cell, singular value decomposition replaces the Cholesky decomposition (SVDUKF) to improve accuracy and stability. The SVDUKF estimates SOC on a micro-time scale, while an EKF estimates resistance, polarization parameters and capacity (SOH) on a macro-time scale. Initial impedance values come from AFFRLS (Source: [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]]).

**Parameterization.** Both papers take the OCV–SOC relation from their own HPPC tests but fit it differently. The A123 study uses an 8th-order polynomial in SOC (Source: [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]). The EVE study fits a 6th-order polynomial OCV–SOC–SOH surface (RMSE 0.0146 V) to HPPC data at different aging stages. It reports an aging-dependent OCV shift of up to 248 mV between SOH 100 % and 80 % (Source: [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]]).

**Validation and boundary conditions.** The A123 mAUKF was validated in three ways: Simulink simulation, a single-cell 0.5C (9.75 A) discharge with PCS-1000 reference coulomb counting, and a hardware-in-the-loop bench with a Raspberry Pi 4. All used a 20 % initial SOC error and were compared with UKF and AUKF by RMSE, MAE and convergence time. The note reports no ambient temperature, mechanical constraint or cell temperature sensing (Source: [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]). The EVE SVDUKF-EKF was verified under DST (SOC RMSE 1.0531 %, SOH error within 2 %) and FUDS (SOC RMSE 1.5611 %, SOH error within 1 %), starting from an initial SOC of 80 % against a true 100 %. Only the static capacity test is stated to be at 25 °C. The temperatures of the aging, HPPC and DST/FUDS tests are not stated (Source: [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]]).

**Reported limitations.** The two papers name different failure modes. In the A123 study, hardware-in-the-loop errors were larger than in simulation because of sensor and ADC noise. Mismatch between the real and simulated battery models made initialization difficult. Transfer to large packs would need balancing, protection and higher computational efficiency; only a preliminary 29-cell pack simulation was done (Source: [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]). In the EVE study, terminal voltage and SOH errors grew once SOC fell below 20 %, which the authors attribute to model deviation at low SOC (Source: [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]]). Both models are lumped and have no thermal component. Neither paper therefore shows how well the filters hold up across ambient temperatures.

## Literature Mentions

- [[hardware-in-the-loop-simulation-for-online-identification-of-lithium-i]]: An exponentially weighted adaptive UKF with FFRLS on a second-order Thevenin model estimates SOC of the A123 AMP20M1HD-A under 20 % initial error, validated in simulation, a 0.5C experiment and HIL.
- [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]]: An SVD-based UKF (SOC) combined with an EKF (capacity/impedance) on the EVE INR18650/33V reaches an SOC RMSE of 1.05 % (DST) and 1.56 % (FUDS).

## Related Concepts

- [[state-of-charge-estimation|State-of-Charge Estimation]]
- [[state-of-health-estimation|State-of-Health Estimation]]
- [[online-parameter-identification|Online Parameter Identification]]
- [[battery-management-system|Battery Management System]]

*Last updated: 2026-09-27*
