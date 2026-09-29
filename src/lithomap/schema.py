"""Schema validation for the structural dataset."""
from __future__ import annotations
import pandas as pd

REQUIRED_COLUMNS = [
    "Event",
    "Latitude",
    "Longitude",
    "Rock",
    "Description (certain / probable / supposed...)",
    "Description (normal / inverted / dextral /...)",
    "Azim [deg] (azimuth of strike)",
    "Angle [deg] (dip angle of plane)",
    "Direction (dip direction)",
    "Angle [deg] (rake angle of striation)",
    "Direction (rake direction)",
]


def validate_schema(df: pd.DataFrame) -> None:
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_ranges(df: pd.DataFrame) -> None:
    checks = {
        "Latitude": (-90, 90),
        "Longitude": (-180, 180),
        "Azim [deg] (azimuth of strike)": (0, 360),
        "Angle [deg] (dip angle of plane)": (0, 90),
    }
    for column, (low, high) in checks.items():
        bad = df[column].dropna().between(low, high, inclusive="both")
        if not bad.all():
            raise ValueError(f"Out-of-range values detected in {column}")
