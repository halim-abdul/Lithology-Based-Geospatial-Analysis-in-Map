# Analysis summary

This repository transforms a small one-line project description into a reproducible geospatial analysis package.

## Data profile
The source contains 1,207 structural observations from 93 outcrop localities across the central German platform. Coordinates span 50.3131–51.4955°N and 9.8600–12.0329°E.

## Lithology
Muschelkalk is the dominant class (1,013 observations), so raw all-data trends largely reflect this lithology. Granite contributes 117 observations; Buntsandstein, Zechstein, Basalt, and Rhyolite are much smaller groups.

## Kinematics
The recorded classes are normal, inverted, dextral, sinistral, extension, and pressure. Normal observations are most frequent (376), followed by inverted (296) and dextral (224).

## Research-grade safeguards
- Right-hand-rule normalization is explicit and tested.
- Sampling density is visualized separately from geological interpretation.
- Within-lithology normalized comparisons complement raw counts.
- Locality-level exports support spatial resampling and GIS workflows.
- The notebook and documentation are intentionally free of personal identity and course/assessment metadata.
