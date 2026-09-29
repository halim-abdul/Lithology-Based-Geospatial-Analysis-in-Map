"""Export locality-level GeoJSON."""
from pathlib import Path
from lithomap.export import export_localities_geojson
from lithomap.io import load_fault_slip

df=load_fault_slip(Path("data/raw/2018_Navabpour_Fault-slip.tab"))
path=export_localities_geojson(df,"outputs/localities.geojson")
print(path)
