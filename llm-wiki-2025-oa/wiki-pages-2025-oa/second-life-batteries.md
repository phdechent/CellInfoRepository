---
type: concept
aliases:
  - "Second-Life Batteries"
tags:
  - synthesis
---

# Second-Life Batteries

**Summary:** Three 2025 open-access papers collect new data on retired commercial 18650 cells destined for stationary second use, addressing second-life aging as a function of first-life usage and data-driven SOC and SoH estimation. Ambient temperature is controlled at 20–24 °C where reported, cell temperature sensing is rarely described, and no study examines temperature-dependent second-life behaviour.

## Synthesized Knowledge

**Aging and first-life history.** Retired Samsung INR18650-35E NCA cells from e-bike packs were first cycled at high (1.18C/0.58C) or low (0.58C/0.29C) current at 100% DoD to about 80% SoH, then cycled for 600 second-life cycles at 30% DoD around 50% SoC at 0.5C or 0.25C; capacity fade was about 2% per 1,000 cycles for high-current second life, 0.6% per 1,000 cycles for HC-LC, and LC-LC cells even showed a capacity increase, while the first-life current level had no significant influence under identical second-life conditions (Source: [[impact-of-first-life-usage-on-second-life-performance-of-lithium-ion-b]]). This study reports a 20 °C room-temperature setpoint in an insulated steel container with some unquantified variation, one thermocouple at the centre of each cell, and custom 18650 holders with welded joints and 4-probe contacts but no pressure constraint; DCIR (1 A, 60 ms pulses) and EIS/ACIR were tracked, and the degradation rates fed a payback analysis of four second-life BESS business cases (Source: [[impact-of-first-life-usage-on-second-life-performance-of-lithium-ion-b]]).

**State estimation without cell history.** For second-life Samsung ICR18650-22P cells with capacities of about 1400/1450–2300 mAh, a two-layer random forest first identifies the capacity class and then applies one of ten capacity-specific SOC models; trained on 18 and tested on 82 own discharge experiments, it achieved about 45 mAh capacity RMSE and 0.85% mean SOC RMSE offline, but 79.94 mAh and 1.8% in 15 real-time Raspberry Pi tests, with the higher online error attributed to training-set size and input noise (Source: [[self-soc-estimation-for-second-life-lithium-ion-batteries]]). This work covers only the discharging process of one SLB type and reports no ambient temperature control or cell temperature measurement (Source: [[self-soc-estimation-for-second-life-lithium-ion-batteries]]). For retired Samsung ICR18650-26F cells, six-cell Samsung packs and retired Panasonic NCR18650BD cells, an MM-GRU using CC charging time, charging current area and 1800 s voltage drop over a four-cycle window estimated SoH with Max AE below 3.8% and MAE not exceeding 1%, trained on a single battery and applied to others; tests ran at 24 °C in an environmental chamber for about 100 cycles under constant 0.5C or dynamic 0.2C–1C discharge (Source: [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]]). Its reported limitations are larger errors during rapid capacity decline and unsuitability of the voltage-drop feature for the Samsung packs (Source: [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]]).

**Boundary-condition gaps and differences.** The three studies differ in ambient conditions (20 °C setpoint with observed variation, 24 °C chamber, and not stated) and none reports temperature-dependent performance or aging of second-life cells (Source: [[impact-of-first-life-usage-on-second-life-performance-of-lithium-ion-b]]; Source: [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]]; Source: [[self-soc-estimation-for-second-life-lithium-ion-batteries]]). The data-driven models are purely lumped with no thermal component (Source: [[self-soc-estimation-for-second-life-lithium-ion-batteries]]; Source: [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]]), so their validity is bounded to the cell types, capacity ranges and (where reported) the single ambient temperature at which they were trained.

## Literature Mentions

- [[impact-of-first-life-usage-on-second-life-performance-of-lithium-ion-b]]: First-life current level of retired Samsung INR18650-35E NCA cells has no significant influence on 600-cycle, 30% DoD second-life aging at 20 °C.
- [[self-soc-estimation-for-second-life-lithium-ion-batteries]]: Two-layer random forest estimates capacity and SOC of second-life Samsung ICR18650-22P cells (0.85% offline, 1.8% real-time SOC RMSE).
- [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]]: MM-GRU estimates SoH of retired Samsung ICR18650-26F cells/packs and Panasonic NCR18650BD cells at 24 °C with MAE ≤ 1%.

## Related Concepts

- [[capacity-degradation|Capacity Degradation]]
- [[state-of-health-estimation|State-of-Health Estimation]]
- [[state-of-charge-estimation|State-of-Charge Estimation]]
- [[machine-learning|Machine Learning]]

*Last updated: 2026-09-27*
