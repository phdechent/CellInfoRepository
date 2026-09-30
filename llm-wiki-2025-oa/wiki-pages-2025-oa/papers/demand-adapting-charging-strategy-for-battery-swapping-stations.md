---
cell_target: "Panasonic-Sanyo NCR18650GA"
doi: "https://doi.org/10.3390/batteries11070251"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Battery Swapping Station"
  - "Dynamic Programming"
  - "Cell-to-Cell Variation"
---

# Demand-Adapting Charging Strategy for Battery-Swapping Stations

## General Analysis

**Core Thesis:** The paper derives a demand-adapting charging policy for an e-bike battery-swapping station using dynamic programming on a two-state station model, traffic-based demand forecasts and electricity price/CO2 data. Own charge tests on ten NCR18650GA cells quantify charging-time variability that is used in the station simulation.

**Methodological Focus**
- Testing Mode: Constant-current 1C partial discharge (33%, 50%, 67%, 83%) followed by CC (0.2C to 4.2 V)–CV recharge on 10 cells
- Operating Conditions: 1C discharge, 0.2C CC-CV charge to 4.2 V; ambient temperature not stated
- Degradation Markers: None measured (cell-to-cell charging-time variability of 1.69–2.44%)

## Keyword Context

- Battery Swapping Station: The charging policy is designed for a battery-swapping station for electric bikes whose 3.96 kWh packs are built from NCR18650GA cells.
- Dynamic Programming: A dynamic programming optimisation on a two-state reduced-order station model computes the daily charging policy minimising electricity cost and/or CO2 emissions.
- [[cell-to-cell-variation|Cell-to-Cell Variation]]: Measured charging-time variability between cells (1.69–2.44% depending on discharge level) is included as a 2% variability in the station simulation.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To derive and evaluate an optimized, demand-adapting charging policy for a battery-swapping station, using own charge tests on NCR18650GA cells to characterize charging-time variability; approach: Hybrid

> Evidence: "Battery tests were conducted to assess charging time variability"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: characterize charging time and its cell-to-cell variability for the station simulation; tests: 10 cells discharged at 1C to four levels of discharge (33%, 50%, 67%, 83%) and fully recharged with 0.2C CC to 4.2 V followed by CV; data origin: Own experiments

> Evidence: "A set of 10 battery cells was discharged and totally charged at four different levels of discharge, namely 33%, 50%, 67% and 83%."

### Q3: Ambient Boundary Conditions

**Answer:** Not explicitly discussed.

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: optimal charging policy (number of batteries activated for charging) minimizing electricity cost and/or CO2 emissions while ensuring battery availability; type: two-state reduced-order station model solved with dynamic programming, combined with queuing theory (Erlang C) for a battery margin buffer and a Matlab simulation environment with per-slot SOC; thermal component: Not stated

> Evidence: "The model simplifies the discrete system with N battery slots by considering only two states: the batteries recently replaced (x1), i.e., to be charged, and the batteries available for swapping (x2)"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from own charge tests (0.2C average charge rate with 2% variability), traffic measurements from the city of Valencia, open bike-rental data (demand ratio 0.005), literature-based initial SOC distribution and historical Spanish electricity cost/emission data; validated only in simulation against the default ASAP strategy (cost reductions of 7.6% in June and 10.71% in December; CO2 reductions of 16.9% and 26%)

> Evidence: "The SOC of a battery that was activated for charging was updated at an average rate of 0.2 C but with a variability of 2%, which corresponds to the values found in experimental tests."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (station-level model with two aggregate states; slots simulated independently in the validation environment); represented inhomogeneities: stochastic cell-to-cell charging-time variability only, no spatial resolution

> Evidence: "Each slot was simulated independently."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: simulation of a 36-slot station for one characteristic day in June and one in December, 800 W (0.2C) chargers, 90 s time step; explicitly reported limitations: DP assumes predefined battery demand and constant service time, and extreme events (e.g., meteorological events or accidents) may alter traffic leading to suboptimal operation

> Evidence: "The optimization via DP is deterministic and assumes a predefined battery demand and also a constant service time, which is not strictly true."
