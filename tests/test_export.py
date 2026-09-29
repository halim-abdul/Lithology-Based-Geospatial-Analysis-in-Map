import json
import pandas as pd
from lithomap.export import export_localities_geojson

def test_geojson_export(tmp_path):
    df=pd.DataFrame({
        "Event":["A"],"Latitude":[50.0],"Longitude":[10.0],"Rock":["Granite"]
    })
    path=export_localities_geojson(df,tmp_path/"x.geojson")
    payload=json.loads(path.read_text())
    assert payload["type"]=="FeatureCollection"
    assert payload["features"][0]["geometry"]["coordinates"]==[10.0,50.0]
