"""Generate lithology and fault-type count diagnostics."""
from pathlib import Path
import matplotlib.pyplot as plt
from lithomap.io import load_fault_slip

FAULT="Description (normal / inverted / dextral /...)"
df=load_fault_slip(Path("data/raw/2018_Navabpour_Fault-slip.tab"))

for column, name, title in [
    ("Rock","lithology_counts","Lithology class distribution"),
    (FAULT,"fault_counts","Fault-slip class distribution"),
]:
    fig,ax=plt.subplots(figsize=(8,5))
    df[column].value_counts().sort_values().plot.barh(ax=ax)
    ax.set(xlabel="Number of observations", title=title)
    ax.grid(axis="x", alpha=.25)
    fig.tight_layout()
    fig.savefig(f"outputs/{name}.png",dpi=180)
    plt.close(fig)
