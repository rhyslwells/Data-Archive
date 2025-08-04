---
aliases: []
category: 
date modified: 1-08-2025
tags: [documentation, software, tool]
---

`nbconvert` is a powerful command-line tool for converting Jupyter notebooks into other formats such as HTML, PDF, Markdown, LaTeX, slides, and more. It supports exporting, cleaning, and customizing output, making it ideal for documentation, presentations, and reporting.

## Typical Use Cases

### 1. Printing or Exporting Without Code

Useful for creating clean reports or meeting documents without code cells:

```bash
jupyter nbconvert stock_analysis.ipynb --no-input --to pdf
```

```bash
jupyter nbconvert phi_analysis.ipynb --to html --no-input --no-prompt
```

Alternatively, using the `TemplateExporter` class:

```bash
jupyter nbconvert Querying.ipynb --to html --TemplateExporter.exclude_input=True
```

See:
[Stack Overflow – Hide Code When Exporting](https://stackoverflow.com/questions/49907455/hide-code-when-exporting-jupyter-notebook-to-html)

### 2. Converting to Reveal.js Slides: [[Reveal.js]]

Turn a notebook into an interactive slideshow: See [[nbconvert slideshows]]

```bash
jupyter nbconvert notebook.ipynb --to slides --post serve
```

* Each cell becomes a slide (if marked with slide metadata).
* Opens a Reveal.js-based presentation in your browser.

To see possible themes see: https://revealjs.com/themes/

Best themes:
- serif
- 
## Additional Capabilities

| Format        | Command example            | Description                                      |
| ------------- | -------------------------- | ------------------------------------------------ |
| HTML          | `--to html`                | Default HTML export                              |
| PDF           | `--to pdf`                 | Export to print-friendly format (requires LaTeX) |
| Markdown      | `--to markdown`            | Convert for static blog/docs integration         |
| Python script | `--to script`              | Convert notebook to plain `.py` script           |
| LaTeX         | `--to latex`               | Generate LaTeX report for academic use           |
| Slides        | `--to slides --post serve` | Interactive Reveal.js presentation               |

## Common Options

| Option                                  | Purpose                                   |
| --------------------------------------- | ----------------------------------------- |
| `--no-input`                            | Hide code cells (inputs)                  |
| `--no-prompt`                           | Hide `In [ ]:` and `Out [ ]:` prompts     |
| `--clear-output`                        | Remove all outputs from the notebook      |
| `--output new_name`                     | Set a custom name for the output file     |
| `--TemplateExporter.exclude_input=True` | Template-based approach for hiding inputs |
