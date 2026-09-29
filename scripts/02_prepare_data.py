"""Build the clean, feature-rich analysis table."""
from pathlib import Path
from lithomap.clean import normalize_strings, coerce_numeric, drop_coordinate_gaps
from lithomap.features import add_frequency_features, add_orientation_features
from lithomap.io import load_fault_slip, save_processed
from lithomap.rhr import add_rhr_columns

raw = Path("data/raw/2018_Navabpour_Fault-slip.tab")
out = Path("data/processed/fault_slip_clean.csv")

df = load_fault_slip(raw)
df = normalize_strings(df)
df = coerce_numeric(df)
df = drop_coordinate_gaps(df)
df = add_rhr_columns(df)
df = add_orientation_features(df)
df = add_frequency_features(df)

save_processed(df, out)
print(f"Wrote {len(df)} rows to {out}")
