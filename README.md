# Lithology-Based Geospatial Analysis in Map

A reproducible Python project for analysing structural-geology observations from the central German platform. The workflow validates fault-slip records, standardizes structural orientation, derives lithology-aware features, and prepares publication-quality maps and diagnostics.

## Dataset
The analysis targets 1,207 structural observations collected at 93 outcrop localities. The source dataset is available from PANGAEA: **doi:10.1594/PANGAEA.893245**.

## Core questions
- How are lithology classes distributed spatially?
- How do fault kinematics vary by lithology and locality?
- What spatial patterns appear in strike, dip, rake, and fault type?
- How robust are interpretations to class imbalance and sampling density?

## Repository layout
```text
src/lithomap/      reusable analysis package
scripts/           command-line analysis stages
config/            reproducible configuration
data/              data acquisition notes
docs/              methodology and interpretation
notebooks/         exploratory workflow
assets/            generated visual outputs
tests/             automated checks
```

The project deliberately contains no student identity, student ID, course title, assessment instructions, or deadline metadata.
