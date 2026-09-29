"""Cleaning and normalization routines."""
from __future__ import annotations
import pandas as pd


def normalize_strings(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for column in out.select_dtypes(include="object").columns:
        out[column] = out[column].map(lambda x: x.strip() if isinstance(x, str) else x)
    return out


def coerce_numeric(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    numeric_columns = [
        "Latitude",
        "Longitude",
        "Azim [deg] (azimuth of strike)",
        "Angle [deg] (dip angle of plane)",
        "Angle [deg] (rake angle of striation)",
    ]
    for column in numeric_columns:
        out[column] = pd.to_numeric(out[column], errors="coerce")
    return out


def drop_coordinate_gaps(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(subset=["Latitude", "Longitude"]).reset_index(drop=True)
