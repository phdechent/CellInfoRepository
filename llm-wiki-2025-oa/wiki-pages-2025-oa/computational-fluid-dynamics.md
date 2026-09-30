---
type: concept
aliases:
  - "Computational Fluid Dynamics"
tags:
  - synthesis
---

# Computational Fluid Dynamics

**Summary:** In the 2025 papers, computational fluid dynamics means 3D thermal-flow simulation in Ansys Fluent or STAR-CCM+. Each model is validated on a single cell or small pack of a commercial cell at one controlled ambient temperature, then used numerically to explore module layouts, PCM-liquid cooling channels or nanofluid tab immersion cooling.

## Synthesized Knowledge

**Model set-ups.** Three studies used 3D CFD with three different battery sub-models:
- **Samsung INR21700-40T:** an Ansys Fluent 2024 R2 thermal-flow model with a Joule heat source based on SOC-dependent internal resistance, plus Coulomb-counted SOC per cell. It was expanded from a single cell to a 4S3P railway module to study how temperature gradients and terminal connections cause cell-to-cell SOC deviation (Source: [[a-modeling-technique-for-high-efficiency-battery-packs-in-battery-powe]]).
- **Samsung INR18650-30Q 3p pack:** STAR-CCM+ with the NTGK semi-empirical battery model, enthalpy-porosity PCM phase change and a 1 mm tetrahedral mesh, with mesh and time-step independence checked (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]).
- **Melasta SLPBB042126 pouch cell:** a transient Ansys Fluent model with Bernardi heat generation, anisotropic conduction, tab Joule heating and a two-phase mixture laminar nanofluid model (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]).

**Parameterization, boundary conditions and validation.** Parameter sources differ. The 40T model used literature properties (2887 kg/m3, 952 J/kg·K, 0.87 W/m·K), a single heat transfer coefficient and constant nickel-plate resistance (Source: [[a-modeling-technique-for-high-efficiency-battery-packs-in-battery-powe]]). The 30Q model used constant battery thermal conductivity and specific heat, literature PCM properties and an external h of 5 W/m2·K (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]). Only the Melasta study drew heat-source parameters from its own HPPC internal-resistance and entropic-coefficient measurements (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]). Each study validated at a single chamber-controlled ambient temperature:

| Cell | Ambient and instrumentation | Validation agreement |
|---|---|---|
| Samsung INR21700-40T | 25 °C chamber; railway driving profile; surface thermocouple ±1 °C | Maximum deviations 0.74 °C (3%) and 0.17 V (5%) (Source: [[a-modeling-technique-for-high-efficiency-battery-packs-in-battery-powe]]) |
| Samsung INR18650-30Q | 20 °C chamber, ±0.3 °C; three K-type thermocouples per cell at 1 s sampling | Predicted 50.6 °C vs measured 51.2 °C maximum surface temperature, error <1% (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]) |
| Melasta SLPBB042126 | 25 °C chamber with 1 h stabilization; seven T-type thermocouples including tab regions | Maximum RMSE 1.33 °C and maximum error 3.50% (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]) |

None of the three studies discusses mechanical constraint.

**Findings and limits of applicability.** In all three studies, the design scenarios beyond the validated case are purely numerical.
- **Samsung INR21700-40T:** the module analysis covers one driving cycle. The proposed terminal connection reduced maximum SOC deviation to 0.00004 but is stated to be optimized only for the 4S3P layout (Source: [[a-modeling-technique-for-high-efficiency-battery-packs-in-battery-powe]]).
- **Samsung INR18650-30Q:** experimentally, PCM gave a maximum surface temperature of 52.7 °C versus 126.1 °C for air. Numerically, channel layout D lowered the temperature by a further 9 °C. At 4C or more, the hybrid system could not keep temperatures within limits (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]).
- **Melasta SLPBB042126:** tab cooling reduced the cell temperature difference by 82.8% relative to surface cooling at 4C. However, excessive tab cooling can make the lower cell surface warmer than the upper section. The model assumes uniform internal heat generation and neglects radiation (Source: [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]).

**Internal inconsistencies.** The 30Q note reports two things that do not match. The PCM is described as paraffin wax with a 40 °C melting point, but its property table lists 1-tetradecanol. The PCM-case maximum surface temperature is given as 52.7 °C in the media comparison and 51.2 °C in the validation (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]).

## Literature Mentions

- [[a-modeling-technique-for-high-efficiency-battery-packs-in-battery-powe]]: Fluent thermal-flow model of Samsung INR21700-40T cells, validated on a single cell at 25 °C (0.74 °C / 0.17 V maximum deviation) and extended to a 4S3P railway module to minimise SOC deviation.
- [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]: STAR-CCM+ NTGK/PCM model of a Samsung INR18650-30Q 3p pack, validated within 1% at 2C and 20 °C and used to optimise hybrid PCM-liquid cooling channels.
- [[thermal-analysis-of-nanofluid-submerged-battery-tab-under-fast-chargin]]: Fluent nanofluid immersion model of the Melasta SLPBB042126 pouch cell, validated at 2C and 25 °C (RMSE ≤1.33 °C); tab cooling beats surface cooling at 4C.

## Related Concepts

- [[phase-change-material|Phase Change Material]]
- [[immersion-cooling|Immersion Cooling]]
- [[liquid-cooling|Liquid Cooling]]
- [[battery-module-design|Battery Module Design]]

*Last updated: 2026-09-27*
