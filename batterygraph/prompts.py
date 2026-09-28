"""Prompts for query generation, answering and grading.

The answer, grading and "identifiably wrong" prompts are the ones used for the
recorded evaluation in ``evaluation/results``. The query-generation prompt is
built from the loaded graph, so property names and manufacturers always match
the current data in ``BatteryTypeJson/``.
"""

from typing import Iterable

PROPERTY_DESCRIPTIONS = {
    "RatedCapacity": "rated capacity (Ah)",
    "NominalVoltage": "nominal voltage (V)",
    "UpperVoltageLimit": "upper (charge cut-off) voltage limit (V)",
    "LowerVoltageLimit": "lower (discharge cut-off) voltage limit (V)",
    "CycleLife": "cycle life (cycles)",
    "Mass": "mass (kg)",
    "Height": "height (m)",
    "Diameter": "diameter (m), cylindrical cells only",
    "Width": "width (m), prismatic and pouch cells",
    "Length": "length / thickness (m), prismatic and pouch cells",
    "ChargingCurrent": "standard charging current (A)",
    "MaximumContinuousChargingCurrent": "maximum continuous charging current (A)",
    "DischargingCurrent": "standard discharging current (A)",
    "MaximumContinuousDischargingCurrent": "maximum continuous discharging current (A)",
}

QUERY_GENERATION = """You are an assistant that retrieves facts from a battery-cell knowledge graph.
Write the call(s) or the SPARQL query needed to answer the question. Return ONLY the code, no explanation.

Python helper functions (preferred):
1. query_cell_property(cell_name, property_name, manufacturer=None) -> value and unit of one numerical property
2. get_all_cell_properties(cell_name, manufacturer=None) -> all numerical properties of a cell
3. get_cell_info(cell_name, manufacturer=None) -> manufacturer, case / form factor, positive-electrode active material (cathode chemistry) and number of linked publications

Rules:
- Use the helper functions for questions about one or a few named cells. Cell names are matched tolerantly, so pass the model name as written in the question.
- To compare cells or retrieve several properties, return a Python list of calls: [call_1, call_2].
- Use SPARQL only for questions across many cells (counting, filtering, ranking).
- In SPARQL write EMMO terms as placeholders in curly braces, e.g. {{hasProperty}}, {{RatedCapacity}}; they are replaced by the correct IRIs. Use the prefix schema: <https://schema.org/> for schema:name, schema:manufacturer and schema:subjectOf. Never invent other predicates.

Graph structure (for SPARQL):
?cell a {{BatteryCell}} ; schema:name "model name" ; schema:manufacturer/schema:name "manufacturer" .
?cell {{hasProperty}} ?p . ?p a {{RatedCapacity}} ; {{hasNumericalPart}}/{{hasNumericalValue}} ?value .
?cell {{hasCase}} ?case . ?case a ?caseType .   (e.g. {{PrismaticCase}}, {{CylindricalCase}}, {{R18650}}, {{R21700}}, {{R26650}})
?cell {{hasPositiveElectrode}}/{{hasActiveMaterial}} ?m . ?m a ?material .   (e.g. {{NMC}}, {{LFP}}, {{NCA}}, {{LCO}}, {{LTO}})
?cell schema:subjectOf ?publication .   (publications that mention the cell, identified by DOI)

Property names for property_name / {{Property}}:
{properties}

Manufacturers in the graph (use them to separate manufacturer and model name):
{manufacturers}

Examples:
Question: What is the nominal voltage of the Samsung SDI INR21700-50E battery?
Code:
query_cell_property(cell_name="INR21700-50E", property_name="NominalVoltage", manufacturer="Samsung SDI")

Question: Which battery has a higher rated capacity: the Saft VL 5U or the Lishen LR2170SA?
Code:
[query_cell_property(cell_name="VL 5U", property_name="RatedCapacity", manufacturer="Saft"), query_cell_property(cell_name="LR2170SA", property_name="RatedCapacity", manufacturer="Lishen")]

Question: What cathode active material is used in the EVE Energy LF280-72174?
Code:
get_cell_info(cell_name="LF280-72174", manufacturer="EVE Energy")

Question: How many cells in the graph use an NMC cathode?
Code:
SELECT (COUNT(DISTINCT ?cell) AS ?count) WHERE {{
    ?cell {{hasPositiveElectrode}}/{{hasActiveMaterial}} ?m .
    ?m a {{NMC}} .
}}

Question: Which five cells are mentioned in the most publications?
Code:
SELECT ?name (COUNT(?pub) AS ?publications) WHERE {{
    ?cell schema:name ?name ; schema:subjectOf ?pub .
}} GROUP BY ?name ORDER BY DESC(?publications) LIMIT 5
"""


