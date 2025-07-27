---
aliases: []
category:
date modified: 27-07-2025
tags: [data_visualization]
---

## 1. Declarative vs. Procedural API

* [[Altair]] is declarative: you specify *what* you want (e.g. “plot *x* against *y* with color by group”) and Vega‑Lite handles *how* to draw it.
* Seaborn is procedural: you call functions (e.g. `sns.scatterplot`) and pass in data and styling arguments each time.

| Aspect            | Altair                                                | Seaborn                                            |
| ----------------- | ----------------------------------------------------- | -------------------------------------------------- |
| API style         | Declarative (chart grammar)                           | Procedural / function‑based                        |
| Underlying engine | Vega‑Lite (JSON specification + JavaScript rendering) | Matplotlib (static plotting)                       |
| Interactivity     | Built‑in (hover, zoom, selection)                     | Limited (requires extra work with `mpld3`, Bokeh…) |
| Output formats    | HTML/JSON (notebooks, web apps, dashboards)           | Static images (PNG, SVG, PDF)                      |
| Learning curve    | Moderate (chart grammar concepts)                     | Gentle (familiar Matplotlib semantics)             |

## 2. Interactivity and Web Embedding

* Altair charts are natively interactive and embed easily in Jupyter, Voila, or web apps.
* Seaborn produces static figures; interactivity must be layered on separately.

```python
# Altair example
import altair as alt, pandas as pd

df = pd.DataFrame({
    'height': [150, 160, 170, 180],
    'weight': [55, 60, 65, 75],
    'gender': ['F','F','M','M']
})

alt.Chart(df).mark_circle(size=100).encode(
    x='height',
    y='weight',
    color='gender'
).interactive()
```

```python
# Seaborn equivalent
import seaborn as sns
sns.scatterplot(data=df, x='height', y='weight', hue='gender')
```

## 3. Data Transformation and Pipelines

* Altair can perform aggregations, binning, and joins *within* the chart specification using the `$transform` pipeline.
* Seaborn expects you to preprocess data (e.g. with Pandas) before plotting.

## 4. Ecosystem Integration

* Altair integrates well with data‑streaming and dashboard tools (e.g. Streamlit, Panel).
* Seaborn sits atop Matplotlib and is ideal for quick exploratory plots and publication‑quality static figures.

### When to choose which?

| Scenario                                           | Altair                                     | Seaborn                   |
| -------------------------------------------------- | ------------------------------------------ | ------------------------- |
| Interactive dashboards                             | ✔︎                                         | ✘ (needs extra layers)    |
| Quick exploratory static plots                     | ✘ (requires more setup)                    | ✔︎                        |
| Complex data transformations within the chart spec | ✔︎                                         | ✘ (preprocess externally) |
| Embedding in web pages                             | ✔︎                                         | ✘                         |
| Publication‑quality static figures                 | ✘ (possible, but Matplotlib more flexible) | ✔︎                        |


