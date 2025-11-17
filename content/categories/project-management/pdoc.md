---
aliases:
  - 
category: PM
date modified: 27-09-2025
tags:
  - documentation
  - ML_Tools
  - architecture
---
## **pdoc Overview**

[pdoc](https://pdoc.dev/) is a lightweight and automatic documentation generator for Python projects. It converts your module’s **docstrings** into clean, modern **HTML** pages that can be viewed locally or hosted online.

### **Key Features**

* **Automatic Documentation:** Generates documentation directly from Python docstrings.
* **Markdown Support:** Allows Markdown formatting inside docstrings.
* **Customizable Output:** Offers configuration options for templates, themes, and output directories.
* **Easy Integration:** Can be integrated into build pipelines or run manually from the command line.
* **Modern Design:** Produces clean, readable, and navigable documentation.

## **Basic Usage**

### **1. Generate HTML documentation**

To document a file or package and save the output as HTML:

```bash
pdoc your_module_or_file.py --output-dir docs
```

This creates a `docs/` folder containing the generated documentation:

```
docs/
 ├── index.html
 └── your_module_or_file.html
```

### **2. Live Preview**

To preview documentation locally without saving files:

```bash
pdoc your_module_or_file.py
```

pdoc starts a local server (usually at `http://localhost:8080`) for interactive viewing.
## **Documenting a Directory**

To generate documentation for a local folder (e.g., `scripts`):

```bash
pdoc -o docs ./scripts
```

This command creates documentation for all Python files in `scripts/` and outputs them to `docs/`.

## **Next Steps**

1. **View Locally:** Open `docs/index.html` in your browser.
2. **Host Online:** Upload the `docs/` folder to a web server, [[GitHub Pages]], or [[Read the Docs]].
3. **Include in Repository:** Commit the `docs/` folder so collaborators can access it easily.
4. **Automate:** Add the `pdoc` command to your build or CI workflow.

### **Common Commands**

| Purpose         | Command                                                |
| --------------- | ------------------------------------------------------ |
| Generate HTML   | `pdoc your_module.py --output-dir docs`                |
| Force overwrite | `pdoc --html --force --output-dir docs your_module.py` |
| Live preview    | `pdoc your_module.py`                                  |
