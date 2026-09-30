---
type: concept
aliases:
  - "Lithium Plating"
tags:
  - synthesis
---

# Lithium Plating

**Summary:** In the 2025 papers, lithium plating is studied on two Samsung SDI 21700 NCA cells. One study predicts plating with a model as a function of C-rate, SOC and temperature to design fast charging; the other detects it experimentally through lithium-stripping plateaus as the end point of lithiation inhomogeneities built up during continuous accelerated cycling.

## Synthesized Knowledge

**Model-based view (Samsung INR21700-50E).** An advanced single-particle model with a lithium-plating overpotential, SEI growth and a lumped heat balance was used to map the plating rate over C-rate, SOC and temperature (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]).
- Plating was found to cause about 72% of capacity loss at 2.1C charging.
- In the parametric study, raising temperature from 25 °C to 55 °C improved lithium-ion diffusivity and reduced plating by a factor of nine. This temperature effect is model-based only; no experimental aging comparison across temperatures was made.
- The resulting Thermal-Boost Fast Charging profile (3C start, stepping down with SOC, SOC 0.05 to 0.75 within 20 min) extended cycle life by 170% experimentally compared with 2.1C CCCV.
- The experimental ambient temperature was not reported. Cell temperature was measured by a thermocouple, and current was cut above 55 °C.
- The model does not include plating dissolution or SEI-plating interaction, which the authors give as the reason SOH error grows over cycling (about 9%).

**Experimental view (Samsung INR21700-50G).** This study used cells extracted from a Lucid Air and cycled them in 25 °C climate chambers without additional active temperature control, with NTC surface-temperature sensing and no reported mechanical constraint (Source: [[the-overlooked-role-of-battery-cell-relaxation-how-reversible-effects]]).
- Lithium-stripping plateaus in the rest-phase differential voltage confirmed plating shortly before the knee point and cell failure in highly inhomogenized cells.
- Shorter cycling interruptions, larger DOD and higher C-rates intensified lithiation and conducting-salt inhomogeneities, and these inhomogeneities preceded plating.
- Static or dynamic recovery phases roughly doubled cycle life.
- For 2C/2C cycling, stronger self-heating was assumed to reduce inhomogenization initially.

**Tensions between the two studies.** The two papers do not contradict each other numerically, because they address different cells and protocols. Their emphases differ in three ways:
- **Driver of plating:** the 50E study attributes plating mainly to charge C-rate, SOC and temperature during fast charging (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]). The 50G study identifies the test procedure itself, meaning the absence of rest and rehomogenization, as a key driver (Source: [[the-overlooked-role-of-battery-cell-relaxation-how-reversible-effects]]).
- **Reversibility:** the 50E model treats plating-related loss as irreversible, with no dissolution (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]). The 50G study shows that part of the capacity loss before plating is reversible and recovers during rest (Source: [[the-overlooked-role-of-battery-cell-relaxation-how-reversible-effects]]).
- **Temperature:** both suggest that higher cell temperature mitigates the precursors of plating. For the 50E this comes from the model's diffusivity argument (Source: [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]). For the 50G it is only an assumption about self-heating at 2C/2C (Source: [[the-overlooked-role-of-battery-cell-relaxation-how-reversible-effects]]).

## Literature Mentions

- [[development-of-a-fast-charging-strategy-considering-degradation-in-lit]]: SPM-based plating map for the Samsung INR21700-50E; plating causes about 72% of capacity loss at 2.1C, falls 9× from 25 to 55 °C (model), and a thermal-boost profile extends cycle life by 170%.
- [[the-overlooked-role-of-battery-cell-relaxation-how-reversible-effects]]: Samsung INR21700-50G (Lucid Air) aging at 25 °C shows lithium-stripping plateaus before the knee point, preceded by inhomogenization that rest and recovery cycles can reverse.

## Related Concepts

- [[fast-charging|Fast Charging]]
- [[capacity-degradation|Capacity Degradation]]
- [[electrochemical-thermal-model|Electrochemical-Thermal Model]]

*Last updated: 2026-09-27*
