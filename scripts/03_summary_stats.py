"""Print reproducible project summary statistics."""
from pathlib import Path
import json
from lithomap.io import load_fault_slip
from lithomap.summary import geographic_extent, category_summary

df = load_fault_slip(Path("data/raw/2018_Navabpour_Fault-slip.tab"))
result = category_summary(df)
result["extent"] = geographic_extent(df)
print(json.dumps(result, indent=2))
