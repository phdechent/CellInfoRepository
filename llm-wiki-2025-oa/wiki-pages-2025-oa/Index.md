---
type: index
---

# 2025 Open-Access Cell Review

*Built 2026-09-27 with Claude Code (Claude Opus 5.5), template `cell_thermal_methods_v2` (Q1–Q11).*

## Scope

- **Papers:** journal articles published in 2025 that the dataset classifies as **USED** for any of the 382 commercial cells in `BatteryTypeJson/`
- **Open access:** OpenAlex `oa_status` **gold** or **diamond** only (venue-level OA; hybrid/green/bronze excluded)
- **New-data screen:** each paper was read in full; papers whose target-cell data come only from public/literature datasets, or that report no measurements, were skipped (see [[Screening Log]])
- **Result:** 108 candidates → **60 reviewed** (56 own experiments, 4 own + public data), 48 skipped
- **Verification:** every `> Evidence:` quote is checked verbatim against the source text (`tools/verify_all.py review/queue/2025-gold-diamond-used.json`)

## Concepts

- [[machine-learning|Machine Learning]] (10 papers)
- [[battery-thermal-management|Battery Thermal Management]] (9 papers)
- [[electrochemical-impedance-spectroscopy|Electrochemical Impedance Spectroscopy]] (9 papers)
- [[state-of-charge-estimation|State-of-Charge Estimation]] (9 papers)
- [[capacity-degradation|Capacity Degradation]] (8 papers)
- [[state-of-health-estimation|State-of-Health Estimation]] (7 papers)
- [[cell-to-cell-variation|Cell-to-Cell Variation]] (6 papers)
- [[hybrid-pulse-power-characterization|Hybrid Pulse Power Characterization]] (5 papers)
- [[air-cooling|Air Cooling]] (4 papers)
- [[battery-dataset|Battery Dataset]] (4 papers)
- [[electrochemical-thermal-model|Electrochemical-Thermal Model]] (4 papers)
- [[fast-charging|Fast Charging]] (4 papers)
- [[fractional-order-equivalent-circuit-model|Fractional-Order Equivalent Circuit Model]] (4 papers)
- [[heat-generation|Heat Generation]] (4 papers)
- [[multi-temperature-evaluation|Multi-Temperature Evaluation]] (4 papers)
- [[online-parameter-identification|Online Parameter Identification]] (4 papers)
- [[phase-change-material|Phase Change Material]] (4 papers)
- [[thermal-runaway|Thermal Runaway]] (4 papers)
- [[battery-management-system|Battery Management System]] (3 papers)
- [[battery-module-design|Battery Module Design]] (3 papers)
- [[computational-fluid-dynamics|Computational Fluid Dynamics]] (3 papers)
- [[immersion-cooling|Immersion Cooling]] (3 papers)
- [[second-life-batteries|Second-Life Batteries]] (3 papers)
- [[x-ray-computed-tomography|X-Ray Computed Tomography]] (3 papers)
- [[cell-teardown-analysis|Cell Teardown Analysis]] (2 papers)
- [[incremental-capacity-analysis|Incremental Capacity Analysis]] (2 papers)
- [[internal-resistance|Internal Resistance]] (2 papers)
- [[liquid-cooling|Liquid Cooling]] (2 papers)
- [[lithium-plating|Lithium Plating]] (2 papers)
- [[open-circuit-voltage|Open-Circuit Voltage]] (2 papers)
- [[parameter-identification|Parameter Identification]] (2 papers)
- [[post-mortem-analysis|Post-Mortem Analysis]] (2 papers)
- [[unscented-kalman-filter|Unscented Kalman Filter]] (2 papers)

## Cells

- [[panasonic-sanyo-ncr18650ga|Panasonic-Sanyo NCR18650GA]] (5)
- [[a123-systems-anr26650m1-b|A123 Systems ANR26650M1-B]] (4)
- [[samsung-sdi-icr18650-26j|Samsung SDI ICR18650-26J]] (4)
- [[samsung-sdi-inr18650-25r|Samsung SDI INR18650-25R]] (4)
- [[samsung-sdi-inr18650-30q|Samsung SDI INR18650-30Q]] (4)
- [[samsung-sdi-inr21700-40t|Samsung SDI INR21700-40T]] (4)
- [[sony-murata-us18650vtc6|Sony-Murata US18650VTC6]] (4)
- [[samsung-sdi-inr21700-50e|Samsung SDI INR21700-50E]] (3)
- [[a123-systems-amp20m1hd-a|A123 Systems AMP20M1HD-A]] (2)
- [[eve-eve-inr18650-33v|EVE EVE-INR18650 33V]] (2)
- [[lg-chem-inr21700-m50t|LG Chem INR21700 M50T]] (2)
- [[panasonic-ncr18650bd|Panasonic NCR18650BD]] (2)
- [[samsung-sdi-icr18650-26f|Samsung SDI ICR18650-26F]] (2)
- [[samsung-sdi-inr18650-20r|Samsung SDI INR18650-20R]] (2)
- [[samsung-sdi-inr21700-50g|Samsung SDI INR21700-50G]] (2)
- [[a123-systems-26ah|A123 Systems 26AH]] (1)
- [[byd-fc4680|BYD FC4680]] (1)
- [[calb-l148n58a|CALB L148N58A]] (1)
- [[catl-cb2w0|CATL CB2W0]] (1)
- [[jgne-jgpfr26650|JGNE JGPFR26650]] (1)
- [[kokam-slpb065070180|Kokam SLPB065070180]] (1)
- [[kokam-slpb120216216g1h|Kokam SLPB120216216G1H]] (1)
- [[lg-chem-18650hg2|LG Chem 18650HG2]] (1)
- [[lg-chem-e66a|LG Chem E66A]] (1)
- [[lg-chem-inr21700-m50|LG Chem INR21700 M50]] (1)
- [[lishen-lp27148134|Lishen LP27148134]] (1)
- [[melasta-slpbb042126|Melasta SLPBB042126]] (1)
- [[molicel-inr-21700-p42a|Molicel INR-21700-P42A]] (1)
- [[panasonic-ncr18650pf|Panasonic NCR18650PF]] (1)
- [[samsung-sdi-icr18650-22p|Samsung SDI ICR18650-22P]] (1)
- [[samsung-sdi-inr-21700-50s|Samsung SDI INR-21700-50S]] (1)
- [[samsung-sdi-inr18650-35e|Samsung SDI INR18650-35E]] (1)
- [[samsung-sdi-inr21700-48x|Samsung SDI INR21700-48X]] (1)
- [[sony-murata-us18650vtc5|Sony-Murata US18650VTC5]] (1)

## Review questions

See the template in `review/templates/cell_thermal_methods_v2.json`: Q1 purpose/approach · Q2 experimental protocol · Q3 ambient conditions · Q4 mechanical constraint · Q5 cell temperature sensing · Q6 temperature-dependent performance · Q7 temperature-dependent aging · Q8 model type · Q9 parameterization/validation · Q10 spatial resolution · Q11 applicability/limitations.
