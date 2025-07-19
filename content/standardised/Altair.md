---
tags:
  - data_visualization
category:
---
## What Is Altair?

Altair provides a [[declarative]] interface where you specify *what* you want to visualize (e.g. variables, encodings, transformations), and the library handles *how* to render it.

It is powered by Vega-Lite, a JavaScript-based visualization grammar, and outputs charts as HTML/[[JSON]] that can be embedded in Jupyter notebooks, web apps, and dashboards.

### Core principles:

* Declarative syntax: You describe *relationships* between data fields and visual properties (e.g. map `x` to time, `color` to category).
* Interactive by default: Charts can support hover, zoom, selection, etc.
* Data-aware: Built-in data transformations like aggregation, filtering, binning.
* Consistent and safe: Prevents many bad visualization practices by design (e.g., overplotting, misaligned axes).

## Why Use Altair?

### 1. Readable and Concise Code

Altair lets you build complex visuals with minimal syntax.

```python
import altair as alt
import pandas as pd

df = pd.read_csv('data.csv')

alt.Chart(df).mark_bar().encode(
    x='category:N',
    y='sales:Q',
    color='region:N'
)
```

You don’t need to specify chart layout, axes, or legends — Altair infers them.

### 2. Interactivity Built-in

With `.interactive()`, you can pan, zoom, and hover out-of-the-box — no extra code.

```python
alt.Chart(df).mark_circle().encode(
    x='x_val', y='y_val'
).interactive()
```

You can also create complex interactivity like brushing, linking, or filtering across charts.

### 3. Data Transformation Within the Chart

Altair supports:

* Filtering
* Aggregating
* Window functions
* Binning
* Calculated fields

You can express a lot of [[preprocessing]] without leaving the plotting context.

### 4. Best for:

* Exploratory data analysis ([[EDA]])
* Interactive data dashboards (e.g. with Streamlit, Voila, or Panel)
* Communicating insights with clean, web-ready charts

## When Not to Use Altair

* If you need fine-grained control over static plots for publication.
* If you're working with large datasets (>5000 rows by default; though workarounds exist).
* If you're deeply invested in Matplotlib or want full control over low-level rendering.

## Example Use-Cases

* [[Time series]] dashboards: Interactively explore metrics across time.
* Exploratory analysis: Quickly test variable relationships with scatter plots, box plots, etc.
* Teaching/Presenting: Embed responsive charts in web slides or notebooks.
* Data storytelling: Combine multiple linked views to guide a narrative.



