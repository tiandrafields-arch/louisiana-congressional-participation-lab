"""Validate referential integrity of curated congressional map litigation records."""
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/congressional_map_litigation.json").read_text(encoding="utf-8"))
assert data["schema_version"] == 1
date.fromisoformat(data["last_verified"])
sources = {x["id"]: x for x in data["sources"]}
maps = {x["id"]: x for x in data["maps"]}
cases = {x["id"]: x for x in data["cases"]}
assert len(sources) == len(data["sources"])
assert len(maps) == len(data["maps"])
assert len(cases) == len(data["cases"])
assert {x["id"] for x in data["events"]} and len({x["id"] for x in data["events"]}) == len(data["events"])
for s in sources.values():
    assert urlparse(s["url"]).scheme == "https"
    date.fromisoformat(s["verified_on"])
for obj in [*data["maps"], *data["cases"], *data["events"]]:
    assert obj["source_ids"]
    assert set(obj["source_ids"]).issubset(sources), obj["id"]
for event in data["events"]:
    date.fromisoformat(event["date"])
    assert event["case_id"] in cases, event["id"]
    assert event["map_id"] in maps, event["id"]
assert {"2024-act2", "2026-act2"}.issubset(maps)
assert maps["2024-act2"]["id"] != maps["2026-act2"]["id"]
print("PASS: litigation source, event, map and case references validated")
