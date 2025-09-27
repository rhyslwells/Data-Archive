---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- forecasting
---
## Autoregression

* **Definition**: A time series model that predicts the current value as a linear combination of its past values.
* **Mathematical form (AR(p))**:

  $$
  X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + \epsilon_t
  $$

  where $\epsilon_t$ is white noise.
* **Purpose**: Forecasting future values from historical dependencies.
* **Use cases**:
  * [[ARIMA]] modeling.
  * Capturing short-term dependencies.