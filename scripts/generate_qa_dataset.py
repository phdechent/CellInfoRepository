"""Generate the stratified Q&A benchmark from the cell profiles.

    python scripts/generate_qa_dataset.py --data BatteryTypeJson --output evaluation/qa_dataset.csv

The questions are sampled with a fixed seed (42) from single-property lookups,
multi-property summaries, comparisons, case/chemistry questions, derived
calculations and negative controls (made-up cells, missing specifications).

Note: ``evaluation/qa_dataset.csv`` was generated from an earlier version of
``BatteryTypeJson`` and is the question set of the recorded results. Running
this script on the current data produces a different set; write it to a new
file if you want to keep the recorded one.
"""
import argparse
import os
import glob
import json
import random
import csv

def load_all_cells(folder_path="BatteryTypeJson"):
    json_files = glob.glob(os.path.join(folder_path, "*.json"))
    cells = []
    
    for f in sorted(json_files):
        try:
            with open(f, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            cell_name = data.get("schema:name", os.path.splitext(os.path.basename(f))[0])
            mfg_obj = data.get("schema:manufacturer", {})
            manufacturer = mfg_obj.get("schema:name", "Unknown") if isinstance(mfg_obj, dict) else str(mfg_obj)
            
            # Format full name cleanly
            if manufacturer != "Unknown" and not cell_name.lower().startswith(manufacturer.lower()):
                full_name = f"{manufacturer} {cell_name}"
            else:
                full_name = cell_name
                
            properties = {}
            for prop in data.get("hasProperty", []):
                if not isinstance(prop, dict):
                    continue
                ptype = prop.get("@type")
                if isinstance(ptype, list):
                    ptype = [t for t in ptype if t != "ConventionalProperty"]
                    ptype = ptype[0] if ptype else None
                if not ptype or ptype == "ConventionalProperty":
                    continue
                
                # Extract value
                val = None
                np = prop.get("hasNumericalPart")
                if isinstance(np, dict) and "hasNumericalValue" in np:
                    val = float(np["hasNumericalValue"])
                elif isinstance(np, (int, float)):
                    val = float(np)
                elif "hasNumericalValue" in prop and isinstance(prop["hasNumericalValue"], (int, float)):
                    val = float(prop["hasNumericalValue"])
                elif "value" in prop and isinstance(prop["value"], (int, float)):
                    val = float(prop["value"])
                if val is None or (isinstance(val, float) and val != val):
                    continue
                
                # Extract unit
                unit_raw = prop.get("hasMeasurementUnit", "")
                unit = str(unit_raw).split(":")[-1].split("#")[-1] if unit_raw else ""
                # Clean unit symbols
                unit_map = {
                    "AmpereHour": "Ah",
                    "Volt": "V",
                    "Kilogram": "kg",
                    "Gram": "g",
                    "Ampere": "A",
                    "Metre": "m",
                    "Millimetre": "mm",
                    "Cycle": "cycles"
                }
                unit = unit_map.get(unit, unit)
                if not unit:
                    if ptype in ["RatedCapacity"]: unit = "Ah"
                    elif ptype in ["NominalVoltage", "LowerVoltageLimit", "UpperVoltageLimit"]: unit = "V"
                    elif ptype in ["Mass"]: unit = "kg"
                    elif ptype in ["CycleLife"]: unit = "cycles"
                    elif "Current" in ptype: unit = "A"
                    elif ptype in ["Height", "Diameter", "Length", "Width"]: unit = "m"
                
                properties[ptype] = (val, unit)
                
            # Case type
            case_type = None
            for c in data.get("hasCase", []):
                if isinstance(c, dict) and "@type" in c:
                    ct = c["@type"]
                    if ct in ["PrismaticCase", "CylindricalCase", "PouchCase", "R18650", "R21700", "R26650"]:
                        case_type = ct
                        break
                        
            # Active material
            active_material = None
            pos = data.get("hasPositiveElectrode", {})
            if isinstance(pos, dict):
                am = pos.get("hasActiveMaterial", {}).get("@type")
                if am and am not in ["nan", "ambiguous - LCO"]:
                    active_material = am
                    
            cells.append({
                "file": f,
                "cell_name": cell_name,
                "manufacturer": manufacturer,
                "full_name": full_name.strip(),
                "properties": properties,
                "case_type": case_type,
                "active_material": active_material
            })
        except Exception as e:
            print(f"Error reading {f}: {e}")
            
    return cells

def generate_dataset(output_path="evaluation/qa_dataset_new.csv", target_size=300, folder_path="BatteryTypeJson"):
    random.seed(42)
    cells = load_all_cells(folder_path)
    print(f"Loaded {len(cells)} cells.")
    
    bucket_single = []
    bucket_multi = []
    bucket_comp = []
    bucket_cat = []
    bucket_calc = []
    bucket_neg = []
    
    # 1. Single-Property Lookups
    prop_templates = {
        "RatedCapacity": [
            "What is the rated capacity of the {full_name} battery?",
            "Can you tell me the rated capacity of the {cell_name} battery from {manufacturer}?",
            "How many Ah is the rated capacity of the {full_name}?",
            "What's the capacity specification for {full_name}?"
        ],
        "NominalVoltage": [
            "What is the nominal voltage of the {full_name} battery?",
            "What’s the nominal voltage of the {cell_name} battery from {manufacturer}?",
            "Can you provide the nominal voltage for the {full_name}?"
        ],
        "CycleLife": [
            "How long is the cycle life of the {full_name} battery?",
            "What is the cycle life of the {cell_name} battery from {manufacturer}?",
            "How many cycles is the {full_name} rated for?"
        ],
        "Mass": [
            "How heavy is the {full_name} battery?",
            "What is the mass of the {cell_name} from {manufacturer}?",
            "What is the weight specification for the {full_name}?"
        ],
        "UpperVoltageLimit": [
            "What is the upper voltage limit of the {full_name} battery?",
            "Can you provide the upper voltage limit for the {cell_name} from {manufacturer}?"
        ],
        "LowerVoltageLimit": [
            "What is the lower voltage limit of the {full_name} battery?",
            "What’s the lower voltage limit for the {cell_name} from {manufacturer}?"
        ],
        "ChargingCurrent": [
            "What is the charging current of the {full_name} battery?",
            "Can you tell me the charging current rating for the {cell_name} from {manufacturer}?"
        ],
        "DischargingCurrent": [
            "What is the discharge current of the {full_name} battery?",
            "What is the standard discharge current rate for the {cell_name} from {manufacturer}?"
        ],
        "MaximumContinuousDischargingCurrent": [
            "Can you tell me the maximum continuous discharge current for the {full_name} battery?",
            "What is the max continuous discharge current limit on the {full_name}?"
        ],
        "Height": [
            "What is the height of the {full_name} battery?",
            "Can you provide the height dimension of the {cell_name} from {manufacturer}?"
        ],
        "Diameter": [
            "What is the diameter of the {full_name} battery?",
            "Can you tell me the diameter of the {cell_name} from {manufacturer}?"
        ]
    }
    
    for cell in cells:
        fn = cell["full_name"]
        cn = cell["cell_name"]
        mfg = cell["manufacturer"]
        
        present_props = list(cell["properties"].keys())
        if present_props:
            sampled_props = random.sample(present_props, min(3, len(present_props)))
            for prop_name in sampled_props:
                if prop_name in prop_templates:
                    tmpl = random.choice(prop_templates[prop_name])
                    query = tmpl.format(full_name=fn, cell_name=cn, manufacturer=mfg)
                    val, unit = cell["properties"][prop_name]
                    val_str = f"{int(val)}" if isinstance(val, float) and val.is_integer() else f"{val:g}"
                    answer = f"{val_str} {unit}".strip()
                    bucket_single.append((query, answer))
                    
    # 2. Multi-Property Specs Summaries
    multi_eligible = [c for c in cells if "RatedCapacity" in c["properties"] and "NominalVoltage" in c["properties"]]
    for cell in multi_eligible:
        fn = cell["full_name"]
        cap_val, cap_unit = cell["properties"]["RatedCapacity"]
        volt_val, volt_unit = cell["properties"]["NominalVoltage"]
        
        query = f"What are the rated capacity and nominal voltage of the {fn} battery?"
        answer = f"Rated Capacity: {cap_val:g} {cap_unit}, Nominal Voltage: {volt_val:g} {volt_unit}"
        bucket_multi.append((query, answer))
        
        if "LowerVoltageLimit" in cell["properties"] and "UpperVoltageLimit" in cell["properties"]:
            l_val, _ = cell["properties"]["LowerVoltageLimit"]
            u_val, _ = cell["properties"]["UpperVoltageLimit"]
            q_win = f"What is the operating voltage window (lower and upper limits) for the {fn}?"
            a_win = f"{l_val:g} V to {u_val:g} V"
            bucket_multi.append((q_win, a_win))
            
    # 3. Comparative Queries
    cap_cells = [c for c in cells if "RatedCapacity" in c["properties"]]
    for _ in range(60):
        c1, c2 = random.sample(cap_cells, 2)
        v1, u1 = c1["properties"]["RatedCapacity"]
        v2, u2 = c2["properties"]["RatedCapacity"]
        if v1 != v2:
            winner = c1 if v1 > v2 else c2
            loser = c2 if v1 > v2 else c1
            wv, _ = winner["properties"]["RatedCapacity"]
            lv, _ = loser["properties"]["RatedCapacity"]
            query = f"Which battery has a higher rated capacity: the {c1['full_name']} or the {c2['full_name']}?"
            answer = f"{winner['full_name']} ({wv:g} Ah vs {lv:g} Ah)"
            bucket_comp.append((query, answer))
            
    mass_cells = [c for c in cells if "Mass" in c["properties"]]
    for _ in range(40):
        c1, c2 = random.sample(mass_cells, 2)
        v1, u1 = c1["properties"]["Mass"]
        v2, u2 = c2["properties"]["Mass"]
        if v1 != v2:
            query = f"Is the {c1['full_name']} heavier than the {c2['full_name']}?"
            ans = "Yes" if v1 > v2 else "No"
            answer = f"{ans} ({v1:g} kg vs {v2:g} kg)"
            bucket_comp.append((query, answer))
            
    # 4. Categorical & Ontological Queries
    case_cells = [c for c in cells if c["case_type"]]
    for cell in case_cells:
        query = f"What type of case form factor does the {cell['full_name']} battery use?"
        bucket_cat.append((query, cell["case_type"]))
        
    mat_cells = [c for c in cells if c["active_material"]]
    for cell in mat_cells:
        query = f"What cathode active material chemistry is used in the {cell['full_name']}?"
        bucket_cat.append((query, cell["active_material"]))
        
    # 5. Derived Physical Calculations & Unit Conversions
    for cell in multi_eligible:
        fn = cell["full_name"]
        cap_val, _ = cell["properties"]["RatedCapacity"]
        volt_val, _ = cell["properties"]["NominalVoltage"]
        energy_wh = round(cap_val * volt_val, 2)
        query = f"Assuming nominal voltage and rated capacity, what is the approximate energy capacity in Wh of the {fn}?"
        answer = f"{energy_wh:.2f} Wh"
        bucket_calc.append((query, answer))
        
    for cell in cap_cells:
        fn = cell["full_name"]
        cap_val, _ = cell["properties"]["RatedCapacity"]
        cap_mah = cap_val * 1000
        query = f"What is the rated capacity of the {fn} expressed in milliampere-hours (mAh)?"
        answer = f"{cap_mah:g} mAh"
        bucket_calc.append((query, answer))
        
    # 6. Negative Controls / Made-Up Cells & Missing Specs
    made_up_cells = [
        "Hyundai SLI 261305",
        "A123 70Ah Prismatic",
        "ATL Amperex Technology 9048168",
        "BMZ Sony BMZ 21700 60EM",
        "Panasonic NCR20700X",
        "CATL 250Ah Sodium-Ion",
        "LG Chem E99 Polymer",
        "Samsung INR18650-35Z",
        "BYD Blade 150Ah Gen2",
        "CALB CA300 High Power",
        "Envision AESC 80Ah",
        "Toshiba SCiB 45Ah LTO",
        "Moli Energy IBR-18650X",
        "Northvolt Lingonberry 50Ah",
        "SVOLT 115Ah Cobalt-Free"
    ]
    for fn in made_up_cells:
        props = ["nominal voltage", "rated capacity", "cycle life", "maximum continuous discharge current", "mass"]
        p = random.choice(props)
        query = f"What is the {p} of the {fn} battery?"
        bucket_neg.append((query, "Not available"))
        
    prismatic_cells = [c for c in cells if c["case_type"] == "PrismaticCase"]
    for cell in prismatic_cells:
        query = f"What is the diameter of the {cell['full_name']} battery?"
        bucket_neg.append((query, "Not available"))
        
    # Shuffle each bucket
    random.shuffle(bucket_single)
    random.shuffle(bucket_multi)
    random.shuffle(bucket_comp)
    random.shuffle(bucket_cat)
    random.shuffle(bucket_calc)
    random.shuffle(bucket_neg)
    
    # Stratified downselection to target_size (e.g. 300)
    qa_rows = []
    if target_size:
        alloc = {
            'single': min(130, len(bucket_single)),
            'multi': min(30, len(bucket_multi)),
            'comp': min(35, len(bucket_comp)),
            'cat': min(45, len(bucket_cat)),
            'calc': min(30, len(bucket_calc)),
            'neg': min(30, len(bucket_neg))
        }
        qa_rows.extend(bucket_single[:alloc['single']])
        qa_rows.extend(bucket_multi[:alloc['multi']])
        qa_rows.extend(bucket_comp[:alloc['comp']])
        qa_rows.extend(bucket_cat[:alloc['cat']])
        qa_rows.extend(bucket_calc[:alloc['calc']])
        qa_rows.extend(bucket_neg[:alloc['neg']])
        
        # If slightly under target_size, top off from remaining single-property lookups
        remaining_needed = target_size - len(qa_rows)
        if remaining_needed > 0:
            qa_rows.extend(bucket_single[alloc['single']:alloc['single'] + remaining_needed])
    else:
        qa_rows = bucket_single + bucket_multi + bucket_comp + bucket_cat + bucket_calc + bucket_neg
        
    # Final deterministic shuffle
    random.shuffle(qa_rows)
    qa_rows = qa_rows[:target_size] if target_size else qa_rows
    
    if output_path:
        with open(output_path, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "query", "answer"])
            for idx, (q, a) in enumerate(qa_rows, 1):
                writer.writerow([idx, q, a])
        print(f"Successfully wrote {len(qa_rows)} Q&A pairs to {output_path}.")
    return qa_rows

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data", default="BatteryTypeJson", help="folder with the JSON-LD cell profiles")
    parser.add_argument("--output", default="evaluation/qa_dataset_new.csv")
    parser.add_argument("--size", type=int, default=300, help="number of questions (0 = all)")
    args = parser.parse_args()
    generate_dataset(args.output, args.size or None, args.data)
