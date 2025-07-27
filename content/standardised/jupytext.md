---
aliases: []
category:
date modified: 27-07-2025
tags: [Research, software]
---

Jupytext is a tool that lets you convert between Jupyter Notebooks (`.ipynb`) and plain text formats like:

* Python scripts (`.py`)
* Markdown (`.md`)
* R (`.R`)
* Julia (`.jl`)

### What Can You Do with It?

* Edit notebooks in your favorite text editor (e.g., VS Code, Vim, Emacs)
* Version-control notebooks easily using Git (avoids messy JSON diffs)
* Convert `.py` ↔ `.ipynb`:

  * From script to notebook:
    ```bash
    jupytext --to notebook script.py
    ```
  * From notebook to script:
    ```bash
    jupytext --to py notebook.ipynb
    ```
* Pair `.ipynb` with `.py` so changes sync in both directions

### Bidirectional Sync ("Paired Notebooks")

You can keep a `.ipynb` notebook and a `.py` (or `.md`, etc.) file synced:
- Edit in Jupyter or in a text editor, and both formats stay up to date.
- Useful for version control (text diffs) while still running interactively in notebooks.
    

python
```
# Add this to the top of a Python script for pairing:
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
# ---
"""# This becomes a markdown cell in the notebook"""
```

Then run:

`jupytext --sync notebook.ipynb`