"""Input/output helpers."""
from __future__ import annotations

from pathlib import Path
import pandas as pd


def load_fault_slip(path: str | Path, skiprows: int = 119) -> pd.DataFrame:
    """Load the PANGAEA tab-delimited fault-slip table."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. See data/README.md for acquisition instructions."
        )
    return pd.read_csv(path, sep="\t", skiprows=skiprows)


def save_processed(df: pd.DataFrame, path: str | Path) -> Path:
    """Write a processed table, creating parent directories if necessary."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path
