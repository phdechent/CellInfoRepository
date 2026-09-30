---
type: concept
aliases:
  - "State-of-Health Estimation"
tags:
  - synthesis
---

# State-of-Health Estimation

**Summary:** Seven 2025 open-access studies estimate the state of health (SoH) of commercial cylindrical and prismatic cells from their own aging data, using either data-driven networks/regressors (LSTM, GRU, RNN, ANN, random forest) or Kalman-filter co-estimation on equivalent circuit models. Most experiments run at a single controlled ambient temperature, and none explicitly reports mechanical constraints, so the models' temperature and mechanical validity is narrow.

## Synthesized Knowledge

**SoH definitions and end-of-life criteria differ between studies.** SoH is defined as current capacity over *rated* capacity for the Samsung ICR18650-26F (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]). It is defined over *initial* capacity for the EVE INR18650/33V (Source: [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]]), the Samsung INR21700-50S (Source: [[random-forest-based-machine-learning-model-design-for-21-700-5-ah-lith]]) and the CATL CB2W0 / Lishen LP27148134 LFP cells (Source: [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]]). It is defined over *nominal* capacity for retired Panasonic NCR18650BD and Samsung ICR18650-26F cells (Source: [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]]). The aging end-points also differ: a 20 % capacity-loss cut-off (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]), SoH < 80 % (Source: [[machine-learning-based-methodology-for-fast-assessment-of-battery-heal]]), 70 % of nominal capacity for the Lishen cells (Source: [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]]), and a fixed 300 cycles (Source: [[random-forest-based-machine-learning-model-design-for-21-700-5-ah-lith]]) or about 100 cycles (Source: [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]]). Because of these differences, the reported error metrics are not directly comparable.

**Model types and validation.** Data-driven models dominate. One is a multi-input metabolic LSTM that uses capacity degradation, discharge-voltage sample entropy and an ohmic-resistance increment ΔR. ΔR comes from a Thevenin model whose R0 is identified online by FFRLS (forgetting factor 0.95) and smoothed by VMD. This model reports a maximum SoH error of ≤ 1.66 % within the same cell type and ≤ 1.98 % cross-type, when trained on a Panasonic NCR18650B reference cell (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]). A metabolic GRU uses constant-current charging time, charging-current area and the 1800 s voltage drop, and needs only four cycles of history. It reports Max AE below 3.8 % and MAE ≤ 1 % on retired cells and six-cell packs (Source: [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]]). An RNN estimates the static capacity of Samsung INR21700-40T cells from 6-min 1C partial discharges with ICA/DVA-derived features (average RMSE 28.439 mAh, R² 0.9993) (Source: [[machine-learning-based-methodology-for-fast-assessment-of-battery-heal]]). A DoG-TVA feature extractor on [[incremental-capacity-analysis|Incremental Capacity Analysis]] curves feeds an ANN. It reaches an RMSE of 1.97 % even for 10 % DOD segments of the CATL 280 Ah cell (Source: [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]]). A random forest trained on voltage, current and surface temperature of an INR21700-50S reaches R² 0.94 and RMSE 0.0570, versus R² 0.909 and RMSE 0.0638 for SVR (Source: [[random-forest-based-machine-learning-model-design-for-21-700-5-ah-lith]]). The model-based alternative is multi-time-scale co-estimation: a UKF (SVD-modified) runs on the fast scale for SOC, and an EKF on the slow scale updates resistances and capacity. This approach is applied with a fractional-order second-order RC model to the Samsung INR18650-30Q, where SOH error stays within 0.25 % (Source: [[cooperative-estimation-method-for-soc-and-soh-of-lithium-ion-batteries]]). It is also applied with an integer-order second-order RC model and an OCV–SOC–SOH surface to the EVE INR18650/33V, where SOH error is within 2 % (DST) and 1 % (FUDS) (Source: [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]]). All of these models are lumped or non-spatial, and none includes a thermal component.

