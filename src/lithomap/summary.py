"""Descriptive summaries."""
from __future__ import annotations
import pandas as pd


def geographic_extent(df: pd.DataFrame) -> dict[str, float]:
    return {
        "north": float(df["Latitude"].max()),
        "south": float(df["Latitude"].min()),
        "east": float(df["Longitude"].max()),
        "west": float(df["Longitude"].min()),
    }


def category_summary(df: pd.DataFrame) -> dict:
    return {
        "rows": int(len(df)),
        "localities": int(df["Event"].nunique()),
        "lithology_counts": df["Rock"].value_counts().to_dict(),
        "fault_type_counts": df[
            "Description (normal / inverted / dextral /...)"
        ].value_counts().to_dict(),
    }


def lithology_fault_crosstab(df: pd.DataFrame) -> pd.DataFrame:
    return pd.crosstab(
        df["Rock"],
        df["Description (normal / inverted / dextral /...)"],
        normalize="index",
    )
