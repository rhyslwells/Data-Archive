---
aliases: []
category:
date modified: 27-07-2025
tags: []
title: 
---
A **strongly typed** programming language is one where ==types== are strictly enforced. This means that once a variable is assigned a type, it cannot be implicitly converted to another type without an explicit conversion. The goal is to ==minimize errors related to incorrect type handling,== as the compiler or interpreter will detect type mismatches early in the development process.

### Characteristics of a Strongly Typed Language:
1. **Type Enforcement**: The language does not allow operations between incompatible types (e.g., trying to add a string to an integer).
2. **Explicit Conversions**: If you need to change the type of a variable, you must explicitly convert it (casting). The compiler or interpreter won't do it automatically.
3. **Compile-time/Runtime Type Checking**: The language performs thorough checks either at compile time (for compiled languages) or at runtime (for interpreted languages) to ensure type safety.

### Example: 

In [[Java]], which is a strongly typed language:
```java
int number = 5;
String text = "Hello";

// The following line will result in an error since you cannot add an integer to a string directly:
text = text + number;  // Type mismatch error

// You must explicitly convert the integer to a string to perform this operation:
text = text + Integer.toString(number);  // Correct
```
### Benefits:
- **Error Prevention**: Type mismatches are caught early, reducing runtime errors.
- **Code Clarity**: Since types are explicitly defined, it’s easier to understand what kind of data is being handled.
- **Efficiency**: Some strongly typed languages can optimize code better due to the predictability of data types.

### Contrast with Weakly Typed Languages:

Weakly typed languages, like [[JavaScript]], allow implicit type conversions, leading to more flexibility but also potential runtime errors due to unexpected conversions:
```javascript
let number = 5;
let text = "Hello";

// JavaScript allows this, and it implicitly converts the number to a string:
text = text + number;  // No error, result is "Hello5"
```
