---
aliases: []
category:
date modified: 1-08-2025
tags: [code_snippet]
---
We connect ([link](https://github.com/rhyslwells/ML_Tools)) with the [[Data Archive]]

We have reorganised ML Tools (see github) so that the folder paths :

https://github.com/rhyslwells/ML_Tools/Explorations/{phase}/{topic}/{filename}.py

phase:
- [[Preprocessing|Preprocess]]
- [[Model Building|Build]]
- [[Model Selection|Selection]]
- [[Model Optimisation|Optimisation]]
- [[Model Deployment|Deployment]]
- [[Model Observability|Observability]]
- [[Utilities]]

topic: Dependant on the phase

filename: Final name of script. We tag files with .py with 
#### Notes

Using the [[0-note]] template we can get the paths for the associated files.

Use [[A YAML Generator]] to get a suggestion of what the YAML should be.

#### Dataview

https://github.com/rhyslwells/ML_Tools/blob/main/
+
Relative path with / correct way.

Full List:
```dataview
table
where contains(file.name, ".py")
```