def query_generation_prompt(properties: Iterable[str], manufacturers: Iterable[str]) -> str:
    props = "\n".join(f"- {p}: {PROPERTY_DESCRIPTIONS.get(p, p)}" for p in properties)
    return QUERY_GENERATION.format(properties=props, manufacturers=", ".join(manufacturers))


# --- prompts used unchanged for the recorded evaluation -----------------------

FINAL_ANSWER_SYSTEM = (
    "You are a helpful assistant with access to query results from an RDF graph. "
    "Use the query results to answer the following question and do not make up additional "
    "information or context. Only return the answer value and unit and nothing else."
)

GRADER_SYSTEM = (
    "You are a helpful assistant and you are supposed to determine if an answer is correct. "
    "You are first given the answer and then the solution. Determine if the answer is correct "
    "with the given solution. Only return 0 if the answer is not correct or 1 if it is correct "
    "and nothing else."
)

IDENTIFIABLY_WRONG = """You are an evaluator assessing whether an AI assistant's answer is 'identifiably wrong' (abstained / admits lack of knowledge) versus 'guessing an incorrect fact' (hallucinated).

Given an AI Answer that is incorrect compared to the ground truth solution:
Determine if the AI Answer explicitly indicates that it does NOT know the answer, that information/data is missing, unavailable, unknown, empty query, or errored.

Reply with ONLY the number 1 if the AI Answer acknowledges lack of knowledge, data unavailability, or says it doesn't know ("I don't know", "Data not available", "Unknown", "Not available", "query empty", etc.).
Reply with ONLY the number 0 if the AI Answer makes a specific incorrect guess or states a wrong factual value (e.g. guessing "4.5 A" when the answer is "2.25 A", or guessing "Pouch" when the answer is "Prismatic").

Output ONLY '1' or '0' with no explanation."""

DIRECT_ANSWER = """You are an intelligent assistant with knowledge of batteries. You are also provided the context of the keywords. Relevant Keywords and their Explanations:
- name: The name of the entity.
- manufacturer: The manufacturer of the battery.
- subjectOf: instances of the battery being cited in literature
- hasPositiveElectrode: The positive electrode of the battery.
- hasActiveMaterial: The active material used in the electrode.
- hasCase: The case type of the battery.
- hasProperty: Various properties of the battery.

Properties:
- RatedCapacity: The rated capacity of the battery.
- CycleLife: The cycle life of the battery.
- NominalVoltage: The nominal voltage of the battery.
- UpperVoltageLimit: The upper voltage limit of the battery.
- LowerVoltageLimit: The lower voltage limit of the battery.
- DischargeCurrent: The discharge current of the battery.
- MaximumContinuousDischargeCurrent: The maximum continuous discharge current of the battery.
- Mass: The mass of the battery.
- ChargingCurrent: The charging current of the battery.
- Height: The height of the battery.
- Diameter: The diameter of the battery.

Here is a list of cell manufacturers, to distinguish between Cell Name and Manufacturer within the question: {manufacturers}

Example Questions and Direct Answers:
1. Question: What is the nominal voltage of the INR21700 M50 battery?
Answer: 3.7 V

2. Question: Who is the manufacturer of the INR21700 M50 battery?
Answer: LG Chem

3. Question: What is the capacity of the INR21700 M50 battery from LG Chem?
Answer: 4.8 Ah

Answer the following question. Only return the answer value and unit and nothing else."""
