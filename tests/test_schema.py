import pandas as pd
import pytest
from lithomap.schema import validate_schema, validate_ranges, REQUIRED_COLUMNS

def frame():
    row={column: 0 for column in REQUIRED_COLUMNS}
    row["Event"]="X"
    row["Rock"]="Granite"
    row["Description (certain / probable / supposed...)"]="certain"
    row["Description (normal / inverted / dextral /...)"]="normal"
    row["Direction (dip direction)"]="E"
    row["Direction (rake direction)"]="N"
    row["Latitude"]=50.0
    row["Longitude"]=10.0
    row["Angle [deg] (dip angle of plane)"]=45
    return pd.DataFrame([row])

def test_schema_accepts_required_columns():
    validate_schema(frame())

def test_range_validation_rejects_bad_latitude():
    df=frame()
    df.loc[0,"Latitude"]=120
    with pytest.raises(ValueError):
        validate_ranges(df)
