---
aliases: []
category: DEVOPS
date modified: 27-07-2025
tags:
- software
---
[[Data Security]] vulnerabilities can be encountered and mitigated in [[Devops Portal]].

Useful Tools
- [[tool.bandit]]
## Examples

### Command Injection

General Description: Command injection is a security vulnerability that occurs when an attacker is able to execute arbitrary commands on the host operating system via a vulnerable application. This typically happens when user input is improperly handled and passed to a system shell.

Example: 
The `dangerous_subprocess` function uses `subprocess.call` with `shell=True`, which can lead to command injection if user input is not properly sanitized.
  ```python
  import subprocess
  def dangerous_subprocess(user_input):
      subprocess.call(user_input, shell=True)
  ```
Mitigation:
  - Avoid using `subprocess.call` with `shell=True`. Use `subprocess.run` or `subprocess.call` with a list of arguments.
  - Validate and sanitize user inputs ([[Input is Not Properly Sanitized]]). 
### [[SQL Injection]]
### AI Injection Attacks

New class of attacks where malicious input is designed to manipulate or confuse AI/ML models.

Example:  
  - Input crafted to cause large language models to leak secrets or behave incorrectly.
  - Poisoning training data to introduce backdoors.

Defending AI requires:
- Input validation.
- Monitoring model behavior.
- Sanitizing training datasets.

### Hardcoded Password

General Description: Hardcoded passwords refer to credentials that are embedded directly in the source code. This practice is insecure as it exposes sensitive information and makes it difficult to change passwords without modifying the code.

Example:
The `hardcoded_password` function contains a hardcoded password, which is a common security issue.
  ```python
  def hardcoded_password():
      password = "123456"
      return password
  ```
  
Mitigation:
  - Use environment variables or configuration files to store sensitive information.
  - Consider using a secrets management tool.

### Use of `eval`

General Description: The `eval` function in Python evaluates a string as a Python expression. If not properly controlled, it can execute arbitrary code, leading to security vulnerabilities.

Example:
  - The `unsafe_eval` function uses `eval`, which can execute arbitrary code if the input is not controlled.
  ```python
  def unsafe_eval(user_input):
      return eval(user_input)
  ```
Mitigation:
  - Avoid using `eval`. Use safer alternatives like `ast.literal_eval`.
  - Ensure input is strictly controlled and sanitized.

### Insecure Deserialization

General Description: Insecure deserialization occurs when untrusted data is used to reconstruct objects. This can lead to arbitrary code execution, data tampering, or other malicious activities.

Example:
  - The `insecure_deserialization` function uses `pickle.loads`, which can be exploited if untrusted data is deserialized.
  ```python
  import pickle
  def insecure_deserialization(data):
      return pickle.loads(data)
  ```

Mitigation:
  - Avoid using `pickle` for untrusted data. Use safer formats like JSON ([[Why JSON is Better than Pickle for Untrusted Data]]).
  - Ensure data is from a trusted source.

### Cross-Site Scripting (XSS)

**General Description**: Cross-Site Scripting (XSS) is a security vulnerability that allows an attacker to inject malicious scripts into content from otherwise trusted websites. It occurs when an application includes untrusted data in a web page without proper validation or escaping.

**Example**:
- The `display_user_input` function directly inserts user input into HTML, which can lead to XSS if the input is not properly sanitized.
```html
<div>
	<%= user_input %>
</div>
```
**Mitigation**:
- Escape user input before rendering it in HTML.
- Use security libraries or frameworks that automatically handle escaping

