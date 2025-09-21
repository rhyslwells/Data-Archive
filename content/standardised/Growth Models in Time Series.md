### Logistic vs. Gompertz growth

Both are **S-shaped (sigmoid) growth curves**, often used to model adoption, population growth, or diffusion of innovations. They differ mainly in **where the inflection point (maximum growth rate) occurs**.

#### **Logistic Growth**

* Symmetric S-shape.
* Growth accelerates until halfway to saturation, then slows down.
* Formula:

  $$
  f(t) = \frac{K}{1 + \exp(-r (t - t_0))}
  $$

  * $K$ = carrying capacity (max customers)
  * $r$ = growth rate
  * $t_0$ = midpoint (inflection point, where growth is fastest)

#### **Gompertz Growth**

* Asymmetric S-shape.
* Inflection point occurs **earlier** than in the logistic curve.
* Growth slows sooner, which can better reflect **customer adoption curves** in real-world settings.
* Formula:

  $$
  f(t) = K \cdot \exp\big(-\exp(-r (t - t_0))\big)
  $$

  * $K$ = asymptotic maximum (saturation level)
  * $r$ = growth rate
  * $t_0$ = time at which growth rate is maximal

### Key Differences

* **Logistic:** Symmetric, assumes adoption accelerates until 50% of maximum.
* **Gompertz:** Skewed, assumes fastest growth happens **earlier** (common in customer/product growth where early adopters drive rapid initial uptake).

### Visual intuition

If you plotted them:

* Logistic = balanced "S" around the midpoint.
* Gompertz = “front-loaded” S, with rapid rise at the start and slower taper toward saturation.

### Why consider Gompertz for your case?

* Logistic might overestimate remaining growth (too symmetric), while Gompertz would more realistically taper earlier.

### Saturation Check

When you use **logistic** or **Gompertz** models, both assume that customer growth will eventually **plateau** at some maximum value $K$ (the **carrying capacity**).

A **saturation check** is simply a way of asking:

* **How close are we to that plateau already?**
* **At what time will growth essentially stop (reach, say, 90–95% of $K$)?**

### Why it matters

* **Business planning**: If you’re already close to saturation, forecasts should expect only small incremental growth.
* **Model choice**: If $K$ is unrealistically high compared to your market size, the logistic/Gompertz fit may not be appropriate.
* [[Energy Demand Forecasting]]/**Forecast horizon**: If you hit 95% saturation in 18 months, forecasting 5 years ahead isn’t meaningful.

### How to check saturation

#### 1. Define a threshold (e.g., 95% of $K$)

For the fitted curve Logistic/Gompertz above. We solve for $t$ where $f(t) = 0.95 , K$.

#### 2. Interpret the result

* If $t$ is **in the past** -> you’re already basically saturated.
* If $t$ is **within your 2-year forecast horizon** -> growth will flatten soon.
* If $t$ is **well beyond forecast horizon** -> you’re still in growth mode.
