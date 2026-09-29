"""Generate structural-orientation diagnostics."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from lithomap.io import load_fault_slip

STRIKE="Azim [deg] (azimuth of strike)"
DIP="Angle [deg] (dip angle of plane)"
df=load_fault_slip(Path("data/raw/2018_Navabpour_Fault-slip.tab"))

angles=np.deg2rad(df[STRIKE].astype(float).to_numpy()%180)
bins=np.linspace(0,np.pi,19)
counts,_=np.histogram(angles,bins=bins)
centers=(bins[:-1]+bins[1:])/2
fig=plt.figure(figsize=(7,7))
ax=fig.add_subplot(111,projection="polar")
ax.bar(centers,counts,width=np.diff(bins),alpha=.75)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_title("Strike orientation rose diagram")
fig.tight_layout()
fig.savefig("outputs/strike_rose.png",dpi=180)
plt.close(fig)

fig,ax=plt.subplots(figsize=(8,5))
for rock,g in df.groupby("Rock"):
    ax.hist(g[DIP],bins=np.arange(0,95,5),histtype="step",linewidth=1.5,label=rock)
ax.set(xlabel="Dip angle (°)",ylabel="Frequency",title="Dip-angle distributions by lithology")
ax.legend(frameon=False,fontsize=8)
fig.tight_layout()
fig.savefig("outputs/dip_histogram.png",dpi=180)
plt.close(fig)
