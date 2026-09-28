"""Load the battery-cell JSON-LD profiles into an RDF graph and query them.

The profiles in ``BatteryTypeJson/`` use the EMMO battery domain context
(https://w3id.org/emmo/domain/battery/context). The context is fetched once
and injected into every document before parsing, so the graph loads quickly
and can also be built offline from a local copy of the context
(set ``BATTERYGRAPH_CONTEXT=/path/to/context.json``).
"""

from __future__ import annotations

import concurrent.futures
import glob
import json
import os
import re
from urllib.parse import quote
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional

import rdflib
import requests

CONTEXT_URL = "https://w3id.org/emmo/domain/battery/context"
# Mirror of the same file, used if w3id.org cannot be reached.
CONTEXT_FALLBACK_URLS = (
    "https://raw.githubusercontent.com/emmo-repo/domain-battery/master/context/context.json",
)
SCHEMA = rdflib.Namespace("https://schema.org/")
# Most cells carry a full battinfo IRI as @id. Cells not (yet) registered there
# carry a bare local UID, which JSON-LD resolves against the document URL.
# This is the URL of the published profiles; override with BatteryGraph(base=...).
DOCUMENT_BASE = "https://raw.githubusercontent.com/phdechent/CellInfoRepository/main/BatteryTypeJson/"

# Numerical cell properties found in the profiles (EMMO term names).
NUMERIC_PROPERTIES = (
    "RatedCapacity",
    "NominalVoltage",
    "UpperVoltageLimit",
    "LowerVoltageLimit",
    "CycleLife",
    "Mass",
    "Height",
    "Diameter",
    "Width",
    "Length",
    "ChargingCurrent",
    "MaximumContinuousChargingCurrent",
    "DischargingCurrent",
    "MaximumContinuousDischargingCurrent",
)

# Common spellings used by people and LLMs -> EMMO term name.
PROPERTY_ALIASES = {
    "capacity": "RatedCapacity",
    "nominalcapacity": "RatedCapacity",
    "voltage": "NominalVoltage",
    "maxvoltage": "UpperVoltageLimit",
    "chargecutoffvoltage": "UpperVoltageLimit",
    "minvoltage": "LowerVoltageLimit",
    "dischargecutoffvoltage": "LowerVoltageLimit",
    "cycles": "CycleLife",
    "weight": "Mass",
    "chargecurrent": "ChargingCurrent",
    "maxcontinuouschargecurrent": "MaximumContinuousChargingCurrent",
    "maximumcontinuouschargecurrent": "MaximumContinuousChargingCurrent",
    "dischargecurrent": "DischargingCurrent",
    "maxcontinuousdischargecurrent": "MaximumContinuousDischargingCurrent",
    "maximumcontinuousdischargecurrent": "MaximumContinuousDischargingCurrent",
    "maxcontinuousdischargingcurrent": "MaximumContinuousDischargingCurrent",
    "continuousdischargecurrent": "MaximumContinuousDischargingCurrent",
}

# Chemistry acronyms -> EMMO term name.
TERM_ALIASES = {
    "NMC": "LithiumNickelManganeseCobaltOxide",
    "LFP": "LithiumIronPhosphate",
    "LCO": "LithiumCobaltOxide",
    "LTO": "LithiumTitanate",
    "NCA": "LithiumNickelCobaltAluminiumOxide",
    "DischargeCurrent": "DischargingCurrent",
    "ChargeCurrent": "ChargingCurrent",
    "MaximumContinuousDischargeCurrent": "MaximumContinuousDischargingCurrent",
    "MaximumContinuousChargeCurrent": "MaximumContinuousChargingCurrent",
}

UNIT_SYMBOLS = {
    "AmpereHour": "Ah",
    "Volt": "V",
    "Ampere": "A",
    "Kilogram": "kg",
    "Gram": "g",
    "Metre": "m",
    "Millimetre": "mm",
}
DEFAULT_UNITS = {"CycleLife": "cycles"}

# Types that only classify a node and carry no information for a user.
_UNINFORMATIVE_TYPES = {"ConventionalProperty", "ActiveMaterial", "PositiveElectrode"}


