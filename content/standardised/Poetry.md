---
tags: 
aliases: 
category: 
phase: 
topic: 
filename:
---
Modern version of setting up dependencies instead of requirements.txt ([[dependency manager]])

Primary Purpose: Poetry is a [[dependency manager]] and packaging tool for Python projects.
    
Main Features:
    - Dependency management: Allows you to declare, install, and lock dependencies in the `pyproject.toml` file.
    - Package management: Can help package your Python project for distribution (e.g., publishing to PyPI).
    - Virtual environment management: Poetry automatically creates and manages a virtual environment for your project.
    - Version management: Ensures that all your project dependencies use compatible versions through its `poetry.lock` file, similar to `npm` or `yarn` in the JavaScript ecosystem.
    - Built-in publishing: Simplifies the process of publishing your Python package to PyPI.

Ideal Use Case:
    - If you need to manage dependencies for a Python project, create virtual environments, and ensure reproducibility (using `poetry.lock`).
    - If you're developing a Python package that you want to distribute or manage versions for, Poetry is a great choice.