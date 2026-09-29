import pandas as pd
from lithomap.spatial import bounding_box, locality_table

def sample():
    return pd.DataFrame({
        "Event":["A","A","B"],
        "Latitude":[50.0,50.0,51.0],
        "Longitude":[10.0,10.0,12.0],
        "Rock":["Granite","Granite","Basalt"],
    })

def test_locality_table_collapses_events():
    out=locality_table(sample())
    assert len(out)==2
    assert out.loc[out["Event"]=="A","observations"].iat[0]==2

def test_bounding_box():
    assert bounding_box(sample())==(10.0,50.0,12.0,51.0)