**Boundary conditions and temperature.** Ambient temperatures, where stated, vary between studies:
- ICR18650-26F aging at 45 °C and 35 °C, with characteristic tests at 10/25/40 °C (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]])
- ICR18650-26F (retired) at 24 °C (Source: [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]])
- INR21700-50S at 25 °C in a climatic chamber (Source: [[random-forest-based-machine-learning-model-design-for-21-700-5-ah-lith]])
- CATL/Lishen cells at 25 °C ± 0.2 °C, with a 10 h 45 °C stress that produced a downward capacity trend (Source: [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]])
- INR21700-40T at unquantified room temperature (Source: [[machine-learning-based-methodology-for-fast-assessment-of-battery-heal]])
- EVE cell at 25 °C only for the static capacity test (Source: [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]])
- INR18650-30Q with no temperature reported (Source: [[cooperative-estimation-method-for-soc-and-soh-of-lithium-ion-batteries]])

Cell temperature is recorded only as a surface temperature used as an ML input feature, and sensor type and attachment are not reported (Source: [[random-forest-based-machine-learning-model-design-for-21-700-5-ah-lith]]). The papers treat temperature differently: one uses the ohmic-resistance *increment* instead of absolute R0 because R0 depends strongly on ambient temperature (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]), while another feeds temperature directly as a feature (Source: [[random-forest-based-machine-learning-model-design-for-21-700-5-ah-lith]]). No paper states a mechanical constraint.

**Reported limitations.**
- Largest errors at SoH fluctuations caused by capacity recovery during test pauses (Source: [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]])
- Larger errors during sudden SoH changes; the voltage-drop feature was unsuitable for Samsung packs (Source: [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]])
- SoH error rising when SOC falls below 20 % (Source: [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]])
- Room-temperature-only data and overestimation from imbalanced aging data (Source: [[machine-learning-based-methodology-for-fast-assessment-of-battery-heal]])
- Higher accuracy only above 50 % SoH (Source: [[random-forest-based-machine-learning-model-design-for-21-700-5-ah-lith]])
- Dynamic temperature and pack level not investigated (Source: [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]])
- Temperature and aging not varied in validation (Source: [[cooperative-estimation-method-for-soc-and-soh-of-lithium-ion-batteries]])

## Literature Mentions

- [[a-novel-online-state-of-health-estimation-method-for-lithium-ion-batte]]: MM-LSTM with online FFRLS-identified ΔR estimates SoH of Samsung ICR18650-26F cells aged at 35/45 °C; Max AE ≤ 1.98 % even when trained on a Panasonic NCR18650B reference cell.
- [[cooperative-estimation-method-for-soc-and-soh-of-lithium-ion-batteries]]: Fractional-order RC model with SVD-UKF/EKF co-estimates SOC and SOH of a Samsung INR18650-30Q; SOH error within 0.25 %, temperature not reported.
- [[joint-estimation-of-soc-and-soh-based-on-kalman-filter-under-multi-tim]]: SVDUKF-EKF multi-time-scale estimator with OCV–SOC–SOH surface for the EVE INR18650/33V; SOH error within 2 % (DST) and 1 % (FUDS).
- [[machine-learning-based-methodology-for-fast-assessment-of-battery-heal]]: RNN estimates the static capacity of aged Samsung INR21700-40T cells from 6-min 1C partial discharges at room temperature (RMSE 28.439 mAh).
- [[random-forest-based-machine-learning-model-design-for-21-700-5-ah-lith]]: Random forest beats SVR for SoH prediction of a Samsung INR21700-50S cycled 300 times at 1C and 25 °C; accuracy best above 50 % SoH.
- [[smart-health-evaluation-for-lithium-ion-battery-with-super-short-segme]]: DoG-TVA IC-curve features plus an ANN estimate SOH of CATL CB2W0 and Lishen LP27148134 LFP cells from short charging segments (RMSE 1.97 % at 10 % DOD).
- [[the-state-of-health-estimation-of-retired-lithium-ion-batteries-using]]: MM-GRU estimates SoH of retired Samsung ICR18650-26F cells/packs and Panasonic NCR18650BD cells at 24 °C from four cycles of history (Max AE < 3.8 %).

## Related Concepts

- [[machine-learning|Machine Learning]]
- [[capacity-degradation|Capacity Degradation]]
- [[unscented-kalman-filter|Unscented Kalman Filter]]
- [[second-life-batteries|Second-Life Batteries]]

*Last updated: 2026-09-27*
