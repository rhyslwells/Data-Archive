---
aliases:
category:
date modified: 1-08-2025
tags:
  - python
  - frontend
  - visualization
---
Dash is an open-source framework for building interactive web applications using Python. 

It is particularly well-suited for [[Data Visualisation]] and dashboard creation. 

Dash integrates with popular libraries such as [[Plotly]], Pandas, and NumPy, making it ideal for creating dynamic and interactive visualizations.

Examples: 
- https://dash.gallery/Portal/?search=[ML]
- https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash

In [[ML_Tools]] see [[Clustering_Dashboard.py]]

Key Components of Dash
1. Dash App: The main application instance, created using `dash.Dash(__name__)`.
2. Dash HTML Components (`dash_html_components`): Provides wrappers for standard HTML elements (e.g., `html.Div`, `html.H1`).
3. Dash Core Components (`dash_core_components`): Includes interactive UI components like graphs, dropdowns, sliders, and more (e.g., `dcc.Graph`, `dcc.Dropdown`).
4. Callback Functions: Used to make components interactive by linking inputs (user actions) to outputs (changes in the UI).
5. [[Plotly]] Integration: Dash apps leverage Plotly for creating interactive visualizations.