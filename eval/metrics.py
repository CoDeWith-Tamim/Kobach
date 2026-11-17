"""
KOBACH — Evaluation Harness (Stage A)
Attack taxonomy + legit queries চালিয়ে defense layer টেস্ট করা, আর metrics বের করা।
"""

import csv
import time
import uuid
from pathlib import Path

import yaml

import sys
sys.path.append(str(Path(__file__).parent.parent))
from defense.regex_prefilter import check as regex_check


def load_attacks(taxonomy_path: str):
    with open(taxonomy_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    rows = []
    for cat in data["categories"]:
        # নতুন format: cases (list of {lang, text})
        if "cases" in cat:
            for case in cat["cases"]:
                rows.append({"category": cat["id"], "lang": case["lang"], "text": case["text"]})
        # পুরনো format: examples (dict of lang -> text) — backward compatible
        elif "examples" in cat:
            for lang, text in cat["examples"].items():
                rows.append({"category": cat["id"], "lang": lang, "text": text})
    return rows


def load_legit(legit_path: str):
    with open(legit_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["legit_queries"]


def run_experiment(taxonomy_path: str, legit_path: str, out_path: str):
    run_id = str(uuid.uuid4())[:8]
    rows_out = []

    # Attack cases — bypass rate মাপার জন্য
    for row in load_attacks(taxonomy_path):
        start = time.time()
        result = regex_check(row["text"])
        latency_ms = (time.time() - start) * 1000
        rows_out.append({
            "run_id": run_id,
            "type": "attack",
            "category": row["category"],
            "lang": row["lang"],
            "text": row["text"],
            "blocked": result["flagged"],
            "matched_pattern": result["matched_pattern"],
            "latency_ms": round(latency_ms, 3),
        })

    # Legit cases — false-positive rate মাপার জন্য
    for text in load_legit(legit_path):
        start = time.time()
        result = regex_check(text)
        latency_ms = (time.time() - start) * 1000
        rows_out.append({
            "run_id": run_id,
            "type": "legit",
            "category": "n/a",
            "lang": "n/a",
            "text": text,
            "blocked": result["flagged"],
            "matched_pattern": result["matched_pattern"],
            "latency_ms": round(latency_ms, 3),
        })

    # CSV-তে লেখা
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows_out[0].keys())
        writer.writeheader()
        writer.writerows(rows_out)

    # Summary print
    attacks = [r for r in rows_out if r["type"] == "attack"]
    legits = [r for r in rows_out if r["type"] == "legit"]
    bypassed = sum(1 for r in attacks if not r["blocked"])
    false_positives = sum(1 for r in legits if r["blocked"])

    print(f"Run ID: {run_id}")
    print(f"Attack cases: {len(attacks)} | Bypassed (NOT blocked): {bypassed} "
          f"| Bypass rate: {bypassed/len(attacks)*100:.1f}%")
    print(f"Legit cases: {len(legits)} | False positives: {false_positives} "
          f"| False-positive rate: {false_positives/len(legits)*100:.1f}%")
    print(f"Full log saved to: {out_path}")


if __name__ == "__main__":
    base = Path(__file__).parent.parent
    run_experiment(
        taxonomy_path=str(base / "attacks" / "taxonomy.yaml"),
        legit_path=str(base / "data" / "legit_queries" / "sample.yaml"),
        out_path=str(base / "data" / "results" / "run_001.csv"),
    )
