---
cell_target: "Kokam SLPB065070180"
doi: "https://doi.org/10.1038/s41467-025-62935-z"
template: "cell_thermal_methods_v2"
reviewed: "2026-09-27"
oa_status: "gold"
data_origin: "Own experiments"
tags:
  - literature_extraction
  - "Ultrasonic Time-of-Flight"
  - "Operando X-Ray Diffraction"
  - "Electrode Dilatometry"
---

# Exploring electrochemical dynamics in graphite||LiNi0.8Mn0.1Co0.1O2 cells via operando ultrasound and multiprobe approaches

## General Analysis

**Core Thesis:** The study aims to interpret operando ultrasound time-of-flight (ToF) signals of a commercial 11.6 Ah Kokam SLPB065070180 graphite||NMC811 pouch cell by correlating them with synchrotron XRD and electrode nanodilatometry. It concludes that from 10% to 80% SoC the ultrasound signal mainly reflects the graphite electrode (its elastic modulus during lithiation), while between 80% and 100% SoC the NMC811 H2 to H3 phase transition affects the signal.

**Methodological Focus**
- Testing Mode: Galvanostatic cycling at C/3 and C/8 plus a GITT-like protocol (C/3, 1 h pulses, 1 h relaxation) with operando ultrasound (two glued piezoceramic transducers) and operando XRD at ESRF BM02; three-electrode nanodilatometry at C/40 on harvested electrodes
- Operating Conditions: ~25 °C thermoregulated hutch, no pressure appliance, 2.7-4.2 V; nanodilatometry at 25 °C ± 0.1
- Degradation Markers: None

## Keyword Context

- Ultrasonic Time-of-Flight: ToF extracted from through-thickness ultrasound between two piezoceramic elements is the central signal whose evolution during charge, discharge and relaxation is interpreted.
- Operando X-Ray Diffraction: Operando synchrotron XRD tracks the graphite (002) and NMC811 (003) Bragg reflections simultaneously with ToF to attribute ToF changes to phase transitions.
- Electrode Dilatometry: Operando nanodilatometry in a three-electrode setup on single-sided electrodes from the same cell deconvolves graphite expansion from NMC811 contraction.

## Cell Experiment and Modelling Review

### Q1: Study Purpose and Approach

**Answer:** To improve the interpretability of ultrasound signal variations in the commercial graphite||NMC811 pouch cell by combining operando ultrasound with synchrotron XRD and nanodilatometry during cycling and relaxation; approach: Hybrid (experiments with an analytical ToF/Young's modulus estimation)

> Evidence: "combining operando ultrasound measurements with synchrotron X-ray diffraction and nanodilatometry"

### Q2: Experimental Purpose and Protocol

**Answer:** Purpose: correlate ultrasound ToF with structural and electrochemical processes of each electrode; tests: operando ultrasound plus scanning XRD during one C/3 cycle, one C/8 cycle and a GITT-like cycle (C/3 charging with 1 h pulses and 1 h relaxation), 2.7-4.2 V; cell disassembly and operando nanodilatometry of graphite and NMC811 electrodes in a three-electrode setup at C/40; checks of temperature sensitivity, lab-vs-beamline similarity and X-ray damage; full-cell thickness data taken from literature; data origin: Own experiments

> Evidence: "Three cycles were performed: theﬁrst cycle at the C/3 rate to verify the cell behavior, the second cycle at the C/8 rate"

### Q3: Ambient Boundary Conditions

**Answer:** ~25 °C via a thermoregulated beamline hutch (nanodilatometry: thermoregulated oven at 25 °C ± 0.1); stability/tolerance: not reported for the full-cell tests; ± 0.1 °C for the dilatometry oven

> Evidence: "In a ther- moregulated hutch at ~25 °C"

### Q4: Mechanical Boundary Conditions

**Answer:** None reported (cell cycled without a pressure appliance, placed on a custom sample holder enabling lateral scanning); magnitude: not applicable (the 25 kPa constant-pressure full-cell expansion data were taken from the literature); fixture: custom sample holder developed by Lyonnard's group

> Evidence: "without a pressure appliance"

### Q5: Cell Temperature Measurement

**Answer:** Cell surface temperature was measured in additional measurements (sensor type, count, placement, attachment and sampling not reported); reported decreases of 0.1-0.3 K during relaxation periods R1 and R2 and ~1 K during R3

> Evidence: "Additional temperature measurements indicate that the surface temperature of the cell decreased by 0.1 K to 0.3 K during R1 and R2"

### Q6: Temperature-Dependent Performance

**Answer:** Based on previous laboratory experiments with similar commercial cells, a ToF temperature dependency of 26 ns/K was estimated; the average 12 ns ToF decrease during relaxation phases corresponded to an inferred ~0.5 K temperature decrease, larger than the measured 0.1-0.3 K surface temperature drop (attributed to ultrasound probing the cell interior)

> Evidence: "an estimated dependency of 26 ns/K was derived"

### Q7: Temperature-Dependent Aging

**Answer:** Not explicitly discussed.

### Q8: Model Purpose and Type

**Answer:** Purpose: explain the ToF evolution by numerically estimating the average effective Young's modulus of the full cell during charging; type: analytical ToF relation (ToF as function of mass, section, thickness and effective elastic modulus, Eq. 1) plus electrode weighting functions from three-electrode data; thermal component: No

> Evidence: "on the basis of the thickness evolution data (extracted from the full-cell expansion, Fig.2b) and the ToF signal measured"

### Q9: Model Parameterization and Validation

**Answer:** Parameters from full-cell thickness evolution (literature data, ref. 26, combined with own nanodilatometry scaled by a factor of 34) and own measured ToF; calibrated with these data; validated qualitatively against DFT literature trends and literature bending tests (no quantitative metric)

> Evidence: "in agreement with bending tests reported in the litera- ture for both materials"

### Q10: Spatial Resolution and Inhomogeneity

**Answer:** Lumped (a single average effective elastic modulus through the cell thickness); represented inhomogeneities: none

> Evidence: "the average effective elastic modulus (Young’s modulus) of the material being crossed by ultrasonic waves"

### Q11: Model Applicability and Limitations

**Answer:** Validated range: 25 °C, low rates (C/3, C/8, C/40), 2.7-4.2 V on a fresh cell; explicitly reported limitations: nonmonotonic ToF evolution indicates complex correlations between cell components; quantitative ToF-structure links require further reproducible experiments, and harsh conditions (low/high temperature, high current, aged cells) remain to be studied; a mechanical relaxation contribution from binder or separator cannot be excluded

> Evidence: "Further measurements should be carried out to gain a deeper understanding of the ultrasound approach under harsh conditions"
