---
tags: 
category: 
---
Tool for converting [[ipynb]] files.

### Printing without code : [[Documentation & Meetings]]/ [[nbconvert]]

https://stackoverflow.com/questions/49907455/hide-code-when-exporting-jupyter-notebook-to-html

jupyter nbconvert stock_analysis.ipynb --no-input --to pdf

jupyter nbconvert --to html --no-input --no-prompt phi_analysis.ipynb

--clear -output

jupyter nbconvert --to html --TemplateExporter.exclude_input=True Querying.ipynb

### 2. Export using `nbconvert`

bash

Copy code

`jupyter nbconvert notebook.ipynb --to slides --post serve`

- This builds and serves the presentation locally in a browser.