---
tags: 
aliases: 
category: 
phase: 
topic: 
filename:
---

Similar to [[Cron jobs ]]in [[Unix]]
### **Using `schtasks` (Command-Line)**

Windows provides `schtasks`, a command-line tool to schedule tasks.

#### **Example Commands**

- **Run a Python script every 5 minutes:**
    
    cmd
    
    CopyEdit
    
    `schtasks /create /tn "MyPythonScript" /tr "C:\Python\python.exe C:\path\to\script.py" /sc minute /mo 5 /f`
    
- **Run a batch file daily at 3 AM:**
    
    cmd
    
    CopyEdit
    
    `schtasks /create /tn "DailyBackup" /tr "C:\path\to\backup.bat" /sc daily /st 03:00 /f`
    
- **Delete a scheduled task:**
    
    cmd
    
    CopyEdit
    
    `schtasks /delete /tn "DailyBackup" /f`