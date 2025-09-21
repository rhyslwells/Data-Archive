### Trends in Time Series

This is the overall direction your data is moving in over time — going up, down or staying flat.  
Example: Steady decrease in monthly cigarette sales.

(long-term upward or downward movement)

* Differencing: Subtract the previous value from the current value:
  $$y'_t = y_t - y_{t-1}$$
  Removes linear trends. Can apply higher-order differencing if needed.
* Detrending with regression: Fit a line or curve to the data and use residuals.
* Transformation: [[Log transformation]] or square root to stabilize growth rates.

In [[Exponential Smoothing]] can add a dampening term to. Which applies a factor (0 < $\phi$< 1) that slows down the trend over time. Damping is useful to avoid overly optimistic or pessimistic forecasts. Without damping, trends extend linearly into the future, which can be unrealistic (e.g., unchecked growth). A damped trend gradually flattens, reflecting real-world limits (like market saturation). This is especially relevant for the customer growth series.