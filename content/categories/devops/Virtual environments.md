---
aliases: []
category: DEVOPS
date modified: 27-09-2025
tags:
- software
---
[Setting up virtual env](https://www.youtube.com/watch?v=yG9kmBQAtW4)

For windows (need to not be in a venv before del)
```cmd
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate
```

pip freeze > requirements.txt

.gitignore 
https://www.youtube.com/watch?v=_vejzukmn4s

Remember to set python interpreter

Related terms:
- [[Poetry]]

- [ ]  How to set up venv using poetry:

Now, instead of manually creating/activating `venv`:

`poetry install   # creates venv + installs deps poetry shell     # activates venv`

If you want to **recreate the environment** (equivalent to `rmdir /s /q venv && python -m venv venv`):

`poetry env remove python poetry install`


Other:
- [[Using requirements or env.yml]]