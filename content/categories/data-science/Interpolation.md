---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- cleaning
- time_series
---
Interpolation is a method used to **estimate unknown values between known data points**. In data analysis, it is often applied when you have missing values in a dataset or want to generate smoother curves for visualization.

Formally, if you have data points $(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)$, interpolation constructs a function $f(x)$ such that $f(x_i) = y_i$ for all $i$, and then you can use $f(x)$ to estimate $y$ at values of $x$ that are not in the original data.

Interpolation is useful for **filling missing data, smoothing curves, and resampling** datasets, but one should avoid extrapolating too far beyond the known points, as it can be unreliable.


Common types of interpolation:

1. **Linear interpolation**: Connects two adjacent points with a straight line. Simple and fast.
   $y = y_1 + \frac{(x - x_1)(y_2 - y_1)}{x_2 - x_1}$

2. **Polynomial interpolation**: Fits a single polynomial through all points. Can be accurate for few points but unstable for many points.

3. **Spline interpolation**: Fits piecewise polynomials (usually cubic) between points, ensuring smoothness at joins. Often used in time series and graphics.

4. **Nearest-neighbor interpolation**: Assigns the value of the nearest known point. Simple but can produce jumps.

5. **Time-series specific methods**: Forward-fill, backward-fill, or more advanced methods like linear or spline interpolation along the time axis.
