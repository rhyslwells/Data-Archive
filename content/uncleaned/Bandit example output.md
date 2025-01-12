## Complicated example output of bandit
Running bandit on [[ML_Tools]] file [[Bandit_Example_Nonfixed.py]] gives. Fixing this gives [[Bandit_Example_Fixed.py]]

```bandit
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.10.8
Run started:2025-01-11 17:19:41.806346

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.8.0/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: .\Bandit_Example.py:1:0
1       import subprocess
2       import os
3       import pickle

--------------------------------------------------
>> Issue: [B403:blacklist] Consider possible security implications associated with pickle module.
   Severity: Low   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.8.0/blacklists/blacklist_imports.html#b403-import-pickle
   Location: .\Bandit_Example.py:3:0
2       import os
3       import pickle
4

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.8.0/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: .\Bandit_Example.py:16:4
15          """
16          subprocess.call(f"cmd /c echo {user_input}", shell=True)
17

--------------------------------------------------
>> Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'SuperSecret123'
   Severity: Low   Confidence: Medium
   CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
   More Info: https://bandit.readthedocs.io/en/1.8.0/plugins/b105_hardcoded_password_string.html
   Location: .\Bandit_Example.py:28:15
27          """
28          password = "SuperSecret123"  # Example of hardcoded sensitive information
29          print(password)

--------------------------------------------------
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.8.0/blacklists/blacklist_calls.html#b307-eval
   Location: .\Bandit_Example.py:40:17
39          try:
40              result = eval(user_input)  # Evaluate the input
41              print(f"Result of eval: {result}")  # Print the result

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.8.0/blacklists/blacklist_calls.html#b301-pickle
   Location: .\Bandit_Example.py:53:11
52          """
53          return pickle.loads(data)  # If data is malicious, it can execute arbitrary code.
54

--------------------------------------------------

Code scanned:
        Total lines of code: 77
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 3
                Medium: 2
                High: 1
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 1
                High: 5
Files skipped (0):
```
## Simple example of bandit output
When i run bandit on the following code.

```python
import subprocess

user_input = input("Enter your name: ")
subprocess.call(f"echo {user_input}", shell=True)
```

it gives:

```
main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.10.8
Run started:2025-01-11 16:56:32.096644

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess motettetted with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.8.0/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: .\Bandit_ex1.py:1:0
1       import subprocess
2
3       user_input = input("Enter your name: ")

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.8.0/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: .\Bandit_ex1.py:4:0
3       user_input = input("Enter your name: ")
4       subprocess.call(f"echo {user_input}", shell=True)

--------------------------------------------------

Code scanned:
        Total lines of code: 3
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 1
                Medium: 0
                High: 1
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 2
Files skipped (0):
```