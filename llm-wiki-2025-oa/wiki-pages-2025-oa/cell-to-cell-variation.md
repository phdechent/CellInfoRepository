---
type: concept
aliases:
  - "Cell-to-Cell Variation"
tags:
  - synthesis
---

# Cell-to-Cell Variation

**Summary:** Cell-to-cell variation covers the spread in capacity, impedance, charging time and state of charge between nominally identical commercial cells, arising from manufacturing (nonconformance) or from operating inhomogeneities in modules. In the 2025 open-access corpus it is quantified with batch characterization datasets, used as a stochastic input in system simulations, and addressed by module design and active balancing.

## Synthesized Knowledge

Two dataset papers characterize fresh-cell batches under controlled ambient temperature. For eleven B-grade CALB L148N58A prismatic NMC/graphite cells (58 Ah), C/20 capacity tests, HPPC (1C and C/3 10 s pulses), scaled WLTP/UDDS/US06 cycles and EIS (0.01 Hz–3 kHz at 20/40/60/80% SOC) were run at 10, 25 and 40 °C in an ESPEC LU-114 chamber, with T-type thermocouples on each cell surface and one in chamber air; the explicit aim is to identify the distribution of post-manufacturing capacity and impedance variation (Source: [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]]). For the high-power Molicel INR-21700-P42A, 45 cells were screened at 25 °C (C/3 discharge with 1C pulses) and 12 cells (ten near-mean, two outliers) were characterized with capacity tests, high C-rate pulse/GITT tests up to 8C and EIS at 5, 25 and 40 °C for stochastic modelling; C/3 capacity changed by -4.25% to +0.66% between screening and characterization, and chamber regulation was imperfect (about 20% of 5 °C EIS tests recorded 8–10 °C, later stabilized at 5–7 °C) (Source: [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]]). Neither paper reports a mechanical constraint.

Temperature modulates the observed spread. Both datasets report that variability is larger at low temperature: the CALB capacity range is larger at 10 °C (Source: [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]]), and the P42A 5 °C pulse resistances are higher and more spread than at 25 and 40 °C, with spread decreasing as C-rate increases (Source: [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]]). Ohmic resistance is higher at lower temperature for the CALB cells (Source: [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]]). **Contradiction on capacity vs. temperature:** for the CALB L148N58A the median C/20 capacity increases monotonically from 10 to 40 °C (Source: [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]]), whereas for the Molicel P42A average discharge capacity is highest at 25 °C (about 3.9 Ah) and lower at both 5 °C and 40 °C (about 3.8 Ah) (Source: [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]]). The cells, chemistries (NMC/graphite vs. NMC/Si-graphite), formats and C-rates differ, so the two results are not directly comparable.

Variation can also be induced at module level. A 3D Ansys Fluent thermal-flow model of a 4S3P module of Samsung INR21700-40T cells (Joule heating from SOC-dependent internal resistance, literature thermal properties, validated on one cell at 25 °C with maximum deviations of 0.17 V / 5% and 0.74 °C / 3%) shows that temperature gradients between central and peripheral cells and interconnection-plate resistances drive current and SOC deviation; a proposed terminal connection reduced the end-of-cycle SOC deviation to 0.00004, but only for the 4S3P structure and in simulation (Source: [[a-modeling-technique-for-high-efficiency-battery-packs-in-battery-powe]]). For a five-cell series pack of Samsung INR18650-25R, an inductor-based cell-to-pack active balancer reduced voltage differences below 10 mV in 47 to 170 min; ambient and cell temperature were not reported (Source: [[inductor-based-active-balancing-topology-with-wide-voltage-range-capab]]).

Variation is further used as a stochastic system input or production-quality metric. Ten Panasonic-Sanyo NCR18650GA cells showed 1.69–2.44% charging-time variability after 1C partial discharges (33–83%) and 0.2C CC-CV recharge, implemented as 2% variability in a battery-swapping-station simulation; ambient temperature was not stated (Source: [[demand-adapting-charging-strategy-for-battery-swapping-stations]]). A production-quality perspective defines nonconformance as cell-to-cell variability and illustrates nondestructive inspection (ultrasound, 2D X-ray, CT) on a BYD FC4680 cell, without thermal or electrochemical testing (Source: [[challenges-and-opportunities-for-high-quality-battery-production-at-sc]]).

## Literature Mentions

- [[a-dataset-for-large-prismatic-lithium-ion-battery-cells-calb-l148n58a]]: Eleven fresh CALB L148N58A cells at 10/25/40 °C; median capacity rises with temperature, capacity spread largest at low temperature.
- [[a-modeling-technique-for-high-efficiency-battery-packs-in-battery-powe]]: CFD of a 4S3P Samsung INR21700-40T module links temperature gradients and terminal connection to SOC deviation (reduced to 0.00004).
- [[challenges-and-opportunities-for-high-quality-battery-production-at-sc]]: Defines nonconformance as cell-to-cell variability; illustrates ultrasound/X-ray/CT inspection on a BYD FC4680 cell.
- [[demand-adapting-charging-strategy-for-battery-swapping-stations]]: Ten Panasonic-Sanyo NCR18650GA cells show 1.69–2.44% charging-time variability, used as 2% in station simulation.
- [[high-power-lithium-ion-battery-characterization-dataset-for-stochastic]]: 45 Molicel INR-21700-P42A screened, 12 characterized at 5/25/40 °C; capacity peaks at 25 °C, 5 °C resistances higher and more spread.
- [[inductor-based-active-balancing-topology-with-wide-voltage-range-capab]]: Inductor-based active balancer brings a five-cell Samsung INR18650-25R pack below 10 mV imbalance in 47–170 min.

## Related Concepts

- [[battery-dataset|Battery Dataset]]
- [[battery-module-design|Battery Module Design]]
- [[battery-management-system|Battery Management System]]
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]]

*Last updated: 2026-09-27*
