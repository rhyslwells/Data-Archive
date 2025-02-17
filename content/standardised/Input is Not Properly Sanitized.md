---
tags: 
aliases: 
category: 
phase: 
topic: 
filename:
---
### Input is Not Properly Sanitized

When we say that =="input is not properly sanitized,"== it means that the input data from users or external sources is not being adequately checked or cleaned before being processed by the application. Proper sanitization involves validating and filtering input to ensure it is safe and expected, preventing malicious data from causing harm. Without proper sanitization, applications can be vulnerable to various attacks, such as:

- **Command Injection**: Malicious commands can be executed on the server.
- **SQL Injection**: Malicious SQL queries can be executed against a database.
- **Cross-Site Scripting (XSS)**: Malicious scripts can be injected into web pages.

Sanitization typically involves:
- Validating input against expected formats or values.
- Escaping special characters that could be interpreted as code.
- Removing or encoding potentially harmful content.