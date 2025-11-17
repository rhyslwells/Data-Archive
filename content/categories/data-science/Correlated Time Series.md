---
aliases: []
category: DS
date modified: 5-10-2025
tags:
  - analysis
  - ml_process
  - statistics
  - time_series
---
To study the correlation among a ==group== of univariate time series, the goal is to understand how they co-move over time — whether their patterns are synchronous, lagged, or independent.

Correlation captures linear co-movement on a common timeline. For misaligned, nonlinear, or lagged dependencies, use DTW or cross-correlation instead.

Steps:

1. Align Time Frames – Resample or interpolate to ensure all series share a common time index.
   
2. [[Z-Normalisation]] or [[Standardisation]] – Convert each series to zero mean and unit variance to remove scale effects:
   
3. Optionally Detrend or Difference – Remove long-term trends or seasonality to focus on short-term co-movement.
   
4. Compute Correlations
   * Use `df.corr()` for standard Pearson correlations.
   * Compute rolling correlations to study how relationships change over time.
     
1. Visualize
   * [[Heatmap]] for pairwise correlation matrix.
   * Network graph or dendrogram for clustering similar series.
