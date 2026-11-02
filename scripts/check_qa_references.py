"""Recompute every reference answer of the question set from cell profiles, with the templates and formatting of
scripts/generate_qa_dataset.py. No model calls.

    python scripts/check_qa_references.py                                   # current BatteryTypeJson
    python scripts/check_qa_references.py --data /path/to/BatteryTypeJson --out evaluation/qa_reference_check.csv

For each question: the cell(s) it names, the reference answer the generator would write from these profiles, and
whether it differs from the reference in evaluation/qa_dataset.csv. Active materials recorded by name (an
ActiveMaterial node with schema:name, e.g. "LithiumNickelManganeseCobaltOxide and LithiumNickelCobaltAluminiumOxide")
are read from the name.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_qa_dataset import load_all_cells  # noqa: E402

SINGLE = {  # template -> property, as in generate_qa_dataset.py
    "What is the rated capacity of the {full_name} battery?": "RatedCapacity",
    "Can you tell me the rated capacity of the {cell_name} battery from {manufacturer}?": "RatedCapacity",
    "How many Ah is the rated capacity of the {full_name}?": "RatedCapacity",
    "What's the capacity specification for {full_name}?": "RatedCapacity",
    "What is the nominal voltage of the {full_name} battery?": "NominalVoltage",
    "What’s the nominal voltage of the {cell_name} battery from {manufacturer}?": "NominalVoltage",
    "Can you provide the nominal voltage for the {full_name}?": "NominalVoltage",
    "How long is the cycle life of the {full_name} battery?": "CycleLife",
    "What is the cycle life of the {cell_name} battery from {manufacturer}?": "CycleLife",
    "How many cycles is the {full_name} rated for?": "CycleLife",
    "How heavy is the {full_name} battery?": "Mass",
    "What is the mass of the {cell_name} from {manufacturer}?": "Mass",
    "What is the weight specification for the {full_name}?": "Mass",
    "What is the upper voltage limit of the {full_name} battery?": "UpperVoltageLimit",
    "Can you provide the upper voltage limit for the {cell_name} from {manufacturer}?": "UpperVoltageLimit",
    "What is the lower voltage limit of the {full_name} battery?": "LowerVoltageLimit",
    "What’s the lower voltage limit for the {cell_name} from {manufacturer}?": "LowerVoltageLimit",
    "What is the charging current of the {full_name} battery?": "ChargingCurrent",
    "Can you tell me the charging current rating for the {cell_name} from {manufacturer}?": "ChargingCurrent",
    "What is the discharge current of the {full_name} battery?": "DischargingCurrent",
    "What is the standard discharge current rate for the {cell_name} from {manufacturer}?": "DischargingCurrent",
    "Can you tell me the maximum continuous discharge current for the {full_name} battery?": "MaximumContinuousDischargingCurrent",
    "What is the max continuous discharge current limit on the {full_name}?": "MaximumContinuousDischargingCurrent",
    "What is the height of the {full_name} battery?": "Height",
    "Can you provide the height dimension of the {cell_name} from {manufacturer}?": "Height",
    "What is the diameter of the {full_name} battery?": "Diameter",
    "Can you tell me the diameter of the {cell_name} from {manufacturer}?": "Diameter",
}
OTHER = {
    "What are the rated capacity and nominal voltage of the {full_name} battery?": "multi",
    "What is the operating voltage window (lower and upper limits) for the {full_name}?": "window",
    "Which battery has a higher rated capacity: the {full_name} or the {full_name2}?": "compare_capacity",
    "Is the {full_name} heavier than the {full_name2}?": "compare_mass",
    "What type of case form factor does the {full_name} battery use?": "case",
    "What cathode active material chemistry is used in the {full_name}?": "material",
    "Assuming nominal voltage and rated capacity, what is the approximate energy capacity in Wh of the {full_name}?": "energy",
    "What is the rated capacity of the {full_name} expressed in milliampere-hours (mAh)?": "mah",
    "What is the {prop} of the {full_name} battery?": "negative",
}
NEGATIVE_PROPS = {"nominal voltage", "rated capacity", "cycle life", "maximum continuous discharge current", "mass"}
CASES = ["PrismaticCase", "CylindricalCase", "PouchCase", "R18650", "R21700", "R26650"]


def pattern(template: str) -> re.Pattern:
    rx = re.escape(template)
    for name in ("full_name2", "full_name", "cell_name", "manufacturer", "prop"):
        rx = rx.replace(re.escape("{" + name + "}"), f"(?P<{name}>.+?)")
    return re.compile("^" + rx + "$")


PATTERNS = [(pattern(t), "single", p) for t, p in SINGLE.items()] + [(pattern(t), k, None) for t, k in OTHER.items()]


def load(data: Path) -> list:
    """The generator's cells, with materials recorded by name read from schema:name."""
    cells = load_all_cells(str(data))
    for c in cells:
        d = json.loads(Path(c["file"]).read_text(encoding="utf-8"))
        am = (d.get("hasPositiveElectrode") or {}).get("hasActiveMaterial")
        if isinstance(am, dict) and am.get("@type") == "ActiveMaterial" and am.get("schema:name"):
            c["active_material"] = am["schema:name"]
        c["case_types"] = [x["@type"] for x in d.get("hasCase", []) if isinstance(x, dict) and x.get("@type") in CASES]
    return cells


