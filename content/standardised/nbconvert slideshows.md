---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - documentation
  - communication
---
[[nbconvert]]

Examples:
- https://digitalhumanities.hkust.edu.hk/tutorials/turn-your-jupyter-notebook-into-interactive-presentation-slides-using-anaconda/
- https://nordicesmhub.github.io/NEGI-Abisko-2019/topics/report/presentation.html
- https://www.youtube.com/watch?v=EOpcxy0RA1A&ab_channel=JamesChurch

In [[DE_Tools]] see:
- Explorations\Other\Nbconvert

jupyter nbconvert main.ipynb --to slides --post serve

jupyter nbconvert presentation.ipynb --to slides --no-prompt --TagRemovePreprocessor.remove_input_tags={\"to_remove\"} --SlidesExporter.reveal_theme=sky

Use tags to remove cells.

Related: Better?
- https://github.com/damianavila/RISE

Use [[Reveal.js]]
- Open the notebook in **Jupyter Notebook** (not Lab).
- Go to `View > Cell Toolbar > Slideshow`
- Set each cell's `Slide Type` as described above. (search within vscode for switch slide type)

Other valid values for "slide_type":
"slide" — starts a new slide
"subslide" — nested slide
"fragment" — incremental appearance
"notes" — speaker notes
"skip" — cell excluded from presentation


![[Pasted image 20250726211647.png]]