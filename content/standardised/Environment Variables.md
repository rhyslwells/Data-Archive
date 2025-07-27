---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
Solution 1: Set Environment Variables Permanently (Recommended)
This ensures that environment variables persist across sessions.

On Windows (Permanent)
Open Control Panel → System → Advanced system settings → Environment Variables.

Under System Variables, click New.

Variable Name: PG_USER

Variable Value: postgres

Click New again.

Variable Name: PG_PASSWORD

Variable Value: your_password

Click OK and restart your computer.

Once restarted, Jupyter Notebook should be able to access the variables.