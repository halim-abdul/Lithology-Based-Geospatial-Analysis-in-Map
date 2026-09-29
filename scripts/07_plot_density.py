"""Visualize observation density without conflating it with geological abundance."""
from pathlib import Path
import matplotlib.pyplot as plt
from lithomap.io import load_fault_slip

df=load_fault_slip(Path("data/raw/2018_Navabpour_Fault-slip.tab"))
fig,ax=plt.subplots(figsize=(8,6))
hb=ax.hexbin(df["Longitude"],df["Latitude"],gridsize=35,mincnt=1)
fig.colorbar(hb,ax=ax,label="Observation count")
local=df.groupby("Event")[["Longitude","Latitude"]].first()
ax.scatter(local["Longitude"],local["Latitude"],s=8,alpha=.45)
ax.set(xlabel="Longitude (°E)",ylabel="Latitude (°N)",title="Sampling density and outcrop localities")
fig.tight_layout()
fig.savefig("outputs/sampling_density.png",dpi=180)
plt.close(fig)