def load_context(source: Optional[str] = None) -> Dict[str, Any]:
    """Return the ``@context`` mapping of the EMMO battery context.

    ``source`` may be a URL or a local file path. If omitted, the environment
    variable ``BATTERYGRAPH_CONTEXT`` is used, then the official w3id URL and
    its GitHub mirror.
    """
    source = source or os.environ.get("BATTERYGRAPH_CONTEXT")
    candidates = [source] if source else [CONTEXT_URL, *CONTEXT_FALLBACK_URLS]
    errors = []
    for candidate in candidates:
        try:
            if os.path.exists(os.path.expanduser(candidate)):
                with open(os.path.expanduser(candidate), encoding="utf-8") as fh:
                    data = json.load(fh)
            else:
                response = requests.get(candidate, timeout=30)
                response.raise_for_status()
                data = response.json()
            return data.get("@context", data)
        except Exception as exc:  # try the next candidate
            errors.append(f"{candidate}: {exc}")
    raise RuntimeError("Could not load the EMMO battery context:\n" + "\n".join(errors))


def _normalize(text: str) -> str:
    """Lower-case and drop everything except letters and digits."""
    return re.sub(r"[^0-9a-z]", "", str(text).lower())


class EmmoContext:
    """Resolve EMMO term names to IRIs and back.

    * ``ctx.RatedCapacity`` or ``ctx["RatedCapacity"]`` -> ``rdflib.URIRef``
    * ``ctx.format_query(q)`` replaces ``{Term}`` placeholders in SPARQL with ``<IRI>``
    * ``ctx.label(iri)`` returns the readable term name of an IRI
    """

    def __init__(self, context: Optional[Dict[str, Any]] = None, source: Optional[str] = None):
        self.context = context if context is not None else load_context(source)
        prefixes = {k: v for k, v in self.context.items() if isinstance(v, str) and v.endswith(("#", "/"))}
        self.iri_map: Dict[str, rdflib.URIRef] = {}
        for key, val in self.context.items():
            iri = val.get("@id") if isinstance(val, dict) else val
            if not isinstance(iri, str) or key.startswith("@"):
                continue
            if ":" in iri and not iri.startswith("http"):
                prefix, local = iri.split(":", 1)
                if prefix in prefixes:
                    iri = prefixes[prefix] + local
            if iri.startswith("http"):
                self.iri_map[key] = rdflib.URIRef(iri)
        for alias, target in TERM_ALIASES.items():
            if target in self.iri_map and alias not in self.iri_map:
                self.iri_map[alias] = self.iri_map[target]
        self._lower = {k.lower(): k for k in self.iri_map}
        # Reverse map; prefer the canonical (non-alias) name.
        self._labels: Dict[str, str] = {}
        for key, iri in self.iri_map.items():
            if key not in TERM_ALIASES:
                self._labels.setdefault(str(iri), key)

    def resolve(self, name: str) -> Optional[str]:
        """Return the canonical term name for ``name`` (case-insensitive, aliases)."""
        if name in self.iri_map:
            return TERM_ALIASES.get(name, name)
        key = self._lower.get(name.lower())
        return TERM_ALIASES.get(key, key) if key else None

    def __getattr__(self, name: str) -> rdflib.URIRef:
        if name.startswith("_") or name in ("iri_map", "context"):
            raise AttributeError(name)
        if name in self.iri_map:
            return self.iri_map[name]
        raise AttributeError(f"Term '{name}' not found in the EMMO context.")

    def __getitem__(self, name: str) -> rdflib.URIRef:
        resolved = self.resolve(name)
        if resolved is None:
            raise KeyError(name)
        return self.iri_map[resolved]

    def label(self, value: Any) -> str:
        """Readable name for an IRI (EMMO term name, else the IRI fragment)."""
        text = str(value)
        if text in self._labels:
            return self._labels[text]
        if text.startswith("http") and "doi.org" not in text and "w3id.org/battinfo" not in text:
            return re.split(r"[#/]", text.rstrip("/"))[-1]
        return text

    def format_query(self, query: str) -> str:
        """Replace ``{Term}`` placeholders with ``<IRI>``; ``{{ }}`` becomes ``{ }``."""
        query = query.replace("{{", "{").replace("}}", "}")

        def replace(match: re.Match) -> str:
            term = match.group(1)
            resolved = self.resolve(term)
            if resolved is None:
                return match.group(0)  # not an EMMO term: leave untouched
            return f"<{self.iri_map[resolved]}>"

        return re.sub(r"\{([A-Za-z][A-Za-z0-9_]*)\}", replace, query)