def fmt_single(val: float, unit: str) -> str:
    val_str = f"{int(val)}" if float(val).is_integer() else f"{val:g}"
    return f"{val_str} {unit}".strip()


def expected(kind: str, prop: str | None, groups: dict, by_full: dict, by_name: dict):
    """(reference the generator would write, the cells it used, note)."""
    def cells_for(key="full_name"):
        if key == "full_name" and "cell_name" in groups:
            return by_name.get((groups["cell_name"].strip(), groups["manufacturer"].strip()), [])
        return by_full.get(groups[key].strip(), [])

    if kind == "negative":
        if groups["prop"] not in NEGATIVE_PROPS:
            return None, [], "unparsed"
        found = cells_for()
        if found:
            p = {"nominal voltage": "NominalVoltage", "rated capacity": "RatedCapacity", "cycle life": "CycleLife",
                 "maximum continuous discharge current": "MaximumContinuousDischargingCurrent", "mass": "Mass"}[groups["prop"]]
            vals = sorted({fmt_single(*c["properties"][p]) for c in found if p in c["properties"]})
            return ("Not available" if not vals else " / ".join(vals)), found, "made-up cell name exists in the data"
        return "Not available", [], "made-up cell"
    found = cells_for()
    if not found:
        return None, [], "cell not found"
    if len(found) > 1:
        note = f"{len(found)} profiles with this name"
    else:
        note = ""
    c = found[0]
    P = c["properties"]
    if kind == "single":
        if prop == "Diameter" and "Diameter" not in P and c["case_type"] == "PrismaticCase":
            return "Not available", found, note
        return (fmt_single(*P[prop]) if prop in P else "Not available"), found, note
    if kind == "multi":
        if "RatedCapacity" not in P or "NominalVoltage" not in P:
            return "Not available", found, note
        (cv, cu), (vv, vu) = P["RatedCapacity"], P["NominalVoltage"]
        return f"Rated Capacity: {cv:g} {cu}, Nominal Voltage: {vv:g} {vu}", found, note
    if kind == "window":
        if "LowerVoltageLimit" not in P or "UpperVoltageLimit" not in P:
            return "Not available", found, note
        return f"{P['LowerVoltageLimit'][0]:g} V to {P['UpperVoltageLimit'][0]:g} V", found, note
    if kind in ("compare_capacity", "compare_mass"):
        other = cells_for("full_name2")
        if not other:
            return None, found, "second cell not found"
        d = other[0]
        p = "RatedCapacity" if kind == "compare_capacity" else "Mass"
        if p not in P or p not in d["properties"]:
            return "Not available", found + other, note
        v1, v2 = P[p][0], d["properties"][p][0]
        if kind == "compare_mass":
            return f"{'Yes' if v1 > v2 else 'No'} ({v1:g} kg vs {v2:g} kg)", found + other, note
        win, lose = (c, d) if v1 > v2 else (d, c)
        return (f"{win['full_name']} ({win['properties'][p][0]:g} Ah vs {lose['properties'][p][0]:g} Ah)",
                found + other, note + (" equal capacities" if v1 == v2 else ""))
    if kind == "case":
        return (c["case_type"] or "Not available"), found, note
    if kind == "material":
        return (c["active_material"] or "Not available"), found, note
    if kind == "energy":
        if "RatedCapacity" not in P or "NominalVoltage" not in P:
            return "Not available", found, note
        return f"{round(P['RatedCapacity'][0] * P['NominalVoltage'][0], 2):.2f} Wh", found, note
    if kind == "mah":
        return (f"{P['RatedCapacity'][0] * 1000:g} mAh" if "RatedCapacity" in P else "Not available"), found, note
    return None, found, "unparsed"


def check(data: Path, questions: Path) -> list:
    cells = load(data)
    by_full, by_name = {}, {}
    for c in cells:
        by_full.setdefault(c["full_name"], []).append(c)
        by_name.setdefault((c["cell_name"], c["manufacturer"]), []).append(c)
    rows = []
    for q in csv.DictReader(open(questions, encoding="utf-8")):
        hit = next(((kind, prop, m.groupdict()) for rx, kind, prop in PATTERNS if (m := rx.match(q["query"]))), None)
        if hit is None:
            rows.append({**q, "kind": "", "current": "", "status": "unparsed", "files": "", "note": ""})
            continue
        kind, prop, groups = hit
        if kind == "negative" and q["answer"] != "Not available":   # a single lookup phrased like a negative control
            kind, prop = "single", next((p for t, p in SINGLE.items() if pattern(t).match(q["query"])), None)
        cur, used, note = expected(kind, prop, groups, by_full, by_name)
        status = "cell not found" if cur is None else ("same" if cur == q["answer"] else "differs")
        rows.append({**q, "kind": kind + (f":{prop}" if prop else ""), "current": cur or "", "status": status,
                     "files": " ".join(Path(c["file"]).name for c in used), "note": note})
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", type=Path, default=ROOT / "BatteryTypeJson")
    ap.add_argument("--questions", type=Path, default=ROOT / "evaluation" / "qa_dataset.csv")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    rows = check(args.data, args.questions)
    from collections import Counter
    print(Counter(r["status"] for r in rows))
    for r in rows:
        if r["status"] != "same":
            print(f"{r['ID']:>4} {r['status']:15s} {r['kind']:28s} ref={r['answer']!r}  now={r['current']!r}  {r['note']}")
    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)


if __name__ == "__main__":
    main()
