---
type: concept
aliases:
  - "Cell Teardown Analysis"
tags:
  - synthesis
---

# Cell Teardown Analysis

**Summary:** Two 2025 studies disassemble commercial cylindrical cells, the A123 ANR26650M1-B (LFP) and the Samsung SDI INR18650-20R (NMC532). The first uses teardown to extract internal geometry for CAD reference models; the second uses it to recover cathode material for direct recycling. Neither study measures electrochemical or thermal operating behaviour under controlled boundary conditions.

## Synthesized Knowledge

**Design analysis.** New high-power and low-temperature LFP cells, including the A123 ANR26650M1-B, were first charged, and the ANR26650M1-B reached 94.58 % of its nominal capacity. The cells were then micro-CT scanned at room temperature (Comet YXLON FF85, about 10.588 µm voxels, a 250 kV / 160 µA helical scan for the 26650 cell). Next they were opened in an argon glovebox, and their jelly rolls were unrolled to measure electrode lengths, tab layouts and component thicknesses by micrometre and confocal laser-scanning microscopy (Source: [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]). The teardown showed that the 26650 cell is not a scaled-up version of the same manufacturer's 18650 cell, and that it uses a four-tab design. More tabs were associated with higher maximum pulse currents (Source: [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]). The link to temperature was inferred from data sheets, not measured: the two cells with the lowest rated operating temperature use a minimal number of tabs, which suggests a trade-off between low-temperature operation and pulse capability (Source: [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]).

**Model output and limitations.** The teardown data were used to build 3D parameterized CAD models (Synera, Siemens NX) intended for finite element analysis. The simplified 26650 layers are: 55 µm anode current collector, 30 µm anode coating, 20 µm separator, 55 µm cathode current collector, 45 µm cathode coating and a 0.30 mm can. The models were checked only against the number of windings (Source: [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]). The models have homogeneous layers with no gaps or tab-induced deformation and do not model tab connections. The authors describe the CT and teardown thicknesses as only indicative (Source: [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]).

**Teardown for recycling.** For the Samsung INR18650-20R, cells were discharged for safety, opened and separated into cathode, anode and separator. Compositions were characterized by TGA and ICP-OES (Source: [[pretreatment-methods-for-recovering-active-cathode-material-from-spent]]). Thermal, NaOH, NMP and triethyl phosphate (TEP) pretreatments were then compared on cathode sheets and whole cells. TEP recovered 97 % on sheets with preserved stoichiometry and about 8 µm particles. A cycled cell gave slightly smaller particles (7.93 µm) and a lower XRD (003)/(101) intensity ratio of 1.45 (Source: [[pretreatment-methods-for-recovering-active-cathode-material-from-spent]]). The cell's operating temperature history is not reported (Source: [[pretreatment-methods-for-recovering-active-cathode-material-from-spent]]).

**Methodological differences.** The two teardown protocols differ in their preparation. The ANR26650M1-B was charged and capacity-checked and then opened under argon (Source: [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]). The INR18650-20R was discharged before disassembly, and no inert atmosphere is reported (Source: [[pretreatment-methods-for-recovering-active-cathode-material-from-spent]]). Neither paper reports mechanical constraint or cell temperature sensing.

## Literature Mentions

- [[design-analysis-of-26650-and-18650-lfp-cells-for-high-power-and-low-te]]: CT and argon-glovebox teardown of the A123 ANR26650M1-B (and other LFP cells) yield component thicknesses, a four-tab design and simplified 3D CAD models.
- [[pretreatment-methods-for-recovering-active-cathode-material-from-spent]]: Discharge and teardown of Samsung SDI INR18650-20R cells precede a comparison of NMC532 recovery pretreatments; TEP gives 97 % recovery on cathode sheets.

## Related Concepts

- [[x-ray-computed-tomography|X-Ray Computed Tomography]]
- [[post-mortem-analysis|Post-Mortem Analysis]]
- [[internal-resistance|Internal Resistance]]

*Last updated: 2026-09-27*
