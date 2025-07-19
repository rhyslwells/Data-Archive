---
tags:
  - software
category:
---
Related to:
- Similar to [[Cron jobs ]]in [[Unix]]

Note:
- Running tasks every minute does not work.
### Using `schtasks` (Command-Line)

Windows provides `schtasks`, a command-line tool to schedule tasks.
## Example

In [[DE_Tools]] see: 
- DE_Tools/Explorations/Other/Scheduled-Tasks
- [[Registering a Scheduled Task]]
### Command to Create the Task:

Remember there may be different Python interpreters on the machine.

Running in cmd

```cmd
schtasks /create /tn "QuickTestTask" ^
    /tr "\"C:\Python312\python.exe\" \"C:\Users\RhysL\Desktop\DE_Tools\Explorations\Other\Scheduled-Tasks\example_task.py\"" ^
    /sc minute /mo 1 /f
```

 `/tn` – Task name: `"ExamplePythonTask"`
 `/tr` – Task run: runs Python with your script as an argument
 `/sc daily` – Schedule type
 `/st 07:30` – Start time
 `/f` – Force create if it already exists

> Note: Adjust `C:\Python\python.exe` to your actual Python path (`where python` can help identify it).

Or run using a [[bat]] file <- Better option.

Delete the Task When Done

```cmd
schtasks /delete /tn "QuickTestTask" /f
```

### To check a task

Add Logging to Your Python Script

This is the most reliable and script-controlled method.

Modify `example_task.py`:

```python
from datetime import datetime
import os

log_path = os.path.join(os.path.dirname(__file__), "task_log.txt")

with open(log_path, "a") as f:
    f.write(f"Task ran at: {datetime.now()}\n")
```

Every time the task runs, it appends a timestamp to `task_log.txt` in the same directory.

> Check the contents of `task_log.txt` to confirm it's being updated every minute.

2. Use Task Scheduler GUI (Manual Inspection)

3. Open Task Scheduler (`taskschd.msc`)
4. In the Task Scheduler Library, find `QuickTestTask`
5. Click on it and look at the "History" tab (if enabled)

    Look for events like "Task started" or "Action completed"

> If "History" is disabled, you can enable it:

 Right-click on the Task Scheduler Library
 Click "Enable All Tasks History"

6. Use Command Line to Check Last Run Time

```cmd
schtasks /query /tn "QuickTestTask" /v /fo LIST
```

Look for:

 Last Run Time – shows the most recent execution
 Last Result – `0` means success

Example output snippet:

```
TaskName:      \QuickTestTask
Last Run Time: 15/07/2025 12:15:00
Last Result:   0
```

## Test if It Works Without Waiting

To verify the task works **right now**:
```cmd
schtasks /run /tn "QuickTestTask"
```
This forces the task to run immediately
