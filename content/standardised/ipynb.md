---
tags:
  - software
---
### Printing without code : [[Documentation]]/ [[nbconvert]]

https://stackoverflow.com/questions/49907455/hide-code-when-exporting-jupyter-notebook-to-html

jupyter nbconvert stock_analysis.ipynb --no-input --to pdf

jupyter nbconvert --to html --no-input --no-prompt phi_analysis.ipynb

--clear -output

jupyter nbconvert --to html --TemplateExporter.exclude_input=True Querying.ipynb


