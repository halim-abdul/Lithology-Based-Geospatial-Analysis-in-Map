"""Right-hand-rule conversion utilities."""
from __future__ import annotations
import numpy as np
import pandas as pd

_DIP_AZIMUTH = {"N": 0.0, "E": 90.0, "S": 180.0, "W": 270.0}


def dip_direction_azimuth(direction: str) -> float:
    try:
        return _DIP_AZIMUTH[str(direction).upper()]
    except KeyError as exc:
        raise ValueError(f"Unsupported dip direction: {direction!r}") from exc


def strike_rhr(strike: float, dip_direction: str) -> float:
    """Return a strike azimuth consistent with the right-hand rule."""
    strike = float(strike) % 360.0
    target = dip_direction_azimuth(dip_direction)
    right_side = (strike + 90.0) % 360.0
    opposite = (strike + 270.0) % 360.0
    d_right = abs(((right_side - target + 180) % 360) - 180)
    d_opposite = abs(((opposite - target + 180) % 360) - 180)
    return strike if d_right <= d_opposite else (strike + 180.0) % 360.0


def add_rhr_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["strike_rhr_deg"] = [
        strike_rhr(s, d)
        for s, d in zip(
            out["Azim [deg] (azimuth of strike)"],
            out["Direction (dip direction)"],
        )
    ]
    out["strike_rhr_rad"] = np.deg2rad(out["strike_rhr_deg"])
    return out
