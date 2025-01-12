Ruff is a fast [[Python]] linter and code formatter.

It is designed to enforce coding style and catch potential errors in Python code. 

Ruff aims to be efficient and comprehensive, supporting a wide range of linting rules and style checks. It can be used to automatically format code to adhere to a specified style guide, making it a useful tool for maintaining consistent code quality across a project.

## in [[TOML]]

have:

```toml
[tool.ruff.format]
# Like Black, use double quotes for strings.
quote-style = "double"
# Like Black, indent with spaces, rather than tabs.
indent-style = "space"
# Like Black, respect magic trailing commas.
skip-magic-trailing-comma = false
# Like Black, automatically detect the appropriate line ending.
line-ending = "auto"
```
