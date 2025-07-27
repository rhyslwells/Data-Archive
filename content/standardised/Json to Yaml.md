---
aliases: []
category:
date modified: 27-07-2025
tags: []
title: 
---
[[Json]]

[[yaml]]

```JSON
{
  "json": [
    "rigid",
    "better for data interchange"
  ],
  "yaml": [
    "slim and flexible",
    "better for configuration"
  ],
  "object": {
    "key": "value",
    "array": [
      {
        "null_value": null
      },
      {
        "boolean": true
      },
      {
        "integer": 1
      },
      {
        "alias": "aliases are like variables"
      },
      {
        "alias": "aliases are like variables"
      }
    ]
  },
  "paragraph": "Blank lines denote\nparagraph breaks\n",
  "content": "Or we\ncan auto\nconvert line breaks\nto save space",
  "alias": {
    "bar": "baz"
  },
  "alias_reuse": {
    "bar": "baz"
  }
}
```

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