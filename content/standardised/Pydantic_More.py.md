---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Utilities/Pydantic_More.py
### Key Features Demonstrated in the Script:

1. **Nested Models:** Use of the `Friend` model inside the `User` model.
2. **Custom Validators:** Validating `age` and `email` fields with specific logic.
3. **Dynamic Defaults:** Using `datetime.now` for `created_at`.
4. **Field Aliases:** Supporting different key names during parsing and serialization.
5. **Configuration Options:** Stripping whitespace and enabling strict typing.
6. **Model Inheritance:** Extending the `User` model to create an `AdminUser` model.
7. **Parsing Raw Data:** Demonstrating `parse_raw` for JSON strings.