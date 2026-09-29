"""Feature engineering for lithology and structural orientation."""
from __future__ import annotations
import numpy as np
import pandas as pd


def add_orientation_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    strike = np.deg2rad(out["strike_rhr_deg"].astype(float))
    dip = np.deg2rad(out["Angle [deg] (dip angle of plane)"].astype(float))
    out["strike_sin"] = np.sin(strike)
    out["strike_cos"] = np.cos(strike)
    out["dip_sin"] = np.sin(dip)
    out["dip_cos"] = np.cos(dip)
    out["is_steep"] = out["Angle [deg] (dip angle of plane)"].astype(float) >= 60
    return out


def add_frequency_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    rock_counts = out["Rock"].value_counts()
    event_counts = out["Event"].value_counts()
    out["lithology_frequency"] = out["Rock"].map(rock_counts)
    out["locality_frequency"] = out["Event"].map(event_counts)
    return out
