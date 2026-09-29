"""Spatial aggregation helpers."""
from __future__ import annotations
import pandas as pd

def locality_table(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Event")
        .agg(
            latitude=("Latitude","first"),
            longitude=("Longitude","first"),
            observations=("Event","size"),
            dominant_lithology=("Rock",lambda x: x.mode().iat[0]),
        )
        .reset_index()
    )

def bounding_box(df: pd.DataFrame) -> tuple[float,float,float,float]:
    return (
        float(df["Longitude"].min()),
        float(df["Latitude"].min()),
        float(df["Longitude"].max()),
        float(df["Latitude"].max()),
    )
