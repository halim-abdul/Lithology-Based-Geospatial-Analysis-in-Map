import pandas as pd
from lithomap.summary import geographic_extent

def test_geographic_extent():
    df=pd.DataFrame({"Latitude":[50.0,51.0],"Longitude":[9.0,12.0]})
    assert geographic_extent(df)=={"north":51.0,"south":50.0,"east":12.0,"west":9.0}
