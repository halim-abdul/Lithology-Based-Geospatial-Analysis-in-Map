"""Generate lithology and fault-type maps."""
from pathlib import Path
from lithomap.io import load_fault_slip
from lithomap.visualize import save_fault_map, save_lithology_map

df=load_fault_slip(Path("data/raw/2018_Navabpour_Fault-slip.tab"))
save_lithology_map(df, "outputs/map_lithology.png")
save_fault_map(df, "outputs/map_fault_types.png")
print("Wrote map outputs")
