---
type: concept
aliases:
  - "Incremental Capacity Analysis"
tags:
  - synthesis
---

# Incremental Capacity Analysis

**Summary:** In the 2025 corpus, incremental capacity analysis (ICA) is used as a feature source for data-driven SOH estimation from short partial discharge or charging segments, both for NMC 21700 cells and for large-format LFP cells. Both studies test at a single (room or 25 °C) ambient temperature and name temperature variation as an open limitation.

## Synthesized Knowledge

**Feature extraction from partial segments.** For Samsung SDI INR21700-40T cells, features inspired by ICA and differential voltage analysis (voltage change and capacity change) are computed from 6-min 1C constant-current partial discharges taken at every 10 % SOC decrement, min-max normalised, and fed to a recurrent neural network that estimates static capacity (Source: [[machine-learning-based-methodology-for-fast-assessment-of-battery-heal]]). For LFP cells (Lishen LP27148134, 40 Ah; CATL CB2W0, 280 Ah), a degradation-mechanism-guided scale-invariant feature transform (DoG-TVA) automatically extracts peak, valley and inflection features from IC curves of charging segments, including 10 % DOD segments where conventional IC peaks disappear, and an ANN maps them to SOH; IC peak shift/diminishing is attributed to LLI and LAM (Source: [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]]). The two studies thus differ in direction (discharge vs. charge segments), chemistry (NMC 21700 vs. LFP) and feature approach (hand-crafted ICA/DVA-derived vs. automatic IC-curve features).

**Protocols and boundary conditions.** The INR21700-40T data come from five cells aged by 2C CC charge/discharge for up to 1000 cycles (until SOH < 80 %) with periodic segmented 1C discharges, DCIR and capacity checks, at room temperature with no numeric value, control method or tolerance reported (Source: [[machine-learning-based-methodology-for-fast-assessment-of-battery-heal]]). The LFP data come from CCCV cycle-life tests in a temperature-controlled chamber at 25 °C ± 0.2 °C (Lishen at 2C, 1C, 0.3C with 100 %/60 % DOD to 70 % capacity; CATL at 140 A with 100/60/40/10 % DOD), with capacity calibration every 10 cycles, plus own EVE cells and public CALCE, Oxford and MST datasets (Source: [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]]). Neither note reports cell temperature measurement or mechanical constraint. The only temperature-dependent aging observation is a downward capacity trend of Lishen 2C cells attributed to a 10 h 45 °C stress simulating thermal-management failure (Source: [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]]).

**Validation and limitations.** The RNN for the INR21700-40T was trained on three cells, validated on one and tested on one over 50 iterations, reaching average RMSE 28.439 mAh and R² 0.9993; the authors note imbalanced aging data can cause overestimation and that room-temperature-only data limit applicability (Source: [[machine-learning-based-methodology-for-fast-assessment-of-battery-heal]]). The DoG-TVA-ANN was trained on one cell per condition and tested on the others, with test RMSE 0.93–1.87 % for Lishen, 2.33 % for CATL at 40 % DOD and 1.97 % at 10 % DOD; dynamic temperatures and pack-level analyses were not investigated (Source: [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]]). Error metrics are expressed in different units (mAh vs. % SOH), so accuracies are not directly comparable.

## Literature Mentions

- [[machine-learning-based-methodology-for-fast-assessment-of-battery-heal]]: ICA/DVA-derived features from 6-min 1C partial discharges feed an RNN estimating capacity of aged Samsung SDI INR21700-40T cells (RMSE 28.439 mAh, room temperature only).
- [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]]: DoG-TVA automatically extracts IC-curve features from short charging segments of Lishen LP27148134 and CATL CB2W0 LFP cells at 25 °C; SOH RMSE 1.97 % at 10 % DOD.

## Related Concepts

- [[state-of-health-estimation|State-of-Health Estimation]]
- [[machine-learning|Machine Learning]]
- [[capacity-degradation|Capacity Degradation]]
- [[open-circuit-voltage|Open-Circuit Voltage]]

*Last updated: 2026-09-27*
