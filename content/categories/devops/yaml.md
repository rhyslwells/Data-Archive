---
aliases: []
category: DEVOPS
date modified: 27-09-2025
tags:
- software
---
Stands for [YAML ain't markup language](https://github.com/yaml/yaml-spec) and is a superset of JSON

- lists begin with a hyphen
- dependent on whitespace / indentation
- better suited for configuration than [[Json]]

YAML is a data serialization language often used to write configuration files. Depending on whom you ask, YAML stands for yet another markup language, or YAML isn’t markup language (a recursive acronym), which emphasizes that YAML is for data, not documents.


```YAML
---
# <- yaml supports comments, json does not
# did you know you can embed json in yaml?
# try uncommenting the next line
# { foo: 'bar' }

json:
  - rigid
  - better for data interchange
yaml:
  - slim and flexible
  - better for configuration
object:
  key: value
  array:
    - null_value: null
    - boolean: true
    - integer: 1
    - alias: aliases are like variables
    - alias: aliases are like variables
paragraph: |
  Blank lines denote
  paragraph breaks
content: |-
  Or we
  can auto
  convert line breaks
  to save space
alias:
  bar: baz
alias_reuse:
  bar: baz 
```