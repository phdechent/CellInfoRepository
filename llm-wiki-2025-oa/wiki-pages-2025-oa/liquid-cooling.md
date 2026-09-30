---
type: concept
aliases:
  - "Liquid Cooling"
tags:
  - synthesis
---

# Liquid Cooling

**Summary:** In the 2025 open-access corpus, indirect liquid (water) cooling is investigated for small packs of commercial 18650 cells in combination with a phase change material or thermal interface materials, using own pack experiments to validate 3D CFD/finite-element models that then explore channel layout, flow rate, C-rate and material choices. Both studies emphasise inter-cell temperature uniformity, and both models are explicitly thermal-comparative with simplified electrochemistry.

## Synthesized Knowledge

**Configurations and results.** For a 3p Samsung SDI INR18650-30Q pack filled with PCM, four indirect water-channel layouts (A–D) beneath the pack were compared numerically; layout D achieved the lowest surface temperature and the highest heat transfer coefficient (209.2 W/m²·K), lowering surface temperature by 9 °C (17.8%) relative to PCM alone, and 0.108 L/min was identified as the optimal flow rate within a simulated range of 0.005–1.08 L/min (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]). For a 3s2p Panasonic-Sanyo NCR18650GA module in a custom aluminium manifold with deionised water at 40 mL/min, 1.4 mm thermal-interface-material slabs between cooling tubes and cells were compared; the cooling time constant scaled inversely with TIM thermal diffusivity, and 40 wt.% BN–60% TPU gave the best combination of fast cooling and inter-cell uniformity (Source: [[polymer-bn-composites-as-thermal-interface-materials-for-lithium-ion-b]]).

**Boundary conditions and temperature sensing.** The INR18650-30Q experiments used 2C constant-current discharge (4.2 V to 2.5 V, three repeats) in a chamber at 20 °C (±0.3 °C stated error), with three K-type thermocouples per cell (top, middle, bottom) plus enclosure and PCM-centre sensors sampled at 1 s; mechanical constraint was not discussed (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]). The NCR18650GA work used two setups: external hot-plate heating to ~45 °C followed by cooling in a hood with 120 cfm airflow, and continuous CC cycling at 1.35C, 1.4C (10 cycles), 2C and 2.7C in a sealed environmental chamber whose temperature was not reported; cell temperature came from six K-type thermocouples (one per cell, sampling not reported) plus a FLIR E60 infrared camera, and no pressure constraint was reported beyond the manifold fixture (Source: [[polymer-bn-composites-as-thermal-interface-materials-for-lithium-ion-b]]). Neither study reports temperature-dependent electrical performance or aging.

**Models, validation and limitations.** The INR18650-30Q study used STAR-CCM+ with the NTGK semi-empirical electro-thermal model and enthalpy-porosity PCM model (1 mm tetrahedral mesh, 2 s time step, external h = 5 W/m²·K), validated against its own 2C PCM-pack measurement (50.6 °C predicted vs. 51.2 °C measured, under 1% error); only this 2C case at 20 °C is validated, battery thermal conductivity and specific heat are constant, the hybrid system cannot keep temperatures within limits at ≥4C (operation ≤2C advised), and long-term durability at the optimal flow rate needs further research (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]). The NCR18650GA study combined a lumped Newtonian analytical model (τ ∝ 1/α_TIM) with a COMSOL 6.2 3D model using anisotropic cell thermal conductivity and laminar coolant flow, but with COMSOL's built-in LiMn2O4–graphite chemistry normalised to the NCA cell's capacity and C-rate (3.3 A = 1C); it was validated against own cycling data (Pearson correlation 0.9775 at 1.4C, within ±10% for relative temperature differences across C-rates), with simulations extending to 1C–8C, and the authors state that it is comparative rather than voltage-predictive and assumes constant other thermal paths and contact resistances (Source: [[polymer-bn-composites-as-thermal-interface-materials-for-lithium-ion-b]]).

**Differences between studies.** Coolant flow scales are not directly comparable: an optimum of 0.108 L/min derived purely numerically for a PCM-embedded 3p pack (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]) versus a fixed experimental 40 mL/min (0.04 L/min) for a TIM-coupled 3s2p module (Source: [[polymer-bn-composites-as-thermal-interface-materials-for-lithium-ion-b]]). The feasible C-rate range also differs by study: the PCM–liquid system is limited to ≤2C (Source: [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]), whereas the TIM module was operated experimentally up to 2.7C and simulated to 8C without a stated limit (Source: [[polymer-bn-composites-as-thermal-interface-materials-for-lithium-ion-b]]); cell type, pack layout and cooling architecture differ, so this is not a direct contradiction.

## Literature Mentions

- [[hybrid-pcm-liquid-cooling-system-with-optimized-channel-design-for-enh]]: Samsung SDI INR18650-30Q 3p pack at 20 °C; CFD-optimised indirect water channel (layout D, 0.108 L/min) cut surface temperature a further 9 °C below PCM alone.
- [[polymer-bn-composites-as-thermal-interface-materials-for-lithium-ion-b]]: Panasonic-Sanyo NCR18650GA 3s2p module with 40 mL/min water manifold; 40 wt.% BN–TPU TIM gave fastest cooling and best inter-cell uniformity, validated by COMSOL.

## Related Concepts

- [[phase-change-material|Phase Change Material]]
- [[computational-fluid-dynamics|Computational Fluid Dynamics]]
- [[battery-thermal-management|Battery Thermal Management]]
- [[battery-module-design|Battery Module Design]]

*Last updated: 2026-09-27*
