# Data

The raw structural-geology table is intentionally not duplicated in version control.

## Source
PANGAEA dataset DOI: **10.1594/PANGAEA.893245**

Expected local filename:
`data/raw/2018_Navabpour_Fault-slip.tab`

The table contains 1,207 observations from 93 localities, with coordinates, lithology, structural orientation, and fault-slip descriptors.

## Reproducibility
1. Download the tab-delimited dataset from the DOI landing page.
2. Save it at the expected local path.
3. Run `python scripts/01_validate_data.py`.
4. Run `python scripts/02_prepare_data.py`.

The original dataset citation and license conditions remain authoritative.
