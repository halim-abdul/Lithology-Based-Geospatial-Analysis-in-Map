"""Validate raw dataset structure and expected dimensions."""
from pathlib import Path
from lithomap.io import load_fault_slip
from lithomap.schema import validate_schema, validate_ranges

DATA = Path("data/raw/2018_Navabpour_Fault-slip.tab")

df = load_fault_slip(DATA)
validate_schema(df)
validate_ranges(df)

assert len(df) == 1207, f"Expected 1207 rows, found {len(df)}"
assert df["Event"].nunique() == 93, "Unexpected number of outcrop localities"
print("Validation passed:", len(df), "rows;", df["Event"].nunique(), "localities")
