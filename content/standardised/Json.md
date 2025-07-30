---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
Stands for [javascript object notation](https://www.json.org/json-en.html)
- records separated by commas
- keys & strings wrapped by double quotes
- good choice for data transport


JSON data embedded inside of a string, is an example of semi-structured data. The string contains all the information required to understand the structure of the data, but is still for the moment just a string -- it hasn't been structured yet. The Raw JSON stored by Airbyte during ELT is an example of semi-structured data. This looks as follows:  

|               |  **\_airbyte_data**|
|---------| -----------|
|Record 1| \"{'id': 1, 'name': 'Mary X'}\" |
|Record 2| \"{'id': 2, 'name': 'John D'}\"|

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
