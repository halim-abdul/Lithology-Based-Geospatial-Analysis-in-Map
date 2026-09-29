"""Interoperable geospatial export helpers."""
from __future__ import annotations
import json
from pathlib import Path
import pandas as pd
from lithomap.spatial import locality_table

def export_localities_geojson(df: pd.DataFrame, path: str | Path) -> Path:
    features=[]
    for _, row in locality_table(df).iterrows():
        features.append({
            "type":"Feature",
            "properties":{
                "event":row["Event"],
                "observations":int(row["observations"]),
                "dominant_lithology":row["dominant_lithology"],
            },
            "geometry":{
                "type":"Point",
                "coordinates":[float(row["longitude"]),float(row["latitude"])],
            },
        })
    payload={"type":"FeatureCollection","features":features}
    path=Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path
