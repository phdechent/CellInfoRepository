---
cell_target: "A123 Systems ANR26650M1-B"
doi: "https://doi.org/10.3390/batteries11010038"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Cell Teardown Analysis"
  - "X-Ray Computed Tomography"
  - "Tab Design"
---

# Design Analysis of 26650 and 18650 LFP Cells for High Power and Low Temperature Use Cases

## General Analysis

**Core Thesis:** The study analyses the internal design and component thicknesses of five high-power and low-temperature 18650/26650 LFP cells, including the ANR26650M1B (green), using CT scans and tear-down, and derives reference CAD models. It finds that the 26650 green cell is not a scaled-up version of the same manufacturer's 18650 cell (orange) and relates tab number and anode properties to pulse capability and impedance.

**Methodological Focus**
- Testing Mode: Initial charge and capacity check, micro-CT scanning, tear-down in argon glovebox, micrometre and confocal laser-scanning microscopy thickness measurement
- Operating Conditions: Initial charging according to data sheet; CT scans at room temperature (no numeric value stated) at 250 kV / 160 µA helical scan for the green cell
- Degradation Markers: None (new cells used)

## Keyword Context

- [[cell-teardown-analysis|Cell Teardown Analysis]]: Cells were opened in an argon glovebox and their jelly rolls unrolled to measure electrode lengths, tab layouts and component thicknesses.
- [[x-ray-computed-tomography|X-Ray Computed Tomography]]: Pristine cells were scanned with a Comet YXLON FF85 at approximately 10.588 µm voxel size, the green ANR26650M1B with a helical scan of the total cell.
- Tab Design: The green cell uses a four-tab design, and configurations with more tabs were associated with higher maximum pulse currents.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To determine the geometry and component thicknesses of high-power and low-temperature LFP cells, including the ANR26650M1B, test design hypotheses (e.g. 26650 as extended 18650) and derive CAD reference models; approach: Hybrid

> Evidence: "The analysis focuses on the geometry and components' thicknesses and deriving CAD models for both cell formats."

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: confirm functionality and obtain internal design data; tests: initial full charge and capacity determination (green reached 94.58% of nominal), micro-CT helical scan, tear-down with micrometre and laser-scanning microscope measurements of electrodes, separators, tabs and can; data origin: Own experiments

> Evidence: "After successful charging, the cell capacity was determined and compared to the nominal capacity."

### Q3: Ambient Boundary Conditions

**Answer:** Room temperature (no numeric value stated) for CT scans; control method: not reported; stability/tolerance: not reported

> Evidence: "At room temperature, the five battery cells were subjected to a micro-tomographic analysis"

### Q4: Mechanical Boundary Conditions

**Answer:** Not explicitly discussed.

### Q5: Cell Temperature Measurement

**Answer:** Not explicitly discussed.

### Q6: Temperature-Dependent Performance

**Answer:** Not measured by the authors; based on data-sheet operating temperature ranges, the two cells with the lowest operating temperature use a minimal number of tabs, indicating a trade-off between low-temperature operation and high pulse capability

> Evidence: "both cells with the lowest operating temperature according to the data sheet utilise a minimal number of tabs"

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: 3D geometric representation of 18650 and 26650 high-power cells for virtual experiments such as finite element analysis; type: parameterized CAD model (Synera and Siemens NX); thermal component: Not stated

> Evidence: "facilitating its integration into virtual experiments such as finite element analysis"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from the authors' own CT and tear-down measurements (simplified 26650 layer thicknesses: 55 µm anode current collector, 30 µm anode coating, 20 µm separator, 55 µm cathode current collector, 45 µm cathode coating, 0.30 mm can); calibrated with: not applicable; validated against the number of windings of the examined cells as a quality check

> Evidence: "As a quality check, the number of windings for the jelly roll of the CAD models were compared with the investigated range of the examined cells."

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** 3D; represented inhomogeneities: none (spiral jelly roll without inter-layer spacing, without tab-induced deformation and with homogeneous wall thicknesses; tab connections not modelled)

> Evidence: "The derived models have a spiral-shaped jelly roll without space between the layers or deformation owing to the taps and homogeneous wall thicknesses."

### Q11: Model Applicability and Limitations

**Answer:** Validated range: not stated (geometric model only); explicitly reported limitations: simplified homogeneous layer thicknesses without thickness deviations, tab connections not designed as they must be adjusted per use case; CT and tear-down thickness data are only indicative due to measurement limitations

> Evidence: "The tab connections were not designed as the amount and positioning of tabs needed to be adjusted for each use case."