@dataclass
class Cell:
    iri: str
    name: str
    manufacturer: str

    @property
    def full_name(self) -> str:
        if self.name.lower().startswith(self.manufacturer.lower()):
            return self.name
        return f"{self.manufacturer} {self.name}"


class BatteryGraph:
    """The knowledge graph of all battery-cell profiles plus query helpers."""

    def __init__(self, folder: str = "BatteryTypeJson", context: Optional[EmmoContext] = None,
                 base: str = DOCUMENT_BASE):
        self.ctx = context or EmmoContext()
        self.folder = folder
        self.base = base
        self.graph = self._load(folder)
        self.cells = self._index_cells()

    # ------------------------------------------------------------------ loading
    def _parse_file(self, path: str) -> rdflib.Graph:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        doc["@context"] = self.ctx.context
        g = rdflib.Graph()
        # base = document URL, so bare local UIDs become absolute IRIs
        base = self.base + quote(os.path.basename(path))
        g.parse(data=json.dumps(doc), format="json-ld", base=base)
        if len(g) == 0:
            raise ValueError(f"{path} produced no triples; check its @id and @context.")
        return g

    def _load(self, folder: str) -> rdflib.Graph:
        files = sorted(glob.glob(os.path.join(folder, "*.json")))
        if not files:
            raise FileNotFoundError(f"No JSON-LD files found in '{folder}'.")
        graph = rdflib.Graph()
        graph.bind("schema", SCHEMA)
        with concurrent.futures.ThreadPoolExecutor() as pool:
            for g in pool.map(self._parse_file, files):
                graph += g
        return graph

    def _index_cells(self) -> List[Cell]:
        rows = self.graph.query(
            """
            PREFIX schema: <https://schema.org/>
            SELECT ?cell ?name ?mfgName WHERE {
                ?cell a ?type ; schema:name ?name .
                OPTIONAL { ?cell schema:manufacturer/schema:name ?mfgName }
            }""",
            initBindings={"type": self.ctx.BatteryCell},
        )
        return [Cell(str(r.cell), str(r.name), str(r.mfgName or "")) for r in rows]

    def __len__(self) -> int:
        return len(self.graph)

    @property
    def manufacturers(self) -> List[str]:
        return sorted({c.manufacturer for c in self.cells if c.manufacturer})

    # ------------------------------------------------------------- cell lookup
    def find_cells(self, cell_name: str, manufacturer: Optional[str] = None) -> List[Cell]:
        """Find cells by model name, tolerant to case, spaces, dashes and to a
        manufacturer name included in ``cell_name``.

        Matching order: exact name, exact "manufacturer name", then substring.
        """
        query = _normalize(cell_name)
        for noise in ("battery", "cell", "liion"):
            if query.endswith(noise) and len(query) > len(noise):
                query = query[: -len(noise)]
        if not query:
            return []
        candidates = self.cells
        if manufacturer:
            m = _normalize(manufacturer)
            filtered = [c for c in candidates if m and (m in _normalize(c.manufacturer) or _normalize(c.manufacturer) in m)]
            candidates = filtered or candidates

        for key in (lambda c: _normalize(c.name), lambda c: _normalize(c.full_name)):
            exact = [c for c in candidates if key(c) == query]
            if exact:
                return exact
        # Substring match in both directions; ignore very short names that
        # would match almost anything (e.g. "D11").
        partial = [
            c for c in candidates
            if query in _normalize(c.full_name)
            or (len(_normalize(c.name)) >= 4 and _normalize(c.name) in query)
        ]
        # Prefer the longest (most specific) matching names.
        partial.sort(key=lambda c: -len(c.name))
        return partial

    # --------------------------------------------------------------- properties
    def _property_rows(self, cell: Cell, property_iri: Optional[rdflib.URIRef] = None):
        q = self.ctx.format_query(
            """
            SELECT ?propType ?value ?unit WHERE {
                ?cell {hasProperty} ?p .
                ?p a ?propType ;
                   {hasNumericalPart}/{hasNumericalValue} ?value .
                OPTIONAL { ?p {hasMeasurementUnit} ?unit }
            }"""
        )
        bindings = {"cell": rdflib.URIRef(cell.iri)}
        if property_iri is not None:
            bindings["propType"] = property_iri
        return self.graph.query(q, initBindings=bindings)

    def _unit(self, prop: str, unit_iri: Any) -> str:
        if unit_iri:
            name = self.ctx.label(unit_iri)
            return UNIT_SYMBOLS.get(name, name)
        return DEFAULT_UNITS.get(prop, "")

    def query_cell_property(self, cell_name: str, property_name: str, manufacturer: Optional[str] = None) -> List[Dict[str, Any]]:
        """Value and unit of one property for every cell matching ``cell_name``."""
        prop = self.resolve_property(property_name)
        if prop is None:
            return [{"error": f"Unknown property '{property_name}'. Known: {', '.join(NUMERIC_PROPERTIES)}"}]
        cells = self.find_cells(cell_name, manufacturer)
        if not cells:
            return [{"cell": cell_name, "property": prop, "value": None, "note": "cell not found in the knowledge graph"}]
        results = []
        for cell in cells[:5]:
            rows = list(self._property_rows(cell, self.ctx[prop]))
            if not rows:
                results.append({"cell": cell.full_name, "property": prop, "value": None, "note": "property not recorded for this cell"})
            for r in rows:
                results.append({"cell": cell.full_name, "property": prop, "value": float(r.value), "unit": self._unit(prop, r.unit)})
        return results

    def get_all_cell_properties(self, cell_name: str, manufacturer: Optional[str] = None) -> List[Dict[str, Any]]:
        """All numerical properties of the matching cell(s)."""
        cells = self.find_cells(cell_name, manufacturer)
        if not cells:
            return [{"cell": cell_name, "note": "cell not found in the knowledge graph"}]
        results = []
        for cell in cells[:3]:
            for r in self._property_rows(cell):
                prop = self.ctx.label(r.propType)
                if prop in _UNINFORMATIVE_TYPES:
                    continue
                results.append({"cell": cell.full_name, "property": prop, "value": float(r.value), "unit": self._unit(prop, r.unit)})
        return results

    def get_cell_info(self, cell_name: str, manufacturer: Optional[str] = None) -> List[Dict[str, Any]]:
        """Manufacturer, case / form factor, positive-electrode active material
        and number of linked publications of the matching cell(s)."""
        cells = self.find_cells(cell_name, manufacturer)
        if not cells:
            return [{"cell": cell_name, "note": "cell not found in the knowledge graph"}]
        q_case = self.ctx.format_query("SELECT ?t WHERE { ?cell {hasCase} ?c . ?c a ?t }")
        q_mat = self.ctx.format_query(
            "SELECT ?t WHERE { ?cell {hasPositiveElectrode}/{hasActiveMaterial} ?m . ?m a ?t }"
        )
        q_pubs = "PREFIX schema: <https://schema.org/> SELECT (COUNT(DISTINCT ?p) AS ?n) WHERE { ?cell schema:subjectOf ?p }"
        info = []
        for cell in cells[:5]:
            b = {"cell": rdflib.URIRef(cell.iri)}
            cases = sorted({self.ctx.label(r.t) for r in self.graph.query(q_case, initBindings=b)})
            mats = sorted({self.ctx.label(r.t) for r in self.graph.query(q_mat, initBindings=b)} - _UNINFORMATIVE_TYPES)
            n_pubs = int(next(iter(self.graph.query(q_pubs, initBindings=b))).n)
            info.append({
                "cell": cell.full_name,
                "id": cell.iri,
                "manufacturer": cell.manufacturer,
                "case": cases or None,
                "positive_electrode_active_material": mats or "not recorded",
                "linked_publications": n_pubs,
            })
        return info

    def resolve_property(self, name: str) -> Optional[str]:
        key = _normalize(name)
        if key in PROPERTY_ALIASES:
            return PROPERTY_ALIASES[key]
        for prop in NUMERIC_PROPERTIES:
            if _normalize(prop) == key:
                return prop
        resolved = self.ctx.resolve(name)
        return resolved if resolved in NUMERIC_PROPERTIES else None

    # ------------------------------------------------------------------- SPARQL
    def sparql(self, query: str, limit: int = 200) -> List[Dict[str, str]]:
        """Run a SPARQL query (``{Term}`` placeholders allowed) and return rows
        with EMMO IRIs translated back to readable term names."""
        formatted = self.ctx.format_query(query)
        if "prefix schema:" not in formatted.lower():
            formatted = "PREFIX schema: <https://schema.org/>\n" + formatted
        rows = []
        for i, row in enumerate(self.graph.query(formatted)):
            if i >= limit:
                break
            rows.append({str(var): self.ctx.label(row[var]) if row[var] is not None else None for var in row.labels})
        return rows
