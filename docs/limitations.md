# Limitations and interpretation safeguards

1. **Sampling imbalance:** observation count is not equivalent to geological abundance.
2. **Spatial dependence:** measurements from the same locality are not independent spatial samples.
3. **Class imbalance:** Muschelkalk dominates the table, so aggregate patterns can be driven by one lithology.
4. **Orientation ambiguity:** source notation requires explicit handling of dip direction when enforcing right-hand-rule convention.
5. **Categorical semantics:** bedding and joint labels occur in the observation-status field and should not be treated as fault kinematics.
6. **Map projection:** longitude/latitude plots are appropriate for overview maps but metric distance analyses should use a projected CRS.
7. **Inference:** this repository emphasizes reproducible descriptive analysis; causal or paleostress reconstruction requires additional geological assumptions.
