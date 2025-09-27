---
aliases: []
category: DEVOPS
date modified: 27-09-2025
tags:
- documentation
- python
- security
---
# Bandit: A Security Linter for Python

## Resources
- [Bandit Documentation](https://bandit.readthedocs.io/en/latest/)

## How to Use Bandit

Installation
To install Bandit, use pip by running the following command in your terminal:
```bash
pip install bandit
```
Running Bandit
After installation, you can run Bandit on your Python files or directories. For example, to scan a file named `example.py`, use:
```bash
bandit example.py
```
This command will analyze the file and report any security issues it finds.
### 3. Customizing Bandit
You can customize Bandit's behavior by specifying options. For example, to scan a directory and exclude certain subdirectories, use:

```bash
bandit -r example_directory -x example_directory/venv
```

- `-r` specifies the directory to scan.
- `-x` specifies directories to exclude.

### 4. Example Script
Here's a simple Python script that Bandit can analyze:

```python
import subprocess

user_input = input("Enter your name: ")
subprocess.call(["echo", user_input])
```

This script takes user input and passes it to the `echo` command using `subprocess.call()`. This can be dangerous as it might allow command injection.

To analyze the script, run:
```bash
bandit example.py
```
Bandit will generate a report highlighting potential security issues. For the script above, it might flag the use of `subprocess.call()` as a potential injection vector.

Fixing Issues
Based on Bandit's report, you can modify your code to fix vulnerabilities. For example, to mitigate the risk of command injection, you can set `shell=False`:

```python
import subprocess

user_input = input("Enter your name: ")
subprocess.call(f"echo {user_input}", shell=True)
```
Then rerun [[Bandit example output]]
## Example Script for Bandit Analysis

In [[ML_Tools]] see: [[Bandit_Example_Nonfixed.py]]

Features Demonstrated: [[Security Vulnerabilities]]
1. **Command Injection**: The `dangerous_subprocess` function uses `subprocess.call` with `shell=True`, which can lead to command injection if user input is not properly sanitized.
2. **Hardcoded Password**: The `hardcoded_password` function contains a hardcoded password, which is a common security issue.
3. **Use of `eval`**: The `unsafe_eval` function uses `eval`, which can execute arbitrary code if the input is not controlled.
4. **Insecure Deserialization**: The `insecure_deserialization` function uses `pickle.loads`, which can be exploited if untrusted data is deserialized.

### Running Bandit on the Example Script
To analyze this script with Bandit, save it as `example.py` and run:

```bash
bandit example.py
```
Bandit will generate a report highlighting the security issues in the script, providing insights into how each feature can be potentially exploited and suggesting ways to mitigate these risks.

By following these steps, you can use Bandit to identify and address security vulnerabilities in your Python code. Remember, while Bandit is a powerful tool, it's important to complement it with good coding practices and thorough security testing.