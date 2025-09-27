---
aliases: []
category: DEVOPS
date modified: 27-09-2025
tags:
- software
---
### Note: Registering a Scheduled Task with a [[bat]] File

You can automate the creation of a [[Windows Scheduled Tasks]] using a `.bat` file. This is useful for reusability, portability, and documentation — especially when deploying or maintaining recurring tasks like data scripts.
#### Example: Create `register_quick_test.bat`

```bat
@echo off
set PYTHON_PATH=C:\Python\python.exe
set SCRIPT_PATH=C:\Users\RhysL\Desktop\DE_Tools\Explorations\Other\Scheduled-Tasks\example_task.py
set TASK_NAME=QuickTestTask

schtasks /create ^
 /tn "%TASK_NAME%" ^
 /tr "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" ^
 /sc minute /mo 1 ^
 /f

echo Task "%TASK_NAME%" registered to run every minute.
pause
```

#### What This Does:

 - Registers a task named `"QuickTestTask"`
 - Runs the Python script every 1 minute
 - Can be double-clicked to set up the task automatically
#### Why Use a `.bat` File:

 - Avoid manual typing of `schtasks` commands
 - Easily re-run or deploy task setup
 - Useful in shared, scripted, or version-controlled environments
