### Explanation:

- **BaseModel**: This is the base class for creating data models in Pydantic. You define your model by subclassing `BaseModel` and specifying fields with type annotations.
- **Optional**: Used to indicate that a field is optional.
- **List**: Used to specify a list of items, in this case, a list of strings for friends.
- **Validator**: A custom validator is used to enforce additional constraints, such as ensuring the age is positive.
- **ValidationError**: This exception is raised when the input data does not conform to the model's constraints.

This script demonstrates how Pydantic can be used to validate and parse data, ensuring it meets the specified types and constraints.



