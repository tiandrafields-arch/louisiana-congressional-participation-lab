"""Validate October 2026 statewide and congressional district registration controls."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/registration_2026-10-01.json").read_text())
districts = data["districts"]
assert sorted(d["district"] for d in districts) == [1, 2, 3, 4, 5, 6]
assert sum(d["total_registered"] for d in districts) == data["total_registered"] == 2978143
assert sum(d["black_registered"] for d in districts) == data["black_registered"] == 933052
assert all(0 <= d["black_registered"] <= d["total_registered"] for d in districts)
print("PASS: district registrations reconcile to October 1 statewide controls")
