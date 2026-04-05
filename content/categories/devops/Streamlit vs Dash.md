---
aliases: []
category: DEVOPS
date modified: 11-02-2026
tags:
  - dashboarding
  - python
  - visualisation
  - web_apps
  - deployment
---
#### 1. Core purpose

**Streamlit**
A framework for turning Python scripts into interactive apps with minimal structure. It is optimized for **rapid exploration and communication of results**.

**Dash**
A framework for building **declarative, callback-driven web applications** using Plotly components. It is optimized for **structured, production-style dashboards**.

---

#### 2. Execution model (most important difference)

##### Streamlit: script re-execution

* The app is a Python script.
* Any user interaction triggers a **top-to-bottom re-run** of the script.
* State must be explicitly preserved.

Mental model:

> A reactive notebook that re-executes on change.

Implication:

* Very low cognitive overhead.
* Care required for expensive computation and caching.

---

##### Dash: callback graph

* The app defines a layout plus a **directed graph of callbacks**.
* Only affected components are recomputed.
* State lives in component properties.

Mental model:

> A reactive UI with explicit dataflow.

Implication:

* More boilerplate.
* Stronger control over dependency and update behavior.

---

#### 3. State management

| Aspect            | Streamlit          | Dash                         |
| ----------------- | ------------------ | ---------------------------- |
| Default state     | Stateless          | Stateful                     |
| Persistence       | `st.session_state` | Component props, `dcc.Store` |
| Mental cost       | Low                | Medium                       |
| Explicit dataflow | Weak               | Strong                       |

In Streamlit, forgetting to manage state leads to recomputation.
In Dash, state is part of the design.

---

#### 4. Performance characteristics

**Streamlit**

* Re-runs entire script per interaction
* Caching via `st.cache_data`, `st.cache_resource`
* Best for light-to-moderate workloads

**Dash**

* Callback-level recomputation
* Better suited to complex dashboards with many inputs
* Scales more predictably with UI complexity

---

#### 5. Layout and UI control

**Streamlit**

* Linear, top-down layout
* Limited control over complex layouts
* Styling is constrained

**Dash**

* HTML/CSS-based layout model
* Full control over layout and responsiveness
* More work, more flexibility

---

#### 6. Typical use cases

| Use case              | Streamlit     | Dash     |
| --------------------- | ------------- | -------- |
| Data exploration      | Strong        | Moderate |
| Prototyping           | Strong        | Moderate |
| Research demos        | Strong        | Moderate |
| Production dashboards | Weak–moderate | Strong   |
| Complex interactivity | Weak          | Strong   |

---

#### 7. Developer experience trade-off

Streamlit optimizes for **speed of thought**.
Dash optimizes for **clarity of system structure**.

A useful heuristic:

* Use **Streamlit** when the app mirrors a notebook workflow.
* Use **Dash** when the app mirrors a front-end application.

#### 9. Summary table

| Dimension         | Streamlit       | Dash           |
| ----------------- | --------------- | -------------- |
| Programming model | Script re-run   | Callback graph |
| Learning curve    | Low             | Medium         |
| State handling    | Explicit add-on | First-class    |
| UI complexity     | Limited         | High           |
| Production fit    | Moderate        | Strong         |
