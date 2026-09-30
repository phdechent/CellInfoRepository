---
cell_target: "Panasonic NCR18650BD"
doi: "https://doi.org/10.1038/s41598-025-15597-2"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Both"
tags:
  - literature_extraction
  - "State-of-Charge Estimation"
  - "CNN-LSTM"
  - "Internal Resistance"
---

# CNN-LSTM optimized with SWATS for accurate state-of-charge estimation in lithium-ion batteries considering internal resistance

## General Analysis

**Core Thesis:** The paper builds a battery test bench that records current, voltage, temperature and internal resistance, and uses it to create a drive-cycle dataset for the Panasonic NCR18650BD cell. A CNN-LSTM whose optimizer switches from Adam to SGDM (SWATS) is proposed for SOC estimation, and including measured internal resistance as an input is shown to roughly halve the estimation error on the own NCR18650BD data; the public CALCE Samsung INR18650-20R dataset is used for benchmarking.

**Methodological Focus**
- Testing Mode: Drive-cycle discharge tests (NYCC, UDDS, HWFET, LA92) with simultaneous internal resistance measurement (HIOKI BT3562); 2 A constant-current charge/discharge cycling for characterization
- Operating Conditions: Thermal chamber at 0 °C, 25 °C and 45 °C; 2 A constant-current full charge; 1 Hz sampling
- Degradation Markers: None

## Keyword Context

- [[state-of-charge-estimation|State-of-Charge Estimation]]: The paper's goal is accurate data-driven SOC estimation, evaluated by RMSE, MAE and maximum error on drive-cycle test cases.
- CNN-LSTM: A CNN-LSTM network trained with the SWATS optimizer is the proposed estimator and is compared with LSTM, CNN-LSTM and other data-driven models.
- [[internal-resistance|Internal Resistance]]: Measured internal resistance of the NCR18650BD shows a Pearson correlation of -0.960 with SOC and, used as an extra input, reduces LA92 MAE by 52.8% and RMSE by 47.6%.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** The study creates a Panasonic NCR18650BD dataset including internal resistance with an own test bench and uses it to show that a SWATS-optimized CNN-LSTM considering internal resistance improves SOC estimation; approach: Hybrid

> Evidence: "In this experiment, a Panasonic NCR18650BD battery cell was tested."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: produce a SOC-estimation dataset containing current, voltage, temperature and internal resistance, and test model generalization; tests: 20 charge–discharge cycles at constant 2 A for voltage/internal-resistance characterization; full charge at 2 A, 2 h thermal soak, then NYCC, UDDS, HWFET and LA92 drive-cycle discharges with recording of current, voltage and internal resistance; data origin: Both (own NCR18650BD tests plus the public CALCE/University of Maryland Samsung INR18650-20R dataset)

> Evidence: "After 20 charge–discharge cycles under a constant 2-A current, the average voltage and internal resistance characteristics were as shown in Fig. 2."

### Q3: Ambient Boundary Conditions

**Answer:** 0 °C, 25 °C and 45 °C via temperature test chamber (ESPEC GMC-71) with 2 h soak before each test; stability/tolerance: not reported

> Evidence: "Place the battery in the thermal chamber for 2 h at the set test temperature (0 ℃, 25℃, or 45℃)."

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Texas Instruments TMP1117 temperature sensor in the purpose-built battery monitor × count not reported at location not reported; attachment: not reported; sampling: 1 Hz

> Evidence: "A current sensor and temperature sensor (IN260 and TMP1117, respectively, manufactured by Texas Instruments) were used to measure the discharge current and temperature."

### Q6: Temperature-Dependent Performance

**Answer:** Not explicitly discussed.

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: SOC estimation from measured temperature, current, voltage and internal resistance; type: data-driven CNN-LSTM (one-dimensional convolution with eight filters, LSTM, fully connected layer) trained with the SWATS optimizer; thermal component: No (temperature is only an input feature)

> Evidence: "The input vectors are some measured signals of the battery, i.e., temperature, current, voltage, and resistance"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from network training (Adam switching to SGDM, dropout 30%, batch size 64, 50 time steps, up to 500 epochs); calibrated with own NCR18650BD data (NYCC, UDDS and HWFET) and with public CALCE Samsung data (US06 and DST); validated against own LA92 data at 25 °C (with internal resistance: MAE 0.017, RMSE 0.022, maximum error 9%; without: MAE 0.036, RMSE 0.042, maximum error 13%) and CALCE FUDS/DST data using RMSE, MAE, maximum error and a paired t-test (P = 0.0075)

> Evidence: "the training case was a mixture of NYCC, UDDS, and HWFET, and the test case was LA92 at an ambient temperature of 25℃."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Not explicitly discussed.

### Q11: Model Applicability and Limitations

**Answer:** Validated range: own NCR18650BD LA92 test at 25 °C; public CALCE data at 0 °C, 25 °C and 45 °C and initial SOC of 80%, 60% and 40%; explicitly reported limitations: on the CALCE data the maximum error exceeds 10% at 0 °C; larger errors occur in the middle and end of discharge; external interference and noise in the test platform reduce estimation performance on the own dataset

> Evidence: "At 0 ℃, the maximum error is greater than 10%, but most of the errors are still less than 5%."
