"""Publication-oriented visualization helpers."""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

FAULT_COL="Description (normal / inverted / dextral /...)"
DIP_COL="Angle [deg] (dip angle of plane)"
STRIKE_COL="Azim [deg] (azimuth of strike)"

def save_lithology_map(df: pd.DataFrame, path: str | Path) -> Path:
    fig, ax = plt.subplots(figsize=(8, 6))
    for rock, group in df.groupby("Rock"):
        ax.scatter(group["Longitude"], group["Latitude"], s=18, alpha=.65, label=rock)
    ax.set(xlabel="Longitude (°E)", ylabel="Latitude (°N)", title="Structural observations by lithology")
    ax.legend(frameon=False, fontsize=8, ncol=2)
    ax.grid(alpha=.25)
    fig.tight_layout()
    path=Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=180)
    plt.close(fig)
    return path

def save_fault_map(df: pd.DataFrame, path: str | Path) -> Path:
    fig, ax = plt.subplots(figsize=(8, 6))
    for label, group in df.groupby(FAULT_COL):
        ax.scatter(group["Longitude"], group["Latitude"], s=17, alpha=.6, label=label)
    ax.set(xlabel="Longitude (°E)", ylabel="Latitude (°N)", title="Fault-slip observations by kinematic class")
    ax.legend(frameon=False, fontsize=8, ncol=2)
    ax.grid(alpha=.25)
    fig.tight_layout()
    path=Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=180)
    plt.close(fig)
    return path
