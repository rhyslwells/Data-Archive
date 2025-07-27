---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Utilities/Debugging.py

This script includes examples of logging, using breakpoints, and reproducing a simple bug for practice
### Key Concepts Demonstrated in the Script

1. **Logging in Python**: The script uses Python's logging module to record debug, info, error, and warning messages. This helps track the flow of execution and diagnose issues.

2. **Reproduce the Bug**: The script intentionally includes a division by zero bug to demonstrate how to identify and fix it.

3. **Breakpoints**: You can set a breakpoint in your IDE at the line where `result = divide_numbers(num1, num2)` to inspect the values of `num1` and `num2`.

4. **Automated Testing**: The script includes a simple assertion to test the `divide_numbers` function, ensuring it behaves as expected.

5. **Static Analysis**: The commented line `unused_variable = 42` can be used to simulate a static analysis warning for an unused variable.

