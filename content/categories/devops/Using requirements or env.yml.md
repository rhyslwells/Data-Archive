---
aliases: []
category: DEVOPS
date modified: 4-10-2025
tags:
  - software
---
## Using requirements or env.yml

This comes up often when moving between **Python projects managed with `pip`** and those managed with **Conda**. Let’s clarify:
### `requirements.txt`

* Standard in Python projects.
* Used by **pip**.
* Lists Python packages (and optionally versions).
* Example:

  ```txt
  numpy==1.26.0
  pandas>=2.0.0
  scikit-learn
  ```

Install with:

```bash
pip install -r requirements.txt
```

### `env.yml` (or `environment.yml`)

* Used by **Conda**.

* YAML format describing the full environment:

  * Python version
  * Conda channels
  * Conda packages
  * Pip dependencies

* Example:

  ```yaml
  name: myproject
  channels:
    - conda-forge
    - defaults
  dependencies:
    - python=3.11
    - numpy=1.26
    - pip
    - pip:
      - some_pip_only_package==0.3.1
  ```

Create environment from it:

```bash
conda env create -f env.yml
```

Update an existing environment:

```bash
conda env update -f env.yml --prune
```

Export an existing environment:

```bash
conda env export > env.yml
```

### Key differences

* **`requirements.txt`** → lightweight, only lists pip packages.
* **`env.yml`** → full specification of environment, includes Python version, Conda channels, and both Conda + pip packages.
### When to use

* Use `requirements.txt` if:
  * Project is pip/venv-based.
  * You want compatibility with tools like `pip install` or deployment on services that expect pip.

* Use `env.yml` if:
  * You want to reproduce a full Conda-managed environment (exact Python version, Conda dependencies).
  * You work in data science projects where binary compatibility matters (e.g., `numpy`, `pandas`, `pytorch`).