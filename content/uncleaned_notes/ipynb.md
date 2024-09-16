---
tags:
  - software
---


- [ ] What can you do in [[ipynb]]
	- [ ] slideshows? cell toolbar\slideshow
		- [ ] [Use rise to get presentations](https://www.youtube.com/watch?v=utNl9f3gqYQ&ab_channel=LiveLessons) Interactive
		- [ ] [Just the slides convert to slides](https://medium.com/@mjspeck/presenting-code-using-jupyter-notebook-slides-a8a3c3b59d67)
		- [ ] Tried installing rise but conflicts. DFN.
### Themes

Chesterish: Fav
oceans 16
onedork

grade 3 : Light theme

jt -l to list
```
jt -t <theme-name>
```

### [[ipynb]]
- [ ] You can convert juyter notebooks with nbconvert:: Incase you want to read some on kobo
	-  Multiple notebooks can be given at the command line in a couple of
	            different ways:

            %3E jupyter nbconvert notebook*.ipynb
             jupyter nbconvert notebook1.ipynb notebook2.ipynb
### Printing without code 

https://stackoverflow.com/questions/49907455/hide-code-when-exporting-jupyter-notebook-to-html

jupyter nbconvert stock_analysis.ipynb --no-input --to pdf

jupyter nbconvert --to html --no-input --no-prompt phi_analysis.ipynb

--clear -output

