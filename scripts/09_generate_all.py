"""Run the complete analysis pipeline in dependency order."""
import runpy
for script in [
    "scripts/01_validate_data.py",
    "scripts/02_prepare_data.py",
    "scripts/03_summary_stats.py",
    "scripts/04_plot_maps.py",
    "scripts/05_plot_distributions.py",
    "scripts/06_plot_orientation.py",
    "scripts/07_plot_density.py",
    "scripts/08_export_geojson.py",
]:
    print(f"==> {script}")
    runpy.run_path(script, run_name="__main__")
